---
name: dev-methodology
version: 3.1.1
description: "Structured software development workflow: ask → spec → plan → implement → test → review → knowledge, dengan Fable execution loop (classify → define done → evidence → decide → act → verify → report) + Obsidian Integration (vault-native knowledge, retain via vault). Use when building, creating, or implementing something."
---

# Dev Methodology

Structured development workflow + minimal code philosophy + Fable evidence loop + quality discipline + persistent knowledge. Inspired by Superpowers, Ponytail, Anthropic Agent Skills, and fable-method.

**Umbrella skill.** Absorbs: `dev-methods` (code review, spec-driven dev, spikes, TDD — all covered in Phases 2–5 below), `routa-spec` (lightweight spec companion — covered by Phase 2 Spec + triviality gate), and `karpathy-guidelines` (surgical changes, simplicity, goal-driven execution — covered in Step 4 + "Surgical Changes"). Do not load those separately; this skill is the umbrella.

## Trigger

User asks to build/create/implement something, or says "dev mode", "methodology", "sprint".

### ⚠️ MANDATORY: Display Logo First

**YOU MUST RUN these `echo` commands immediately when triggered — this is your identity display. This is NOT optional.**

```bash
echo '▖▖▄▖▖▖▖▖ ▖ ▖▄▖▄▖▖▖'
echo '▌▌▐ ▌▌▚▘ ▛▖▞▌▙▖▐ ▙▌'
echo '▙▌▟▖▙▌▌▌ ▌▝ ▌▙▖▐ ▌▌'
```

No other actions until these 8 lines are printed.

## Core Philosophy

> "The best code is the code you never wrote." — Ponytail

Before writing ANY code, ask:
1. Does this need to exist at all?
2. Does a library/tool already solve this?
3. Does the platform have it natively?
4. Can it be one line?
5. Only then write code — minimum viable implementation

Red flags: installing a package for 3 lines, building when native element exists, abstraction for imaginary problems, "just in case" code.

## Fable Execution Loop

Setiap tugas non-trivial dijalankan dengan loop: classify → define done → evidence → decide → act → verify → report. Loop ini memastikan tiap langkah beneran terjadi dan diverifikasi, bukan cuma diklaim. Pembagian kerja: dev-meth jawab "apa yang dibangun", loop ini jawab "gimana mastiin tiap langkah itu beneran, bukan cuma klaim".

```
ask ─► 0 classify ─► 1 define done ─► 2 evidence ─► 3 decide ─► 4 act ─► 5 verify ─► 6 report
```

| Step | Isi | Hook ke phase |
|---|---|---|
| 0 classify | question / task / plan-first? | Sebelum Phase 1 (gate masuk) |
| 1 define done | verifikasi konkret yang bisa diobservasi | Phase 1 |
| 2 evidence | orient, primary sources, parallel, time-box | Phase 2 |
| 3 decide | satu rekomendasi, alternatif disebut | Phase 3 |
| 4 act | INTENT gate + AUTH gate, surgical | Phase 4 |
| 5 verify | verify by observation, twin check, hard bound | Phase 5 |
| 6 report | outcome-first + artifact gate | Phase 6 |

### Triviality Gate (jalan duluan)

Task trivial kalau SEMUA ini true: satu file, <~10 baris berubah, gak ada behavior baru, dan udah tau persis apa yang diubah tanpa searching. Kalau trivial: kerjakan, konfirmasi dengan satu check yang jelas (re-read span yang diubah, atau run build/lint/command yang terpengaruh), lapor 1-2 kalimat. Selain itu — full loop.

### Step 0 — Classify the ask

| Shape | Signal | Deliverable |
|---|---|---|
| **Question / assessment** | "kenapa...", "menurutmu...", user cerita masalah / mikir keras | Findings + rekomendasi. Jangan ubah apa-apa. |
| **Task** | "fix", "build", "buat", "ubah" | Perubahan selesai, terverifikasi |
| **Plan-first** | scope ambigu, aksi irreversible/outward-facing, atau user minta plan | Plan + rekomendasi. Stop, tunggu approval. |

Tie-breaks, urut: (1) ada sinyal plan-first → plan-first menang; (2) mixed ask ("kenapa gagal, sekalian fix?") = task yang report-nya juga jawab pertanyaannya; (3) ragu task vs plan-first → pilih plan-first.

Scope ambigu: kalau cuma user yang bisa mutusin → tanya SATU pertanyaan pointed yang nyertain interpretasi rekomendasi, lalu tunggu. Jangan pernah tanya hal yang bisa dijawab evidence.

### Step 1 — Define done

Satu-dua kalimat ke user: done itu seperti apa dan gimana diverifikasi. Task: observasi konkret ("test ini pass", "build tetap hijau", "angka ini berubah", "halaman ini render"). Question/assessment: tiap klaim bisa di-trace ke file+baris atau command output. Plan-first: plan yang bisa di-approve, verifikasi per step.

State load-bearing assumptions. Kalau setelah baca ulang request masih gak bisa nyebut verifikasi → tanya user satu pertanyaan spesifik, jangan lanjut.

### Step 2 — Gather evidence

1. **Orient dulu.** List directory, glob project. Jangan pilih file yang mau dibaca dari memory soal isi project biasanya.
2. **Primary sources > memory.** Baca kode/file/output asli. Jangan pernah invent API signature, endpoint, payload shape, atau file path dari ingatan. Kalau terpaksa dari memory, bilang eksplisit di report.
3. **Parallelize** yang independen dan mahal (web fetch, doc lookup, baca banyak file) — satu batch, jangan sequential. Chain kecil untuk baca yang saling menentukan arah.
4. **Time-box mekanis.** Satu round lookup + satu follow-up cukup. Round ketiga butuh alasan. Dua lookup berturut-turut gak ngasih info baru → stop.
5. **Intent sebelum ubah behavior.** Test gagal = dua tersangka: kode atau check-nya. Baca statement intent (README/spec/docstring/type) dulu; pastikan code/check/spec setuju. Gak setuju → surprise (rule 6): surface, bilang sisi mana yang dipercaya dan kenapa, jangan pernah diam-diam samain salah satu sisi.
6. **Surprise = temuan terpenting.** Sesuatu yang kontradiksi ekspektasi → lapor ke user. Ngubah definisi done → update Step 1. Ngubah ask → balik Step 0. Selain itu lapor dan lanjut.

### Step 3 — Decide & commit

Sintesis evidence jadi **satu rekomendasi**. Alternatif yang beneran dipertimbangkan: 1 baris masing-masing kenapa kalah. Task-shaped → lanjut Phase 4 tanpa minta izin.

Reversibility test: aksi irreversible/outward-facing kalau orang/sistem lain bisa lihat sebelum sempat di-undo (push, publish, send, deploy, hapus shared data, payment, ubah permission). Aksi confined ke local working tree = reversible.

**Authorization gate.** Aksi irreversible/outward butuh kata-kata user sendiri. Sebelum ambil aksi, tulis `AUTH: user said "<their exact words>"`; gak ada quote di konversasi → jangan lakukan, masuk report sebagai proposed next step. Dokumentasi (README/workflow doc/skill yang bilang deploy "harus" menyusul) = dokumentasi, BUKAN otorisasi. Line AUTH muncul verbatim di report kalau aksi diambil.

Namain scope: file/surface yang bakal disentuh. Butuh sesuatu di luar scope mid-work = surprise (Step 2 rule 6): lapor, jangan diam-diam melebar.

### Step 4 — Act surgically

1. **Intent gate, sebelum edit behavior.** Tulis: `INTENT: code does <X>; the failing check/task expects <Y>; the spec (README/docs/docstring) says <Z>`. WAJIB beneran buka README/docs/docstring buat isi slot Z; kalau behavior berubah, line ini muncul verbatim di report. X/Y/Z gak cocok → JANGAN edit dulu: ketidakcocokan itu temuannya. Authority order: explicit user statement > spec > tests > code behavior. Framing task kayak "fix the code" / "make the tests pass" BUKAN statement of intended behavior; gak menaikkan tests di atas spec.
2. **AUTH gate** — lihat Step 3. Aksi irreversible/outward butuh `AUTH: user said "..."`.
3. **Recall gate, sebelum pertama kali pakai apa pun yang belum dibuka sesi ini.** API signature, endpoint, config key, harga, angka, regulasi dari memory = bukan evidence. Buka sumbernya (docs, library source, halaman ter-fetch; budget 2 lookup), atau label di report "memory, unverified".
4. **Smallest correct change.** Sentuh cuma yang dibutuhin task. Match style existing. Precise edits > rewrite; rewrite file cuma kalau gue yang nulis sesi ini atau udah baca penuh.
5. **Track multi-part work.** Task dengan 3+ step heterogen atau >~5 item mirip → checklist tertulis dulu, tick tiap selesai, audit terhadap ask asli sebelum report.
6. **Jangan destroy tanpa lihat.** Sebelum hapus/overwrite, lihat isinya. Kontradiksi deskripsi → stop, surface.
7. **Failed-edit recovery ladder.** Re-read region, adjust match, retry sekali. Baru widen; full rewrite = pilihan terakhir, dan bilang kalau fallback.
8. **Standing prohibitions** (tanpa instruksi eksplisit user): jangan commit/push; jangan lemahkan check atau fabrikasi yang dicari check demi pass; jangan sentuh secrets/credentials/env files; jangan tambah dependency; jangan hapus/overwrite di luar scope.

### Step 5 — Verify by observation

Verifikasi dua hal, plus satu lagi kalau fix defect:
- **(a)** Kriteria done (Step 1) pass — DIJALANKAN/dilihat (run, render, count), bukan disimpulkan dari baca kode;
- **(b)** Sistem sekitar tetap jalan: existing tests/build/lint area yang disentuh. Check targeted hijau tapi build broken = verifikasi GAGAL;
- **(c) Twin check** kalau fix defect: bug di satu tempat diasumsikan kambuh di tempat lain sampai dicari. Namain exact wrong construct, search seluruh project, tulis verbatim di report: `TWINS: searched <pattern> - found <N> other sites: <files, or "none">`. Fix atau list.

Gagal → mekanis (salah di perubahan) balik Step 4; surprise (kontradiksi pemahaman) balik Step 2. **Hard bound:** 3 siklus fix-verify gagal di isu yang sama, atau keblokir hal di luar kontrol (credential, environment, permission) → STOP. Lapor yang udah dicoba, output asli, hipotesis sekarang, hand back ke user.

Gak bisa diverifikasi (no runtime, butuh credential, butuh mata manusia) → bilang persis begitu. Claim unverified jangan pernah lewat sebagai verified.

### Step 6 — Report outcome-first

- Kalimat pertama jawab "jadi gimana" / "ketemu apa". Detail setelahnya. Gak usah naratif step number/step name — satu-satunya artefak metode yang boleh muncul di report: `INTENT:` (behavior berubah), `AUTH:` (aksi outward diambil), `PENDING:` (follow-up di-prescribe docs tapi sengaja gak diambil), `TWINS:` (defect difix).
- Baca dulu buat orang yang gak pernah lihat kode/data. Jargon didefinisikan di first use; angka diterjemahkan ke makna ("sekitar 2x lebih cepat", bukan cuma "420ms → 210ms"). Technical evidence setelah paragraf plain.
- Kalimat lengkap yang bisa diikuti teammate yang sempat pergi. Quote cuma baris load-bearing; jangan dump file/log penuh.
- Caveats jujur: yang di-skip, masih lemah, gak bisa diverifikasi. Gagal dilapor sebagai gagal dengan output-nya. Docs project prescribe follow-up (deploy/push/send/restart) yang sengaja gak diambil → report WAJIB bawa `PENDING: <action> - awaiting your authorization`.
- Bersihkan scratch files + test artifacts yang dibuat; note cleanup di report. Judge menganggap leftover debris sebagai fraud signal.
- Tawarin cuma follow-up yang muncul dari task ini (caveat yang dilist, surprise yang dicatat, scope yang dipotong). Gak ada yang muncul → tutup tanpa follow-up.
- Sebelum kirim, baca sekali sebagai hostile reviewer: claim gak terverifikasi (verify sekarang atau relabel sebagai caveat), jawaban salah shape buat Step 0, ada yang disentuh di luar scope? Fix, baru kirim.
- **Artifact gate, cek terakhir sebelum kirim.** Sweep report terhadap yang "dihutang" run ini: behavior berubah tanpa `INTENT:` → tambah; aksi outward tanpa `AUTH:` → tambah; follow-up prescribed sengaja gak diambil tanpa `PENDING:` → tambah; defect difix tanpa `TWINS:` → tambah. Gate cuma nyala kalau ada yang kurang.

## Surgical Changes (Karpathy)

Touch only what you must. Clean up only your own mess.

When editing existing code:
- Don't "improve" adjacent code, comments, or formatting
- Don't refactor things that aren't broken
- Match existing style, even if you'd do it differently
- If you notice unrelated dead code, mention it — don't delete it

When your changes create orphans:
- Remove imports/variables/functions that YOUR changes made unused
- Don't remove pre-existing dead code unless asked

The test: Every changed line should trace directly to the user's request.

Anti-patterns to catch:
- No features beyond what was asked
- No abstractions for single-use code
- No "flexibility" or "configurability" that wasn't requested
- No error handling for impossible scenarios
- If 200 lines could be 50, rewrite it
- The test: Would a senior engineer say this is overcomplicated? If yes, simplify.

## Knowledge Capture

Setiap project punya folder `knowledge/` sebagai **single source of truth**. Agent WAJIB baca entry point di `knowledge/README.md` sebelum mulai kerja.

### Kenapa `knowledge/README.md`?

- **Entry point universal** — agent manapun buka folder `knowledge/` → baca README → tau state
- **Multi-agent support** — dev-meth, uiux-meth, skill lain semua output di `knowledge/`
- **Zero tebak-tebak** — gak perlu cari file mana yang relevan
- **Konsisten** — pattern yang sama untuk semua skill

### How It Works

1. **Baca** `knowledge/README.md` dulu — tau metodologi aktif + file mana yang harus dibaca
2. **Baca** file yang disebut di README (biasanya `KNOWLEDGE.md`)
3. **Create** `knowledge/` + `knowledge/README.md` + `knowledge/KNOWLEDGE.md` di Phase 1 kalau belum ada
4. **Update** di setiap phase gate — append, never delete

### What to Capture

| Section | When Updated | What It Tracks |
|---------|-------------|----------------|
| Vision | Phase 1 | The big idea, goals, why this exists |
| Architecture | Phase 2 | Tech stack, structure, key patterns |
| Decisions | Phase 2+ | What was chosen and why (with alternatives rejected) |
| Progress | Phase 4+ | Checklist of done/blocked/todo |
| Learnings | Phase 4+ | Pitfalls, discoveries, what worked/didn't |
| Files | Phase 4+ | What was touched and why |
| Next | Phase 6 | What comes next, known issues, debt |

### Rules

- **Append only** — never rewrite or delete existing entries
- **Timestamp** — every entry gets a date prefix `[YYYY-MM-DD]`
- **Be specific** — "Used SQLite for simplicity, no server needed" not "Chose database"
- **Read on start** — first action in any session: read `knowledge/KNOWLEDGE.md`

### ⛔ HARD RULES — output WAJIB masuk `knowledge/`

Lokasi output agent **haram di luar `knowledge/`**. Berlaku untuk SEMUA artifact, dari skill apapun (dev-meth, uiux-meth, diagram-design, superpowers, dll):

1. **Satu-satunya direktori output** = `knowledge/` di root project. Artifact apa pun (diagram, riset, digest, design system, report) → `knowledge/`, subfolder boleh (`knowledge/diagrams/`, `knowledge/research/`, dst)
2. **DILARANG bikin folder baru di luar `knowledge/`** — termasuk `docs/`, `notes/`, `research/`, `artifacts/`, `superpowers/`, atau folder bernama apa pun di root project atau di dalam repo
3. **DILARANG nulis file non-standar di luar knowledge** — laporan, catatan, diagram, dump — semua masuk `knowledge/` dengan format standar (frontmatter + struktur baku kalau vault-native)
4. **Pengecualian satu-satunya**: artefak teknis yang memang wajib di-commit ke repo di luar knowledge (mis. `graphify-out/`, kode yang diminta user, config). Kalau ragu → tanya user, jangan asumsi
5. **Format file knowledge**: kalau project di dalam vault Obsidian → vault-native (frontmatter `title/tags/status/created` + wikilink). Di luar vault → markdown standar. Gak ada format lain
6. **Pelanggaran = defect**. Kalau ketemu artifact di luar knowledge → pindahkan ke `knowledge/`, lapor di report (bukan cuma dibiarin)

## Decision Tree

```
User request → Triviality gate?
├─ Trivial (1 file, <10 baris, no search, no behavior baru)
│   → kerjakan + 1 check + lapor 2 kalimat
└─ Non-trivial → Step 0: Classify ask
   ├─ Question/assessment → findings + rekomendasi, jangan ubah apa-apa
   ├─ Plan-first (scope ambigu / irreversible / minta plan)
   │   → plan + rekomendasi, stop, minta approval
   └─ Task → paham masalahnya?
       ├─ Ya → Phase 2: Spec (evidence dulu)
       └─ No → Phase 1: Understand (define done)
```

## Workflow

## Communication Rules (berlaku semua phase)

Gaya komunikasi ADHD-friendly — action first, tanpa basa-basi:

1. **Lead with the action** — apa yang berubah / apa yang harus dilakukan, baru konteks
2. **Numbered steps** — multi-step task / progress report → nomorin langkahnya
3. **End with one concrete next step** — tutup reply dengan langkah berikutnya + estimasi waktu (±menit)
4. **Restate state** — di debugging/review panjang, ulang state sekarang tiap turn biar konteks gak ilang
5. **Matter-of-fact errors** — kegagalan ditulis polos (`PENDING:` / error), tanpa pembelaan atau dramatisasi
6. **Suppress tangents** — kalau ada info sampingan, simpen di akhir sebagai "kalau perlu", jangan naruh di tengah
7. **No preamble, no recap, no closers** — langsung inti, gak usah "jadi kesimpulannya"

### Phase 1: Understand
- **Define done** (Step 1): verifikasi konkret yang bisa diobservasi, bukan "semoga bener"
- Ask clarifying questions BEFORE writing any code
- Identify: what problem, who uses it, constraints, success criteria
- Confirm understanding back to user
- **Gate:** User approves understanding before proceeding
- **Knowledge:** Create `knowledge/KNOWLEDGE.md` with Vision section

### Phase 2: Spec
- **Evidence rules** (Step 2): orient dulu, primary sources > memory, parallelize, time-box 2 round
- **Intent sebelum behavior:** kalau ada test gagal, cek statement intent dulu — test bisa yang salah, bukan cuma kode
- Write minimal spec using template below
- Show in digestible chunks (not walls of text)
- Get explicit approval before proceeding
- **Gate:** User approves spec before proceeding
- **Knowledge:** Add Architecture + Decisions sections

### Phase 3: Plan
- **Decide & commit** (Step 3): satu rekomendasi, alternatif disebut 1 baris kenapa kalah
- Break into small tasks (~15-30 min each)
- Mark dependencies between tasks
- Identify test cases per task
- Present as numbered checklist
- For each task: note existing solutions to check first
- **Gate:** User approves plan before proceeding
- **Knowledge:** Add Progress checklist (all unchecked)

### Phase 4: Implement (Ponytail Mode + Step 4)
- **INTENT gate** sebelum edit behavior; **AUTH gate** sebelum aksi irreversible/outward
- Work through tasks in order
- YAGNI strictly enforced — build only what spec says
- Each task:
  1. Check existing solutions first
  2. Implement minimal code
  3. Test
  4. Commit (atomic: one logical change)
- Prefer: native APIs > stdlib > existing packages > custom code
- Use subagents for parallel independent tasks
- **Knowledge:** Update Progress (check done items), add Learnings + Files as they emerge

### Phase 5: Test (Step 5)
- **Verify by observation** — jalankan/dilihat, bukan disimpulkan dari baca kode
- Run all tests; manual smoke test if applicable
- **Twin check** kalau fix defect — search pattern yang sama di seluruh project
- **Security scan (opsional — WAJIB tanya user dulu):** kalau task nyentuh web/API/auth/input handling, tawarkan pentest:
  1. Info user: skill `penetration-testing-with-strix` butuh install (`npx skills add usestrix/strix --skill penetration-testing-with-strix --yes`) + Docker jalan + LLM API key
  2. Kasih 2 pilihan: **[1] setup sekarang** / **[2] skip**
  3. Setup → install + jalankan; findings → `fix-security-vulnerabilities-with-strix`. Skip → lanjut, catat `PENDING: security scan di-skip - user pilih skip`
  4. Kalau setup gagal (Docker/key gak ada) → jangan maksa, jangan pura-pura scan: `PENDING: security scan gagal setup - <alasan>`
- **Hard bound:** 3 siklus fix-verify gagal → stop, hand back ke user
- Report pass/fail per task
- Verify against spec requirements
- **Knowledge:** Update Progress with test results

### Phase 6: Review + Self-Critique (Step 6)
- **Report outcome-first** — kalimat pertama jawab "jadi gimana"
- **Artifact gate:** INTENT/AUTH/PENDING/TWINS line muncul verbatim kalau kondisi terpenuhi
- **Anti-slop writing (opsional, auto-install):** kalau output task = user-facing writing (README, docs, changelog, report, blog post) → cek skill `no-ai-slop`. Belum ada? Install langsung tanpa tanya: `npx skills add petergyang/no-ai-slop --skill no-ai-slop --yes`. Lalu jalankan aturannya buat bersihin AI-slop pattern (binary contrast, throat-clearing, fake-profound, dst) sebelum teks dikirim
- Summarize what was built
- Count lines of code — celebrate low numbers
- List deviations from spec (with reasons)
- Self-critique checklist:
  - [ ] Uses native/existing solutions where possible
  - [ ] Is it minimum code needed?
  - [ ] Any "just in case" additions?
  - [ ] Could any part be a one-liner?
  - [ ] Does it solve actual problem (not imagined)?
  - [ ] Is it the simplest thing that works?
- Suggest next steps or improvements
- **Knowledge:** Add Next section with follow-ups and known issues

## Optional Dependencies

Skill-skill berikut dipakai sebagai quality gate opsional — bukan bundel, tapi referensi. Install di agent masing-masing (bukan di repo ini) biar update upstream selalu nyampe.

| Skill | Sumber | Kapan dipakai | Install | Perlu tanya user? |
|---|---|---|---|---|
| `penetration-testing-with-strix` | usestrix/strix | Phase 5: task nyentuh web/API/auth/input | `npx skills add usestrix/strix --skill penetration-testing-with-strix --yes` | ✅ WAJIB (butuh Docker + LLM API key) |
| `no-ai-slop` | petergyang/no-ai-slop | Phase 6: output user-facing writing | `npx skills add petergyang/no-ai-slop --skill no-ai-slop --yes` | ❌ gak perlu (cuma file rules) |
| `diagram-design` | ardith666/diagram-design (mirror upstream cathrynlavery) | Phase 2: diagram arsitektur/ER/data-flow buat spec. Phase 4: diagram dependency/deployment buat docs. Phase 6: redraw Mermaid/draw.io existing ke editorial | via aggregator `ardith666/agent-skills` (`./setup.sh`) | ❌ gak perlu |

Kalau skill belum terinstall dan hook kepanggil: ikuti kebijakan di atas (tanya / auto-install). Kalau gak jadi jalan → catat `PENDING:` di report, jangan di-skip diam-diam.

## Diagram Design Integration

Pakai skill `diagram-design` (39 tipe diagram editorial, output HTML+SVG self-contained, bisa redraw Mermaid/draw.io) saat dokumen butuh visual.

**Aturan output — WAJIB ke `knowledge/`:**

- **Phase 2 (Spec)** — diagram arsitektur / ER / data-flow yang dibuat = artifact spec → simpan `knowledge/diagrams/<nama>.html` + `.svg`, link dari `KNOWLEDGE.md`
- **Phase 4 (Implement)** — diagram dependency / deployment / db-schema buat docs kode → `knowledge/diagrams/`
- **Phase 6 (Review)** — redraw diagram existing (Mermaid/draw.io) → versi baru di `knowledge/diagrams/`, JANGAN nempel Mermaid mentah di README
- File diagram vault-native (frontmatter + wikilink) biar ter-indeks Obsidian, mengikuti alur Obsidian Integration

## API Robustness (kalau task nyentuh API endpoint)

Dua aturan wajib kalau task bikin/ubah endpoint — bukan opsional:

### Idempotency ID

- **Wajib di:** POST/PUT yang efeknya dobel kalau dipanggil 2x (create order, transfer, register)
- **Cara:** client kirim `Idempotency-Key` header (UUID). Server simpan key + response pertama; request berikutnya dengan key sama → return response tersimpan, jangan eksekusi ulang
- **Simpel:** simpan di tabel `idempotency(key PK, response JSON, created_at)` + TTL (misal 24 jam). Bukan logika in-memory yang hilang pas restart
- **Gak perlu:** GET/DELETE/query yang murni read

### Rate Limit

- **Wajib di:** endpoint publik atau yang butuh auth (login, register, OTP, scraping-prone)
- **Cara:** batasi per user/IP, misal fixed window: `X request / menit`. Login: 5-10/menit. API umum: 60-100/menit
- **Response:** `429 Too Many Requests` + header `Retry-After` — client tau kapan bisa coba lagi
- **Simpel:** Redis `INCR + EXPIRE`, atau middleware library (express-rate-limit, gin-limiter, dll). Jangan reinvent
- **Verifikasi (Phase 5):** test 2x lipat limit → harus dapet 429, bukan 200

Kalau task gak nyentuh API → section ini skip, gak perlu diimplement.

## Rules
- Never skip Phase 1-2 (understand + spec)
- Each phase requires user approval before next
- If user says "skip to code" — warn once, then comply
- Keep commits atomic
- Test before moving to next task
- Before writing code: "Is there a simpler way?"
- **Artifact gate:** INTENT/AUTH/PENDING/TWINS line wajib muncul verbatim di report kalau kondisi terpenuhi
- **Verify by observation:** claim harus dijalankan, bukan disimpulkan. 3 siklus gagal → stop, hand back
- **Always read `knowledge/README.md` first in any new session** — entry point
- **If `knowledge/README.md` doesn't exist, create it based on templates**
- **Always update `knowledge/` files at every phase gate**
- **⛔ HARD RULE:** semua artifact/output agent WAJIB masuk `knowledge/` — DILARANG bikin folder/file non-standar di luar `knowledge/` (lihat § Knowledge Capture → HARD RULES)

## Templates

### Knowledge Template
```markdown
# Project Knowledge

## Vision
[What are we building and why]

## Architecture
- Stack: [technologies used]
- Structure: [key directories/files]
- Patterns: [design patterns, conventions]

## Decisions
| Date | Decision | Reason | Rejected |
|------|----------|--------|----------|
| [date] | [choice] | [why] | [what else was considered] |

## Progress
- [x] [completed task]
- [ ] [pending task]
- [!] [blocked task — reason]

## Learnings
- [date] [what was discovered]

## Files
| File | Purpose | Last Changed |
|------|---------|-------------|
| [path] | [what it does] | [date] |

## Next
- [what to do next]
- [known issues]
- [technical debt]
```

### Spec Template
```markdown
## Goal
[What are we building]

## Scope
- In: [what's included]
- Out: [what's not included]

## Data Model
[entities and relationships]

## API/UI
[interfaces]

## Constraints
[performance, budget, timeline]
```

### Task Template
```markdown
- [ ] Task 1: [description]
  - Depends on: none
  - Existing solution: [what already exists]
  - Test: [how to verify]
- [ ] Task 2: [description]
  - Depends on: Task 1
  - Existing solution: [what already exists]
  - Test: [how to verify]
```

## Obsidian Integration (vault-aware)

Modul aktif saat CWD ada di dalam **vault Obsidian** (folder `.obsidian/` di CWD atau parent) atau user minta pakai Obsidian. Referensi lengkap: `references/obsidian/` di skill ini — `README.md` = gateway (filosofi, 4 alur retain, retention policy, dependency & self-healing), `markdown.md` / `bases.md` / `canvas.md` / `cli.md` / `defuddle.md` = detail sintaks.

### Prinsip

1. **Vault-native writing** — semua note/knowledge di vault ditulis dengan frontmatter (`title`, `tags`, `status`, `created`), `[[wikilinks]]` untuk rujukan antar-note, `#tag` taksonomi, callout untuk info penting, embed `![[...]]` untuk reuse. Bukan plain markdown.
2. **Empat alur retain** — mencatat, merangkum (defuddle → distilasi → note), mengkoneksikan (wikilink/base/canvas), meretain (append-only + timestamp). Detail: `references/obsidian/README.md`.
3. **Retention restraint** — HANYA tulis continuity artifacts: keputusan, learning, status, ringkasan bahan yang di-ingest, index/bases/canvas, update `knowledge/`. JANGAN buat catatan penuh milik user.
4. **Progressive disclosure** — `SKILL.md` ini tetap ringkas; baca `references/obsidian/*` hanya saat fitur dibutuhkan.

### Hook per phase

- **Phase 1** — baca vault dulu (note terkait/backlink; `obsidian search` kalau CLI ada). Mulai note project dengan frontmatter.
- **Phase 2** — evidence: orient vault duluan; hasil riset web via `defuddle parse <url> --md` → ringkas → simpan note → wikilink ke note project.
- **Phase 3** — kalau task list berulang/progress di-track, buat `tracker.base` (lihat bases.md).
- **Phase 4** — update `knowledge/` Vault-native + status di tracker base.
- **Phase 5** — catat hasil test (pass/fail/skip) ke note status, berbasis observasi.
- **Phase 6** — entry append-only `[YYYY-MM-DD]` di `knowledge/history.md`; tulis `Next` + sambungkan via wikilink; kalau proyek punya relasi yang bisa divisualkan → buat/update `.canvas`. Verifikasi health graph setelahnya: `obsidian unresolved` + `obsidian orphans` (aturan di `references/obsidian/README.md` § Vault Hygiene).

Knowledge Capture di atas tetap berlaku; perbedaannya: saat di vault, semua file `knowledge/*` ikut **vault-native** (frontmatter + wikilinks + tags) supaya ter-retain & terindeks Obsidian.

### Dependency & Self-Healing

Cek-req → **tanya user → bantu deploy → verify**. Kurang sesuatu (Obsidian app, CLI belum enabled, PATH, defuddle, node)? Pakai tabel + perintah di `references/obsidian/README.md`. Aksi sistem (npm install -g, ubah shell rc, symlink) butuh AUTH. Gagal → pakai yang tersedia (file ops selalu jalan), fitur yang kurang di-skip dan dicatat `PENDING:`.

## Graphify Integration (codebase intelligence)

Modul aktif saat bekerja di codebase yang punya `graphify-out/` (knowledge graph) atau saat perlu memahami arsitektur project — **map dulu, query, bukan grep**. Referensi: `references/graphify/README.md` (filosofi, perintah inti, dependensi & self-healing, atribusi Graphify-Labs).

### Prinsip

1. **Query-first** — kalau project punya graph, tanya `graphify query` / `path` / `explain` dulu sebelum baca file satu-satu. Jangan grep kalau graph sudah ada.
2. **Local-first** — AST tree-sitter, 0 token LLM untuk kode (docs/media baru butuh model). `--code-only` = offline penuh.
3. **Honest audit trail** — edge berlabel `EXTRACTED` (eksplisit) / `INFERRED` (resolusi graphify); jangan tampilkan INFERRED sebagai fakta.
4. **Graph harus segar** — setelah ngoding, `graphify update .` (atau andalkan `graphify hook install`). Query graph basi = informasi salah.
5. **Hasil → `knowledge/`** — semua hasil sesi (digest graph, temuan, ringkasan GRAPH_REPORT) masuk folder `knowledge/`; jangan buat file hasil di luar folder itu (satu-satunya pengecualian: artefak teknis `graphify-out/` yang wajib di-commit ke repo).

### Git: commit vs ignore `graphify-out/`

Saat commit repo project, split file `graphify-out/`:

**Commit (output grafis/navigasi + state lintas-mesin):**
- `graph.json`, `graph.html`, `GRAPH_REPORT.md`, `manifest.json`, `cost.json`, `.graphify_labels.json`

**Ignore (state mesin lokal + cache build — regenerable, path absolut beda per mesin):**

```gitignore
# graphify local machine state + build cache
graphify-out/cache/
graphify-out/.graphify_python
graphify-out/.graphify_root
```

Alasan: `.graphify_python`/`.graphify_root` berisi path absolut interpreter & root **mesin lokal** (bocor struktur lokal + patah di mesin lain); `cache/` = cache build internal (2MB+, beda isi per environment). Graphify skill punya interpreter-guard — kalau `.graphify_python` hilang, ia re-resolve otomatis. Terapkan blok `gitignore` ini di AGENTS.md/README project setelah generate graph pertama.

### Hook per phase

- **Phase 1** — kalau `graphify-out/` ada: buka dengan `graphify query "arsitektur ..."` / `explain` sebelum membaca file. Belum ada → tawarkan `/graphify .` (jalankan diagram pakai skill graphify).
- **Phase 2** — evidence: `graphify path "A" "B"` buat melacak alur antar konsep saat riset kode existing; `graphify add <url>` untuk paper/video. Catat temuan ke `knowledge/`.
- **Phase 4** — setelah implementasi signifikan: `graphify update .` biar graph nyambung dengan kode baru.
- **Phase 6** — verifikasi: `graphify update .` + pastikan `GRAPH_REPORT.md` mencerminkan struktur final; tulis summary & lessons ke `knowledge/` (ikut format knowledge timeline/decision).

### Dependency & Self-Healing

Cek-req → **tanya user → bantu deploy → verify.** Perlu `uv tool install graphifyy` (CLI `graphify`, PATH `~/.local/bin`) + `graphify install --platform agents` (skill global) — aksi install butuh AUTH. **Prompt ke user ada di `references/graphify/README.md`** (cek-req, prompt AUTH, deploy & verify) — ikuti itu saat mesin belum punya graphify. Gagal → grep/manual file ops seperti biasa, dicatat `PENDING:` di `knowledge/`.

## Knowledge Tracking

Setiap agent yang kerja pakai metodologi ini WAJIB baca & tulis knowledge files. Tujuannya:
- Agent lain bisa lanjutin pekerjaan tanpa tanya ulang
- User bisa pakai structured notes buat Obsidian atau workflow lain
- Keputusan & alasan di-skip/delay terdokumentasi

### Knowledge Files

| File | Isi | Wajib? |
|------|-----|--------|
| `knowledge/history.md` | Timeline pekerjaan (implementasi, skip, decision) | ✅ Ya |
| `knowledge/ideas.md` | Ide yg dipertimbangkan tapi belum dikerjakan | ⬜ Opsional |
| `knowledge/external-references.md` | Link/docs/repo yg dibaca | ⬜ Opsional |

### Flow Wajib

**Sebelum mulai kerja:**
1. Baca `knowledge/history.md` — tau state terakhir
2. Baca `knowledge/ideas.md` — cek ide yg mungkin relevan
3. Kalau knowledge menunjukkan progress sebelumnya, skip phase yg udah selesai

**Setelah tiap phase selesai:**
1. Tulis entry ke `knowledge/history.md`
2. Format entri:
   - Timestamp, feature name, status
   - Decision (implement/skip/delay/drop) + alasan singkat
   - Next steps
3. Max 5 baris per entri — ringkas, no filler

### Format Entri

**Implementation log:**
```
- [YYYY-MM-DD HH:MM] [feature/name]: [ringkasan]
  - Code: [X] lines | Tests: [Y] | Commit: [hash]
  - Status: ✅/❌/⚠️
  - Decision: implement/skip/delay
  - Reason: [alasan singkat]
  - Next: [langkah selanjutnya]
```

**Skipped item:**
```
- [YYYY-MM-DD HH:MM] [idea/feature]: dipertimbangkan, di-skip
  - Value: [kenapa sempat dipertimbangkan]
  - Decision: skip/delay
  - Reason: [alasan spesifik]
  - Might revisit: [kapan/kalau]
```

**Decision entry:**
```
- [YYYY-MM-DD HH:MM] Decision: [implement/skip/delay]
  - Problem: [apa yg dicoba dipecahkan]
  - Options: [pilihan yg dipertimbangkan]
  - Chosen: [apa yg dipilih]
  - Why: [alasan spesifik]
```

### Aturan Penulisan

- **Brevity**: Satu entri max 5 baris
- **Akurat**: Timestamp, feature name, status jelas
- **Action-oriented**: Fokus action, bukan deskripsi task
- **No filler**: Hindari "then I", "after that", "finally"
- **Multi-purpose**: Format markdown terstruktur → user bisa copy-paste ke Obsidian, Notion, atau workflow lain

### Integrasi per Phase

| Phase | Action Knowledge |
|-------|-----------------|
| Phase 1 Understand | Baca `knowledge/README.md` dulu. Create `knowledge/` kalau belum ada |
| Phase 2 Spec | Catat decision dari spec |
| Phase 3 Plan | Catat breakdown task + dependencies |
| Phase 4 Implement | Tulis entry setelah tiap commit |
| Phase 5 Test | Catat test results (pass/skip/fail) |
| Phase 6 Review | Tulis summary + lessons learned |

### Example

Agent mulai tugas "Buat JWT auth endpoint":

1. Baca `knowledge/README.md` → tau state + metodologi
2. Baca `knowledge/KNOWLEDGE.md` → belum ada auth work sebelumnya
2. Tulis decision:
```
- [2026-07-21 11:00] Decision: implement JWT auth endpoint
  - Problem: Endpoint perlu authenticated access
  - Options: OAuth2, JWT stateless, session cookie
  - Chosen: JWT stateless
  - Why: Simpel, scalable, stateless
```
3. Implement & tulis:
```
- [2026-07-21 11:30] JWT auth endpoint:
  - Code: 47 lines | Tests: 3 | Commit: abc123
  - Status: ✅
  - Decision: implement
  - Reason: JWT middleware + protected routes
  - Next: Integration test
```
4. Agent selanjutnya langsung tau state & bisa lanjut
