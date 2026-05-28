# Methodology

## Scoring Model

The opportunity score is a transparent weighted model:

- Market impact: 18%
- Customer impact: 16%
- Operating leverage: 15%
- Data readiness: 15%
- Machine learning feasibility: 13%
- Confidence: 13%
- Compliance risk penalty: 3.5%
- Rollout effort penalty: 2.5%
- Stakeholder complexity penalty: 2.5%

The model adds a calibration constant so scores stay readable on a 0 to 100 product-prioritization scale. This is not a predictive model. It is a roadmap decision model for product discussion.

## Readiness Gates

- 82 or higher: Ready for MVP.
- 72 to 81.9: Pilot with guardrails.
- 62 to 71.9: Discovery first.
- Below 62: Defer.

## Synthetic Data Method

The service lines and marketplace actors are modeled on a common super app structure: riders, drivers, couriers, restaurants, stores, payment agents, enterprise customers, support teams, policy reviewers, and country operations teams.

The synthetic metrics use bounded 0 to 100 scales. Higher values mean stronger opportunity quality for impact, readiness, feasibility, and confidence. Higher values mean greater friction for compliance risk, rollout effort, and stakeholder complexity.

The experiment plan derives target lift from the final opportunity score and assigns the test type based on the operational nature of the opportunity: geo holdout, service cohort A/B, or staged rollout.
