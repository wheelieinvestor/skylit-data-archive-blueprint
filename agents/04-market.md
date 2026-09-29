# Market, sectors and industries

Read [COMMON.md](COMMON.md) and every required document it names before starting.

Role: `04-market`.

## Objective

Build the market adapter for market overview/tide, breadth, sector/industry flow and daily/weekly rankings.

Preserve the full returned structure, aggregate level, sector/industry membership, filter and rank scope, units, calculation version and source timestamps. Coordinate ticker-level source ownership with Agent 02.

Backfill genuinely date-addressable aggregates to observed boundaries. Archive current-only overviews and rankings prospectively. Do not represent a top-N list as a complete market universe, or use current group membership as known historical membership.

Validate nested fields, partial sector/industry returns, stale snapshots, timestamp/session boundaries and revisions. Publish daily and admitted intraday coverage, explicit missing groups, size measurements, release manifests and a fresh recurring publication.

## Assigned route inventory

- `flow GET /v1/flow/market-breadth`
- `flow GET /v1/flow/sector/{sector}`
- `flow GET /v1/market/overview`
- `flow GET /v1/market/tide`
- `flow GET /v1/underlying/top/daily`
- `flow GET /v1/underlying/top/weekly`

Refresh current specifications and actual access before acquisition. Keep changes to shared ownership coordinated with Agent 00.
