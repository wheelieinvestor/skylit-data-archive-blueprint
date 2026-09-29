# Status and scope

This guide was prepared on **September 29, 2026**, from the author's collection design, existing local collection code/operations, and the shared platform interface under development.

| Layer | What this guide can establish |
|---|---|
| Original collection pattern | The reference system has local historical collectors, immutable raw/curated objects, upload verification, resumable work and a private dashboard. |
| Expanded platform | A shared adapter interface exists in development. Distributed coordination, shared admission, cloud workers and the expanded library are implementation work in progress. This guide is not a live deployment audit. |
| This public repository | Documentation, portable agent prompts, configuration/metadata templates, a dated route inventory and an offline check. |
| Software to run the archive | Must be implemented in the reader's own repository. No collector package, deployable container, database migration, or working dashboard is distributed here. |
| Data coverage | No data or coverage results are distributed. Every operator must establish their own source boundaries, permissions and verified publications. |

The service names and interfaces describe the target architecture. They are not commands or resources that a fork already has. Do not copy commands from a private implementation and assume they are available in this repository.

## Architecture-only completion

Build and integrate the runtime, pass offline checks, verify a persistent default-off request gate and leave collection/schedules disabled. Provider-dependent checks are intentionally pending. Explicit operator confirmation is required before the later live phase.

## What success means after collection is authorized

Complete a bounded real job through source fetch, raw storage, normalized storage, checksum verification, a committed manifest and an authenticated catalog view. Show recovery after an interrupted upload and a fresh recurring collection cycle. Then finish the admitted historical partitions through a fixed cutoff while reporting all gaps.

A working health check, a scheduled job or a successful API response establishes only that narrower fact. None establishes a complete archive.

Update this page when public deliverables change. Date observations and clearly separate design targets from tested functionality.
