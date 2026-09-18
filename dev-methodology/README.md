<p align="center">
<pre align="center">
______   _______                  _______  _______ _________         
(  __  \ (  ____ \|\     /|       (       )(  ____ \\__   __/|\     /|
| (  \  )| (    \/| )   ( |       | () () || (    \/   ) (   | )   ( |
| |   ) || (__    | |   | | _____ | || || || (__       | |   | (___) |
| |   | ||  __)   ( (   ) )(_____)| |(_)| ||  __)      | |   |  ___  |
| |   ) || (       \ \_/ /        | |   | || (         | |   | (   ) |
| (__/  )| (____/\  \   /         | )   ( || (____/\   | |   | )   ( |
(______/ (_______/   \_/          |/     \|(_______/   )_(   |/     \|
</pre>
</p>

<p align="center" style="margin-top: -20px;">
  <b>Structured workflow + minimal code + Fable evidence loop + persistent knowledge</b><br>
  <i>For AI coding agents that forget nothing — and verify everything.</i>
</p>

<p align="center">
  <a href="#quick-start">Quick Start</a> •
  <a href="#the-workflow">Workflow</a> •
  <a href="#the-fable-loop">Fable Loop</a> •
  <a href="#installation">Installation</a> •
  <a href="#knowledge-portability">Knowledge</a>
</p>

---

## Why This Exists

AI coding agents are powerful but make predictable mistakes:

```
 ❌ Over-engineering      → building abstractions nobody asked for
 ❌ Silent assumptions    → picking interpretations without asking
 ❌ Scope creep           → refactoring adjacent code during changes
 ❌ Skipping understanding→ jumping straight to code
 ❌ Context loss          → forgetting everything between sessions
 ❌ Claiming success      → "all tests pass" without actually running them
```

**Dev Methodology** fixes all six — with one workflow, one evidence loop, and one verification discipline.

---

## The DNA

Six sources, six problems solved:

```
 ┌─────────────────────────────────────────────────────────────────────┐
 │                         DEV METHODOLOGY                            │
 ├──────────────┬──────────────┬──────────────┬───────────────────────┤
 │ SUPERPOWERS  │  PONYTAIL    │  ANTHROPIC   │      KARPATHY         │
 │              │              │   SKILLS     │                       │
 │  🕐 WHEN     │  📏 HOW MUCH │  🏗️ HOW      │  🔪 WHERE             │
 │              │              │              │                       │
 │  Workflow    │  Minimal     │  Decision    │  Surgical changes —   │
 │  order       │  code        │  trees +     │  touch only what's    │
 │  (gates at   │  philosophy  │  checklists  │  needed               │
 │  every phase)│              │              │                       │
 └──────────────┴──────────────┴──────────────┴───────────────────────┘
        +                     +                            +
 ┌──────────────┐    ┌──────────────────┐      ┌──────────────────────┐
 │  📚 KNOWLEDGE│    │  🔍 FABLE        │      │  📏 TRIVIALITY GATE  │
 │              │    │                  │      │                      │
 │  Persistent  │    │  Evidence loop:  │      │  <10 baris, 1 file,  │
 │  project     │    │  classify →      │      │  no search → skip    │
 │  context     │    │  done → evidence │      │  the 6 phases,       │
 │  across      │    │  → decide → act  │      │  do it + 1 check     │
 │  sessions    │    │  → verify →      │      │                      │
 │              │    │  report          │      │                      │
 └──────────────┘    └──────────────────┘      └──────────────────────┘
```

Fable (from [fable-method](https://github.com/Sahir619/fable-method)) answers *"how do we know each step really happened?"* — the loop turns every claim into something observed, and every report into something auditable. Dev Methodology answers *"what are we building, in what order?"* — the phases, gates, and knowledge capture. The two are orthogonal; this skill runs both.

---

## The Workflow

```
  ┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐
  │          │    │          │    │          │    │          │    │          │    │          │    │          │
  │ 1.UNDER- │───▶│ 2.SPEC   │───▶│ 3.PLAN   │───▶│ 4.IMPLE- │───▶│ 5.TEST   │───▶│ 6.REVIEW │───▶│ 7.KNOW-  │
  │  STAND   │    │          │    │          │    │  MENT    │    │          │    │          │    │  LEDGE   │
  │          │    │          │    │          │    │          │    │          │    │          │    │          │
  └────┬─────┘    └────┬─────┘    └────┬─────┘    └────┬─────┘    └────┬─────┘    └────┬─────┘    └────┬─────┘
       │               │               │               │               │               │               │
       ▼               ▼               ▼               ▼               ▼               ▼               ▼
  ┌─────────┐    ┌─────────┐    ┌─────────┐    ┌─────────┐    ┌─────────┐    ┌─────────┐    ┌─────────┐
  │  GATE:  │    │  GATE:  │    │  GATE:  │    │PONYTAIL │    │VERIFY   │    │  SELF-  │    │ CAPTURE │
  │ approve │    │ approve │    │ approve │    │ minimal │    │ by      │    │ CRITIQUE│    │ context │
  │ before  │    │ before  │    │ before  │    │ code +  │    │ observ- │    │ + low   │    │ to file │
  │ next    │    │ next    │    │ next    │    │ INTENT/ │    │ ation + │    │ LOC     │    │         │
  │         │    │         │    │         │    │ AUTH    │    │ TWINS   │    │         │    │         │
  └─────────┘    └─────────┘    └─────────┘    └─────────┘    └─────────┘    └─────────┘    └─────────┘
       │               │               │               │               │               │               │
       ▼               ▼               ▼               ▼               ▼               ▼               ▼
   📚 Vision      📚 Arch +      📚 Progress    📚 Progress    📚 Progress    📚 Next        ✅ Done
                   Decisions      (unchecked)    (check done)   (results)      (follow-ups)
```

> Every phase auto-updates `knowledge/KNOWLEDGE.md`. New sessions read it first → **zero context loss**.
> Every phase runs inside the Fable loop below → **zero unverified claims**.

---

## The Fable Loop

Setiap tugas non-trivial dijalankan lewat loop ini. Loop menyatu dengan phase — bukan lapisan terpisah:

```
                     ┌────────────────────────────────────────────────────────────┐
                     │                        FABLE LOOP                          │
                     │                                                            │
 ask ──► ┌────────┐ ┌┴─────────┐ ┌──────────┐ ┌──────────┐ ┌─────────┐ ┌────────┐ ┌┴────────┐
         │TRIVIAL?│ │0 CLASSIFY│ │1 DEFINE  │ │2 EVIDENCE│ │3 DECIDE │ │4 ACT   │ │5 VERIFY │
         │1 file, │ │question/ │ │DONE      │ │orient →  │ │satu     │ │INTENT  │ │by       │
         │<10 baris││task/plan-│ │verifikasi │ │primary → │ │rekomend-│ │gate +  │ │observ-  │
         │no search│ │first?    │ │konkret   │ │parallel →│ │asi +    │ │AUTH    │ │ation +  │
         └───┬─────┘ └────┬─────┘ └────┬─────┘ └────┬─────┘ └────┬────┘ └───┬────┘ └────┬────┘
             │yes         │            │            │            │          │          │
             ▼            │            │            │            │          │          │
      kerjakan + 1 check  │            │            │            │          │          │
      + lapor 2 kalimat   │            │            │            │          │          │
                          │            │            │            │          │          ▼
                          │            │            │            │          │      ┌─────────┐
                          │            │            │            │          │      │6 REPORT │
                          │            │            │            │          │      │outcome- │
                          │            │            │            │          │      │first +  │
                          │            │            │            │          │      │artifact │
                          │            │            │            │          │      │gate     │
                          └────────────┴────────────┴────────────┴──────────┴──────┴─────────┘
                                        (non-trivial → loop penuh, 0 → 6)
```

### Phase ↔ Fable mapping

| Fable step | Isi | Hook ke phase |
|---|---|---|
| 0 · Classify | question / task / plan-first? Tie-break: plan-first menang | Sebelum Phase 1 — gate masuk |
| 1 · Define done | verifikasi konkret yang bisa diobservasi, bukan "semoga bener" | Phase 1 · Understand |
| 2 · Evidence | orient dulu, primary sources > memory, parallelize, time-box 2 round | Phase 2 · Spec |
| 3 · Decide | satu rekomendasi, alternatif disebut 1 baris kenapa kalah | Phase 3 · Plan |
| 4 · Act | INTENT gate + AUTH gate + recall gate, surgical, smallest change | Phase 4 · Implement |
| 5 · Verify | dijalankan/dilihat, twin check, hard bound 3 siklus → stop | Phase 5 · Test |
| 6 · Report | outcome-first, caveat jujur, artifact gate (INTENT/AUTH/PENDING/TWINS) | Phase 6 · Review |

---

## Quick Start

```bash
# Clone the skill
git clone https://github.com/ardith666/dev-methodology.git

# Copy to your project
cp dev-methodology/SKILL.md your-project/

# Or install globally (OpenCode)
cp dev-methodology/SKILL.md ~/.agents/skills/dev-methodology/SKILL.md
```

Then just say: **"dev mode"** or ask to build something.

## Obsidian Integration

Modul `references/obsidian/*` = cara skill ini terhubung ke vault Obsidian: **mencatat, merangkum (defuddle), mengkoneksikan (wikilink/base/canvas), meretain** pengetahuan lintas sesi & lintas mesin.

- Saat bekerja di dalam vault → semua `knowledge/*` ditulis **vault-native** (frontmatter + wikilinks + tags) + update tracker/base/canvas sesuai phase.
- **Dependency self-healing** — kurang Obsidian / CLI / defuddle / node → tanya user → bantu deploy → verify. Detail: `references/obsidian/README.md`.
- Setup per mesin: `git pull` skill repo + `npm install -g defuddle` + enable Obsidian CLI (Settings → General → Advanced).
- Konten diadaptasi dari [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) (MIT).

## Version

Current: **v3.1.1** (lihat `VERSION` + tag repo)

- v3.1.1 — **Graphify gitignore rule**: panduan commit-vs-ignore `graphify-out/` (commit graph.json/html/GRAPH_REPORT/manifest/cost/labels; ignore `cache/`, `.graphify_python`, `.graphify_root`); blok gitignore utk terapkan di repo project
- v3.1.0 — **Graphify Integration** (modul baru `references/graphify/`): knowledge graph codebase (extract/query/path/explain, offline `--code-only`), query-first di Phase 1/2/4/6; aturan hasil → `knowledge/`; cara instalasi & deploy per mesin + prompt AUTH ke user
- v3.0.1 — **Vault Hygiene** (`references/obsidian/README.md`): graph check `unresolved`/`orphans` + 7 aturan dari audit nyata; hook Phase 6 verifikasi health graph
- v3.0.0 — **Obsidian Integration Module** (`references/obsidian/*`): vault-native capture, 4 retention flows (mencatat/merangkum/mengkoneksikan/meretain), dependency self-healing, `version:` di frontmatter SKILL.md
- v2.3.0 — (tag sebelumnya)
- v1.3.0 — API Robustness section (idempotency key + rate limit)
- v1.2.1 — README: version history + optional deps
- v1.2.0 — Communication rules (ADHD-friendly, berlaku semua phase)
- v1.1.0 — no-ai-slop hook Phase 6 + Strix ask-user policy + optional dependencies table
- v1.0.0 — Baseline: dev-methodology + Strix security skills (Phase 5 optional hook)

Cek update: `git fetch --tags && git tag -l` — versi terbaru = tag tertinggi. Agent di mesin lain: bandingkan `version:` frontmatter lokal dengan tag remote.

## Optional Dependencies

Quality gate opsional — bukan bundel, referensi. Install di agent (bukan di repo ini) biar update upstream selalu nyampe:

| Skill | Sumber | Kapan dipakai | Install | Perlu tanya user? |
|---|---|---|---|---|
| `penetration-testing-with-strix` | usestrix/strix | Phase 5: task nyentuh web/API/auth/input | `npx skills add usestrix/strix --skill penetration-testing-with-strix --yes` | ✅ WAJIB (butuh Docker + LLM API key) |
| `no-ai-slop` | petergyang/no-ai-slop | Phase 6: output user-facing writing | `npx skills add petergyang/no-ai-slop --skill no-ai-slop --yes` | ❌ gak perlu (cuma file rules) |

Kalau skill belum terinstall dan hook kepanggil: ikuti kebijakan (tanya / auto-install). Gak jadi jalan → catat `PENDING:` di report, jangan di-skip diam-diam.

---

## Knowledge Portability

Your `knowledge/KNOWLEDGE.md` is **plain markdown** — own the data, export anywhere:

```
 knowledge/
 ├── knowledge/KNOWLEDGE.md  ← single source of truth
 │
 ├──▶ Obsidian    → copy folder into vault (wikilinks work instantly)
 ├──▶ Notion      → import as page (tables + checklists render natively)
 ├──▶ GitHub      → commit with code (renders in repo)
 ├──▶ GitBook     → add to docs folder (structure compatible)
 └──▶ Any editor  → it's just markdown
```

**No vendor lock-in. No export scripts.**

---

## What Each Phase Does

### Communication Rules (berlaku semua phase)

ADHD-friendly output — action first, tanpa basa-basi:

1. **Lead with the action** — apa yang berubah / yang harus dilakukan, baru konteks
2. **Numbered steps** — multi-step task / progress report → nomorin langkahnya
3. **End with one concrete next step** — tutup reply dengan langkah berikutnya + estimasi waktu (±menit)
4. **Restate state** — di debugging/review panjang, ulang state sekarang tiap turn
5. **Matter-of-fact errors** — kegagalan polos (`PENDING:` / error), tanpa pembelaan
6. **Suppress tangents** — info sampingan simpen di akhir, jangan di tengah
7. **No preamble, no recap, no closers** — langsung inti

### Phase 1: Understand 🤔 — *define done dulu*
```
 Classify ask (Step 0) → Define done (Step 1) → Ask questions → Confirm
 └─ Verifikasi: observasi konkret ("test ini pass", "halaman ini render")
 └─ 📚 Create knowledge/KNOWLEDGE.md with Vision section
```

### Phase 2: Spec 📝 — *evidence dulu*
```
 Orient project → Evidence (Step 2): primary sources, parallel, time-box
 → Intent check: kalau ada test gagal, cek spec/README dulu (test bisa yang salah)
 → Write minimal spec → Show in chunks → Get approval
 └─ 📚 Add Architecture + Decisions sections
```

### Phase 3: Plan 📋 — *satu rekomendasi*
```
 Decide & commit (Step 3): satu rekomendasi, alternatif 1 baris kenapa kalah
 → Break into tasks → Mark dependencies → Identify test cases
 → AUTH gate kalau ada aksi irreversible/outward-facing
 └─ 📚 Add Progress checklist (all unchecked)
```

### Phase 4: Implement ⚡ — *surgical + gates*
```
 INTENT gate: "code does X; check expects Y; spec says Z" — wajib sebelum edit behavior
 → AUTH gate: aksi outward butuh quote user sendiri
 → Check existing → Implement minimal → Test → Commit
 └─ 📚 Update Progress, add Learnings + Files
```

### Phase 5: Test ✅ — *verify by observation*
```
 Jalankan, bukan baca kode. Twin check: habis fix defect, search pattern yang sama
 → Run all tests → Manual smoke test → Report pass/fail
 → Security scan (opsional — WAJIB tanya user dulu): task nyentuh web/API/auth/input
   → tawarkan skill penetration-testing-with-strix (butuh Docker + LLM API key)
   → user pilih: [1] setup sekarang / [2] skip. Skip/gagal → catat PENDING: di report
 → Hard bound: 3 siklus gagal → stop, hand back ke user
 └─ 📚 Update Progress with test results
```

### Phase 6: Review 🎯 — *outcome-first + artifact gate*
```
 Kalimat pertama = "jadi gimana". Caveat jujur. Artifact gate:
 INTENT: line muncul kalau behavior berubah | AUTH: kalau aksi outward diambil
 PENDING: kalau follow-up prescribed sengaja gak diambil | TWINS: kalau defect difix
 → Anti-slop writing (opsional, auto-install): output user-facing writing
   (README/docs/changelog/report) → cek & install skill no-ai-slop kalau belum ada
   → jalankan aturannya sebelum teks dikirim
 → Summarize → Count LOC → Self-critique checklist
 └─ 📚 Add Next section with follow-ups
```

---

## Core Principles

## API Robustness

Kalau task bikin/ubah API endpoint, dua aturan wajib (bukan opsional):

**Idempotency ID** — POST/PUT yang efeknya dobel kalau dipanggil 2x:
- Client kirim `Idempotency-Key` header (UUID) → server simpan key + response pertama
- Request sama dengan key yang sama → return response tersimpan, jangan eksekusi ulang
- Simpen di tabel `idempotency(key PK, response, created_at)` + TTL, bukan in-memory

**Rate Limit** — endpoint publik/auth (login, register, OTP, scraping-prone):
- Batasi per user/IP: login 5-10/menit, API umum 60-100/menit
- Response `429` + header `Retry-After`
- Pakai Redis INCR+EXPIRE atau middleware library — jangan reinvent
- Verifikasi Phase 5: test 2x lipat limit → harus 429

Kalau task gak nyentuh API → section ini skip.

---

### 🎯 Minimal Code (Ponytail)
```
 Before writing ANY code:
   1. Does this need to exist at all?
   2. Does a library/tool already solve this?
   3. Does the platform have it natively?
   4. Can it be one line?
   5. Only then write code.
```

### 🔪 Surgical Changes (Karpathy)
```
 When editing existing code:
   ✗ Don't "improve" adjacent code
   ✗ Don't refactor things that aren't broken
   ✓ Match existing style
   ✓ Every changed line traces to user's request
```

### 🚦 Phase Gates (Superpowers)
```
 Each phase requires user approval.
 No skipping ahead (without a warning).
```

### 🔍 Fable Evidence Loop (fable-method)
```
 Setiap claim harus diobservasi, bukan disimpulkan.
 INTENT / AUTH / PENDING / TWINS line wajib verbatim kalau kondisinya terpenuhi.
 Test gagal = 2 tersangka: kode ATAU check-nya. Cek spec dulu, jangan asal fix.
 3 siklus fix-verify gagal → STOP, hand back, jangan ngotot.
```

---

## Installation

<details>
<summary><b>Claude Code</b></summary>

```bash
# Option A: Project root
curl -o CLAUDE.md https://raw.githubusercontent.com/ardith666/dev-methodology/main/SKILL.md

# Option B: Append to existing
echo "" >> CLAUDE.md
curl https://raw.githubusercontent.com/ardith666/dev-methodology/main/SKILL.md >> CLAUDE.md

# Option C: Plugin
/plugin install dev-methodology@ardith666/dev-methodology
```
</details>

<details>
<summary><b>OpenCode</b></summary>

```bash
# Project-level
cp SKILL.md .opencode/instructions.md

# Global
cp SKILL.md ~/.agents/skills/dev-methodology/SKILL.md
```
</details>

<details>
<summary><b>Cursor</b></summary>

```bash
mkdir -p .cursor/rules
cp SKILL.md .cursor/rules/dev-methodology.mdc
```
</details>

<details>
<summary><b>GitHub Copilot</b></summary>

```bash
mkdir -p .github
cp SKILL.md .github/copilot-instructions.md
```
</details>

<details>
<summary><b>Hermes</b></summary>

```bash
curl -o .hermes/skills/dev-methodology.md https://raw.githubusercontent.com/ardith666/dev-methodology/main/SKILL.md
```
</details>

<details>
<summary><b>Pi Agent</b></summary>

```bash
cp SKILL.md ~/.pi/skills/dev-methodology.md
```
</details>

<details>
<summary><b>Factory Droid / Kimi / Codex / Other</b></summary>

```bash
# Factory Droid
droid plugin install https://github.com/ardith666/dev-methodology

# Kimi Code
/plugins → Search: dev-methodology → Install

# Codex
/plugins → Search: dev-methodology → Install

# Any tool: copy SKILL.md to system prompt / AGENTS.md / .cursorrules
```
</details>

---

## Quality Checklist

After every implementation:

```
 [ ] Uses native/existing solutions where possible
 [ ] Is it minimum code needed?
 [ ] Any "just in case" additions?
 [ ] Could any part be a one-liner?
 [ ] Does it solve actual problem (not imagined)?
 [ ] Is it the simplest thing that works?
 [ ] Every changed line traces to user's request
 [ ] Would a senior engineer say this is overcomplicated?
 [ ] Setiap claim diverifikasi by observation — bukan dibaca dari kode
 [ ] INTENT/AUTH/PENDING/TWINS line ada kalau kondisi terpenuhi (artifact gate)
 [ ] Caveat jujur: apa yang di-skip, masih lemah, gak bisa diverifikasi
```

---

## License

MIT
