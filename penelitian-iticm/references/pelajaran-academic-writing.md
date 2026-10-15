# Bedah: jamditis academic-writing (claude-skills-journalism)

Sumber: `https://github.com/jamditis/claude-skills-journalism` → `research-toolkit/skills/academic-writing/SKILL.md` (28.155 bytes, 794 baris, 3.974 kata, branch `master`) + `agents/openai.yaml` (trivial, 2 field saja) via awesomeskill.ai. Dibedah tuntas 2026-10-15: baris 1–150, 150–190, 190–750, 750–794, dan `agents/` — tidak ada bagian terlewat.

## Yang diadopsi ke penelitian-iticm
1. **IMRaD + funnel**: Introduction funnel (konteks → gap → RQ → kontribusi); Discussion reverse funnel; Methods = reproducibility test; Results = report don't interpret. → dipakai Tahap 4/7/8.
2. **Hedging + tense**: suggests/may/indicates bukan proves; Abstract past-untuk-metode/hasil + present-untuk-simpulan; Methods/Results past. → Tahap 8/11/12.
3. **Anti-fabrication**: LLM menghalusinasi DOI/penulis/halaman → verifikasi manual tiap sitasi; detektor AI tidak reliabel. → Tahap 10 + Quick Reference.
4. **AI-disclosure**: LLM dilarang jadi co-author; cantumkan tool + versi + fungsi di methods/acknowledgments sesuai kebijakan jurnal; cek kebijakan tiap submit. → penutup prompts.
5. **Paragraf 100–200 kata**, topic sentence + 1 ide + evidence + transisi (furthermore/however/therefore/for instance). → Quick Reference.
6. **IMRaD detail baris 150–190** (validasi, bukan hal baru): Intro funnel 5 langkah, lit review tematik-bukan-kronologis, Methods checklist (sampel–instrumen–prosedur–analisis–etik), Results (effect size bukan sekadar p-value, jawab tiap RQ), Discussion 7 langkah — semuanya sudah tercermin di Tahap 4–8, tidak perlu perubahan.
7. **Reference manager**: Zotero disarankan (open source, sync); Mendeley Desktop legacy tanpa pengembangan fitur — Paperpile/EndNote/Citavi alternatif. → masuk Tahap 10.

## Yang TIDAK diadopsi (rujukan saja)
- **FINER** (Feasible, Interesting, Novel, Ethical, Relevant) + tipe RQ (deskriptif/komparatif/korelasional/kausal/eksploratori) — berguna saat Tahap 2 masih kabur.
- **Systematic search**: database per bidang (WoS/Scopus, JSTOR/SSRN, PubMed/MEDLINE, ERIC), template Boolean + kriteria inklusi/eksklusi + catat tanggal/jumlah hasil — untuk SLR di Tahap 6/7.
- **Citation manager**: pola Zotero/BibTeX, gaya apa7/mla9/chicago/harvard/ieee/vancouver; kutip sekunder "as cited in".
- **Grant (NSF/NIH)**: aims/significance/innovation/approach/broader impacts + budget — di luar skop artikel.
- **Publishing**: pilih jurnal (scope/fit/acceptance rate/indexing), red-flag predator (email agresif, review hitungan hari, tak terindeks), Think-Check-Submit, DOAJ, COPE, ICMJE authorship, OA routes (Gold/Green/Diamond/Hybrid-dikecualikan-Plan S/Bronze-bukan-OA), Nelson Memo 2026 (akses langsung tanpa embargo untuk riset federal AS), Plan S (CC-BY tanpa embargo).
- **Preprint/PID**: arXiv/SSRN/bioRxiv/medRxiv/PsyArXiv/SocArXiv/EngrXiv/EarthArXiv; ORCID/DOI (Zenodo)/ROR.
- **Ethics**: IRB/consent, data management plan, CRediT 14 peran, preregistrasi OSF/AsPredicted, Registered Reports; misconduct (fabrication/falsification/plagiarism/p-hacking/HARKing/salami/gift-authorship).
- **Review**: template response letter per reviewer + strategi setuju/sebagian/tolak-sopan; cover letter + suggested reviewers.
- **Sengaja TIDAK diadopsi**: writing routine (daily habit, "shitty first draft", placeholder) — bertentangan dengan aturan AMP utuh-1x-generate; task/focus tools (Todoist, Forest), kolaborasi (Google Docs/Overleaf), version control (Git vs Track Changes), analisis/visualisasi (R/Python/NVivo/ggplot2) — di luar skop artikel; grant/proposal penuh.

## Kapan buka file asli
- RQ kabur → FINER; SLR → search template; submit → journal vetting + disclosure; grant → proposal structure. File asli tidak dibundel (28KB) — ambil dari GitHub bila perlu.
