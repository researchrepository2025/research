# F34: On-Premises API Gateway & Service Discovery

## Executive Summary

Deploying an API gateway entirely on-premises eliminates cloud-native managed API management (AWS API Gateway, Azure APIM, Google Cloud Endpoints) and forces ISVs to self-operate every layer of the API control plane: gateway software, its backing datastore, distributed rate limiting infrastructure, a self-hosted identity provider, and service discovery tooling. The leading open-source options — Kong, Apache APISIX, Tyk, and KrakenD — each carry distinct infrastructure dependencies and operational profiles that range from a single stateless binary (KrakenD) to multi-component stacks requiring etcd clusters, Redis sentinels, and PostgreSQL (APISIX, Tyk). Raw gateway throughput is high enough for most enterprise workloads, with Kong achieving [130,014 RPS at a P99 latency of 6.01ms in proxy-only configuration](https://developer.konghq.com/gateway/performance/benchmarks/) on a single 16-vCPU node; however, each additional plugin (rate limiting, authentication) adds measurable latency overhead and operational surface area. Traffic management capabilities — canary routing, A/B testing, traffic splitting — that cloud providers deliver as managed features must be hand-configured through gateway plugins, Consul service splitters, or weighted upstream definitions, each requiring dedicated operational expertise. The cumulative staffing burden for a mid-size on-premises gateway deployment serving 50 enterprise customers is estimated at 1.5–3.0 FTE, excluding on-call rotation, making on-premises API gateway management one of the most operationally intensive commitments in the self-hosted stack.

---

## 1. Gateway Platform Landscape

Four open-source API gateways dominate the self-hosted, on-premises market. Each is architected differently, creating radically different operational profiles.

### 1.1 Kong Gateway

Kong is the most widely deployed self-hosted gateway. It operates in three topologies: [Traditional, Hybrid, and DB-less](https://developer.konghq.com/gateway/deployment-topologies/).

[FACT] "Every Kong Gateway node runs as both a Control Plane (CP) and Data Plane (DP)" in Traditional mode — the only topology supporting database-dependent plugins such as cluster-strategy rate limiting and OAuth2 out of the box.
URL: https://developer.konghq.com/gateway/deployment-topologies/

[FACT] In Hybrid mode, "the availability of the database does not affect the availability of the Data Planes" and "if a Control Plane is offline, Data Planes will run using their last known configuration."
URL: https://developer.konghq.com/gateway/deployment-topologies/

[FACT] DB-less mode eliminates the database dependency entirely but makes the Admin API read-only, limiting dynamic configuration to declarative YAML/JSON files committed to version control.
URL: https://developer.konghq.com/gateway/deployment-topologies/

[FACT] Hybrid mode "allows groups of Data Planes in different data centers, geographies, or zones without needing a local clustered database for each DP group," enabling multi-site on-premises deployments.
URL: https://developer.konghq.com/gateway/deployment-topologies/

[FACT] Kong plugins are written in Lua, and "most AI engineers and ML Ops teams live in Python but do not know Lua, so if custom guardrails are needed, one must hire a Lua specialist or spend valuable engineering time learning a niche language."
URL: https://api7.ai/blog/kong-konnect-pricing

### 1.2 Apache APISIX

APISIX, governed by the Apache Foundation, uses etcd as its configuration store. [APISIX offers three deployment modes](https://apisix.apache.org/docs/apisix/deployment-modes/): Traditional, Decoupled, and Standalone.

[FACT] APISIX requires etcd v3.4.0 or later and communicates with the etcd cluster over HTTP(S) — not gRPC directly — requiring that the etcd gRPC gateway be enabled.
URL: https://apisix.apache.org/docs/apisix/deployment-modes/

[FACT] "By default Apache APISIX uses HTTP protocol to talk with etcd cluster, which is insecure. Please configure certificate and corresponding private key for your etcd cluster."
URL: https://apisix.apache.org/docs/apisix/FAQ/

[FACT] APISIX Standalone mode, introduced to eliminate the etcd dependency, operates via file-driven configuration with checks every second for changes, or through an API-driven mode that stores configuration in memory.
URL: https://apisix.apache.org/docs/apisix/deployment-modes/

[FACT] APISIX supports integration with multiple service discovery systems including Consul, Eureka, Nacos, and DNS SRV-compatible systems.
URL: https://docs.api7.ai/apisix/how-to-guide/service-discovery/consul-integration/

[FACT] For production HA, etcd must be deployed as a 3 or 5 member cluster; APISIX "will automatically failover to other members if one becomes unavailable."
URL: https://apisix.apache.org/docs/apisix/deployment-modes/

### 1.3 Tyk

Tyk is a Go-based gateway offering full API lifecycle management. It carries the most complex infrastructure dependency profile of the four options examined.

[FACT] Tyk Gateway has a hard dependency on Redis; "it is advisable to not treat Redis instances as ephemeral" and Redis must be persisted or configured for easy failover.
URL: https://tyk.io/docs/planning-for-production/database-settings

[FACT] Tyk Dashboard requires either PostgreSQL (versions 13.x through 17.x) or MongoDB (versions 5.0.x, 6.0.x, 7.0.x) as a backing store. Enterprise Developer Portal requires PostgreSQL; MongoDB is not supported for that component.
URL: https://tyk.io/docs/planning-for-production/database-settings

[FACT] Tyk supports Redis Sentinel from v2.9.3, and Gateway, Dashboard, and Pump all support Redis Sentinel integration.
URL: https://tyk.io/docs/planning-for-production/database-settings

[FACT] Tyk supported Redis versions for Tyk 5.3+: Redis 6.2.x, 7.0.x, 7.2.x. For Tyk 5.2 and earlier, only Redis 6.0.x and 6.2.x are supported.
URL: https://tyk.io/docs/planning-for-production/database-settings

[STATISTIC] Storage estimate for Tyk: 1 million daily requests generates approximately 1GB request logs + 1MB aggregate stats monthly, totaling approximately 30GB requests and 30MB aggregates per month.
URL: https://tyk.io/docs/planning-for-production/database-settings

[FACT] Production topology for Tyk separates all components: "two or more Tyk Gateway nodes (load balanced, each Gateway installed on separate machines)," dedicated MongoDB/PostgreSQL cluster, separate Redis with failover, and individual Dashboard and Pump instances.
URL: https://tyk.io/docs/planning-for-production/database-settings

### 1.4 KrakenD

KrakenD is a stateless, declarative API gateway written in Go. It has no external database dependency, making it the operationally simplest option but also the most limited for stateful features.

[FACT] KrakenD operates as a stateless API gateway using JSON-based declarative configuration. There is no database, no Admin API at runtime, and no state shared between instances.
URL: https://api7.ai/learning-center/api-gateway-guide/api-gateway-comparison-apisix-kong-traefik-krakend-tyk

[STATISTIC] KrakenD processed close to 1 million requests per second in a 20-machine cluster and achieves 70,000+ RPS on a single standard hardware node.
URL: https://www.krakend.io/docs/benchmarks/api-gateway-benchmark/

[FACT] KrakenD "uses 40% less CPU than competitors at 5,000 RPS" in comparative benchmark configurations.
URL: https://api7.ai/learning-center/api-gateway-guide/api-gateway-comparison-apisix-kong-traefik-krakend-tyk

---

## 2. Performance Benchmarks

Gateway-introduced latency directly affects end-user SLAs. The figures below represent vendor-published benchmarks and should be treated as best-case performance under controlled conditions.

### 2.1 Kong Gateway (Official Benchmarks, Gateway 3.13)

Testing was conducted on a single AWS EC2 c5.4xlarge (16 vCPU) using HTTPS, averaged across five 15-minute test runs. [Source: Kong official benchmarks](https://developer.konghq.com/gateway/performance/benchmarks/)

| Test Scenario | Routes/Consumers | RPS | P95 Latency | P99 Latency |
|---|---|---|---|---|
| Proxy only (no plugins) | 1 route / 0 consumers | 130,014 | 3.55ms | 6.01ms |
| Proxy only (no plugins) | 100 routes / 0 consumers | 125,804 | 3.51ms | 6.11ms |
| Rate limiting (no auth) | 100 routes / 0 consumers | 108,436 | 3.93ms | 7.85ms |
| Rate limiting + key auth | 100 routes / 100 consumers | 92,707 | 4.75ms | 9.46ms |
| Rate limiting + basic auth | 100 routes / 100 consumers | 86,827 | 5.40ms | 10.09ms |

[FACT] Each additional plugin layer (rate limiting, authentication) reduces Kong's throughput by approximately 14–33% from the proxy-only baseline.
URL: https://developer.konghq.com/gateway/performance/benchmarks/

### 2.2 KrakenD (Official Benchmarks)

An older KrakenD benchmark (2016 hardware) showed [KrakenD achieving 3,479 RPS vs. Kong at 1,754 RPS and Tyk at 451 RPS on identical hardware](https://www.krakend.io/docs/benchmarks/api-gateway-benchmark/). Hardware was an Intel Core i7 2.2 GHz MacBook Pro. Note: [PRE-2025: 2016] — no 2025 hardware-equivalent benchmark from KrakenD is publicly available at time of writing; the 70,000 RPS / 1M RPS cluster figures are from vendor marketing pages.

[FACT] KrakenD's P99 latency in the 2016 benchmark was 77.1ms and average latency was 28.7ms on low-end consumer hardware. Modern server hardware with HTTP/2 and TLS session resumption reduces this significantly.
URL: https://www.krakend.io/docs/benchmarks/api-gateway-benchmark/

### 2.3 TLS Termination Overhead

[FACT] "The biggest performance hit when doing TLS decryption is the initial handshake." Techniques including keep-alive connections, HTTP/2 session reuse, and TLS session resumption significantly reduce this per-request cost.
URL: https://www.haproxy.com/blog/http-keep-alive-pipelining-multiplexing-and-connection-pooling

[FACT] "Starting August 31, 2025, all clients and backend servers interacting with Azure Application Gateway must use Transport Layer Security (TLS) 1.2 or higher." This industry mandate applies pressure for on-premises gateways to deprecate TLS 1.0/1.1 configurations.
URL: https://docs.azure.cn/en-us/application-gateway/application-gateway-faq

[FACT] HTTP/2 multiplexing "allows multiple concurrent requests/responses to be multiplexed over a single connection," eliminating per-request TCP and TLS handshake costs when properly configured between gateway and upstream services.
URL: https://www.haproxy.com/blog/http-keep-alive-pipelining-multiplexing-and-connection-pooling

---

## 3. Distributed Rate Limiting Without Cloud-Native Services

Cloud-managed API gateways (AWS API Gateway, Azure APIM) handle distributed rate limiting as a first-class managed service. On-premises deployments must implement this themselves using a shared datastore, typically Redis.

[FACT] "Redis serves as a fast, in-memory data store that all gateway instances can access and acts as the central source of truth for all token bucket state" in distributed rate limiting architectures.
URL: https://codescoddler.medium.com/designing-a-distributed-api-rate-limiter-8f688290220f

[STATISTIC] "A single Redis node handles approximately 100k operations/second, with each check requiring ~2 operations (supporting ~50k RPS per node)."
URL: https://www.hellointerview.com/learn/system-design/problem-breakdowns/distributed-rate-limiter

[FACT] Redis Lua scripting is required to handle race conditions in distributed rate limiting: "bundles the logic into a Lua script that Redis executes as a single atomic unit, completely eliminating race conditions."
URL: https://www.freecodecamp.org/news/build-rate-limiting-system-using-redis-and-lua/

[FACT] WSO2 API Manager's fallback behavior when Redis is unavailable: "the fallback option is to have node-local counters." This means gateway instances enforce per-node limits independently, allowing aggregate overshoot during Redis outages.
URL: https://apim.docs.wso2.com/en/latest/manage-apis/design/rate-limiting/advanced-topics/configuring-rate-limiting-api-gateway-cluster/

[FACT] Tyk requires Redis for all API token and OAuth client storage. Rate limit counters are stored in Redis and are lost if Redis is not configured with persistence.
URL: https://tyk.io/docs/planning-for-production/database-settings

### Rate Limiting Algorithm Comparison

| Algorithm | Burst Handling | Accuracy | Redis Key Count |
|---|---|---|---|
| Fixed Window Counter | Poor (double burst at boundary) | Low | 1 per client |
| Sliding Window Log | Perfect | High | O(events per window) |
| Token Bucket | Controlled burst | High | 2 per client |
| Leaky Bucket | No burst (smoothed) | High | 1 per client |

[FACT] The Token Bucket algorithm "is widely selected for rate limiting due to its ability to gracefully handle legitimate bursts of traffic while enforcing a strict long-term average rate."
URL: https://redis.io/tutorials/howtos/ratelimiting/

---

## 4. Authentication at the Gateway Layer

On-premises deployments cannot use cloud-native auth services (AWS Cognito, Azure AD B2C, Google Identity Platform) natively. ISVs must deploy and operate a self-hosted identity stack.

### 4.1 Keycloak as the Standard Self-Hosted IdP

[FACT] Keycloak is an open-source identity and access management solution that "supports standard protocols like OAuth2, OpenID Connect, and SAML" and can delegate authentication to other IdPs as a broker.
URL: https://www.keycloak.org/

[FACT] "A realm in Keycloak is the equivalent of a tenant; realms are isolated from one another and can only manage and authenticate their users," enabling multi-tenant API key and token management for an ISV's enterprise customers.
URL: https://medium.com/@nsalexamy/keycloak-and-spring-boot-oauth-2-0-and-openid-connect-oidc-authentication-304e7b511d02

[FACT] APISIX demonstrates Keycloak integration using OpenID Connect: the gateway "handles user authentication, and once authenticated, decode the JWT token and pull out the unique identity id (sub), and add it to the request headers for backend services to use."
URL: https://apisix.apache.org/blog/2022/07/06/use-keycloak-with-api-gateway-to-secure-apis/

### 4.2 JWT Validation

[FACT] A critical security concern in self-hosted JWT validation: attackers can switch the token's algorithm field to "none," and "some libraries incorrectly skip signature verification entirely when this occurs."
URL: https://securityboulevard.com/2026/01/api-authentication-methods-explained-api-keys-oauth-jwt-hmac-compared/

[FACT] For token revocation in self-hosted environments: "Keep your access tokens short-lived (think 5-15 minutes) and use refresh tokens to get new ones." Additionally, "using a fast cache like Redis to store 'revoked' token ids" provides revocation capability while maintaining performance.
URL: https://securityboulevard.com/2026/01/api-authentication-methods-explained-api-keys-oauth-jwt-hmac-compared/

### 4.3 API Key Management

[FACT] API keys "remain valid indefinitely once exposed, unlike tokens with expiration." Rotation requires "grace periods where old and new keys coexist briefly before deprecation." On-premises deployments must build or configure this lifecycle without managed rotation services.
URL: https://securityboulevard.com/2026/01/api-authentication-methods-explained-api-keys-oauth-jwt-hmac-compared/

[FACT] For self-hosted API key management: "implement rate limiting per key and mandatory secret storage in secure vaults rather than environment files."
URL: https://securityboulevard.com/2026/01/api-authentication-methods-explained-api-keys-oauth-jwt-hmac-compared/

---

## 5. Request Routing and Transformation

### 5.1 Kong Request Transformation

[FACT] Kong Gateway's built-in Request Transformer plugin "allows you to configure requests to transform those requests—mutating headers, query string parameters, the request body and so on—before forwarding those requests to their final destination."
URL: https://docs.konghq.com/hub/kong-inc/request-transformer/

[FACT] Complex URL rewriting in Kong requires the Request Transformer Advanced plugin, which is "bundled with Kong Enterprise" (not the open-source edition). It supports Lua expressions within placeholder evaluation for dynamic header values.
URL: https://docs.konghq.com/hub/kong-inc/request-transformer-advanced/

[FACT] Kong's Request Transformer plugin is compatible with DB-less mode, enabling transformation functionality in declarative on-premises deployments without a database dependency.
URL: https://docs.konghq.com/hub/kong-inc/request-transformer/

### 5.2 APISIX Traffic-Split Plugin

[FACT] APISIX's traffic-split plugin supports weight-based routing. A basic 50/50 split example from official documentation:

```yaml
routes:
  - uri: /api/v1/resource
    upstream:
      nodes:
        "service-v1:80": 50
        "service-v2:80": 50
      type: roundrobin
```

URL: https://api7.ai/learning-center/api-gateway-guide/ab-testing-canary-release-api-gateway

[FACT] APISIX supports user-segment routing via header-based conditional variables. Routes use `vars` conditions (e.g., `["http_x-user-group", "==", "A"]`) to direct specific user cohorts to specific upstream versions.
URL: https://api7.ai/learning-center/api-gateway-guide/ab-testing-canary-release-api-gateway

### 5.3 Protocol Translation

[FACT] On-premises gateways can handle format conversion at the gateway layer: "If an old system requires XML but a new system uses JSON, you can ensure compatibility by dynamically converting data formats at the API gateway."
URL: https://konghq.com/blog/engineering/api-gateway-request-transformation

---

## 6. Service Discovery

On-premises environments do not benefit from cloud-provider DNS (Route 53, Azure DNS, GCP Cloud DNS) with automatic health-checked service registration. Service discovery must be self-operated.

### 6.1 Consul

[FACT] Consul "maintains a service catalog [that] acts as a single source of truth that allows your services to query and communicate with each other" and supports both client-side and server-side discovery patterns.
URL: https://developer.hashicorp.com/consul/docs/use-case/service-discovery

[FACT] Consul can be "implemented across any type of infrastructure, whether it is on-premise or in the cloud," and supports virtual machines, containers, serverless, and container orchestration platforms.
URL: https://developer.hashicorp.com/consul/docs/use-case/service-discovery

[FACT] Consul has a built-in DNS interface allowing services to be found using standard DNS queries. Unhealthy service instances are automatically removed from the load balancing pool through health check integration.
URL: https://developer.hashicorp.com/consul/docs/use-case/service-discovery

[FACT] APISIX supports Consul integration for service discovery; configuration requires only DNS SRV-compatible keys.
URL: https://docs.api7.ai/apisix/how-to-guide/service-discovery/consul-integration/

### 6.2 etcd

[FACT] "etcd does not have a built-in DNS interface, and to use DNS-based service discovery with etcd, you need to deploy extra components such as CoreDNS or SkyDNS."
URL: https://slickfinch.com/consul-vs-etcd-service-discovery-tools-comparison/

[FACT] etcd is required as APISIX's configuration store in Traditional and Decoupled deployment modes; minimum supported version is etcd v3.4.0.
URL: https://apisix.apache.org/docs/apisix/deployment-modes/

### 6.3 KrakenD Service Discovery

[FACT] KrakenD integrates with DNS SRV-based service discovery, supporting Consul and Kubernetes-compatible systems, configured via the `sd` and `scheme` keys in backend definitions.
URL: https://www.krakend.io/docs/backends/service-discovery/

---

## 7. Traffic Management: Canary, A/B Testing, and Traffic Splitting

### 7.1 Self-Hosted Canary Patterns

[FACT] Apache APISIX, Kong, and Envoy "provide traffic routing and observability features essential for controlled rollouts" without cloud-native dependency.
URL: https://api7.ai/learning-center/api-gateway-guide/ab-testing-canary-release-api-gateway

[FACT] Canary pattern in APISIX: traffic is split (e.g., 90% to v1, 10% to v2), verification is performed, and "if successful, traffic to v2 is increased (20%, 50%…), eventually making v2 become the new v1."
URL: https://api7.ai/learning-center/api-gateway-guide/ab-testing-canary-release-api-gateway

[FACT] A/B testing use case: "Test different versions to optimize UX" with traffic divided by user segments, presenting low risk through controlled test groups. Canary releases "gradually roll out a new API version" with progressively increasing traffic and medium risk requiring monitoring and rollback capability.
URL: https://api7.ai/learning-center/api-gateway-guide/ab-testing-canary-release-api-gateway

### 7.2 Consul Service Splitters for Canary

[FACT] Consul service splitters "enable splitting of layer-7 (L7) traffic, using Envoy proxies configured by Consul, to roll out a new version of a service."
URL: https://developer.hashicorp.com/consul/tutorials/control-network-traffic/service-splitters-canary-deployment

[FACT] For additional orchestration, Argo Rollouts can "orchestrate the progressive delivery (the Canary logic), while Traefik Proxy serves as an Ingress Controller and Gateway" in self-hosted Kubernetes-adjacent deployments.
URL: https://medium.com/@nsalexamy/canary-deployments-with-argo-rollouts-gateway-api-and-traefik-on-kubernetes-358ae2cdcd4f

---

## 8. Circuit Breaking and Retry Policies for Service-to-Service Communication

### 8.1 Circuit Breaking

[FACT] Istio "simplifies configuration of service-level properties like circuit breakers, timeouts, and retries" through Envoy proxy sidecars. For non-Kubernetes on-premises environments, Consul's ServiceDefaults configuration entry achieves equivalent circuit breaking.
URL: https://istio.io/latest/docs/concepts/traffic-management/

[FACT] In Consul service mesh, "you can set circuit breaker values by creating a ServiceDefaults configuration entry on the source service, which will apply for requests sent towards the destination service."
URL: https://developer.hashicorp.com/consul/tutorials/control-network-traffic/service-mesh-circuit-breaking

### 8.2 Retry Policies

[FACT] Kubernetes Gateway API v1.4.0, released October 6, 2025, achieves General Availability and includes enhanced gRPC route (GRPCRoute) capabilities with retry support.
URL: https://kubernetes.io/blog/2025/11/06/gateway-api-v1-4/

[FACT] A 2025 research paper (RetryGuard) identifies retry storms as a systemic risk in cloud microservice architectures: "various cloud providers and service mesh platforms offer specific recommendations to optimize retry mechanisms while avoiding pitfalls."
URL: https://arxiv.org/html/2511.23278v1

---

## 9. API Versioning and Lifecycle Without a Managed Developer Portal

Cloud-native platforms (AWS API Gateway stages, Azure APIM developer portal) provide managed versioning, documentation hosting, and consumer notification. On-premises ISVs must replicate this with self-hosted tooling.

### 9.1 Versioning Strategies

[FACT] URL path versioning (`/v1/`, `/v2/`) is the recommended approach for public APIs: "Its clarity and operational simplicity are unbeatable when you have thousands of consumers." Advantages include: explicit versioning, debuggable, cache-friendly, and independent infrastructure per version.
URL: https://apidog.com/blog/api-versioning-deprecation-strategy/

[FACT] Breaking changes requiring new API versions include: removing or renaming fields, changing data types, making optional fields required, removing endpoints, and changing authentication requirements. Non-breaking changes (adding new fields, endpoints, enum values) do not require a new version.
URL: https://apidog.com/blog/api-versioning-deprecation-strategy/

### 9.2 Deprecation Headers and Sunset Process

[FACT] RFC 8594 defines the `Sunset` header standard. Deprecation implementation: add `Deprecation: true` header and `Sunset: Wed, 31 Dec 2025 23:59:59 GMT` to all deprecated version responses, beginning at Month 1 of the deprecation cycle.
URL: https://apidog.com/blog/api-versioning-deprecation-strategy/

[FACT] A 12-month deprecation timeline is the industry recommended minimum: Months 0-1 (documentation and testing), Month 1 (add headers), Months 2-9 (migration guides and direct engagement), Month 10 (final warning), Month 11 (enhanced monitoring), Month 12 (sunset — return `410 Gone` if traffic near zero).
URL: https://apidog.com/blog/api-versioning-deprecation-strategy/

[FACT] "Never Break Without Warning — achieve zero active traffic before turning off deprecated versions through relentless communication and easy migration paths."
URL: https://apidog.com/blog/api-versioning-deprecation-strategy/

### 9.3 Self-Hosted Developer Portals

[FACT] Backstage (open-source, created by Spotify) "provides a highly extensible platform for building internal portals, including APIs, services, docs, and infra components." Teams can "see the spec of each API, and understand versioning or lifecycle without duplicating effort."
URL: https://roadie.io/backstage/plugins/api-docs/

[FACT] The Backstage API Docs plugin supports separate Swagger documents per version (e.g., `swagger/v1/swagger.json` and `swagger/v2/swagger.json`) and can be configured with version selection dropdowns.
URL: https://moldstud.com/articles/p-a-developers-guide-to-navigating-api-versioning-challenges-and-solutions-with-swagger

[FACT] Tyk includes a built-in Enterprise Developer Portal, but this component requires PostgreSQL — MongoDB is not supported.
URL: https://tyk.io/docs/planning-for-production/database-settings

---

## 10. Operational Comparison Table

Assumptions: Mid-size on-premises deployment serving 50 enterprise customers; single data center; 2 gateway nodes in HA; dedicated infrastructure team supporting the gateway stack as part of a broader on-premises responsibility.

| Capability | On-Premises | Managed K8s | Cloud-Native |
|------------|-------------|-------------|--------------|
| **Gateway Software** | Difficulty: 4/5 | Difficulty: 3/5 | Difficulty: 1/5 |
| | Deploy, patch, HA-configure Kong/APISIX/Tyk; own database (PostgreSQL/Redis/etcd) | Helm-managed with K8s operators; cloud storage for state | Fully managed (AWS API Gateway, Azure APIM) |
| | Kong, APISIX, Tyk, KrakenD | Kong Ingress Controller, Traefik, NGINX Ingress | AWS API Gateway, Azure APIM, GCP APIGEE |
| | Est. FTE: 0.5–1.0 | Est. FTE: 0.25–0.5 | Est. FTE: 0.1–0.25 |
| **Distributed Rate Limiting** | Difficulty: 4/5 | Difficulty: 3/5 | Difficulty: 1/5 |
| | Redis Cluster required; Lua scripts for atomicity; fallback-to-local on Redis failure | Redis via managed cache (ElastiCache/Azure Cache); K8s operator | Native, zero-config; per-route in console |
| | Redis Cluster, Redis Sentinel, custom Lua | Redis (cloud-managed), K8s rate limit CRDs | Cloud provider managed; no Redis ops |
| | Est. FTE: 0.25–0.5 | Est. FTE: 0.1–0.25 | Est. FTE: 0.0 |
| **Authentication (JWT/OAuth2)** | Difficulty: 4/5 | Difficulty: 3/5 | Difficulty: 2/5 |
| | Self-host Keycloak + PostgreSQL; configure JWT signing keys; build rotation pipeline | Keycloak on K8s (statefulset) or cloud OIDC hybrid | Cognito, Azure AD B2C, Google Identity; managed JWKS rotation |
| | Keycloak, Dex, Ory Hydra | Keycloak Operator, cloud IdP hybrid | Cognito, Auth0, Azure AD B2C |
| | Est. FTE: 0.25–0.5 | Est. FTE: 0.1–0.25 | Est. FTE: 0.05–0.1 |
| **Service Discovery** | Difficulty: 3/5 | Difficulty: 2/5 | Difficulty: 1/5 |
| | Deploy and operate Consul (3-node HA) or etcd cluster; configure health checks; integrate with gateway | Kubernetes-native DNS (CoreDNS); optional Consul on K8s | Cloud DNS + health checks; zero ops |
| | Consul, etcd + CoreDNS, DNS SRV | CoreDNS, Consul on K8s, AWS Cloud Map | Route 53, Azure DNS, GCP Cloud DNS |
| | Est. FTE: 0.25–0.5 | Est. FTE: 0.1–0.2 | Est. FTE: 0.0 |
| **Traffic Management (Canary/A/B)** | Difficulty: 4/5 | Difficulty: 3/5 | Difficulty: 2/5 |
| | Gateway plugin config; Consul service splitters; manual weight adjustment; no auto-rollback without additional tooling | Argo Rollouts + Gateway API; K8s HTTPRoute weights; automated analysis | Managed canary (Lambda weighted aliases, APIM revisions, Apigee A/B) |
| | APISIX traffic-split plugin, Consul splitters, Argo Rollouts | Argo Rollouts, Flagger, K8s Gateway API | Cloud-native canary features |
| | Est. FTE: 0.1–0.25 | Est. FTE: 0.05–0.1 | Est. FTE: 0.0 |
| **API Versioning & Developer Portal** | Difficulty: 4/5 | Difficulty: 3/5 | Difficulty: 2/5 |
| | Self-host Backstage + configure Swagger UI; maintain Deprecation/Sunset headers manually; consumer notification via email | Backstage on K8s or cloud-hosted; similar config complexity | Managed portals (AWS API Gateway developer portal, Azure APIM portal, Apigee) |
| | Backstage, Swagger UI, Redoc, manual email pipelines | Backstage, Redoc, cloud portals | Azure APIM Developer Portal, Apigee Hub |
| | Est. FTE: 0.1–0.25 | Est. FTE: 0.1–0.2 | Est. FTE: 0.05–0.1 |

**Total On-Premises FTE Estimate: 1.5–3.0 FTE** (active engineering + operations, excluding on-call burden)
**Total Managed K8s FTE Estimate: 0.7–1.5 FTE**
**Total Cloud-Native FTE Estimate: 0.2–0.55 FTE**

[UNVERIFIED] FTE estimates are synthesized from vendor documentation on operational scope, a published range of "0.5–2 FTE for manual operations" for API gateway management (digitalapi.ai), and standard platform engineering benchmarks. No Gartner or Forrester report specifically quantifying API gateway staffing for mid-size ISVs was found in 2025 sources.

---

## 11. Gateway Platform Infrastructure Dependency Summary

| Gateway | Configuration Store | Rate Limit Store | Auth Store | Min HA Nodes (Store) |
|---|---|---|---|---|
| Kong (Traditional) | PostgreSQL | PostgreSQL | PostgreSQL | 2+ (DB cluster) |
| Kong (Hybrid) | PostgreSQL (CP only) | Redis | PostgreSQL/Redis | 1 CP + 2 DP |
| Kong (DB-less) | None (YAML/JSON) | Redis (if used) | External IdP | None |
| APISIX (Traditional/Decoupled) | etcd | Redis | External IdP | 3-node etcd cluster |
| APISIX (Standalone) | File / Memory | Redis | External IdP | None |
| Tyk | Redis + PostgreSQL/MongoDB | Redis | Redis + external IdP | Redis Sentinel + DB cluster |
| KrakenD | None (JSON config file) | External Redis | External IdP | None |

---

## Key Takeaways

- **Every cloud-managed API feature becomes a self-operated system.** Rate limiting requires Redis Cluster with Lua atomicity. Auth requires a self-hosted IdP (typically Keycloak) backed by its own PostgreSQL. Service discovery requires Consul or etcd cluster. Each is a separate operational concern with its own HA, patching, and monitoring requirements.

- **KrakenD minimizes infrastructure dependencies at the cost of stateful features.** It is the only gateway with no mandatory external datastore, making it the lowest operational burden — but it cannot natively support cluster-strategy rate limiting, OAuth2 flows, or dynamic admin configuration without external systems.

- **Kong's Traditional mode is the gateway model most comparable to cloud-native API management in features, but it concentrates risk.** A compromised Traditional-mode node exposes the entire configuration database. Hybrid mode resolves this but requires additional operational complexity to manage the CP/DP separation.

- **Performance headroom is not the bottleneck in on-premises API gateway deployments.** Kong achieves 130,000+ RPS at 6ms P99 on a single 16-vCPU node; throughput rarely constrains on-premises ISV deployments serving 50 enterprise customers. The operational burden of maintaining the supporting infrastructure — not the gateway's raw performance — is the primary cost driver.

- **API versioning and consumer lifecycle management without a managed developer portal requires explicit process investment.** RFC 8594's `Sunset`/`Deprecation` headers are the standard signaling mechanism, but consumer notification, usage monitoring, and migration tracking must be built and staffed — they are not provided by the gateway software itself.

---

## Related — Out of Scope

- **K8s service mesh (Istio, Linkerd, Cilium):** Envoy-based circuit breaking and retry policies within Kubernetes are covered by F55. This file covers application-level service-to-service resilience only.
- **Network infrastructure and hardware load balancers:** Physical load balancers (F5, Citrix ADC), VLANs, and datacenter network topology are covered by F40.
- **Microservices lifecycle management:** Service registration, deployment orchestration, and container lifecycle beyond the gateway and discovery layer are covered by F32.
- **AI/LLM-specific API gateway features:** Token-based rate limiting, model routing, and prompt caching at the gateway layer are an emerging 2025 product category (Kong AI Gateway, Portkey, LiteLLM) that intersects with this topic but is outside this file's scope.

---

## Sources

- [Kong Gateway Deployment Topologies](https://developer.konghq.com/gateway/deployment-topologies/)
- [Kong Gateway Performance Benchmarks (Official, v3.13)](https://developer.konghq.com/gateway/performance/benchmarks/)
- [Kong Gateway Resource Sizing Guidelines](https://developer.konghq.com/gateway/resource-sizing-guidelines/)
- [Kong Request Transformer Plugin](https://docs.konghq.com/hub/kong-inc/request-transformer/)
- [Kong Request Transformer Advanced Plugin](https://docs.konghq.com/hub/kong-inc/request-transformer-advanced/)
- [Kong Common API Gateway Transformation Patterns](https://konghq.com/blog/engineering/api-gateway-request-transformation)
- [Kong API Versioning Guidelines](https://konghq.com/blog/engineering/service-design-guidelines-api-versioning)
- [Kong 2025 Pricing Analysis](https://api7.ai/blog/kong-konnect-pricing)
- [Apache APISIX Deployment Modes](https://apisix.apache.org/docs/apisix/deployment-modes/)
- [Apache APISIX FAQ (etcd security)](https://apisix.apache.org/docs/apisix/FAQ/)
- [APISIX Consul Integration](https://docs.api7.ai/apisix/how-to-guide/service-discovery/consul-integration/)
- [APISIX + Keycloak Integration](https://apisix.apache.org/blog/2022/07/06/use-keycloak-with-api-gateway-to-secure-apis/)
- [Tyk Database Settings & Production Requirements](https://tyk.io/docs/planning-for-production/database-settings)
- [Tyk Redis Configuration](https://tyk.io/docs/4.1/planning-for-production/redis/)
- [Tyk Performance Benchmarks](https://tyk.io/performance-benchmarks/)
- [KrakenD API Gateway Benchmark](https://www.krakend.io/docs/benchmarks/api-gateway-benchmark/)
- [KrakenD Service Discovery](https://www.krakend.io/docs/backends/service-discovery/)
- [API Gateway Comparison: APISIX vs Kong vs KrakenD vs Tyk (API7.ai)](https://api7.ai/learning-center/api-gateway-guide/api-gateway-comparison-apisix-kong-traefik-krakend-tyk)
- [A/B Testing and Canary Releases with API Gateways (API7.ai)](https://api7.ai/learning-center/api-gateway-guide/ab-testing-canary-release-api-gateway)
- [API Release Strategies (API7.ai)](https://api7.ai/blog/api-release-strategies-with-api-gateway)
- [Consul Service Discovery Documentation](https://developer.hashicorp.com/consul/docs/use-case/service-discovery)
- [Consul Circuit Breaking Tutorial](https://developer.hashicorp.com/consul/tutorials/control-network-traffic/service-mesh-circuit-breaking)
- [Consul Canary Deployments with Service Splitters](https://developer.hashicorp.com/consul/tutorials/control-network-traffic/service-splitters-canary-deployment)
- [Consul vs etcd Service Discovery Comparison](https://slickfinch.com/consul-vs-etcd-service-discovery-tools-comparison/)
- [Distributed Rate Limiter Design (HelloInterview)](https://www.hellointerview.com/learn/system-design/problem-breakdowns/distributed-rate-limiter)
- [Designing a Distributed API Rate Limiter (Medium)](https://codescoddler.medium.com/designing-a-distributed-api-rate-limiter-8f688290220f)
- [WSO2 Distributed Rate Limiting (Cluster Gateway)](https://apim.docs.wso2.com/en/latest/manage-apis/design/rate-limiting/advanced-topics/configuring-rate-limiting-api-gateway-cluster/)
- [Redis Rate Limiting Tutorials](https://redis.io/tutorials/howtos/ratelimiting/)
- [Build Rate Limiting with Redis + Lua (freeCodeCamp)](https://www.freecodecamp.org/news/build-rate-limiting-system-using-redis-and-lua/)
- [API Authentication Methods: JWT, OAuth2, API Keys (Security Boulevard)](https://securityboulevard.com/2026/01/api-authentication-methods-explained-api-keys-oauth-jwt-hmac-compared/)
- [Keycloak Official Documentation](https://www.keycloak.org/)
- [Keycloak + Spring Boot OAuth2/OIDC (Medium)](https://medium.com/@nsalexamy/keycloak-and-spring-boot-oauth-2-0-and-openid-connect-oidc-authentication-304e7b511d02)
- [HAProxy: HTTP Keep-Alive, Pipelining, Multiplexing, Connection Pooling](https://www.haproxy.com/blog/http-keep-alive-pipelining-multiplexing-and-connection-pooling)
- [API Versioning & Deprecation Strategy (APIDog)](https://apidog.com/blog/api-versioning-deprecation-strategy/)
- [API Versioning Strategies 2025 (DreamFactory)](https://blog.dreamfactory.com/top-5-api-versioning-strategies-2025-dreamfactory)
- [Backstage API Docs Plugin](https://roadie.io/backstage/plugins/api-docs/)
- [Swagger API Versioning Guide](https://moldstud.com/articles/p-a-developers-guide-to-navigating-api-versioning-challenges-and-solutions-with-swagger)
- [Kubernetes Gateway API v1.4 GA Release](https://kubernetes.io/blog/2025/11/06/gateway-api-v1-4/)
- [RetryGuard: Preventing Retry Storms (arXiv 2025)](https://arxiv.org/html/2511.23278v1)
- [Canary Deployments with Argo Rollouts, Traefik, Gateway API (Medium)](https://medium.com/@nsalexamy/canary-deployments-with-argo-rollouts-gateway-api-and-traefik-on-kubernetes-358ae2cdcd4f)
- [API Management Cost Breakdown (DigitalAPI)](https://www.digitalapi.ai/blogs/api-management-cost)
- [Istio Traffic Management Documentation](https://istio.io/latest/docs/concepts/traffic-management/)
