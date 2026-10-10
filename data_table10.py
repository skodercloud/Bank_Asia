# -*- coding: utf-8 -*-
"""
data_table10.py
Technical Specification Details (90 rows) - Responses and Remarks
"""

T10_SPECS = {
    2: (
        "Complied",
        "Skoder LMS Enterprise is engineered on a modern N-tier, modular microservices-ready architecture using high-performance PHP/Laravel framework and PostgreSQL/Oracle enterprise database. Comprehensive system documentation, API gateway specs, HA/DR failover topology, and data flow diagrams are included in the Technical Proposal."
    ),
    3: (
        "Complied",
        "Fully complied. Sized for Bank Asia's on-premises enterprise DC & DR deployment utilizing Dell PowerEdge R760 Rack Servers, VMware vSphere 8, and RHEL 9. Detailed server BoQ and architecture attached in Table 16 and separate Hardware Quotation."
    ),
    5: (
        "Complied",
        "Complied. Skoder Technologies operates a dedicated Level 1/2/3 technical helpdesk from 09:00 AM to 08:00 PM Sunday through Thursday, with 24/7/365 emergency on-call and remote incident resolution via ticketing portal, email, and phone."
    ),
    6: (
        "Complied",
        "Complied. The platform includes an advanced dynamic query builder allowing custom search filters across case types, borrower TIN/NID, court stages, outstanding balances, and hearing dates with export to Excel/PDF."
    ),
    7: (
        "Complied",
        "Complied. Includes comprehensive web-based management console, Prometheus/Grafana health metrics endpoints, APM monitoring, and secure SSL VPN administrative access."
    ),
    8: (
        "Complied",
        "Complied. 100% browser-independent responsive web interface built on HTML5, CSS3, and modern JavaScript, fully supported on latest Google Chrome, Microsoft Edge, Mozilla Firefox, and Apple Safari without plugins."
    ),
    9: (
        "Complied",
        "Complied. Supports bilingual English and Bengali (Unicode UTF-8 / Nikosh / SolaimanLipi) for legal notices, court cause lists, case summaries, and statutory reports."
    ),
    10: (
        "Complied",
        "Complied. Automated test execution framework supported using simulated API payloads and automated regression test scripts for UAT verification."
    ),
    11: (
        "Complied",
        "Complied. Perpetual enterprise bank-wide license covers Primary Data Center (DC), Near DR, and Far DR active-passive deployment without additional per-core or per-seat licensing penalties."
    ),
    12: (
        "Complied",
        "Complied. Dynamic Master Parameter Setup module allows authorized administrators to configure court codes, case classifications, expense heads, branch codes, and legal acts."
    ),
    13: (
        "Complied",
        "Complied. Bank Asia PLC branding, official logo, and branch headers are dynamically rendered across application headers, printable legal notices, Jari statements, and reports."
    ),
    14: (
        "Complied",
        "Complied. Comprehensive administrative console provided for schema configurations, workflow rules, audit log review, role management, and routine operational maintenance."
    ),
    15: (
        "Complied",
        "Complied. Enforces TLS 1.3 / HTTPS encryption across all web interfaces and API endpoints with strong cipher suites (HSTS, forward secrecy)."
    ),
    16: (
        "Complied",
        "Complied. Modular architecture allows rapid local customization of validation rules, form fields, court stages, and screen layouts based on Bank Asia's specific legal workflows."
    ),
    17: (
        "Complied",
        "Complied. Designed to operate within Bank Asia's secure internal network zone / dedicated DMZ/VLAN with mutual TLS (mTLS) and IP whitelisting for CBS integration."
    ),
    18: (
        "Complied",
        "Complied. Supports automated End-of-Day (EOD) cron scheduling, ETL batch synchronisation, and real-time delta fetching for classified loan balances and customer details."
    ),
    19: (
        "Complied",
        "Complied. Features robust RESTful and SOAP API gateways with JSON/XML payloads, JWT token authentication, and rate limiting for bidirectional CBS/peripheral system integration."
    ),
    20: (
        "Complied",
        "Complied. Strong AES-256 column-level encryption for confidential PII and financial records at rest; TLS 1.3 encryption for all data in transit across networks."
    ),
    22: (
        "Complied",
        "Complied. Built upon open, standard architectural patterns (REST APIs, microservices, OpenAPI/Swagger 3.0 specs) ensuring seamless integration with Bank Asia CBS and other banking modules."
    ),
    23: (
        "Complied",
        "Complied. Native support for enterprise Single Sign-On (SSO) via Active Directory (LDAP / Kerberos / SAML 2.0 / OAuth2 / OpenID Connect) and open banking API integration."
    ),
    24: (
        "Complied",
        "Complied. Extensible modular schema design supports dynamic custom attributes and backwards-compatible API versioning to absorb CBS upgrades without downtime."
    ),
    25: (
        "Complied",
        "Complied. Native integration with Bank Asia's internal SMS Gateway (SMPP / HTTP REST) and enterprise SMTP / Microsoft Exchange email servers for automated alert delivery."
    ),
    26: (
        "Complied",
        "Complied. Notification engine handles both SMS and email queues with failure retry mechanisms and delivery audit logging."
    ),
    27: (
        "Complied",
        "Complied. Automated background scheduler dispatches upcoming court hearing reminders, legal notice deadlines, and warrant execution alerts via SMS and email on configurable intervals."
    ),
    28: (
        "Complied",
        "Complied. Provides read-replica database support and automated daily ETL pipelines / data staging views for Bank Asia's Central Data Warehouse / MIS reporting."
    ),
    29: (
        "Complied",
        "Complied. Comprehensive integration toolkit including REST/JSON, SOAP/XML, automated SFTP batch file exchange, and OpenAPI/Swagger documentation."
    ),
    31: (
        "Complied",
        "Complied. Case document repository maintains immutable version control, timestamped revision history, and one-click rollback/retrieval of historical file versions."
    ),
    32: (
        "Complied",
        "Complied. Automated real-time notifications dispatched to assigned case handlers, desk officials, and legal supervisors whenever case status or documents are modified."
    ),
    33: (
        "Complied",
        "Complied. Comprehensive data migration strategy, automated Excel/CSV ETL ingest utilities, data cleansing scripts, and validation audits ensure 100% legacy litigation data migration."
    ),
    34: (
        "Complied",
        "Complied. Pre-migration gap analysis, automated staging tables with validation rules, and manual reconciliation workflows handle unmapped or missing legacy attributes."
    ),
    36: (
        "Complied",
        "Complied. Flexible workflow engine allows concurrent parallel tracking of civil suits (Artha Rin), criminal proceedings (NI Act 138), auction notices, and writ petitions for the same borrower."
    ),
    38: (
        "Complied",
        "Complied. Parameterized business rules engine supports configurable escalation rules, mandatory legal notice statutory wait periods (e.g. 30 days under NI Act), and approval limits."
    ),
    40: (
        "Complied",
        "Complied. Multi-tier permission matrix enforces granular restrictions per user role, branch, and division for drafting, maker approval, checker authorization, viewing, and exporting reports."
    ),
    42: (
        "Complied",
        "Complied. Detailed enterprise deployment architecture diagram depicting Web Server, App Server, DB Cluster, CBS Gateway, SMS/Email Server, and Active Directory enclosed in Technical Proposal."
    ),
    43: (
        "Complied",
        "Complied. Proposed 100% on-premises deployment adhering to Bangladesh Bank ICT Guidelines for full data sovereignty across Bank Asia Primary DC and DR sites."
    ),
    44: (
        "Complied",
        "Complied. Three distinct, isolated environments (Development/Test, UAT/Staging, and Production) will be provisioned, configured, and maintained during rollout."
    ),
    46: (
        "Complied",
        "Complied. 100% perpetual bank-wide enterprise license with unlimited users, branches, and cases without recurring subscription or license expiry locks."
    ),
    47: (
        "Complied",
        "Complied. Granular RBAC supporting administrative, legal officer, branch maker, branch checker, panel lawyer, and executive management roles with immutable audit logging."
    ),
    48: (
        "Complied",
        "Complied. Passwords hashed using industry-standard bcrypt / Argon2id algorithms with cryptographic salt, ensuring zero plain-text storage."
    ),
    49: (
        "Complied",
        "Complied. Database stores one-way salted cryptographic hashes adhering to Bangladesh Bank Information Security Standards."
    ),
    50: (
        "Complied",
        "Complied. Configurable password complexity policy (minimum length, uppercase, lowercase, numbers, special characters, expiration intervals, password history prevention)."
    ),
    51: (
        "Complied",
        "Complied. Seamless Single Sign-On (SSO) supported via Active Directory LDAP / SAML 2.0 / Kerberos integration."
    ),
    52: (
        "Complied",
        "Complied. Supports assigning multiple complementary roles to a single user profile while preserving strict Maker-Checker segregation of duties."
    ),
    53: (
        "Complied",
        "Complied. System administrators can reassign user roles, transfer branch assignments, and adjust approval limits instantly with full audit logging."
    ),
    54: (
        "Complied",
        "Complied. Strict Maker-Checker access matrix defined and administered through graphical administrative interface."
    ),
    55: (
        "Complied",
        "Complied. Menu items, form actions (Create, Edit, Delete, Authorize), and data access scopes are dynamically restricted per assigned role."
    ),
    56: (
        "Complied",
        "Complied. Fully integrated with Microsoft Active Directory / Azure AD via secure LDAP/LDAPS for centralized authentication and automated user provisioning."
    ),
    57: (
        "Complied",
        "Complied. Immutable audit trail captures user ID, client IP, timestamp, action type, old values, and new values for every create, update, delete, and view event."
    ),
    58: (
        "Complied",
        "Complied. Database-level AES-256 transparent data encryption (TDE) for data at rest and TLS 1.3 encryption for data in transit across all endpoints."
    ),
    59: (
        "Complied",
        "Complied. Supports hierarchical user group definitions (Legal Division, Special Asset Management, Branch Recovery, Panel Lawyers, Executive Management)."
    ),
    60: (
        "Complied",
        "Complied. Parameterized security rules enforce IP whitelisting per user/branch, allowed operating business hours, and authorized application server bindings."
    ),
    61: (
        "Complied",
        "Complied. Self-service password reset workflow with secure one-time password (OTP) verification sent to registered official mobile and email."
    ),
    62: (
        "Complied",
        "Complied. Configurable idle session timeout (default 15 minutes) automatically terminates inactive sessions and clears client-side tokens."
    ),
    63: (
        "Complied",
        "Complied. Administrators can immediately lock, deactivate, or reactivate user accounts with mandatory reason logging and audit trail recording."
    ),
    64: (
        "Complied",
        "Complied. Concurrent login prevention enforces single active session per user ID; subsequent logins invalidate existing sessions or are blocked."
    ),
    65: (
        "Complied",
        "Complied. Advanced ad-hoc reporting module allows authorized users to construct parameterized queries, filter audit trails, and export datasets to Excel/PDF."
    ),
    66: (
        "Complied",
        "Complied. Account automatically locks after parameterized number of consecutive failed attempts (default 5 attempts), requiring admin unlock or OTP verification."
    ),
    68: (
        "Complied",
        "Complied. Active-passive high-availability configuration supported with automated database replication to Bank Asia DR site and documented BCP/DR runbook."
    ),
    69: (
        "Complied",
        "Complied. Engineered for 99.9% uptime with automated health checks, seamless DR failover procedures, RPO < 5 minutes, and RTO < 15 minutes."
    ),
    70: (
        "Complied",
        "Complied. ACID-compliant transactional database engine with Write-Ahead Logging (WAL) ensures complete data integrity and automated crash recovery upon restart."
    ),
    71: (
        "Complied",
        "Complied. Fault-tolerant services with state recovery mechanisms ensure zero transaction loss and immediate resumption of operations upon system reboot."
    ),
    72: (
        "Complied",
        "Complied. Automated error tracking and anomaly detection engine alerts system administrators via email and dashboard notifications upon application exceptions."
    ),
    74: (
        "Complied",
        "Complied. Comprehensive enterprise RBAC model strictly enforces segregation of duties between Maker, Checker, Approver, and Viewer roles."
    ),
    75: (
        "Complied",
        "Complied. Pre-built connector for Microsoft Active Directory / LDAPS provides single-source credential verification and role mapping."
    ),
    76: (
        "Complied",
        "Complied. Passwords stored using salted SHA-256 / bcrypt cryptographic hashing; no plain-text passwords stored under any circumstances."
    ),
    77: (
        "Complied",
        "Complied. 100% browser-independent web client compatible with Windows, macOS, and Linux on Chrome, Edge, Firefox, and Safari; backend compatible with RHEL and PostgreSQL/Oracle."
    ),
    78: (
        "Complied",
        "Complied. Hardened application security layer featuring rate limiting, CSRF tokens, XSS sanitization, parameterized SQL queries, and secure session headers."
    ),
    79: (
        "Complied",
        "Complied. Built and audited according to OWASP Top 10 security standards; certified against SQL Injection, XSS, CSRF, broken access control, and insecure deserialization."
    ),
    80: (
        "Complied",
        "Complied. Automated batch execution log monitors CBS daily data ingestion, records record-level success/error counts, failure reasons, and issues alert notifications."
    ),
    81: (
        "Complied",
        "Complied. Global exception handling intercepts all errors, logging detailed stack traces internally while presenting secure, user-friendly messages to the end user."
    ),
    82: (
        "Complied",
        "Complied. Enforces TLS 1.3 / HTTPS encryption across all client-server interactions and inter-service communications with HSTS headers."
    ),
    83: (
        "Complied",
        "Complied. Audit log search console allows authorized security officers to filter logs by user ID, action type, date range, IP address, and module."
    ),
    84: (
        "Complied",
        "Complied. Built on open standards (REST, container-ready, standard SQL, POSIX OS) ensuring forward compatibility with upcoming hardware, OS, and DB upgrades."
    ),
    85: (
        "Complied",
        "Complied. Skoder Technologies provides rapid vulnerability remediation and hotfix patch releases within 24–48 hours upon issuance of critical security advisories."
    ),
    86: (
        "Complied",
        "Complied. Supports device fingerprinting, client certificate validation, and MAC/IP binding to restrict application access to authorized corporate terminals."
    ),
    87: (
        "Complied",
        "Complied. Skoder Technologies provides comprehensive Infrastructure & Application Security Hardening Guidelines covering OS, DB, Web Server, and network policies."
    ),
    88: (
        "Complied",
        "Complied. Compatible with enterprise SIEM solutions (Splunk, IBM QRadar, ELK), Web Application Firewalls (WAF), and endpoint protection systems."
    ),
    89: (
        "Complied",
        "Complied. 100% of underlying frameworks, libraries, and runtime dependencies are licensed under permissive enterprise open-source licenses, fully updated and free from known CVE vulnerabilities."
    ),
}
