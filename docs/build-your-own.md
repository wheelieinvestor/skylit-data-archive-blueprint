# Build your own archive

This is an implementation guide. The repository has no production collector to start and no Railway deployment button. The prompts turn the design into software in your own implementation repository.

## 1. Set up your own access and workspace

You need a Skylit account with the API access your datasets require, a Railway account if using the reference cloud layout, Git, a coding environment, and writable local storage. Verify your access and applicable usage terms with [Skylit's current API documentation](https://www.skylit.ai/docs/api-reference/introduction). Your subscription and historical coverage may differ from the reference system.

Clone or use this repository as a GitHub template. Choose a separate implementation repository for your collector and a data directory outside both repositories. Private implementation repositories are a useful default when operational material may accumulate. Public code can remain separate from private runtime configuration and data.

Python with a web framework, Postgres, an S3 client, Parquet and lossless compression is the reference approach. Pin actual dependencies and supported versions when implementing; this guide does not ship a dependency lock.

## 2. Record the operator decisions

Copy `config/operator.example.json` to `config/operator.local.json`. The latter is ignored by Git. Fill in the repository location, data directory, Railway project/environment, budget, local disk limit and historical cutoff. An empty field is an unresolved decision, not a default deployment target.

Record whether the implementation agent may provision, deploy and start collection. These permissions are for your selected research archive only. Set them once to match your intent; do not require repeated approval for an unchanged scope. API credit limits and concurrency must come from your own account and current endpoint behavior.

Do not place secret values in that configuration. It names the environment variables or secret-store references your implementation will use. `.env.example` lists suggested variable names with blank values; a file existing does not load it into a process. Implement a documented secret-loading path or configure protected service variables directly.

## 3. Start Agent 00

Open your coding agent in the cloned blueprint and paste the coordinator launcher from [agents/README.md](../agents/README.md). It reads your local choices, creates or uses the selected implementation repository, and builds the common interfaces, scheduler, catalog, reservation controls and runtime profiles.

Have Agent 00 publish the shared interface in that implementation repository before dependent adapters integrate. It should first demonstrate a bounded job with interruption recovery, shared admission and verified publication.

## 4. Build adapters in parallel

Use the remaining prompts for the families you want. All seven data-family modules plus the dashboard belong to the same implementation. Give each agent its own branch/worktree and file ownership. Reuse existing gamma/Tempest implementations where you have them; don't create duplicate backfills.

Adapters can develop against fake contexts while infrastructure is built. Actual acquisition begins only through the working coordinator with a valid lease and resource reservation. If you use fewer coding agents, implement the same roles sequentially.

## 5. Provision the selected Railway environment

Agent 00 should inspect your chosen project before creating resources. For a new archive create one project/environment with three private buckets, one small Postgres instance/metadata volume, the control service, one forward worker and the private web service. The code must exist and pass its checks before deploying application services.

| Resource | Configuration requirements |
|---|---|
| Postgres | Private access, strong credentials, bounded volume, backup and tested restore |
| Control | Database access, worker authentication, shared cost/rate controls, metadata request limits |
| Forward worker | Provider key, required bucket access, control access, bounded scratch, recoverable journal |
| Local workers | Provider key, bucket access, authenticated control URL, disk/memory limits and resume support |
| Web | Read-only catalog access, necessary results/download permissions, user authentication; no provider key |

Keep real resource IDs, credentials and generated config in your own protected implementation environment. Match service region and database networking where supported. Object storage uses its S3 endpoint; see [Railway bucket documentation](https://docs.railway.com/storage-buckets).

Do not deploy this guide as an application. Agent 00 must supply real start commands, health checks, migrations and container configuration for the code it builds, and verify the installed version after deployment. Health checks and startup must not contact Skylit while paused.

## 6. Stop at architecture-ready; obtain activation confirmation

Complete code, integration and offline tests first. Enforce the default-off request gate in shared and legacy paths, disable schedulers and verify that every attempted provider request is rejected before opening a connection. Keep live smoke tests, live schema refreshes and pilots pending. Read [activation control](activation.md).

Only after the operator explicitly confirms starting Skylit requests should the coordinator enable collection. General permission to provision/deploy does not satisfy this confirmation.

## 7. After confirmation: validate a pilot, then admit broader work

Run a bounded representative pilot to measure storage and request behavior. Verify the full fetch-to-dashboard path, incomplete/empty responses, retries, stale leases, duplicate claims and upload recovery. Include concurrent jobs from two different families before scaling parallel writers.

Freeze a historical cutoff and admit broad daily history first. Schedule observations with limited retrospective availability early. Let measured costs determine how much dense intraday data fits. A small successful pilot is a starting point, not completion of the archive.

## 8. Operate and maintain

Use the [operations guide](operations.md). Record actual costs, progress, freshness and coverage. Reconcile retained objects, reservations and provider schema changes. Complete all admitted initial partitions, verify a fresh recurring cycle, and publish private release manifests and recovery instructions.

Share code and methods if you want; keep your acquired data and operational credentials out of this public blueprint. The repository license applies to its original material, not your provider account or acquired datasets.
