# Build first; enable collection separately

The initial phase builds and verifies the architecture while all Skylit API access is disabled. This includes discovery, account/capability calls, schema refreshes, probes, samples, backfills, scheduled snapshots and streams. Use saved metadata and offline fixtures until the operator explicitly confirms starting collection.

## Enforce the boundary

Agent 00 must implement a persistent global provider-access gate, defaulting to disabled when state is absent, unreadable or unconfirmed. Check it before opening a provider connection, including retries and stream reconnects. Stop open streams and new requests when the gate changes; requests already sent cannot be recalled.

The gate applies to shared workers, legacy collectors, manual commands, startup checks and integration probes. Disable recurring launchers/cron work that could bypass it. A deployment, restart, agent continuation or passing test must not reset it to enabled. Do not repurpose or revoke credentials shared with unrelated systems as a shortcut.

Store the operator's explicit activation decision in protected runtime state with its scope and timestamp. The example operator configuration starts with `collection_enabled=false` and no confirmation. That example file is a declaration only; implementation and verification of the actual request gate are required.

## Architecture-ready acceptance

- Common contracts, catalog, jobs, adapters and dashboard are integrated or their exact remaining dependencies are reported.
- Offline behavior checks pass, including proving no transport connection occurs while paused.
- Shared and legacy request paths enforce the pause; schedules and active streams are stopped.
- Data and journals remain intact; queued work is resumable later.
- Infrastructure may be deployed within recorded authority, but health/startup checks remain offline with respect to Skylit.
- Live publication, coverage and source-boundary checks are explicitly pending, not claimed complete.

Stop at this point and report readiness. Ask for the one material decision to enable collection only when the architecture is ready for review. Do not interpret a timeout, silence or an earlier implementation authorization as activation confirmation.

## After explicit confirmation

Verify the selected account and effective limits, perform a bounded real pilot, and then admit broader backfills/forward work. Confirm real immutable publication and a fresh recurring cycle before claiming the archive is collecting successfully. A later pause overrides the earlier activation decision until renewed confirmation.
