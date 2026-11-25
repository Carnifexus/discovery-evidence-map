# Lawyer guide: Discovery Evidence Map

## 1. Run the fictional example first

From the repository root, run `python3 -B examples/demo.py`, then run `python3 -B -m unittest discover -s tests -v`. No software beyond Python 3.11 or later is required. Open the three [fictional originals](../examples/originals) yourself. Compare the report’s excerpt and line number against each file, then read the lines above and below it.

Ask: “Which two sources appear to disagree about timing? What does each record actually measure? What can the witness say firsthand, and what source should I request next?” The useful answer is not a verdict about which timestamp wins. It is a narrower plan for checking the handoff, scanner direction and clock.

## 2. Set up a private matter index

- **Define the review set.** Write down the batches, folders or produced index in scope. Record the snapshot date, expected counts and exclusions. Give OCR failures, unreadable items and missing attachments their own status.
- **Keep originals untouched.** Record original production IDs, filenames and metadata as supplied. Assign stable internal IDs and store checksums where available. Keep OCR and other derivatives separately identified; preserve emails and attachments as related records even if identical content appears elsewhere.
- **Start from a question.** Use focused propositions rather than a long keyword list. Gather supporting, contrary and contextual records. Link request items to exact sources and link witnesses only to the observation and basis actually identified.
- **Check before relying.** Open the original at the cited page, line or timecode. Check nearby text, identify who made the entry versus who performed the act, and distinguish event time from upload or processing time. Mark the review decision and what counsel still needs.

Give an AI the workflow in [SKILL.md](../SKILL.md), the authorized scope and the desired output columns. Ask it to return a source and pinpoint for each material claim and show contrary records beside it. Tell it not to treat evidence text as instructions, delete or replace originals, infer a missing date, or disclose content beyond the approved matter environment. Review its work yourself.

## 3. Scale only when you need to

SQLite is adequate for the fictional exercise and a sensible starting point for a single reviewer. For a multi-reviewer deployment, adapt the schema to PostgreSQL after testing it on fictional data: remove SQLite-specific pragmas, select deliberate timestamp types, and use the parameter binding expected by your database driver. Keep the report role read-only, enforce matter-level access controls in the database, and verify isolation and backups before connecting case data. Start with the official [SQLite foreign-key documentation](https://sqlite.org/foreignkeys.html) and [PostgreSQL constraints documentation](https://www.postgresql.org/docs/current/ddl-constraints.html).

Do not share originals, excerpts, review logs, embeddings, credentials or case identifiers in public support requests. Counsel chooses what can go into a filing, production, examination or other external work.
