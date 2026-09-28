# Wiki Pattern (karpathy-obsidian-vault)

Schema knowledge untuk SEMUA skill. Adapted dari [joshpocock/karpathy-obsidian-vault](https://github.com/joshpocock/karpathy-obsidian-vault) (pola wiki Karpathy, implementasi Stride) — bukan salinan, hanya adopsi 4 aturan yang skill kita belum punya.

Skill lain (uiux-methodology, mk-iticm, obsidian-notes) **pointer ke file ini**, bukan menyalin aturan. Perubahan di sini otomatis berlaku di semua.

## Empat Aturan Inti

1. **Sumber immutable** — file sumber tidak pernah diedit. Artikel yang diperbarui, bukan sumbernya.
2. **Source contract** — setiap artikel wajib punya `**Source:**` yang bisa dilacak balik.
3. **Index = lapisan retrieval** — query lewat `README → KNOWLEDGE → artikel`, bukan grep/glob semua file.
4. **`lint` = operasi resmi** — health check hanya Melapor, tidak pernah mengubah. Fix masuk approval satu-satu.

Aturan 1 & 3 sudah ada di skill kita dengan nama lain. Yang baru: **2 (source contract)** dan **4 (lint sebagai operasi)**.

## Kontrak Artikel

Setiap file knowledge yang bukan index — minimal:

```markdown
# Judul Artikel

**Source:** `knowledge/research/<file>.md` · `[2026-09-28]` · fase: Phase 2

2-4 kalimat ringkasan. Scope jelas, bukan abstrak.

## Key Takeaways

- Poin yang langsung kepakai, spesifik
- Angka/nama/path, bukan "bagus"

## Related

[[KNOWLEDGE]] · [[research/<file>]]
```

Exception: `KNOWLEDGE.md` dan `README.md` themselves (mereka index, bukan artikel).

## Mapping ke Struktur Kita

Tidak ada folder `raw/ wiki/ output/ ai-research/` baru. equivalents yang sudah ada:

| Layer pola Karpathy | Equivalent di skill kita | Aturan |
|---|---|---|
| `raw/` (sumber immutable) | `knowledge/research/` (dev-meth) · `RPS/` (mk-iticm) · `data/` (uiux) · `references/raw/` (research web) | Jangan diedit. Kalau perlu koreksi → tulis file baru, catat di `history.md` |
| `ai-research/` (sumber dari web) | `knowledge/research/` dengan frontmatter `url:` + `fetched:` | **Satu file per URL.** Jangan gabung 2 sumber dalam 1 file |
| `wiki/` (artikel hasil compile) | `knowledge/*.md` + `knowledge/<topic>/` | Wikilink = satu-satunya cara rujukan internal |
| `wiki/_master-index.md` | `knowledge/README.md` + `knowledge/KNOWLEDGE.md` | Baca ini duluan, jangan grep |
| `wiki/log.md` | `knowledge/history.md` | Append-only, 1 baris per operasi, format sudah ada |
| `output/` (report) | `knowledge/lint-reports/` | Isi: temuan lint, bukan artikel |

## Operasi

### 1. Ingest (`compile`)

Trigger: ada sumber baru masuk folder sumber, atau user bilang "compile".

1. Baca sumber **penuh**.
2. Cek `knowledge/README.md` — topik ini sudah ada atau belum.
3. Tulis/perbarui artikel. Isi `**Source:**`, `## Key Takeaways`, `## Related`.
4. Backlink dari artikel yang menyentuh artikel ini — update `Related` dua arah.
5. Update `knowledge/README.md` kalau ada topic/indeks berubah.
6. Append 1 baris di `knowledge/history.md`.

Satu sumber bisa menyentuh banyak artikel sekaligus — itu normal, kerjakan dalam satu run.

### 2. Research

Trigger: user minta riset, atau ada gap yang tidak bisa dijawab dari sumber yang ada.

1. Cari sumber web yang relevan.
2. **Satu URL = satu file** di `knowledge/research/`, format:
   ```markdown
   ---
   url: https://example.com/artikel
   fetched: YYYY-MM-DD
   summary: satu baris — artikel ini soal apa
   ---

   <konten penuh, bersih, bukan ringkasan>
   ```
3. Jangan overwrite file yang sudah ada. Buat baru.
4. Setelah semua sumber tersimpan → jalankan Ingest.
5. Artikel boleh mengutip banyak file; **listing semua di `**Source:**`**.

Ringkasan terjadi di artikel, bukan di sini. File ini sumber kebenaran untuk verifikasi klaim.

### 3. Query

Trigger: pertanyaan tentang isi knowledge.

1. `knowledge/README.md` → topic mana.
2. `knowledge/KNOWLEDGE.md` → artikel mana.
3. Baca 1-3 artikel penuh.
4. Jawaban substantial → tanyakan user dulu sebelum difile jadi artikel baru.

Default **3-4 file read**. Kalau butuh lebih, index-nya yang bermasalah — bukan seluruhnya perlu dibaca.

### 4. Lint

Trigger: user bilang "lint"/"audit knowledge", atau sebelum handover/serah terima.

Baca semua artikel di `knowledge/` (index dan `history.md` dikecualikan), laporkan:

1. **Contradictions** — klaim yang saling bertentangan. Cantumkan path + kalimatnya.
2. **Stale claims** — artikel lama yang sudah disusuli sumber/sumber-keputusan baru.
3. **Orphan pages** — artikel nol inbound link.
4. **Missing concepts** — konsep yang disebut di ≥3 artikel tapi belum punya halaman.
5. **Missing cross-links** — pasangan artikel yang 관련된 tapi tidak saling link.
6. **Unsourced claims** — klaim tanpa `**Source:**`, atau sumbernya tidak menyebut klaim itu.
7. **Suggested articles** — 3-5 ide konkret.

Tulis ke `knowledge/lint-reports/lint-YYYY-MM-DD.md`.

**Jangan ubah apa pun saat lint.** Wait for user, apply fix satu per satu, append tiap fix ke `history.md`.

Tool yang sudah ada: `mk-iticm` punya `audit-akhir.py` (jalur `lint` untuk folder RPS). Kalau tidak ada, tulis report manual — tidak perlu bikin script baru.

### 5. Fix

Hanya setelah user menyetujui temuan tertentu:

- Terapkan 1 temuan = 1 turn.
- Append 1 baris di `knowledge/history.md` per fix.
- Kalau sebuah fix menyentuh beberapa artikel, itu tetap 1 fix.

## Konvensi

- **`**Source:**` wajib.** Tidak ada sumber → tulis di `## Open Questions`, jangan ditebak.
- **Nama file lowercase-hyphenated.** `auth-flow.md`, bukan `Auth_Flow.md`.
- **Wikilink untuk rujukan internal.** Path relatif hanya untuk `**Source:**`. Link eksternal wajib `[text](https://...)` dengan skema lengkap.
- **Bullets, bukan paragraf.** Paragraf panjang → section `## Details`.
- **Angka apa adanya.** Kalau sumber bilang 16 pertemuan, tulis 16. Kalau meragukan → catat di `## Open Questions`.
- **Append-only** untuk `KNOWLEDGE.md` sections dan `history.md`.
- **Format vault-native** kalau project di dalam vault Obsidian (frontmatter `title/tags/status/created` + wikilink) — detail di `references/obsidian/markdown.md`.

## Kalau User Minta di Luar Aturan Ini

Tanya klarifikasi, jangan diam-diam bikin operasi baru. Kalau kelihatan berguna, ajukan sebagai tambahan di `SKILL.md` skill terkait — tunggu persetujuan sebelum commit.
