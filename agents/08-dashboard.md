# Private data library

Read [COMMON.md](COMMON.md) and every required document it names before starting.

Role: `08-dashboard`.

## Objective

Build a private data-library interface over the coordinator's paginated catalog. Show all families in one place with filters for dataset, instrument, session, resolution, revision and coverage state.

Expose field definitions and provenance, actual first/last observations, gaps, source freshness, pending/completed jobs, deferred work, stored bytes and shared cost forecasts. Separate an empty/unsupported source from a failed job, and a queued partition from completed history.

Provide bounded authorized exports, using short-lived object URLs where supported. Do not load the whole archive into one JSON document or proxy large files unnecessarily through the web service. Keep provider keys out of the web app and the buckets private.

Implement authentication and authorization on catalog and download paths, pagination, safe error handling and clear empty states. Coordinate shared dependencies/deployment with Agent 00. Verify an actual new publication appears to an authorized user and anonymous access is denied. Include tests for these behaviors and report the installed version and real verification evidence.

## Assigned route inventory

No provider routes. Consume the shared catalog.

Refresh current specifications and actual access before acquisition. Keep changes to shared ownership coordinated with Agent 00.
