# Options flow and ticker activity

Read [COMMON.md](COMMON.md) and every required document it names before starting.

Role: `02-flow`.

## Objective

Build the flow adapter for all assigned ticker-level routes: net premium/tide, aggregates, momentum, baselines, historical comparisons, strike and moneyness views, sweeps, underlying activity, volume/OI comparisons and scoring.

Inventory every response field and determine which routes expose history versus current snapshots. Reuse overlapping sources and coordinate contract-level ownership with Agent 03. Save filter/ranking scope and do not mistake a capped feed for the full tape.

Backfill affordable daily aggregates broadly and admitted intraday premium/activity series. Collect current-only snapshots prospectively at a cadence justified by provider recomputation. Preserve trade IDs, source timestamps, score versions and any attached quote context without inventing missing fields.

Audit pagination, duplicate trades, late revisions, time zones, empty success, truncated responses and source freshness. Publish per-instrument field/date coverage, size evidence, stable cursors and a verified fresh collection cycle.

## Assigned route inventory

- `flow GET /v1/aggregate/{ticker}`
- `flow GET /v1/chain-bull-bear/{ticker}`
- `flow GET /v1/chain-ratio/{ticker}`
- `flow GET /v1/flow/{ticker}`
- `flow GET /v1/flow/{ticker}/aggregate`
- `flow GET /v1/flow/{ticker}/baseline`
- `flow GET /v1/flow/{ticker}/historical-compare`
- `flow GET /v1/flow/{ticker}/momentum`
- `flow GET /v1/flow/{ticker}/strikes`
- `flow GET /v1/flow/{ticker}/tide`
- `flow GET /v1/moneyness/{ticker}`
- `flow GET /v1/score/{trade_id}`
- `flow GET /v1/sweeps/{ticker}`
- `flow GET /v1/underlying/bulk/stats`
- `flow GET /v1/underlying/{ticker}/chart`
- `flow GET /v1/underlying/{ticker}/history`
- `flow GET /v1/underlying/{ticker}/rvol`
- `flow GET /v1/underlying/{ticker}/stats`
- `flow GET /v1/underlying/{ticker}/trades`
- `flow GET /v1/vol-oi/{ticker}`

Refresh current specifications and actual access before acquisition. Keep changes to shared ownership coordinated with Agent 00.
