# F41 — On-Premises Relational Databases: Operational Requirements and Trade-offs

**Research Date:** February 18, 2026
**Scope:** Self-hosted relational databases (PostgreSQL / MySQL) in production on-premises environments, compared against managed services (Amazon RDS, Azure SQL, Google Cloud SQL)
**Audience:** C-suite and technical leadership evaluating ISV deployment models

---

## Executive Summary

Self-hosting a production relational database — most commonly PostgreSQL — carries a substantial and frequently underestimated operational burden. An on-premises PostgreSQL cluster requires expert-level configuration across at least seven distinct domains: OS-level tuning, connection pooling, high-availability orchestration, backup and recovery, upgrade management, monitoring, and security hardening. Each domain demands dedicated DBA expertise, and failures in any single domain can cause data loss or multi-hour outages. Managed services such as Amazon RDS, Azure Database for PostgreSQL, and Google Cloud SQL automate the majority of this operational surface, trading flexibility and control for dramatically lower staff burden — typically shifting DBA effort from 1.5–3.0 FTE to 0.25–0.5 FTE for equivalent workloads. For ISVs without in-house database specialists, the risk-adjusted cost of self-hosting is almost always higher than the raw infrastructure premium of managed services. On-premises relational database hosting is best suited to organizations with strict data-residency mandates, highly customized PostgreSQL configurations, or existing deep DBA capability.

---

## 1. Installation and Initial Configuration

### 1.1 OS-Level Tuning

A production PostgreSQL deployment begins not with the database itself, but with Linux kernel tuning. The default kernel settings on most Linux distributions are optimized for general workloads and perform poorly under database I/O patterns. Key parameters that must be configured include:

- **`vm.swappiness`**: Should be set to `1`–`10` to minimize swapping. The Linux default of `60` causes PostgreSQL's shared buffer pool to be paged out under memory pressure, producing severe latency spikes. [Percona recommends `vm.swappiness = 10`](https://www.percona.com/blog/tune-linux-kernel-parameters-for-postgresql-optimization/).
- **Transparent Huge Pages (THP)**: Must be disabled at the OS level. THP causes memory fragmentation and unpredictable latency spikes in database workloads; explicit Huge Pages must be reserved instead. [Stormatics (2025) documents that THP causes "memory fragmentation and unpredictable latency spikes in database workloads"](https://stormatics.tech/blogs/configuring-linux-huge-pages-for-postgresql).
- **`vm.dirty_ratio` / `vm.dirty_background_ratio`**: Must be tuned down from defaults to prevent large dirty-page write bursts that stall I/O. Recommended values are `10` and `3`, respectively.
- **`vm.overcommit_memory`**: Set to `0` (heuristic overcommit) to prevent the OOM killer from terminating postgres backend processes.

### 1.2 PostgreSQL Configuration Parameters

PostgreSQL ships with a deliberately conservative `postgresql.conf` that must be retuned for production. For a representative 16 GB RAM server, [the Percona and Mydbops 2025 tuning guides](https://www.mydbops.com/blog/postgresql-parameter-tuning-best-practices) recommend:

| Parameter | Default | Production Recommendation | Rationale |
|---|---|---|---|
| `shared_buffers` | 128 MB | 4 GB (25% of RAM) | Primary in-memory data cache |
| `work_mem` | 4 MB | 64 MB (OLTP) | Per-sort operation allocation |
| `maintenance_work_mem` | 64 MB | 512 MB | VACUUM, REINDEX, CREATE INDEX |
| `max_connections` | 100 | 200 (with pooler) | See connection pooling below |
| `wal_level` | minimal | replica | Required for replication |
| `checkpoint_timeout` | 5 min | 15 min | Balance WAL I/O vs. recovery time |
| `max_wal_size` | 1 GB | 2–4 GB | Reduce checkpoint frequency |
| `effective_cache_size` | 4 GB | 12 GB | Query planner hint (12 GB = 75% RAM) |

Source: [PostgreSQL Performance Tuning Best Practices 2025 — Mydbops](https://www.mydbops.com/blog/postgresql-parameter-tuning-best-practices); [dbadataverse.com Complete Guide 2025](https://dbadataverse.com/tech/postgresql/2025/02/postgresql-performance-tuning-complete-guide)

### 1.3 Connection Pooling with PgBouncer

PostgreSQL uses a **process-per-connection model**: each new client connection spawns a separate OS-level process. Research from Microsoft's Azure PostgreSQL team shows that [each backend process starts at around 5 MB and can grow substantially under load](https://techcommunity.microsoft.com/blog/adforpostgresql/analyzing-the-limits-of-connection-scalability-in-postgres/1757266). A general rule of thumb is that more than 200 direct connections without a pooler causes measurable performance degradation.

PgBouncer is the production-standard connection pooler. A typical production configuration sets `listen_port = 6432`, `pool_mode = transaction`, `default_pool_size` matching the database's server-side connection capacity, `max_client_conn = 1000`, and `max_db_connections = 100`. [Opstree's 2025 production guide](https://opstree.com/blog/2025/10/07/postgresql-performance-with-pgbouncer/) documents PgBouncer as the standard solution for preventing "performance degradation caused by too many simultaneous or idle database connections." The operational overhead of maintaining PgBouncer (configuration, auth sync, monitoring) is non-trivial and adds to the overall DBA workload.

---

## 2. High Availability

### 2.1 Streaming Replication

PostgreSQL's native high-availability mechanism is **streaming replication** — a WAL-based approach where changes to the Write-Ahead Log are continuously shipped from a primary node to one or more standbys. [Patroni documentation confirms](https://patroni.readthedocs.io/en/latest/replication_modes.html) that standby instances replay WAL in near real-time and can assume the primary role on failover.

By default, streaming replication is **asynchronous**, meaning a primary can acknowledge a committed transaction before it is confirmed on the standby. For workloads where losing committed transactions is unacceptable, `synchronous_mode` must be enabled, which blocks commits until the standby confirms receipt. This introduces latency on every write.

### 2.2 Automated Failover: Patroni vs. repmgr

Manual failover of a PostgreSQL primary is a multi-step, error-prone procedure. Two open-source tools automate this: **Patroni** and **repmgr**.

**Patroni** is the more capable and more widely adopted option. It uses a distributed consensus store (etcd, Consul, or ZooKeeper) to hold a leader lease, ensuring only one node can be primary at any time. [Percona's enterprise documentation](https://www.percona.com/blog/patroni-the-key-postgresql-component-for-enterprise-high-availability/) states that Patroni "monitors the health of PostgreSQL nodes and automatically promotes a replica to primary if the current primary fails, with this automated failover process reducing downtime to just a few seconds." The dependency on a correctly configured etcd/Consul cluster adds significant operational complexity — Patroni is described as "one of the most automated failover management systems but also one of the most difficult to properly deploy and debug."

**repmgr** is lighter-weight and simpler to install. [repmgr's official documentation](https://www.repmgr.org/docs/current/repmgrd-witness-server.html) describes witness server support: a witness is a standalone PostgreSQL instance whose purpose is to "provide proof that it is the primary server itself which is unavailable, rather than a network split." However, [Stormatics' 2025 analysis of split-brain scenarios](https://stormatics.tech/blogs/split-brain-in-postgresql-clusters-causes-prevention-and-resolution) notes that repmgr's split-brain prevention requires at least three nodes and careful configuration.

### 2.3 Split-Brain Prevention

Split-brain — where two nodes simultaneously believe they are the primary — is the most dangerous failure mode in a PostgreSQL HA cluster. Patroni prevents this by design: [Patroni's documentation states](https://patroni.readthedocs.io/en/latest/replication_modes.html) that the consensus store ensures "only one node can hold the leadership lease, making split brain not possible." Witness nodes in repmgr configurations reduce but do not eliminate the risk.

A minimum production HA topology requires: 1 primary, 1 or 2 standbys, 1 witness node or distributed consensus cluster (3 etcd nodes minimum), and a load balancer or virtual IP for client routing.

---

## 3. Backup and Recovery

### 3.1 Backup Strategy Components

A production PostgreSQL backup strategy must combine three mechanisms:

1. **pg_basebackup**: Creates a consistent physical copy of the entire data directory. [Official PostgreSQL documentation](https://www.postgresql.org/docs/current/continuous-archiving.html) states this is "the easiest way to perform a base backup." Suitable for full restores; does not support PITR on its own.

2. **WAL Archiving**: Continuously copies completed WAL segment files to an archive location (NFS, S3-compatible storage, or dedicated backup server). Requires `wal_level = replica`, `archive_mode = on`, and a working `archive_command` in `postgresql.conf`. [pgedge's PITR documentation](https://www.pgedge.com/blog/point-in-time-recovery-pitr-in-postgresql) confirms that WAL archiving combined with a base backup is the foundation of PITR.

3. **Point-in-Time Recovery (PITR)**: Restores a base backup and replays archived WAL up to a specified target time, transaction ID, or LSN. Achieves RPOs measured in minutes (limited by `archive_timeout`, which controls how frequently WAL files are closed and archived even under low load).

### 3.2 RTO and RPO Targets

For a typical on-premises PostgreSQL deployment:

- **RPO**: Determined by WAL archiving frequency. Setting `archive_timeout = 5min` yields a worst-case RPO of 5 minutes for low-traffic periods. During high write volumes, WAL segments fill and archive continuously, approaching near-zero RPO. [CloudNativePG documentation](https://cloudnative-pg.io/documentation/1.19/backup_recovery/) documents this `archive_timeout` behavior explicitly.
- **RTO**: For a base backup restore + WAL replay, RTO depends on database size and the number of WAL files to replay. A 100 GB database with 6 hours of WAL replay may require 30–90 minutes. Failover to a pre-built streaming standby (via Patroni) achieves RTO measured in seconds to minutes.

### 3.3 Backup Testing

[UNVERIFIED] Industry practice recommends testing full PITR restores monthly and after every major schema change. This estimate is based on standard database operations practice, but no specific 2025 survey data was located quantifying testing frequency at production organizations. The operational burden of backup testing — spinning up a restore target, running the recovery, validating row counts and application functionality — is typically 4–8 hours per test cycle.

### 3.4 Backup Tools for On-Premises

Beyond native tools, **pgBackRest** is widely used in production for its parallelized compression, incremental backups, and built-in WAL archiving management. [Stormatics' physical backup guide](https://stormatics.tech/blogs/postgresql-physical-backups-using-pg_basebackup-a-comprehensive-guide) provides a comprehensive walkthrough of pg_basebackup for production environments.

---

## 4. Scaling

### 4.1 Read Replicas

Read replicas are streaming standbys configured to accept read-only queries. This horizontally distributes SELECT-heavy workloads but requires the application to maintain separate read and write connection strings. [The Meerako 2025 scaling guide](https://www.meerako.com/blogs/postgresql-database-scaling-strategies-sharding-replication) documents that read replicas are the first scaling lever for read-heavy workloads.

Replication lag is the primary operational risk: a replica may serve stale data if it falls behind the primary. This must be monitored continuously via `pg_stat_replication`.

### 4.2 Vertical Scaling

Vertical scaling of an on-premises PostgreSQL instance requires physical downtime: memory and CPU upgrades on bare-metal hardware require a server shutdown. Even in a VM environment, live memory hot-add is not universally supported. A planned vertical scaling event in an HA cluster typically involves:

1. Promote a replica to primary (brief failover)
2. Upgrade the old primary hardware
3. Re-join as a replica
4. Optional: fail back

This is a multi-hour maintenance window with non-trivial risk.

### 4.3 Horizontal Sharding with Citus

For workloads that exceed the capacity of a single PostgreSQL instance, **Citus** provides distributed sharding as a PostgreSQL extension. [The Citus GitHub repository](https://github.com/citusdata/citus) describes it as extending "PostgreSQL with distributed tables that are sharded across a cluster of PostgreSQL nodes to combine their CPU, memory, storage and I/O capacity." Schema-based sharding (Citus 12+) places all tables within a schema on the same node, enabling single-node performance for schema-isolated tenants.

However, [ScaleGrid's Citus production guide](https://scalegrid.io/blog/citus-for-postgresql-how-to-scale-your-database/) notes that "complex joins across shards may result in degraded performance unless data is co-located or replicated, and distributed transactions require additional coordination." Sharding adds significant application design complexity and should be treated as a last resort after vertical scaling and read replicas are exhausted.

---

## 5. Patching and Upgrades

### 5.1 Minor Version Patches

PostgreSQL minor version updates (e.g., 16.3 → 16.4) are binary-compatible and typically require only a restart. In an HA cluster with Patroni, minor patching can be performed with rolling restarts — one node at a time — achieving near-zero downtime.

[PostgreSQL's versioning policy](https://www.postgresql.org/support/versioning/) states that minor releases contain bug fixes and security patches only; they never change the on-disk data format and are always safe to apply.

### 5.2 Major Version Upgrades

Major version upgrades (e.g., PostgreSQL 15 → 17) are the most operationally demanding maintenance event for self-hosted deployments. Three primary methods exist:

1. **pg_dump / pg_restore**: Logical export and re-import. Safest for multi-version jumps and cross-platform migrations. Requires a full outage window proportional to database size — multi-hour for large databases.

2. **pg_upgrade**: In-place upgrade that rewrites system catalogs while reusing user data files. [Official pg_upgrade documentation](https://www.postgresql.org/docs/current/pgupgrade.html) notes that upgrades can be performed "in minutes, particularly with --link mode" which avoids copying data files. However, this is still an **offline operation**: [Microsoft's Azure documentation](https://learn.microsoft.com/en-us/azure/postgresql/configure-maintain/concepts-major-version-upgrade) confirms that "an in-place major version upgrade is an offline operation, meaning the server will be unavailable during the process."

3. **Logical Replication to a New Major Version**: The lowest-downtime approach. A new-version standby is built using logical replication (which [supports cross-version replication](https://www.postgresql.org/docs/current/upgrading.html)). Once caught up, a brief cutover completes the upgrade. This requires the most DBA expertise and planning. [pgedge's zero-downtime upgrade guide](https://www.pgedge.com/blog/always-online-or-bust-zero-downtime-major-version-postgres-upgrades) documents this approach in detail.

**Extension compatibility** is an additional risk: every installed extension must be compatible with the target major version before the upgrade can proceed. A testing matrix covering all application workloads against the new version is mandatory.

---

## 6. Monitoring

A production on-premises PostgreSQL instance requires monitoring across at least six dimensions:

| Signal | Source | Tool/Query | Alert Threshold |
|---|---|---|---|
| Query performance | `pg_stat_statements` | pganalyze, Datadog | P99 latency > baseline |
| Active connections | `pg_stat_activity` | Prometheus + postgres_exporter | > 80% of `max_connections` |
| Replication lag | `pg_stat_replication` | Grafana dashboard | > 30 seconds |
| Disk space | OS + `pg_database_size()` | Prometheus | > 80% full |
| Cache hit ratio | `pg_statio_user_tables` | Custom query | < 95% |
| Autovacuum health | `pg_stat_user_tables` | pganalyze | Bloat > threshold |

[Uptrace's 2025 monitoring tools comparison](https://uptrace.dev/tools/postgresql-monitoring-tools) identifies the core signals a PostgreSQL monitoring stack must capture: "slow/normalized queries, wait events/locks, pg_stat_statements, replication lag, WAL/checkpoints, autovacuum runs, cache hit ratio, temp files, and connection saturation."

[CYBERTEC's replication monitoring guide](https://www.cybertec-postgresql.com/en/monitoring-replication-pg_stat_replication/) documents that `pg_stat_replication` provides "the delay in bytes or seconds" and measures "the time taken for recent WAL to be written, flushed and replayed."

Monitoring infrastructure must be deployed independently of the database cluster it monitors — a common operational failure is monitoring that depends on the database being up, creating blind spots precisely during incidents. Prometheus with `postgres_exporter` and Grafana is the most common open-source monitoring stack. Commercial options include pganalyze, Datadog, and Uptrace.

---

## 7. Security

### 7.1 Authentication

PostgreSQL uses a client authentication file (`pg_hba.conf`) to control which users can connect from which hosts using which authentication methods. Production deployments should enforce:

- `scram-sha-256` authentication for all application connections (the default as of PostgreSQL 14)
- No use of `trust` authentication for remote connections
- Role-based access following the principle of least privilege

[EDB's security hardening guide](https://www.enterprisedb.com/blog/how-to-secure-postgresql-security-hardening-best-practices-checklist-tips-encryption-authentication-vulnerabilities) recommends configuring "PostgreSQL server to require TLS 1.3 for all connections to ensure that only the latest and most secure version of the protocol is used."

### 7.2 Encryption in Transit and at Rest

- **In transit**: PostgreSQL natively supports SSL/TLS for client-server communication. Mutual TLS (client certificates) is available for applications requiring bidirectional identity verification.
- **At rest**: PostgreSQL does not natively encrypt data files. Options include:
  - **OS-level**: Full-disk encryption (LUKS on Linux) or filesystem-level encryption
  - **Column-level**: The `pgcrypto` extension enables encryption of individual fields, described by [EDB's encryption guide](https://www.enterprisedb.com/postgresql-best-practices-encryption-monitoring) as "allowing for the encryption of individual fields, entire tables, or data transactions."

### 7.3 Row-Level Security

Row-Level Security (RLS) allows database administrators to define policies restricting which rows users can view or modify. [Permit.io's RLS implementation guide](https://www.permit.io/blog/postgres-rls-implementation-guide) describes RLS as "extremely useful for multi-tenant applications or environments where the principle of least privilege is critical." RLS policies are applied automatically at query time, providing transparent enforcement that cannot be bypassed at the application layer.

### 7.4 Audit Logging with pgAudit

The `pgAudit` extension provides session and object-level audit logging required for compliance with HIPAA, GDPR, SOX, and PCI DSS. [pgAudit's official documentation](https://www.pgaudit.org/) states its goal is "to provide PostgreSQL users with capability to produce audit logs often required to comply with government, financial, or ISO certifications." pgAudit automatically redacts sensitive values like passwords from logs.

[Bytebase's audit logging guide (2025)](https://www.bytebase.com/blog/postgres-audit-logging/) notes that logging all statements can be verbose and impact performance; most compliance workloads should configure `WRITE + DDL` logging rather than `ALL` to balance coverage and overhead. Audit logs should be shipped to an external SIEM (Splunk, Elastic, Datadog) — storing them on the database server creates a conflict-of-interest and creates risk if the server is compromised.

---

## 8. Operational Staffing

### 8.1 DBA Skill Requirements

A production on-premises PostgreSQL deployment requires a DBA (or team) with competency across:

- Linux systems administration (kernel tuning, storage configuration, network)
- PostgreSQL internals (WAL, MVCC, autovacuum, query planner)
- High-availability tooling (Patroni or repmgr, etcd/Consul)
- Backup and recovery operations (pgBackRest, pg_basebackup, PITR)
- Security hardening (pg_hba.conf, SSL, pgAudit, RLS)
- Monitoring and alerting (Prometheus, Grafana, postgres_exporter)
- Upgrade planning and execution (pg_upgrade, logical replication)

This skill set is not uniformly available in the market. [ZipRecruiter salary data (2025)](https://www.ziprecruiter.com/Jobs/Postgresql-Dba) shows PostgreSQL DBA market rates of $48–$76/hour in the US, reflecting the specialized nature of the role.

### 8.2 FTE Estimates by Deployment Model

**Assumptions:** Mid-size deployment; 2–3 node HA cluster; 500 GB–2 TB database; serving 50 enterprise customers; business-hours primary coverage plus on-call rotation.

| Capability Domain | On-Premises | Managed K8s (Operator) | Cloud-Native (RDS/Azure SQL) |
|---|---|---|---|
| Initial setup & tuning | Difficulty: 4/5 | Difficulty: 3/5 | Difficulty: 1/5 |
| | Full OS + DB config | Operator config, limited OS access | Console/API driven |
| | Linux + PostgreSQL expertise | Helm + CloudNativePG | Cloud console |
| | Est. FTE (one-time): 0.5 | Est. FTE (one-time): 0.25 | Est. FTE (one-time): 0.1 |
| High availability | Difficulty: 5/5 | Difficulty: 3/5 | Difficulty: 1/5 |
| | Patroni + etcd cluster design | Operator-managed failover | Automatic Multi-AZ |
| | HA expertise, consensus systems | K8s + operator knowledge | No DBA work required |
| | Est. FTE: 0.5–1.0 ongoing | Est. FTE: 0.2–0.4 ongoing | Est. FTE: 0.0–0.1 |
| Backup & recovery | Difficulty: 4/5 | Difficulty: 3/5 | Difficulty: 1/5 |
| | pgBackRest, WAL archiving, PITR | Operator + external storage | Automated; PITR configurable |
| | Backup testing mandatory | Partial automation | Provider SLA |
| | Est. FTE: 0.25–0.5 | Est. FTE: 0.1–0.2 | Est. FTE: 0.05–0.1 |
| Patching & upgrades | Difficulty: 4/5 | Difficulty: 3/5 | Difficulty: 2/5 |
| | Manual pg_upgrade + testing | Operator-assisted, still needs testing | Provider-managed minor; major needs window |
| | Full version matrix testing | Reduced but required | Simplified; some config still required |
| | Est. FTE: 0.25 | Est. FTE: 0.15 | Est. FTE: 0.1 |
| Monitoring | Difficulty: 3/5 | Difficulty: 3/5 | Difficulty: 2/5 |
| | Build + maintain full stack | Build + maintain, cloud visibility | CloudWatch/Azure Monitor built-in |
| | Prometheus + Grafana + exporters | Same tools, cloud integrations | Native dashboards, custom metrics extra |
| | Est. FTE: 0.25 | Est. FTE: 0.2 | Est. FTE: 0.1 |
| Security hardening | Difficulty: 4/5 | Difficulty: 3/5 | Difficulty: 2/5 |
| | Full control, full responsibility | Partial OS access | Provider handles infra; config still manual |
| | pgAudit, RLS, SSL, disk crypto | Same DB-level, limited OS | pgAudit available; RLS/SSL still manual |
| | Est. FTE: 0.25 | Est. FTE: 0.15 | Est. FTE: 0.1 |
| **Total ongoing FTE** | **1.5–3.0 FTE** | **0.85–1.25 FTE** | **0.25–0.5 FTE** |
| **On-call burden** | High: 24/7 pager | Moderate: 24/7 pager | Low: Provider primary on-call |

### 8.3 Incident Response Burden

Database emergencies — disk full, replication split-brain, corruption, runaway queries — require immediate, expert response at any hour. For on-premises deployments, the ISV or customer must staff or contract for 24/7 DBA on-call coverage. [Rapydo's 2025 RDS vs. self-managed comparison](https://www.rapydo.io/blog/aws-rds-vs-self-managed-databases-a-comprehensive-comparison) characterizes this as requiring "significant investment in terms of hardware and software, as well as ongoing operational costs and hiring skilled professionals."

The total cost of ownership for on-premises includes not only the DBA salary but the on-call premium, which typically adds 20–30% to compensation for staff carrying pagers. For a small ISV, achieving 24/7 DBA coverage without burnout requires a minimum of two DBA-capable staff — meaning a practical floor of 2.0 FTE even for a small database deployment.

---

## 9. Comparison with Managed Services

The table below summarizes the operational profile difference between on-premises self-hosting and cloud managed services for a representative mid-size PostgreSQL deployment.

| Capability | On-Premises | Cloud-Native (RDS / Azure SQL / Cloud SQL) |
|---|---|---|
| Setup time | Days to weeks (OS, cluster, HA) | Hours (console/API) |
| Failover automation | Manual or Patroni (requires separate etcd cluster) | Automatic Multi-AZ (seconds) |
| Backup | Manual config, test, and storage management | Automated; PITR configurable via console |
| Major upgrades | High risk, requires DBA-led testing and downtime | Provider-managed with maintenance windows |
| Monitoring | Build and operate full stack | Native cloud dashboards |
| Security patching (OS) | ISV/customer responsibility | Provider responsibility |
| Encryption at rest | OS-level or pgcrypto | Provider-managed, FIPS-certified options |
| Horizontal sharding | Complex (Citus extension) | Managed sharding (Aurora Limitless, Citus on Azure) |
| Max connections | Must pool manually (PgBouncer) | Built-in pooler on most managed services |
| Total DBA FTE | 1.5–3.0 | 0.25–0.5 |

Sources: [rapydo.io RDS vs. Self-Managed 2025](https://www.rapydo.io/blog/aws-rds-vs-self-managed-databases-a-comprehensive-comparison); [Medium: RDS vs. Self-Managed Complete Guide 2025](https://medium.com/appfoster/aws-rds-vs-self-managed-databases-in-2025-complete-guide-for-developers-and-architects-3199cb0ed57d); [Percona Patroni enterprise HA](https://www.percona.com/blog/patroni-the-key-postgresql-component-for-enterprise-high-availability/)

---

## Key Takeaways

- **On-premises PostgreSQL demands deep, multi-domain expertise across at least seven operational domains** — OS tuning, connection pooling, HA orchestration, backup/recovery, upgrades, monitoring, and security — each requiring dedicated DBA skill and ongoing attention. Deficiency in any single domain represents a material production risk.

- **Staffing requirements are 3–6x higher for on-premises versus cloud-native managed services.** Estimated DBA FTE for a mid-size production PostgreSQL cluster on-premises is 1.5–3.0 FTE (including 24/7 on-call coverage), compared to 0.25–0.5 FTE for an equivalent managed-service deployment on RDS, Azure SQL, or Cloud SQL.

- **Major version upgrades are the highest-risk maintenance event in the on-premises lifecycle.** PostgreSQL releases a new major version annually (supported for 5 years), and major upgrades require a planned outage window, extension compatibility testing, and either a pg_upgrade execution or a logical replication cutover. Skipping upgrades accumulates technical debt and eventually forces a high-risk multi-version jump.

- **High availability is solvable but not simple.** Patroni eliminates split-brain risk via consensus-based leader election, but requires a correctly operated etcd/Consul cluster as a dependency. An incorrect HA configuration is more dangerous than no HA, as it may create false confidence. A minimum resilient topology requires five nodes: one primary, two standbys, and three etcd nodes.

- **The on-premises model is justified only for specific regulatory or technical constraints.** Organizations with data-residency mandates, air-gapped environments, or highly customized PostgreSQL configurations (extensions, kernel patches, specialized storage) that managed services cannot accommodate have legitimate reasons to self-host. For ISVs without these constraints, the managed-service premium almost always delivers net positive ROI through reduced DBA staffing, reduced incident risk, and faster time-to-production.

---

## Related — Out of Scope

- **F42 (NoSQL databases)**: MongoDB, Redis, Cassandra on-premises operational profiles — similar operational burden patterns apply but with different tooling.
- **F43 (Backup infrastructure)**: The network storage, tape libraries, and off-site backup systems that support WAL archiving and pg_basebackup targets.
- **F1 (Application data patterns)**: ORM design, query optimization at the application layer, multi-tenancy schema patterns.
- **Managed Kubernetes database operators** (CloudNativePG, Zalando Postgres Operator): These bridge the on-premises and managed K8s models and represent a distinct sub-category not fully covered here.

---

## Sources

1. [PostgreSQL Performance Tuning Best Practices 2025 — Mydbops](https://www.mydbops.com/blog/postgresql-parameter-tuning-best-practices)
2. [PostgreSQL Performance Tuning: Complete Guide — dbadataverse.com 2025](https://dbadataverse.com/tech/postgresql/2025/02/postgresql-performance-tuning-complete-guide)
3. [Tune Linux Kernel Parameters for PostgreSQL — Percona](https://www.percona.com/blog/tune-linux-kernel-parameters-for-postgresql-optimization/)
4. [Configuring Linux Huge Pages for PostgreSQL — Stormatics 2025](https://stormatics.tech/blogs/configuring-linux-huge-pages-for-postgresql)
5. [Linux Swappiness and PostgreSQL Performance Optimization — Medium, Dec 2025](https://ozwizard.medium.com/linux-swappiness-and-postgresql-performance-optimization-ea41c60b6b95)
6. [Complete Guide to Fixing PostgreSQL Performance with PgBouncer — Opstree 2025](https://opstree.com/blog/2025/10/07/postgresql-performance-with-pgbouncer/)
7. [Analyzing the Limits of Connection Scalability in Postgres — Microsoft Community Hub](https://techcommunity.microsoft.com/blog/adforpostgresql/analyzing-the-limits-of-connection-scalability-in-postgres/1757266)
8. [Patroni — The Key PostgreSQL Component for Enterprise High Availability — Percona](https://www.percona.com/blog/patroni-the-key-postgresql-component-for-enterprise-high-availability/)
9. [Patroni Replication Modes Documentation](https://patroni.readthedocs.io/en/latest/replication_modes.html)
10. [Split-Brain in PostgreSQL Clusters — Stormatics](https://stormatics.tech/blogs/split-brain-in-postgresql-clusters-causes-prevention-and-resolution)
11. [Using a Witness Server — repmgr Official Documentation](https://www.repmgr.org/docs/current/repmgrd-witness-server.html)
12. [PostgreSQL Continuous Archiving and PITR — Official Documentation](https://www.postgresql.org/docs/current/continuous-archiving.html)
13. [Physical Backups Using pg_basebackup — Stormatics](https://stormatics.tech/blogs/postgresql-physical-backups-using-pg_basebackup-a-comprehensive-guide)
14. [Point-In-Time Recovery (PITR) in PostgreSQL — pgedge](https://www.pgedge.com/blog/point-in-time-recovery-pitr-in-postgresql)
15. [Backup and Recovery — CloudNativePG Documentation](https://cloudnative-pg.io/documentation/1.19/backup_recovery/)
16. [Zero Downtime Major Version Postgres Upgrades — pgedge](https://www.pgedge.com/blog/always-online-or-bust-zero-downtime-major-version-postgres-upgrades)
17. [PostgreSQL: pg_upgrade Official Documentation](https://www.postgresql.org/docs/current/pgupgrade.html)
18. [PostgreSQL: Upgrading a Cluster — Official Documentation](https://www.postgresql.org/docs/current/upgrading.html)
19. [Major Version Upgrades — Azure Database for PostgreSQL](https://learn.microsoft.com/en-us/azure/postgresql/configure-maintain/concepts-major-version-upgrade)
20. [PostgreSQL Versioning Policy](https://www.postgresql.org/support/versioning/)
21. [Top 10 PostgreSQL Monitoring Tools 2025 — Uptrace](https://uptrace.dev/tools/postgresql-monitoring-tools)
22. [Monitoring Replication: pg_stat_replication — CYBERTEC](https://www.cybertec-postgresql.com/en/monitoring-replication-pg_stat_replication/)
23. [How to Monitor PostgreSQL Performance — OneUptime 2026](https://oneuptime.com/blog/post/2026-02-02-postgresql-performance-monitoring/view)
24. [PostgreSQL Security Hardening Best Practices — EDB](https://www.enterprisedb.com/blog/how-to-secure-postgresql-security-hardening-best-practices-checklist-tips-encryption-authentication-vulnerabilities)
25. [PostgreSQL Data Security: Encryption and Monitoring — EDB](https://www.enterprisedb.com/postgresql-best-practices-encryption-monitoring)
26. [Postgres RLS Implementation Guide — Permit.io](https://www.permit.io/blog/postgres-rls-implementation-guide)
27. [pgAudit Official Documentation](https://www.pgaudit.org/)
28. [Postgres Audit Logging Guide — Bytebase 2025](https://www.bytebase.com/blog/postgres-audit-logging/)
29. [Best Practices for Securing PostgreSQL in Hybrid Environments — Severalnines](https://severalnines.com/blog/best-practices-for-securing-postgresql-in-hybrid-environments/)
30. [Citus for PostgreSQL: How to Scale Your Database — ScaleGrid](https://scalegrid.io/blog/citus-for-postgresql-how-to-scale-your-database/)
31. [Citus GitHub Repository](https://github.com/citusdata/citus)
32. [Scaling PostgreSQL: Read Replicas, Sharding, and Beyond — Meerako](https://www.meerako.com/blogs/postgresql-database-scaling-strategies-sharding-replication)
33. [AWS RDS vs. Self-Managed Databases: A Comprehensive Comparison — Rapydo 2025](https://www.rapydo.io/blog/aws-rds-vs-self-managed-databases-a-comprehensive-comparison)
34. [AWS RDS vs. Self-Managed Databases in 2025 — Medium / Appfoster](https://medium.com/appfoster/aws-rds-vs-self-managed-databases-in-2025-complete-guide-for-developers-and-architects-3199cb0ed57d)
35. [PostgreSQL Hosting: Complete Production Deployment Guide 2025 — PloyCloud](https://ploy.cloud/blog/postgresql-hosting-guide-2025/)
36. [PostgreSQL DBA Roles and Responsibilities — Koenig Solutions](https://www.koenig-solutions.com/blog/postgresql-dba-roles-and-responsibilities-skills-jobs-description-salary)
37. [PostgreSQL DBA Salary Data 2025 — ZipRecruiter](https://www.ziprecruiter.com/Jobs/Postgresql-Dba)
38. [How to Recover Data with Point-in-Time Recovery — OneUptime, Jan 2026](https://oneuptime.com/blog/post/2026-01-25-point-in-time-recovery-postgresql/view)
39. [pgBouncer for PostgreSQL: How Connection Pooling Solves Enterprise Slowdowns — Percona](https://www.percona.com/blog/pgbouncer-for-postgresql-how-connection-pooling-solves-enterprise-slowdowns/)
40. [Tuning max_connections in PostgreSQL — CYBERTEC](https://www.cybertec-postgresql.com/en/tuning-max_connections-in-postgresql/)
