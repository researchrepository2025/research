# F21: Azure Networking Services
**Research Agent:** Fact Extraction
**Scope:** Azure managed networking services — load balancing, DNS, API management, and connectivity
**Date:** 2026-02-18
**Target Audience:** C-suite executives and technical leadership evaluating ISV deployment models

---

## Executive Summary

Azure provides a layered networking stack that abstracts nearly all physical infrastructure management from the operator, replacing it with declarative configuration and pay-as-you-go managed services. For an ISV building SaaS on Azure, the managed networking plane eliminates dedicated hardware procurement, BGP router management, certificate lifecycle work, and global anycast infrastructure — capabilities that would require specialized staff and significant capital expenditure in an on-premises deployment. The core services span four functional domains: load balancing (Azure Load Balancer, Application Gateway, Front Door), private connectivity (VNet, Private Link, NSGs, service endpoints), DNS (Azure Public DNS, Azure Private DNS), and API management (Azure API Management). Hybrid connectivity services — ExpressRoute and VPN Gateway — bridge on-premises or multi-cloud environments into Azure VNets over dedicated or encrypted tunnels. For most ISV SaaS architectures serving enterprise customers, a combination of Azure Front Door (global ingress), Application Gateway (regional L7), Azure API Management (API lifecycle), and Azure Private Link (PaaS isolation) covers the majority of networking requirements with operational difficulty ratings of 2–3 out of 5 on the standardized scale.

---

## Section 1: Azure Load Balancer (L4)

### Overview

Azure Load Balancer operates at Layer 4 (TCP/UDP) and distributes inbound flows from a frontend IP address to backend pool instances according to configured load-balancing rules and health probes. It is a fully managed, zero-infrastructure service — Microsoft manages the underlying hardware, routing fabric, and control plane entirely.

[Azure Load Balancer overview — Microsoft Learn](https://learn.microsoft.com/en-us/azure/load-balancer/load-balancer-overview)

### SKU Status (2025)

As of September 30, 2025, the Basic Load Balancer SKU was retired. Standard Load Balancer is now the only generally available SKU for production use.

[Migrate from Azure Basic to Standard Load Balancers Before 30 September 2025 — Medium/Precious Ajuru](https://medium.microsoft.com/@precious.ajuru/migrate-from-azure-basic-to-standard-load-balancers-before-30-september-2025-aab0fb2afe01)

### Health Probes

Health probes attempt to check the configured health probe port every 5 seconds by default. Azure Load Balancer supports three health probe types: TCP, HTTP, and HTTPS. If the health probe fails, backend pool instances are immediately marked unhealthy; on the next successful probe, they are marked healthy again.

[Azure Load Balancer health probes — Microsoft Learn](https://learn.microsoft.com/en-us/azure/load-balancer/load-balancer-custom-probe-overview)

### HA Ports

High availability (HA) ports are a type of load-balancing rule that load-balances all TCP and UDP flows that arrive on all ports simultaneously when using an internal Standard Load Balancer. The rule is configured by setting frontend and backend ports to 0 and protocol to All.

Primary use case: high availability and scale for [Network Virtual Appliances (NVAs)](https://learn.microsoft.com/en-us/azure/load-balancer/load-balancer-ha-ports-overview) inside virtual networks — specifically hub-and-spoke deployments where NVAs inspect all traffic.

[High availability ports overview — Microsoft Learn](https://learn.microsoft.com/en-us/azure/load-balancer/load-balancer-ha-ports-overview)

Key constraints:
- HA ports load-balancing rules are available **only** for an internal Standard Load Balancer
- Flow symmetry is not guaranteed across two or more load balancer components; use Gateway Load Balancer for NVA scenarios requiring flow symmetry
- ICMP traffic is supported for internal Standard Load Balancer when HA port is enabled
- IP fragmenting is not supported

### Gateway Load Balancer

Gateway Load Balancer (GWLB) provides transparent insertion of NVAs for scenarios requiring high performance and high scalability. GWLB should be used when flow symmetry is required and when placing NVAs between a public and internal load balancer.

[Gateway load balancer overview — Microsoft Learn](https://learn.microsoft.com/en-us/azure/load-balancer/gateway-overview)

### What Azure Load Balancer Abstracts Away

- Physical load-balancing hardware and firmware management
- BGP route advertisement for VIP failover
- Health monitoring daemons
- Redundant hardware provisioning (the service is zone-redundant by default in Standard SKU)

### Operational Profile

| Capability | On-Premises | Managed K8s | Cloud-Native (Azure LB) |
|------------|-------------|-------------|--------------------------|
| L4 Load Balancing | Difficulty: 4/5 | Difficulty: 2/5 | Difficulty: 1/5 |
| Key requirements | HAProxy/F5/hardware, BGP config | Service type LoadBalancer, MetalLB or cloud controller | Rules, backend pools, health probes via portal/Bicep |
| Representative tools | F5 BIG-IP, HAProxy, Nginx | cloud-controller-manager, MetalLB | Azure Load Balancer (Standard SKU) |
| Est. FTE | 0.5–1.0 FTE | 0.25–0.5 FTE | 0.1–0.25 FTE |

---

## Section 2: Azure Application Gateway (L7)

### Overview

Azure Application Gateway is a Layer 7 load balancer that controls traffic to web applications using advanced routing rules, SSL/TLS termination, a built-in Web Application Firewall (WAF), and cookie-based session affinity. It operates regionally and is the recommended reverse proxy for single-region HTTP/HTTPS workloads.

[What is Azure Application Gateway — Microsoft Learn](https://learn.microsoft.com/en-us/azure/application-gateway/overview)

### v2 SKU and Autoscaling

Application Gateway Standard_v2 supports autoscaling — the v2 SKU eliminates the need to choose a deployment size or instance count during provisioning. Microsoft strongly recommends moving to v2 to take advantage of feature updates in that SKU.

Minimum instance count recommendation: 2–4 to prevent instability during scale-in. Maximum: up to 10–20 depending on workload.

[Azure Application Gateway features — Microsoft Learn](https://learn.microsoft.com/en-us/azure/application-gateway/features)

### WAF Integration

The built-in WAF protects web applications against Layer 7 DDoS and the OWASP Top 10 vulnerability categories. WAF v2 uses the Default Rule Set (DRS) 2.2, baselined off OWASP Core Rule Set (CRS) 3.3.4, and includes additional proprietary protection rules developed by the Microsoft Threat Intelligence team.

If an existing WAF policy uses DRS 2.1, CRS 3.2, or CRS 3.1, Microsoft recommends upgrading to DRS 2.2.

[CRS and DRS rule groups and rules — Microsoft Learn](https://learn.microsoft.com/en-us/azure/web-application-firewall/ag/application-gateway-crs-rulegroups-rules)
[What Is Azure Web Application Firewall on Application Gateway — Microsoft Learn](https://learn.microsoft.com/en-us/azure/web-application-firewall/ag/ag-overview)

### URL Routing

URL path-based routing allows traffic to be routed to different backend server pools based on URL path patterns in the request. This is used to route requests for different content types (e.g., /api/ vs. /static/) to separate backend pools.

[Azure Application Gateway features — Microsoft Learn](https://learn.microsoft.com/en-us/azure/application-gateway/features)

### SSL/TLS Termination

Application Gateway supports TLS termination, cookie-based session affinity, and round-robin load balancing. End-to-end TLS (re-encryption to the backend) is also supported.

Starting August 31, 2025, all clients and backend servers interacting with Azure Application Gateway must use TLS 1.2 or higher; support for TLS 1.0 and 1.1 was discontinued.

[Enabling end to end TLS on Azure Application Gateway — Microsoft Learn](https://learn.microsoft.com/en-us/azure/application-gateway/ssl-overview)
[TLS policy overview for Azure Application Gateway — Microsoft Learn](https://learn.microsoft.com/en-us/azure/application-gateway/application-gateway-ssl-policy-overview)

### Integration with Azure API Management

Application Gateway v2 and Azure API Management can be combined for secure, scalable API delivery — Application Gateway handles ingress WAF and routing while API Management handles API lifecycle, rate limiting, and developer portal.

[Integrating Azure Application Gateway v2 with Azure API Management — Microsoft Community Hub](https://techcommunity.microsoft.com/blog/azurenetworkingblog/integrating-azure-application-gateway-v2-with-azure-api-management-for-secure-an/4470804)

### What Application Gateway Abstracts Away

- Certificate lifecycle management (autorotated managed certificates available)
- SSL offload hardware
- Manual WAF rule signature updates (managed ruleset auto-updates)
- Autoscaling decisions for request volume changes

### Operational Profile

| Capability | On-Premises | Managed K8s | Cloud-Native (App Gateway) |
|------------|-------------|-------------|---------------------------|
| L7 WAF + SSL Termination | Difficulty: 4/5 | Difficulty: 3/5 | Difficulty: 2/5 |
| Key requirements | Nginx Plus/F5, WAF licensing, cert management | Ingress controller + cert-manager | WAF policy, listener, backend pool config |
| Representative tools | ModSecurity, F5 ASM, Nginx WAF | AGIC, ingress-nginx + cert-manager | Application Gateway v2 with WAF_v2 |
| Est. FTE | 0.5–1.0 FTE | 0.5 FTE | 0.25 FTE |

---

## Section 3: Azure Front Door (Global Edge)

### Overview

Azure Front Door is Microsoft's advanced cloud Content Delivery Network (CDN) designed to provide fast, reliable, and secure access to static and dynamic web content globally. It operates at Layer 7 (HTTP/HTTPS) and sits at Microsoft's global edge network.

[Azure Front Door — Microsoft Learn](https://learn.microsoft.com/en-us/azure/frontdoor/front-door-overview)

### Edge Network Scale

Azure Front Door uses over 118 edge locations across 100 metro cities connected to Azure using a private enterprise-grade WAN. The service claims to improve application latency by up to three times using anycast routing and split-TCP connections.

[Azure Front Door — Microsoft Learn](https://learn.microsoft.com/en-us/azure/frontdoor/front-door-overview)
[Azure Front Door POP Locations by Region — Microsoft Learn](https://learn.microsoft.com/en-us/azure/frontdoor/edge-locations-by-region)

### Tiers

Azure Front Door is offered in three tiers: Standard, Premium, and Classic. The Classic tier is legacy. Standard and Premium are the current production tiers with the following distinctions:

- Standard: Unified static and dynamic delivery, caching, SSL offload, and layer 3–4 DDoS protection
- Premium: Adds Private Link origin support (private backend connectivity), advanced WAF with bot protection, and security analytics

[Compare Pricing Between Azure Front Door Tiers — Microsoft Learn](https://learn.microsoft.com/en-us/azure/frontdoor/understanding-pricing)

### WAF at the Edge

Azure Front Door includes built-in layer 3–4 DDoS protection and seamlessly attaches Web Application Firewall (WAF) at the edge. Bot manager rules are based on Microsoft's own Threat Intelligence. WAF provides protection against layer 7 DDoS attacks.

[Azure Front Door — Microsoft Learn](https://learn.microsoft.com/en-us/azure/frontdoor/front-door-overview)

### Certificate Management (2025 Note)

As of August 15, 2025, Azure Front Door migrated existing managed certificate domains. Users on the Classic tier managing certificates on existing domains must either move to Bring Your Own Certificate (BYOC) or migrate to Front Door Standard or Premium.

[Azure Front Door FAQ — Microsoft Learn](https://learn.microsoft.com/en-us/azure/frontdoor/front-door-faq)

### Routing Engine

Front Door's enhanced rules engine supports regular expressions and server variables. It allows custom routing business logic to be moved to the edge, enabling path-based routing, header manipulation, and redirect rules without backend changes.

[Azure Front Door — Microsoft Learn](https://learn.microsoft.com/en-us/azure/frontdoor/front-door-overview)

### SaaS ISV Recommendation

The Azure Well-Architected Framework recommends sharing Front Door profiles among multiple customers in a multi-tenant SaaS architecture, as it reduces costs and operational overhead. It also recommends using Front Door as the primary reverse proxy for global HTTP/HTTPS traffic management.

[Networking for SaaS Workloads on Azure — Microsoft Learn](https://learn.microsoft.com/en-us/azure/well-architected/saas/networking)

### What Front Door Abstracts Away

- Global anycast CDN infrastructure management
- Edge certificate provisioning (autorotation with managed certs)
- DDoS scrubbing at the network edge
- Multi-region health probe coordination and failover
- WAF signature management and rule updates

### Operational Profile

| Capability | On-Premises | Managed K8s | Cloud-Native (Front Door) |
|------------|-------------|-------------|--------------------------|
| Global CDN + WAF + Routing | Difficulty: 5/5 | Difficulty: 4/5 | Difficulty: 2/5 |
| Key requirements | Global PoP infrastructure, Anycast BGP, WAF appliances | External CDN + ingress, cross-region federation | Profile, route rules, WAF policy, origins |
| Representative tools | Akamai/Cloudflare on-prem edge | Cloudflare + K8s Ingress | Azure Front Door Standard/Premium |
| Est. FTE | 2.0+ FTE | 0.5–1.0 FTE | 0.25 FTE |

---

## Section 4: Azure DNS

### Public DNS

Azure DNS is a hosting service for DNS domains that provides name resolution using Azure infrastructure. DNS zones hosted in Azure DNS are served from a global network of DNS name servers, providing high availability and fast performance.

Azure DNS supports A, AAAA, CNAME, MX, PTR, SOA, SRV, and TXT records for public zones.

[What is Azure Public DNS — Microsoft Learn (docs.azure.cn mirror)](https://docs.azure.cn/en-us/dns/public-dns-overview)

### Alias Records (Public DNS)

Azure DNS supports alias record sets that can directly reference Azure resources such as a public IP address, an Azure Traffic Manager profile, or an Azure CDN endpoint. When the underlying Azure resource's IP address changes, the alias record updates automatically. Standard CNAME records do not support this behavior.

[Alias records overview — Azure DNS (docs.azure.cn mirror)](https://docs.azure.cn/en-us/dns/dns-alias)

### Private DNS Zones

Azure Private DNS provides a reliable, secure DNS service to manage and resolve domain names in a virtual network without requiring a custom DNS solution. Private DNS zones allow custom domain names to be used for internal resources rather than Azure-provided names.

Private DNS zones support standard DNS records including CNAME records for aliasing purposes. Zone delegations (NS records) cannot be created in a private DNS zone, but child domains can be created directly as separate private DNS zones.

[Azure Private DNS Zone Overview — Microsoft Learn](https://learn.microsoft.com/en-us/azure/dns/private-dns-privatednszone)

### Private Endpoint DNS Integration

When a private endpoint is created for a PaaS service (e.g., Azure Storage, Azure SQL), a corresponding Private DNS Zone is required to resolve the service's FQDN to the private IP address within the VNet. The required zone name for each service is documented by Microsoft.

[Azure Private Endpoint private DNS zone values — Microsoft Learn](https://learn.microsoft.com/en-us/azure/private-link/private-endpoint-dns)

### What Azure DNS Abstracts Away

- DNS server hardware and OS maintenance
- Zone replication and failover infrastructure
- Anycast DNS resolution infrastructure
- Certificate validation DNS record management (when integrated with Azure services)

### Operational Profile

| Capability | On-Premises | Managed K8s | Cloud-Native (Azure DNS) |
|------------|-------------|-------------|--------------------------|
| DNS Hosting + Private Zones | Difficulty: 3/5 | Difficulty: 2/5 | Difficulty: 1/5 |
| Key requirements | BIND/Windows DNS, zone replication, failover | CoreDNS config, external-dns operator | Zone creation, record sets, VNet links |
| Representative tools | BIND, Windows DNS, Infoblox | CoreDNS + external-dns | Azure DNS Public + Private Zones |
| Est. FTE | 0.25–0.5 FTE | 0.1–0.25 FTE | 0.05–0.1 FTE |

---

## Section 5: Azure API Management

### Overview

Azure API Management (APIM) is a fully managed service that allows organizations to publish, secure, transform, maintain, and monitor APIs. It consists of three components: the API gateway (processes API calls), the Azure portal (admin interface for API program definition), and the developer portal (auto-generated interactive API documentation for API consumers).

[Azure API Management V2 Tiers — Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/v2-service-tiers-overview)

### Service Tiers (Current — 2025/2026)

The v2 tiers are built on a new, more reliable and scalable platform and are generally available as of 2025:

- **Basic v2**: Development and testing scenarios, SLA-backed. Scales to 10 units.
- **Standard v2**: Production-ready tier with support for network-isolated backends. VNet integration (outbound), private endpoint support (inbound). Scales to 10 units.
- **Premium v2**: Enterprise features — full VNet isolation (injection), availability zones, workspaces, scaling to 30 units.

[Azure API Management V2 Tiers — Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/v2-service-tiers-overview)
[Azure API Management Premium v2 GA — InfoQ (December 2025)](https://www.infoq.com/news/2025/12/apim-v2-premium-secure-vnet/)

The classic tiers (Developer, Basic, Standard, Premium) remain available and are not being retired.

### Rate Limiting Policies

Azure API Management implements rate limiting via policies applied at global, product, or API-specific scope. Common policies include:

- `rate-limit`: Limit calls per second or per minute for a subscription
- `rate-limit-by-key`: Flexible throttling keyed on any request attribute (IP, JWT claim, header)
- `azure-openai-token-limit` / `llm-token-limit`: Token-based limits for AI API traffic (GenAI gateway capability)

Rate limiting policy behavior by tier:
- Classic tiers: sliding window algorithm
- V2 tiers: token bucket algorithm (more efficient, aligns with Azure Resource Manager rate limiting)

In multi-region deployments, each regional gateway has a separate rate-limit counter. Limits are enforced independently per region.

[Azure API Management policy reference — rate-limit — Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/rate-limit-policy)
[Azure API Management policy reference — rate-limit-by-key — Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/rate-limit-by-key-policy)
[AI gateway in Azure API Management — Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities)

### Developer Portal

The developer portal automatically generates interactive API documentation and provides tools for developers to explore, test, and subscribe to APIs. It is enabled optionally per APIM instance.

[Azure API Management V2 Tiers — Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/v2-service-tiers-overview)

### Caching

Azure API Management supports response caching policies via built-in internal cache or external Azure Cache for Redis. Caching policies reduce backend load for frequently called, low-variance API responses.

[Advanced Request Throttling with Azure API Management — Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/api-management-sample-flexible-throttling)

### Networking in V2 Tiers

- Standard v2 and Premium v2: VNet integration for outbound access to isolated backends + private endpoint for inbound
- Premium v2 only: Full VNet injection for complete inbound and outbound isolation without a public IP (equivalent to classic Premium tier VNet injection)

A Standard v2 service integrated with a VNet has a public IP address for inbound access; Premium v2 injection eliminates the public IP entirely.

[Azure API Management V2 Tiers — Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/v2-service-tiers-overview)

### Known V2 Limitations (as of early 2026)

Currently unavailable in v2 tiers: multi-region deployment, multiple custom domain names, Azure DDoS Protection enablement, Git-based configuration, back up and restore, and upgrade path from classic tiers to v2 tiers (new instances only).

[Azure API Management V2 Tiers — Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/v2-service-tiers-overview)

### What APIM Abstracts Away

- API gateway infrastructure (reverse proxy fleet) management
- TLS certificate management for API endpoints
- Developer documentation portal hosting and authentication
- Rate-limiting counter infrastructure across request flows
- Policy engine execution and observability integration

### Operational Profile

| Capability | On-Premises | Managed K8s | Cloud-Native (APIM) |
|------------|-------------|-------------|---------------------|
| API Gateway + Rate Limiting + Dev Portal | Difficulty: 4/5 | Difficulty: 3/5 | Difficulty: 2/5 |
| Key requirements | Kong/Nginx + Lua, portal build, Redis for rate counters | Kong Ingress Controller or Gloo, manual portal | APIM instance, APIs, products, policies |
| Representative tools | Kong Gateway, Tyk, AWS API GW self-hosted | Kong for Kubernetes, custom Envoy | Azure API Management (Standard v2 / Premium v2) |
| Est. FTE | 0.5–1.0 FTE | 0.5 FTE | 0.25 FTE |

---

## Section 6: Azure VNet — Subnets, NSGs, Service Endpoints, Private Endpoints

### Virtual Network (VNet)

An Azure Virtual Network is the fundamental building block for private networks in Azure. VNets enable Azure resources to communicate securely with each other, with the internet, and with on-premises networks. Each VNet is scoped to a single Azure region.

[Azure virtual network service endpoints — Microsoft Learn](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-network-service-endpoints-overview)

### Subnets and NSGs

VNets are subdivided into subnets. Network Security Groups (NSGs) are stateful packet filters (containing allow/deny rules based on source/destination IP, port, and protocol) that can be applied at the subnet or NIC level. NSGs support service tags (e.g., `AzureStorage`, `Sql`) as destinations, enabling rules that allow traffic to specific Azure services without specifying IP ranges.

[Network policies for Private Endpoints with UDR and NSG — msandbu.org](https://msandbu.org/network-policies-for-private-endpoints-with-udr-and-nsg/)

### Service Endpoints

Service endpoints enable a subnet to support traffic to Azure PaaS services (e.g., Azure Storage, Azure SQL) over the Microsoft backbone network. When a service endpoint is enabled, source IP addresses of VMs in the subnet switch from public IPv4 to private IPv4 addresses for service traffic.

Key characteristics:
- Traffic still exits the VNet and hits the public endpoint of the PaaS resource (but traverses the Microsoft backbone, not the public internet)
- Service endpoints do not provide a private IP address for the PaaS resource
- Lower cost than Private Endpoints (no per-resource charge)
- Cross-tenant support varies by Azure service

[Azure virtual network service endpoints — Microsoft Learn](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-network-service-endpoints-overview)
[Azure Private Endpoint vs. Service Endpoint: A Comprehensive Guide — Microsoft Community Hub](https://techcommunity.microsoft.com/blog/fasttrackforazureblog/azure-private-endpoint-vs-service-endpoint-a-comprehensive-guide/4363095)

### Private Endpoints

A private endpoint is a network interface that assigns a private IP address from the VNet to a specific instance of a PaaS resource (not the entire service). Traffic to the PaaS resource travels entirely over the Microsoft backbone network; the resource does not need to be exposed to the public internet.

Key differences from service endpoints:
- Provides a private IP within the VNet for the target resource
- Accessible from on-premises via ExpressRoute private peering or VPN
- Accessible from peered networks
- Cross-region access supported
- Protection against data leakage: access is scoped to the specific resource instance, not the entire service
- NSGs can be applied to private endpoints when `PrivateEndpointNetworkPolicies` is set to enabled

[Service Endpoints vs Private Endpoints — Microsoft Community Hub](https://techcommunity.microsoft.com/blog/coreinfrastructureandsecurityblog/service-endpoints-vs-private-endpoints/3962134)
[Azure Virtual Network Integration for Service Network Isolation — Microsoft Learn](https://learn.microsoft.com/en-us/azure/virtual-network/vnet-integration-for-azure-services)

### SaaS ISV Guidance on VNet Topology

The Azure Well-Architected Framework identifies three SaaS network topologies:
1. **Flat network**: Single isolated network with subnets for segmentation. Suitable for simple multitenant applications but can hit resource limits at scale.
2. **Hub-and-spoke**: Centralized hub peers to isolated spoke networks per customer or application. Spoke-to-spoke (transitive) communication through the hub is disabled by default, which maintains customer isolation. Recommended for high scalability and customer isolation.
3. **No network**: PaaS-only solutions where VNets are not deployed. Simplifies management but limits security control flexibility.

[Networking for SaaS Workloads on Azure — Microsoft Learn](https://learn.microsoft.com/en-us/azure/well-architected/saas/networking)

---

## Section 7: Azure Private Link

### Overview

Azure Private Link enables access to Azure PaaS services and Azure-hosted customer/partner services over a private endpoint in a VNet. Traffic between the VNet and the service travels over the Microsoft backbone network; exposing the service to the public internet is not required.

[What is Azure Private Link — Microsoft Learn](https://learn.microsoft.com/en-us/azure/private-link/private-link-overview)

### Key Benefits (from official documentation)

1. **Private access**: Connect the VNet to Azure services via private endpoints. The Private Link platform handles connectivity over the Azure backbone network.
2. **On-premises and peered network access**: Access services running in Azure from on-premises via ExpressRoute private peering, VPN tunnels, and peered VNets — no need for ExpressRoute Microsoft peering or internet traversal.
3. **Data leakage protection**: A private endpoint is mapped to an instance of a PaaS resource, not the entire service. Access to any other resource in the service is blocked.
4. **Global reach**: Connect privately to services running in other Azure regions.
5. **Multi-tenant ISV support**: Works for consumers and services belonging to different Microsoft Entra tenants.

[What is Azure Private Link — Microsoft Learn](https://learn.microsoft.com/en-us/azure/private-link/private-link-overview)

### Private Link Service (ISV Pattern)

An ISV can place their own service behind a Standard Azure Load Balancer and enable Private Link Service, allowing enterprise customers to connect directly to the ISV service via a private endpoint in their own VNet — across Microsoft Entra tenants. This is the recommended architecture for ISVs deploying into customer Azure environments.

[What is Azure Private Link service — Microsoft Learn](https://learn.microsoft.com/en-us/azure/private-link/private-link-service-overview)
[Azure Private Link Explained (2025) — Orchestra](https://www.getorchestra.io/blog/azure-private-link-explained-2025)

### Network Security Perimeter (GA 2025)

Azure Network Security Perimeter is now generally available in all Azure public cloud regions. It provides a secure logical boundary restricting communication to services within its perimeter and allows non-perimeter public traffic through inbound and outbound access rules.

[What is Azure Private Link — Microsoft Learn](https://learn.microsoft.com/en-us/azure/private-link/private-link-overview)

### ISV Cost Consideration

Private Link incurs a per-endpoint charge. The Azure Well-Architected Framework notes this tradeoff explicitly: "Private Link helps ensure that your traffic remains within your private network. We recommend Private Link for network connectivity across Microsoft Entra tenants. However, each private endpoint incurs costs, which can add up depending on your security needs. Service endpoints can be a cost-effective alternative."

[Networking for SaaS Workloads on Azure — Microsoft Learn](https://learn.microsoft.com/en-us/azure/well-architected/saas/networking)

### Operational Profile

| Capability | On-Premises | Managed K8s | Cloud-Native (Private Link) |
|------------|-------------|-------------|------------------------------|
| Private PaaS Connectivity | Difficulty: 5/5 | Difficulty: 3/5 | Difficulty: 2/5 |
| Key requirements | Physical network segmentation, dedicated circuits | VNet CNI plugin, private service annotations | Private endpoint per PaaS resource, DNS zone linking |
| Representative tools | Physical VLANs, dedicated fiber | Calico NetworkPolicy + VNet CNI | Azure Private Link + Private DNS Zones |
| Est. FTE | 1.0+ FTE | 0.25–0.5 FTE | 0.1–0.25 FTE |

---

## Section 8: Azure ExpressRoute and VPN Gateway (Hybrid Connectivity)

### Azure ExpressRoute

ExpressRoute extends on-premises networks into the Microsoft cloud over a private connection through a connectivity provider. ExpressRoute connections do not route through the public internet, providing more reliability, faster speeds, consistent latency, and higher security.

[Azure ExpressRoute Overview — Microsoft Learn](https://learn.microsoft.com/en-us/azure/expressroute/expressroute-introduction)

#### Bandwidth Options

ExpressRoute circuits are available in the following bandwidths: 50 Mbps, 100 Mbps, 200 Mbps, 500 Mbps, 1 Gbps, 2 Gbps, 5 Gbps, and 10 Gbps via connectivity providers. ExpressRoute Direct provides dual 100-Gbps connectivity with physical isolation for regulated industries.

[Azure ExpressRoute Overview — Microsoft Learn](https://learn.microsoft.com/en-us/azure/expressroute/expressroute-introduction)

#### Circuit SKUs

- **Local SKU**: Data transfer included in the port charge; connects to a single Azure region near the peering location.
- **Standard SKU**: Connectivity to all regions within the same geopolitical region.
- **Premium SKU (add-on)**: Global connectivity across all regions, increased route limits (4,000 → 10,000 routes for Azure private peering), increased VNet links per circuit.

[Azure ExpressRoute Overview — Microsoft Learn](https://learn.microsoft.com/en-us/azure/expressroute/expressroute-introduction)

#### Redundancy Model

Each ExpressRoute circuit consists of two connections to two Microsoft Enterprise edge routers (MSEEs) from the connectivity provider. Microsoft recommends establishing connections to two ExpressRoute circuits in two peering locations for maximum resiliency.

[Azure ExpressRoute Overview — Microsoft Learn](https://learn.microsoft.com/en-us/azure/expressroute/expressroute-introduction)

#### Dynamic Bandwidth Scaling

ExpressRoute circuit bandwidth can be increased without tearing down connections.

[Azure ExpressRoute Overview — Microsoft Learn](https://learn.microsoft.com/en-us/azure/expressroute/expressroute-introduction)

#### ExpressRoute Global Reach

ExpressRoute Global Reach allows data exchange across on-premises sites through ExpressRoute circuits — cross-datacenter traffic uses the Microsoft backbone rather than the public internet.

[Azure ExpressRoute Overview — Microsoft Learn](https://learn.microsoft.com/en-us/azure/expressroute/expressroute-introduction)

### Azure VPN Gateway

Azure VPN Gateway creates encrypted tunnels over the public internet between Azure VNets and on-premises networks (site-to-site VPN) or individual devices (point-to-site VPN). It is lower cost than ExpressRoute but does not guarantee predictable throughput.

[About Azure VPN Gateway — Microsoft Learn](https://learn.microsoft.com/en-us/azure/vpn-gateway/vpn-gateway-about-vpngateways)

#### Zone-Redundant SKUs (2025 Transition)

Effective November 1, 2025, creation of new VPN gateways using VpnGw1-5 SKUs (non-AZ) is no longer possible. Microsoft transitioned to availability zone-supported SKUs (VpnGw1AZ or higher) to improve redundancy. Zone-redundant SKUs physically and logically separate gateways into different Availability Zones.

Bandwidth thresholds remain the same for zone-redundant gateways — upgrading to AZ SKUs does not reduce throughput.

[About zone-redundant virtual network gateway in Azure — Microsoft Learn](https://learn.microsoft.com/en-us/azure/vpn-gateway/about-zone-redundant-vnet-gateways)
[About gateway SKUs — Microsoft Learn](https://learn.microsoft.com/en-us/azure/vpn-gateway/about-gateway-skus)

#### Effective June 2025: AZ SKUs in All Regions

As of June 2025, AZ SKUs can be deployed in all Azure regions. If a region does not yet support availability zones, deployment remains regional until zone support is enabled.

[About gateway SKUs — Microsoft Learn](https://learn.microsoft.com/en-us/azure/vpn-gateway/about-gateway-skus)

### ExpressRoute vs. VPN Gateway Comparison

| Attribute | ExpressRoute | VPN Gateway |
|-----------|--------------|-------------|
| Connection type | Private (via connectivity provider) | Encrypted tunnel over public internet |
| Bandwidth | 50 Mbps – 10 Gbps (100 Gbps with Direct) | Up to 10 Gbps (VpnGw5AZ) |
| Latency | Consistent, predictable | Variable (internet path) |
| SLA | Yes — connection uptime SLA | Yes |
| Cost | Higher (circuit + gateway + port fees) | Lower |
| Setup complexity | High (requires connectivity provider) | Moderate |
| On-premises hardware | Requires CE router or colocation | Standard IPsec-capable device |
| ISV use case | Enterprise customer hybrid connectivity requirements | Dev/test hybrid or smaller enterprise customers |

[Azure ExpressRoute Overview — Microsoft Learn](https://learn.microsoft.com/en-us/azure/expressroute/expressroute-introduction)
[Azure ExpressRoute Vs Azure VPN Gateway — K21 Academy](https://k21academy.com/microsoft-azure/architect/azure-expressroute-vs-vpn/)
[Networking for SaaS Workloads on Azure — Microsoft Learn](https://learn.microsoft.com/en-us/azure/well-architected/saas/networking)

### Operational Profile

| Capability | On-Premises | Managed K8s | Cloud-Native (ExpressRoute/VPN GW) |
|------------|-------------|-------------|-------------------------------------|
| Hybrid Connectivity | Difficulty: 4/5 | Difficulty: 3/5 | Difficulty: 3/5 |
| Key requirements | Physical BGP routers, provider coordination | Gateway node pool, VPN/ER gateway integration | Gateway deployment, BGP peering, circuit provisioning |
| Representative tools | Cisco ASR, Juniper MX, provider circuits | Azure CNI with ER Gateway attachment | ExpressRoute Circuit + VNet Gateway |
| Est. FTE | 1.0–2.0 FTE | 0.5 FTE | 0.25–0.5 FTE |

*Note: Cloud-native difficulty for hybrid connectivity is rated 3/5 because ExpressRoute requires a connectivity provider relationship and BGP configuration regardless of deployment model. VPN Gateway alone rates 2/5.*

---

## Section 9: ISV SaaS Staffing Benchmarks

### IT-to-FTE Ratio Trend (2025)

The IT-to-FTE ratio has climbed 31% year-over-year to 1 IT person for every 108 full-time employees, the largest single-year increase in demand on IT teams in the history of the State of SaaS survey.

[State of SaaS 2025 Report — PRNewswire](https://www.prnewswire.com/news-releases/state-of-saas-2025-report-reveals-operational-complexity-and-risk-concerns-as-economic-uncertainty-and-ai-apply-spending-pressure-on-technology-investments-302441868.html)

### Azure Well-Architected SaaS Networking Guidance

"As you onboard more customers and their usage increases, networking requirements change. Handling growth can be challenging because of limited resources, like IP address ranges. Your network design affects security and customer isolation. Plan your network strategy to help manage growth, improve security, and reduce operational complexity."

"It's common to share networking resources, like virtual networks and Azure Front Door profiles, among multiple customers. This approach reduces costs and operational overhead."

"Manual operations are impractical, so automation and structured processes are necessary, requiring a degree of operational maturity."

[Networking for SaaS Workloads on Azure — Microsoft Learn](https://learn.microsoft.com/en-us/azure/well-architected/saas/networking)

---

## Key Takeaways

- **Azure networking is a fully managed control plane**: All services in this scope — Load Balancer, Application Gateway, Front Door, DNS, APIM, VNet, Private Link, ExpressRoute Gateway — abstract away physical hardware, control plane software, redundancy provisioning, and certificate lifecycle management. The ISV's operational burden shifts from infrastructure maintenance to declarative configuration.

- **Front Door + Application Gateway is the recommended ingress stack for ISV SaaS**: Front Door handles global anycast, CDN, and edge WAF (PoP count: 118 edge locations across 100 metro cities); Application Gateway handles regional L7 routing, WAF enforcement, and SSL termination. Together they eliminate the need for a globally distributed reverse proxy fleet.

- **Private Link is the ISV-to-customer connectivity primitive**: For ISVs deploying into customer Azure environments or accessing customer-owned Azure resources, Azure Private Link with Private DNS Zone integration is the recommended pattern — it supports cross-Entra-tenant connectivity, eliminates public IP exposure, and provides data leakage protection scoped to individual resource instances.

- **Azure API Management V2 tiers (GA 2025) materially reduce APIM operational complexity**: Premium v2 provides full VNet injection, availability zones, and workspaces in a platform that deploys in minutes. The token bucket rate-limiting algorithm in V2 tiers is more efficient than the sliding window in classic tiers. However, V2 tiers currently lack multi-region deployment and upgrade paths from classic instances.

- **Hybrid connectivity difficulty is inherently 3/5 regardless of deployment model**: ExpressRoute requires an external connectivity provider relationship, BGP configuration, and physical circuit provisioning. VPN Gateway is lower cost but does not guarantee throughput. The zone-redundant SKU mandate (effective November 1, 2025) is now enforced — all new VPN Gateway deployments must use AZ SKUs.

---

## Consolidated Operational Difficulty Summary

| Service | On-Premises | Managed K8s | Cloud-Native |
|---------|-------------|-------------|--------------|
| L4 Load Balancing (Azure LB) | 4/5 | 2/5 | 1/5 |
| L7 + WAF (Application Gateway) | 4/5 | 3/5 | 2/5 |
| Global CDN + Edge WAF (Front Door) | 5/5 | 4/5 | 2/5 |
| DNS (Public + Private) | 3/5 | 2/5 | 1/5 |
| API Management (APIM) | 4/5 | 3/5 | 2/5 |
| Private PaaS Connectivity (Private Link) | 5/5 | 3/5 | 2/5 |
| Hybrid Connectivity (ExpressRoute / VPN GW) | 4/5 | 3/5 | 3/5 |

---

## Related — Out of Scope

- Azure Firewall and Azure DDoS Protection Standard — related to perimeter security but not strictly networking services for this scope; covered as part of security research if assigned
- Azure Traffic Manager — DNS-based global load balancing; distinct from Front Door's anycast model; not investigated further
- Azure Virtual WAN — hub-and-spoke at scale; related to ExpressRoute and VPN Gateway aggregation but not investigated further
- Azure NAT Gateway — SNAT port exhaustion mitigation for egress at scale; mentioned in SaaS guidance but not a primary research topic for this file
- Azure Bastion — secure RDP/SSH access; out of networking services scope for this file

See [F16: Azure Compute] for AKS and VM context that interacts with the networking services documented here.

---

## Sources

| # | Source | URL |
|---|--------|-----|
| 1 | Azure Load Balancer health probes — Microsoft Learn | https://learn.microsoft.com/en-us/azure/load-balancer/load-balancer-custom-probe-overview |
| 2 | High availability ports overview — Microsoft Learn | https://learn.microsoft.com/en-us/azure/load-balancer/load-balancer-ha-ports-overview |
| 3 | Azure Load Balancer SKUs — Microsoft Learn | https://learn.microsoft.com/en-us/azure/load-balancer/skus |
| 4 | Gateway load balancer overview — Microsoft Learn | https://learn.microsoft.com/en-us/azure/load-balancer/gateway-overview |
| 5 | What is Azure Application Gateway — Microsoft Learn | https://learn.microsoft.com/en-us/azure/application-gateway/overview |
| 6 | Azure Application Gateway features — Microsoft Learn | https://learn.microsoft.com/en-us/azure/application-gateway/features |
| 7 | Enabling end to end TLS on Azure Application Gateway — Microsoft Learn | https://learn.microsoft.com/en-us/azure/application-gateway/ssl-overview |
| 8 | TLS policy overview for Azure Application Gateway — Microsoft Learn | https://learn.microsoft.com/en-us/azure/application-gateway/application-gateway-ssl-policy-overview |
| 9 | What Is Azure Web Application Firewall on Application Gateway — Microsoft Learn | https://learn.microsoft.com/en-us/azure/web-application-firewall/ag/ag-overview |
| 10 | CRS and DRS rule groups and rules — Microsoft Learn | https://learn.microsoft.com/en-us/azure/web-application-firewall/ag/application-gateway-crs-rulegroups-rules |
| 11 | Integrating Azure Application Gateway v2 with Azure API Management — Microsoft Community Hub | https://techcommunity.microsoft.com/blog/azurenetworkingblog/integrating-azure-application-gateway-v2-with-azure-api-management-for-secure-an/4470804 |
| 12 | Azure Front Door — Microsoft Learn | https://learn.microsoft.com/en-us/azure/frontdoor/front-door-overview |
| 13 | Azure Front Door POP Locations by Region — Microsoft Learn | https://learn.microsoft.com/en-us/azure/frontdoor/edge-locations-by-region |
| 14 | Azure Front Door FAQ — Microsoft Learn | https://learn.microsoft.com/en-us/azure/frontdoor/front-door-faq |
| 15 | Compare Pricing Between Azure Front Door Tiers — Microsoft Learn | https://learn.microsoft.com/en-us/azure/frontdoor/understanding-pricing |
| 16 | Architecture Best Practices for Azure Front Door — Microsoft Learn | https://learn.microsoft.com/en-us/azure/well-architected/service-guides/azure-front-door |
| 17 | What is Azure Public DNS — Azure Docs (mirror) | https://docs.azure.cn/en-us/dns/public-dns-overview |
| 18 | Alias records overview — Azure DNS — Azure Docs (mirror) | https://docs.azure.cn/en-us/dns/dns-alias |
| 19 | Azure Private DNS Zone Overview — Microsoft Learn | https://learn.microsoft.com/en-us/azure/dns/private-dns-privatednszone |
| 20 | Azure Private Endpoint private DNS zone values — Microsoft Learn | https://learn.microsoft.com/en-us/azure/private-link/private-endpoint-dns |
| 21 | Azure API Management V2 Tiers — Microsoft Learn | https://learn.microsoft.com/en-us/azure/api-management/v2-service-tiers-overview |
| 22 | Azure API Management policy reference — rate-limit — Microsoft Learn | https://learn.microsoft.com/en-us/azure/api-management/rate-limit-policy |
| 23 | Azure API Management policy reference — rate-limit-by-key — Microsoft Learn | https://learn.microsoft.com/en-us/azure/api-management/rate-limit-by-key-policy |
| 24 | AI gateway in Azure API Management — Microsoft Learn | https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities |
| 25 | Advanced Request Throttling with Azure API Management — Microsoft Learn | https://learn.microsoft.com/en-us/azure/api-management/api-management-sample-flexible-throttling |
| 26 | Azure API Management Premium v2 GA — InfoQ (December 2025) | https://www.infoq.com/news/2025/12/apim-v2-premium-secure-vnet/ |
| 27 | Azure virtual network service endpoints — Microsoft Learn | https://learn.microsoft.com/en-us/azure/virtual-network/virtual-network-service-endpoints-overview |
| 28 | Service Endpoints vs Private Endpoints — Microsoft Community Hub | https://techcommunity.microsoft.com/blog/coreinfrastructureandsecurityblog/service-endpoints-vs-private-endpoints/3962134 |
| 29 | Azure Private Endpoint vs. Service Endpoint — Microsoft Community Hub | https://techcommunity.microsoft.com/blog/fasttrackforazureblog/azure-private-endpoint-vs-service-endpoint-a-comprehensive-guide/4363095 |
| 30 | Azure Virtual Network Integration for Service Network Isolation — Microsoft Learn | https://learn.microsoft.com/en-us/azure/virtual-network/vnet-integration-for-azure-services |
| 31 | What is Azure Private Link — Microsoft Learn | https://learn.microsoft.com/en-us/azure/private-link/private-link-overview |
| 32 | What is Azure Private Link service — Microsoft Learn | https://learn.microsoft.com/en-us/azure/private-link/private-link-service-overview |
| 33 | Azure Private Link Explained (2025) — Orchestra | https://www.getorchestra.io/blog/azure-private-link-explained-2025 |
| 34 | Demystifying Azure Private Link — Microsoft Community Hub | https://techcommunity.microsoft.com/blog/azureinfrastructureblog/demystifying-azure-private-link-benefits-pitfalls--best-practices/4413945 |
| 35 | Azure ExpressRoute Overview — Microsoft Learn | https://learn.microsoft.com/en-us/azure/expressroute/expressroute-introduction |
| 36 | About Azure VPN Gateway — Microsoft Learn | https://learn.microsoft.com/en-us/azure/vpn-gateway/vpn-gateway-about-vpngateways |
| 37 | About gateway SKUs — Microsoft Learn | https://learn.microsoft.com/en-us/azure/vpn-gateway/about-gateway-skus |
| 38 | About zone-redundant virtual network gateway in Azure — Microsoft Learn | https://learn.microsoft.com/en-us/azure/vpn-gateway/about-zone-redundant-vnet-gateways |
| 39 | Azure ExpressRoute Vs Azure VPN Gateway — K21 Academy | https://k21academy.com/microsoft-azure/architect/azure-expressroute-vs-vpn/ |
| 40 | Networking for SaaS Workloads on Azure — Microsoft Well-Architected Framework | https://learn.microsoft.com/en-us/azure/well-architected/saas/networking |
| 41 | ISV considerations for Azure landing zones — Cloud Adoption Framework | https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/landing-zone/isv-landing-zone |
| 42 | State of SaaS 2025 Report — PRNewswire | https://www.prnewswire.com/news-releases/state-of-saas-2025-report-reveals-operational-complexity-and-risk-concerns-as-economic-uncertainty-and-ai-apply-spending-pressure-on-technology-investments-302441868.html |
| 43 | Migrate from Azure Basic to Standard Load Balancers Before 30 September 2025 | https://medium.com/@precious.ajuru/migrate-from-azure-basic-to-standard-load-balancers-before-30-september-2025-aab0fb2afe01 |
