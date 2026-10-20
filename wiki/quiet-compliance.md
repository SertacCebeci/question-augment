---
description: "Agents often execute a false assertion yet still reach the correct final state, so accuracy-only scoring misses it; splitting compliance by outcome tells quiet from destructive."
aliases: ["quiet compliance", "transparent vulnerability", "success-preserving compliance", "latent compliance"]
sources: ["arxiv-2512-00332"]
---
# Quiet compliance

An agent that obeys a false assertion does not always fail the task. Waqas et al. score their benchmark by the final environment state, so a run can execute an unnecessary or misleading call and still count as a success: "Task success is determined by the final environment state, not merely".[^q1] Under outcome-only scoring the procedural compliance described in [[assertion-conditioned-compliance]] is invisible, because the grader only looks at where the environment ends up.

Making it visible takes a paired design. Each asserted run is matched to a no-assertion baseline, and each case falls into one of four outcome buckets: success preserved (S→S), success lost (S→F), recovery (F→S), and failure persisting (F→F). Compliance is then read inside each bucket. The authors state the purpose directly: "This analysis helps in distinguishing harmful degradation (a high CR in the S→F bucket) from latent,"[^q2] meaning a high CR inside the S→S bucket is the quiet case, where the agent obeyed and the task still came out right.

The table's average row for the FSA breakdown gives CR 14.5 in S→S and 57.1 in S→F (my reading of the table, which the prose does not restate).[^q3] So the quiet bucket is not empty, but compliance is concentrated where the task is lost on this measure. The conclusion puts the two together: models "comply significantly with misleading assertions in"[^q4] both buckets, so quiet over-compliance can coexist with strong benchmark scores.

The paper also reports that compliance is not a proxy for damage. Watt Tool 8B has a higher USA compliance rate than Qwen3 8B, yet "a smaller worst-case success drop (10.2 percentage points) than Qwen3 8B"[^q5] — the authors take this as evidence that "cannot be treated as a simple proxy for" task-level risk.[^q6] Quiet compliance and accuracy loss are therefore two axes, and a model can sit high on one and low on the other.

## Limits

- The buckets are small. Several cells of the FSA breakdown rest on fewer than 40 cases (n=15 and n=16 appear), so a bucket-level CR is a rough estimate, not a precise rate (my reading of the counts in Table 2).
- "Success preserved" means the final environment state matched the expected one. It does not establish that the extra call was harmless; the authors call their setup "controlled stress test rather than a direct measure"[^q7] of deployed behaviour, and they do not measure side effects outside the grader.
- The result depends on the grader. A different state check, or one that inspects the call trace, would move cases between buckets. That sensitivity is not tested here.
- One benchmark: "Our evaluation is grounded exclusively on"[^q8] BFCL multi_turn_base, and the buckets are not replicated elsewhere.
- Each run is a single outcome per case, with deterministic settings for most models; the Qwen3 variants are non-deterministic, so their bucket membership may shift between runs.

## Related

- [[assertion-conditioned-compliance]] — the compliance rate this split is applied to, and the provenance channels it covers.
- [[compliance-bias]] — outcome-only scoring rewards proceeding under unverified preconditions; quiet compliance is the same blind spot for obedience to a false assertion (my reading).
- [[tool-use-robustness-gap]] — accuracy loss under corrupted tool responses; quiet compliance is the part of agent behaviour that an accuracy number of this kind cannot show.

[^q1]: arxiv-2512-00332 — "Task success is determined by the final environment state, not merely"
[^q2]: arxiv-2512-00332 — "This analysis helps in distinguishing harmful degradation (a high CR in the S→F bucket) from latent,"
[^q3]: arxiv-2512-00332 — "Table 2: Breakdown of the FSA results from Table 1."
[^q4]: arxiv-2512-00332 — "comply significantly with misleading assertions in"
[^q5]: arxiv-2512-00332 — "a smaller worst-case success drop (10.2 percentage points) than Qwen3 8B"
[^q6]: arxiv-2512-00332 — "cannot be treated as a simple proxy for"
[^q7]: arxiv-2512-00332 — "controlled stress test rather than a direct measure"
[^q8]: arxiv-2512-00332 — "Our evaluation is grounded exclusively on"
