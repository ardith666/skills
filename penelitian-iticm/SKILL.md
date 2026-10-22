---
name: penelitian-iticm
description: Use when drafting an Indonesian scientific journal article section by section — pendahuluan, tinjauan pustaka, metode, hasil, pembahasan, SINTA/journal publication, target journal selection, PRISMA for SLR, QC and submission package, AMP prompts, literature-based or field research
---

# Penelitian-ITICM

## Overview
Step-by-step router for a journal-ready Indonesian article (AMP Gen.03, Tahap 0–13). Work ONE stage at a time: read only that stage's file, ask what it needs, run its prompt, pass its gate, then advance.

## When to Use
- User says: tulis artikel ilmiah, pendahuluan, tinjauan pustaka, metode, jurnal SINTA, AMP Gen.03
- Field (kualitatif/kuantitatif/mixed) or literature-based (SLR, narrative/integrative review, conceptual paper)
- NOT for: skripsi/thesis chapters, non-academic copywriting, single-paragraph paraphrase

## Cara Kerja
0. Siapkan/baca `<proyek>/knowledge/` dulu (lihat "Workspace knowledge/") — sesi lanjutan mulai dari ROADMAP + HISTORY, bukan dari nol.
1. Mulai dari Tahap 0. Baca HANYA file tahap aktif di `stages/` — jangan preload sisanya.
2. Tanyakan input yang dibutuhkan tahap itu (lihat "Tanya ke user" per file). Data kosong → tandai + tanya ulang, JANGAN asumsi.
3. Jalankan prompt tahap itu: satu bagian = satu generate utuh, judul bab eksplisit di awal.
4. Cek gate tahap itu bersama user sebelum lanjut. Urutan default berurutan; boleh lompat hanya bila gate tahap yang dilewati sudah terpenuhi.
5. SLR → baca `references/prisma-slr.md` saat Tahap 6 dan 7.

## Workspace knowledge/
Setiap proyek artikel WAJIB punya folder `<proyek>/knowledge/` sebagai memori bersama:
1. Saat proyek baru dimulai: buat `<proyek>/knowledge/` berisi `ROADMAP.md` (semua tahap sebagai checkbox `- [ ]`/`- [x]` + artefak tiap tahap) dan `HISTORY.md` (log berjalan per tanggal).
2. Setiap selesai satu pekerjaan: centang checkbox di ROADMAP dan tambah 1 entri HISTORY (tanggal, ringkasan, file ditulis/diubah, keputusan user).
3. Setiap sesi lanjutan: baca ROADMAP + HISTORY dulu sebelum bertanya — status sudah/belum terbaca dari checkbox.

## Index Tahap
| # | File | Hasil |
|---|---|---|
| 0 | `stages/tahap-00-jurnal.md` | Jurnal target + template dikunci |
| 1 | `stages/tahap-01-aturan.md` | Aturan sitasi dikunci (verbatim Notes) |
| 2 | `stages/tahap-02-desain.md` | 13 field desain + data (verbatim Notes) |
| 3 | `stages/tahap-03-struktur.md` | Struktur IMRaD+ dikunci |
| 4 | `stages/tahap-04-pendahuluan.md` | Pendahuluan 5 paragraf, min 10 kutipan |
| 5 | `stages/tahap-05-tinjauan.md` | Tinjauan pustaka 6 paragraf, min 10 kutipan |
| 6 | `stages/tahap-06-metode.md` | Metode 6 komponen, min 6 kutipan (+PRISMA bila SLR) |
| 7 | `stages/tahap-07-hasil.md` | Hasil: report only, tanpa interpretasi |
| 8 | `stages/tahap-08-pembahasan.md` | Pembahasan reverse funnel, min 10 kutipan |
| 9 | `stages/tahap-09-kesimpulan.md` | Kesimpulan ≤3 paragraf, tanpa ref baru |
| 10 | `stages/tahap-10-pustaka.md` | Daftar pustaka terverifikasi (Zotero) |
| 11 | `stages/tahap-11-abstrak.md` | Abstrak 150–250 kata + kata kunci |
| 12 | `stages/tahap-12-english.md` | Terjemahan Academic English |
| 13 | `stages/tahap-13-qc-submit.md` | QC + metadata + cover letter + cek plagiarisme |

## Aturan Global
- Template jurnal (Tahap 0) menang atas aturan Tahap 1 bila konflik — catat konfliknya eksplisit.
- Sitasi: 5 tahun terakhir / SINTA 1-2, open-access + hyperlink, APA 7, tanpa repeat ref per bagian.
- Tense: Pendahuluan present, Metode/Hasil past, Pembahasan campuran; hedging (`suggests/may`) bukan `proves`.
- Setiap DOI/nama/tahun diverifikasi; yang tak terkonfirmasi ditandai `[PERLU VERIFIKASI MANUAL]`.
- LLM tidak boleh jadi co-author; cek AI-disclosure jurnal sebelum submit.
- Humanizer & Turnitout pass: sebelum Tahap 13 (submit), jalankan skill humanizer mode file atas draf final untuk nada alami. Selanjutnya, gunakan [Turnitout-Humanizer](https://github.com/ardith666/Turnitout-Humanizer) (alat zero-AI deterministik) untuk membersihkan token watermark AI, zero-width tracking Unicode, metadata C2PA, dan memecah contiguous n-gram pemicu Turnitin/iThenticate pada berkas .docx/.tex.
- Dependensi ekosistem: `Turnitout-Humanizer` (sanitasi Turnitin/AI), `naskah-id` (kaidah EYD V / KBBI), `dev-methodology` (state tracking), dan `officecli` (`tools/officecli.md` untuk build format .docx).
- Dependensi .docx: officecli (instal + konvensi JUTISI di `tools/officecli.md`); dipakai Tahap 13 untuk membangun file .docx naskah.
- Latar: Tahap 1–6 verbatim Notes ITICM/Penelitian "Aturan Promt"; Tahap 0, 7–13 lanjutan gaya sama. Pelajaran `jamditis/academic-writing`: `references/pelajaran-academic-writing.md`. Verifikasi sumber + IEEE (dari `endigo/academic-research-writer`): `references/verifikasi-sumber.md`, `references/format-ieee.md`.
