const state = {
  payload: null,
  selectedId: null,
  serviceFilter: "all",
};

const number = new Intl.NumberFormat("en-US", { maximumFractionDigits: 0 });

function selectedOpportunity() {
  return state.payload.opportunities.find((item) => item.opportunity_id === state.selectedId) || state.payload.opportunities[0];
}

function selectedPrd() {
  return state.payload.prd_cards.find((item) => item.opportunity_id === state.selectedId) || state.payload.prd_cards[0];
}

function selectedExperiment() {
  return state.payload.experiments.find((item) => item.opportunity_id === state.selectedId) || state.payload.experiments[0];
}

function filteredOpportunities() {
  return state.payload.opportunities.filter((item) => state.serviceFilter === "all" || item.service_line === state.serviceFilter);
}

function renderSummary() {
  const { summary } = state.payload;
  document.querySelector("#topDecision").textContent = summary.top_decision;
  document.querySelector("#summaryGrid").innerHTML = [
    ["Top AI bet", summary.top_opportunity, `Priority score ${summary.top_score}`],
    ["Ready bets", number.format(summary.ready_count), "MVP candidates"],
    ["Pilot queue", number.format(summary.pilot_count), "Guardrailed tests"],
    ["Avg target lift", `${summary.avg_target_lift_pct}%`, "Across proposed experiments"],
  ]
    .map(
      ([label, value, detail]) => `
        <article class="metric-card">
          <span>${label}</span>
          <strong>${value}</strong>
          <p>${detail}</p>
        </article>
      `
    )
    .join("");
}

function renderFilters() {
  const select = document.querySelector("#serviceFilter");
  const services = [...new Set(state.payload.opportunities.map((item) => item.service_line))].sort();
  select.innerHTML = [`<option value="all">All services</option>`, ...services.map((service) => `<option value="${service}">${service}</option>`)].join("");
  select.addEventListener("change", () => {
    state.serviceFilter = select.value;
    renderPortfolio();
  });
}

function scoreBars(item) {
  const bars = [
    ["Market impact", item.market_impact],
    ["Customer impact", item.customer_impact],
    ["Ops leverage", item.ops_leverage],
    ["Data readiness", item.data_readiness],
    ["ML feasibility", item.ml_feasibility],
    ["Confidence", item.confidence],
  ];

  return bars
    .map(
      ([label, value]) => `
        <div class="bar-row">
          <div><span>${label}</span><strong>${value}</strong></div>
          <div class="bar-track"><i style="width:${value}%"></i></div>
        </div>
      `
    )
    .join("");
}

function renderOpportunityList() {
  document.querySelector("#opportunityList").innerHTML = filteredOpportunities()
    .map(
      (item, index) => `
        <button class="queue-item ${item.opportunity_id === state.selectedId ? "active" : ""}" type="button" data-id="${item.opportunity_id}">
          <span class="rank">${index + 1}</span>
          <span class="queue-body">
            <strong>${item.opportunity_name}</strong>
            <small>${item.service_line}, ${item.country_stage}</small>
          </span>
          <span class="score">${item.priority_score}</span>
        </button>
      `
    )
    .join("");

  document.querySelectorAll(".queue-item").forEach((button) => {
    button.addEventListener("click", () => {
      state.selectedId = button.dataset.id;
      renderAllViews();
    });
  });
}

function renderPortfolioDetail() {
  const item = selectedOpportunity();
  document.querySelector("#portfolioDetail").innerHTML = `
    <article class="decision-card">
      <p class="eyebrow">Roadmap decision</p>
      <h3>${item.decision}</h3>
      <p>${item.hypothesis}</p>
    </article>
    <div class="detail-grid">
      <article>
        <span>Primary user</span>
        <strong>${item.persona}</strong>
        <p>${item.user_problem}</p>
      </article>
      <article>
        <span>AI capability</span>
        <strong>${item.ai_capability}</strong>
        <p>${item.dependency}</p>
      </article>
    </div>
    <div class="evidence-bars">${scoreBars(item)}</div>
    <div class="risk-strip">
      <div><span>Compliance risk</span><strong>${item.compliance_risk}</strong></div>
      <div><span>Rollout effort</span><strong>${item.rollout_effort}</strong></div>
      <div><span>Stakeholder complexity</span><strong>${item.stakeholder_complexity}</strong></div>
    </div>
  `;
}

function renderPortfolio() {
  renderOpportunityList();
  renderPortfolioDetail();
}

function renderPrd() {
  const item = selectedOpportunity();
  const card = selectedPrd();
  const criteria = JSON.parse(card.acceptance_criteria);
  const risks = JSON.parse(card.risks);

  document.querySelector("#prdTitle").textContent = card.opportunity_name;
  document.querySelector("#prdMain").innerHTML = `
    <div class="panel-title">
      <div>
        <p class="eyebrow">PRD slice</p>
        <h3>${card.opportunity_name}</h3>
      </div>
      <span>${card.service_line}</span>
    </div>
    <div class="prd-section">
      <p class="eyebrow">Problem</p>
      <p>${card.problem_statement}</p>
    </div>
    <div class="prd-section">
      <p class="eyebrow">MVP scope</p>
      <p>${card.mvp_scope}</p>
    </div>
    <div class="prd-two">
      <article>
        <p class="eyebrow">KPI tree</p>
        <strong>${card.north_star}</strong>
        <span>Guardrail: ${card.guardrail}</span>
      </article>
      <article>
        <p class="eyebrow">Non-goal</p>
        <strong>${card.non_goal}</strong>
        <span>${card.stakeholders}</span>
      </article>
    </div>
    <div class="prd-two list-panels">
      <article>
        <p class="eyebrow">Acceptance criteria</p>
        <ul>${criteria.map((criterion) => `<li>${criterion}</li>`).join("")}</ul>
      </article>
      <article>
        <p class="eyebrow">Risks to manage</p>
        <ul>${risks.map((risk) => `<li>${risk}</li>`).join("")}</ul>
      </article>
    </div>
    <div class="validation-strip">
      <strong>Product bet</strong>
      <span>${item.hypothesis}</span>
    </div>
  `;
  document.querySelector("#roleList").innerHTML = state.payload.role_alignment.map((text) => `<li>${text}</li>`).join("");
}

function renderLaunch() {
  const experiment = selectedExperiment();
  const readiness = state.payload.readiness.filter((item) => item.opportunity_id === state.selectedId);
  document.querySelector("#experimentCard").innerHTML = `
    <div class="panel-title">
      <div>
        <p class="eyebrow">Experiment plan</p>
        <h3>${experiment.opportunity_name}</h3>
      </div>
      <span>${experiment.launch_gate}</span>
    </div>
    <div class="experiment-grid">
      <article><span>Test type</span><strong>${experiment.test_type}</strong></article>
      <article><span>Primary metric</span><strong>${experiment.primary_metric}</strong></article>
      <article><span>Baseline</span><strong>${experiment.baseline}%</strong></article>
      <article><span>Target lift</span><strong>${experiment.target_lift_pct}%</strong></article>
      <article><span>Minimum sample</span><strong>${number.format(experiment.minimum_sample)}</strong></article>
      <article><span>Risk watch</span><strong>${experiment.risk_watch}</strong></article>
    </div>
    <div class="validation-strip">
      <strong>Next decision</strong>
      <span>${experiment.next_decision}</span>
    </div>
  `;

  document.querySelector("#readinessGrid").innerHTML = readiness
    .map(
      (row) => `
        <article class="readiness-card ${row.status.toLowerCase()}">
          <span>${row.check_name}</span>
          <strong>${row.score}</strong>
          <p>${row.question}</p>
          <small>${row.owner}, ${row.status}</small>
        </article>
      `
    )
    .join("");
}

function setupTabs() {
  document.querySelectorAll(".view-tabs button").forEach((button) => {
    button.addEventListener("click", () => {
      document.querySelectorAll(".view-tabs button").forEach((tab) => tab.classList.toggle("active", tab === button));
      document.querySelectorAll(".view").forEach((view) => view.classList.remove("active"));
      document.querySelector(`#${button.dataset.view}`).classList.add("active");
    });
  });
}

function renderAllViews() {
  renderPortfolio();
  renderPrd();
  renderLaunch();
}

async function init() {
  const response = await fetch("analysis/outputs/app_payload.json");
  state.payload = await response.json();
  state.selectedId = state.payload.opportunities[0].opportunity_id;
  setupTabs();
  renderSummary();
  renderFilters();
  renderAllViews();
}

init();
