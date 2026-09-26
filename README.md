# skills — Koleksi Skill Ardith666

Repositori agregasi skill milik `ardith666`. Setiap skill tetap mandiri — repo ini
adalah **index/copy snapshot**, bukan submodule. Repo per-skill tetap menjadi sumber
otoritatif (`ardith666/<nama>`).

## Daftar Skill

| Skill | Fungsi | Repo sumber |
|---|---|---|
| `obsidian-notes` | Aturan menulis note di vault Obsidian (iCloud) — frontmatter wajib, wikilink internal, markdown link eksternal, INDEX.md + LOG.md per folder | https://github.com/ardith666/obsidian-notes |
| `mk-iticm` | Orkestrator (entry point) — bangun perangkat pembelajaran lengkap dari RPS: slides, kode, jobsheet, bank soal, penugasan, studi kasus, paket LMS (OBE) | https://github.com/ardith666/mk-iticm |
| `pptx-iticm` | Generator deck PowerPoint branded ITICM (dark navy + orange, OBE, diagram) | https://github.com/ardith666/pptx-iticm |
| `dev-methodology` | Workflow pengembangan terstruktur: spesifikasi → plan → implementasi → review → knowledge (Fable loop + Obsidian) | https://github.com/ardith666/dev-methodology |
| `uiux-methodology` | Intelijen desain UI/UX: design system, brand identity, palet, font pairing, 99+ UX guidelines, 21st.dev MCP | https://github.com/ardith666/uiux-methodology |
| `diagram-design` | 39 tipe diagram editorial, output HTML+SVG self-contained, bisa redraw Mermaid/draw.io | https://github.com/ardith666/diagram-design |
| `security-meth` | Audit keamanan source-first 6 fase (recon → coverage hunting → validasi → output terstruktur → verifikasi independen → report), fork cloudflare/security-audit-skill (MIT) | https://github.com/ardith666/security-meth |

## Bootstrap Otomatis (setup.sh)

Clone repo ini, lalu jalankan `setup.sh` — symlink semua skill yang punya `SKILL.md` di root ke `~/.agents/skills/`:

```bash
git clone https://github.com/ardith666/skills.git /tmp/skills
/tmp/skills/setup.sh   # SKILLS_DIR bisa di-override via env
```

Skill yang sudah ada sebagai folder asli (bukan symlink) di-skip. Detail: `./setup.sh`

## Instalasi Manual di Mesin Baru

Clone reponya (langsung dari repo sumber atau dari sini) ke folder skills agent:

```bash
SKILLS_DIR="${HOME}/.agents/skills"
git clone https://github.com/ardith666/mk-iticm            "$SKILLS_DIR/mk-iticm"
git clone https://github.com/ardith666/pptx-iticm           "$SKILLS_DIR/pptx-iticm"
git clone https://github.com/ardith666/dev-methodology      "$SKILLS_DIR/dev-methodology"
git clone https://github.com/ardith666/uiux-methodology     "$SKILLS_DIR/uiux-methodology"
git clone https://github.com/ardith666/obsidian-notes       "$SKILLS_DIR/obsidian-notes"
git clone https://github.com/ardith666/diagram-design      "$SKILLS_DIR/diagram-design"
git clone https://github.com/ardith666/security-meth        "$SKILLS_DIR/security-meth"
```

Lihat `SKILL.md` di masing-masing skill untuk `REQUIRED BACKGROUND` / dependensi
eksternal (mis. `mk-iticm` butuh `obra/superpowers` untuk `dispatching-parallel-agents`,
`uiux-methodology` butuh data CSV + `python-pptx`/node untuk script).

## Hubungan Antar Skill

```
mk-iticm (entry point, orkestrasi 5 phase)
├── butuh dev-methodology          → disiplin knowledge/ + history.md
├── butuh pptx-iticm               → produksi deck (Phase 3)
└── butuh dispatching-parallel-agents (superpowers) → fan-out 4 workstream

pptx-iticm (mandiri, bisa dipakai tanpa mk-iticm untuk edit/generate deck)
uiux-methodology (independen)
security-meth (dipanggil dev-methodology Phase 5 — audit coverage; strix buat pentest aktif)
```

## Update Snapshot

Untuk menyegarkan copy di repo ini:

```bash
for s in mk-iticm pptx-iticm dev-methodology uiux-methodology obsidian-notes; do
  rsync -a --exclude '.git' --exclude '__pycache__' --exclude '*.pyc' --exclude '.env' \
    "${HOME}/.agents/skills/$s/" "skills/$s/"
done
```

`diagram-design` di-sync dari mirror terpisah (`~/code/diagram-design-mirror`, bare clone
upstream cathrynlavery/diagram-design) via `./sync.sh` — bukan dari `~/.agents/skills/`:

```bash
./sync.sh   # sync mirror -> push ardith666/diagram-design -> refresh snapshot di sini
```

## Keamanan

- `.env` dari `uiux-methodology` **tidak** dilacak (dikecualikan `.gitignore`).
- Jangan pernah commit `.env` / kunci API ke repo mana pun; gunakan `.env.example`.

## Panduan Kebutuhan — Skill Mana untuk Apa

| Kebutuhan | Skill yang dipakai | Keterangan |
|---|---|---|
| **Perangkat pembelajaran / RPS kampus (OBE)** | `mk-iticm` (orserkestrasi) + `pptx-iticm` (slide) + `dev-methodology` (knowledge) + `obsidian-notes` (catatan) | Satu paket lengkap: RPS → slides, kode, jobsheet, bank soal, penugasan, studi kasus, paket LMS |
| **Slide/deck presentasi (branded ITICM)** | `pptx-iticm` | Dark navy + orange, alur OBE, diagram, kode |
| **Coding assistant / workflow dev** | `dev-methodology` (+ `diagram-design` utk diagram) | Spek → plan → implementasi → review → knowledge (Fable loop + checkpointing) |
| **Desain UI/UX** | `uiux-methodology` | Design system, brand identity, palet, font pairing, UX guidelines, 21st.dev |
| **Catatan/knowledge base (Obsidian)** | `obsidian-notes` | Frontmatter wajib, wikilink, INDEX.md, LOG.md — konsisten antar agent |
| **Security audit / review keamanan** | `security-meth` (+ `dev-methodology` Phase 2/5 hook) | Source-first 6 fase: recon → coverage hunting → validasi adversarial → findings.json + REPORT.md. Pentest aktif terpisah: `penetration-testing-with-strix` |

> **RPS kampus = jalur lengkap:** `mk-iticm` memanggil `pptx-iticm`, `dev-methodology`, dan `obsidian-notes` di dalam alurnya — cek `SKILL.md` masing-masing utk dependency.
> **Diagram:** `diagram-design` = snapshot flat di repo ini (folder `diagram-design/`),
di-sync via `./sync.sh` dari mirror `ardith666/diagram-design` (upstream
cathrynlavery/diagram-design).
