# slidev-iticm

Generator dan auditor slide presentasi web interaktif mandiri (*single-file HTML*) untuk seluruh perkuliahan di lingkungan ITICM.

Skill ini dirancang dengan memadukan **12 Aturan Baku Slidev-ITICM** dan **`humanizer-indonesia`** sebagai dependensi wajib.

## Fitur Utama

- **12 Aturan Standar Slidev-ITICM**: Kerangka deck tunggal, narasi 3 paragraf, kunci angka RPS, glosarium interaktif dengan jump widget, navigasi mobile-first, visual aman, diagram Mermaid bebas galat, diagram arsitektur inline SVG dengan modal zoom, dan blok kode Prism.js dengan tombol salin.
- **Dependensi Wajib `humanizer-indonesia`**: Bahasa alami mengalir tanpa pola kaku AI, nol em dash (`—`), nol pola penyangkalan antisipatif (*bukan berarti*, *bukan X melainkan Y*), analogi ramah mahasiswa awam, dan kotak intisari "💡 Apa sih maksudnya?" di setiap slide materi.
- **Peralatan Audit Otomatis**: Dilengkapi skrip verifikasi bahasa (`check_humanizer.py`), audit struktur deck (`audit.py`), verifikasi peta rangkuman (`rk_verify.py`), dan injeksi Prism.js (`prism_patch.py`).

## Instalasi

```bash
git clone https://github.com/ardith666/skills.git
./setup.sh
```
