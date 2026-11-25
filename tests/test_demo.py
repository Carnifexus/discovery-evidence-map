from contextlib import closing
from pathlib import Path
import shutil
import sqlite3
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "examples"))
import demo


class EvidenceFixtureTests(unittest.TestCase):
    def test_independent_source_checks_and_competing_records(self):
        with closing(demo.open_demo()) as db:
            self.assertEqual(demo.verify_originals(db), 3)
            rows = demo.observations(db, "I-01")
            self.assertEqual([r["relation"] for r in rows], ["supports", "challenges", "context"])
            self.assertEqual(rows[2]["display_name"], "Rowan Vale")
            self.assertIsNone(rows[2]["event_time_utc"])
            self.assertEqual(demo.observations(db, "absent"), [])
            self.assertEqual([r["request_id"] for r in demo.request_gaps(db)], ["RQ-02"])
            with self.assertRaises(sqlite3.OperationalError):
                db.execute("DELETE FROM source")

    def test_changing_fictional_original_fails_before_reliance(self):
        with tempfile.TemporaryDirectory() as temp:
            copyroot = Path(temp) / "examples"
            shutil.copytree(demo.HERE, copyroot)
            with (copyroot / "originals/gate-log.txt").open("a", encoding="utf-8") as f:
                f.write("Altered training record.\n")
            with closing(demo.open_demo(copyroot)) as db:
                with self.assertRaisesRegex(ValueError, "Original hash mismatch: S-02"):
                    demo.verify_originals(db, copyroot)

    def test_bad_excerpt_fails_even_with_correct_source_hash(self):
        with tempfile.TemporaryDirectory() as temp:
            copyroot = Path(temp) / "examples"
            shutil.copytree(demo.HERE, copyroot)
            seed = copyroot / "seed.sql"
            seed.write_text(seed.read_text(encoding="utf-8").replace("complete by 14:02.", "complete by 14:01."), encoding="utf-8")
            with closing(demo.open_demo(copyroot)) as db:
                with self.assertRaisesRegex(ValueError, "excerpt mismatch: O-01"):
                    demo.verify_originals(db, copyroot)


if __name__ == "__main__":
    unittest.main()
