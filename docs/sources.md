# Public sources

Checked while preparing this guide on September 29, 2026. Recheck current documentation before implementation.

| Source | Use |
|---|---|
| [Skylit API reference](https://www.skylit.ai/docs/api-reference/introduction) | Products, hosts, authentication links and live specifications |
| [Heatseeker public specification](https://www.skylit.ai/docs/openapi.yaml) | Source for current route/field discovery |
| [Flowseeker public specification](https://www.skylit.ai/docs/flowseeker-openapi.yaml) | Source for current route/field discovery |
| [Atlas public specification](https://www.skylit.ai/docs/atlas-openapi.yaml) | Source for current route/field discovery |
| [Railway projects](https://docs.railway.com/projects) | Resource organization |
| [Railway buckets](https://docs.railway.com/storage-buckets) | S3-compatible storage setup |
| [Bucket billing](https://docs.railway.com/storage-buckets/billing) | Retained storage, egress and plan capacity |
| [Railway pricing](https://docs.railway.com/pricing/plans) | Subscription and resource costs |
| [Cost control](https://docs.railway.com/pricing/cost-control) | Billing controls and their scope |

Live JSON specification locations documented by Skylit:

```text
https://api.skylit.ai/v1/openapi.json
https://api.skylit.ai/v1/flow/openapi.json
https://atlas-api.skylit.ai/v1/openapi.json
```

The route inventory labels Flowseeker separately. Its `flow-api.skylit.ai` alias supports the service-relative paths in that inventory, including `/v1/openapi.json`. Verify the chosen host/path combination against the current spec rather than swapping hosts blindly. Tempest routes are under `/v1/vol/` on the main API host.

The architecture and operational rules in this guide are the author's design choices. Provider documentation establishes API contracts and platform pricing; it does not establish that this entire system is deployed or that any particular data history is complete.
