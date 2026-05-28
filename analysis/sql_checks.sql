-- Review the top AI product opportunities.
select
  opportunity_id,
  opportunity_name,
  service_line,
  priority_score,
  decision
from opportunity_queue
order by priority_score desc;

-- Check that high-risk opportunities have launch guardrails.
select
  opportunity_id,
  opportunity_name,
  compliance_risk,
  guardrail,
  non_goal
from opportunity_queue
where compliance_risk >= 60;

-- Review model readiness flags.
select
  opportunity_id,
  check_name,
  score,
  status,
  owner
from model_readiness
where status in ('Yellow', 'Red')
order by opportunity_id, score;

-- Confirm each PRD card has a KPI, guardrail, non-goal, and stakeholders.
select
  opportunity_id,
  opportunity_name,
  north_star,
  guardrail,
  non_goal,
  stakeholders
from prd_cards
where north_star is not null
  and guardrail is not null
  and non_goal is not null
  and stakeholders is not null;
