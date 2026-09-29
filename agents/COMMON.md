# Shared instructions for implementation agents

Read the blueprint's LAUNCHPAD_CONTEXT.md, docs/activation.md, docs/status.md, docs/build-your-own.md, docs/architecture.md, docs/data-model.md, docs/collection-workflow.md, docs/budget.md, config/endpoint-inventory.json and your role prompt. Then read the operator's ignored config/operator.local.json and the selected implementation repository's own instructions and current state.

This is a public guide, not an installed runtime. Work in the explicitly selected implementation repository and data directory, not in this blueprint. Credentials remain in the operator's protected environment. No collected data, private configuration or real response samples belong in this public guide.

Resolve material missing targets, limits or authority with one grouped question while continuing independent design/code work. Honor the operator's recorded authority for implementation, provisioning, deployment and activation; finish authorized work without repeated approval. This is research acquisition only and does not authorize broker orders or unrelated service changes.

All roles share the chosen total budget, local working-space allowance and actual provider limits. Agent 00 owns common code, dependencies, transport, scheduling, reservations, infrastructure and integration. Other roles own their adapter/web namespace plus related tests and documentation in separate branches/worktrees. Communicate through implementation PRs and committed handoff files; interface changes go through Agent 00.

Develop concurrently against a fake context if necessary. Real acquisition requires a working shared coordinator, ownership lease and resource admission. Do not create an independent bulk scheduler or assign yourself the whole budget. Existing collectors remain owned until a safe batch-boundary cutover.

Preserve every returned field in raw form and map it to a normalized field, a derived view or an explicit coverage outcome. Full catalog breadth comes before indiscriminate maximum frequency. Current catalog membership, HTTP 200 or top-N output cannot prove complete history. Preserve identities, time/availability semantics, revisions, schemas and code/source provenance.

Use lazy plans, bounded memory/scratch, deterministic acquisition keys, raw-source reuse, immutable objects and readback verification before an atomic catalog/cursor commit. Do not fabricate missing source times, historical fields, quotes or identities.

Deliver code, dataset registrations, field inventory, boundary/sizing evidence, coverage report, private release manifest references, recurring schedule and a handoff matching templates/handoff.example.json. Run focused behavior tests for real failure cases and coordinate final integrated checks with Agent 00. Do not use documentation-string tests as runtime evidence.

Freeze the initial historical cutoff, complete all admitted partitions and account for unsupported/partial/unresolved/budget-deferred work. Verify a fresh incremental publication and interruption recovery. A pilot or queued schedule is not completion. Report implemented, deployed, activated and collected as separate outcomes; preserve exact outstanding work.

## Phase boundary: architecture first

The initial task is architecture-only. Do not send ANY Skylit API request, including schema refreshes, capability/account checks, probes, sample fetches or streams. Use saved metadata and offline fixtures. Stop existing collection safely, preserve journals, disable schedules and implement a persistent shared pause gate that defaults off on restart/deploy.

Agent 00 must enforce this in both shared and legacy request paths. Build and verify the architecture, integration and offline failure cases, then stop with live acceptance explicitly pending. The other roles' live-acquisition objectives describe a later phase; they do not override this boundary. Only a new explicit operator confirmation permits enabling provider requests. Do not enable collection merely because general provisioning/deployment authority is true or code tests pass.
