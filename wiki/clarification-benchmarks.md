---
description: "Ready-made benchmarks scoring whether and how well an LLM agent asks a clarifying question; the field's own measurements of the questioner's decision to consult a source."
aliases: ["clarification datasets", "clarifying-question benchmarks", "Fuse", "Framework for User-mediated Social Evaluation", "Fuse social-reasoning benchmark"]
sources: ["albattra-2026", "aliannejadi-2020", "ambig-ds", "arxiv-2601-06676", "arxiv-2604-27419", "bai-2026-mapsatisfybench", "chen-2026-appworld", "chen-2026-vitabench", "clamber-2024", "clareval", "clarq-llm-2024", "fang-2026-clarifycodebench", "ge-2026", "huang-2026", "huang-2026-clarify", "mi-2026", "min-2020", "nvidia-2025", "presacan-2026", "somasekharan-2026", "srinivasan-2026", "stoisser-2026", "su-2026", "suri-2026", "ta-2026", "tao-2026", "wang-2026-deskcraft", "wang-2026-turning", "wang-2026-when", "yin-2026", "zhang-2026-dlawbench", "zhao-2026-agent", "doi-10-48550-arxiv-2606-05112"]
---
# Clarification benchmarks

> Ready-made evaluation sets that score an agent on whether it asks — the
> only external measurements of a questioner's decision to consult a source.

## The map

| Benchmark | What it measures |
|---|---|
| **Qulac / ClariQ** (Aliannejadi et al. 2020) | Whether clarification is needed, and which question to ask, in conversational search |
| **AmbigQA** (Min et al. 2020) | [[efe-planning-as-variational-inference|Ambiguity]] detection plus disambiguated rewriting; over half of NQ-open questions are found ambiguous |
| **CLAMBER** (Zhang et al. 2024) | ~12K queries under an 8-category [[ambiguity-taxonomy|ambiguity taxonomy]]; two tasks — identify, then clarify |
| **When2Call** (Ross, Mahabaleshwarkar & Suhara, NVIDIA 2025) | A four-way choice: direct answer / tool call / follow-up question / unable to answer |
| **ClarQ-LLM** (Gan et al. 2024) | Task-oriented bilingual dialog, 31 task types, seeker agent scored by task success |
| **ClarifyBench** (Suri et al. 2026) | Multi-turn, tool-augmented, with LLM user simulation |
| **ClarEval** (2026) `[?]` | Code agents under injected instruction ambiguity |
| **Ambig-DS** (Stoisser et al. 2026) | Two independently analyzed diagnostic suites for code-based data-science agents — Ambig-DS-Target (51 DSBench tasks, prediction-target ambiguity) and Ambig-DS-Objective (61 MLE-bench tasks, evaluation-objective ambiguity); pairs each Full task with an Ambig. variant and an Ask condition (one scoped clarifying question against a truthful oracle), scoring unflagged misframing, one-shot recovery ($\Delta_{ask}$), and ask/don't-ask calibration with [[calibscore\|CalibScore]] |
| **OR-Clarify** (Ge et al. 2026) | Operations-research model formulation: withholds facts whose value changes the induced formulation structure; scores exact slot [[recovery-postulate|recovery]] (Core/All-Slot Exact over P0–P2 severity), silent assumptions, and turn/question cost under free-form and multiple-choice protocols |
| **Tri-Agent Framework** (Zhao et al. 2026) | Simulates the dialogue itself rather than scoring a fixed corpus: a Respondent Agent stands in for the user (including irrelevant or adversarial replies) and a third LLM, the Evaluator Agent, judges the transcript against a metric set — ambiguity-detection accuracy, question relevance/clarity, turn count, unsupported-input handling, and final-intent alignment |
| **HerHealthEval** (Albattra et al. 2026) | Multilingual (English/French/Modern Standard Arabic) women's-health communication; six matched register forms per case, one deliberately under-specified; scores concern classification, risk/triage [[calibration]], and clarification recall/specificity on the under-specified stress-test form |
| **MT-InfoSeek** (Huang et al. 2026) | Formalizes multi-turn information seeking as solving a k-underspecified [[k-underspecified-csp\|CSP]]; 9,006 task instances over mathematics, logic, biology, medicine and [[twenty-questions\|20 Questions]]; scores k-prediction, minimal-sufficient-set identification, and [[final-sufficiency\|final sufficiency]] separately from final answer accuracy |
| **AcCoRD** (Srinivasan et al. 2026) | User-agent collaboration under four preference dynamics (see [[preference-dynamics-taxonomy]]) in shopping and travel-booking simulators; scores Task Completion, Outcome Score, Perfect Outcome Rate and Task Score under vanilla ReAct vs. an uncertainty-guided prompting variant (UncReAct) |
| **Interactive Visual Grounding** (Wang & Rambow 2026) | Four controlled protocols (STATIC / FULL / PARTIAL / NONE) trading how much of a target's referring description is given upfront against how much a Matcher LVLM must recover through yes/no dialogue with a simulated Director; scores accuracy, question rate, confidence calibration and self-repair across eight LVLMs and four human-grounded visual domains |
| **UserToolBench** (Yin et al. 2026) | Profile-hidden personalized tool use: 10 persistent user profiles, 36 tool sets, 1,065 turns, 170 tools; evaluated LLMs see only interaction history, not the profile, and must choose a tool trajectory, including whether to ask for clarification or infer a missing constraint from history, for single-tool, multi-tool and lack-of-information (LOI) task types; scored by Exact trajectory accuracy and a Relaxed Task Completion accuracy |
| **AppWorld-UL** (Chen et al. 2026) | 516 agentic tool-use tasks built on the AppWorld environment (9 apps, 475+ APIs), perturbed so a task additionally requires clarification (underspecified goal), infeasibility-reporting or confirmation-seeking (high-cost action), individually or composed two/three at a time; scores Interactive Task/Scenario Goal Completion (I-TGC/I-SGC), which credit a trajectory only if it also asked every question in a per-task knowledge set K removed by the perturbation |
| **ClarifyCodeBench** (Fang et al. 2026) | Code generation under deletion-only injected ambiguity, built on LiveCodeBench v6 (419 tasks, 1–3 ambiguity points each, 10 taxonomy types); scores clarification quality directly with [[turn-discounted-key-question-rate\|Turn-discounted Key Question Rate]] (early coverage of annotated key questions) and [[optimal-round-adherence\|Optimal Round Adherence]] (closeness to the optimal round count), alongside pass@1 under four input settings (Full / Ambiguous / Interactive-Clarified / Oracle-Clarified) |
| **REAL-Bench** (Mi et al. 2026) | Embodied vision-driven mobile-manipulation agent, no oracle perceptual APIs; one of its four task families (Simulator-User-Loop, SUL, 65/241 tasks) scores an ask-or-act decision under visually and instructionally ambiguous goals against a simulated human-in-the-loop user, not a text-only clarification decision |
| **RegretBench** (Ta et al. 2026) | Free-form multi-turn dialogue under a hidden-intent clarification interaction graph (CIG); scores a whole-dialogue reward (intent-match utility minus token cost minus a penalty for unsupported/redundant/premature clarification) and a benchmark-relative regret against a semantic reference [[planner-dynamic-stopping|planner]], rather than final accuracy alone |
| **MapSatisfyBench** (Bai et al. 2026) | 500 behavior-grounded map-service instances; ground truth built by a [[restore-identify-filter|restore-identify-filter]] procedure over pre-query context, spatio-temporal setting and post-query behavior; scores Explicit-factor Completion (ECR), Implicit-factor Satisfaction (IISR), Tool Selection (TS), Information Faithfulness (IFS), Interaction Efficiency (Eff), and composite Accepted-response Probability (AR = ECR·IISR) and Satisfaction Efficiency (SES = AR·Eff) |
| **Clarify-Then-Search** (Huang et al. 2026) | Deep search on 518 Baidu-derived underspecified queries; a closed-book two-phase protocol (User Answerer and Rewriter each see only part of the hidden intent) isolates the Clarifier's own contribution across a clarification budget $k\in\{1,2,3\}$; scores end-to-end utility with [[weighted-nugget-recall\|weighted nugget recall]] (`restore_score_100`) against a static, evidence-grounded gold nugget set archived from one oracle deep-search run |
| **DiscoBench** (Tao et al. 2026) | Deep search under multi-step ambiguity propagation: 211 samples, 463 ambiguity instances across 11 domains and four ambiguity types (Entity / Version / Criteria / Factual Inaccuracy), decomposed into an ordered sequence of checkpoints; scores end-to-end accuracy, checkpoint pass rate, ambiguity-detection accuracy/F1, clarification accuracy and clarification-to-advance rate, and cost (ask turns, tool-use turns, tokens) under Neutral vs. Guided prompting |
| **DeskCraft** (Wang et al. 2026) | 538-task, long-horizon desktop-GUI benchmark (18 agents, 11 professional applications); interactive tasks are built from a composable mid-turn/post-turn trigger protocol (see [[mid-turn-post-turn-protocol]]) and success is scored on standard vs. interactive splits, and separately by human-in-the-loop collaboration mode (Ask, Interruption, Correction, Progressive Refinement, Requirement Change) |
| **DLawBench** (Zhang et al. 2026) | Multi-turn legal consultation: 461 court-opinion-grounded cases (Chinese and U.S. law), replayed under four client narrative styles (Cooperative / Dependent / Withdrawn / Adversarial); scores Fact Coverage and Inquiry (information gathering), Fact Resolution and Issue Resolution (legal reasoning), and Fidelity (claim support) separately, so *whether the right follow-up question is asked* is scored apart from whether an elicited fact is later used correctly |
| **VitaBench 2.0** (Chen et al. 2026) | Long-term personalized-agent task sequences (56 users, 2,000+ curated preferences) interleaved with proactive tasks that withhold information the agent must recognize as missing and query the user or explore the environment for; scores the proactive subscore separately from ordinary personalization accuracy, across Full Context, Agentic Memory and RAG Memory settings |
| **Safe-Psych** (Presacan et al. 2026) | 1,048 real-world psychiatric clinical notes, each segmented into up to five sections and revealed incrementally; psychiatrist-derived, section-level ground truth converts an earliest-sufficient-section judgment into stepwise DIAGNOSE/CLARIFY/ABSTAIN labels; scores under-[[abstention]] (diagnosing before evidence is judged sufficient) separately from over-abstention (abstaining once it is), plus clarification-seeking at the first, most-uncertain stage and the accuracy of premature vs. on-time diagnoses |
| **SciConvBench** (Somasekharan et al. 2026) | Multi-turn clarification for scientific task formulation across four computational-science domains (fluid mechanics, solid mechanics, materials science, PDEs); each instance perturbs a clean 9-component task ontology (objective, geometry, governing model, properties, boundary/initial conditions, numerical controls, outputs, tool settings) into a request with planted missing (disambiguation) or conflicting (inconsistency) information, and scores Final Resolution Rate (FRR), Conversation-Grounded Resolution Rate (CGRR) and Silent Resolution Rate (SRR) both per case and per ontology component |
| **SpecBench** (Wang, Han & Xu 2026) | 50 software-project intents crossed with 48 LLM-simulated personas; Task 1 scores an 80-item design-preference checklist predicted under a fixed query-round budget (T=5 or T=10) against the persona's own answers; Task 2 scores a collaboratively drafted 9-section spec sheet on a five-criterion LLM-judge panel (coverage, precision, consistency, insight, readability); both tasks report accuracy/quality jointly with query count and an early-submission rate |
| **InteractWeb-Bench** (Wang et al. 2026) | Multimodal interactive website generation under four user personas (P-MIN, P-RAM, P-INT, P-CON) grounded in requirement-engineering defect taxonomies; a unified Clarify/Implement/Verify/Submit action space lets the agent interleave asking with acting; scores a constraint-slot-weighted Task Completion Rate (TCR) and Hallucination Rate, plus an Intent Alignment Score and Clarification Hit Rate on the interaction itself |
| **IDRBench** (Feng et al. 2026) | Interactive deep research: 100 DeepResearch Bench query-report pairs (22 fields, English/Chinese), queries compressed 10%-90% so room for clarification exists; each model runs once autonomously and once interactively under a shared stage-wise budget (1 / 3 / 1 clarification turns for Planning / Research Loop / Generation) with an LLM feedback policy that answers from the paired report as private context; scores Report Alignment (report similarity, sentence/paragraph/chunk F1, LLM aspect coverage) as the interactive-minus-autonomous change, plus Interaction Cost in turns and tokens |

## The common finding

Elicited ambiguity judgments are far above the rate at which a model
actually asks.

- **Su & Cardie (2026)**, 10 models (GPT-4/4.1 family, Claude 3.5, Qwen 2.5)
  on AmbigQA: asked explicitly, most models label the ambiguous class
  correctly 60–80% of the time; in the plain QA setting the answer rate is
  above 95% and a clarifying question appears in **under 5% of responses to
  ambiguous questions** (Claude-3.5-Haiku highest at 4.9%; GPT-4.1 0.3%).
  Supplying retrieved context *lowers* the [[query-clarification-rate|clarification rate]] further
  (Haiku 4.9% → 2.4%).
- **When2Call (2025)**, four-way choice: the best community tool-calling
  models score ~F1 34 and GPT-4-Turbo 64.6 F1 under LLM-as-judge; the authors
  report unwanted tool calls on many items where a follow-up question is the
  correct answer, and tool-hallucination rates of 9–67% — the model fabricates
  a parameter rather than request it.
- **ClarQ-LLM (2024)**: LLM seeker agents complete 50.8% (GPT-4o) and ~60%
  (Llama-3.1-405B) of tasks against 85% for human seekers, where success
  depends on gathering the missing facts by asking.
- **OR-Clarify (2026)**: no tested model exceeds 60% Core Exact and all
  retain substantial silent assumptions; a stopping audit flags 40.6% of
  free-form runs as premature even though the agent declared readiness in
  98.8% of them — the bottleneck is knowing when enough has been recovered,
  not recognising that something is missing.[^c7]
- **Tri-Agent Framework (2026)**: the judge is a model, not a label — the
  Evaluator Agent's scores on a synthetic supply-chain dialogue set
  correlate with the authors' own ratings at r = 0.87, and the evaluated
  Question Clarifying Agent (Claude 3.5 Sonnet) reaches an Ambiguity
  Detection Accuracy of 0.92, a Question Relevance score of 4.48, and an
  Overall Task Success rate of 87% — the first entry in this table where the
  scoring itself, not just the questioner, is an LLM validated against
  humans.[^c8]
- **HerHealthEval (2026)**: a zero-shot multilingual model reaches 0.856
  clarification recall on English deliberately under-specified cases; the
  same benchmark then measures what happens to that rate under domain
  adaptation (see [[adaptation-suppresses-clarification]]) rather than
  stopping at a single elicited number, the first entry here to track the
  rate across a training intervention instead of across models.[^c9]
- **MT-InfoSeek (2026)**: on multiple-choice k-prediction, models rarely
  call a problem fully specified (0.6±0.8% predict k=0) but accuracy falls
  below 0.5 for k≥2, and errors are asymmetric — at k=2, where the choice
  set is balanced above and below the truth, models predict a smaller k
  more than 4× as often as a larger one, so recognition of missing
  information does not translate into a calibrated estimate of how much is
  missing.[^c10]
- **AcCoRD (2026)**: across five frontier LLMs, prompting the agent to
  declare `<friction>` or `<no_friction>` and resolve preference ambiguity
  before every action (UncReAct) does not reliably improve elicitation —
  weaker models (Llama-3.1-70B, DeepSeek-V3.2) over-ask under the
  instruction and exhaust their dialogue budget, dropping Task Score, while
  GPT and Claude models see only marginal or negative Task Score changes;
  the same benchmark also finds models satisfy hard/soft underspecified
  preferences well (outcome score 0.7–0.95) but fall furthest on
  unachievable and triggered preferences, the two dynamics that need
  negotiation or proactive disclosure rather than a direct question.[^c11]
- **Interactive Visual Grounding (2026)**: all eight tested LVLM matchers
  ask more questions as the upfront description shrinks (NONE > PARTIAL >
  FULL > STATIC = 0 by design), but every one of them scores below its own
  no-interaction (STATIC) baseline under NONE despite asking the most
  questions there — the protocol demanding fully question-driven grounding
  is the one every model performs worst on, so a rising question rate does
  not track a rising ability to recover the missing target information.[^c12]
- **UserToolBench (2026)**: across nine tool-use LLMs, accuracy on
  lack-of-information (LOI) turns — deciding whether to ask for
  clarification or infer a missing constraint from history — does not track
  a model's ordinary single-tool (ST) accuracy. GPT-5.4 reaches the highest
  LOI exact accuracy (42.22%) despite the lowest ST exact accuracy (40.22%)
  of the six frontier models tested, while Qwen 3.6 Plus scores highest on
  ST (58.02%) but falls to 19.52% on LOI — the authors read this as
  missing-constraint handling needing uncertainty calibration in addition
  to preference retrieval, since over-inference and excessive clarification
  are both scored as errors.[^c13]
- **AppWorld-UL (2026)**: on 516 user-in-the-loop tool-use tasks, the
  best system (Code Agent, Claude Opus 4.7) reaches only 48.6% I-TGC /
  30.2% I-SGC overall, dropping to 35.7% I-TGC / 21.3% I-SGC on the harder
  compositional subset where two or three interaction types (clarification,
  infeasibility-reporting, confirmation-seeking) are required in the same
  task; interaction quality and downstream success are strongly linked —
  on tasks the agent completes, it asks with 100% recall and 80–91%
  precision against the knowledge set K removed by the perturbation, but on
  failed tasks recall falls to 37–40% and precision to 40–47%.[^c14]
- **ClarifyCodeBench (2026)**: across six LLMs, clarification quality is
  low and close together on both new metrics — the best model
  (DeepSeek-V3.2) reaches TKQR 0.30 and ORA 0.50, most others below
  0.30/0.35 — and the weakness propagates downstream: pass@1 under the
  ambiguity-resolution pipeline is 7.8–19.8 points below pass@1 under the
  complete requirement for every model. Enabling "thinking" raises pass@1
  under complete requirements (e.g. Claude-Sonnet-4.5 48.8→50.0, GPT-5 to
  52.5) but does not raise TKQR or ORA and can lower pass@1 under ambiguity
  (Claude-Sonnet-4.5 38.2→34.3) — the reasoning budget that improves code
  synthesis does not transfer to the asking step.[^c15]
- **REAL-Bench (2026)**: on the interaction-heavy SUL split, a
  Qwen3-VL-8B mobile-manipulation policy reinforcement-trained with a
  reward that pays its `ask` action only within a difficulty-conditioned
  budget ($B_{ask}\le3$, see [[query-budgeted-social-reward]]) reaches
  56.9% success, up from 36.9% for the same architecture after supervised
  fine-tuning alone, and above the strongest zero-shot commercial VLM
  baselines tested — unlike the text-only entries above, the deficit here
  is closed by training the ask decision into the policy with reward
  rather than by better prompting or a labeled information-gain signal.[^c16]
- **RegretBench (2026)**: across 16 models on open-domain QA, final
  success rate does not predict whole-dialogue reward or regret — K2Think
  V2's success rate is "relatively high" but its "reward is strongly
  negative due to excessive turns, high costs, and substantial penalties,"
  while GPT-4.1, a non-reasoning model, "achieved a nearly optimal
  whole-dialogue reward and the lowest normalized regret of any model, only
  surpassed by Gemini 3.1 Pro" — direct confirmation that "models with
  similar accuracy can differ substantially in efficiency, robustness to
  user behaviors, and stopping decisions."[^c17]
- **MapSatisfyBench (2026)**: across 12 LLM map agents, explicit-task
  completion is comparatively strong (best ECR 0.9272, GPT-5.3) but
  implicit-need recovery is not — the best IISR is 0.7170 (Claude-4.6-opus)
  and tool selection for recovering evidence stays low across every model:
  "TS ranges from 0.2859 to 0.4942, and even the best model on this metric,
  Claude-4.6-opus, remains below 0.50"; the authors' own tool-call
  inspection finds "all models invoke the profile-related tool at a
  relatively low rate," and turn efficiency is below the reference budget
  for every agent (Eff < 0.5) — evaluated agents lean toward asking rather
  than retrieving evidence a [[restore-identify-filter|restore-identify-filter]]
  audit shows was already recoverable.[^c18]
- **Clarify-Then-Search (2026)**: across seven Clarifiers, all improve over
  the no-clarification baseline at $k=1$ (mean `restore_score_100` 19.434 →
  22.527–26.474, every 95% CI strictly above zero) and larger budgets
  ($k=2,3$) yield further gains, but a low-yield failure mode persists
  regardless of budget: region-only clarification questions (asking for a
  city or province) draw an "unknown" answer 75.0–86.9% of the time under
  the closed-book protocol, yet models ask them at rates from 14.3%
  (Kimi) to 49.8% (Gemini) — a plausible, topical question is not the same
  as a useful one.[^c19]
- **DiscoBench (2026)**: across nine frontier models under a checkpoint-level
  protocol, the SearchThenAsk strategy (ask when a checkpoint is ambiguous)
  reaches a mean 93.4% checkpoint pass rate, against 56.5% for DirectGuess
  and 51.9% for SearchHeavyGuess (repeated retrieval, then guess without
  asking) — SearchHeavyGuess *underperforms* DirectGuess despite more
  retrieval steps, so the failure is not missing the ambiguity but failing
  to escalate retrieval uncertainty into a clarification act; separately,
  Guided prompting (an explicit reminder that ambiguity may exist) lifts
  mean detection F1 from 45.3% to 64.9% while mean end-to-end accuracy
  rises only from 28.6% to 33.7%, so better detection under-transfers to
  task success.[^c20]
- **DeskCraft (2026)**: across 18 agents on 538 long-horizon desktop-GUI
  tasks, the best model (GPT-5.4) reaches 31.6% on standard tasks and drops
  to 27.6% on the interactive split; grouped by human-in-the-loop
  collaboration mode, Ask-style tasks — where the agent must use its own
  `call_user` channel to request missing information — have the lowest
  success rate of any mode for both tested models (GPT-5.4, Kimi-K2.6), and
  the authors read this as agents proceeding on an initial guess rather
  than as a missing capability: "exposing an Ask channel is not sufficient;
  current agents often proceed without requesting the missing information
  needed for successful execution."[^c21]
- **DLawBench (2026)**: across 26 LLMs on multi-turn legal consultation,
  the best model still leaves the *asking* sub-skill weaker than the
  *mentioning* sub-skill — GLM-5.1 covers 0.766 of annotated facts (Fact
  Coverage) but reaches only 0.360 Inquiry, "showing that a model can cover
  many facts in the memo while still missing key factual follow-up and
  verification actions"; even the top model (GPT-5.5) reaches only 0.576
  Inquiry against 0.837 Fact Coverage, and every model's Elicitation and
  Resolution scores fall further under the Dependent and Withdrawn client
  styles — see [[legal-consultation-paradox]].[^c22]
- **VitaBench 2.0 (2026)**: across model families under the full-context
  setting, proactive-task performance is consistently lower than the same
  models' ordinary personalization performance — Claude 46.0 vs. 27.4,
  DeepSeek 44.1 vs. 27.8, GLM 36.4 vs. 19.3 — and the authors read this as
  "current agents often fail to recognize when their knowledge is
  insufficient, and instead proceed with incomplete information rather than
  initiating clarification."[^c23]
- **Safe-Psych (2026)**: across nine LLMs under Full Information -
  Abstention Aware prompting, "under-abstention exceeds 60% for most
  models, indicating that many systems still diagnose despite insufficient
  evidence even when explicitly permitted to abstain," with "Gemma-3-27B
  the most extreme case, diagnosing over 90% of insufficient cases, whereas
  Mistral-3.1-24B reduces under-abstention but abstains on nearly 60% of
  sufficient cases" — lower under-abstention trades for higher
  over-abstention rather than eliminating error. Under neutral (no
  abstention instruction) sequential prompting, clarification-seeking at
  the first, most-uncertain stage is rare and uneven: "Mistral-3.1-24B and
  Claude-Opus-4.6 request clarification in over half of cases, but GPT-5.4
  does so in only about one quarter, and Gemini-Flash-2.5 and Med42-v2-8B
  in fewer than 10%," and premature diagnoses — made before the section the
  psychiatrist annotators judged sufficient — are less accurate than
  on-time ones.[^c24]
- **SciConvBench (2026)**: under the same model (Gemini 2.5 Pro) and
  protocol, resolution rate drops from 86.1% on a filtered subset of
  CLAMBER (general-domain) to as low as 18.2% on SciConvBench's
  fluid-mechanics disambiguation split; across five frontier LLMs, even the
  best model resolves only 52.7% of fluid-mechanics disambiguation cases,
  and every model exhibits a non-zero gap between Final Resolution Rate and
  Conversation-Grounded Resolution Rate — averaging 8.2 percentage points
  on disambiguation and 14.7 on inconsistency resolution, i.e. silent
  guessing or unannounced repair is more common when resolving a planted
  conflict than when eliciting a missing fact.[^c25]
- **Ambig-DS (2026)**: across five code-based agents (efficient to
  frontier), agents "commit to the wrong prediction target on 39–63% of
  ambiguous tasks — and do not flag the ambiguity in any of them," and a
  trace/answer audit shows "user-overridable flagging in the final answer
  never exceeds 4% even when traces acknowledge the ambiguity" — silent,
  evaluator-accepted misframing rather than an execution failure. Allowing
  exactly one scoped clarifying question against a truthful oracle
  recovers much of the resulting loss, "with ∆ask reaching +0.20 on
  Ambig-DS-Target and +0.09 on Ambig-DS-Objective," "essentially clos[ing]
  the Ambig.–Full gap on Objective but leav[ing] a residual gap on
  Target" — yet "no model–prompt-policy combination we test achieves both
  calibrated asking on ambiguous tasks and restraint on fully-specified
  ones" (see [[calibscore|CalibScore]]): the two ambiguity axes are
  analyzed independently and never pooled.[^c26]
- **SpecBench (2026)**: across three CLI coding-agent baselines (Claude
  Code, Cursor CLI, Gemini CLI), the two ways a fixed query budget goes
  wrong are asymmetric and separately measured. Gemini CLI has the highest
  early-submission rate (17% vs. 0–3% for the others) and its "prediction
  accuracy on the checklist questions degrades from T = 0 to T = 5 and T =
  10" — under-asking that actively hurts it. Claude Code and Cursor CLI
  instead "often exhaust the full question budget, querying the user
  whenever any ambiguity remains," which on Task 2 "becomes a less
  efficient strategy" as returns diminish — over-asking that the checklist
  task does not penalize but the spec-drafting task does. An
  ensemble-gated query strategy ([[simulated-user-consensus-filtering]])
  avoids both: it "queries the user significantly fewer times than other
  agents, while still achieving the highest evaluation scores."[^c27]

## What this means

The measured deficit is in **acting**, not in the classifier: a system that
scores well on ambiguity detection can still ask in under 5% of the cases
where it should. Treating a low ask-rate as evidence that the questioner
priced the cost of asking ([[question-budgets]]) is therefore unsafe — these
numbers are produced without any such pricing. The sourced account of *why*
the rate is this low is [[preference-signal-against-asking]]; When2Call's
authors point the same way, reporting that a helpfulness training step after
tool-calling SFT compounds the over-eagerness to act. AcCoRD adds that the
deficit survives an explicit instruction to reason about the uncertainty
before acting — a prompt-level fix is not sufficient on its own. Interactive
Visual Grounding adds a case where the deficit is the opposite shape: models
do ask, and ask more as information shrinks, yet the extra questions do not
convert into the accuracy a purely quantity-based account of question value
would predict. UserToolBench adds that the deficit is not a single scalar
per model: a model's rank on ordinary tool-use accuracy predicts nothing
about its rank on deciding whether to ask, so a system that benchmarks well
on task completion can still be the weakest at the specific judgment this
wiki's stall 2 concerns. AppWorld-UL adds that the gap is not confined to
whether the agent asks at all: its interaction recall/precision pair shows
the same agents both under-ask and over-ask depending on the task, and both
failure directions coincide with task failure rather than one dominating.
ClarifyCodeBench adds that even where the deficit is measured directly, as
an ordering and stopping quality rather than a binary ask/don't-ask
decision, more inference-time computation does not close it. REAL-Bench adds
a case where the deficit is closed rather than measured: an RL reward on the
ask action itself, not a better classifier or prompt, raises success on the
interactive split by 20 points, at the cost of every limit named on
[[query-budgeted-social-reward]] — one simulator, one budget, one frozen
vision encoder. RegretBench adds that even among models that do ask, final
accuracy is the wrong lens on the deficit: two policies can reach similar
success rates while one pays for it in turns, cost and penalized
(unsupported, redundant or premature) clarification that a single accuracy
number hides. MapSatisfyBench adds a case where the deficit is on the other
side of the trade named by [[restore-identify-filter]]: agents under-use the
tool that would let them infer instead of ask, so the observed low ask-rate
elsewhere on this page cannot be read as evidence the questioner already
prices recovery-from-evidence against asking — one benchmark's agents mostly
do neither well. Clarify-Then-Search adds a case where volume of asking is
not the deficit at all — every model gains from asking, monotonically in
budget — and the deficit instead sits inside question *choice*: models keep
spending a sizeable share of their questions (up to half, for Gemini) on the
one axis (region) least likely to be recoverable under a closed-book answerer.
DiscoBench adds a case where the alternative to asking is not inaction but
*more retrieval*: continued search without escalating to a question is
measurably worse than a same-effort guess, so the deficit here is not too
few tool calls but tool calls substituting for the act of asking. DeskCraft
adds a long-horizon, execution-embedded case: the Ask channel sits inside a
50+-step GUI workflow rather than at a single decision point, and it is
still the lowest-scoring collaboration mode of all — so the deficit
documented elsewhere for short-form QA and bounded tool calls persists
unchanged when the surrounding task is long-horizon and physically
executed, not just read and answered. DLawBench adds a domain (professional
consultation) where a model can ask enough to cover most facts and still
fail the narrower asking skill (case-specific follow-up and verification),
and where the deficit worsens exactly when the client is least forthcoming
rather than staying constant across users. VitaBench 2.0 adds a case wrapped
inside a long-term, memory-mediated personalization pipeline: the same
models score higher at retrieving and using an already-available preference
than at recognizing that a conditional preference cannot yet be resolved and
must be asked about, so the deficit survives being embedded in a multi-task,
multi-session agent rather than isolated as a single-turn decision.
Safe-Psych adds that where the field so far measures a single ask-or-not
rate, the two errors an "ask more" fix can produce are separable and trade
against each other: prompting a model to be abstention-aware does not close
the deficit, it moves error mass from unsafe premature commitment toward
missed diagnoses, so a benchmark that reports only one of under- or
over-abstention cannot say whether a proposed fix reduced the deficit or
relocated it. SciConvBench adds a domain-transfer case: the same model and
protocol that resolves 86% of a filtered general-domain benchmark's
ambiguity falls to 18% on a scientific task-formulation benchmark, so the
deficit measured elsewhere for short-form and agentic settings holds, more
sharply, once the domain requires scientific groundedness rather than
general-purpose disambiguation — and its FRR–CGRR gap shows the silent
half of the deficit is worse for resolving a stated conflict than for
eliciting an unstated fact. Ambig-DS adds a case where the missing-question
deficit is measured causally rather than only correlationally: an idealized
one-shot oracle that supplies exactly the missing framing variable recovers
most of the induced loss, so on this benchmark's evidence the degradation
is attributable to missing framing information rather than to a harder
underlying prediction problem — but the same agents cannot reliably tell,
from the prompt-data pair alone, which tasks warrant spending that question.
That gap is this note's claim, not a source's. SpecBench adds that the two
failure directions surveyed above can appear in the same field of baselines
at once rather than trading off across models: one CLI agent under-asks and
is actively hurt by the questions it does ask, while the other two over-ask
on a task that does not reward it, and an ensemble-gated strategy that
answers most dimensions from simulated agreement, not from the user, beats
all three on accuracy while asking the fewest questions.
- **InteractWeb-Bench (2026)**: across nine MLLM-based website-generation agents given an explicit `Clarify` action, the deficit is not comprehension — an Intent Alignment Score judging whether the agent's stated reasoning matches ground truth stays above 3.9/5 for every model — but conversion into a question: a Clarification Hit Rate scoring whether a `Clarify` action actually surfaces a hidden constraint stays under 40% for all of them, and models close the gap by generating more code instead of asking, since "models tend to compensate for missing requirements through aggressive generation rather than iterative clarification, resulting in increased code size and higher hallucination rates." See [[blind-execution]].[^c28]
- **IDRBench (2026)**: across seven LLMs on long-horizon deep research, a clarification opportunity helps on average (all five alignment measures rise for every model, mean gain 6.39 points) but not reliably per task: interaction improves the report in 74.4% of model-task pairs and degrades it in 19.9%, so benefit depends on what is asked and how the reply is used.[^c29] Models rank differently on autonomous score (GPT-5.1 75.59), interactive score (Claude-Sonnet-4.5 80.47) and gain (Llama-4-Maverick +10.96), so interactive ability is not read off autonomous strength.[^c30] In a timing ablation on two models, every single-stage setting beats no interaction, Planning-only is the strongest single stage, and all-stage is highest overall (my reading: early framing questions carry most of the value); Llama-4-Maverick's Planning-only slightly beats all-stage on sentence and chunk F1.[^c31] The design is the paired autonomous-vs-interactive trajectory under one budget, scoring the change in alignment with the paired report, not final-answer accuracy.
- **MedSP1000 (2026)**: 1,638 standardized-patient cases in which a clinician model must elicit history and test results from a patient agent and an environment controller that hold them; rubric items are checked over the whole encounter. The best of seven models "completes only 60.4% of expert-defined rubric items," and a best-of-5 or multi-agent consultation on that model moves it by less than one point.[^c32] "Additional test-time scaling does not improve interactive performance."[^c33] See [[closed-loop-standardized-patient-evaluation]].

## Limits

- The pitfall claim above assumes the entries in the table are
  representative of the class; it rests on a table the wiki assembled, not on
  a survey, and a benchmark published since would falsify it cheaply.
- Ask-rates are measured against labels of when a question was *needed*;
  those labels are annotator judgements, and Su & Cardie use an LLM judge to
  classify responses into answer / refusal / clarification.
- Su & Cardie run on AmbigQA only: the observed rate is a rate for
  short-form open-domain QA, not for agentic or long-horizon tasks.
- **ClarEval** (arXiv 2603.00187) is still `[?]` in sources: the arXiv
  listing is recovered but its row here rests on the abstract, not a
  reading of the paper. **Ambig-DS** (arXiv 2605.09698,
  Stoisser et al. 2026) is now read in full: its Ask
  condition is an idealized, always-available oracle read as "an upper
  bound on recoverable performance, not a deployment estimate," and its
  intended-framing label θ⋆ is "a protocol scoring convention rather than
  the unique correct reading," so the recovery numbers above bound what a
  perfect answerer would yield, not what a real stakeholder would.
- Results move with model generation and prompt; CLAMBER shows chain-of-thought
  and few-shot prompting changing identification accuracy in both directions.
- OR-Clarify's "formulation-critical" label is constructed by the
  benchmark's own masking procedure over one fixed source collection (100
  cases, one domain), not an independent ground truth.
- The Tri-Agent Framework's r = 0.87 is the Evaluator Agent against the
  paper's own authors' ratings on one synthetic domain with one evaluated
  model; it is not an independent-annotator agreement study and has not been
  replicated on a public dataset. `[?]` — read from the arXiv listing and its
  web rendering, not an archived text extract.
- HerHealthEval's clarification target is mechanical (the deliberately
  under-specified form is positive, all others negative), not a
  clinician-adjudicated judgement of real need — it tests recognition of an
  injected information gap, not clinical necessity.
- MT-InfoSeek's four structured domains (Logic-Q-MT, GSME-Q-MT, GeneReg-MT,
  ClinGuide-MT) give the model a predefined, finite set of queryable
  variables; only its fifth domain, [[twenty-questions|20 Questions]], tests open-ended natural-
  language question generation, so most of its results describe selection
  among known variables, not formulation of a new one.
- AcCoRD's outcome scoring for shopping uses an LLM judge (Claude-Sonnet-4.5)
  against natural-language preference criteria; travel-booking scoring is
  deterministic, so the two halves of the benchmark are not equally
  independent of a model judge.
- Interactive Visual Grounding's Director is itself a fixed LLM (GPT-5.4)
  simulating the human who provided the reference description, not a human
  in the loop; the paper reports comparable results under an alternative
  Director as a sensitivity check, but the main table's accuracy numbers are
  model-vs-simulated-model, not model-vs-human dialogue throughout.
- UserToolBench's LOI correctness credits clarification (under Exact
  accuracy) only when the missing constraint is judged "unrecoverable from
  history" by the benchmark's own reference-construction pipeline, which had
  the profile visible; the Relaxed metric credits clarification or inference
  only when a human-verified reviewer judged the constraint "unambiguously"
  recoverable. Both rest on one verified reference trajectory per instance,
  not a multi-reference or severity-weighted ground truth, and the paper
  itself names this an open problem.
- AppWorld-UL's task perturbations (infeasible, underspecified,
  confirmation-requiring, and their compositions) were all manually
  designed and verified by the paper's authors from 34 base AppWorld
  scenarios (102 scenarios, 516 tasks total), not drawn from naturally
  occurring user requests; and its simulated user is itself an LLM, so
  I-TGC/I-SGC also measures how well an agent models a synthetic user's
  response distribution, not a human one.
- ClarifyCodeBench's ambiguity is injected by deletion from a complete
  specification (LiveCodeBench v6) by two PhD annotators, not naturally
  occurring underspecification, and the LLM-as-judge that matches a model's
  question to the annotated key question is itself a model (GPT-4o), not a
  human rater.
- REAL-Bench's simulated user is itself an LLM (gemini-3-flash) with a
  task-specific profile restricting it to objects already in the scene, not
  a human in the loop; and its 56.9%/36.9% comparison is one training
  ablation on one benchmark family, not a cross-benchmark or cross-domain
  replication.
- RegretBench's regret is benchmark-relative, not an oracle measure: the
  reference planner shares the benchmark's own closed semantic [[possible-worlds|state space]],
  observation model, cost function and horizon with the scored policy, and
  its CIGs depend on a semantic parser and a persona-conditioned LLM
  simulator (GPT-5 Nano) rather than human interlocutors — a parsing or
  simulation error can mark a useful clarification unsupported.
- MapSatisfyBench's implicit-factor set is annotated by an LLM
  judge-and-human-review pipeline over one company's anonymized map-service
  logs (AMAP), not an independently collected corpus; its restore step uses
  post-query behavior h⁺ that the evaluated agent never sees, so the ground
  truth is built with privileged information the scored agent could not have
  had.
- Clarify-Then-Search's gold nugget set is a single archived WebDancer run
  per query, not a human-curated reference, and its coverage judge is
  itself an LLM (ERNIE-4.5-Turbo); the closed-book Rewriter never sees the
  intent query, so a Clarifier that under-asks cannot be rescued by the
  Rewriter guessing correctly, but this also means the benchmark cannot
  separate "the Clarifier asked a bad question" from "the closed-book User
  Answerer withheld an answerable fact."
- DiscoBench's four ambiguity types are grounded only in objective
  question-answering scenarios; subjective preference ambiguity is out of
  scope by the authors' own statement. Its interaction partner is an LLM
  user simulator (Gemini-3-Flash-Medium) with progressive clue disclosure,
  not a human, so its checkpoint-level accuracy numbers describe agent-vs-
  simulated-user behaviour, and the DirectGuess/SearchHeavyGuess/
  SearchThenAsk comparison is a forced three-way protocol split, not a
  policy choosing freely among the three on each checkpoint.
- DeskCraft's interaction triggers (`agent_ask`, `step_count`, `agent_done`)
  are authored and scripted for reproducibility: `step_count` is a fixed
  proxy for "user-initiated interruption," not a naturalistic interruption
  signal, and both the mid-turn responses to `agent_ask` and the post-turn
  follow-ups are produced by an LLM user simulator conditioned on the
  authored scenario, not by a human interlocutor; the two collaboration-mode
  numbers cited above (GPT-5.4, Kimi-K2.6) are two models among 18
  evaluated.
- DLawBench's Inquiry and Issue Resolution rubrics are LLM-judge scored
  (three-judge median panel, or two-judge mean after same-vendor recusal);
  human validation checks only 422 sampled rubric items (95.5% combined
  agreement, panel-human Cohen's κ = 0.848), not the full 3,411 + 3,348
  rubric set, and its client simulator is itself an LLM conditioned on
  annotated beliefs and a style prompt, not a human client (96.9%
  segment-level style-recovery accuracy from human annotators is the only
  human check on the simulator itself).
- VitaBench 2.0's user preferences, interaction histories and proactive
  tasks are programmatically constructed by the authors, not drawn from
  naturally occurring under-specification; both the user simulator and the
  evaluator are the same fixed LLM (gpt-4.1-2025-04-14), so the proactive
  subscore is one model's judgment of another model's dialogue with a third
  copy of itself, and Avg@4/Pass@4/Passˆ4 are computed at temperature 0.0
  over four runs of one fixed scenario set, not a cross-benchmark or
  cross-population replication.
- Safe-Psych's ground truth is a psychiatrist-annotated [[sufficient-statistic|sufficiency]]
  judgement on anonymized, LLM-translated (Romanian to English) clinical
  notes, not the original treating clinician's diagnosis, and the original
  Romanian notes are not released; annotator agreement on sufficiency is
  moderate by Cohen's κ (0.593, skewed 81%/9%/10% class split) though high
  by Gwet's AC1 (0.874); the action-label pipeline runs through an
  LLM-assisted judge (GPT-5.4) validated against human majority vote on
  only 149 sampled responses, and clarification-seeking is measured at
  stage 1 only, under a neutral (no-abstention-instruction) prompt, not
  across the whole sequential trajectory.
- SciConvBench's headline numbers use a single LLM judge (Gemini 2.5 Pro);
  robustness checks against alternative judges, prompt paraphrases and
  user-simulator models cover only an 80-case stratified subset of the
  1,142-case total, and its answering user is itself an LLM (Claude Sonnet
  4.6 by default) instructed to answer strictly from a hidden reference
  specification, not a human interlocutor.
- Ambig-DS's construction and oracle are model-assisted (Claude Opus
  generation/verification, Claude Haiku 4.6 oracle); cross-family verifier
  and judge/oracle robustness checks (swapping the oracle to GPT-5.4, the
  judge to GPT) shift results by only a few points, but residual
  generation- and oracle-family effects "cannot be fully ruled out," and
  the ambiguous variants are constructed by controlled prompt–data edits
  on two existing benchmarks (DSBench, MLE-bench), not collected from
  naturally occurring underspecified requests.
- SpecBench's 48 personas and every baseline's dialogue partner are LLM
  role-plays, not human users, and every baseline besides Buddy is a
  general-purpose CLI coding agent adapted with two MCP tools rather than a
  system built for this task, so the measured under-/over-asking split is
  driven by baseline agnosticism as well as by the ask-decision itself.
- IDRBench's feedback policy is an LLM (GPT-5.1) answering from the paired report, which is one reasonable report among many, so alignment measures agreement with one target, not report quality; the paper checks leakage (97.91% of replies classed as preference clarification, 2.09% object-level) and a 10-task human-feedback comparison (two humans), but its robustness diagnostics use a 30-task subset, and effects are attributed to the whole joint policy, not to individual questions.
- InteractWeb-Bench's Intent Alignment Score and Clarification Hit Rate are both LLM-as-judge scores (GPT-5-mini), not a ground-truth annotation of which hidden constraint was actually needed, and its simulated non-expert user is itself an LLM (DeepSeek-V3.2) under a persona-conditioned prompt, not a human low-code user; the result is domain-specific to interactive website generation.
- MedSP1000's scenarios are teaching simulations driven by LLM patient and environment agents, so its rubric completion measures a simulated encounter, not a live clinical one; "the resulting scenarios remain idealized."[^c34]

## Known as

| Field | Name there | Relation |
|---|---|---|
| llm-evaluation | clarifying-question benchmarks | exact |
| conversational IR | clarification datasets | close — usually means the labelled corpora (Qulac, ClariQ) alone, not the agentic four-way and multi-turn suites |

*ClariQ, CLAMBER, When2Call, ClarQ-LLM, ClarifyBench, ClarEval, Ambig-DS,
OR-Clarify, the Tri-Agent Framework, HerHealthEval, MT-InfoSeek, AcCoRD,
Interactive Visual Grounding, UserToolBench, AppWorld-UL, ClarifyCodeBench,
REAL-Bench, RegretBench, MapSatisfyBench, Clarify-Then-Search, DiscoBench,
DeskCraft, DLawBench, VitaBench 2.0, Safe-Psych, SciConvBench and SpecBench are not aliases of this concept.* They are members of the
class, and they measure different quantities — a question-selection
ranking, a binary ambiguity label, a four-way action choice, an end-to-end
task success rate, (OR-Clarify) exact recovery of formulation-critical slots
under a severity-weighted rubric, (Tri-Agent Framework) an LLM-judge's
composite score across five dialogue-quality dimensions, (HerHealthEval) a
recall/specificity pair on one deliberately under-specified form matched
across registers and languages, (MT-InfoSeek) final sufficiency against a
ground-truth CSP, (AcCoRD) an outcome score over four preference dynamics
under two prompting strategies, (Interactive Visual Grounding) a paired
model-vs-simulated-human accuracy gap across four protocols that vary how
much of a visual referent's description is given upfront, (UserToolBench)
an Exact/Relaxed trajectory accuracy on profile-hidden tool-call
trajectories split by single-tool, multi-tool and lack-of-information task
type, (AppWorld-UL) a knowledge-recall-gated task/scenario completion rate
over three agent-user interaction types and their compositions,
(ClarifyCodeBench) a discounted-early-coverage score (TKQR) paired with a
Gaussian round-count-deviation score (ORA), scored against an annotated
key-question set, (REAL-Bench) an RL-trained, budget-gated ask/act
success rate on a physically-groundable embodied manipulation task,
(RegretBench) a whole-dialogue reward (intent-match utility minus token
cost minus an unsupported/redundant/premature-clarification penalty)
scored as regret against a semantic reference planner, (MapSatisfyBench)
a restore-identify-filter-derived, evidence-weighted implicit-factor
satisfaction rate (IISR) multiplied with explicit completion (AR) and
turn efficiency (SES), (Clarify-Then-Search) a judge-weighted nugget
recall with partial credit (`restore_score_100`) scored end to end through
a closed-book rewrite and a fresh deep-search run, (DiscoBench) a
checkpoint-level pass rate over an ordered multi-step search trajectory,
paired with a forced-strategy accuracy gap (ask vs. guess after
retrieval vs. guess without it), (DeskCraft) a standard-vs-interactive
task success-rate pair plus a per-collaboration-mode success rate, scored
under a scripted, composable mid-turn/post-turn trigger protocol on
50+-step desktop-GUI workflows, (DLawBench) a five-metric hierarchy
(Fact Coverage, Inquiry, Fact Resolution, Issue Resolution, Fidelity)
scored by an LLM judge panel across four simulated client narrative
styles, (VitaBench 2.0) a proactive-task subscore compared against the
same model's ordinary personalization subscore across three memory
settings (Full Context, Agentic Memory, RAG Memory) on temporally ordered,
multi-domain task sequences, (Safe-Psych) a separated
under-abstention/over-abstention error pair over a stepwise
DIAGNOSE/CLARIFY/ABSTAIN sequential decision, scored against psychiatrist
sufficiency judgements, (SciConvBench) a case- and ontology-component-level
triple (Final Resolution Rate, Conversation-Grounded Resolution Rate, Silent
Resolution Rate) scored against a planted-issue reference over a fixed
9-component scientific task specification, (Ambig-DS) an
unflagged-misframing rate paired with a one-shot-oracle recovery delta
($\Delta_{ask}$) and an ask/don't-ask [[calibscore|CalibScore]], scored
independently across two disjoint ambiguity axes (prediction target,
evaluation objective) on two source benchmarks, or (SpecBench) a checklist
prediction-accuracy-vs-budget curve (T0→T5, T5→T10, T0→T10) paired with a
five-criterion LLM-judge spec-sheet score, both reported jointly with query
count and early-submission rate over 50 projects and 48 personas —
rather than a single ambiguity or success label — not a single accuracy number.
| llm-evaluation | Fuse | exact |
| llm-evaluation | Framework for User-mediated Social Evaluation | exact |
| llm-evaluation | Fuse social-reasoning benchmark | exact |

## Related

[[preference-signal-against-asking]] · [[uncertainty-decomposition]] · [[question-budgets]] · [[elicitation-protocols]] · [[multi-agent-clarification]] · [[interopt-gap-guided-clarification]] · [[preference-dynamics-taxonomy]] · [[restore-identify-filter]] · [[mid-turn-post-turn-protocol]] · [[legal-consultation-paradox]] · [[calibscore]] · [[simulated-user-consensus-filtering]] · [[blind-execution]]

[^c32]: doi-10-48550-arxiv-2606-05112 — "completes only 60.4% of expert-defined rubric items"
[^c33]: doi-10-48550-arxiv-2606-05112 — "Additional test-time scaling does not improve interactive performance."
[^c34]: doi-10-48550-arxiv-2606-05112 — "the resulting scenarios remain idealized"
[^c31]: arxiv-2601-06676 — "Table 4 shows that every single-stage setting exceeds None in Average Score, Planning is the strongest single-stage setting for both models, and All is highest overall."
[^c30]: arxiv-2601-06676 — "GPT-5.1 achieves the highest autonomous score (75.59), Claude-Sonnet-4.5 the highest interactive score (80.47), and Llama-4-Maverick the largest"
[^c29]: arxiv-2601-06676 — "in 74.4% of cases but degrades it in 19.9%, demonstrating"
[^c28]: arxiv-2604-27419 — "models tend to compensate for missing requirements through aggressive generation rather than iterative clarification, resulting in increased code size and higher hallucination rates."
[^c27]: wang-2026-turning — "for many data instances in Task 1, the prediction accuracy on the checklist questions degrades from T = 0 to T = 5 and T = 10"
[^c26]: stoisser-2026 — "commit to the wrong prediction target on 39–63% of ambiguous tasks — and do not flag the ambiguity"
[^c25]: somasekharan-2026 — "under the same model and protocol, G EMINI 2.5 P RO resolves 86.1% of cases on a filtered subset of CLAMBER but drops to as low as 18.2% on S CI C ONV B ENCH disambiguation"
[^c24]: presacan-2026 — "Under-abstention exceeds 60% for most models, indicating that many systems still diagnose despite insufficient evidence even when explicitly permitted to abstain."
[^c23]: chen-2026-vitabench — "current agents often fail to recognize when their knowledge is insufficient, and instead proceed with incomplete information rather than initiating clarification"
[^c22]: zhang-2026-dlawbench — "GLM-5.1 covers 0.766 of annotated facts but reaches only 0.360 Inquiry, showing that a model can cover many facts in the memo while still missing key factual follow-up and verification actions."
[^c21]: wang-2026-deskcraft — "We evaluate 18 proprietary and open source agents on 538 tasks and find that GPT-5.4 reaches 31.6% on standard tasks and 27.6% on interactive tasks."
[^c20]: tao-2026 — "substantially outperforming DirectGuess (56.5%) and SearchHeavyGuess (51.9%)."
[^c19]: huang-2026-clarify — "All Clarifiers improve over orig, showing that even one clarification can elicit useful intent-grounded information for rewriting and downstream deep search."
[^c18]: bai-2026-mapsatisfybench — "TS ranges from 0.2859 to 0.4942, and even the best model on this metric, Claude-4.6-opus, remains below 0.50."
[^c17]: ta-2026 — "models with similar accuracy can differ substantially in efficiency, robustness to user behaviors, and stopping decisions"
[^c16]: mi-2026
[^c15]: fang-2026-clarifycodebench — "DeepSeek-V3.2 achieves the highest TKQR, at 0.30, and the highest ORA, at 0.50, while most other models remain below 0.30 on TKQR and below 0.35 on ORA."
[^c14]: chen-2026-appworld — "We observe low performance across all agents, with the best-performing system (Code Agent with Claude Opus 4.7) achieving only 48.6% I-TGC and 30.2% I-SGC overall."
[^c13]: yin-2026 — "For instance, GPT-5.4 obtains the highest LOI accuracy at 42.22% despite its lower overall exact accuracy, whereas Qwen 3.6 Plus performs strongly on single-tool tasks at 58.02% but drops to 19.52% on LOI tasks."
[^c12]: wang-2026-when — "All models ask more questions when less initial information is available: N ONE > PARTIAL > F ULL > S TATIC (= 0 by design; lower panels of Figure 3)."
[^c11]: srinivasan-2026 — "UncReAct prompting alone does not improve preference elicitation and satisfaction. Weaker models (Llama-3.1-70B, DeepSeek-V3) cannot execute uncertainty reasoning correctly under UncReAct: rather than making calibrated elicitation decisions, they over-ask and exhaust their dialogue"
[^c10]: huang-2026
[^c9]: albattra-2026 — "In contrast, Model 1 exhibits strong uncertainty handling, achieving a clarification recall of 0.856 and a specificity of 0.862 on the 90 cases requiring clarification."
[^c8]: zhao-2026-agent
[^c7]: ge-2026 — "Performance varies by model and protocol; Opus-4.8 is strongest in both settings, but no model exceeds 60% Core Exact and all retain substantial silent assumptions."
