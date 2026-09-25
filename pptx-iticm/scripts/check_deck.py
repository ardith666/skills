#!/usr/bin/env python3
"""check_deck.py — pemeriksa mekanis deck PPTX ITICM (FAIL 0 untuk serah terima).

Usage:
    python3 check_deck.py pptx/P01-*.pptx [pptx/P02-*.pptx ...]
    python3 check_deck.py pptx/            # semua .pptx di folder

Bergantung python-pptx. Reference aturan: references/slide-rules.md
(section §8 untuk alur, §9 untuk kedalaman).

Exit code 1 bila ada FAIL. WARN tidak menggagalkan.
"""
import re
import sys
from pathlib import Path

try:
    from pptx import Presentation
    from pptx.enum.shapes import MSO_SHAPE_TYPE
    from pptx.util import Emu
except ImportError:
    sys.exit("python-pptx tidak terpasang. Jalankan: pip3 install python-pptx")

TARGET_W, TARGET_H = 12192000, 6858000  # 16:9 EMU

PLACEHOLDER_RE = re.compile(
    r"(?i)\b(text[ \t]*\d|label[ \t]*\d|title[ \t]*\d|lorem|xxx|yyy|placeholder|"
    r"source[ \t]*\d|sampeldata)\b"
)

AI_SMELL_WORDS = [
    "sangat", "luar biasa", "terbaik", "canggih", "mengoptimalkan",
    "memaksimalkan", "pentingnya", "menarik", "modern", "transformatif",
    "dapat disimpulkan", "tentunya", "perlu diingat", "secara keseluruhan",
    "di dunia nyata", "revolusioner", "menjanjikan",
]

SIZE_PREFIX_RE = re.compile(r"(?i)[Pp]\d{2}")

MAX_CARDS_PER_SLIDE = 3
THIN_SLIDE_MIN_CHARS = 60
AI_SMELL_WARN_THRESHOLD = 3
SIZE_TOLERANCE = 1000  # EMU

SKIP_THIN_SLIDES = ("Ringkasan", "Referensi", "Daftar", "Terima", "Closing")  # per judul slide
SKIP_NOTES_SLIDES = (
    "Ringkasan", "Referensi", "Daftar", "Tugas", "Terima", "Closing", "Studi Kasus",
)


def shape_texts(shape, out):
    """Kumpulkan teks dari shape, termasuk yang di dalam group."""
    if shape.shape_type == MSO_SHAPE_TYPE.GROUP:
        for s in shape.shapes:
            shape_texts(s, out)
    if getattr(shape, "has_text_frame", False) and shape.text_frame.text.strip():
        out.append(shape.text_frame.text)


def is_picture(shape):
    return shape.shape_type in (MSO_SHAPE_TYPE.PICTURE,)


def slide_body_text(slide):
    texts = []
    for shape in slide.shapes:
        if shape.has_text_frame and shape.text_frame.text.strip():
            is_title = (
                shape == slide.shapes.title
                if slide.shapes.title is not None
                else False
            )
            if not is_title:
                texts.append(shape.text_frame.text)
    return "\n".join(texts)


def count_rounded_rects(shape, counter):
    if shape.shape_type == MSO_SHAPE_TYPE.GROUP:
        for s in shape.shapes:
            count_rounded_rects(s, counter)
    if getattr(shape, "shape_type", None) == MSO_SHAPE_TYPE.AUTO_SHAPE:
        try:
            if shape.auto_shape_type in (2,):  # ROUNDED_RECTANGLE
                counter[0] += 1
        except Exception:
            pass


def check_file(path):
    fails, warns = [], []
    prs = Presentation(str(path))

    # --- ukuran (toleransi ±1px EMU; lihat slide-rules §1) ---
    if (
        abs(prs.slide_width - TARGET_W) > SIZE_TOLERANCE
        or abs(prs.slide_height - TARGET_H) > SIZE_TOLERANCE
    ):
        fails.append(
            f"Ukuran {prs.slide_width}x{prs.slide_height} bukan 16:9 "
            f"({TARGET_W}x{TARGET_H}) — §1"
        )

    n = len(prs.slides)
    is_exam = bool(SIZE_PREFIX_RE.search(path.name)) and any(
        t in path.name.lower() for t in ("uts", "uas")
    )
    if not is_exam and n < 15:
        warns.append(f"Hanya {n} slide (deck materi ≥20 direkomendasikan, §9)")

    # --- cek per slide ---
    for i, slide in enumerate(prs.slides):
        idx = i + 1
        title = None
        if slide.shapes.title is not None:
            title = slide.shapes.title.text or None

        # placeholder di seluruh teks (konten + catatan)
        alltext = []
        for shape in slide.shapes:
            shape_texts(shape, alltext)
        try:
            if slide.has_notes_slide:
                alltext.append(slide.notes_slide.notes_text_frame.text)
        except Exception:
            pass
        for m in PLACEHOLDER_RE.findall("\n".join(alltext)):
            fails.append(f"slide {idx}: placeholder terdeteksi '{m}' — §2.8/§8")

        # logo (gambar kecil di pojok kanan atas) pada slide non-title/closing
        if 1 < idx < n:
            for shape in slide.shapes:
                if is_picture(shape):
                    h = Emu(shape.height).emu if isinstance(shape.height, int) else 0
                    w = Emu(shape.width).emu if isinstance(shape.width, int) else 0
                    if h <= 1.3e6 and w <= 2.6e6 and shape.top is not None and shape.top < 1.5e6:
                        fails.append(f"slide {idx}: logo pada slide konten — §1")

        # kartu > 3 (heuristik, rounded rectangle)
        counter = [0]
        for sh in slide.shapes:
            count_rounded_rects(sh, counter)
        if counter[0] > MAX_CARDS_PER_SLIDE:
            warns.append(f"slide {idx}: {counter[0]} rounded cards (> {MAX_CARDS_PER_SLIDE}) — §4.1")

        # slide tipis (karakter sedikit, tanpa pengecualian)
        if 1 < idx < n and title and not any(k in title for k in SKIP_THIN_SLIDES):
            body = slide_body_text(slide)
            chars = len(re.sub(r"\s", "", body))
            if chars < THIN_SLIDE_MIN_CHARS:
                warns.append(
                    f"slide {idx}: kemungkinan tipis ({chars} karakter isi < {THIN_SLIDE_MIN_CHARS}) — §9.3"
                )

        # catatan kosong pada slide isi (kejar Ringkasan/Tugas/Referensi/Closing)
        if 1 < idx < n and title and not any(
            k in title for k in SKIP_NOTES_SLIDES
        ):
            try:
                notes = slide.notes_slide.notes_text_frame.text if slide.has_notes_slide else ""
            except Exception:
                notes = ""
            if not notes.strip():
                warns.append(f"slide {idx}: narasi speaker-notes kosong — §7.9")

        # jumlah kartu vs judul ber-"N fasa/tahap/langkah/bagian" (kuras skrip §2.9)
        if title:
            mm = re.search(r"(?i)(\d)\s*(fase|fasa|tahap|langkah|bagian|proses)", title)
            if mm:
                declared = int(mm.group(1))
                if counter[0] and counter[0] != declared:
                    warns.append(
                        f"slide {idx}: judul '{title}' menyebut {declared} tapi "
                        f"ada {counter[0]} kartu — §2.9"
                    )

    # --- kata AI-smell (dek keseluruhan) ---
    smell_hits = []
    for i in range(n):
        texts = []
        for shape in prs.slides[i].shapes:
            shape_texts(shape, texts)
        for w in AI_SMELL_WORDS:
            c = len(re.findall(re.escape(w), "\n".join(texts), re.IGNORECASE))
            if c:
                smell_hits.append((w, c))
    total_smell = sum(c for _, c in smell_hits)
    if total_smell >= AI_SMELL_WARN_THRESHOLD:
        by_word = {}
        for w, c in smell_hits:
            by_word[w] = by_word.get(w, 0) + c
        top = ", ".join(f"{w}×{c}" for w, c in sorted(by_word.items(), key=lambda x: -x[1])[:5])
        warns.append(f"kata AI-smell {total_smell}× ({top}) — §7.7")

    # --- judul slide 1 vs prefix nama file ---
    first_title = prs.slides[0].shapes.title
    if first_title is not None:
        first_title = first_title.text or ""
    fpre = SIZE_PREFIX_RE.search(path.name)
    tpre = SIZE_PREFIX_RE.search(first_title or "")
    if fpre and tpre and fpre.group(0).lower() != tpre.group(0).lower():
        warns.append(
            f"prefix file '{fpre.group(0)}' vs judul slide 1 '{tpre.group(0)}' berbeda"
        )

    return fails, warns, n


def main(argv):
    if not argv:
        sys.exit(__doc__)
    targets = []
    for a in argv:
        p = Path(a)
        if p.is_dir():
            targets.extend(sorted(p.glob("*.pptx")))
        else:
            targets.append(p)

    total_f = total_w = 0
    for t in targets:
        if not t.exists():
            print(f"[SKIP] {t}: tidak ada")
            continue
        try:
            fails, warns, n = check_file(t)
        except Exception as e:  # noqa: BLE001
            print(f"=== {t.name} ===")
            print(f"[ERROR] gagal dibuka: {e}")
            continue
        print(f"=== {t.name} ({n} slide) ===")
        for f in fails:
            print(f"  [FAIL] {f}")
        for w in warns:
            print(f"  [WARN] {w}")
        print(f"  -> FAIL {len(fails)} · WARN {len(warns)}")
        total_f += len(fails)
        total_w += len(warns)

    print(f"\nTotal: FAIL {total_f} · WARN {total_w}")
    if total_f:
        sys.exit(1)


if __name__ == "__main__":
    main(sys.argv[1:])