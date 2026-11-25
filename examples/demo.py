"""Offline fictional evidence-map demonstration. No input arguments, network, or writes."""
from contextlib import closing
from pathlib import Path
import hashlib
import json
import sqlite3

HERE = Path(__file__).resolve().parent


def read_original(root, relpath):
    path = (root / relpath).resolve(strict=True)
    if not path.is_relative_to((root / "originals").resolve(strict=True)):
        raise ValueError("Fixture outside originals")
    return path.read_bytes()


def open_demo(root=HERE):
    root = root.resolve()
    db = sqlite3.connect(":memory:")
    db.row_factory = sqlite3.Row
    try:
        db.executescript((root / "schema.sql").read_text(encoding="utf-8"))
        if db.execute("PRAGMA foreign_keys").fetchone()[0] != 1:
            raise RuntimeError("Foreign keys must be enabled")
        for row in json.loads((root / "source_manifest.json").read_text(encoding="utf-8")):
            db.execute(
                "INSERT INTO source VALUES (?, ?, ?, ?)",
                (row["source_id"], row["relative_path"], row["sha256"], row["provenance"]),
            )
        db.executescript((root / "seed.sql").read_text(encoding="utf-8"))
        db.execute("PRAGMA query_only = ON")
        return db
    except BaseException:
        db.close()
        raise


def verify_originals(db, root=HERE):
    """Check static reference digests, exact line locators and excerpts. No merits conclusion."""
    originals = {}
    for s in db.execute("SELECT * FROM source ORDER BY source_id"):
        raw = read_original(root, s["relative_path"])
        if hashlib.sha256(raw).hexdigest() != s["sha256"]:
            raise ValueError(f"Original hash mismatch: {s['source_id']}")
        originals[s["source_id"]] = raw.decode("utf-8").splitlines()
    for row in db.execute("SELECT observation_id, source_id, line_no, excerpt FROM observation"):
        lines = originals[row["source_id"]]
        i = row["line_no"] - 1
        if not 0 <= i < len(lines) or row["excerpt"] not in lines[i]:
            raise ValueError(f"Original locator or excerpt mismatch: {row['observation_id']}")
    return len(originals)


def observations(db, issue):
    # Separating observation count from any one-to-many witness join avoids inflated counts.
    statement = (HERE / "queries.sql").read_text(encoding="utf-8").split(";")[0]
    return [dict(r) for r in db.execute(statement, {"issue": issue})]


def request_gaps(db):
    statement = (HERE / "queries.sql").read_text(encoding="utf-8").split(";")[1]
    return [dict(r) for r in db.execute(statement) if not r["linked_sources"]]


def main():
    with closing(open_demo()) as db:
        count = verify_originals(db)
        rows = observations(db, "I-01")
        missing_times = [r["observation_id"] for r in rows if r["event_time_utc"] is None]
        print(json.dumps({
            "verified_fixture_files": count,
            "issue": "I-01",
            "observations": rows,
            "observations_with_unknown_time": missing_times,
            "unlinked_requests_in_this_index": request_gaps(db),
            "open_question": "What event did each clock or person measure?",
        }, indent=2))


if __name__ == "__main__":
    main()
