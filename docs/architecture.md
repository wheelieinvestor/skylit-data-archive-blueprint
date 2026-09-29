# Architecture

## One project, shared resources

```text
your-archive / research
  results-web       authenticated catalog, coverage, progress and exports
  catalog-db        small Postgres database and metadata volume
  ingest-control    shared coordination and publication service
  ingest-forward    bounded ongoing worker hosting the data adapters
  raw               compressed original responses
  curated           normalized partitions and manifests
  results           coverage reports, summaries and catalog exports

your computer
  historical workers using the same coordinator and buckets
```

Use your own resource names. A bucket is a storage resource, not another always-running worker. Create resources inside the selected project/environment; inspect existing resources before provisioning duplicates. Consult [Railway's resource documentation](https://docs.railway.com/projects).

## Responsibilities

**catalog-db** holds dataset definitions, schema versions, instrument aliases, universe membership, plans, jobs, leases, reservations, object references, partitions, revisions, coverage findings, publication events and cost snapshots. Keep full market responses out of Postgres. Back up the metadata and verify a restore.

**ingest-control** grants job ownership, checks budget and resource capacity, enforces global request permits, and commits publications. Local workers access a small authenticated API. Database access remains private. The coordinator never proxies bulk response files from local workers.

**ingest-forward** runs registered adapters for ongoing collection. Prioritize observations that disappear or cannot be reconstructed historically. Use one bounded runtime initially; add concurrency only after measuring load and testing shared ownership.

**results-web** shows searchable data coverage, field availability, revision history, job progress, costs and authorized downloads. It reads paginated metadata, not a huge in-memory JSON listing. Give it only the credentials its views require; it does not need the provider API key. Download links must remain authorized and short-lived where supported.

**Local workers** process large backfills using bounded disk and memory, persist response journals, and upload directly to object storage. Sleep interrupts local compute; it should not corrupt a publication or reset a cursor. Their disk allowance is shared across workers.

## Shared ownership and limits

Before fetching, a worker obtains a transactional job lease with an owner, expiration, heartbeat and increasing fencing token. A fencing token lets the coordinator reject a worker whose lease has expired, even if that worker later resumes.

API rate limits, concurrent requests, streams, local scratch, cloud scratch and monetary reservations belong to the whole system. A worker cannot treat a startup bucket listing as its own remaining budget. Reconcile actual usage plus all outstanding reservations centrally.

Acquisition may be retried after a crash; do not promise exactly-once HTTP requests. Guarantee that duplicate attempts cannot advance a cursor twice or publish conflicting versions under the same identity. Keep immutable objects and transactional catalog commits.

## Development agents versus running collectors

Agents 01–07 implement seven modules in one application. Agent 00 owns shared types, transport, storage, scheduling, dependencies, deployment and integration. Agent 08 owns the web interface. These development roles do not imply nine permanent paid services or LLM calls for every market-data request.

A suggested implementation layout:

```text
src/archive/
  ingestion/
    contracts.py
    catalog.py
    admission.py
    scheduler.py
    transport.py
    publication.py
    adapters/
      atlas/ flow/ contracts/ market/ dark_pool/ heat/ tempest/
  web/
tests/
configs/collection/
docs/collection/handoffs/
```

These are suggested implementation paths, not files shipped by this guide.
