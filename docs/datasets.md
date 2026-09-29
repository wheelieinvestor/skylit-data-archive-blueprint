# Dataset families and coverage

The initial inventory lists **77 service-qualified GET operations** observed on September 29, 2026, including three OpenAPI specifications and one account-capability route. That is a route count, not a count of independent market metrics or a promise of complete history.

[config/endpoint-inventory.json](../config/endpoint-inventory.json) contains route names and role ownership only. It contains no source responses, instrument lists or account details. Refresh the current specifications before implementing, since routes, fields and plan access can change.

| Role | Operations | Collection responsibility |
|---|---:|---|
| 00 Platform | 4 | Capabilities and the three API specifications |
| 01 Atlas and identity | 9 | Catalog discovery, instrument resolution, prices and available sided volume |
| 02 Flow | 20 | Ticker-level options activity, premium series, sweeps, pressure, momentum, scoring and underlying trade context |
| 03 Contracts | 16 | Chain discovery, expirations/strikes, contract activity/history, OI and available trade/quote context |
| 04 Market | 6 | Market tide/overview, breadth, sector/industry flow and rankings |
| 05 Dark pool | 2 | Off-exchange trades and top-print summaries |
| 06 Heat | 6 | Gamma/vanna historical/live matrices, daily statistics, levels and stream |
| 07 Tempest | 14 | History, derived comparisons, IV, term, cones, sigma, surface, tilt, events, market, screener, snapshots, status and stream |
| 08 Dashboard | 0 | Reads the shared catalog; does not independently fetch provider data |

## Collection priorities

1. **Discovery:** All known routes/fields, symbols, identities, calendars and source versions.
2. **Broad daily history:** All supported instruments and metrics with actual historical coverage, including daily/closing snapshots where supported.
3. **Selected intraday history:** Preserve chosen research cohorts, then widen under measured capacity.
4. **Forward-only observations:** Start early for changing classifications, velocity, surfaces, event context and other unrecoverable snapshots.
5. **Dense detail:** Larger trade tapes, chains, one-second windows and broader matrices after sizing and admission.

The priorities are not strict serial phases: forward-only collection should run alongside historical work. Keep capacity available for it.

## Family-specific cautions

- **Prices:** Preserve native versus derived bars, session scope, adjustment conventions and sided volume when offered. Re-normalize old raw objects to recover fields before re-fetching.
- **Flow:** Different endpoints overlap. Model shared source objects and derived views so that equivalent requests aren't repeated by multiple agents.
- **Contracts:** Separate current OI, historical OI changes, rankings and a complete contract population. Preserve available quotes without inventing quote timestamps, historical Greeks or executability.
- **Market:** Save rank/filter scope and distinguish sector-level, industry-level and whole-market aggregates. A top list does not enumerate the entire universe.
- **Dark pool:** Audit cursor/page exhaustion, duplicate prints, timestamps and retention boundaries. An empty date is an observation about availability, not evidence of no real-world trading.
- **Heat:** Preserve full expiry-by-strike matrices versus net-across-expiry series as different shapes. Live velocity is distinct from historical exposure. Keep raw node labels and audit matrix geometry.
- **Tempest:** Snapshot components can overlap individual module routes. Preserve returned daily columns and changing current panels; some derived windows do not provide arbitrary long historical replay.

For every known field record one of: collected, derived from saved source, current-only, partial, empty, unsupported, unresolved identity, or budget-deferred. New fields remain in raw data and trigger a schema decision.

## Provider references

Use [Skylit's API reference](https://www.skylit.ai/docs/api-reference/introduction) and the linked live specifications. The reference explains the primary and alias hosts and access requirements. The inventory preserves service qualification so identical-looking paths on different APIs aren't confused.

Host and schema links appear in [sources](sources.md). Do not send credentials to arbitrary URLs copied from an API response or user-supplied job.
