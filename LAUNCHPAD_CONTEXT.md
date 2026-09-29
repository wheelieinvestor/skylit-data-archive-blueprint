# Public blueprint context

Version 1, September 29, 2026.

The purpose of this repository is to explain a Skylit data-collection architecture and give readers portable instructions and agent prompts to implement it independently. The author has authorized publication of this guide without collected data or private deployment details.

The underlying research system began with local collectors, immutable object storage, and a private dashboard. The shared distributed coordinator, seven data-family adapters and dashboard have since reached a verified architecture-only deployment with collection disabled. This repository publishes the design and implementation guide, not that private runtime or collected data. Source-dependent live acceptance remains pending. See docs/status.md for the dated milestone.

The reference topology uses one Railway project, one research environment, three private buckets, a small Postgres metadata database, a coordinator, a shared ongoing worker, and a private dashboard. Local bulk workers use the same shared queue and upload directly to object storage.

The reference Railway budget is $150/month for the entire archive; all local workers share a 10 GiB working-data allowance. Readers choose their own explicit limits in config/operator.local.json. Limits depend on their own plan and measurements; no provider entitlement, historical range, or concurrency value is inherited from the author's account.

Seven data-family modules collect identity/prices, options flow, contracts/OI, market/sectors, dark pool, gamma/vanna, and Tempest. Agent 00 owns common infrastructure and integration; Agent 08 owns the data-library interface. Development agents are temporary builders. Scheduled collectors are deterministic programs, not permanent LLM conversations.

This guide itself authorizes no spending, deployment, API collection, public dataset redistribution, or trading for a reader. A reader chooses an implementation repository and records scope in the operator configuration before launching agents. That recorded scope should permit agents to finish implementation and verification without repeated questions about already agreed decisions.

For changes, read README.md, docs/status.md and the relevant design document. For implementation, read docs/build-your-own.md, docs/architecture.md, docs/data-model.md, docs/collection-workflow.md, agents/COMMON.md and the assigned role prompt. Keep current provider documentation authoritative for API details.

## Default activation boundary

Build architecture and validate offline first. All provider API requests remain disabled until the operator explicitly confirms collection may begin. Permission to implement or provision is not permission to probe the provider. Live-data acceptance is a later phase and must be reported pending while paused. See docs/activation.md.
