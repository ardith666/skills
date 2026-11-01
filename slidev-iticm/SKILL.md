---
name: "slidev-iticm"
description: "Generator and auditor of single-file interactive web slides (Slidev) for ITICM courses based on 12 strict Slidev-ITICM rules. Seamlessly integrates humanizer-indonesia as a mandatory dependency for natural, engaging, anti-AI Indonesian narrative."
---

# Slidev-ITICM

Hasilkan deck HTML tunggal interaktif ala P04 untuk MK ITICM mana pun.

## REQUIRED BACKGROUND & DEPENDENCY
- **`humanizer-indonesia` (MANDATORY DEPENDENCY)**:
  Setiap kali `slidev-iticm` digunakan untuk membuat, menulis ulang, atau mengaudit slide kuliah, aturan dan metrik dari `humanizer-indonesia` **WAJIB otomatis diterapkan secara utuh**. Slide interaktif yang baik tidak hanya benar secara teknis, tetapi harus menggunakan bahasa Indonesia yang mengalir alami, hidup, bebas dari pola kaku AI, dan mudah dipahami oleh mahasiswa awam.
- **`diagram-design`**:
  Pedoman perancangan diagram editorial SVG untuk slide Peta Rangkuman arsitektural.

---

## Integrasi Wajib: `slidev-iticm` + `humanizer-indonesia`

Setiap pembuatan atau pembaruan slide wajib menerapkan standar `humanizer-indonesia` (Preset `ajar` / `akademik`):

1. **Nol Em Dash (`—`) dan En Dash (`–`) di Badan Prosa**:
   * Dilarang keras menggunakan tanda pisah em dash (`—`) di judul, narasi, keypoint, maupun skrip demo.
   * Ganti dengan tanda koma, titik dua (`:`), tanda kurung, atau pecah menjadi dua kalimat mandiri.
2. **Nol Pola Penyangkalan Antisipatif**:
   * Dilarang menggunakan pola klise AI seperti *"bukan berarti bahwa..."*, *"bukan X melainkan Y"*, *"X, bukan berarti Y"*.
   * Ganti dengan konstruksi lugas: *"X belum tentu Y"*, *"X menyimpan Y"*, dsb.
3. **Pembersihan Diksi Klise & Nominalisasi Berlebih**:
   * Ubah verba ringan klise (*melakukan analisis*, *memberikan pengaruh*, *mengalami peningkatan*) menjadi kata kerja aktif (*menganalisis*, *memengaruhi*, *naik*).
   * Buang frasa kosong klise (*penting untuk diingat bahwa*, *perlu dicatat bahwa*, *merupakan salah satu hal yang krusial*).
4. **Analogi Nyata untuk Mahasiswa Awam**:
   * Gunakan analogi yang dekat dengan kehidupan kampus dan prodi ITICM (Informatika, Logistik, Bisnis Digital), misalnya: kamar kos, kantin, antrean kasir UMKM, ojek online, barcode rak gudang, buku tebal dan daftar isi.
5. **Kotak Intisari Wajib "💡 Apa sih maksudnya?"**:
   * Di setiap slide konten (`s1` sampai `sN-1`), letakkan kotak intisari berbingkai oranye ITICM di **posisi paling bawah**, persis di atas baris rujukan `<p class="caption">...lihat sX</p>`.
   * Bahasa di dalam kotak harus sederhana, santai, analogis, dan merangkum konsep utama agar mahasiswa awam langsung paham tanpa bingung.
6. **Verifikasi Metrik Tulisan**:
   * Rerata panjang kalimat: 16 sampai 21 kata.
   * Simpangan baku panjang kalimat: $\ge$ 6.4 (irama bervariasi).
   * Kalimat panjang ($\ge$ 28 kata): maksimal 20%.
   * Gunakan `scripts/check_humanizer.py` untuk menguji kepatuhan teks secara otomatis.

---

## Alur baku deck baru (12 Aturan)

1. **Kerangka Deck Tunggal (`index.html`)**
   * Satu berkas mandiri `index.html`.
   * Slide `s0` adalah cover pembuka (tidak masuk hitungan nomor slide). Slide isi bernomor `s1` sampai `sN`. Slide `sN` adalah cover penutup.
   * Mendukung routing URL hash `#/N`, navigasi keyboard, swipe sentuh pada ponsel, progress bar dinamis, tombol fullscreen, dan mode cetak dokumen penuh via URL parameter `?all=1`.

2. **Struktur Narasi 3 Paragraf & Kotak Maksud**
   * Tiap konten utama terdiri dari paragraf dengan 8-12 kalimat santun formal.
   * Selalu jelaskan alasan di balik konsep, sertakan 1 contoh nyata, 1 kartu *Keypoint* (maksimal 4 poin ringkas), dan 1 elemen visual.
   * Format teks: inden 2em, rata kanan-kiri (*justify*).
   * Tambahkan kotak `<div class="narrow maksud-box">` di ujung bawah slide.

3. **Kunci Angka RPS (Zero Drift)**
   * Catat angka fakta awal, aturan, turunan, total, iterasi maksimal, dan batasan tugas di kepala deck dan cover.
   * Angka harus konsisten 100% antara narasi, kartu poin kunci, diagram alur, demo interaktif, dan tabel rujukan.

4. **Glosarium Interaktif + Fitur Jump**
   * Berkas memuat array tunggal `GLO = [["istilah", "kategori", "definisi"], ...]`.
   * Mendukung pencarian instan (*substring search*), filter chip kategori, penyorotan teks `<mark>`, paginasi 12 item per halaman.
   * Klik tombol lompat akan mengarahkan pengguna langsung ke slide target dengan efek visual kuning/oranye *pulse*, didukung widget mengambang di pojok kanan bawah.

5. **Persistensi Status (State Persistence)**
   * Simpan posisi slide, kata kunci pencarian, filter kategori glosarium, dan modal zoom ke `localStorage` (`pXXstate_v1` disesuaikan per kode pertemuan MK).
   * Routing hash URL selalu menang atas localStorage saat pertama kali dibuka. Mode `?all=1` otomatis menonaktifkan pemulihan status.

6. **Standar Visual ITICM**
   * Tema warna resmi: Kartu putih beraksen `#e86c00` dengan latar belakang `#1a1a2e`.
   * Tabel bergaya *card* putih dengan warna header lembut dan baris belang (*zebra stripe*).
   * Batas lebar elemen visual maksimal 720px (`narrow`), kecuali tabel komparasi lebar atau *trace matrix* (`wide`).
   * Pustaka CDN: Tailwind CSS, GSAP, Mermaid.js, dan Chart.js dengan *lazy initialization on-enter*.
   * Efek animasi transisi halus durasi 0.45s (*fade up* bertingkat), menghormati preferensi aksesibilitas `prefers-reduced-motion`.

7. **Navigasi Bawah & Mobile First**
   * Panel navigasi bawah: `[⏮ Prev Next ⏭]` (`goTo(0)` dan `goTo(N)`).
   * Indikator tengah: `iticm.ac.id · Slide X/N` (otomatis disembunyikan di layar ponsel sempit).
   * Logo kanan (`ml-auto`) berfungsi sebagai tombol buka glosarium dengan *badge* jumlah kata.
   * Kueri media layar ponsel $\le$ 640px merampingkan header, bilah navigasi, dan padding.

8. **Diagram Mermaid Aman (Target 0 Galat)**
   * Alur proses memakai `flowchart TD` (orientasi vertikal agar pas di layar ponsel).
   * Diagram sekuens memakai nama partisipan 1 kata.
   * Pesan dan label simpul **bebas dari karakter `+`, `?`, `=`** (menggunakan frasa deklaratif dengan penghubung `dan`).
   * Jangan gunakan anotasi `Note over`.

9. **Keamanan Sintaks JavaScript (JS Lock)**
   * Dilarang melakukan penggantian teks global yang dapat merusak skrip logika (misal: jangan mengubah `changedTouches` menjadi teks lain).
   * Validasi integritas kode secara berkala via `node --check`.

10. **Kartu Tugas Resmi RPS**
    * Salin parameter tugas resmi langsung dari RPS (nama tugas, sifat individu/kelompok, uraian instruksi, tenggat, dan bobot nilai) tanpa menebak atau mengurangi bobot.

11. **Slide Peta Rangkuman Premium (Arsitektural)**
    * Wajib ada 1 slide rangkuman di akhir deck (`sN-2`) memuat diagram arsitektur utuh dalam format **inline SVG** (berawalan ID `rk-*`, skala fleksibel, max-width 720px).
    * Dilengkapi tombol modal perbesar *fullscreen* dengan kontrol zoom interaktif (`+`, `−`, `0`), penutup via tombol Esc atau tombol X, serta otomatis tersembunyi saat dicetak (`?all=1`).

12. **Blok Kode Terstandar (Prism.js + Tombol Salin)**
    * Setiap blok kode dibungkus format `<pre><code class="language-sql">` / `language-php` / `language-markup` / `language-none`.
    * Memuat 7 berkas komponen Prism.js 1.29.0 dari CDN sebelum tag `<style>`.
    * Dilengkapi tombol Salin satu klik dengan mekanisme salin otomatis dan fallback kompatibilitas lama.

---

## Demo praktik PHP via iframe (pola P05 s25)

1. **File demo mandiri** — satu `demo.php` di folder deck: `declare(strict_types=1)`, data studi kasus tetap (bukan random) didefinisikan di awal + ditampilkan sebagai tabel, logika + HTML dalam satu file, dijalankan lewat `php -S 127.0.0.1:8000 -t .` (bukan `file://`). Data jangan diakses fungsi lewat `global` (lihat Pitfalls: inklusi dari controller).
2. **Struktur slide** — narasi lengkap **di atas** iframe (`<div class="narrow">` h2 border oranye + 2–3 paragraf: studi kasus, constraint, goal, g(n)/h(n)), lalu iframe `loading="lazy"` tinggi ~520px **wajib ditutup `</iframe>`** (tidak ditutup = slide aneh, konten melorot), baris catatan cara menjalankan, lalu dua tombol: **Unduh** (`demo.php?unduh=1`, endpoint unduh di header PHP pakai `readfile(__FILE__)` + `Content-Disposition` filename deskriptif `pXX-topik.php`) dan **Buka di tab baru** (`target="_blank"`).
3. **Grafik perbandingan di dalam demo, bukan di deck** — taruh di bawah kartu hasil sebagai SVG inline buatan PHP (tanpa library JS), label nilai per batang, skala logaritmik bila angka timpang (mis. 3390 vs 7); jangan tambah `<script>` chart.js besar di bawah iframe (lambat, deck jadi berat).
4. **Kartu hasil + rangkuman** — tiap kartu algoritma: KPI (ekspansi / penugasan / slot), tabel hasil, jejak pencarian di `<details>`, dan paragraf "kenapa eksplorasinya segitu" (`<p class="kenapa">`); paling bawah satu card rangkuman: tabel perbandingan + grafik + kesimpulan.
5. **Jebakan performa ruang keadaan** — penugasan berurutan (hanya MK berikutnya yang dipasang slot+ruang) supaya ruang keadaan kecil; `h(n)` di-cache (`static $cache`); string jejak jangan simpan frontier penuh (pakai helper potong 4 simpul + `… +N`) — kalau tidak, BFS OOM dan A* bisa 7 detik; target render < 1s via `php -l` + `php -r '$_GET=[]; include "demo.php";'` tanpa notice.
6. **Narasi slide vs isi demo** — paragraf di slide harus memuat angka/istilah yang sama persis dengan demo (banyak ekspansi, definisi g/h, constraint) supaya tidak ada klaim yang didemo tidak mendukung.

---

## Prism.js + tombol Salin (pola P04–P15)

Blok kode di deck WAJIB disorot sintaks + bisa disalin satu klik. Tanpa ini mahasiswa screenshot layar, bukan menyalin teks.

### 1. Markup

`<pre><code class="language-sql">…</code></pre>` — satu baris, isi escape `&lt; &gt;`.

| class | untuk |
|---|---|
| `language-sql` | SQL: SELECT/INSERT/UPDATE/DELETE/CREATE/ALTER/DROP/SHOW/EXPLAIN/GRANT/REVOKE/WITH/START TRANSACTION/BEGIN/COMMIT/ROLLBACK/TRUNCATE/CALL/DESCRIBE/USE/SET/ANALYZE/OPTIMIZE/SAVEPOINT |
| `language-php` | PHP: `<?php`, `$var =`, `// komentar` |
| `language-markup` | HTML: `&lt;form`, `&lt;input`, `&lt;button` (grammar `markup` sudah ikut CDN) |
| `language-none` | teks polos: output `mysql>`, daftar pustaka, path, hasil hitung, pseudocode `PROGRAM/DEKLARASI/ISI` |

Prism core **tidak** punya grammar `none` → blok dibiarkan polos (aman, tanpa error). Jangan asal tebak `language-sql` untuk blok teks.

### 2. Head — 7 baris, sisipkan SEBELUM `<style>` deck

```html
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/prismjs@1.29.0/themes/prism-tomorrow.min.css">
<script src="https://cdn.jsdelivr.net/npm/prismjs@1.29.0/components/prism-core.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/prismjs@1.29.0/components/prism-markup.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/prismjs@1.29.0/components/prism-clike.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/prismjs@1.29.0/components/prism-markup-templating.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/prismjs@1.29.0/components/prism-php.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/prismjs@1.29.0/components/prism-sql.min.js"></script>
```

`prism-php` butuh `prism-markup-templating` (isi `<?php ?>`), `prism-sql` butuh `prism-clike`. Urutan: core → markup → clike → markup-templating → php → sql.

### 3. CSS — sisipkan setelah `<style>` deck (tema Prism harus kalah spesifisitas)

```css
pre{position:relative}
pre code{background:none;padding:0;border-radius:0;font-size:inherit}
pre[class*=language-]{background:#2d2d3a;padding:14px;margin:12px auto;max-width:720px;border-radius:10px;font-size:.82rem;line-height:1.45}
pre code[class*=language-]{color:inherit}
.codeBtn{position:absolute;top:6px;right:6px;z-index:2;background:#1a1a2e;color:#c0c5d0;border:1px solid #4a4a60;border-radius:6px;font-size:.68rem;padding:2px 8px;cursor:pointer;opacity:0;transition:opacity .18s}
pre:hover .codeBtn,.codeBtn:focus{opacity:1}
.codeBtn:hover{background:#e86c00;border-color:#e86c00;color:#fff}
@media (hover:none){.codeBtn{opacity:1}}
@media print{.codeBtn{display:none!important}}
```

### 4. JS — sisipkan di awal `<script>` inline deck

```js
function kodeTeks(pre){var c=pre.querySelector('code');return c?c.textContent:pre.textContent;}
function salinLama(t,ok){var ta=document.createElement('textarea');ta.value=t;ta.setAttribute('readonly','');ta.style.position='fixed';ta.style.left='-9999px';document.body.appendChild(ta);ta.select();try{document.execCommand('copy');ok();}catch(e){}document.body.removeChild(ta);}
function salinTeks(t,btn){var ok=function(){btn.textContent='Tersalin';setTimeout(function(){btn.textContent='Salin';},1400);};if(navigator.clipboard&&navigator.clipboard.writeText){navigator.clipboard.writeText(t).then(ok,function(){salinLama(t,ok);});}else{salinLama(t,ok);}}
function pasangTombolSalin(){document.querySelectorAll('pre').forEach(function(pre){if(pre.querySelector('.codeBtn'))return;if(!pre.querySelector('code'))return;var btn=document.createElement('button');btn.className='codeBtn';btn.type='button';btn.textContent='Salin';btn.setAttribute('aria-label','Salin kode');btn.addEventListener('click',function(e){e.stopPropagation();salinTeks(kodeTeks(pre),btn);});pre.appendChild(btn);});}
```

Panggil `pasangTombolSalin();` di dalam `sync()` atau setelah DOM siap.

---

## Kamus Ganti Kata Tak Baku $\rightarrow$ Formal

Wajib mengganti kata kolokial berikut ke bentuk formal baku di seluruh teks slide:

| Kata Tak Baku / Kolokial | Pengganti Baku Formal |
|---|---|
| muter | berputar |
| boros | tidak efisien |
| hang | tidak merespons |
| sunyi | hening |
| gampang | mudah |
| bikin | membuat |
| ngubek | menelusuri |
| bolong | belum lengkap |
| kepagian | berhenti terlalu dini |
| ngaruh | berpengaruh |
| ketemu | ditemukan |
| nyumbang | berkontribusi |
| wasit | penentu |
| plus | dan / serta / beserta |
| sapu bersih | pembersihan menyeluruh |

---

## Pitfalls yang Sering Terjadi

- **Deck separuh bisa terlihat penuh**: `index.html` berisi section konten s0–s25 tapi nol `<script>` inline → tak ada nav/glosarium/jump, `goTo` mati dan deck tak bisa dipindah. Verifikasi: `grep -c '<section'` = N+1, `node --check` pada isi `<script>`, dan DOM key yang dipakai `sync()` (`label`, `prog`, `barFill`, `glo*`, `jw*`) ada.
- **Caption tidak center meski `.caption` sudah `text-align:center`**: Penyebabnya `.slide p.mt-3` justify lebih spesifik; tetap pertahankan penimpa `.slide p.caption{text-align:center;text-indent:0}`, bukan menambah `!important` acak.
- **Istilah pakai dulu definisi belakangan**: Wajib footnote `lihat sX` di caption kemunculan, definisi eksplisit di s-basis/s-metode; kuis/drill tetap self-contained.
- **`+` di mermaid picu `<g> translate(undefined,NaN)`**: Ganti `dan`.
- **`iticm.ac.id` kepotong `itic...` di HP**: Hide mid, kanan `ml-auto`.
- **Swipe dilarang**: Navigasi via tombol `[⏮ Prev Next ⏭]` + keyboard panah.
- **Keypoint/bullet terlihat center padahal isi kiri**: Wadah `.kp{text-align:left}`, `.card{text-align:left}` + `.card p{left,indent 0}` + `details.card summary{left}`.
- **Slide demo praktik melorot**: Iframe `</iframe>` tidak ditutup atau narasi/iframe/tombol terpisah `</div>` tak seimbang; wajib tutup iframe dan pastikan tag div seimbang.
- **Demo PHP berat (OOM / >5 detik)**: Ruang keadaan meledak (penugasan semua kombinasi sekaligus); perbaiki: penugasan berurutan, cache `static`, potong string jejak. Grafik perbandingan berupa SVG inline di dalam demo dengan skala log.
- **Perubahan demo tak terlihat setelah edit**: Stream mengirim `Cache-Control: private, max-age=3600`; lakukan hard refresh (Cmd+Shift+R).
- **Blok kode tanpa Prism atau tombol Salin**: Wajib sertakan CDN Prism, bungkus dengan `<code class="language-*">`, dan terapkan CSS override `pre[class*=language-]`.
