# How the data is organized

## Three storage layers

| Layer | Contents | Why retain it |
|---|---|---|
| Raw | Losslessly compressed response bodies, safe request metadata, source timestamps and hashes | Reproduce normalization and recover fields without repeating the provider request |
| Curated | Bounded Parquet partitions and immutable manifests | Query consistently across datasets without repeatedly decoding raw responses |
| Results | Coverage/quality reports, catalog exports, release summaries and authorized derived exports | Explain what the archive contains and make it usable |

Never store credentials or authorization headers in an envelope. Preserve provider precision, units, nulls, absent fields and newly introduced fields. An omitted field, a null value and numeric zero are different observations.

## Physical versus logical layout

Physical objects use a content hash:

```text
objects/<first-two-sha256-characters>/<sha256>.<format>
```

Logical catalog keys describe their meaning:

```text
family / dataset / instrument / session / resolution / revision
```

For example, the schema identifier `skylit.atlas.ohlcv.v1` names a dataset, not a file or data sample. A catalog entry maps its instrument/session partitions to immutable raw and curated object references. This makes deduplication possible without reorganizing old files whenever names or parsers change.

## The three identities

**Acquisition identity:** hash the provider, host-qualified route, canonical parameters, time interval and explicit refresh generation. Do not include the worker, branch or parser version. Identical source requests should share saved input.

**Normalization identity:** bind source hashes to schema version, parser version, code commit and dependency-lock hash. A new parser creates a new derived version, without pretending the source was fetched again.

**Release identity:** bind exact immutable objects, schemas, universe version and coverage cutoff into a manifest. Later provider corrections produce retained revisions; they do not silently change a frozen release.

See the [dataset specification](../templates/dataset-spec.example.json) and [publication schema](../templates/publication.schema.json). They describe metadata, not collected observations.

## Provenance fields

Record provider/service/route and safe normalized request parameters; canonical instrument and provider symbol; alias validity and catalog version; session timezone and interval; resolution and session scope; requested time, source/event time and ingestion time; source calculation version when supplied; raw hash, curated references, parser version, commit and lock hash; expected versus observed coverage; and revision relationships.

Do not infer a quote timestamp from its trade timestamp. Missing source timestamps remain unknown. Separate observed availability from conservative modeled availability; daily closing values must not become fictitious intraday inputs. For prices and exposures, document adjustment conventions rather than inferring them from a smooth chart.

## Identity and universe history

Use canonical instrument IDs with time-bounded provider aliases. An equity and a crypto asset may share a ticker. Cash indices, option roots, share classes, currencies, ADRs and reused tickers need distinct identities or explicit relationships. Mark unverified mappings unresolved.

Snapshot the collection universe regularly, including additions and removals. Keep research cohorts as named frozen subsets. A current catalog does not establish a complete historical or survivorship-free universe. Retain known delisted instruments for historical planning where supported.

## Coverage is a dataset

For every dataset/instrument/window retain requested and actual ranges, expected sessions, observed buckets, gaps, null/absent counts, duplicate/conflicting revisions, pagination exhaustion and source freshness.

Use explicit outcomes: `published`, `partial`, `empty`, `unsupported`, `unresolved_identity`, `deferred_budget` and `retryable_failure`. Job progress states such as `pending`, `leased`, `fetching`, `uploaded` and `verified` are separate from completeness. Empty HTTP-success responses and capped top-N lists are not full population coverage.
