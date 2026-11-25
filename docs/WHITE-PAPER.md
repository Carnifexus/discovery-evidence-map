# Discovery Evidence Map
## A source-checked index for large productions

### Abstract

As productions grow, finding a promising record gets easier than knowing what the record actually establishes. A discovery evidence map keeps those jobs separate. It links an observation to the original and a precise locator, shows what evidence cuts the other way, and records who might explain the source. The index helps counsel decide what to read next; it does not decide facts or replace the original.

### Separate records from claims about records

The example models a received source, a proposition, a source-grounded observation, a witness, and a request as different things. Each observation has its own pinpoint and excerpt, a description of how it relates to the proposition, and a limitation. Link tables preserve many-to-many relationships: several records may answer parts of a request, and several witnesses may know different things about one event. A source without a witness stays visible rather than disappearing from the report.

A manifest records the fixture files' SHA-256 hashes. The demonstration compares them to received bytes and checks the exact cited excerpts against those bytes, independently of the SQL seed. That checks one aspect of integrity; it does not show who created a record, whether its contents are accurate, or whether missing records were withheld. Counsel should inspect the source in context. For OCR and transcripts, keep the extracted text distinct from the source and verify important quotations against the page or recording.

### The contradiction is a lead, not a verdict

The fictional dispatch log places a handoff before 14:05 UTC. A gate log shows a later scan, but scanner direction and clock accuracy are unconfirmed, and a scan may measure something other than a handoff. A witness describes seeing scanner use but not the handoff. A defensible report presents all three records together, marks the witness time as unknown, and lists the foundation checks needed before making an attribution or timing claim.

An unlinked request is different from an unknown value. The clock-calibration request has zero links in this index; the witness observation lacks a known time. Neither fact establishes that a clock record or a timestamp does not exist. Record search scope, date, exclusions and failed parses so a reviewer can distinguish an evidence gap from a workflow gap.

### Implementation and operating boundaries

Start with an offline case-specific index. For concurrent review, PostgreSQL is an optional backend: use controlled access, least-privilege identities, tested isolation between matters, and matter-approved storage and retention settings. Put precise source locators next to any conclusion exported from the index. Investigative leads from outside the scoped production should be labeled separately, not presented as evidence received in that production. The example is not a finding of admissibility, a privilege protocol, or a guarantee of appropriate security.
