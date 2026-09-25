---
name: "Powerpoint / PPTX ITICM"
slug: pptx-iticm
version: 4.1.0
description: "Branded PowerPoint generator untuk ITICM — dark theme, OBE-based. Logo, nama dosen, tugas, code snippet, diagram."
---

# PPTX ITICM (Dark Theme, OBE)

Branded PowerPoint generator untuk ITICM. Dark navy + orange accent + Calibri. RPS berbasis OBE — tiap presentasi wajib ada tugas.

> **CANON ATURAN: `references/slide-rules.md`** — bacakan SEKALI penuh sebelum
> generate apa pun (aturan di SKILL.md ini ringkasan; slide-rules menang bila
> bertentangan). Setelah generate, jalankan `scripts/check_deck.py` (FAIL 0) dan
> fresh-eyes review (`references/content-review-prompt.md`).

## Trigger

Gunakan saat: buat/generate presentasi `.pptx` kuliah ITICM, matakuliah, keperluan kampus.

## Brand Tokens

| Token | Nilai | Keterangan |
|---|---|---|
| `DARK_BG` | `#1a1a2e` | Dark navy — bg title/closing/summary |
| `ACCENT` | `#e86c00` | Oranye — accent, badge, underline |
| `LIGHT_GRAY` | `#f5f5f5` | Bg slide konten |
| `DARK_TEXT` | `#1a1a2e` | Text di atas light bg |
| `WHITE` | `#ffffff` | Text di atas dark bg |
| `MUTED` | `#6b7080` | Subtitle, note |
| `CODE_BG` | `#2d2d3a` | Bg code card |
| `CODE_LIGHT` | `#c0c5d0` | Warna teks kode (Consolas) |
| `TASK_BG` | `#25253a` | Bg tugas card |
| `CARD_BORDER` | `#e0e0e0` | Border kartu 1pt |
| `ROUND_ADJ` | `0.167` | Radius kartu rounded |
| Font | Calibri | Semua slide |
| Code Font | Consolas | Code snippet |
| Logo | 1.0×1.0" | Kanan atas, HANYA title + closing |
| Label | `iticm.ac.id` | Kiri bawah semua slide (warna adaptif) |
| Nama | `Ardiyan NP S.Kom, M.Kom` | Kiri bawah (title slide only) |

## Urutan Slide Standar (OBE)

```
1. Title         → judul + nama dosen (logo)
2. Definisi      → add_split_slide (definisi + analogi + badge)
3. Konsep        → add_cards_slide 2-3 kartu (pecah 6 item jadi 2 slide)
4. Aturan        → add_list_slide 3 kartu bernomor (pecah bila > 3)
5. Langkah       → add_steps_slide 3 kartu angka (pecah bila > 3)
6. Pendalaman    → add_explain_slide (rinci + tips)
7. Contoh 1-2    → add_steps_code_slide (langkah + panel kode)
8. Diagram       → add_diagram_slide PNG (opsional, wajib bila bahas flowchart)
9. Code          → add_code_slide (opsional)
10. Contoh Tugas → add_example_task_slide (1-2 soal + jawaban)
11. Tugas OBE    → add_task_slide (Tipe A latihan / Tipe B resmi)
12. Ringkasan    → add_summary_slide
13. Referensi    → add_references_slide
14. Closing      → terima kasih (logo)
```

Contoh + tugas (10-11) wajib. Diagram wajib bila materi membahas flowchart/sequence.

**Isi tiap slot mengikuti kesepakatan stack/pendekatan di knowledge/** (lihat "Filosofi konten" di bawah) — mis. course implementasi web memakai pola request → engine → response.

## Target Kedalaman (berbasis DATA — tanpa batas atas slide)

Kedalaman diukur dari isi, bukan jumlah slide (slide-rules §9). **TIDAK ada batas atas**:
deck materi biasanya ≥20 slide dan boleh 25–35+ bila materi kaya data. Yang dilarang adalah
menambah slide untuk menipiskan topik.

**Kerangka inti wajib (minimal — boleh plus):**

```
1 Title · 2 Split (definisi+analogi) · 3-4 Cards (1/2, 2/2)
5-6 List (1/2, 2/2) · 7-8 Steps (1/2, 2/2)
9 Explain A (pendalaman konsep) · 10 Explain B (jebakan + praktik)
11-13 Contoh (3× steps+code) · 14 Diagram · 15 Code 1 · 16 Code 2 (varian)
17 Contoh soal · 18 Tugas (+B bila milestone) · 19 Ringkasan · 20 Referensi · 21 Closing
```

**Lapisan data (perluas DI SINI, bukan menambah bullet saja):**
- Tiap slide konten wajib memuat minimal satu unsur data: tabel, angka konkret berunit,
  dataset, contoh perhitungan bertahap, kode + output dijalankan, kasus nyata, atau
  perbandingan multi-dimensi. Slide yang cuma 1–2 bullet singkat tanpa data = slide "tipis" =
  pelanggaran (check_deck memberi WARN, slide-rules §9.3).
- Perluas satu topik dengan membuka dimensi: definisi → mekanisme → contoh angka →
  studi kasus perhitungan manual → implementasi kode + output → analisis hasil → latihan.
  Setiap dimensi boleh 1+ slide, masing-masing berbahan data nyata.
- Deck algoritma: WAJIB slide "Studi Kasus: Perhitungan Manual" (trace angka langkah
  demi-langkah: tabel, jarak, voting, SSE, cost) SEBELUM Code 1. Slide ini wajib ada angka
  yang bisa diikuti mahasiswa dari nol (contoh: A* cost = 4, akurasi 93.3%, SSE 0.76).

Deck ujian (UTS/UAS) boleh ramping (±8-12 slide, tanpa tugas baru) — pembebasan dari aturan
kedalaman, tapi struktur/judul tetap ikut slide-rules.

## Layout Rules (V3 — gaya referensi terukur)

- Judul konten: teks gelap 36pt + garis orange — TANPA header bar navy.
- Semua kartu: `ROUNDED_RECTANGLE` adjust 0.167, border `#e0e0e0` 1pt; badge = lingkaran orange + emoji/angka putih.
- Maks 3 kartu per slide. Materi 6 item selalu dipecah 2 slide (1/2, 2/2).
- Logo hanya title + closing. Slide konten hanya label `iticm.ac.id`.
- Kode: Consolas, panel gelap rounded, teks `#c0c5d0`.
- Rincian tiap konsep dapat slide pendalaman (`add_explain_slide`: 2-3 kalimat + tips 💡).

## Penamaan Deck (standar konsisten — audit 2026-09-19)

Format kebab lowercase, satu konvensi untuk semua MK (lihat skill `mk-iticm` → Konvensi Penamaan / standarisasi-struktur-mk di vault Obsidian):

- `p00-pengantar-kontrak-kuliah.pptx`, `p01-konsep-dasar-….pptx`, `p08-uts.pptx`, `p16-uas.pptx`
- DILARANG: `P00_Pengantar_…`, `P01-Konsep-Dasar-…` (campuran casing/underscore)
- Setiap deck WAJIB punya export PDF di `pptx/pdf/` dengan nama sama (audit fase 5: nama PDF == nama deck).

## Workflow

### WAJIB: Diskusi → Knowledge → Draft → Generate (sebelum buat pptx)

**JANGAN pernah langsung generate `.pptx`.** Alur wajib (sudah disepakati user):

```
[0] RPS → knowledge/ (extraction: CPMK, meeting map, bobot, referensi utk draft)
[1] WAJIB DISKUSI dengan user sebelum menulis draft:
    - bahasa pemrograman / stack yang dipakai (bila materi butuh, mis. PHP, Python,
      JS, Java, atau tanpa bahasa)
    - pendekatan penyampaian (teori murni / implementasi nyata / hybrid)
    - Ini TIDAK boleh diasumsikan dari skill — tiap course beda keputusan.
[2] Catat hasil kesepakatan ke knowledge/ (KNOWLEDGE.md section: "Panduan Generate
    Draft"), termasuk stack & pola implementasi. Ini jadi acuan saat bikin draft.
[3] Buat SATU file draft: pptx/draft/draft-pertemuan.md
    - 17 deck (P00 = pengantar/kontrak-kuliah, P01–P16 = pertemuan)
    - Filename target pakai prefix konsisten: pXX-slug lowercase (contoh: p01-pengenalan-ai.pptx, p00-pengantar-kontrak-kuliah.pptx)
    - Isi mengikuti kesepakatan di knowledge/ (stack + pendekatan)
[4] Setiap slide konten (2..sebelum Ringkasan/Tugas) WAJIB punya:
    - Heading `### Slide N — <Judul slot>` (Title/Cards/List/Steps/Explain/Contoh/Diagram/Code/Contoh Soal)
    - Baris `> **Narasi:** <paragraf 3-4 kalimat>` — narasi PANJANG menjelaskan
      isi materi slide tsb, biar belajar lebih mudah (bukan label pendek)
    - Body: konten slide (bullets/tabel/kode) sesuai slot V3
[5] USER REVIEW draft → diskusi → revisi sampai final
[6] Generate file .pptx dari draft (pakai iticm_base V3)
[7] Verify:
    - `python3 scripts/check_deck.py pptx/Pxx-*.pptx` → **FAIL 0** + baca semua WARN
    - Daftar judul dibaca berurutan → satu cerita (slide-rules §2.6)
    - fresh-eyes review via references/content-review-prompt.md → tabel terima/tolak → perbaiki
[8] Multi-agent untuk komponen lain
```

**Stack & pendekatan TIDAK hardcoded.** Contoh keputusan yang pernah disepakati
(course AI, web-implementation): PHP + MySQL (Laragon), tiap deck membangun 1 class
+ 1 endpoint, struktur `public/ api/ class/ data/ config.php`. Course lain bisa
memilih Python, JS, atau tanpa bahasa — yang penting DIDISKUSIKAN dulu dan dicatat
di knowledge/.

**Filosofi konten: ikuti kesepakatan di knowledge/ (mis. implementasi web).** Bila course disepakati berbasis implementasi (contoh: AI via web), tiap deck membangun **1 class/modul + 1 endpoint/service** (mesin + service). Konsep dijelaskan ringkas lalu langsung ke implementasi. Struktur file mengikuti stack yang dicatat di knowledge/. Contoh yang pernah dipakai (course AI, PHP web):

**Peta class + endpoint per topik (CONTOH — PHP; ganti sesuai stack di knowledge):**

| Topik | Class (PHP) | Endpoint | Algoritma |
|---|---|---|---|
| Struktur web | `config.php` | `api/status.php` | — |
| Agen | `ReflexAgent.php` | `api/agent.php` | simple reflex |
| Klasifikasi masalah | `ProblemClassifier.php` | `api/classify.php` | decision |
| Logika proposisi | `TruthTable.php` | `api/truthtable.php` | 2ⁿ tabel |
| Representasi pengetahuan | `RuleEngine.php` | `api/diagnosa.php` | forward chaining |
| Pencarian heuristik | `Heuristic.php` | `api/search.php` | Greedy vs A* |
| A* pathfinder | `AStar.php` | `api/rute.php` | A* search |
| KNN klasifikasi | `KNN.php` | `api/klasifikasi.php` | KNN |
| Evaluasi model | `Evaluator.php` | `api/evaluasi.php` | confusion matrix |
| Clustering konsep | `KMeans.php` | `api/cluster.php` | K-Means |
| Clustering + SSE | `KMeans.php` + `sse()` | `api/cluster.php` | K-Means++ , elbow |
| Implementasi aplikasi | `Chatbot.php` dll | `api/chat.php` | integrasi |
| Pengujian | `AppTester.php` | smoke test | unit/integration |

**Pergeseran isi tiap slot (bila kesepakatan = implementasi nyata):**
- **Split (slide 2):** definisi + analogi konteks penerapan (request → proses → response bila web).
- **Cards/List:** arsitektur atau komponen nyata (layer/file modul), bukan daftar konsep saja.
- **Explain A/B:** "kenapa penting di praktik" + tips debugging (ada di stack: curl/error log/var_dump/pdb/console).
- **Contoh 1–3:** langkah buat modul → service/endpoint → coba di runtime/browser.
- **Diagram (slide 14):** flowchart alur nyata (request → engine → response), bukan cuma algoritma.
- **Code 1/2 (15/16):** Code 1 = modul/engine, Code 2 = service/endpoint/variasi.
- **Contoh Soal (17):** soal implementasi (debug kode, baca output, bedakan input/output).
- **Tugas (18):** bangun fitur nyata sesuai stack (modul + service + bukti output).

Untuk course teori murni (tanpa bahasa), slot-slot di atas kembali ke penjelasan konsep biasa — keputusan ada di knowledge/.

**Footprint = narasi panjang**, bukan label pendek. Contoh yang diterima user:

```markdown
### Slide 5 — List 1/2 (Poin Penting)
> **Narasi:** Slide ini menjelaskan tiga poin penting terkait perangkat dan evaluasi. Pertama, seluruh
> praktikum dikerjakan dengan PHP dan MySQL melalui Laragon. Kedua, komposisi penilaian mulai
> ditampilkan: kehadiran 17%, UTS 20%, dan UAS 23%. Ketiga, ada tiga tugas mandiri sebesar 9%
> masing-masing ditambah proyek akhir 13%. Pesan yang perlu diingat: nilai akhir bukan berasal dari
> satu ujian saja, tetapi akumulasi dari kehadiran, tugas, dan proyek sepanjang semester.
1. **Alat:** PHP + MySQL (Laragon) — semua pratikum dikerjakan dengan PHP.
```

**Struktur draft per deck:**

```markdown
## P01 — <Judul Pertemuan>

**File:** `p01-nama-slug.pptx`
**Sub-CPMK:** Sub-CPMKx | **Bobot:** x% | **Tipe:** Kuliah/Praktikum

### Slide 1 — Title
...
### Slide 2 — Definisi & Analogi (Split)
> **Narasi:** ...
...
### Slide 21 — Closing
```

Generate script: `python3 /tmp/gen_v3_decks.py` (referensi eksekusi di sibling course / prior session). Simpan hasil ke folder `pptx/` sesuai `**File:**` di tiap deck.

## Quick Start (Generate Script)

```python
import sys
sys.path.insert(0, "/Users/ardith666/.agents/skills/pptx-iticm/templates")
from iticm_base import *

prs = create_presentation()
add_title_slide(prs, "Judul", "Subjudul")
add_split_slide(prs, "Apa itu X?", "Definisi", "Penjelasan definisi.",
                "Analogi", "Penjelasan analogi.", ["📐 Logis", "📋 Urut"])
add_cards_slide(prs, "Karakteristik", [("📥", "Input", "Data masuk.")])
add_steps_slide(prs, "Langkah", [("Siapkan", "Siapkan bahan.")])
add_steps_code_slide(prs, "Contoh", "Sub", ["Langkah 1"], "PHP", "echo 1;")
add_diagram_slide(prs, "Alur", "/path/to/diagram.png", "Sumber: draw.io")
add_code_slide(prs, "Pseudocode", "IF x > 0 THEN\n  cetak('positif')\nENDIF")
add_example_task_slide(prs, "Contoh Pengerjaan", [
    {"question": "Apa itu algoritma?", "answer": "Langkah sistematis menyelesaikan masalah"}
])
add_task_slide(prs, "Tugas 1", "Buat algoritma belanja online.", "10%")
add_summary_slide(prs, "Ringkasan", ["Poin 1", "Poin 2"])
add_references_slide(prs, ["Kadir, A. (2018). ..."])
add_closing_slide(prs, "Terima Kasih")
prs.save("output.pptx")
```

## Helper Functions

- `create_presentation()` → 16:9
- `add_title_slide(prs, title, subtitle)` → dark bg + nama + logo
- `add_content_slide(prs, title, items)` → fallback bullet ringan (light style)
- `add_two_column_slide(prs, title, left, right, ...)` → dua kolom (light style)
- `add_split_slide(prs, title, def_h, def_d, ana_h, ana_d, badges)` → definisi + analogi + panel badge
- `add_cards_slide(prs, title, cards, subtitle)` → kartu ikon, 2-3 per slide
- `add_list_slide(prs, title, items, start, subtitle)` → kartu bernomor, maks 3
- `add_steps_slide(prs, title, steps, start, subtitle)` → kartu angka besar, maks 3
- `add_steps_code_slide(prs, title, subtitle, steps, code_title, code)` → langkah + panel kode
- `add_explain_slide(prs, title, body, tip)` → pendalaman + tips
- `add_diagram_slide(prs, title, image_path, caption, subtitle)` → insert PNG (fit 9.5×4.6")
- `add_code_slide(prs, title, code, lang)` → panel kode Consolas `#c0c5d0`
- `add_example_task_slide(prs, title, examples)` → 2 contoh + jawaban (green bar)
- `add_task_slide(prs, title, description, weight)` → tugas OBE (rounded card)
- `add_summary_slide(prs, title, points)` → ringkasan dark
- `add_references_slide(prs, references)` → referensi light
- `add_closing_slide(prs, text)` → closing + logo

## Diagram (Flowchart/Sequence)

Pipeline: generate PNG → `add_diagram_slide()`

1. **draw.io** — gambar di app.diagrams.net → File > Export as > PNG (simpan juga `.drawio` sebagai sumber)
2. **Mermaid** — tulis `.mmd` → `mmdc -i input.mmd -o output.png`
3. **PIL fallback** — gaya ITICM bila tool di atas tak ada: oval navy, proses putih, diamond orange, panah navy + label Ya/Tidak

Kuliah flowchart: draw.io wajib. Lainnya: mermaid cukup.

## Tugas OBE

- **Contoh** (`add_example_task_slide`): 1-2 soal + jawaban sebelum tugas
- **Tugas** (`add_task_slide`): judul, deskripsi, bobot (opsional)
- WAJIB sesuai tema/kompetensi

## Rules

- WAJIB baca `references/slide-rules.md` penuh sebelum generate (canon; menang bila bertentangan dgn SKILL.md)
- WAJIB jalankan `scripts/check_deck.py` → FAIL 0 sebelum serah terima; WARN dibaca & dievaluasi
- WAJIB fresh-eyes review (`references/content-review-prompt.md`) → tabel terima/tolak; 1 rally lalu tanya user
- WAJIB diskusi + catat stack/pendekatan di knowledge/ sebelum draft (bukan asumsi skill)
- WAJIB draft berdasarkan knowledge → user review final → baru generate
- WAJIB narasi panjang (> 3 kalimat) per slide konten — bukan label pendek
- WAJIB pakai helper functions
- WAJIB deck materi berisi data nyata per slide (tabel/angka/dataset/contoh/output) — tanpa batas atas slide; slide "tipis" = pelanggaran (slide-rules §9)
- WAJIB ada tugas OBE (minimal 1 slide)
- Sebelum tugas: kasih contoh pengerjaan
- Maks 3 kartu per slide — pecah materi panjang
- Logo hanya title + closing
- Code: Consolas `#c0c5d0`, panel gelap rounded
- Diagram flowchart wajib ada bila materi membahas flowchart
- Label warna adaptif (putih di dark, gelap di light)

## File Structure

```
pptx-iticm/
├── SKILL.md
├── references/
│   ├── slide-rules.md          # CANON aturan (bacakan tiap generate; tumbuh dari review)
│   └── content-review-prompt.md# fresh-eyes review
├── scripts/
│   └── check_deck.py           # pemeriksa mekanis PPTX → FAIL 0
├── templates/
│   └── iticm_base.py
└── assets/
    └── logo_iticm.png
```

## Dependencies

- `python-pptx`
- `mermaid-cli` (npm) — untuk diagram (opsional bila draw.io/PIL)
- Font Calibri + Consolas

## Related

- [[powerpoint-pptx]] — methodology PPTX umum
