# Data Dictionary

## `data/ai_opportunities.csv`

- `opportunity_id`: Stable opportunity identifier.
- `opportunity_name`: Product bet name.
- `service_line`: Marketplace service area.
- `country_stage`: Market context for rollout.
- `persona`: Primary internal user or accountable product partner.
- `user_problem`: Problem statement.
- `ai_capability`: AI capability being evaluated.
- `market_impact`: Synthetic 0 to 100 score for marketplace upside.
- `customer_impact`: Synthetic 0 to 100 score for customer or partner value.
- `ops_leverage`: Synthetic 0 to 100 score for operational leverage.
- `data_readiness`: Synthetic 0 to 100 score for instrumentation and usable signals.
- `ml_feasibility`: Synthetic 0 to 100 score for likely technical feasibility.
- `compliance_risk`: Synthetic 0 to 100 friction score.
- `rollout_effort`: Synthetic 0 to 100 friction score.
- `stakeholder_complexity`: Synthetic 0 to 100 friction score.
- `confidence`: Synthetic 0 to 100 confidence score.
- `priority_score`: Weighted roadmap score.
- `decision`: Readiness gate.

## `data/prd_cards.csv`

PRD content for each AI opportunity, including problem, hypothesis, MVP scope, KPI, guardrail, non-goal, stakeholders, acceptance criteria, and risks.

## `data/experiment_plan.csv`

Experiment design for each AI opportunity, including test type, primary metric, baseline, target lift, minimum sample, launch gate, risk watch, and next decision.

## `data/model_readiness.csv`

Readiness checks for each opportunity, including instrumentation, labels, latency fit, human review, and fairness review.
