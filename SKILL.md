---
name: discovery-evidence-map
description: Create a source-checked index connecting discovery records, discovery requests, disputed facts, and witnesses. Use for an indexed production or an explicitly defined review subset.
---

# Discovery Evidence Map

Build an auditable index, not a substitute for the evidence. Work in the lawyer’s authorized environment. Do not upload originals, excerpts, embeddings, or analysis to a third-party service without the lawyer's approval for that specific use. The software example uses only fictional records.

1. **Bound the review.** Ask for the production or index in scope, what is excluded, the date of the snapshot, and the questions the lawyer wants answered. Mark absent, unreadable, encrypted, and unprocessed material separately. Report coverage by batch; do not silently expand scope.
2. **Record provenance.** Assign a stable source ID and record original filename or production ID, batch, pinpoint, and hash if available. Keep received bytes untouched. Store OCR, translations, and normalized text separately and identify how they were produced. Exact duplicate bytes do not erase separate production IDs or family relationships.
3. **Connect facts without resolving them.** For each observation save the exact excerpt, pinpoint, relation (supports, challenges, or context), limitation, and review status. Link a witness with a basis and limit of knowledge. Link requests to source records with a review status; a candidate match is not a complete response.
4. **Keep gaps distinct.** Use NULL for unknown fields. Record “no index link” or “no hit in the reviewed subset” as a scoped search result, not “no such record exists.” Track facts needing verification and flag conflicting sources side by side.
5. **Verify before relying.** Open the original at the pinpoint, read the surrounding context, and confirm the record type, attribution and what the timestamp measures. Compare audiovisual transcripts with the relevant recording segment. Tag unresolved disagreements and preserve the contrary evidence. Do not mark them resolved unless counsel decides on an adequately sourced explanation.
6. **Hand back a usable result.** Provide a short table of propositions, supporting and contrary records, witness foundations, missing sources and next checks. Give coverage limits, the search snapshot, and an exact source locator for material statements. Keep source facts, investigator hypotheses, and legal conclusions separate.

Use [the lawyer guide](docs/LAWYER-GUIDE.md) to run the example and [the white paper](docs/WHITE-PAPER.md) to understand the design.
