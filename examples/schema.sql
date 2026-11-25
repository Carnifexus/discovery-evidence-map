PRAGMA foreign_keys = ON;

CREATE TABLE source (
  source_id TEXT PRIMARY KEY NOT NULL,
  relative_path TEXT UNIQUE NOT NULL,
  sha256 TEXT NOT NULL CHECK(length(sha256) = 64),
  provenance TEXT NOT NULL
);
CREATE TABLE witness (
  witness_id TEXT PRIMARY KEY NOT NULL,
  display_name TEXT NOT NULL,
  knowledge_limit TEXT NOT NULL
);
CREATE TABLE request_item (
  request_id TEXT PRIMARY KEY NOT NULL,
  requested_item TEXT NOT NULL
);
CREATE TABLE issue (
  issue_id TEXT PRIMARY KEY NOT NULL,
  proposition TEXT NOT NULL
);
CREATE TABLE observation (
  observation_id TEXT PRIMARY KEY NOT NULL,
  issue_id TEXT NOT NULL REFERENCES issue(issue_id),
  source_id TEXT NOT NULL REFERENCES source(source_id),
  line_no INTEGER NOT NULL CHECK(line_no > 0),
  excerpt TEXT NOT NULL,
  relation TEXT NOT NULL CHECK(relation IN ('supports', 'challenges', 'context')),
  reviewer_status TEXT NOT NULL CHECK(reviewer_status IN ('lead', 'checked', 'needs-context')),
  event_time_utc TEXT,
  limitation TEXT NOT NULL
);
CREATE TABLE observation_witness (
  observation_id TEXT NOT NULL REFERENCES observation(observation_id),
  witness_id TEXT NOT NULL REFERENCES witness(witness_id),
  basis TEXT NOT NULL,
  PRIMARY KEY (observation_id, witness_id)
);
CREATE TABLE request_source (
  request_id TEXT NOT NULL REFERENCES request_item(request_id),
  source_id TEXT NOT NULL REFERENCES source(source_id),
  coverage TEXT NOT NULL CHECK(coverage IN ('candidate', 'partial', 'reviewed')),
  PRIMARY KEY (request_id, source_id)
);
CREATE INDEX obs_by_issue ON observation(issue_id, source_id);
