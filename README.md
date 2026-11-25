# Discovery Evidence Map

A portable workflow for mapping discovery records to disputed facts, witnesses and requests without mistaking a search result for proof. The example is entirely fictional and runs offline; there is no account, service, package installation, or AI integration required.

## Try it in two commands

From the repository root, with Python 3.11 or later:

```sh
python3 -B examples/demo.py
python3 -B -m unittest discover -s tests -v
```

The demo uses an in-memory SQLite database. It first checks the bytes and cited excerpts of three fictional originals, then prints one disputed proposition's observations and one request with no indexed source link. Open [the dispatch record](examples/originals/dispatch-log.txt) and [the gate record](examples/originals/gate-log.txt) to see why their timestamps cannot settle the proposition. [The witness note](examples/originals/witness-notes.txt) describes a firsthand observation but supplies no time.

- [AI workflow instructions](SKILL.md)
- [White paper](docs/WHITE-PAPER.md)
- [Lawyer guide](docs/LAWYER-GUIDE.md)
- [Schema](examples/schema.sql) and [queries](examples/queries.sql)

The software is a starter example, not a production review platform, legal advice, a security certification, or a substitute for counsel's review. Do not add actual case materials to this repository or put them in Git history, examples, issue reports or screenshots.


## Downloads

- [White paper (PDF)](docs/discovery-evidence-map-white-paper.pdf)
- [Lawyer’s guide (PDF)](docs/discovery-evidence-map-lawyer-guide.pdf)
- [Skill](SKILL.md)
- [Apache License 2.0](LICENSE)
