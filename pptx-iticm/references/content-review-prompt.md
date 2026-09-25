# Prompt Review Eyes-Fresh (Fresh-eyes Review) — Deck ITICM

Kapan: SETELAH `check_deck.py` menghasilkan FAIL 0. Keseluruhan ini diberikan ke
**agent/sesi BARU (tanpa konteks build)**, bersama file `.pptx` deck.

> JANGAN beri tahu reviewer: cara pembuatan, skill/script, brand, aturan internal,
> atau konteks RPS. Biarkan ia membaca deck sebagai pembaca baru (mahasiswa/penilai).

---

## Prompt untuk reviewer (tempel apa adanya)

```
Kamu adalah me-review deck PowerPoint kuliah [Nama Matakuliah] untuk dosen.
Deck ada di file <path.pptx>. Buka dan baca SEMUA slide, termasuk speaker notes.

Tugasku: temukan masalah yang akan mengganggu mahasiswa/penilai dan ditulis dalam
bahasa Indonesia.

Periksa khususnya:
1. KEHALUSAN BAHASA (paling penting): kalimat aneh, tidak lengkap, kata berlebihan,
   campuran subjek/objek, istilah yang tidak konsisten (satu konsep dua nama).
2. LOGIKA & ISI: judul yang menjanjikan hal yang isi slide tidak beri; angka tanpa
   satuan/konteks (mis. "85%" tanpa "dari dataset apa, k berapa"); alur yang tidak
   nyambung dari slide ke slide (baca judul saja jadi tidak masuk akal).
3. KEKURANGAN DATA: slide yang bermutu "tipis" (hanya definisi/bullet kosong tanpa
   tabel, angka, contoh, kode+output, atau studi kasus).
4. BAHASA PERCAKAPAN KULIAH yang tidak pantas di slide materi ("kita semua tahu…",
   "seperti yang telah kita bahas", "sangat menarik").

Untuk tiap temuan berikan:
- halaman slide (nomor)
- kutipan persis yang bermasalah
- satu kalimat alasan + saran perbaikan

Lalu buat TABEL AKHIR persis format ini:

## Tabel Terima/Tolak
| No | Slide | Temuan (kutipan) | Alasan | Saran | Keputusan (Terima/Tolak/Pending) |

Mana yang TOLAK beri alasan singkat (mis. "salah interpretasi — '85%' sudah tertulis
dengan cond 10-fold CV di slide tsb").

Tidak usah pujian. Jangan merombak isi akademik yang benar — hanya perbaikan
bahasa/logika/data.
```

---

## Penggunaan hasil (untuk pembuat)

1. **Terima** → perbaiki di `pptx/draft/draft-pertemuan.md`, lalu regenerate deck.
2. **Tolak** → tulis alasan 1 baris di kolom Keputusan (jangan tinggalkan kosong).
3. **Pending** → tampilkan kepada user; minta keputusan.
4. LAMPIRKAN tabel ini ke hasil (serah terima/pengiriman) sebagai bukti QA.
5. Temuan yang **diterima & sifatnya umur panjang** (bukan satu kali) → tambahkan
   1 baris ke `references/slide-rules.md` (§0/§7/§9, atau seksi terakhir) agar tidak
   terulang. Ini cara rulebook tumbuh.

## Ingat

- **Rally = 1 putaran**: check → QA visual → fresh-eyes → perbaiki → check ulang.
  Setelah 1 rally, TAMPILKAN hasil + tabel ke user, lalu TANYA "lanjut rally berikutnya?".
  Jangan auto-loop (slide-rules §8.5).
- Review tidak menggantikan `check_deck.py` (struktur) — keduanya berbeda; jalankan keduanya.