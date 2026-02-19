# F13: AWS Networking Services
**Agent ID:** F13 | **Scope:** AWS Managed Networking — Load Balancing, DNS, API Management, CDN, VPC, Connectivity
**Date:** 2026-02-18 | **Audience:** C-suite and Technical Leadership

---

## Executive Summary

AWS provides a comprehensive suite of managed networking services that abstract away virtually all low-level infrastructure operations that an ISV would otherwise need to staff and operate. Elastic Load Balancing (ALB, NLB, GWLB), Route 53, API Gateway, CloudFront, and VPC networking collectively replace the equivalent of multiple specialized networking engineering roles — each service is fully managed by AWS with no control-plane overhead on the ISV. For SaaS ISVs, the most operationally significant abstractions are: automatic scaling of load balancers to handle sudden traffic spikes without provisioning, global anycast DNS with programmatic failover, and edge CDN with serverless compute capable of running at 200+ points of presence worldwide. The networking layer on AWS is a key operational differentiator versus on-premises deployment, where the equivalent capabilities require dedicated network engineers, hardware refresh cycles, and significant capital expenditure. AWS PrivateLink's November 2025 expansion to native cross-region connectivity further strengthens AWS's position for ISVs building globally distributed SaaS architectures with strict data residency requirements.

---

## 1. Elastic Load Balancing (ELB): ALB, NLB, and GWLB

AWS Elastic Load Balancing is a fully managed service offered in three distinct types, each targeting a different layer of the networking stack. The core abstraction is automatic scaling, health-aware traffic distribution, and TLS termination — all without ISV-managed hardware or software load balancers.

### 1.1 Application Load Balancer (ALB) — Layer 7

ALB operates at the request level (Layer 7), routing traffic to targets including EC2 instances, containers, IP addresses, and Lambda functions based on the content of the request. [AWS ALB documentation](https://aws.amazon.com/elasticloadbalancing/application-load-balancer/)

**Routing Rules:** ALB supports content-based routing on host headers, paths, HTTP headers, HTTP request methods, query strings, and source IP addresses. Each rule can include zero or one condition from: host-header, http-request-method, path-pattern, and source-ip, plus zero or more http-header and query-string conditions. [AWS Listener Rules Documentation](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/listener-update-rules.html)

**TLS Termination:** ALB terminates SSL/TLS connections and decrypts traffic at the edge, with SSL certificates residing on the ALB itself. Both ALB and NLB support FIPS 140-3 validated TLS termination using TLS policies, supporting compliance requirements. [AWS FSI ELB Spotlight](https://aws.amazon.com/blogs/industries/fsi-services-spotlight-featuring-elastic-load-balancing-elb-2/)

**Sticky Sessions:** ALB supports both duration-based cookies and application-based cookies for session affinity. WebSocket connections are inherently sticky: the target that returns HTTP 101 to accept the connection upgrade becomes the target for the entire WebSocket connection. [AWS ALB Sticky Sessions Documentation](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/sticky-sessions.html)

**WAF Integration:** AWS WAF can be attached directly to an ALB to protect web applications from common web exploits. [AWS ELB Features](https://aws.amazon.com/elasticloadbalancing/features/)

**Weighted Target Groups:** ALB supports weighted target groups, enabling canary deployments and blue/green traffic shifting at the load balancer level. [AWS ALB Weighted Target Groups](https://aws.amazon.com/blogs/aws/new-application-load-balancer-simplifies-deployment-with-weighted-target-groups/)

### 1.2 Network Load Balancer (NLB) — Layer 4

NLB operates at the connection level (Layer 4), routing connections within Amazon VPC based on IP protocol data. [AWS NLB Documentation](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/introduction.html)

**Performance:** NLB is designed to handle tens of millions of requests per second while maintaining high throughput at ultra-low latency. [AWS NLB Blog Announcement](https://aws.amazon.com/blogs/aws/new-network-load-balancer-effortless-scaling-to-millions-of-requests-per-second/)

**Static IP:** NLB provides a single static IP address per Availability Zone and also supports Elastic IP assignment per subnet, which is critical for ISVs whose enterprise customers whitelist IP addresses in their firewall rules. [AWS NLB Page](https://aws.amazon.com/elasticloadbalancing/network-load-balancer/)

**Protocol Support:** NLB supports TCP, UDP, and TCP+UDP (Layer 4) listeners, as well as TLS listeners. NLB also supports the QUIC and TCP_QUIC protocols with built-in TLS, fewer round-trip connection establishment, and connection migration across networks. [AWS NLB Page](https://aws.amazon.com/elasticloadbalancing/network-load-balancer/)

**Health Checks:** NLB supports TCP, HTTP, and HTTPS health check protocols. [AWS NLB Health Checks Documentation](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/target-group-health-checks.html)

### 1.3 Gateway Load Balancer (GWLB) — Layer 3

GWLB is designed to simplify deployment, scaling, and management of third-party virtual network appliances such as firewalls, intrusion detection and prevention systems, and deep packet inspection devices. [AWS GWLB Page](https://aws.amazon.com/elasticloadbalancing/gateway-load-balancer/)

**Transparent Inspection:** GWLB operates as a bump-in-the-wire solution, transparently intercepting and forwarding traffic without acting as a proxy. Original source and destination IP addresses are preserved. [AWS GWLB Architecture Patterns](https://aws.amazon.com/blogs/networking-and-content-delivery/introducing-aws-gateway-load-balancer-supported-architecture-patterns/)

**Centralized Inspection Architecture:** A dedicated inspection VPC is established to host firewall appliances. All traffic requiring inspection from spoke VPCs is routed through AWS Transit Gateway to these appliances. GWLB supports both east-west and north-south traffic inspection via GWLB endpoints powered by AWS PrivateLink. [AWS Centralized Inspection Architecture](https://aws.amazon.com/blogs/networking-and-content-delivery/centralized-inspection-architecture-with-aws-gateway-load-balancer-and-aws-transit-gateway/)

**Note:** GWLB does not perform TLS termination at the load balancer layer; this is intentional, as security appliances require access to the raw packet stream. [AWS ELB Overview](https://tutorialsdojo.com/aws-elastic-load-balancing-elb/)

---

## 2. Amazon Route 53: DNS Management and Routing

Route 53 is a fully managed, globally distributed DNS service built on a highly resilient anycast network of DNS servers, ensuring high availability, low latency, and automatic scaling to handle any query volume. [AWS Route 53 Complete Guide 2025](https://builder.aws.com/content/35T6YBNG2ywpuwZurZPnAZaJBY4/aws-route-53-the-complete-guide-2025-edition)

### 2.1 Routing Policies

Route 53 supports multiple routing policies that are programmable via API, enabling sophisticated global traffic management:

| Policy | Description | ISV Use Case |
|--------|-------------|--------------|
| **Simple** | Returns a single resource for DNS queries | Single-region deployments |
| **Weighted** | Distributes traffic in proportions specified by ISV (e.g., 25/75 split) | Canary releases, A/B testing |
| **Latency** | Routes to the AWS Region providing the lowest latency for the user | Global SaaS performance optimization |
| **Geolocation** | Routes based on continent, country, or US state | Data residency, localization |
| **Failover** | Active-passive failover; redirects to standby when primary fails health check | Disaster recovery |
| **Multivalue Answer** | Returns up to 8 healthy records selected at random | Simple load distribution |
| **IP-based** | Routes based on the CIDR block the DNS query originates from | Network-specific routing |

[AWS Route 53 Routing Policy Documentation](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html)

### 2.2 Health Checks

Route 53 health checks monitor the health and performance of application endpoints. If an endpoint becomes unhealthy, Route 53 automatically stops routing traffic to it. Health checks can be configured on endpoints, other health checks (calculated health checks), and CloudWatch alarms. [AWS Route 53 Complex Health Check Configurations](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-complex-configs.html)

### 2.3 Traffic Flow

Route 53 Traffic Flow is a visual editor for creating complex routing configurations using combinations of routing policies. Traffic policies can be versioned and reused across multiple hosted zones. [AWS Route 53 Traffic Policies Documentation](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/traffic-policies.html)

### 2.4 Route 53 Global Resolver (2025)

In late 2025, AWS announced the preview of Route 53 Global Resolver — a global, internet-reachable DNS resolver that enables resolution and forwarding for both public and private domains. Global Resolver simplifies resolution and forwarding of queries made from on-premises, branch offices, and remote clients to public domains and private applications hosted in the cloud or on-premises, offered as a unified solution reachable over global anycast IPs. [AWS Route 53 Global Resolver Announcement](https://aws.amazon.com/blogs/aws/introducing-amazon-route-53-global-resolver-for-secure-anycast-dns-resolution-preview/)

---

## 3. Amazon API Gateway: REST, HTTP, and WebSocket APIs

Amazon API Gateway is a fully managed service that enables ISVs to create, publish, maintain, monitor, and secure APIs at scale, without managing API servers or infrastructure. [AWS API Gateway Features Page](https://aws.amazon.com/api-gateway/features/)

### 3.1 API Types

AWS offers three distinct API types within API Gateway with meaningfully different capabilities and pricing:

| Feature | REST API | HTTP API | WebSocket API |
|---------|----------|----------|---------------|
| **Pricing** | $3.50/million requests | $1.00/million requests | $1.00/million messages |
| **API Key / Usage Plans** | Yes | No | No |
| **Per-client throttling** | Yes | No | No |
| **Request validation** | Yes | No | No |
| **AWS WAF integration** | Yes | No | No |
| **Response caching** | Yes | No | No |
| **Private API endpoints** | Yes | No | No |
| **Native OIDC/OAuth2** | Yes | Yes | No |
| **Lambda authorizers** | Yes | Yes | Yes |

[AWS API Gateway REST vs HTTP Comparison](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-vs-rest.html)

**ISV Guidance:** ISVs building multi-tenant SaaS APIs with per-customer rate limiting and monetization controls require REST APIs due to the Usage Plans feature. HTTP APIs are appropriate for internal microservice APIs where cost is the primary concern and per-client throttling is not required.

### 3.2 Throttling

API Gateway throttles requests using the token bucket algorithm. By default, API Gateway limits the steady-state request rate to 10,000 requests per second (rps) with a 5,000 request burst limit. These are soft limits adjustable via AWS Service Quotas. [AWS API Gateway Throttling Documentation](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-request-throttling.html)

For REST APIs, Usage Plans define per-API-key throttle limits (rate and burst) and quota limits (maximum requests per day, week, or month). This makes REST APIs the appropriate choice for tiered SaaS pricing models. [AWS API Gateway FAQs](https://aws.amazon.com/api-gateway/faqs/)

Lambda authorizer policy caching: if a policy returned by a custom authorizer is valid, API Gateway caches the policy associated with the incoming token for up to 1 hour, reducing Lambda invocation costs at scale. [AWS API Gateway Security Overview Whitepaper](https://docs.aws.amazon.com/whitepapers/latest/security-overview-amazon-api-gateway/about-amazon-api-gateway.html)

### 3.3 Authorization

API Gateway supports the following authorization mechanisms:
- AWS IAM authorization (SigV4-signed requests)
- Amazon Cognito user pools (JWT-based)
- Lambda authorizers (custom logic — JWT verification, OAuth provider callout, API key validation)
- Native OIDC and OAuth2 token validation (HTTP APIs only)

[AWS API Gateway FAQs](https://aws.amazon.com/api-gateway/faqs/)

### 3.4 Caching

REST APIs support optional response caching, charged at an hourly rate that varies based on the cache size selected. Caching reduces backend calls for frequently accessed, non-personalized data. Cache TTL and invalidation are configurable per method. [AWS API Gateway FAQs](https://aws.amazon.com/api-gateway/faqs/)

### 3.5 WebSocket APIs

API Gateway WebSocket APIs support persistent, stateful connections. Connections are managed via the `@connect`, `@disconnect`, and custom route keys. WebSocket APIs support Lambda authorizers for connection-time authorization. [AWS WebSocket API Protection Documentation](https://docs.aws.amazon.com/apigateway/latest/developerguide/websocket-api-protect.html)

---

## 4. Amazon CloudFront: CDN and Edge Compute

CloudFront is AWS's globally distributed CDN and edge compute platform. It serves content from a network of edge locations, reducing latency by delivering content closer to end users and absorbing traffic before it reaches origin servers.

### 4.1 Core CDN Capabilities

CloudFront caches content at edge locations. Cache-Hit Ratio and error rates (4xx/5xx) are observable in real-time via CloudWatch metrics. [Amazon CloudFront Cheat Sheet](https://tutorialsdojo.com/amazon-cloudfront/)

**Real-Time Logs:** CloudFront real-time logs can be streamed to Amazon Kinesis Data Streams for operational dashboards, monitoring, and alarms. Real-Time Logs are priced at $0.01 per 1 million log lines delivered to Kinesis Data Streams. [AWS CloudFront Origin Shield Blog](https://aws.amazon.com/blogs/networking-and-content-delivery/using-cloudfront-origin-shield-to-protect-your-origin-in-a-multi-cdn-deployment/)

### 4.2 Origin Shield

Origin Shield provides an additional caching layer between regional edge caches and origin servers. All requests from all CloudFront regional edge caches route through Origin Shield, increasing cache hit probability and reducing load on origin. This is particularly valuable for ISVs with compute-intensive or database-backed API responses. [AWS CloudFront Origin Shield Documentation](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/origin-shield.html)

### 4.3 Edge Functions: CloudFront Functions vs Lambda@Edge

CloudFront supports two distinct edge compute models with different capability envelopes:

| Characteristic | CloudFront Functions | Lambda@Edge |
|----------------|---------------------|-------------|
| **Execution locations** | 200+ edge caches | 13 regional edge caches |
| **Max execution time** | Sub-millisecond | 5s (viewer) / 30s (origin) |
| **Network calls** | Not supported | Supported |
| **AWS service access** | Not supported | Supported (S3, DynamoDB, etc.) |
| **Trigger events** | Viewer request, viewer response | Viewer request/response + origin request/response |
| **Runtime** | JavaScript (ES5.1) | Node.js, Python |
| **Relative cost** | ~1/6th of Lambda@Edge | Higher |

[AWS CloudFront Edge Functions Comparison](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/edge-functions-choosing.html)

**CloudFront Functions** are ideal for: URL rewrites, HTTP security header injection, lightweight request manipulation, and cookie manipulation — all at sub-millisecond latency at scale. [AWS CloudFront Functions Documentation](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cloudfront-functions.html)

**Lambda@Edge** is required for: JWT verification against external services, real-time authentication callouts, content personalization pulling from DynamoDB, and any logic requiring network I/O. [AWS CloudFront Functions vs Lambda@Edge](https://www.stormit.cloud/blog/cloudfront-functions-vs-lambda-at-edge/)

### 4.4 Post-Quantum TLS (2025)

In September 2025, AWS announced the new `TLS1.3_2025` security policy for CloudFront, which supports TLS 1.3 only. In November 2025, CloudFront added TLS 1.3 support for origin connections. Post-quantum key establishment (hybrid cryptography) support is available across all existing TLS security policies by default, with no additional charges and no customer configuration required. [AWS CloudFront TLS Post-Quantum Announcement](https://aws.amazon.com/about-aws/whats-new/2025/09/amazon-cloudfront-TLS-policy-post-quantum-support/)

---

## 5. Amazon VPC: Network Foundation

Amazon VPC is the foundational networking layer for all AWS compute workloads. It provides a logically isolated virtual network with full control over IP addressing, subnetting, routing, and security.

### 5.1 Subnets

Subnets are ranges of IP addresses within a VPC used to isolate tiers (public-facing, application, database). Public subnets route to an Internet Gateway; private subnets do not have direct internet access and route outbound traffic through NAT Gateways or NAT instances. [AWS VPC Security Best Practices](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-security-best-practices.html)

### 5.2 Security Groups

Security groups are stateful, instance-level firewalls. Because they are stateful, if a security group allows inbound traffic to an EC2 instance, responses are automatically allowed regardless of outbound security group rules. Security groups can reference other security groups by ID, enabling clean tier-based access control without managing IP ranges. [AWS VPC Infrastructure Security](https://docs.aws.amazon.com/vpc/latest/userguide/infrastructure-security.html)

### 5.3 Network Access Control Lists (NACLs)

NACLs are stateless, subnet-level packet filters. Because they are stateless, if a NACL rule allows inbound traffic, responses to that traffic are not automatically allowed — return traffic rules must be explicitly configured. NACLs evaluate rules in numeric order; the first matching rule is applied. [AWS VPC NACLs Documentation](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html)

**Security Group vs NACL Summary:** Security groups operate at the instance level and are stateful; NACLs operate at the subnet level and are stateless. Most ISV architectures rely primarily on security groups for day-to-day access control, with NACLs used as a coarse-grained defense-in-depth layer.

### 5.4 VPC Flow Logs

VPC Flow Logs capture IP traffic information going to and from network interfaces. Flow log data can be published to: Amazon CloudWatch Logs, Amazon S3, or Amazon Data Firehose. [AWS VPC Flow Logs Documentation](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html)

Flow logs consolidate records at 5-minute intervals and support Parquet formatting with time-based partitioning for cost-efficient querying via Amazon Athena. [AWS Flow Logs to S3 Documentation](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs-s3.html)

In 2025, Amazon CloudWatch added the ability to automatically enable VPC Flow Logs to CloudWatch Logs across an entire AWS Organization, with enablement rules that auto-create flow logs for both existing and newly created VPCs matching a defined scope. [AWS CloudWatch 2025 Update](https://www.thenasguy.com/2025/12/02/amazon-cloudwatch-introduces-unified-data-management-and-analytics-for-operations-security-and-compliance/)

### 5.5 VPC Peering

VPC peering connects two VPCs via an encrypted virtual link. VPC peering is supported within the same region, across regions, and across AWS accounts. Traffic travels over the AWS backbone and does not traverse the public internet. [AWS VPC Blog](https://www.applify.co/blog/what-is-aws-vpc)

**Limitation:** VPC peering does not support transitive routing — VPC A peered to VPC B and VPC B peered to VPC C does not give VPC A connectivity to VPC C. This limitation is the primary driver for adopting AWS Transit Gateway at scale. [AWS VPC Peering vs Transit Gateway](https://cloudviz.io/blog/aws-vpc-peering-vs-transit-gateway)

---

## 6. AWS PrivateLink: Private Service Connectivity

AWS PrivateLink enables private connectivity from a VPC to services and resources as if they were within the same VPC, without needing an internet gateway, NAT device, public IP address, Direct Connect connection, or VPN connection. [AWS PrivateLink Documentation](https://docs.aws.amazon.com/vpc/latest/privatelink/what-is-privatelink.html)

### 6.1 Interface VPC Endpoints

Interface VPC endpoints (powered by PrivateLink) create Elastic Network Interfaces (ENIs) with private IP addresses in the VPC's subnets. VPC Security Groups can be attached to these ENIs for fine-grained access control. [AWS PrivateLink Concepts](https://docs.aws.amazon.com/vpc/latest/privatelink/concepts.html)

Traffic between a VPC endpoint and an endpoint service or resource stays within the AWS network and does not traverse the public internet. [AWS PrivateLink Page](https://aws.amazon.com/privatelink/)

### 6.2 ISV Endpoint Services (Selling via PrivateLink)

ISVs can expose their own services as PrivateLink Endpoint Services, allowing customer VPCs in other AWS accounts to connect privately to the ISV's service. This is a common pattern for B2B SaaS ISVs delivering services to enterprise customers who prohibit internet-bound API calls. [AWS PrivateLink Page](https://aws.amazon.com/privatelink/)

### 6.3 Cross-Region PrivateLink (November 2025)

A significant capability expansion announced November 19, 2025: AWS PrivateLink now supports native cross-region connectivity to AWS services. Previously, Interface VPC endpoints only supported connectivity to AWS services in the same region. This launch enables customers to connect to select AWS services hosted in other AWS regions of the same partition over Interface endpoints. Supported services at launch include Amazon S3, Route 53, ECR, IAM, and Amazon Data Firehose. [AWS PrivateLink Cross-Region Announcement](https://aws.amazon.com/about-aws/whats-new/2025/11/aws-privatelink-cross-region-connectivity-aws-services/)

Cross-region connectivity is billed at standard PrivateLink pricing with standard EC2 inter-region data transfer charges. [AWS SDxCentral Cross-Region Coverage](https://www.sdxcentral.com/news/aws-brings-cross-region-connectivity-at-zero-extra-cost/)

---

## 7. AWS Transit Gateway: Scalable Multi-VPC Networking

AWS Transit Gateway acts as a hub in a hub-and-spoke architecture, providing centralized connectivity for Amazon VPC networks and on-premises networks. It eliminates the need for complex, full-mesh VPC peering arrangements. [AWS Transit Gateway Documentation](https://docs.aws.amazon.com/whitepapers/latest/building-scalable-secure-multi-vpc-network-infrastructure/transit-gateway.html)

### 7.1 Core Capabilities

Transit Gateway scales to support thousands of VPCs and VPN connections. Each attachment to Transit Gateway has an associated route table, and Transit Gateway makes forwarding decisions using the route table associated with each incoming attachment. This enables sophisticated network segmentation (e.g., isolating production from development VPCs while allowing shared services access). [AWS Transit Gateway FAQs](https://aws.amazon.com/transit-gateway/faqs/)

AWS Transit Gateway traffic always stays on the global AWS backbone and never traverses the public internet. [AWS Building Scalable Multi-VPC Whitepaper](https://docs.aws.amazon.com/whitepapers/latest/building-scalable-secure-multi-vpc-network-infrastructure/transit-gateway.html)

### 7.2 Cross-Region Peering

Transit Gateway supports inter-region peering, allowing Transit Gateway instances across regions to be connected. Traffic between regions travels over the AWS backbone without traversing the public internet, reducing threat vectors. [AWS Building a Global Network with TGW Inter-Region Peering](https://aws.amazon.com/blogs/networking-and-content-delivery/building-a-global-network-using-aws-transit-gateway-inter-region-peering/)

### 7.3 Connect Attachments (SD-WAN Integration)

Transit Gateway Connect attachments support SD-WAN integration. Each Connect attachment supports up to 4 Connect peers with a maximum of 20 Gbps total bandwidth per Connect attachment, provided the underlying transport attachment supports the required bandwidth. [AWS Transit Gateway Quotas](https://docs.aws.amazon.com/vpc/latest/tgw/transit-gateway-quotas.html)

There are no additional data processing charges for Transit Gateway Connect beyond those applied to the underlying VPC or Direct Connect attachment. [AWS Transit Gateway Pricing](https://aws.amazon.com/transit-gateway/pricing/)

### 7.4 AWS Cloud WAN (2025 Evolution)

AWS Cloud WAN introduces global network segments that unify multiple Transit Gateways, regions, and on-premises connections under a single policy, with centralized route management integrated directly with AWS Network Manager. For ISVs operating across many regions, Cloud WAN represents a further abstraction above Transit Gateway. [AWS CloudOptimo TGW Guide](https://www.cloudoptimo.com/blog/mastering-aws-transit-gateway-architecture-use-cases-and-best-practices/)

---

## 8. AWS App Mesh and Amazon VPC Lattice: Service Mesh

### 8.1 AWS App Mesh — Deprecation Notice

AWS App Mesh is a managed service mesh based on the open-source Envoy proxy. It configures Envoy proxies as sidecars to manage all traffic into and out of service containers, providing traffic management, mutual TLS, observability, and load balancing without application code changes. [AWS App Mesh Features](https://aws.amazon.com/app-mesh/features/)

**End-of-Life:** AWS has announced the discontinuation of AWS App Mesh, effective September 30, 2026. Existing customers can use the service as normal, including creating new resources, until that date. [AWS App Mesh Deprecation Guide](https://earezki.com/ai-news/2026-02-15-aws-app-mesh-deprecated-migration-guide-before-september-2026-shutdown/)

App Mesh relies on a self-managed Envoy proxy sidecar container with each Pod, which added operational overhead for certificate management, proxy versioning, and configuration. [AWS Migrating from App Mesh to VPC Lattice](https://aws.amazon.com/blogs/containers/migrating-from-aws-app-mesh-to-amazon-vpc-lattice/)

**ISV Action Required:** ISVs currently running App Mesh must migrate before September 30, 2026. AWS officially recommends Amazon VPC Lattice (for EKS) and Amazon ECS Service Connect (for ECS) as replacements.

### 8.2 Amazon VPC Lattice — Recommended Replacement

Amazon VPC Lattice is a fully managed application networking service that enables consistent connectivity, security, and monitoring for communications between services across Amazon ECS, EKS, Lambda, and EC2 — without sidecar proxies. VPC Lattice provides a managed control plane and data plane, eliminating the need for additional components within Pods. [AWS VPC Lattice Page](https://aws.amazon.com/vpc/lattice/)

**Multi-Tenant SaaS Applications:** VPC Lattice provides prescriptive guidance for multi-tenant SaaS network architectures, addressing challenges such as managing overlapping IP addresses, complex CIDR planning, and scaling connectivity to thousands of customers. Resource Gateways extend VPC Lattice capabilities to allow direct connectivity to customer resources that traditionally needed complex networking setups. [AWS VPC Lattice Multi-Tenant SaaS Blog](https://aws.amazon.com/blogs/networking-and-content-delivery/secure-customer-resource-access-in-multi-tenant-saas-with-amazon-vpc-lattice/)

**Cross-Account Connectivity:** VPC Lattice natively solves cross-account and cross-VPC access problems by incorporating load balancing and AWS Resource Access Manager (RAM), allowing Kubernetes services to be accessed from other AWS accounts without VPC peering or Transit Gateway. [Application Networking with VPC Lattice and EKS](https://aws.amazon.com/blogs/containers/application-networking-with-amazon-vpc-lattice-and-amazon-eks/)

---

## 9. Operational Difficulty Comparison by Deployment Model

The following table rates the operational difficulty of AWS networking capabilities across three deployment models. Assumptions: mid-size ISV serving 50 enterprise SaaS customers; single primary cloud region with one DR region; 10–50 microservices.

| Capability Domain | On-Premises | Managed K8s (EKS/AKS/GKE) | Cloud-Native (AWS Managed) |
|---|---|---|---|
| **Load Balancing** | **Difficulty: 4/5** | **Difficulty: 3/5** | **Difficulty: 1/5** |
| | HAProxy/NGINX/F5 hardware provisioning, HA config, cert rotation | nginx-ingress or AWS LB Controller, K8s integration, version upgrades | ELB fully managed; ISV defines rules, AWS handles capacity |
| | Manual failover testing, firmware updates | Helm chart management, ingress class config | No software to install or upgrade |
| | Est. FTE: 0.5–1.0 | Est. FTE: 0.25–0.5 | Est. FTE: 0.1 |
| **DNS Management** | **Difficulty: 3/5** | **Difficulty: 3/5** | **Difficulty: 1/5** |
| | BIND/PowerDNS cluster management, zone file versioning, TTL planning | ExternalDNS operator, K8s service annotations, split-horizon DNS | Route 53 API-driven; routing policies programmatic |
| | Manual failover, geo-routing requires appliances | Health check integration requires controller config | Built-in health-check-based failover |
| | Est. FTE: 0.25–0.5 | Est. FTE: 0.25 | Est. FTE: 0.05 |
| **API Gateway** | **Difficulty: 5/5** | **Difficulty: 3/5** | **Difficulty: 2/5** |
| | Kong/Apigee self-hosted, Lua/plugin management, Redis for rate limiting | Kong Ingress Controller, CRD management, plugin version compatibility | AWS API Gateway fully managed; usage plans configured via console/API |
| | Capacity planning, HA setup, upgrade windows | Operator management, Helm values complexity | No patching, auto-scaling, built-in auth integrations |
| | Est. FTE: 0.5–1.0 | Est. FTE: 0.5 | Est. FTE: 0.25 |
| **CDN / Edge Compute** | **Difficulty: 5/5** | **Difficulty: 4/5** | **Difficulty: 1/5** |
| | CDN appliance or commercial CDN contract, PoP management | External CDN (Cloudflare) integration, cache invalidation logic | CloudFront fully managed; edge functions deployed via CLI/console |
| | Cache invalidation, edge node provisioning, DDoS contracts | WAF rule propagation across zones | Lambda@Edge/CloudFront Functions serverless; no server management |
| | Est. FTE: 1.0+ or outsourced | Est. FTE: 0.5 | Est. FTE: 0.1–0.25 |
| **Private Network / VPC** | **Difficulty: 4/5** | **Difficulty: 3/5** | **Difficulty: 2/5** |
| | VLAN design, physical switch config, ACL management | VPC CNI plugin config, network policy (Calico/Cilium), pod CIDR planning | VPC subnets, security groups, NACLs — managed via Terraform/CDK |
| | Firewall appliance management, BGP routing | Security group management for nodes + pods | No physical infrastructure; flow logs built-in |
| | Est. FTE: 1.0–2.0 | Est. FTE: 0.5–1.0 | Est. FTE: 0.25–0.5 |
| **Inter-Service Connectivity** | **Difficulty: 4/5** | **Difficulty: 3/5** | **Difficulty: 2/5** |
| | Manual VLAN trunking, BGP peering for multi-datacenter | VPC peering or Transit Gateway, K8s Network Policies | VPC Lattice or PrivateLink; no sidecar proxies required |
| | Service discovery requires Consul or custom DNS | Service mesh (Istio) adds significant operational burden | AWS manages control plane and data plane |
| | Est. FTE: 0.5–1.0 | Est. FTE: 0.5 | Est. FTE: 0.1–0.25 |

---

## 10. What AWS Networking Abstracts Away

For ISV leadership evaluating build-vs-buy for networking infrastructure, the following table catalogs specific operational tasks eliminated by AWS managed networking services:

| Task Eliminated | Self-Hosted Equivalent | AWS Managed Equivalent |
|-----------------|------------------------|------------------------|
| Load balancer capacity planning | HAProxy/F5 right-sizing, over-provisioning | Auto-scales transparently — ALB/NLB/GWLB |
| TLS certificate renewal | Certbot/ACME automation, renewal monitoring | AWS Certificate Manager auto-renews; integrated with ALB/NLB |
| DNS zone file management | BIND zone files, version control, propagation | Route 53 API; changes propagate in seconds |
| API rate limiting infrastructure | Redis cluster for token buckets | API Gateway Usage Plans, no Redis to manage |
| CDN node operation | Commercial CDN SLA, PoP management | CloudFront — no PoP operations required |
| Network appliance patching | Firewall/IDS firmware updates, maintenance windows | GWLB auto-scales the appliance fleet; AWS patches underlying infrastructure |
| Service mesh sidecar management | Envoy proxy versioning, certificate rotation via SPIFFE | VPC Lattice eliminates sidecars entirely |
| BGP / inter-datacenter routing | BGP expertise, route leaking prevention | Transit Gateway handles hub-and-spoke routing with GUI/API |
| VPN endpoint management | IPsec IKE negotiation, dead peer detection | AWS Site-to-Site VPN managed by AWS |
| DDoS mitigation | Commercial DDoS scrubbing contracts | AWS Shield Standard (included) / Advanced |

---

## Key Takeaways

- **AWS managed networking eliminates an entire networking engineering function for most mid-size ISVs.** The aggregate FTE saving versus on-premises across load balancing, DNS, API gateway, CDN, and VPC networking is estimated at 3.0–6.0 FTE for a 50-customer SaaS deployment, based on the difficulty ratings and FTE estimates above. [UNVERIFIED: No industry benchmark directly measuring this specific stack combination was found for 2025–2026; this estimate is derived by summing the FTE ranges in Section 9 above.]

- **AWS App Mesh has a hard end-of-life deadline of September 30, 2026.** ISVs using App Mesh must plan and execute migration to Amazon VPC Lattice or ECS Service Connect before this date to avoid service disruption. [AWS App Mesh Deprecation](https://earezki.com/ai-news/2026-02-15-aws-app-mesh-deprecated-migration-guide-before-september-2026-shutdown/)

- **PrivateLink's November 2025 cross-region expansion directly benefits ISVs with enterprise customers requiring private API connectivity across AWS regions.** ISVs can now serve customers consuming APIs from a different region without exposing traffic to the public internet or requiring VPC peering. [AWS PrivateLink Cross-Region Announcement](https://aws.amazon.com/about-aws/whats-new/2025/11/aws-privatelink-cross-region-connectivity-aws-services/)

- **CloudFront's post-quantum TLS (TLS1.3_2025 policy, September 2025) is available at no additional cost** and positions ISVs selling to government, financial services, and defense customers who will face post-quantum cryptography compliance requirements in the 2025–2030 timeframe. [AWS CloudFront Post-Quantum TLS](https://aws.amazon.com/about-aws/whats-new/2025/09/amazon-cloudfront-TLS-policy-post-quantum-support/)

- **The operational complexity gap between on-premises and cloud-native networking is the largest of any infrastructure domain.** Networking on-premises requires specialized hardware expertise, BGP/routing knowledge, physical cabling, and appliance lifecycle management — skills that are scarce and expensive. AWS managed networking replaces all of this with API calls, Terraform/CDK configuration, and managed services with AWS-backed SLAs.

---

## Related — Out of Scope

- **AWS compute services (EC2, ECS, EKS, Lambda):** Referenced as ALB/NLB target types but not investigated. See [F8: AWS Compute Services] for detailed coverage of compute options.
- **AWS WAF and AWS Shield:** Mentioned as ALB and CloudFront integrations but not investigated in depth. These are security-layer services beyond the networking scope of this file.
- **AWS Direct Connect:** Physical dedicated connectivity from on-premises to AWS. Mentioned as an alternative to PrivateLink but not investigated.
- **Azure and GCP networking equivalents:** Out of scope per assignment; comparable services (Azure Front Door, GCP Cloud Load Balancing) exist but are not covered here.
- **Amazon VPC Lattice pricing details:** Lattice was identified as the App Mesh replacement and covered at an architectural level; detailed pricing analysis was not investigated.

---

## Sources

- [AWS Application Load Balancer](https://aws.amazon.com/elasticloadbalancing/application-load-balancer/)
- [AWS ALB Listener Rules Documentation](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/listener-update-rules.html)
- [AWS ALB Condition Types](https://docs.aws.amazon.com/en_us/elasticloadbalancing/latest/application/rule-condition-types.html)
- [AWS ALB Sticky Sessions](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/sticky-sessions.html)
- [AWS ALB Weighted Target Groups Blog](https://aws.amazon.com/blogs/aws/new-application-load-balancer-simplifies-deployment-with-weighted-target-groups/)
- [AWS ELB Features](https://aws.amazon.com/elasticloadbalancing/features/)
- [AWS FSI ELB Spotlight](https://aws.amazon.com/blogs/industries/fsi-services-spotlight-featuring-elastic-load-balancing-elb-2/)
- [AWS NLB Documentation](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/introduction.html)
- [AWS NLB Page](https://aws.amazon.com/elasticloadbalancing/network-load-balancer/)
- [AWS NLB Blog — Millions of Requests per Second](https://aws.amazon.com/blogs/aws/new-network-load-balancer-effortless-scaling-to-millions-of-requests-per-second/)
- [AWS NLB Health Checks Documentation](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/target-group-health-checks.html)
- [AWS GWLB Page](https://aws.amazon.com/elasticloadbalancing/gateway-load-balancer/)
- [AWS GWLB Architecture Patterns Blog](https://aws.amazon.com/blogs/networking-and-content-delivery/introducing-aws-gateway-load-balancer-supported-architecture-patterns/)
- [AWS GWLB Centralized Inspection Architecture](https://aws.amazon.com/blogs/networking-and-content-delivery/centralized-inspection-architecture-with-aws-gateway-load-balancer-and-aws-transit-gateway/)
- [AWS Route 53 Routing Policy Documentation](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html)
- [AWS Route 53 Failover Routing](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy-failover.html)
- [AWS Route 53 Traffic Policies Documentation](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/traffic-policies.html)
- [AWS Route 53 Complex Health Check Configurations](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-complex-configs.html)
- [AWS Route 53 Complete Guide 2025](https://builder.aws.com/content/35T6YBNG2ywpuwZurZPnAZaJBY4/aws-route-53-the-complete-guide-2025-edition)
- [AWS Route 53 Global Resolver Announcement](https://aws.amazon.com/blogs/aws/introducing-amazon-route-53-global-resolver-for-secure-anycast-dns-resolution-preview/)
- [AWS API Gateway Features Page](https://aws.amazon.com/api-gateway/features/)
- [AWS API Gateway FAQs](https://aws.amazon.com/api-gateway/faqs/)
- [AWS API Gateway REST vs HTTP Comparison](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-vs-rest.html)
- [AWS API Gateway Throttling Documentation](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-request-throttling.html)
- [AWS API Gateway Quotas](https://docs.aws.amazon.com/apigateway/latest/developerguide/limits.html)
- [AWS API Gateway Security Overview Whitepaper](https://docs.aws.amazon.com/whitepapers/latest/security-overview-amazon-api-gateway/about-amazon-api-gateway.html)
- [AWS WebSocket API Protection Documentation](https://docs.aws.amazon.com/apigateway/latest/developerguide/websocket-api-protect.html)
- [AWS CloudFront Edge Functions Comparison](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/edge-functions-choosing.html)
- [AWS CloudFront Functions Documentation](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cloudfront-functions.html)
- [AWS CloudFront Origin Shield Documentation](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/origin-shield.html)
- [AWS CloudFront Origin Shield Multi-CDN Blog](https://aws.amazon.com/blogs/networking-and-content-delivery/using-cloudfront-origin-shield-to-protect-your-origin-in-a-multi-cdn-deployment/)
- [AWS CloudFront Post-Quantum TLS Announcement](https://aws.amazon.com/about-aws/whats-new/2025/09/amazon-cloudfront-TLS-policy-post-quantum-support/)
- [AWS CloudFront TLS 1.3 Origin Announcement](https://aws.amazon.com/about-aws/whats-new/2025/11/amazon-cloudfront-tls13-origin/)
- [Amazon CloudFront Cheat Sheet — Tutorials Dojo](https://tutorialsdojo.com/amazon-cloudfront/)
- [CloudFront Functions vs Lambda@Edge — Stormit](https://www.stormit.cloud/blog/cloudfront-functions-vs-lambda-at-edge/)
- [AWS VPC Security Best Practices](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-security-best-practices.html)
- [AWS VPC NACLs Documentation](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html)
- [AWS VPC Infrastructure Security](https://docs.aws.amazon.com/vpc/latest/userguide/infrastructure-security.html)
- [AWS VPC Flow Logs Documentation](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html)
- [AWS VPC Flow Logs to S3 Documentation](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs-s3.html)
- [AWS VPC Peering vs Transit Gateway — Cloudviz](https://cloudviz.io/blog/aws-vpc-peering-vs-transit-gateway)
- [AWS PrivateLink Documentation](https://docs.aws.amazon.com/vpc/latest/privatelink/what-is-privatelink.html)
- [AWS PrivateLink Concepts](https://docs.aws.amazon.com/vpc/latest/privatelink/concepts.html)
- [AWS PrivateLink Page](https://aws.amazon.com/privatelink/)
- [AWS PrivateLink Cross-Region Announcement — November 2025](https://aws.amazon.com/about-aws/whats-new/2025/11/aws-privatelink-cross-region-connectivity-aws-services/)
- [AWS PrivateLink Cross-Region Technical Blog](https://aws.amazon.com/blogs/networking-and-content-delivery/aws-privatelink-extends-cross-region-connectivity-to-aws-services/)
- [AWS PrivateLink Cross-Region Additional Regions — March 2025](https://aws.amazon.com/about-aws/whats-new/2025/03/aws-privatelink-cross-region-connectivity-6-additional-regions/)
- [AWS Transit Gateway Documentation — Scalable Secure Multi-VPC](https://docs.aws.amazon.com/whitepapers/latest/building-scalable-secure-multi-vpc-network-infrastructure/transit-gateway.html)
- [AWS Transit Gateway FAQs](https://aws.amazon.com/transit-gateway/faqs/)
- [AWS Transit Gateway Features](https://aws.amazon.com/transit-gateway/features/)
- [AWS Transit Gateway Pricing](https://aws.amazon.com/transit-gateway/pricing/)
- [AWS Transit Gateway Quotas](https://docs.aws.amazon.com/vpc/latest/tgw/transit-gateway-quotas.html)
- [AWS TGW Inter-Region Peering Blog](https://aws.amazon.com/blogs/networking-and-content-delivery/building-a-global-network-using-aws-transit-gateway-inter-region-peering/)
- [AWS App Mesh Features](https://aws.amazon.com/app-mesh/features/)
- [AWS App Mesh FAQs](https://aws.amazon.com/app-mesh/faqs/)
- [AWS App Mesh Deprecation Guide](https://earezki.com/ai-news/2026-02-15-aws-app-mesh-deprecated-migration-guide-before-september-2026-shutdown/)
- [AWS Migrating from App Mesh to VPC Lattice](https://aws.amazon.com/blogs/containers/migrating-from-aws-app-mesh-to-amazon-vpc-lattice/)
- [AWS VPC Lattice Page](https://aws.amazon.com/vpc/lattice/)
- [AWS VPC Lattice Multi-Tenant SaaS Blog](https://aws.amazon.com/blogs/networking-and-content-delivery/secure-customer-resource-access-in-multi-tenant-saas-with-amazon-vpc-lattice/)
- [AWS Application Networking with VPC Lattice and EKS](https://aws.amazon.com/blogs/containers/application-networking-with-amazon-vpc-lattice-and-amazon-eks/)
- [AWS SDxCentral PrivateLink Cross-Region Coverage](https://www.sdxcentral.com/news/aws-brings-cross-region-connectivity-at-zero-extra-cost/)
