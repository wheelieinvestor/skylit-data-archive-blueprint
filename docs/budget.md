# Budget and capacity

The reference target is **$150/month for the entire Railway archive**, including existing collection obligations. Your provider subscription, coding tools, hardware, internet service and taxes are separate costs to evaluate. A reference budget is not an account spending control until the implementation enforces it.

| Envelope | Monthly allocation |
|---|---:|
| Retained object storage | $60 |
| Web, coordinator, database, ongoing worker and metadata volumes | $35 |
| Cloud-service outbound traffic | $20 |
| Reserve | $35 |
| **Total** | **$150** |

These are allocations, not measured forecasts or separate allowances for each worker. See [the editable example](../config/budget.example.json).

## Cost model

As checked September 29, 2026, Railway lists bucket storage at $0.015/GB-month. S3 operations and bucket downloads are free, but uploads originating from Railway services still count as service egress; buckets are outside the private service network. Hobby has a combined 1 TB bucket capacity limit. A 4 TB plan therefore requires an eligible larger tier. [Bucket billing](https://docs.railway.com/storage-buckets/billing).

Published container rates are $10/GB-month RAM, $20/vCPU-month, $0.15/GB-month volume storage, and $0.05/GB service egress. Account subscription minimums and included usage affect the actual invoice. Verify your tier and avoid counting the same included usage or subscription twice. [Resource pricing](https://docs.railway.com/pricing/plans).

Using decimal GB for this planning calculation:

```text
4,000 GB retained × $0.015 = $60/month storage
400 GB outbound × $0.05 = $20 service egress
```

A 2,800 GB upload from a cloud service would cost about $140 in service egress at that rate, before storage and compute. Uploading from your computer directly to the bucket avoids that Railway service charge; your own network costs and constraints still apply.

The 4 TB figure is a possible budget ceiling, not preallocated space or permission to fill it. Include compressed raw files, curated duplicates, revisions, metadata backups and abandoned uploads when measuring retained bytes. Do not confuse GB with GiB or physical bucket capacity with affordable capacity.

## Admission

Maintain separate forecasts for the remainder of the billing cycle and a full future month at the accepted retention level. Avoid counting accrued storage twice: the cycle forecast adds only remaining-cycle storage to accrued charges; the steady-state forecast uses full-month retained storage. Include:

- Actual attributable accrued charges.
- Committed remaining compute/volume and egress costs.
- Newly reserved work across every worker.
- Retention from existing objects and accepted future outputs.
- Protected operational headroom.

Both forecasts must remain inside the chosen cap. Reconcile the ledger with actual object bytes and platform usage. If telemetry is stale, use conservative commitments, not an assumption of zero usage. Pause discretionary dense work before consuming the reserve.

The reference local cap is **10 GiB aggregate working data** across all workers. Reserve scratch/cache/journal capacity centrally and retain a configurable free-space floor. Evict only local cache copies whose remote objects have been verified. No automatic deletion of retained history is part of this design.

Use project-specific admission rather than a workspace-wide hard stop that could affect unrelated services. Stored objects continue to create costs even when workers stop. See [Railway cost control](https://docs.railway.com/pricing/cost-control).
