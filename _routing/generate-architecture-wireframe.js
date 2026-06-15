const fs = require("fs");
const path = require("path");

const root = path.resolve(__dirname, "..");
const sourcePath = path.join(__dirname, "architecture-map.json");
const source = JSON.parse(fs.readFileSync(sourcePath, "utf8"));
const outputPath = path.join(root, source.outputPath);
const roleStatusPath = source.agentsSourcePath
  ? path.join(root, source.agentsSourcePath)
  : null;
const roleStatus = roleStatusPath
  ? JSON.parse(fs.readFileSync(roleStatusPath, "utf8"))
  : { roles: source.agents };

const requiredAgentFields = [
  "title",
  "description",
  "color",
  "truthStatus",
  "sourcePath",
  "contractStatus",
  "runtimeStatus",
  "invocationStatus",
];

const allowedTruthStatuses = new Set([
  "active-root-operating-role",
  "active-specialist-role",
  "queued-specialist",
  "provisional-review-lens",
]);

const allowedInvocationStatuses = new Set([
  "invokable-as-role",
  "not-invokable",
  "review-lens-only",
]);

function fail(message) {
  throw new Error(`Generator contract failed: ${message}`);
}

function resolveRootPath(relativePath) {
  const resolved = path.resolve(root, relativePath);
  if (!resolved.startsWith(root)) {
    fail(`Path escapes the OS root: ${relativePath}`);
  }
  return resolved;
}

function assertFile(relativePath, label) {
  const resolved = resolveRootPath(relativePath);
  if (!fs.existsSync(resolved) || !fs.statSync(resolved).isFile()) {
    fail(`${label} does not exist: ${relativePath}`);
  }
}

function assertDirectory(relativePath, label) {
  const resolved = resolveRootPath(relativePath);
  if (!fs.existsSync(resolved) || !fs.statSync(resolved).isDirectory()) {
    fail(`${label} does not exist: ${relativePath}`);
  }
}

function validateGeneratorContract() {
  if (!source.generatorContractPath) {
    fail("architecture-map.json is missing generatorContractPath");
  }
  assertFile(source.generatorContractPath, "Generator contract");
  assertFile(source.architectureBlueprintPath, "Architecture blueprint");
  assertFile(source.commandSurfaceAcceptancePath, "Command surface acceptance standard");
  assertFile(source.generatorPath, "Generator path");
  if (!source.agentsSourcePath) {
    fail("architecture-map.json is missing agentsSourcePath");
  }
  assertFile(source.agentsSourcePath, "Role status registry");
  if (!String(source.outputPath || "").startsWith("_output/")) {
    fail(`Output path must stay in _output/: ${source.outputPath}`);
  }
}

function validateAgent(agent, index) {
  const label = agent?.title || `agent at index ${index}`;
  for (const field of requiredAgentFields) {
    if (!agent || !Object.prototype.hasOwnProperty.call(agent, field) || agent[field] === "") {
      fail(`${label} is missing required field: ${field}`);
    }
  }
  if (!allowedTruthStatuses.has(agent.truthStatus)) {
    fail(`${label} has unsupported truthStatus: ${agent.truthStatus}`);
  }
  if (!allowedInvocationStatuses.has(agent.invocationStatus)) {
    fail(`${label} has unsupported invocationStatus: ${agent.invocationStatus}`);
  }
  assertFile(agent.sourcePath, `${label} sourcePath`);

  if (agent.truthStatus === "active-root-operating-role" || agent.truthStatus === "active-specialist-role") {
    if (agent.invocationStatus !== "invokable-as-role") {
      fail(`${label} active role must use invocationStatus invokable-as-role`);
    }
    if (!agent.folderPath || !agent.contractPath || !Array.isArray(agent.stagePaths)) {
      fail(`${label} active role must define folderPath, contractPath, and stagePaths`);
    }
    assertDirectory(agent.folderPath, `${label} folderPath`);
    assertFile(agent.contractPath, `${label} contractPath`);
    if (agent.stagePaths.length !== 4) {
      fail(`${label} active role must define exactly four stage contract paths`);
    }
    agent.stagePaths.forEach((stagePath) => assertFile(stagePath, `${label} stagePath`));
    return;
  }

  if (agent.invocationStatus === "invokable-as-role") {
    fail(`${label} is not an active role but claims invokable-as-role`);
  }
  if (agent.contractPath || agent.folderPath || agent.stagePaths) {
    fail(`${label} non-active entry must not declare active role contract, folder, or stage paths`);
  }
}

function validateSource() {
  validateGeneratorContract();
  if (!Array.isArray(roleStatus.roles) || roleStatus.roles.length === 0) {
    fail("role status registry must define roles");
  }
  roleStatus.roles.forEach(validateAgent);
}

validateSource();

function esc(value) {
  return String(value ?? "")
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;");
}

function node(item, extraClass = "") {
  const items = Array.isArray(item.items) && item.items.length
    ? `<ul>${item.items.map((entry) => `<li>${esc(entry)}</li>`).join("")}</ul>`
    : "";
  const tag = item.tag
    ? `<span class="tag ${esc(item.color)}">${esc(item.tag)}</span>`
    : "";
  const strong = item.strong ? " root-node" : "";
  return `
          <article class="node ${esc(item.color)}${strong}${extraClass}">
            <strong>${esc(item.title)}</strong>
            <p>${esc(item.description)}</p>
            ${items}
            ${tag}
          </article>`;
}

function agentNode(item) {
  const metaRows = [
    ["Truth", item.truthStatus],
    ["Source", item.sourcePath],
    ["Contract", item.contractStatus],
    ["Stages", item.stagePaths ? "four stage contracts verified" : "no active stage spine"],
    ["Runtime", item.runtimeStatus],
  ];
  const rows = metaRows
    .map(([label, value]) => `<li><span>${esc(label)}</span>${esc(value)}</li>`)
    .join("");
  const statusClass = item.invocationStatus === "invokable-as-role"
    ? "active"
    : item.invocationStatus === "review-lens-only"
      ? "provisional"
      : "blocked";
  return `
          <article class="node ${esc(item.color)} agent ${statusClass}">
            <strong>${esc(item.title)}</strong>
            <p>${esc(item.description)}</p>
            <ul class="agent-meta">${rows}</ul>
            <span class="status-tag ${statusClass}">${esc(item.invocationStatus)}</span>
          </article>`;
}

function project(project) {
  const pills = project.items
    .map((item) => `<div class="pill ${esc(item.state)}">${esc(item.label)}</div>`)
    .join("");
  return `
          <article class="node project ${esc(project.color)}">
            <strong>${esc(project.title)}</strong>
            <p>${esc(project.description)}</p>
            <div class="project-grid">${pills}</div>
            <span class="tag ${esc(project.color)}">${esc(project.tag)}</span>
          </article>`;
}

function legend() {
  return source.legend
    .map((item) => `<span><i class="dot ${esc(item.color)}"></i>${esc(item.label)}</span>`)
    .join("");
}

function flow() {
  return source.workflow
    .map((step, index) => {
      const arrow = index === 0 ? "" : `<div class="arrow">&gt;</div>`;
      return `${arrow}<div class="flow-step">${esc(step)}</div>`;
    })
    .join("");
}

function vigloreComponents() {
  const rows = source.viglore.componentBreakdown
    .map((item) => `
            <tr>
              <td>${esc(item.component)}</td>
              <td>${esc(item.behavior)}</td>
              <td>${esc(item.bucket)}</td>
              <td>${esc(item.estimate)}</td>
            </tr>`)
    .join("");
  return `
          <table class="data-table component-table">
            <thead>
              <tr>
                <th>Component</th>
                <th>What it actually does</th>
                <th>60 / 30 / 10 bucket</th>
                <th>AI part vs everything else</th>
              </tr>
            </thead>
            <tbody>${rows}
            </tbody>
          </table>`;
}

function vigloreRatio() {
  const rows = source.viglore.honestRatio
    .map((item) => `
              <tr>
                <td>${esc(item.category)}</td>
                <td>${esc(item.share)}</td>
              </tr>`)
    .join("");
  return `
            <table class="data-table ratio-table">
              <thead>
                <tr>
                  <th>Category</th>
                  <th>Estimated share</th>
                </tr>
              </thead>
              <tbody>${rows}
              </tbody>
            </table>`;
}

function truthmodeRows() {
  const rows = source.truthmodeComparison.comparisonRows
    .map((item) => `
            <tr>
              <td>${esc(item.dimension)}</td>
              <td>${esc(item.collideascope)}</td>
              <td>${esc(item.atx)}</td>
              <td>${esc(item.assessment)}</td>
            </tr>`)
    .join("");
  return `
          <table class="data-table truthmode-table">
            <thead>
              <tr>
                <th>Dimension</th>
                <th>CollideascopeOS</th>
                <th>Command Center OS</th>
                <th>Truthmode Assessment</th>
              </tr>
            </thead>
            <tbody>${rows}
            </tbody>
          </table>`;
}

function performanceGaps() {
  return source.truthmodeComparison.performanceGaps
    .map((item) => `
            <article class="gap-card ${esc(item.state)}">
              <div>
                <strong>${esc(item.gap)}</strong>
                <span>${esc(item.state)}</span>
              </div>
              <p>${esc(item.nextAction)}</p>
            </article>`)
    .join("");
}

function truthmodeComparison() {
  const comparison = source.truthmodeComparison;
  return `
      <div class="band truthmode-band">
        <div class="band-title">${esc(comparison.title)} <small>${esc(comparison.source)}</small></div>
        <div class="truthmode-judgment">
          <strong>${esc(comparison.judgment)}</strong>
          <p>${esc(comparison.operatingLine)}</p>
        </div>
        ${truthmodeRows()}
        <div class="gap-grid">${performanceGaps()}</div>
      </div>`;
}

function html() {
  const blueprintLine = source.architectureBlueprintPath
    ? `<br><strong>Architecture blueprint:</strong> ${esc(` ${source.architectureBlueprintPath}`)}`
    : "";
  const acceptanceLine = source.commandSurfaceAcceptancePath
    ? `<br><strong>Acceptance standard:</strong> ${esc(` ${source.commandSurfaceAcceptancePath}`)}`
    : "";
  const contractLine = source.generatorContractPath
    ? `<br><strong>Generator contract:</strong> ${esc(` ${source.generatorContractPath}`)}`
    : "";
  const roleStatusLine = source.agentsSourcePath
    ? `<br><strong>Role status registry:</strong> ${esc(` ${source.agentsSourcePath}`)}`
    : "";
  const statusLine = source.commandSurfaceStatus
    ? `<br><strong>Surface status:</strong> ${esc(` ${source.commandSurfaceStatus}`)}`
    : "";
  return `<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>${esc(source.title)}</title>
  <style>
    :root {
      --bg-0: #13001f;
      --bg-1: #210033;
      --panel: rgba(31, 10, 54, 0.82);
      --panel-strong: rgba(42, 14, 78, 0.94);
      --text: #f8eeff;
      --muted: #d8b8ff;
      --cyan: #20f6ff;
      --blue: #55b9ff;
      --green: #6dff9f;
      --pink: #ff4fd8;
      --amber: #ffe66d;
      --violet: #a66cff;
      --red: #ff5f8f;
      color-scheme: dark;
      font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
    }
    * { box-sizing: border-box; }
    body {
      min-width: 1420px;
      margin: 0;
      color: var(--text);
      background:
        radial-gradient(circle at 20% 8%, rgba(255, 79, 216, 0.28), transparent 28%),
        radial-gradient(circle at 78% 4%, rgba(32, 246, 255, 0.20), transparent 30%),
        linear-gradient(145deg, var(--bg-0), var(--bg-1) 48%, #0b0017);
    }
    main { position: relative; min-height: 100vh; padding: 32px; overflow: hidden; }
    .grid-glow {
      position: fixed; inset: 0; pointer-events: none;
      background-image:
        linear-gradient(rgba(255, 255, 255, 0.045) 1px, transparent 1px),
        linear-gradient(90deg, rgba(255, 255, 255, 0.045) 1px, transparent 1px);
      background-size: 36px 36px;
      mask-image: linear-gradient(to bottom, rgba(0, 0, 0, 0.9), transparent 85%);
    }
    header {
      position: relative; display: flex; align-items: flex-end; justify-content: space-between;
      gap: 24px; margin-bottom: 18px; z-index: 2;
    }
    h1 {
      margin: 0; color: #fff; font-size: 34px; line-height: 1.05; letter-spacing: 0;
      text-shadow: 0 0 22px rgba(166, 108, 255, 0.9);
    }
    .subtitle { margin: 9px 0 0; color: var(--muted); font-size: 14px; max-width: 760px; }
    .source-banner {
      position: relative; z-index: 2; display: grid; grid-template-columns: 1fr 1fr; gap: 12px;
      margin-bottom: 18px;
    }
    .source-box {
      min-height: 54px; padding: 11px 13px; border: 1px solid rgba(32, 246, 255, 0.38);
      border-radius: 8px; background: rgba(32, 246, 255, 0.08); color: #e8fdff;
      font-size: 12px; line-height: 1.35; box-shadow: 0 0 16px rgba(32, 246, 255, 0.18);
    }
    .source-box strong { color: #fff; }
    .legend {
      display: grid; grid-template-columns: repeat(2, auto); gap: 8px 16px; padding: 14px 16px;
      border: 1px solid rgba(190, 120, 255, 0.36); border-radius: 8px;
      background: rgba(18, 0, 32, 0.64); box-shadow: 0 0 22px rgba(166, 108, 255, 0.18);
      font-size: 12px; white-space: nowrap;
    }
    .legend span { display: inline-flex; align-items: center; gap: 8px; color: var(--muted); }
    .dot { width: 10px; height: 10px; border-radius: 50%; box-shadow: 0 0 12px currentColor; }
    .dot.cyan { color: var(--cyan); background: var(--cyan); }
    .dot.blue { color: var(--blue); background: var(--blue); }
    .dot.green { color: var(--green); background: var(--green); }
    .dot.pink { color: var(--pink); background: var(--pink); }
    .dot.red { color: var(--red); background: var(--red); }
    .canvas { position: relative; display: grid; grid-template-columns: 1fr; gap: 18px; z-index: 1; }
    .band {
      position: relative; border: 1px solid rgba(190, 120, 255, 0.26); border-radius: 8px;
      background: rgba(11, 0, 23, 0.54); box-shadow: inset 0 0 28px rgba(166, 108, 255, 0.10);
      padding: 18px;
    }
    .band-title {
      display: flex; align-items: center; justify-content: space-between; gap: 12px; margin-bottom: 14px;
      color: var(--amber); font-size: 12px; font-weight: 800; text-transform: uppercase;
      letter-spacing: 0.08em; text-shadow: 0 0 12px rgba(255, 230, 109, 0.6);
    }
    .band-title small { color: var(--muted); font-weight: 600; text-transform: none; letter-spacing: 0; }
    .root-row { display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); gap: 14px; }
    .systems-row { display: grid; grid-template-columns: repeat(auto-fit, minmax(132px, 1fr)); gap: 14px; }
    .agents-row { display: grid; grid-template-columns: repeat(9, minmax(0, 1fr)); gap: 10px; }
    .projects-row { display: grid; grid-template-columns: repeat(auto-fit, minmax(230px, 1fr)); gap: 14px; }
    .node {
      position: relative; min-height: 104px; padding: 14px; border: 1px solid rgba(255, 255, 255, 0.12);
      border-radius: 8px; background: var(--panel); overflow: hidden;
    }
    .node::before { content: ""; position: absolute; inset: 0; border-radius: 8px; opacity: 0.86; pointer-events: none; }
    .node strong, .node p, .node ul, .node .tag, .project-grid { position: relative; z-index: 1; }
    .node strong { display: block; margin-bottom: 7px; font-size: 15px; line-height: 1.1; color: #fff; }
    .node p { margin: 0; color: var(--muted); font-size: 12px; line-height: 1.35; }
    .node ul { display: grid; gap: 5px; margin: 10px 0 0; padding: 0; list-style: none; color: var(--muted); font-size: 11px; line-height: 1.25; }
    .node li { padding-left: 12px; position: relative; }
    .node li::before {
      content: ""; position: absolute; left: 0; top: 0.58em; width: 5px; height: 5px;
      border-radius: 50%; background: currentColor; box-shadow: 0 0 9px currentColor; transform: translateY(-50%);
    }
    .tag {
      display: inline-flex; align-items: center; width: max-content; max-width: 100%; min-height: 22px;
      margin-top: 10px; padding: 3px 8px; border-radius: 999px; font-size: 11px; font-weight: 800;
      line-height: 1.1; text-transform: uppercase; letter-spacing: 0.04em;
    }
    .cyan { border-color: rgba(32, 246, 255, 0.55); box-shadow: 0 0 18px rgba(32, 246, 255, 0.45); }
    .cyan::before { background: linear-gradient(135deg, rgba(32, 246, 255, 0.18), transparent 55%); }
    .green { border-color: rgba(109, 255, 159, 0.50); box-shadow: 0 0 18px rgba(109, 255, 159, 0.36); }
    .green::before { background: linear-gradient(135deg, rgba(109, 255, 159, 0.15), transparent 55%); }
    .pink { border-color: rgba(255, 79, 216, 0.55); box-shadow: 0 0 18px rgba(255, 79, 216, 0.45); }
    .pink::before { background: linear-gradient(135deg, rgba(255, 79, 216, 0.18), transparent 55%); }
    .amber { border-color: rgba(255, 230, 109, 0.58); box-shadow: 0 0 18px rgba(255, 230, 109, 0.34); }
    .amber::before { background: linear-gradient(135deg, rgba(255, 230, 109, 0.16), transparent 55%); }
    .red { border-color: rgba(255, 95, 143, 0.58); box-shadow: 0 0 18px rgba(255, 95, 143, 0.34); }
    .red::before { background: linear-gradient(135deg, rgba(255, 95, 143, 0.16), transparent 55%); }
    .violet { border-color: rgba(166, 108, 255, 0.58); box-shadow: 0 0 18px rgba(166, 108, 255, 0.34); }
    .violet::before { background: linear-gradient(135deg, rgba(166, 108, 255, 0.18), transparent 55%); }
    .tag.cyan { color: #001b20; background: var(--cyan); box-shadow: 0 0 18px rgba(32, 246, 255, 0.45); }
    .tag.green { color: #001b09; background: var(--green); box-shadow: 0 0 18px rgba(109, 255, 159, 0.36); }
    .tag.pink { color: #2b0020; background: var(--pink); box-shadow: 0 0 18px rgba(255, 79, 216, 0.45); }
    .tag.amber { color: #251b00; background: var(--amber); box-shadow: 0 0 16px rgba(255, 230, 109, 0.42); }
    .tag.red { color: #27000d; background: var(--red); box-shadow: 0 0 16px rgba(255, 95, 143, 0.42); }
    .tag.violet { color: #140026; background: #caa8ff; box-shadow: 0 0 16px rgba(166, 108, 255, 0.42); }
    .root-node { min-height: 136px; background: var(--panel-strong); }
    .agent { min-height: 126px; padding: 12px; }
    .agent strong { font-size: 13px; }
    .agent p { font-size: 11px; }
    .agent.blocked { opacity: 0.88; }
    .agent.provisional { opacity: 0.94; }
    .agent-meta {
      display: grid; gap: 5px; margin: 10px 0 0; padding: 0; list-style: none;
      color: var(--muted); font-size: 10px; line-height: 1.25;
    }
    .agent-meta li {
      display: grid; grid-template-columns: 52px minmax(0, 1fr); gap: 6px; padding-left: 0;
      word-break: break-word;
    }
    .agent-meta li::before { content: none; }
    .agent-meta span { color: #fff; font-weight: 800; }
    .status-tag {
      position: relative; z-index: 1; display: inline-flex; align-items: center; width: max-content;
      max-width: 100%; min-height: 22px; margin-top: 10px; padding: 3px 8px; border-radius: 999px;
      font-size: 10px; font-weight: 900; line-height: 1.1; text-transform: uppercase; letter-spacing: 0.04em;
    }
    .status-tag.active { color: #001b09; background: var(--green); box-shadow: 0 0 14px rgba(109, 255, 159, 0.28); }
    .status-tag.provisional { color: #140026; background: #caa8ff; box-shadow: 0 0 14px rgba(166, 108, 255, 0.28); }
    .status-tag.blocked { color: #27000d; background: var(--red); box-shadow: 0 0 14px rgba(255, 95, 143, 0.28); }
    .project { min-height: 220px; }
    .project-grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 7px; margin-top: 12px; }
    .pill {
      min-height: 28px; padding: 6px 8px; border: 1px solid rgba(255, 255, 255, 0.12);
      border-radius: 7px; background: rgba(255, 255, 255, 0.045); color: var(--muted);
      font-size: 11px; line-height: 1.2;
    }
    .pill.ok { color: #d8ffe3; border-color: rgba(109, 255, 159, 0.38); background: rgba(109, 255, 159, 0.10); }
    .pill.project { color: #d9f0ff; border-color: rgba(85, 185, 255, 0.42); background: rgba(85, 185, 255, 0.11); }
    .pill.missing { color: #ffd2df; border-color: rgba(255, 95, 143, 0.42); background: rgba(255, 95, 143, 0.10); }
    .pill.placeholder { color: #fff4bd; border-color: rgba(255, 230, 109, 0.42); background: rgba(255, 230, 109, 0.10); }
    .connector-labels { display: grid; grid-template-columns: repeat(auto-fit, minmax(230px, 1fr)); gap: 14px; margin-top: 10px; }
    .note {
      min-height: 56px; padding: 10px 12px; border-left: 3px solid var(--cyan); border-radius: 7px;
      background: rgba(32, 246, 255, 0.08); color: var(--muted); font-size: 12px; line-height: 1.35;
    }
    .flow { display: grid; grid-template-columns: repeat(auto-fit, minmax(92px, 1fr)); align-items: center; gap: 8px; margin-top: 14px; }
    .flow-step {
      min-height: 48px; display: grid; place-items: center; text-align: center; padding: 8px;
      border: 1px solid rgba(32, 246, 255, 0.42); border-radius: 8px;
      background: rgba(32, 246, 255, 0.08); color: #e8fdff; font-size: 11px; font-weight: 700;
      box-shadow: 0 0 12px rgba(32, 246, 255, 0.16);
    }
    .arrow { color: var(--pink); text-align: center; text-shadow: 0 0 12px rgba(255, 79, 216, 0.9); font-weight: 900; }
    .viglore-grid { display: grid; grid-template-columns: minmax(0, 1fr) 260px; gap: 14px; align-items: start; }
    .data-table {
      width: 100%; border-collapse: collapse; overflow: hidden; border-radius: 8px;
      background: rgba(31, 10, 54, 0.62); border: 1px solid rgba(32, 246, 255, 0.24);
      box-shadow: 0 0 16px rgba(32, 246, 255, 0.12);
    }
    .data-table th, .data-table td {
      padding: 10px 11px; border-bottom: 1px solid rgba(255, 255, 255, 0.10);
      border-right: 1px solid rgba(255, 255, 255, 0.08); text-align: left; vertical-align: top;
      font-size: 11px; line-height: 1.35;
    }
    .data-table th {
      color: #fff; background: rgba(32, 246, 255, 0.12); font-size: 10px;
      text-transform: uppercase; letter-spacing: 0.08em;
    }
    .data-table td { color: var(--muted); }
    .component-table tbody td { color: #fff; }
    .data-table td:first-child { color: #fff; font-weight: 800; }
    .data-table tr:last-child td { border-bottom: 0; }
    .data-table th:last-child, .data-table td:last-child { border-right: 0; }
    .ratio-table td:last-child { color: var(--amber); font-size: 16px; font-weight: 900; text-align: right; }
    .truthmode-band {
      border-color: rgba(255, 230, 109, 0.42);
      box-shadow: inset 0 0 28px rgba(255, 230, 109, 0.08), 0 0 22px rgba(255, 230, 109, 0.10);
    }
    .truthmode-judgment {
      display: grid; gap: 8px; margin-bottom: 14px; padding: 14px;
      border: 1px solid rgba(255, 230, 109, 0.34); border-radius: 8px;
      background: rgba(255, 230, 109, 0.08);
    }
    .truthmode-judgment strong { color: #fff; font-size: 15px; line-height: 1.3; }
    .truthmode-judgment p { margin: 0; color: var(--amber); font-size: 13px; font-weight: 800; }
    .truthmode-table { margin-bottom: 14px; }
    .truthmode-table td:nth-child(4) { color: #fff; font-weight: 700; }
    .gap-grid { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 12px; }
    .gap-card {
      min-height: 104px; padding: 12px; border: 1px solid rgba(255, 255, 255, 0.12);
      border-radius: 8px; background: rgba(31, 10, 54, 0.62);
    }
    .gap-card div { display: flex; align-items: flex-start; justify-content: space-between; gap: 10px; margin-bottom: 9px; }
    .gap-card strong { color: #fff; font-size: 13px; line-height: 1.2; }
    .gap-card span {
      min-height: 20px; padding: 3px 7px; border-radius: 999px; font-size: 10px; font-weight: 900;
      line-height: 1.1; text-transform: uppercase; letter-spacing: 0.05em;
    }
    .gap-card p { margin: 0; color: var(--muted); font-size: 11px; line-height: 1.35; }
    .gap-card.pending { border-color: rgba(255, 230, 109, 0.45); box-shadow: 0 0 14px rgba(255, 230, 109, 0.16); }
    .gap-card.pending span { color: #251b00; background: var(--amber); }
    .gap-card.active { border-color: rgba(109, 255, 159, 0.42); box-shadow: 0 0 14px rgba(109, 255, 159, 0.14); }
    .gap-card.active span { color: #001b09; background: var(--green); }
    .gap-card.blocked { border-color: rgba(255, 95, 143, 0.42); box-shadow: 0 0 14px rgba(255, 95, 143, 0.14); }
    .gap-card.blocked span { color: #27000d; background: var(--red); }
    footer { margin-top: 18px; padding: 14px 4px 0; color: var(--muted); font-size: 12px; }
    @media (max-width: 1280px) {
      main { padding: 24px; }
      .agents-row { grid-template-columns: repeat(4, 1fr); }
      .root-row, .systems-row, .projects-row { grid-template-columns: repeat(2, 1fr); }
      .source-banner, .connector-labels, .viglore-grid { grid-template-columns: 1fr; }
      .gap-grid { grid-template-columns: 1fr; }
      .flow { grid-template-columns: repeat(3, 1fr); }
      .arrow { display: none; }
    }
  </style>
</head>
<body>
  <div class="grid-glow" aria-hidden="true"></div>
  <main>
    <header>
      <div>
        <h1>${esc(source.title)}</h1>
        <p class="subtitle">${esc(source.subtitle)}</p>
      </div>
      <div class="legend" aria-label="Legend">${legend()}</div>
    </header>
    <section class="source-banner" aria-label="Source of truth">
      <div class="source-box"><strong>Source of truth:</strong> ${esc(" _routing/architecture-map.json")}<br><strong>Generator:</strong> ${esc(" _routing/generate-architecture-wireframe.js")}${blueprintLine}${acceptanceLine}${contractLine}${roleStatusLine}${statusLine}</div>
      <div class="source-box"><strong>Human interface truth:</strong> ${esc(source.humanInterfaceTruth)}</div>
    </section>
    <section class="canvas" aria-label="${esc(source.title)}">
      <div class="band">
        <div class="band-title">Root Spine <small>identity, route, source systems, and review lane</small></div>
        <div class="root-row">${source.rootSpine.map((item) => node(item)).join("")}
        </div>
      </div>
      <div class="band">
        <div class="band-title">Layer 3 Source Systems <small>the rules and records that govern future runs</small></div>
        <div class="systems-row">${source.sourceSystems.map((item) => node(item)).join("")}
        </div>
      </div>
      <div class="band">
        <div class="band-title">Agent And Review Layer <small>source-backed role status; queued roles are not built</small></div>
        <div class="agents-row">${roleStatus.roles.map((item) => agentNode(item)).join("")}
        </div>
        <div class="flow" aria-label="Default workflow">${flow()}</div>
      </div>
      <div class="band">
        <div class="band-title">Viglore Component Breakdown <small>current 60 / 30 / 10 operating decomposition</small></div>
        <div class="viglore-grid">
          ${vigloreComponents()}
          <div>
            <div class="band-title">Honest Ratio <small>no summary text</small></div>
            ${vigloreRatio()}
          </div>
        </div>
      </div>
      ${truthmodeComparison()}
      <div class="band">
        <div class="band-title">Project Workspaces <small>current wiring state</small></div>
        <div class="projects-row">${source.projects.map((item) => project(item)).join("")}
        </div>
        <div class="connector-labels">${source.notes.map((noteText) => `<div class="note">${esc(noteText)}</div>`).join("")}</div>
      </div>
    </section>
    <footer>
      Generated from ${esc("_routing/architecture-map.json")}. To update this interface, edit the source map and run ${esc("node _routing/generate-architecture-wireframe.js")}.
    </footer>
  </main>
</body>
</html>
`;
}

fs.mkdirSync(path.dirname(outputPath), { recursive: true });
const renderedHtml = html().replace(/[ \t]+$/gm, "");
fs.writeFileSync(outputPath, renderedHtml, "utf8");
console.log(`Generated ${path.relative(root, outputPath)} from ${path.relative(root, sourcePath)}`);
