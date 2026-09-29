# Full Tempest volatility archive

Read [COMMON.md](COMMON.md) and every required document it names before starting.

Role: `07-tempest`.

## Objective

Build or extend the Tempest adapter across its whole supported catalog. Reuse existing source/history objects, preserve frozen research subsets and consume the shared identity registry.

Cover history, derived comparisons, IV, term structure, cones, sigma, surfaces, tilt, events, market context, screener, status, snapshots and streams. Preserve all daily columns and unknown future fields. Reuse snapshot components instead of repeatedly fetching equivalent module content without a reason.

Separate date-indexed history, rolling derived windows, current panels and model/calculation revisions. Probe actual date boundaries, module freshness and account-specific batch/stream limits. Backfill supported daily history broadly; collect changing modules prospectively at their meaningful recomputation cadence.

Normalize in bounded chunks instead of accumulating a multiyear universe in memory. Verify null/absent fields, empty modules, symbol/root aliases, stale snapshots, revisions, timestamp policy and reconnect gaps. Publish per-module coverage, size measurements, frozen releases and a verified new recurring cycle.

## Assigned route inventory

- `heat GET /v1/vol/cones`
- `heat GET /v1/vol/derived`
- `heat GET /v1/vol/events`
- `heat GET /v1/vol/history`
- `heat GET /v1/vol/iv`
- `heat GET /v1/vol/market`
- `heat GET /v1/vol/screener`
- `heat GET /v1/vol/sigma`
- `heat GET /v1/vol/snapshot`
- `heat GET /v1/vol/status`
- `heat GET /v1/vol/stream`
- `heat GET /v1/vol/surface`
- `heat GET /v1/vol/term`
- `heat GET /v1/vol/tilt`

Refresh current specifications and actual access before acquisition. Keep changes to shared ownership coordinated with Agent 00.
