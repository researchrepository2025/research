# F40 — On-Premises Networking: Infrastructure, Operations, and Trade-offs for ISV Deployments

**Research File | Wave 6 | Scope: On-Premises Networking**
**Date:** 2026-02-18

---

## Executive Summary

An ISV deploying its AI-driven SaaS platform on customer-owned hardware must self-manage every networking layer that cloud providers otherwise abstract away — from Layer 4 load balancing and TLS termination through DNS authority, service discovery, ingress routing, and network segmentation. The operational burden is substantial: where a cloud-native deployment delegates these concerns to managed services (AWS ALB/NLB, Route 53, AWS Cloud Map, VPC security groups), an on-premises ISV must staff, configure, and operate purpose-built tools including HAProxy or Nginx for load balancing, Consul or CoreDNS for service discovery, Traefik or Nginx Ingress for Kubernetes ingress, and NetFlow/tcpdump for observability — each with its own operational profile, update cadence, and failure modes. Health-check endpoint design is a particularly underestimated integration point: in cloud deployments, the ALB automatically polls `/health` and drains traffic from unhealthy targets; on-premises, this same workflow requires explicit HAProxy or Nginx configuration, Consul service registry integration, and a purpose-built health aggregation dashboard. Across all sub-domains, on-premises networking difficulty ratings run 3–5 out of 5, compared to 1–2 for equivalent cloud-native managed services, and representative staffing for a mid-size ISV (50 enterprise customers) runs 1.5–3.0 FTE for network operations alone, excluding on-call burden.

---

## 1. Load Balancing: HAProxy, Nginx, and F5

### Capabilities

Self-managed load balancers are the first active networking component an ISV must provision and maintain on-premises. The three dominant options — HAProxy, Nginx Plus, and F5 BIG-IP — each support SSL/TLS termination, session persistence, and active health checking, but differ substantially in operational profile.

[HAProxy](https://www.haproxy.com/blog/how-to-enable-health-checks-in-haproxy) is a dedicated load balancer and proxy optimized for high-performance L4/L7 traffic distribution. It supports multiple session persistence mechanisms including sticky cookies, sticky routes, and IP hash, and provides advanced ACL-based routing. HAProxy 3.3, released in November 2025, introduced persistent stats across configuration reloads via Linux shared memory, improving observability continuity during hitless reloads. Nginx functions as both a web server and a load balancer; its SSL termination and session affinity capabilities parallel HAProxy's, but HAProxy is generally favored for advanced health-checking, connection draining, and real-time statistics in dedicated load balancing roles, as documented in the [HAProxy vs Nginx comparison](https://1gbits.com/blog/haproxy-vs-nginx/).

[F5 BIG-IP LTM](https://docs.nginx.com/nginx/deployment-guides/migrate-hardware-adc/f5-big-ip-configuration/) uses a proprietary SSL/TLS implementation while Nginx Plus relies on system libraries. F5 faces documented criticism for high cost, inflexible licensing, complex management, and a UI that requires dedicated expertise, per [Gartner Peer Insights reviews](https://www.gartner.com/reviews/market/application-delivery-controllers/compare/f5-vs-haproxy-technologies). For ISVs deploying on customer hardware where licensing cost is a constraint, HAProxy (open-source) or Nginx (open-source core) are typically preferred.

### SSL Termination Configuration Requirements

SSL/TLS termination at the load balancer layer requires: (1) certificate provisioning and renewal pipelines (no automatic Let's Encrypt integration comparable to AWS Certificate Manager); (2) cipher suite configuration and periodic rotation for compliance; (3) OCSP stapling configuration to avoid latency from real-time revocation checks. On-premises ISVs must implement these workflows manually or via tooling such as Certbot or Vault PKI, with no provider-managed certificate lifecycle.

### Session Persistence

[F5 BIG-IP and Nginx Plus](https://docs.nginx.com/nginx/deployment-guides/migrate-hardware-adc/f5-big-ip-configuration/) configure session persistence (affinity) at the upstream server level, supporting multiple persistence forms. HAProxy supports [SSL session ID-based affinity](https://www.haproxy.com/blog/maintain-affinity-based-on-ssl-session-id) in addition to cookie and IP-hash methods, giving it an advantage for stateful AI application backends that rely on GPU session continuity.

---

## 2. DNS Management

### Internal DNS and Split-Horizon Architecture

On-premises deployments require a fully self-managed DNS authority. [Split-horizon DNS](https://en.wikipedia.org/wiki/Split-horizon_DNS) (also called split-view or split-brain DNS) provides different DNS responses based on the source of the query — internal users resolve services to private IPs, while external users reach public-facing addresses. This is a foundational requirement for ISVs whose application spans internal service-to-service calls and externally accessible API endpoints.

[Split-horizon DNS implementation](https://resorsit.com/insights/dns-split-horizon/) for enterprises requires maintaining two DNS zones for the same domain: an internal authoritative zone served by an internal resolver (e.g., BIND, CoreDNS, or Unbound), and an external zone delegated to a public DNS provider. Any misconfiguration — such as incorrect zone delegation or TTL synchronization errors — can cause internal services to route traffic externally, incurring egress costs and latency.

### CoreDNS for Service Discovery

In Kubernetes on-premises clusters, [CoreDNS](https://kubernetes-sigs.github.io/external-dns/latest/docs/advanced/split-horizon/) handles internal service discovery under the `.svc.cluster.local` zone and can be configured to fall through for external domains. When paired with external-dns, CoreDNS can store DNS records in etcd and resolve zone queries against the etcd backend, enabling dynamic service registration without a cloud DNS provider.

### TTL Management

TTL management on-premises is entirely manual. Cloud DNS providers automatically tune TTLs based on change frequency and zone health; on-premises DNS administrators must explicitly set TTLs low enough to enable fast failover (e.g., 30–60 seconds for service endpoints) while avoiding excessive resolver cache churn. [UNVERIFIED — no Tier 1/2 2025 source quantifying optimal on-premises TTL ranges was found; the 30–60 second range is an operational heuristic widely referenced in infrastructure communities but not formally benchmarked in a current report.]

---

## 3. Service Discovery: Consul, etcd, and Custom Solutions

### Consul

[HashiCorp Consul](https://developer.hashicorp.com/consul/docs/use-case/service-discovery) provides service registration, health checking, and multi-datacenter federation in a single platform, making it the dominant self-hosted service discovery solution for on-premises ISV deployments. Consul agents run as sidecars alongside each microservice; services self-register with the Consul catalog on startup and deregister on shutdown or failure.

[Consul health checks](https://developer.hashicorp.com/consul/docs/register/health-check/vm) support HTTP, TCP, TTL-based, and gRPC check types. The `interval` parameter (e.g., `"5s"`, `"10s"`, `"15s"`) controls polling frequency; the `timeout` parameter controls when an unresponsive check is marked as failed. The [DeregisterCriticalServiceAfter](https://developer.hashicorp.com/consul/docs/register/health-check/vm) configuration is strongly recommended — it automatically removes service instances from the catalog after remaining in a critical (failing) state for a specified duration, with a minimum of 1 minute. The reaper process runs every 30 seconds, so actual deregistration may occur up to 90 seconds after the configured threshold. [A December 2025 guide](https://oneuptime.com/blog/post/2025-12-11-consul-health-checks/view) confirmed this architecture remains the standard for on-premises deployments.

### etcd

[etcd](https://charleswan111.medium.com/comparing-service-discovery-and-coordination-tools-etcd-consul-eureka-nacos-polaris-157820eb1810) provides strong consistency and is the key-value store backing Kubernetes itself, but it does NOT include native health checking for application services. etcd monitors its own cluster member health but depends on external tooling for application-level health verification. This makes etcd alone an incomplete service discovery solution for ISVs; it is best combined with Consul or a custom health-checking layer.

### Health Check Integration with Service Registries

When a [Kubernetes pod is connect-injected with Consul](https://developer.hashicorp.com/consul/docs/register/health-check/k8s), Consul registers a health check within its catalog that reflects the pod's readiness status. This bridges Kubernetes-native readiness probes with Consul's service registry, enabling HAProxy or Nginx upstreams to consume Consul's health catalog via the Consul API or consul-template for dynamic backend management.

---

## 4. Ingress Control

### Self-Managed Ingress Controllers

On-premises Kubernetes deployments require an Ingress controller to handle external traffic routing, TLS termination, path-based routing, and rate limiting. The primary options in 2025–2026 are [Traefik](https://traefik.io/choose-traefik-oss) and [HAProxy Ingress](https://oneuptime.com/blog/post/2026-01-06-kubernetes-ingress-controllers-nginx-traefik-haproxy/view).

A critical 2025–2026 development: the Ingress-NGINX Controller has reached end-of-life, with all security fixes and maintenance ending in March 2026, per [Skyscrapers' migration analysis](https://skyscrapers.eu/the-end-of-ingress-nginx-how-were-navigating-the-migration/) and [Telelink Business Services](https://www.tbs.tech/nginx-ingress-eol-migration/). ISVs relying on Ingress-NGINX in on-premises deployments must migrate to Traefik or an alternative before March 2026.

### Traefik Capabilities

[Traefik](https://doc.traefik.io/traefik/providers/kubernetes-ingress/) supports native path-based routing, TLS termination, CORS enforcement, and rate limiting, and integrates with production-hardened on-premises deployments across hybrid-cloud, multi-cloud, and pure on-premises environments. Its `IngressRoute` CRD provides more expressive routing than standard Ingress resources, matching on host, path, headers, and other request attributes. Traefik also offers a smooth migration path from Ingress-NGINX via its Ingress NGINX Provider, which preserves existing NGINX annotations.

### Absence of Cloud ALB/NLB Automation

The key operational gap versus cloud networking is the absence of managed WAF integration, automatic SSL certificate renewal tied to the load balancer, and elastic scaling of the ingress tier. An AWS ALB provisioned in a cloud-native deployment handles certificate rotation, HTTP/2 and gRPC support, and target group health checking with zero operator intervention. On-premises, each of these requires explicit configuration and operational ownership.

---

## 5. Network Segmentation

### VLANs and Traditional Segmentation

Traditional on-premises network segmentation uses VLANs to divide the network into broadcast domains, with firewall rules controlling inter-VLAN traffic. [CISA's 2025 Zero Trust Microsegmentation guidance](https://www.cisa.gov/sites/default/files/2025-07/ZT-Microsegmentation-Guidance-Part-One_508c.pdf) notes that VLAN-based segmentation is now insufficient for securing modern workloads: VLANs control north-south traffic at the network perimeter but do not enforce east-west traffic controls between services within the same segment.

### Microsegmentation

[Microsegmentation](https://www.paloaltonetworks.com/cyberpedia/what-is-microsegmentation) divides data centers and cloud environments into small isolated segments with granular, workload-level security policies, focusing on east-west traffic control. For on-premises ISV deployments, microsegmentation implementations include: (1) host-based firewall policies (iptables/nftables, Windows Firewall) enforced per workload; (2) next-generation firewall policies applied at the switch or inline between rack segments; (3) software-defined approaches via Calico NetworkPolicy or Cilium for Kubernetes east-west traffic.

[Cisco](https://www.cisco.com/site/us/en/learn/topics/security/what-is-network-segmentation.html) and [Tufin](https://www.tufin.com/blog/microsegmentation-vs-network-segmentation) both document that microsegmentation security policies should be specific to the workload, not the network segment, enabling consistent policy enforcement across on-premises data centers and hybrid cloud environments. For ISVs deploying AI workloads, this means GPU node pools, inference API services, and data ingestion pipelines each require separate network policy sets with explicit allow-lists.

---

## 6. Network Performance: Bandwidth, Latency, and GPU Interconnects

### Bandwidth Provisioning

On-premises ISV deployments must provision and manage their own top-of-rack (ToR) switches, inter-rack cables, and uplinks. For AI inference workloads, [100 GbE or 200 GbE networking](https://www.vitextech.com/blogs/blog/infiniband-vs-ethernet-for-ai-clusters-effective-gpu-networks-in-2025) is the baseline recommendation, with NVIDIA's Spectrum-X 400 Gbps Ethernet fabric approaching InfiniBand-level performance for multi-GPU workloads.

### Jumbo Frames and MTU

Enabling [jumbo frames (MTU 9000)](https://stonefly.com/resources/jumbo-frames-configuration-and-best-mtu-size/) reduces CPU overhead and increases throughput by reducing packet counts. [AKS engineering benchmarks](https://blog.aks.azure.com/2025/07/15/network-perf-aks) demonstrate that increasing MTU on all node interfaces can raise east-west pod-to-pod throughput to 75–80% of line rate on a 10G network (7.5–8 Gbps). On-premises, jumbo frame enablement requires coordinated configuration across all network devices in the path — switches, routers, and NICs — as packet fragmentation or dropping occurs if any device in the path does not support the configured MTU.

### RDMA for GPU Interconnects

For distributed AI training across multiple GPU nodes, [GPUDirect RDMA over InfiniBand](https://blogs.vmware.com/cloud-foundation/2025/09/16/deploy-distributed-llm-inference-with-gpudirect-rdma-over-infiniband-in-private-ai/) enables direct GPU-to-GPU data transfer bypassing the CPU and system memory, achieving over 90% efficiency in distributed training tasks. A 1:1 GPU-to-NIC ratio is a [documented best practice](https://docs.nvidia.com/ai-enterprise/planning-resource/reference-architecture-for-multi-tenant-clouds/latest/perf-reqs.html) for optimal GPUDirect RDMA performance. [RoCE v2 (RDMA over Converged Ethernet)](https://dataoorts.com/roce-v2-vs-infiniband-compare-for-gpu-clusters/) delivers 85–95% of InfiniBand performance for typical workloads at significantly lower cost, making it the recommended choice for tier 2/3 companies deploying 256–1,024 GPU clusters.

---

## 7. VPN and Remote Access

### Site-to-Site VPN

On-premises ISV deployments require site-to-site VPN for connecting multiple customer data centers or branch offices. [WireGuard](https://www.onlinehashcrack.com/guides/tutorials/howto-wireguard-vpn-setup-2025-secure-remote-access.php) has become the recommended protocol for new deployments in 2025, outperforming both IPSec and OpenVPN in throughput and handshake latency while supporting AES-256 encryption. Managed platforms such as [Netmaker](https://www.netmaker.io) and [Pritunl](https://pritunl.com/) provide web-based management interfaces for WireGuard and OpenVPN tunnels, simplifying site-to-site and client-to-site configuration for ISVs without a dedicated network engineering team.

### Remote Developer Access

[OpenVPN Access Server](https://blog.openvpn.net/how-to-set-up-a-vpn-for-remote-access/) provides a self-hosted VPN supporting fine-grained routing control for remote developers accessing on-premises resources. For ISVs where developers are distributed, [Tailscale](https://tailscale.com/) provides a zero-configuration WireGuard overlay network that does not require a self-hosted VPN server, reducing operational burden for remote access while still encrypting traffic to on-premises endpoints.

---

## 8. Health-Check Endpoint Design and Integration (Amended Scope)

This sub-topic receives expanded coverage per the amended research scope.

### Health Check Endpoint Design Patterns

The [microservices.io Health Check API pattern](https://microservices.io/patterns/observability/health-check-api.html) establishes `/health` (overall liveness) and `/ready` (readiness to serve traffic) as the standard endpoints per microservice. A well-designed `/health` endpoint performs thorough application and dependency checks — database connectivity, cache availability, downstream service reachability — and returns a single structured response (HTTP 200 OK with JSON body) if all dependencies are healthy.

[Kubernetes distinguishes three probe types](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/):
- **Liveness probe** (`/health`): signals that the container is alive; failure triggers a container restart.
- **Readiness probe** (`/ready`): signals that the container can serve traffic; failure removes the pod from Service endpoints without restarting it.
- **Startup probe**: disables liveness and readiness probes during slow startup; once it succeeds, the other probes activate.

[Best practices from Fairwinds](https://www.fairwinds.com/blog/a-guide-to-understanding-kubernetes-liveness-probes-best-practices) recommend setting `initialDelaySeconds` to the p99 startup time of the application, using conservative `failureThreshold` values, and making readiness probes more comprehensive than liveness probes (checking all dependencies), while keeping liveness probes lightweight (checking only that the process is responsive) to avoid false-positive restarts.

### HAProxy Health Check Integration

[HAProxy's `option httpchk`](https://www.haproxy.com/documentation/haproxy-configuration-tutorials/reliability/health-checks/) directive enables HTTP health checking against a specific endpoint (e.g., `GET /health HTTP/1.1`). HTTP responses in the 200–399 range are treated as healthy. Key configuration parameters for on-premises ISV deployments:

| Parameter | Default | Recommended for AI SaaS |
|-----------|---------|--------------------------|
| `inter` (poll interval) | 2s | 5–10s (reduce noise) |
| `fall` (failures to mark DOWN) | 3 | 3–5 (avoid flapping) |
| `rise` (successes to mark UP) | 2 | 3 (conservative re-admission) |
| `timeout check` | N/A | 2–3s (set explicitly) |

[HAProxy 3.3 (2025)](https://www.haproxy.com/blog/how-to-enable-health-checks-in-haproxy) supports querying multiple endpoints in a single health check session, enabling validation of both the primary application port and a metrics port simultaneously. With default settings (`inter 2s`, `fall 3`), a backend is marked DOWN after 6 seconds of consecutive failures. The `slowstart` parameter implements graceful traffic drain by progressively increasing traffic to a recovering server from 0% to 100% over a configured time window, preventing thundering-herd effects on restarts.

HAProxy does not natively poll a service registry; dynamic backend management requires [consul-template](https://developer.hashicorp.com/consul) or HAProxy's Runtime API, which adds operational complexity not present in cloud ALB deployments.

### Nginx Health Check Integration

[Nginx Plus](https://devtoolbox.dedyn.io/blog/nginx-load-balancing-complete-guide) supports active HTTP health checks against custom endpoints (Nginx OSS only supports passive health checking via failed request detection). The Taylor Built Solutions guide documents [combining HAProxy and Nginx](https://blog.taylorbuiltsolutions.com/haproxy-nginx-health-check-method/) in layered configurations where HAProxy handles health-check-aware load balancing at L4 while Nginx handles L7 routing and SSL termination.

### Consul Service Registry Integration

[Consul's health check system](https://developer.hashicorp.com/consul/tutorials/connect-services/monitor-applications-health-checks) natively supports HTTP checks that poll `/health` endpoints at configured intervals (e.g., every 10 seconds). When a service's check enters a `critical` state, Consul immediately removes it from the catalog's healthy endpoints. This integrates with HAProxy via consul-template, which dynamically rewrites HAProxy backend configuration blocks as Consul catalog membership changes — achieving behavior equivalent to ALB target group health-based routing, but with operational overhead proportional to the number of services registered.

### Cloud ALB/NLB vs. Self-Hosted: Health Check Comparison

[AWS ALB](https://aws.amazon.com/blogs/networking-and-content-delivery/choosing-the-right-health-check-with-elastic-load-balancing-and-ec2-auto-scaling/) automatically polls target group endpoints, integrates with Auto Scaling Groups for instance replacement, and provides passive health checking to detect deteriorating servers before they are marked unhealthy — all with zero operator configuration beyond initial target group setup. Self-hosted on-premises equivalents (HAProxy + Consul) replicate this behavior but require:
1. Explicit HAProxy health check configuration per backend pool
2. Consul agent deployment and health check registration per service instance
3. consul-template or Runtime API integration to propagate Consul health state to HAProxy
4. A health aggregation dashboard (Prometheus + Grafana) to provide the unified observability that CloudWatch provides natively in AWS

### Health Aggregation Dashboards

[Prometheus and Grafana](https://orkes.io/blog/monitoring-microservices-using-prometheus-and-grafana/) form the standard observability stack for on-premises health aggregation. Microservices expose `/metrics` endpoints (Prometheus format) alongside `/health` and `/ready`; Prometheus scrapes all endpoints at configurable intervals and stores time-series data; [Grafana dashboards](https://corp.sonar.software/new-gazette/grafana-health-monitoring-2025-1770332310) visualize aggregate health status, dependency failure counts, and latency percentiles. [Microsoft's Kubernetes health dashboard guidance](https://learn.microsoft.com/en-us/answers/questions/2283570/health-status-dashboard-for-kubernetes) and [Grafana's own pre-built Kubernetes Pods Health Overview dashboard](https://grafana.com/grafana/dashboards/13826-kubernetes-pods-health-overview/) provide reference architectures for on-premises Kubernetes health monitoring.

---

## 9. Troubleshooting Complexity

### Absence of VPC Flow Logs

In cloud deployments, VPC Flow Logs capture all accepted and rejected traffic flows for every network interface, searchable via CloudWatch or S3 analytics. On-premises, this visibility requires deploying [NetFlow or IPFIX](https://www.query.ai/resources/blogs/limitations-and-applicability-of-flow-logs/) on switches and routers, which provide similar flow-level data but demand a flow collector (e.g., ntopng, Elastic Stack with NetFlow module, Grafana Alloy) and dedicated storage.

### Packet Capture

[tcpdump and Wireshark](https://repost.aws/articles/ARsHcx7IJYQ3uT8vhLuyqiAA/troubleshoot-performance-issues-packet-drop-latency-or-slow-throughput-between-on-premises-and-aws-vpc-when-using-aws-site-to-site-vpn) remain the primary packet-level debugging tools. The documented best practice is to initiate packet capture before generating test traffic and to perform simultaneous captures on both source and destination hosts to isolate where packet loss or retransmission occurs. In large on-premises clusters with east-west traffic across hundreds of pods, identifying the culprit interface requires operator knowledge of physical topology — rack assignments, ToR switch ports, uplink cables — that does not exist in cloud VPC environments.

### Distributed Tracing Gaps

Without a managed observability platform, on-premises ISVs must self-deploy distributed tracing infrastructure (Jaeger, Zipkin, or OpenTelemetry Collector + backend) to correlate network-level latency events with application-level traces. This adds 0.25–0.5 FTE of observability engineering to the networking operational profile. [UNVERIFIED — no Tier 1/2 2025 source quantifying this specific FTE attribution was found; this estimate is derived from general observability staffing heuristics.]

---

## 10. Deployment Model Comparison

**Assumptions:** Mid-size ISV, 50 enterprise customers, ~200 microservices, 3 data center locations.

| Capability | On-Premises | Managed K8s (EKS/AKS/GKE) | Cloud-Native |
|------------|-------------|----------------------------|--------------|
| **Load Balancing** | Difficulty: 4/5 | Difficulty: 2/5 | Difficulty: 1/5 |
| | HAProxy/Nginx/F5 self-managed; TLS cert lifecycle; hitless reload management | Cloud LB provisioned via Kubernetes service annotations; cert management via cert-manager | AWS ALB/NLB fully managed; ACM auto-renews certs; zero operator config |
| | HAProxy 3.3, Nginx Plus, F5 BIG-IP | MetalLB, AWS Load Balancer Controller | AWS ALB/NLB, GCP Cloud Load Balancing, Azure Load Balancer |
| | Est. FTE: 0.5–1.0 | Est. FTE: 0.25–0.5 | Est. FTE: 0.0–0.1 |
| **DNS Management** | Difficulty: 4/5 | Difficulty: 3/5 | Difficulty: 1/5 |
| | Full DNS authority; split-horizon zones; manual TTL management; zone synchronization | CoreDNS for internal; external-dns for cloud DNS provider integration | Route 53, Azure DNS, Cloud DNS — managed, API-driven, auto-scaling |
| | BIND, CoreDNS, PowerDNS | CoreDNS + external-dns | Route 53, Azure DNS |
| | Est. FTE: 0.25–0.5 | Est. FTE: 0.1–0.25 | Est. FTE: 0.0–0.1 |
| **Service Discovery** | Difficulty: 4/5 | Difficulty: 2/5 | Difficulty: 1/5 |
| | Consul cluster management; health check config per service; consul-template integration | Kubernetes DNS + optional Consul for multi-cluster | AWS Cloud Map, Azure Service Bus, GCP Service Directory |
| | Consul, etcd | Consul, Kubernetes DNS | AWS Cloud Map, GCP Service Directory |
| | Est. FTE: 0.25–0.5 | Est. FTE: 0.1–0.25 | Est. FTE: 0.0–0.1 |
| **Ingress Control** | Difficulty: 4/5 | Difficulty: 2/5 | Difficulty: 1/5 |
| | Ingress controller self-managed (Ingress-NGINX EOL Mar 2026; migration to Traefik required); TLS cert pipeline; rate limiting config | Ingress controller managed by cloud provider or add-on; WAF integration optional | AWS API Gateway, ALB Ingress, managed WAF; zero ingress controller operations |
| | Traefik, HAProxy Ingress | Traefik, Kong, AWS Load Balancer Controller | AWS API Gateway, Azure API Management |
| | Est. FTE: 0.25–0.5 | Est. FTE: 0.1–0.25 | Est. FTE: 0.0–0.1 |
| **Network Segmentation** | Difficulty: 5/5 | Difficulty: 3/5 | Difficulty: 2/5 |
| | VLAN design, firewall rule management, Kubernetes NetworkPolicy, microsegmentation policy per workload; no automated policy drift detection | Kubernetes NetworkPolicy + cloud security groups; CNI plugin management | VPC security groups, NACLs, PrivateLink — API-managed; AWS Network Firewall optional |
| | Calico, Cilium, physical firewall (Cisco, Palo Alto) | Calico, Cilium, AWS Security Groups | AWS Security Groups, VPC NACLs, GCP Firewall Rules |
| | Est. FTE: 0.25–0.5 | Est. FTE: 0.1–0.25 | Est. FTE: 0.1–0.2 |
| **Health Check / Observability** | Difficulty: 4/5 | Difficulty: 2/5 | Difficulty: 1/5 |
| | `/health` and `/ready` design per service; HAProxy httpchk config; Consul health check registration; consul-template for dynamic backends; Prometheus + Grafana aggregation | Kubernetes liveness/readiness probes native; cloud LB health checks via annotations | ALB target group health checks automatic; CloudWatch integration native |
| | Prometheus, Grafana, Consul, consul-template | Prometheus, Grafana, Kubernetes probes | CloudWatch, AWS Health, Azure Monitor |
| | Est. FTE: 0.25–0.5 | Est. FTE: 0.1–0.2 | Est. FTE: 0.0–0.1 |
| **Troubleshooting** | Difficulty: 5/5 | Difficulty: 3/5 | Difficulty: 1/5 |
| | No flow logs; NetFlow/IPFIX collector required; tcpdump/Wireshark; physical topology knowledge required | CloudWatch/Azure Monitor for managed control plane; pod-level tcpdump still required | VPC Flow Logs, CloudTrail, X-Ray — managed and searchable |
| | tcpdump, Wireshark, ntopng, Elastic Stack | CloudWatch, pod-level tcpdump, Jaeger | AWS X-Ray, VPC Flow Logs, Azure Network Watcher |
| | Est. FTE: 0.25–0.5 + on-call | Est. FTE: 0.1–0.25 + on-call | Est. FTE: 0.0–0.1 |

**Total Estimated Networking FTE:**
- On-Premises: **1.75–3.5 FTE** (active) + 0.5–1.0 FTE on-call equivalent
- Managed K8s: **0.75–1.75 FTE** (active) + 0.25–0.5 FTE on-call equivalent
- Cloud-Native: **0.1–0.7 FTE** (active) + 0.0–0.1 FTE on-call equivalent

---

## Related — Out of Scope

- **Service mesh (F55):** Istio, Linkerd, and Cilium Mesh provide a Layer 7 networking overlay that implements mTLS, traffic policies, and observability at the sidecar/eBPF level. This is distinct from the ingress and load balancing covered here but shares health-check integration surface area.
- **Security policy (F46):** Specific firewall rule authoring, zero-trust architecture, and network access control policies are covered separately.
- **Compute operations (F39):** GPU node provisioning, Kubernetes node lifecycle, and hardware maintenance are out of scope.

---

## Key Takeaways

- **On-premises networking demands a full networking engineering function.** Every capability that cloud providers manage as a service — load balancing, DNS, service discovery, ingress, segmentation, flow logging — becomes a self-operated system with its own failure modes, update cadence, and staffing requirement. Total active FTE for networking alone runs 1.75–3.5 for a mid-size ISV, versus 0.1–0.7 for a cloud-native equivalent deployment.

- **Health-check endpoint integration is a multi-system problem on-premises.** Achieving the behavior that AWS ALB provides automatically (poll `/health`, drain traffic on failure, re-admit on recovery) requires coordinating at least three systems: the microservice's `/health` and `/ready` endpoint design, HAProxy's `httpchk` configuration with explicit `inter`/`fall`/`rise` parameters, and Consul's service registry with `DeregisterCriticalServiceAfter` set — plus consul-template to propagate health state changes to HAProxy backends in near-real time.

- **Ingress-NGINX reached end-of-life in March 2026.** ISVs with on-premises Kubernetes deployments using Ingress-NGINX must complete migration to Traefik or an alternative ingress controller immediately. Traefik is the documented migration path via its Ingress NGINX Provider.

- **VLAN-based segmentation is no longer sufficient for AI workload isolation.** CISA's 2025 Zero Trust Microsegmentation guidance explicitly identifies VLAN-only segmentation as inadequate; microsegmentation using Kubernetes NetworkPolicy (Calico/Cilium) and/or next-generation firewall workload policies is required to enforce east-west traffic controls between AI model inference, data ingestion, and API gateway components.

- **RDMA networking for GPU clusters is operationally complex but performance-critical.** Deploying GPUDirect RDMA over InfiniBand or RoCE v2 for distributed AI training requires 1:1 GPU-to-NIC ratios, coordinated MTU configuration (jumbo frames at 9000 bytes) across all switch and NIC hardware in the path, and specialized network engineering skills that cloud providers absorb internally. ISVs planning on-premises GPU deployments at scale should budget 0.5–1.0 FTE of dedicated HPC network engineering.

---

## Sources

1. [How to master SSL termination in HAProxy — Loadbalancer.org](https://www.loadbalancer.org/blog/how-to-master-ssl-termination-in-haproxy/)
2. [Migrating Load Balancer Configuration from F5 BIG-IP LTM to F5 NGINX Plus — NGINX Documentation](https://docs.nginx.com/nginx/deployment-guides/migrate-hardware-adc/f5-big-ip-configuration/)
3. [HAProxy vs NGINX: Which Load Balancer Should You Choose in 2026? — 1Gbits](https://1gbits.com/blog/haproxy-vs-nginx/)
4. [Maintain affinity based on SSL session ID — HAProxy Blog](https://www.haproxy.com/blog/maintain-affinity-based-on-ssl-session-id)
5. [Health checks — HAProxy Configuration Tutorials](https://www.haproxy.com/documentation/haproxy-configuration-tutorials/reliability/health-checks/)
6. [A Guide to HAProxy Health Checks for High Availability — HAProxy Blog](https://www.haproxy.com/blog/how-to-enable-health-checks-in-haproxy)
7. [Using HAProxy as an API Gateway, Part 3: Health Checks — HAProxy Blog](https://www.haproxy.com/blog/using-haproxy-as-an-api-gateway-part-3-health-checks)
8. [Service Discovery Explained — HashiCorp Consul](https://developer.hashicorp.com/consul/docs/use-case/service-discovery)
9. [Define health checks — HashiCorp Consul (VM)](https://developer.hashicorp.com/consul/docs/register/health-check/vm)
10. [Configure Health Checks for Consul on Kubernetes — HashiCorp Developer](https://developer.hashicorp.com/consul/docs/register/health-check/k8s)
11. [How to Implement Consul Health Checks — OneUptime (Dec 2025)](https://oneuptime.com/blog/post/2025-12-11-consul-health-checks/view)
12. [Monitor your application health with distributed checks — HashiCorp Consul](https://developer.hashicorp.com/consul/tutorials/connect-services/monitor-applications-health-checks)
13. [Comparing Service Discovery and Coordination Tools — Medium](https://charleswan111.medium.com/comparing-service-discovery-and-coordination-tools-etcd-consul-eureka-nacos-polaris-157820eb1810)
14. [Split-horizon DNS — Wikipedia](https://en.wikipedia.org/wiki/Split-horizon_DNS)
15. [DNS Split Horizon Architecture Guide — ResorsIT](https://resorsit.com/insights/dns-split-horizon/)
16. [Split Horizon DNS with external-dns and cert-manager for Kubernetes — Kubernetes SIGs](https://kubernetes-sigs.github.io/external-dns/latest/docs/advanced/split-horizon/)
17. [Pattern: Health Check API — microservices.io](https://microservices.io/patterns/observability/health-check-api.html)
18. [Configure Liveness, Readiness and Startup Probes — Kubernetes Official Docs](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/)
19. [A Guide to Understanding Kubernetes Liveness Probes Best Practices — Fairwinds](https://www.fairwinds.com/blog/a-guide-to-understanding-kubernetes-liveness-probes-best-practices)
20. [Readiness vs liveness probes — Google Cloud Blog](https://cloud.google.com/blog/products/containers-kubernetes/kubernetes-best-practices-setting-up-health-checks-with-readiness-and-liveness-probes)
21. [HAProxy & Nginx - Health Check Method — Taylor Built Solutions](https://blog.taylorbuiltsolutions.com/haproxy-nginx-health-check-method/)
22. [The Journey to Zero Trust Microsegmentation — CISA 2025 (PDF)](https://www.cisa.gov/sites/default/files/2025-07/ZT-Microsegmentation-Guidance-Part-One_508c.pdf)
23. [What Is Microsegmentation? — Palo Alto Networks](https://www.paloaltonetworks.com/cyberpedia/what-is-microsegmentation)
24. [Microsegmentation vs Network Segmentation — Tufin](https://www.tufin.com/blog/microsegmentation-vs-network-segmentation)
25. [What Is Network Segmentation? — Cisco](https://www.cisco.com/site/us/en/learn/topics/security/what-is-network-segmentation.html)
26. [InfiniBand vs Ethernet for AI Clusters: GPU Networks 2025 — Vitex LLC](https://www.vitextech.com/blogs/blog/infiniband-vs-ethernet-for-ai-clusters-effective-gpu-networks-in-2025)
27. [RoCE v2 vs InfiniBand: The Ultimate 2025 Comparison — DataOorts](https://dataoorts.com/roce-v2-vs-infiniband-compare-for-gpu-clusters/)
28. [Deploy Distributed LLM Inference with GPUDirect RDMA over InfiniBand — VMware Cloud Foundation Blog (Sept 2025)](https://blogs.vmware.com/cloud-foundation/2025/09/16/deploy-distributed-llm-inference-with-gpudirect-rdma-over-infiniband-in-private-ai/)
29. [NVIDIA Software Reference Architecture: Performance Requirements](https://docs.nvidia.com/ai-enterprise/planning-resource/reference-architecture-for-multi-tenant-clouds/latest/perf-reqs.html)
30. [Performance Tuning AKS for Network Intensive Workloads — AKS Engineering Blog (July 2025)](https://blog.aks.azure.com/2025/07/15/network-perf-aks)
31. [Ultimate Guide to Jumbo Frames: Configuration and Best MTU Size — Stonefly](https://stonefly.com/resources/jumbo-frames-configuration-and-best-mtu-size/)
32. [WireGuard VPN Setup 2025: Secure Remote Access — OnlineHashCrack](https://www.onlinehashcrack.com/guides/tutorials/howto-wireguard-vpn-setup-2025-secure-remote-access.php)
33. [Netmaker: Zero Trust Platform for Secure Networking](https://www.netmaker.io)
34. [Pritunl: Open Source Enterprise Distributed OpenVPN, IPsec and WireGuard Server](https://pritunl.com/)
35. [How to Set Up a VPN for Remote Access — OpenVPN Blog](https://blog.openvpn.net/how-to-set-up-a-vpn-for-remote-access/)
36. [Tailscale: Secure Connectivity for AI, IoT & Multi-Cloud](https://tailscale.com/)
37. [Ingress-NGINX Controller End-of-Life: 2026 — Medium / Hristo Stoychev](https://medium.com/@h.stoychev87/nginx-ingress-end-of-life-2026-f30e53e14a2e)
38. [Ingress-nginx retires in March 2026: our migration plan — Skyscrapers](https://skyscrapers.eu/the-end-of-ingress-nginx-how-were-navigating-the-migration/)
39. [Migrate from Ingress-NGINX to Traefik — Traefik Labs](https://traefik.io/choose-traefik-oss)
40. [Traefik Kubernetes Ingress Documentation](https://doc.traefik.io/traefik/providers/kubernetes-ingress/)
41. [How to Set Up Ingress Controllers in Kubernetes: NGINX vs Traefik vs HAProxy — OneUptime (Jan 2026)](https://oneuptime.com/blog/post/2026-01-06-kubernetes-ingress-controllers-nginx-traefik-haproxy/view)
42. [Choosing the right health check with ELB and EC2 Auto Scaling — AWS Networking Blog](https://aws.amazon.com/blogs/networking-and-content-delivery/choosing-the-right-health-check-with-elastic-load-balancing-and-ec2-auto-scaling/)
43. [Limitations and Applicability of Flow Logs — Query.ai](https://www.query.ai/resources/blogs/limitations-and-applicability-of-flow-logs/)
44. [Troubleshoot performance issues between on-premises and AWS VPC — AWS re:Post](https://repost.aws/articles/ARsHcx7IJYQ3uT8vhLuyqiAA/troubleshoot-performance-issues-packet-drop-latency-or-slow-throughput-between-on-premises-and-aws-vpc-when-using-aws-site-to-site-vpn)
45. [Monitoring Microservices using Prometheus and Grafana — Orkes.io](https://orkes.io/blog/monitoring-microservices-using-prometheus-and-grafana/)
46. [Grafana Health Dashboard: Monitor and Optimize in 2025 — Sonar/Corp](https://corp.sonar.software/new-gazette/grafana-health-monitoring-2025-1770332310)
47. [Health status dashboard for Kubernetes — Microsoft Q&A / Learn](https://learn.microsoft.com/en-us/answers/questions/2283570/health-status-dashboard-for-kubernetes)
48. [Kubernetes Pods Health Overview Dashboard — Grafana Labs](https://grafana.com/grafana/dashboards/13826-kubernetes-pods-health-overview/)
49. [F5 vs HAProxy Technologies 2026 — Gartner Peer Insights](https://www.gartner.com/reviews/market/application-delivery-controllers/compare/f5-vs-haproxy-technologies)
50. [Nginx Load Balancing Complete Guide: Upstream, Health Checks & SSL — DevToolbox](https://devtoolbox.dedyn.io/blog/nginx-load-balancing-complete-guide)
