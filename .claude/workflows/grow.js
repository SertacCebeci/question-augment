export const meta = {
  name: 'grow',
  description: 'Grow the wiki for N rounds unattended: harvest (queries + arXiv sweep), select, fetch, read, review, apply, commit',
  whenToUse: 'Running many /grow rounds in the background, e.g. sweeping the horizon month by month',
  phases: [
    { title: 'Find', detail: 'harvest, explorer when the queue runs dry, selector, judge, fetch' },
    { title: 'Read', detail: 'one reader per work, then one reviewer per reading (pipelined)' },
    { title: 'Commit', detail: 'apply, check, commit' },
  ],
}

// args: { rounds: N }. The workflow reads no files: every deterministic step is `python3 tools/wiki.py …`, run by a
// runner agent that returns the command's one-line JSON; the agents write their outputs under .claude/runs/ themselves.
const ROUNDS = (args && args.rounds) || 1
const RUN = { type: 'object', properties: { code: { type: 'integer' }, stdout: { type: 'string' } }, required: ['code', 'stdout'] }
const PKG = { type: 'object', properties: { key: { type: 'string' }, files: { type: 'array', items: { type: 'string' } },
  queries: { type: 'array', items: { type: 'string' } }, nothing: { type: ['string', 'null'] } }, required: ['key', 'files'] }
const REV = { type: 'object', properties: { key: { type: 'string' }, notes: { type: 'array', items: { type: 'object',
  properties: { file: { type: 'string' }, verdict: { type: 'string', enum: ['pass', 'drop'] }, why: { type: 'string' } },
  required: ['file', 'verdict'] } } }, required: ['key', 'notes'] }

async function sh(cmd, label, ph, file) {
  const pre = file ? `First, with the Write tool, write exactly this JSON (verbatim, nothing added) to .claude/runs/round/_workflow.json:

${file}

Then run` : 'Run'
  const r = await agent(`${pre} exactly this one shell command from the repository root with the Bash tool (timeout 600000 ms), once. Do not run anything else; do not fix or retry anything.

${cmd}

Return {"code": <exit code>, "stdout": <the last line of its stdout, verbatim>}.`, { label, phase: ph, schema: RUN, model: 'haiku', effort: 'high' })
  if (!r) { log(`${label}: runner returned nothing`); return null }
  try { return JSON.parse(r.stdout.trim()) } catch (e) { log(`${label}: ${r.stdout.slice(0, 200)}`); return null }
}

const rounds = []
for (let n = 1; n <= ROUNDS; n++) {
  phase('Find')
  const h = await sh('python3 tools/wiki.py harvest', `harvest ${n}`, 'Find')
  if (!h) break
  if (h.explore) {
    const e = await agent('The search queue is nearly empty. Propose ten queries per your procedure; write {"queries": [...]} to .claude/runs/explore.json (Write) and return it.',
      { agentType: 'explorer', phase: 'Find', label: `explore ${n}` })
    if (e) await sh('python3 tools/wiki.py query add --input .claude/runs/explore.json --origin explore', `queue ${n}`, 'Find')
  }
  if (h.n > 0) {
    const s = await agent(`Batch file: .claude/runs/batch.json (${h.n} candidates, one per line). Judge every candidate; write the verdicts JSON to .claude/runs/verdicts.json and return the short summary.`,
      { agentType: 'selector', phase: 'Find', label: `select ${n}` })
    if (s) await sh('python3 tools/wiki.py judge --input .claude/runs/verdicts.json', `judge ${n}`, 'Find')
  }
  await sh('python3 tools/wiki.py fetch', `fetch ${n}`, 'Find')

  phase('Read')
  // keys only: a runner relaying the full listing truncates it; the text of a work is always meta/archive/<key>.txt
  const keys = (await sh(`python3 tools/wiki.py next | python3 -c "import json,sys; print(json.dumps([w['key'] for w in json.load(sys.stdin)]))"`, `next ${n}`, 'Read')) || []
  const reads = keys.map(key => ({ key, text: `meta/archive/${key}.txt` }))
  const done = await pipeline(reads,
    w => agent(`Key: ${w.key} · Text: ${w.text} (its title is in the text). Read per your procedure; write your package JSON to .claude/runs/round/${w.key}.package.json (Write) and return it.`,
      { agentType: 'reader', phase: 'Read', label: `read ${w.key}`, schema: PKG }),
    (pkg, w) => (pkg && pkg.files && pkg.files.length)
      ? agent(`Key: ${w.key} · Text: ${w.text} · Files: ${pkg.files.join(', ')} (git status tells new from enriched; an enriched note is judged by its git diff). Judge each per your procedure; write your verdict JSON to .claude/runs/round/${w.key}.review.json (Write) and return it.`,
        { agentType: 'reviewer', phase: 'Read', label: `review ${w.key}`, schema: REV }).then(rev => ({ pkg, rev }))
      : { pkg, rev: null })

  // the agents write their own files; this copy covers a reviewer (or reader) that returned its JSON without writing it
  const items = reads.map((w, i) => ({ key: w.key, package: (done[i] && done[i].pkg) || null, review: (done[i] && done[i].rev) || null }))

  phase('Commit')
  const a = await sh('python3 tools/wiki.py apply', `apply ${n}`, 'Commit', JSON.stringify(items))
  const c = await sh('python3 tools/wiki.py commit', `commit ${n}`, 'Commit')
  log(`round ${n}: ${c && c.message ? c.message : JSON.stringify(c)}`)
  rounds.push({ round: n, found: h.new, cursor: h.cursor, apply: a, commit: c })
  if (!c || !c.committed) { log(`round ${n} not committed — stopping`); break }
  if (!h.n && !reads.length) { log('nothing found, nothing to read — stopping'); break }
  if (h.sweep_done && !reads.length) { log('the sweep reached the end of its horizon and nothing is left to read — stopping'); break }
}
return rounds
