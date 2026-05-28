import csv
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
OUTPUT_DIR = ROOT / "analysis" / "outputs"


def ensure_dirs():
    DATA_DIR.mkdir(exist_ok=True)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def score_opportunity(row):
    positive = (
        row["market_impact"] * 0.18
        + row["customer_impact"] * 0.16
        + row["ops_leverage"] * 0.15
        + row["data_readiness"] * 0.15
        + row["ml_feasibility"] * 0.13
        + row["confidence"] * 0.13
    )
    friction = (
        row["compliance_risk"] * 0.035
        + row["rollout_effort"] * 0.025
        + row["stakeholder_complexity"] * 0.025
    )
    return round(min(100, positive - friction + 9), 1)


def readiness_grade(score):
    if score >= 82:
        return "Ready for MVP"
    if score >= 72:
        return "Pilot with guardrails"
    if score >= 62:
        return "Discovery first"
    return "Defer"


def write_csv(path, rows, fieldnames):
    with path.open("w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def build_opportunities():
    rows = [
        {
            "opportunity_id": "AIOP-001",
            "opportunity_name": "Marketplace Balance Copilot",
            "service_line": "Ride hailing",
            "country_stage": "Core Maghreb cities",
            "persona": "Marketplace operations lead",
            "user_problem": "Dispatch teams react late when rider demand, driver supply, weather, and local events move at the same time.",
            "ai_capability": "Demand forecast, supply gap clustering, and human-approved incentive recommendations.",
            "market_impact": 91,
            "customer_impact": 87,
            "ops_leverage": 92,
            "data_readiness": 84,
            "ml_feasibility": 82,
            "compliance_risk": 45,
            "rollout_effort": 62,
            "stakeholder_complexity": 71,
            "confidence": 83,
            "hypothesis": "If operators receive city-zone supply gaps two hours earlier, completed trips rise while surge volatility decreases.",
            "mvp": "Zone-level alert queue, incentive recommendation, dispatch note, and override reason capture.",
            "north_star": "Completed rides per active supply hour",
            "guardrail": "Cancellation rate and driver earnings volatility",
            "non_goal": "Fully automated pricing changes without country operations approval.",
            "dependency": "Dispatch analytics, driver incentives, legal, country operations",
        },
        {
            "opportunity_id": "AIOP-002",
            "opportunity_name": "Courier ETA Risk Engine",
            "service_line": "Food delivery",
            "country_stage": "Dense urban zones",
            "persona": "Delivery reliability PM",
            "user_problem": "Restaurants, couriers, and customers see ETA misses too late for useful recovery actions.",
            "ai_capability": "Late-order risk prediction, restaurant prep anomaly detection, and recovery playbook ranking.",
            "market_impact": 84,
            "customer_impact": 90,
            "ops_leverage": 88,
            "data_readiness": 79,
            "ml_feasibility": 80,
            "compliance_risk": 38,
            "rollout_effort": 55,
            "stakeholder_complexity": 66,
            "confidence": 81,
            "hypothesis": "If high-risk orders are identified before courier pickup, support contacts and refund exposure decline.",
            "mvp": "Order risk score, prep delay reason codes, courier escalation, and customer recovery message test.",
            "north_star": "On-time delivered orders",
            "guardrail": "Refund rate and courier reassignment rate",
            "non_goal": "Changing restaurant ranking based only on model output.",
            "dependency": "Restaurant ops, courier ops, support, lifecycle messaging",
        },
        {
            "opportunity_id": "AIOP-003",
            "opportunity_name": "Wallet Cash-In Assistant",
            "service_line": "Payments",
            "country_stage": "Payments expansion markets",
            "persona": "Wallet growth PM",
            "user_problem": "Users trust cash but struggle to understand when wallet balance, agents, and payment acceptance help them complete daily services.",
            "ai_capability": "Personalized wallet prompt, agent availability prediction, and payment-method recommendation.",
            "market_impact": 88,
            "customer_impact": 78,
            "ops_leverage": 76,
            "data_readiness": 72,
            "ml_feasibility": 75,
            "compliance_risk": 68,
            "rollout_effort": 65,
            "stakeholder_complexity": 76,
            "confidence": 74,
            "hypothesis": "If wallet prompts are tied to service intent and agent availability, cash-in conversion rises without harming trust.",
            "mvp": "Contextual cash-in prompt, agent confidence badge, and controlled eligibility rules.",
            "north_star": "Wallet-funded completed orders",
            "guardrail": "KYC failure rate and payment support contacts",
            "non_goal": "Credit, savings, or lending recommendations.",
            "dependency": "Payments, risk, compliance, agent network, lifecycle marketing",
        },
        {
            "opportunity_id": "AIOP-004",
            "opportunity_name": "Merchant Menu Quality Copilot",
            "service_line": "Food and grocery",
            "country_stage": "Merchant growth cities",
            "persona": "Merchant operations manager",
            "user_problem": "Missing photos, out-of-stock items, unclear modifiers, and poor descriptions reduce conversion and increase order errors.",
            "ai_capability": "Menu issue detection, item normalization, translation support, and merchant action queue.",
            "market_impact": 78,
            "customer_impact": 82,
            "ops_leverage": 83,
            "data_readiness": 86,
            "ml_feasibility": 84,
            "compliance_risk": 30,
            "rollout_effort": 49,
            "stakeholder_complexity": 58,
            "confidence": 80,
            "hypothesis": "If merchants receive prioritized catalog fixes, add-to-cart conversion and order accuracy improve.",
            "mvp": "Catalog QA score, image and modifier checklist, merchant task feed, and before-after conversion readout.",
            "north_star": "Menu sessions with add-to-cart",
            "guardrail": "Order defect rate and merchant task completion",
            "non_goal": "Replacing merchant-provided pricing decisions.",
            "dependency": "Merchant ops, catalog tooling, localization, analytics",
        },
        {
            "opportunity_id": "AIOP-005",
            "opportunity_name": "Driver Earnings Quality Advisor",
            "service_line": "Partner supply",
            "country_stage": "High-supply neighborhoods",
            "persona": "Driver supply lead",
            "user_problem": "Drivers receive inconsistent signals about where and when work is likely to be profitable.",
            "ai_capability": "Personalized earnings forecast, shift planning suggestion, and fairness-aware intervention checks.",
            "market_impact": 81,
            "customer_impact": 74,
            "ops_leverage": 86,
            "data_readiness": 76,
            "ml_feasibility": 73,
            "compliance_risk": 55,
            "rollout_effort": 63,
            "stakeholder_complexity": 72,
            "confidence": 73,
            "hypothesis": "If partners can plan profitable supply hours, marketplace liquidity improves without creating unfair exposure.",
            "mvp": "Earnings range, recommended zones, confidence label, and feedback capture from drivers.",
            "north_star": "Active partner hours in shortage zones",
            "guardrail": "Earnings variance by partner cohort",
            "non_goal": "Guaranteed earnings or automated deactivation decisions.",
            "dependency": "Partner product, marketplace, trust, policy, operations",
        },
        {
            "opportunity_id": "AIOP-006",
            "opportunity_name": "B2B Fleet Demand Planner",
            "service_line": "B2B mobility",
            "country_stage": "Enterprise accounts",
            "persona": "B2B account operator",
            "user_problem": "Corporate mobility demand arrives in bursts, making fleet budgeting and availability hard to plan.",
            "ai_capability": "Account-level demand forecast, budget burn alert, and service reliability recommendation.",
            "market_impact": 72,
            "customer_impact": 76,
            "ops_leverage": 74,
            "data_readiness": 70,
            "ml_feasibility": 72,
            "compliance_risk": 42,
            "rollout_effort": 50,
            "stakeholder_complexity": 57,
            "confidence": 70,
            "hypothesis": "If account teams can forecast demand and budget burn, renewal risk decreases.",
            "mvp": "Weekly account forecast, budget threshold alert, and operations checklist.",
            "north_star": "Enterprise trips completed within budget plan",
            "guardrail": "Account complaint rate",
            "non_goal": "Automated contract pricing changes.",
            "dependency": "B2B product, sales, account operations, finance",
        },
        {
            "opportunity_id": "AIOP-007",
            "opportunity_name": "Trust Incident Triage",
            "service_line": "Cross-service trust",
            "country_stage": "All active markets",
            "persona": "Trust and safety lead",
            "user_problem": "Safety, fraud, and abuse reports compete with routine support issues, slowing urgent intervention.",
            "ai_capability": "Incident classification, severity routing, duplicate detection, and reviewer assist notes.",
            "market_impact": 79,
            "customer_impact": 89,
            "ops_leverage": 80,
            "data_readiness": 66,
            "ml_feasibility": 69,
            "compliance_risk": 74,
            "rollout_effort": 69,
            "stakeholder_complexity": 78,
            "confidence": 68,
            "hypothesis": "If urgent incidents are routed faster with human review, response SLA improves without over-automation.",
            "mvp": "Human-in-the-loop severity queue, duplicate clustering, reviewer rationale, and escalation audit trail.",
            "north_star": "Critical incident response SLA",
            "guardrail": "False negative severity review rate",
            "non_goal": "Fully automated account bans.",
            "dependency": "Support, legal, trust and safety, policy, data science",
        },
        {
            "opportunity_id": "AIOP-008",
            "opportunity_name": "Cross-Service Next Best Action",
            "service_line": "Super app growth",
            "country_stage": "Multi-service users",
            "persona": "Lifecycle growth PM",
            "user_problem": "Users who start in one service often miss relevant adjacent services because prompts are generic.",
            "ai_capability": "Intent clustering, next-service recommendation, and offer guardrail rules.",
            "market_impact": 86,
            "customer_impact": 73,
            "ops_leverage": 69,
            "data_readiness": 77,
            "ml_feasibility": 78,
            "compliance_risk": 48,
            "rollout_effort": 58,
            "stakeholder_complexity": 63,
            "confidence": 76,
            "hypothesis": "If cross-service prompts match intent and local availability, multi-service adoption increases.",
            "mvp": "Eligibility rules, recommendation score, local supply check, and holdout measurement.",
            "north_star": "Second-service activation",
            "guardrail": "Notification opt-out rate",
            "non_goal": "Always-on discounting.",
            "dependency": "Lifecycle marketing, service PMs, analytics, data platform",
        },
    ]

    for row in rows:
        row["priority_score"] = score_opportunity(row)
        row["decision"] = readiness_grade(row["priority_score"])
    return rows


def build_experiments(opportunities):
    experiments = []
    for index, row in enumerate(opportunities, start=1):
        baseline = 42 + (row["customer_impact"] % 19)
        lift = round((row["priority_score"] - 55) / 4.2, 1)
        experiments.append(
            {
                "opportunity_id": row["opportunity_id"],
                "opportunity_name": row["opportunity_name"],
                "test_type": "Geo holdout" if index % 3 == 1 else "Service cohort A/B" if index % 3 == 2 else "Staged rollout",
                "primary_metric": row["north_star"],
                "baseline": baseline,
                "target_lift_pct": max(3.8, lift),
                "minimum_sample": 3800 + index * 740,
                "launch_gate": "Ship MVP" if row["priority_score"] >= 82 else "Pilot only" if row["priority_score"] >= 72 else "Discovery",
                "risk_watch": row["guardrail"],
                "next_decision": "Expand two cities" if row["priority_score"] >= 82 else "Run limited pilot" if row["priority_score"] >= 72 else "Collect more evidence",
            }
        )
    return experiments


def build_readiness(opportunities):
    rows = []
    checks = [
        ("Event instrumentation", "Are key user and partner events captured with stable IDs?"),
        ("Label quality", "Can model labels be reviewed or corrected by operators?"),
        ("Latency fit", "Does the use case require real-time, near-real-time, or batch scoring?"),
        ("Human review", "Is there a clear approval point before customer or partner impact?"),
        ("Fairness review", "Could recommendations create unfair partner, merchant, or user outcomes?"),
    ]
    for row in opportunities:
        for idx, (check, question) in enumerate(checks):
            base = row["data_readiness"] if idx in (0, 1) else row["ml_feasibility"] if idx == 2 else 100 - row["compliance_risk"] if idx == 4 else 82
            score = max(45, min(96, round(base - idx * 2 + (row["confidence"] - 75) * 0.22)))
            rows.append(
                {
                    "opportunity_id": row["opportunity_id"],
                    "check_name": check,
                    "question": question,
                    "score": score,
                    "status": "Green" if score >= 80 else "Yellow" if score >= 65 else "Red",
                    "owner": "Data science" if idx < 3 else "Product and policy",
                }
            )
    return rows


def build_prd_cards(opportunities):
    cards = []
    for row in opportunities:
        cards.append(
            {
                "opportunity_id": row["opportunity_id"],
                "opportunity_name": row["opportunity_name"],
                "service_line": row["service_line"],
                "primary_user": row["persona"],
                "problem_statement": row["user_problem"],
                "hypothesis": row["hypothesis"],
                "mvp_scope": row["mvp"],
                "north_star": row["north_star"],
                "guardrail": row["guardrail"],
                "non_goal": row["non_goal"],
                "stakeholders": row["dependency"],
                "acceptance_criteria": json.dumps(
                    [
                        f"{row['persona']} can review the AI recommendation with a confidence label.",
                        f"The workflow captures an override reason before changing {row['service_line']} operations.",
                        f"The launch report shows {row['north_star']} and {row['guardrail']} by city cohort.",
                    ]
                ),
                "risks": json.dumps(
                    [
                        "Model confidence may be misread as an automated decision.",
                        "Country operations may need local policy or language changes.",
                        "Sparse data in expansion markets may lower recommendation quality.",
                    ]
                ),
            }
        )
    return cards


def build_summary(opportunities, experiments, readiness):
    top = opportunities[0]
    avg_score = round(sum(row["priority_score"] for row in opportunities) / len(opportunities), 1)
    ready_count = sum(1 for row in opportunities if row["priority_score"] >= 82)
    pilot_count = sum(1 for row in opportunities if 72 <= row["priority_score"] < 82)
    avg_lift = round(sum(row["target_lift_pct"] for row in experiments) / len(experiments), 1)
    readiness_yellow = sum(1 for row in readiness if row["status"] == "Yellow")
    readiness_red = sum(1 for row in readiness if row["status"] == "Red")
    return {
        "top_opportunity": top["opportunity_name"],
        "top_decision": top["decision"],
        "top_score": top["priority_score"],
        "avg_score": avg_score,
        "ready_count": ready_count,
        "pilot_count": pilot_count,
        "avg_target_lift_pct": avg_lift,
        "readiness_flags": readiness_yellow + readiness_red,
        "domain": "multi-service super app marketplace",
    }


def main():
    ensure_dirs()
    opportunities = sorted(build_opportunities(), key=lambda row: row["priority_score"], reverse=True)
    experiments = build_experiments(opportunities)
    readiness = build_readiness(opportunities)
    prd_cards = build_prd_cards(opportunities)
    summary = build_summary(opportunities, experiments, readiness)

    write_csv(DATA_DIR / "ai_opportunities.csv", opportunities, list(opportunities[0].keys()))
    write_csv(DATA_DIR / "experiment_plan.csv", experiments, list(experiments[0].keys()))
    write_csv(DATA_DIR / "model_readiness.csv", readiness, list(readiness[0].keys()))
    write_csv(DATA_DIR / "prd_cards.csv", prd_cards, list(prd_cards[0].keys()))
    write_csv(OUTPUT_DIR / "opportunity_queue.csv", opportunities, list(opportunities[0].keys()))
    write_csv(OUTPUT_DIR / "experiment_plan.csv", experiments, list(experiments[0].keys()))
    write_csv(OUTPUT_DIR / "model_readiness.csv", readiness, list(readiness[0].keys()))
    write_csv(OUTPUT_DIR / "prd_cards.csv", prd_cards, list(prd_cards[0].keys()))

    payload = {
        "summary": summary,
        "opportunities": opportunities,
        "experiments": experiments,
        "readiness": readiness,
        "prd_cards": prd_cards,
        "role_alignment": [
            "Crafts a product vision for AI at marketplace scale.",
            "Balances ride hailing, delivery, grocery, payments, partner supply, and B2B stakeholders.",
            "Uses KPI guardrails, experiment design, and model readiness checks before launch.",
            "Documents a roadmap decision that engineering, data science, operations, and marketing can debate.",
        ],
    }

    (OUTPUT_DIR / "app_payload.json").write_text(json.dumps(payload, indent=2))
    (OUTPUT_DIR / "summary.json").write_text(json.dumps(summary, indent=2))

    print(f"Top opportunity: {summary['top_opportunity']} ({summary['top_score']})")
    print(f"Ready for MVP: {summary['ready_count']}, pilot candidates: {summary['pilot_count']}")
    print(f"Readiness flags: {summary['readiness_flags']}")


if __name__ == "__main__":
    main()
