INSERT INTO witness VALUES ('W-01', 'Rowan Vale', 'Gate clerk; did not observe the handoff.');
INSERT INTO request_item VALUES
  ('RQ-01', 'Bay 4 movement records for training shipment K-17'),
  ('RQ-02', 'Gate controller clock calibration records');
INSERT INTO issue VALUES ('I-01', 'The K-17 handoff finished by 14:05 UTC.');
INSERT INTO observation VALUES
 ('O-01', 'I-01', 'S-01', 3, 'Shipment K-17 transfer was complete by 14:02.', 'supports', 'checked', '2032-04-08T14:02:00Z', 'A manual entry; verify the author and event being recorded.'),
 ('O-02', 'I-01', 'S-02', 3, 'K-17 associated with entry scan; direction awaits confirmation.', 'challenges', 'needs-context', '2032-04-08T14:10:00Z', 'A scan time is not necessarily the handoff time; check clock, direction and association.'),
 ('O-03', 'I-01', 'S-03', 3, 'The scanner was in use, but I did not see the handoff.', 'context', 'checked', NULL, 'The witness reports scanner use, not when the handoff occurred.');
INSERT INTO observation_witness VALUES ('O-03', 'W-01', 'Firsthand scanner observation; no firsthand handoff observation.');
INSERT INTO request_source VALUES
 ('RQ-01', 'S-01', 'partial'),
 ('RQ-01', 'S-02', 'partial');
