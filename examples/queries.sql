-- One issue, all competing records. A row without a witness stays visible.
SELECT o.observation_id, o.relation, o.reviewer_status, s.source_id, s.relative_path,
       o.line_no, o.event_time_utc, o.excerpt, o.limitation, w.display_name, ow.basis
FROM observation o
JOIN source s ON s.source_id = o.source_id
LEFT JOIN observation_witness ow ON ow.observation_id = o.observation_id
LEFT JOIN witness w ON w.witness_id = ow.witness_id
WHERE o.issue_id = :issue
ORDER BY o.observation_id, w.witness_id;

-- A zero count says only that there is no link in this index.
SELECT r.request_id, r.requested_item, COUNT(rs.source_id) AS linked_sources
FROM request_item r LEFT JOIN request_source rs ON rs.request_id = r.request_id
GROUP BY r.request_id, r.requested_item
ORDER BY r.request_id;
