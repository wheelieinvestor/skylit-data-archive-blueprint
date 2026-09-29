# Off-exchange prints

Read [COMMON.md](COMMON.md) and every required document it names before starting.

Role: `05-dark-pool`.

## Objective

Build the dark-pool adapter for paginated off-exchange trades and top-print summaries. Preserve native identifiers, event/receipt timestamps where supplied, venue/condition fields, units, notional filters and ordering semantics.

Probe actual retention and per-symbol/date availability before a large backfill. Exhaust pagination where supported; mark saturated unpageable results partial. Distinguish no returned rows from an assertion that no real-world prints occurred.

Use deterministic deduplication, bounded partitions and stable cursors. Preserve conflicting/corrected observations. Start prospective capture early when historical retention is limited. Admit dense tape only after measuring raw and curated bytes and shared cost.

Verify duplicate pages, cursor repetition, out-of-order prints, equal timestamps, empty success and interruptions. Produce symbol/date/filter coverage, source boundaries and a verified forward publication.

## Assigned route inventory

- `flow GET /v1/dark-pool/top-prints/{ticker}`
- `flow GET /v1/dark-pool/trades`

Refresh current specifications and actual access before acquisition. Keep changes to shared ownership coordinated with Agent 00.
