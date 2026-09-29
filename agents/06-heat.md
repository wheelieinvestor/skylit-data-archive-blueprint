# Gamma, vanna and live heat data

Read [COMMON.md](COMMON.md) and every required document it names before starting.

Role: `06-heat`.

## Objective

Build or extend the heat adapter without duplicating an existing gamma/vanna backfill. Import verified sources and preserve frozen cohorts and acquisition provenance.

Prioritize broad daily statistics and closing full matrices across supported instruments. Keep selected richer intraday cohorts and admit dense windows only after sizing. Represent full expiry-by-strike matrices separately from ranges netted across the expiry axis.

Preserve source matrix geometry, units, node classifications and all offered gamma/vanna fields. Recover omitted normalized fields from raw archives before re-fetching. Capture live velocity, classified levels and streams prospectively, with explicit stream gaps and deduplication.

Verify layout/dimension consistency, expiry handling, resolution/timestamp behavior, empty/partial history, revisions and underlying price basis. Do not treat live-only values as historical observations. Publish full field/coverage inventories, incremental schedules and verified immutable releases.

## Assigned route inventory

- `heat GET /v1/gex/levels`
- `heat GET /v1/heatmap`
- `heat GET /v1/historical`
- `heat GET /v1/historical/range`
- `heat GET /v1/stats/daily`
- `heat GET /v1/stream`

Refresh current specifications and actual access before acquisition. Keep changes to shared ownership coordinated with Agent 00.
