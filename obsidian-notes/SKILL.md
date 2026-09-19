---
name: obsidian-notes
description: Write every note in the iCloud Obsidian vault with consistent Obsidian Flavored Markdown — frontmatter, wikilinks, callouts, INDEX.md hubs, per-project LOG.md. Use for any .md note inside the vault.
metadata:
  openclaw:
    emoji: "💎"
---

# Obsidian Notes

Vault: `~/Library/Mobile Documents/iCloud~md~obsidian/Documents/Obsidian Vault` (iCloud sync, **NOT** a git repo — no push). Applies to every agent writing notes in the vault.

## Steps

1. **Check syntax reference first** — for OFM details read the `obsidian-markdown` skill.
2. **Add frontmatter** — every note starts with a `---` block: `title`, `tags`, `date` (+ `aliases` when alternative names exist). Tags lowercase, project-scoped (`iticm`, `discord`).
3. **Link internal notes with wikilinks** — `[[Note]]`, `[[Note#Heading]]`, `[[Note|text]]`. Never use file paths for internal links.
4. **Link external URLs with markdown links** — `[text](https://...)`. Never wikilink external URLs.
5. **Use callouts for important info** — `> [!note]`, `> [!tip]`, `> [!warning]`.
6. **Connect new notes to the graph** — every new note must be linked from a nearby index/note with `[[...]]`.
7. **Maintain per-folder INDEX.md** — every note collection folder has an `INDEX.md` hub linking all notes inside it.
8. **Log work per project** — chronological `LOG.md` in the project folder; append newest at the bottom.
9. **Write via full absolute path** — listing the vault often fails (TCC → `EPERM`). Write/read files using the complete path; do not rely on `ls` of the vault.

## Pitfalls

- Vault folder listing returns `EPERM: operation not permitted` — that is TCC, not a missing file. Write directly to the known full path.
- iCloud sync means no git history inside the vault: don't `git push` from there; version control lives elsewhere (e.g., skill repos).
- Keep `LOG.md` chronological — append, never reorder.
- New note with no incoming/outgoing link breaks the graph view — always connect it.