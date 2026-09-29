# Agent launch prompts

These prompts work with a coding agent that can read local files, edit your chosen implementation repository and access the services you authorize. They are plain instructions; they do not require a particular agent product or paid orchestration service.

First fill `config/operator.local.json` using the [setup guide](../docs/build-your-own.md). Start Agent 00 in the blueprint checkout. Use the full local path to this checkout if another agent starts elsewhere. Never paste credentials into a prompt.

The first phase is architecture-only: all Skylit requests stay disabled until a new explicit operator confirmation. Read [activation control](../docs/activation.md).

Start 00 first so it establishes the shared contract. Agents 01–08 can develop concurrently once file ownership is clear; production acquisition waits for shared permits. If you already have gamma/Tempest agents, give them roles 06/07 as extensions instead of launching duplicate backfills. With fewer agents, perform the roles sequentially.

The common instructions live in [COMMON.md](COMMON.md). The prompts below are launchers, not substitutes for reading each role file.

## 00-platform — Shared platform and integration

[Full instructions](00-platform.md)

```text
Read agents/00-platform.md and every document it references. Use my completed config/operator.local.json to implement and verify this role in my selected implementation repository. Build and verify the architecture offline. Keep every Skylit request disabled until I explicitly confirm starting collection; report live acceptance as pending.
```

## 01-atlas — Catalog, identity and prices

[Full instructions](01-atlas.md)

```text
Read agents/01-atlas.md and every document it references. Use my completed config/operator.local.json to implement and verify this role in my selected implementation repository. Build and verify the architecture offline. Keep every Skylit request disabled until I explicitly confirm starting collection; report live acceptance as pending.
```

## 02-flow — Options flow and ticker activity

[Full instructions](02-flow.md)

```text
Read agents/02-flow.md and every document it references. Use my completed config/operator.local.json to implement and verify this role in my selected implementation repository. Build and verify the architecture offline. Keep every Skylit request disabled until I explicitly confirm starting collection; report live acceptance as pending.
```

## 03-contracts — Contracts, chains and open interest

[Full instructions](03-contracts.md)

```text
Read agents/03-contracts.md and every document it references. Use my completed config/operator.local.json to implement and verify this role in my selected implementation repository. Build and verify the architecture offline. Keep every Skylit request disabled until I explicitly confirm starting collection; report live acceptance as pending.
```

## 04-market — Market, sectors and industries

[Full instructions](04-market.md)

```text
Read agents/04-market.md and every document it references. Use my completed config/operator.local.json to implement and verify this role in my selected implementation repository. Build and verify the architecture offline. Keep every Skylit request disabled until I explicitly confirm starting collection; report live acceptance as pending.
```

## 05-dark-pool — Off-exchange prints

[Full instructions](05-dark-pool.md)

```text
Read agents/05-dark-pool.md and every document it references. Use my completed config/operator.local.json to implement and verify this role in my selected implementation repository. Build and verify the architecture offline. Keep every Skylit request disabled until I explicitly confirm starting collection; report live acceptance as pending.
```

## 06-heat — Gamma, vanna and live heat data

[Full instructions](06-heat.md)

```text
Read agents/06-heat.md and every document it references. Use my completed config/operator.local.json to implement and verify this role in my selected implementation repository. Build and verify the architecture offline. Keep every Skylit request disabled until I explicitly confirm starting collection; report live acceptance as pending.
```

## 07-tempest — Full Tempest volatility archive

[Full instructions](07-tempest.md)

```text
Read agents/07-tempest.md and every document it references. Use my completed config/operator.local.json to implement and verify this role in my selected implementation repository. Build and verify the architecture offline. Keep every Skylit request disabled until I explicitly confirm starting collection; report live acceptance as pending.
```

## 08-dashboard — Private data library

[Full instructions](08-dashboard.md)

```text
Read agents/08-dashboard.md and every document it references. Use my completed config/operator.local.json to implement and verify this role in my selected implementation repository. Build and verify the architecture offline. Keep every Skylit request disabled until I explicitly confirm starting collection; report live acceptance as pending.
```
