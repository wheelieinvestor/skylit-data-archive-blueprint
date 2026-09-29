# Operations and recovery

The implementation must provide actual commands for these actions. This guide specifies their behavior; it does not pretend those commands already exist here.

## What to monitor

Track completed publications and advancing cursors by dataset, expected versus observed sessions, source freshness, lease heartbeats, retry counts, missing fields, stream gaps, actual stored bytes, outstanding reservations and cost forecasts.

Show meaningful distinctions: waiting for a lease, provider throttling, retryable failure, unsupported source, unresolved identity, budget deferral and a truly completed partition. A loaded scheduler or green health endpoint is not proof that fresh data is being stored.

## Recovery cases

| Event | Required behavior |
|---|---|
| Local sleep or worker restart | Resume from journal and last committed cursor; reacquire a valid lease |
| Provider throttles/errors | Respect retry guidance, reduce shared concurrency and preserve progress |
| Upload interrupted | Retain the only source copy; check remote checksum before retry |
| Upload succeeds, catalog commit fails | Reuse verified objects and retry the catalog transaction idempotently |
| Lease expires | Reject stale publication/cursor writes with a fencing token |
| Budget or scratch is exhausted | Stop new admissions and report the exact limit; retain verified history |
| Provider changes fields | Preserve raw response, record schema change and version normalization |
| Source revision arrives | Retain both versions and identify supersession; keep frozen releases stable |

## Existing collector cutover

Inventory current workloads, source objects, ownership and journals before replacing a scheduler. Import references without moving or deleting originals. Count old workers against shared limits. Transfer ownership at completed batch boundaries, and verify old and new schedulers cannot claim the same partitions.

Never clear every reservation on startup. Expire only the reservations proven abandoned by the shared ownership model. Preserve original acquisition provenance when a runtime wrapper or parser changes.

## Deployment acceptance

Run documented format/lint/type checks and the implementation's relevant test suite against the final code; satisfy CI. Tests should cover real behavior, including duplicate claims, stale leases, quota contention, empty/truncated responses, timestamp collisions and interrupted publication.

After deployment, verify the installed commit, service startup, effective resource settings, authenticated access and a real ingestion round trip. Check that anonymous catalog/export access is denied. Run concurrent jobs from at least two families and confirm one shared budget and API ceiling. Restore a metadata backup in an isolated test target.

Each activated family must finish a newly observed publication cycle. Every admitted historical job through the release cutoff must be complete or have an explicit evidenced source outcome. Work remaining queued is still work remaining.

## Privacy and credentials

Keep provider keys in worker secret stores, database credentials on the private service network, and protected worker tokens on local machines. Redact headers and credential-bearing URLs. Log request identities and error categories rather than raw account payloads. Use bounded authenticated exports and keep buckets private.

This public repository accepts documentation, code for offline checks and metadata templates. It does not accept real responses, symbol exports, collection manifests pointing to private objects, or operational logs.
