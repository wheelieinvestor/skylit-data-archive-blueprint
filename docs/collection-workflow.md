# Collection workflow

## 1. Discover

Read the current API specifications, account capabilities and endpoint-specific limits using your own access. Build an inventory of routes and returned fields. Snapshot symbol catalogs and resolve instrument identities. See [datasets](datasets.md) for the initial inventory and public sources.

Do not assume access, concurrency, credit pricing or dates from another operator's account. Keep requests on approved provider hosts and documented read-only routes. Implement bounded responses, timeouts, retry/backoff and shared rate permits before bulk collection.

## 2. Probe and size

Use a bounded set of liquid, thin, newly listed and identity-change cases across old/recent and ordinary/busy sessions. Measure returned dates, field presence, compressed raw bytes, curated bytes, latency and pagination behavior. This is an initial sizing step, not a permanent restriction of the universe.

Determine whether each field is historical, current-only, rolling-window or derived. Preserve current-only observations early because they may not be reconstructible. A theoretical endpoint range is not an observed historical boundary.

## 3. Plan lazily

Freeze an initial historical cutoff at the last completed relevant session. Produce bounded jobs lazily by dataset, instrument and time window. Do not expand years of every symbol into a giant local queue before doing useful work.

Prioritize broad daily fields across the supported catalog. Then preserve selected intraday cohorts and expand expensive tapes or matrices only under measured shared admission. Record every unaffordable or unsupported partition explicitly.

## 4. Claim and reserve

Claim a unique job transactionally. Reserve shared API capacity, response/scratch limits and storage/egress cost before requesting data. Leases expire safely; only the owner with the current fencing token can change its cursor or reservation.

Existing collectors count toward every global limit until ownership is transferred at completed batch boundaries. A new worker must never delete another worker's reservation or run the same logical partition alongside an old scheduler.

## 5. Fetch and journal

Reuse a verified existing raw object when the acquisition identity matches. Otherwise fetch through the shared transport and journal the successful response with a checksum. Handle 429/503 responses and provider retry headers centrally. Never log keys or raw account responses.

## 6. Normalize and publish

Normalize in bounded chunks. Upload raw and curated objects, read them back to verify bytes/checksums, then atomically commit the manifest, coverage findings and next cursor. Immutable objects are never overwritten.

```text
claim + reserve
  -> fetch or reuse
  -> journal response
  -> raw / curated uploads
  -> verify stored bytes
  -> commit publication + coverage + cursor
  -> release reservation
  -> evict only remotely verified local cache
```

If an upload succeeds but its acknowledgment is lost, recovery checks the object before uploading again. If publication fails, keep the journal and retry idempotently. Orphaned uploads remain accountable storage until reconciled; never treat them as zero cost.

## 7. Audit and continue

Check timestamps, field missingness, pagination, identity, duplicate revisions, source freshness and first/last observations. Preserve revisions rather than overwriting prior releases. Derived bars or features must identify their inputs and calculation method separately from native observations.

Incremental schedules use exchange calendars, holidays, early closes, completed bars and endpoint recomputation cadence. Stream reconnects record real gaps; they must not invent missed events. Recurring operation requires evidence of a newly completed publication cycle.

## Adapter contract

```text
specs() -> dataset specifications
plan(context, universe_version, start, end, tier) -> lazy job iterator
fetch(context, leased_job) -> bounded raw envelope or stream chunks
normalize(context, raw_reference, schema_version) -> bounded batches
audit(context, publication) -> coverage findings
```

The shared context supplies transport, secrets without logging, calendars, permits, resource reservations, raw-object reuse, publication and progress reporting. The adapter owns its field inventory and dataset-specific logic, not a separate scheduler or budget.

## Completion

Finish every admitted partition through the chosen cutoff; list partial, unsupported, unresolved and budget-deferred work with reasons. Verify interruption recovery and a fresh forward cycle. Do not reclassify runnable admitted work as deferred simply to declare the task finished.
