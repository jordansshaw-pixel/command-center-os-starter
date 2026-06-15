const fs = require("fs");
const path = require("path");

const root = path.resolve(__dirname, "..");
const sourcePath = path.join(__dirname, "agent-review-interface-map.json");
const source = JSON.parse(fs.readFileSync(sourcePath, "utf8"));
const outputPath = path.join(root, source.outputPath);
const readmePath = path.join(root, source.readmePath);

const forbiddenPublicTerms = [
  ["Jor", "dan"].join(""),
  ["Brand", " Guide"].join(""),
  ["Brand", "-Guide"].join(""),
  ["brand", "-guide"].join(""),
  ["Brand", " Guardian"].join(""),
  ["Truth", " Cockpit"].join(""),
  ["Truth", "-cockpit"].join(""),
  ["Collidea", "scope"].join(""),
  ["Project", " Workspaces"].join(""),
  ["Cali", "ber"].join(""),
  ["EC", "MA"].join(""),
  ["Cl", "ief"].join(""),
  ["LGAI", "PRO"].join(""),
  ["Safety", "Call"].join(""),
  ["Solutions", "Factory"].join(""),
  ["Hoku", "lani"].join(""),
  "C:" + "\\",
  "_" + "operator",
  "CLAUDE" + ".md"
];

function fail(message) {
  throw new Error(`Agent review interface generation failed: ${message}`);
}

function assertArray(value, label) {
  if (!Array.isArray(value) || value.length === 0) {
    fail(`${label} must be a non-empty array`);
  }
}

function assertText(value, label) {
  if (typeof value !== "string" || value.trim() === "") {
    fail(`${label} must be a non-empty string`);
  }
}

function validateSource() {
  assertText(source.title, "title");
  assertText(source.subtitle, "subtitle");
  assertText(source.outputPath, "outputPath");
  assertText(source.readmePath, "readmePath");
  assertText(source.generatorPath, "generatorPath");
  assertArray(source.sourceSystems, "sourceSystems");
  assertArray(source.agentGroups, "agentGroups");
  assertArray(source.stageSpine, "stageSpine");
  assertArray(source.reviewFlow, "reviewFlow");
  assertArray(source.reviewGates, "reviewGates");
  assertArray(source.publicNotes, "publicNotes");

  if (!source.outputPath.startsWith("_output/")) {
    fail("outputPath must stay under _output/");
  }
  if (!source.readmePath.startsWith("_output/")) {
    fail("readmePath must stay under _output/");
  }
  if (source.publicSafety?.mustNotShow?.includes("foundation layer") !== true) {
    fail("publicSafety.mustNotShow must include foundation layer");
  }

  source.sourceSystems.forEach((item, index) => {
    assertText(item.title, `sourceSystems[${index}].title`);
    assertText(item.description, `sourceSystems[${index}].description`);
    assertArray(item.checks, `sourceSystems[${index}].checks`);
  });

  source.agentGroups.forEach((group, groupIndex) => {
    assertText(group.title, `agentGroups[${groupIndex}].title`);
    assertArray(group.agents, `agentGroups[${groupIndex}].agents`);
    group.agents.forEach((agent, agentIndex) => {
      assertText(agent.title, `agentGroups[${groupIndex}].agents[${agentIndex}].title`);
      assertText(agent.description, `agentGroups[${groupIndex}].agents[${agentIndex}].description`);
      assertText(agent.status, `agentGroups[${groupIndex}].agents[${agentIndex}].status`);
      assertText(agent.stageModel, `agentGroups[${groupIndex}].agents[${agentIndex}].stageModel`);
      assertText(agent.accent, `agentGroups[${groupIndex}].agents[${agentIndex}].accent`);
    });
  });
}

function esc(value) {
  return String(value ?? "")
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;");
}

function sourceCard(item) {
  const checks = item.checks.map((check) => `<span>${esc(check)}</span>`).join("");
  return `
      <article class="source-card">
        <div class="card-top">
          <strong>${esc(item.title)}</strong>
          <em>${esc(item.type)}</em>
        </div>
        <p>${esc(item.description)}</p>
        <div class="chips">${checks}</div>
      </article>`;
}

function agentCard(agent) {
  return `
      <article class="agent-card ${esc(agent.accent)}">
        <div class="orb"></div>
        <strong>${esc(agent.title)}</strong>
        <p>${esc(agent.description)}</p>
        <div class="agent-meta">
          <span>${esc(agent.status)}</span>
          <span>${esc(agent.stageModel)}</span>
        </div>
      </article>`;
}

function stageCard(stage, index) {
  return `
      <article class="stage-card">
        <span>${String(index + 1).padStart(2, "0")}</span>
        <strong>${esc(stage.title)}</strong>
        <p>${esc(stage.description)}</p>
      </article>`;
}

function gateCard(gate) {
  return `
      <article class="gate-card">
        <strong>${esc(gate.title)}</strong>
        <p>${esc(gate.description)}</p>
      </article>`;
}

function html() {
  const sourceSystems = source.sourceSystems.map(sourceCard).join("");
  const agentGroups = source.agentGroups.map((group) => `
    <section class="band">
      <div class="band-head">
        <span>${esc(group.title)}</span>
        <small>${esc(group.description)}</small>
      </div>
      <div class="agent-grid">${group.agents.map(agentCard).join("")}
      </div>
    </section>`).join("");
  const stages = source.stageSpine.map(stageCard).join("");
  const gates = source.reviewGates.map(gateCard).join("");
  const flow = source.reviewFlow.map((step) => `<span>${esc(step)}</span>`).join("");
  const notes = source.publicNotes.map((note) => `<li>${esc(note)}</li>`).join("");

  return `<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>${esc(source.title)}</title>
  <style>
    :root {
      --bg: #090b12;
      --panel: rgba(20, 25, 36, 0.88);
      --panel-strong: rgba(27, 34, 48, 0.94);
      --line: rgba(255, 255, 255, 0.12);
      --text: #f4f7fb;
      --muted: #aeb9ca;
      --cyan: #27d9ff;
      --green: #70f3a5;
      --pink: #ff72bd;
      --amber: #ffd166;
      --red: #ff6b6b;
      --violet: #a78bfa;
      font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      color-scheme: dark;
    }
    * { box-sizing: border-box; }
    body {
      margin: 0;
      color: var(--text);
      background:
        radial-gradient(circle at 18% 0%, rgba(39, 217, 255, 0.20), transparent 28%),
        radial-gradient(circle at 72% 3%, rgba(167, 139, 250, 0.18), transparent 30%),
        linear-gradient(135deg, #080a10, #101522 48%, #080a10);
    }
    body::before {
      content: "";
      position: fixed;
      inset: 0;
      background-image:
        linear-gradient(rgba(255, 255, 255, 0.045) 1px, transparent 1px),
        linear-gradient(90deg, rgba(255, 255, 255, 0.045) 1px, transparent 1px);
      background-size: 34px 34px;
      mask-image: linear-gradient(to bottom, rgba(0,0,0,.9), transparent 82%);
      pointer-events: none;
    }
    main {
      position: relative;
      width: min(1440px, calc(100vw - 48px));
      margin: 0 auto;
      padding: 32px 0 36px;
    }
    header {
      display: grid;
      grid-template-columns: minmax(0, 1fr) 390px;
      gap: 22px;
      align-items: end;
      margin-bottom: 18px;
    }
    h1 {
      margin: 0;
      font-size: clamp(36px, 5vw, 72px);
      line-height: 0.92;
      letter-spacing: 0;
      text-transform: uppercase;
    }
    .subtitle {
      max-width: 820px;
      margin: 14px 0 0;
      color: var(--muted);
      font-size: 16px;
      line-height: 1.45;
    }
    .status-panel {
      padding: 16px;
      border: 1px solid rgba(39, 217, 255, 0.35);
      border-radius: 8px;
      background: rgba(39, 217, 255, 0.08);
      box-shadow: 0 0 24px rgba(39, 217, 255, 0.12);
    }
    .status-panel strong { display: block; margin-bottom: 8px; }
    .status-panel p { margin: 0; color: var(--muted); font-size: 13px; line-height: 1.45; }
    .layout {
      display: grid;
      gap: 18px;
    }
    .band {
      border: 1px solid var(--line);
      border-radius: 8px;
      background: rgba(9, 11, 18, 0.58);
      box-shadow: inset 0 0 30px rgba(255,255,255,0.035);
      padding: 18px;
    }
    .band-head {
      display: flex;
      align-items: flex-end;
      justify-content: space-between;
      gap: 16px;
      margin-bottom: 14px;
    }
    .band-head span {
      color: #ffffff;
      font-size: 14px;
      font-weight: 900;
      letter-spacing: 0.08em;
      text-transform: uppercase;
    }
    .band-head small {
      max-width: 680px;
      color: var(--muted);
      font-size: 12px;
      line-height: 1.35;
      text-align: right;
    }
    .source-grid {
      display: grid;
      grid-template-columns: repeat(4, minmax(0, 1fr));
      gap: 12px;
    }
    .source-card, .agent-card, .stage-card, .gate-card, .note-card {
      position: relative;
      border: 1px solid var(--line);
      border-radius: 8px;
      background: var(--panel);
      overflow: hidden;
    }
    .source-card { min-height: 176px; padding: 14px; }
    .source-card::before {
      content: "";
      position: absolute;
      inset: 0;
      background: linear-gradient(135deg, rgba(39, 217, 255, 0.12), transparent 54%);
      pointer-events: none;
    }
    .card-top, .source-card p, .chips, .agent-card > *, .stage-card > *, .gate-card > * { position: relative; z-index: 1; }
    .card-top { display: flex; align-items: flex-start; justify-content: space-between; gap: 10px; margin-bottom: 9px; }
    .card-top strong, .agent-card strong, .stage-card strong, .gate-card strong {
      display: block;
      color: #fff;
      font-size: 14px;
      line-height: 1.18;
    }
    .card-top em {
      color: var(--cyan);
      font-size: 10px;
      font-style: normal;
      font-weight: 900;
      text-transform: uppercase;
      white-space: nowrap;
    }
    p { color: var(--muted); font-size: 12px; line-height: 1.42; }
    .chips { display: flex; flex-wrap: wrap; gap: 6px; margin-top: 12px; }
    .chips span, .agent-meta span {
      min-height: 23px;
      display: inline-flex;
      align-items: center;
      padding: 4px 7px;
      border: 1px solid rgba(255,255,255,.12);
      border-radius: 999px;
      background: rgba(255,255,255,.055);
      color: #dce7f7;
      font-size: 10px;
      font-weight: 800;
      line-height: 1.1;
      text-transform: uppercase;
    }
    .agent-grid {
      display: grid;
      grid-template-columns: repeat(4, minmax(0, 1fr));
      gap: 12px;
    }
    .agent-card {
      min-height: 184px;
      padding: 14px;
    }
    .agent-card::before {
      content: "";
      position: absolute;
      inset: 0;
      background: linear-gradient(135deg, color-mix(in srgb, currentColor 18%, transparent), transparent 58%);
      opacity: .75;
      pointer-events: none;
    }
    .agent-card.cyan { color: var(--cyan); border-color: rgba(39, 217, 255, .38); box-shadow: 0 0 18px rgba(39,217,255,.12); }
    .agent-card.green { color: var(--green); border-color: rgba(112, 243, 165, .38); box-shadow: 0 0 18px rgba(112,243,165,.12); }
    .agent-card.pink { color: var(--pink); border-color: rgba(255, 114, 189, .38); box-shadow: 0 0 18px rgba(255,114,189,.12); }
    .agent-card.amber { color: var(--amber); border-color: rgba(255, 209, 102, .38); box-shadow: 0 0 18px rgba(255,209,102,.12); }
    .agent-card.red { color: var(--red); border-color: rgba(255, 107, 107, .38); box-shadow: 0 0 18px rgba(255,107,107,.12); }
    .agent-card.violet { color: var(--violet); border-color: rgba(167, 139, 250, .40); box-shadow: 0 0 18px rgba(167,139,250,.12); }
    .orb {
      width: 28px;
      height: 28px;
      margin-bottom: 12px;
      border-radius: 50%;
      background: currentColor;
      box-shadow: 0 0 24px currentColor;
    }
    .agent-card p { margin: 8px 0 0; }
    .agent-meta { display: flex; flex-wrap: wrap; gap: 6px; margin-top: 12px; }
    .stage-grid, .gate-grid {
      display: grid;
      grid-template-columns: repeat(4, minmax(0, 1fr));
      gap: 12px;
    }
    .stage-card, .gate-card { min-height: 128px; padding: 14px; background: var(--panel-strong); }
    .stage-card span {
      display: inline-flex;
      margin-bottom: 10px;
      color: var(--cyan);
      font-size: 22px;
      font-weight: 900;
      line-height: 1;
    }
    .flow {
      display: grid;
      grid-template-columns: repeat(5, minmax(0, 1fr));
      gap: 8px;
    }
    .flow span {
      min-height: 46px;
      display: grid;
      place-items: center;
      text-align: center;
      padding: 8px;
      border: 1px solid rgba(39, 217, 255, .28);
      border-radius: 8px;
      background: rgba(39, 217, 255, .075);
      color: #dcf9ff;
      font-size: 11px;
      font-weight: 900;
      text-transform: uppercase;
    }
    .note-list {
      margin: 0;
      padding: 0;
      list-style: none;
      display: grid;
      grid-template-columns: repeat(4, minmax(0, 1fr));
      gap: 12px;
    }
    .note-list li {
      min-height: 74px;
      padding: 13px;
      border: 1px solid rgba(112, 243, 165, .22);
      border-radius: 8px;
      background: rgba(112, 243, 165, .07);
      color: #dfffee;
      font-size: 12px;
      line-height: 1.4;
    }
    footer {
      margin-top: 18px;
      color: var(--muted);
      font-size: 12px;
      text-align: center;
    }
    @media (max-width: 980px) {
      main { width: min(100vw - 28px, 1440px); padding-top: 22px; }
      header { grid-template-columns: 1fr; }
      .source-grid, .agent-grid, .stage-grid, .gate-grid, .note-list { grid-template-columns: 1fr; }
      .flow { grid-template-columns: repeat(2, minmax(0, 1fr)); }
      .band-head { display: block; }
      .band-head small { display: block; margin-top: 6px; text-align: left; }
    }
  </style>
</head>
<body>
  <main>
    <header>
      <div>
        <h1>${esc(source.title)}</h1>
        <p class="subtitle">${esc(source.subtitle)}</p>
      </div>
      <aside class="status-panel">
        <strong>${esc(source.audience)}</strong>
        <p>${esc(source.publicSafety.scope)} ${esc(source.publicSafety.artifactStatus)}</p>
      </aside>
    </header>
    <div class="layout">
      <section class="band">
        <div class="band-head">
          <span>Layer 3 Source Systems</span>
          <small>Source systems carry rules, records, contracts, and generator constraints behind the review layer.</small>
        </div>
        <div class="source-grid">${sourceSystems}
        </div>
      </section>
      ${agentGroups}
      <section class="band">
        <div class="band-head">
          <span>Four-Stage Agent Lane</span>
          <small>Every contracted role follows the same operating spine.</small>
        </div>
        <div class="stage-grid">${stages}
        </div>
      </section>
      <section class="band">
        <div class="band-head">
          <span>Review Gates</span>
          <small>Build movement is allowed only after the relevant gates clear or stop the work.</small>
        </div>
        <div class="gate-grid">${gates}
        </div>
      </section>
      <section class="band">
        <div class="band-head">
          <span>Review Flow</span>
          <small>The layer turns a request into a routed, scored, reviewable, and handoff-ready packet.</small>
        </div>
        <div class="flow">${flow}</div>
      </section>
      <section class="band">
        <div class="band-head">
          <span>Public Boundary</span>
          <small>What this artifact is and is not showing.</small>
        </div>
        <ul class="note-list">${notes}</ul>
      </section>
    </div>
    <footer>Static technical architecture artifact. Generated from a local source map; no private operating lanes or live-system data included.</footer>
  </main>
</body>
</html>`;
}

function readme() {
  return `# Agent Review Neural Interface

Static public-facing technical architecture artifact.

## What This Shows

- Layer 3 source-system pattern.
- Contracted agent and review roles.
- Four-stage agent operating lane.
- Review gates and flow.
- Public boundary notes.

## What This Does Not Show

- Private identity details.
- Foundation layer.
- Private doctrine material.
- Internal comparison artifacts.
- Private operating lanes.
- Client details or client status.
- Live-system access, credentials, or private paths.

## GitHub Pages

To publish:

1. Put this folder's contents at the root of a GitHub repository.
2. Commit index.html and this README.md.
3. In GitHub, open Settings -> Pages.
4. Set the source to the repository's default branch and root folder.
5. Use the Pages URL GitHub provides.
`;
}

function assertPublicSafe(rendered) {
  const normalized = rendered.toLowerCase();
  for (const term of forbiddenPublicTerms) {
    if (normalized.includes(term.toLowerCase())) {
      fail(`public output contains forbidden term: ${term}`);
    }
  }
}

validateSource();

const renderedHtml = html().replace(/[ \t]+$/gm, "");
const renderedReadme = readme().replace(/[ \t]+$/gm, "");

assertPublicSafe(renderedHtml);
assertPublicSafe(renderedReadme);

fs.mkdirSync(path.dirname(outputPath), { recursive: true });
fs.writeFileSync(outputPath, renderedHtml, "utf8");
fs.writeFileSync(readmePath, renderedReadme, "utf8");

console.log(`Generated ${path.relative(root, outputPath)} and ${path.relative(root, readmePath)}`);
