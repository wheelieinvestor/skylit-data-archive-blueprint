# Contracts, chains and open interest

Read [COMMON.md](COMMON.md) and every required document it names before starting.

Role: `03-contracts`.

## Objective

Build the contracts adapter for contract discovery, chain/strike/expiration structure, bulk statistics, OI changes, unusual activity, rankings, histories, trade context and contract pressure/ratios.

Preserve underlying identity, option root, expiry, right, strike, multiplier/deliverable evidence and observation time. Do not infer missing deliverables or merge contracts using ticker alone. Coordinate identity with Agent 01 and raw trade overlap with Agent 02.

Separate current OI from historical OI changes, and rankings from an enumerated population. Snapshot changing chains prospectively. Backfill actually supported history, prioritizing broad summaries before expensive full contract tapes under shared budget admission.

Retain quote prices/sizes and timestamps only when supplied. Report missing historical Greeks, quotes and adjustment evidence explicitly. Verify pagination, expiry boundaries, identity transitions, timestamp collisions, revisions, empty results and truncated listings. Publish complete field/coverage inventories and a verified incremental cycle.

## Assigned route inventory

- `flow GET /v1/contract-bull-bear/{symbol}`
- `flow GET /v1/contract-ratio/{symbol}`
- `flow GET /v1/contract/bulk/stats`
- `flow GET /v1/contract/top/daily`
- `flow GET /v1/contract/top/weekly`
- `flow GET /v1/contract/unusual-oi`
- `flow GET /v1/contract/unusual-volume`
- `flow GET /v1/contract/{symbol}/chart`
- `flow GET /v1/contract/{symbol}/history`
- `flow GET /v1/contract/{symbol}/rvol`
- `flow GET /v1/contract/{symbol}/stats`
- `flow GET /v1/contract/{symbol}/trades`
- `flow GET /v1/underlying/{ticker}/by-strike`
- `flow GET /v1/underlying/{ticker}/by-strike/{strike}/expirations`
- `flow GET /v1/underlying/{ticker}/chain`
- `flow GET /v1/underlying/{ticker}/expirations`

Refresh current specifications and actual access before acquisition. Keep changes to shared ownership coordinated with Agent 00.
