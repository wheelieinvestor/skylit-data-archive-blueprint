# Shared platform and integration

Read [COMMON.md](COMMON.md) and every required document it names before starting.

Role: `00-platform`.

## Objective

First implement the persistent default-off provider request gate described in [activation control](../docs/activation.md). Build and verify offline; live collection acceptance below belongs to a separately confirmed later phase.


Build the common adapter interface, durable Postgres catalog and job queue, authenticated control API, shared forward worker and local-worker bridge. Own common transport/storage, dependencies, CLI, deployment configuration, migrations and resource admission.

Publish a versioned interface and development context first. Implement lazy plans, canonical acquisition keys, source reuse, leases with fencing, atomic resource reservations, publication transactions and a paginated read API. Request and stream limits come from this operator's actual account; count existing collectors too. Use explicit local/container runtime profiles with bounded scratch and recoverable journals.

Import existing immutable releases and journals without changing originals. Fix process-local budget accounting and unsafe reservation cleanup before parallel writers. Transfer legacy ownership only at completed batch boundaries.

Maintain current-cycle and full-month retained-cost forecasts with protected headroom. Reconcile object bytes and outstanding reservations. Use local direct-to-bucket uploads for bulk work and cloud capacity for forward-only observations. Keep database access private and provider keys out of the dashboard.

Integrate each family and dashboard through focused branches/PRs in the implementation repository. Deploy and activate only when the operator's recorded authority permits it, completing the authorized scope without repeated permission questions. Verify installed versions, effective limits, authenticated access, two families collecting concurrently, stale-lease rejection, interruption recovery and fresh publications. Remain responsible for all seven families and the dashboard; report evidenced source/dependency gaps with a continuation path.

## Assigned route inventory

- `heat GET /v1/account`
- `heat GET /v1/openapi.json`
- `flow GET /v1/openapi.json`
- `atlas GET /v1/openapi.json`

Refresh current specifications and actual access before acquisition. Keep changes to shared ownership coordinated with Agent 00.
