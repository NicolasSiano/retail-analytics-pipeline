# Roadmap and learning exercises

Each sprint requires explicit learner approval before it starts.

| Sprint | Deliverable | Completion evidence |
| --- | --- | --- |
| 0 | Foundation and development environment | Smoke tests, lint, documented setup |
| 1 | Data contract and synthetic generator | Deterministic CSV/XLSX, three branches, 12 months, generator tests |
| 2 | Extraction, validation, cleaning | Invalid fixtures rejected with reasons; counts reconcile |
| 3 | SQL model and idempotent loading | Approved DDL, integration tests, rerun and rollback evidence |
| 4 | Orchestration and observability | Run audit, failure handling, end-to-end tests |
| 5 | Commercial KPIs and exports | Hand-calculated fixtures match CSV/XLSX totals |
| 6 | Power BI and portfolio presentation | Dashboard, architecture narrative, reproducible demo |

## Sprint 0 tasks and practice

| Task | Outcome | Practical exercise |
| --- | --- | --- |
| Inspect repository | Baseline and interpreter identified | Explain git status --short and python --version |
| Propose architecture | Module responsibilities documented | Trace one input file through the proposed stages |
| Create folders | Source, tests, data, SQL, reports, logs separated | Explain why raw and rejected data are separate |
| Create .venv | Project interpreter isolated | Print sys.executable and identify its location |
| Configure dependencies | Runtime/dev groups and tested snapshot | Explain why pytest is a dev dependency |
| Review ignores | Local/generated artifacts excluded | Use git check-ignore on a sample secret filename |
| Update README | English onboarding guide | Follow setup commands in a new PowerShell terminal |
| Add AGENTS.md | Learning and authorization rules persisted | Identify which action requires sprint approval |
| Write design documents | Scope, architecture, and roadmap explicit | Propose a measurable acceptance criterion for reruns |
| Verify foundation | Smoke checks and quality results recorded | Explain why imports do not prove database connectivity |

## Next task, only after approval

Agree on the sales data contract: grain, identifiers, year, currency, timestamp semantics,
discounts, returns, and invalid-record scenarios. Define examples and expected outcomes
before implementing the synthetic generator.
