# skills — Koleksi Skill Ardith666

Repositori agregasi skill milik `ardith666`. Setiap skill tetap mandiri — repo ini
adalah **index/copy snapshot**, bukan submodule. Repo per-skill tetap menjadi sumber
otoritatif (`ardith666/<nama>`).

## Daftar Skill

| Skill | Fungsi | Repo sumber |
|---|---|---|
| `obsidian-notes` | Aturan menulis note di vault Obsidian (iCloud) — frontmatter wajib, wikilink internal, markdown link eksternal, INDEX.md + LOG.md per folder | repo ini (snapshot) |
| `mk-iticm` | Orkestrator (entry point) — bangun perangkat pembelajaran lengkap dari RPS: slides, kode, jobsheet, bank soal, penugasan, studi kasus, paket LMS (OBE) | https://github.com/ardith666/mk-iticm |
| `pptx-iticm` | Generator deck PowerPoint branded ITICM (dark navy + orange, OBE, diagram) | https://github.com/ardith666/pptx-iticm |
| `dev-methodology` | Workflow pengembangan terstruktur: spesifikasi → plan → implementasi → review → knowledge (Fable loop + Obsidian) | https://github.com/ardith666/dev-methodology |
| `uiux-methodology` | Intelijen desain UI/UX: design system, brand identity, palet, font pairing, 99+ UX guidelines, 21st.dev MCP | https://github.com/ardith666/uiux-methodology |

## Instalasi di Mesin Baru

Clone reponya (langsung dari repo sumber atau dari sini) ke folder skills agent:

```bash
SKILLS_DIR="${HOME}/.agents/skills"
git clone https://github.com/ardith666/mk-iticm            "$SKILLS_DIR/mk-iticm"
git clone https://github.com/ardith666/pptx-iticm           "$SKILLS_DIR/pptx-iticm"
git clone https://github.com/ardith666/dev-methodology      "$SKILLS_DIR/dev-methodology"
git clone https://github.com/ardith666/uiux-methodology     "$SKILLS_DIR/uiux-methodology"
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
```

## Update Snapshot

Untuk menyegarkan copy di repo ini:

```bash
for s in mk-iticm pptx-iticm dev-methodology uiux-methodology; do
  rsync -a --exclude '.git' --exclude '__pycache__' --exclude '*.pyc' --exclude '.env' \
    "${HOME}/.agents/skills/$s/" "skills/$s/"
done
git add -A && git commit -m "sync snapshot" && git push
```

## Keamanan

- `.env` dari `uiux-methodology` **tidak** dilacak (dikecualikan `.gitignore`).
- Jangan pernah commit `.env` / kunci API ke repo mana pun; gunakan `.env.example`.