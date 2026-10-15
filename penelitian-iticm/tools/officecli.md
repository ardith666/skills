# officecli — dependensi .docx penelitian-iticm

Sumber skill: https://github.com/iOfficeAI/OfficeCLI/blob/main/SKILL.md

## Instal (sekali per mesin)
```bash
curl -fsSL https://d.officecli.ai/install.sh | bash
officecli --version
```
Skill tersimpan di `~/.agents/skills/officecli/SKILL.md` (disalin dari raw GitHub).
Aturan akademik lanjutan: `officecli load_skill academic-paper` (IEEE, hanging indent, SEQ/PAGEREF).

## Konvensi naskah JUTISI yang dipakai
- A4 (21 x 29,7 cm), margin 3 cm semua sisi:
  `officecli set FILE '/section[1]' --prop pageWidth=21cm --prop pageHeight=29.7cm --prop marginTop=3cm --prop marginBottom=3cm --prop marginLeft=3cm --prop marginRight=3cm`
- Default font: `officecli set FILE / --prop docDefaults.font=Arial --prop docDefaults.fontSize=10pt`
- Judul 16pt tengah tebal; isi justify; pustaka hanging indent:
  `--prop leftIndent=0.75cm --prop hangingIndent=0.75cm`
- Isi via batch JSON: `officecli batch FILE --input part.json --json`
  (atomik: satu gagal = rollback; kutip path `[N]` dengan tanda kutip di zsh)
- Tabel via `add --type table --prop 'data=H1,H2;R1C1,R1C2'`
- QA: `officecli validate FILE` + `officecli view FILE issues --limit N`

## Catatan
- Nama penulis/afiliansi selalu placeholder sampai user mengisi.
- Angka sensitif memakai rentang (lihat VOICE/keputusan proyek).
