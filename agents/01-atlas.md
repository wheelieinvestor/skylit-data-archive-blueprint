# Catalog, identity and prices

Read [COMMON.md](COMMON.md) and every required document it names before starting.

Role: `01-atlas`.

## Objective

Build the atlas adapter and versioned instrument/universe registry. Discover the union of supported provider catalogs; use search and rankings as supplementary discovery, not proof of a full historical master. Preserve known removed instruments and keep research cohorts separate.

Distinguish listings, currencies, equity/crypto collisions, cash indices/option roots, share classes and ticker reuse. Record time-bounded aliases, calendars, session scopes, adjustment conventions and unresolved mappings.

Backfill daily OHLCV across the resolvable catalog, then admitted intraday and extended-session bars. Preserve buy/sell/unknown volume when offered. Re-normalize existing raw prices before issuing equivalent requests. Keep native and derived resolutions distinguishable and validate any aggregation.

Measure real earliest/latest coverage and request-window limits. Verify array alignment, timestamp order, OHLC consistency, sided-volume reconciliation where defined, identity transitions, empty responses and revisions. Publish daily catalog changes and incremental completed bars through the shared coordinator.

## Assigned route inventory

- `heat GET /v1/symbols`
- `heat GET /v1/vol/symbols`
- `flow GET /v1/underlying`
- `flow GET /v1/underlying/search`
- `atlas GET /v1/config`
- `atlas GET /v1/history`
- `atlas GET /v1/search`
- `atlas GET /v1/symbols`
- `atlas GET /v1/time`

Refresh current specifications and actual access before acquisition. Keep changes to shared ownership coordinated with Agent 00.
