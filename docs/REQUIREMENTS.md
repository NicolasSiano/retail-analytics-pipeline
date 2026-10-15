# Requirements

## Scope

Build an international freelance portfolio demonstrating a local batch ETL and BI workflow
with 100% synthetic retail data: approximately 10,000 sales across three branches and
12 consecutive months. Target Windows, Python 3.13, SQL Server 2025 Developer,
and the existing RetailAnalyticsDB database. Power BI integration is a later milestone.

## Functional requirements and future acceptance criteria

| ID | Requirement | Acceptance evidence |
| --- | --- | --- |
| FR01 | Generate reproducible CSV and XLSX inputs | Same seed and configuration produce equivalent records; three branches and all 12 months represented |
| FR02 | Extract data using Pandas | Both formats load with an explicit data contract |
| FR03 | Validate and clean records | Invalid rows carry reason codes; accepted/rejected counts reconcile with input |
| FR04 | Persist valid data in SQL Server | Transactional loads reconcile with accepted records |
| FR05 | Support safe reprocessing | Loading the same business keys twice does not increase sales count or totals |
| FR06 | Record runs and errors | Run ID, timestamps, status, counts, and sanitized errors are available |
| FR07 | Calculate commercial KPIs | Revenue, units, sales count, and average ticket match controlled fixtures |
| FR08 | Export CSV and XLSX reports | Exported totals match the analytical source |
| FR09 | Automate tests | Unit tests are isolated; SQL integration tests are explicitly selected |
| FR10 | Enable Power BI consumption | Documented model, relationships, measures, and refresh procedure |

## Quality requirements

- No real customer or employee information, credentials, or generated bulk data in Git.
- Explicit types, validation rules, monetary rounding, and transaction boundaries.
- Raw inputs remain immutable; rejected data is traceable to source and run.
- Configuration is separate from code. Use standard-library logging with secret redaction.
- Document installation, data contracts, limitations, and evidence of validation.
- Keep the first implementation local and batch-oriented; no cloud or orchestration platform required.

## Decisions deferred to Sprint 1

Confirm the calendar year, currency, timezone, sales grain (header versus line item),
business key, treatment of returns/discounts/taxes, and intentional invalid-data rate.
Define average ticket only after the transaction grain is agreed.
SQL Server instance name, authentication, driver availability, and connectivity must be
verified before the database sprint. Existing database contents must be inspected first.

## Sprint 0 acceptance

Repository scaffold, isolated environment, dependency metadata, ignore rules, English
documentation, mentoring rules, and successful offline smoke/quality checks.
No generator, ETL logic, SQL DDL, or database writes are included.
