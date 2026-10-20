---
description: "Let the model reason unconstrained and switch the grammar mask on only at a trigger token; a lone end-of-sequence trigger avoids premature triggering and gives full parse rate at small token cost."
aliases: ["In-Writing", "reason-then-constrain decoding", "delayed constrained decoding"]
sources: ["doi-10-48550-arxiv-2601-07525"]
---
# Trigger-gated constrained decoding

Constrained decoding applied from the first token forces the model to reason inside the schema. Trigger-gated decoding (named In-Writing by Nguyen et al., 2026) splits one generation call in two phases. The model first writes free-form reasoning. Only after a trigger token appears does the grammar mask apply, and then only to the final structured field.[^c1] The mask therefore governs the format of the answer and not the reasoning that leads to it. This is a variant of [[constrained-decoding]] that keeps its guarantee for the answer field only.

## What was measured

The authors compare four methods on the same models and prompts: natural generation, vanilla constrained decoding, NL-to-Format (a second stage that extracts the answer) and the gated method. Natural generation, NL-to-Format and the gated method share the same reasoning trace, so their accuracy differences come only from how the answer is extracted.[^c2]

On GSM8K with LLaMA3-8B-it, accuracy was 66.2 for natural generation, 48.9 for constrained decoding, 74.7 for NL-to-Format and 77.9 for the gated method. On Shuffled Objects with Gemma2-9B-it the figures were 10.0, 50.5, 49.4 and 50.5.[^c3] The paper reports gains of up to 27% over LLM-based parsing, and the gated method reaches a 100% parse rate.[^c4]

## Premature triggering

The failure mode is that the trigger fires while reasoning is still going on, so the constraint cuts the reasoning off. With two triggers (end-of-sequence and `{`), premature triggering truncated reasoning and cut quality, by over 30% on GSM8K compared with the single-trigger variant. Classification tasks were barely affected.[^c5] Using end-of-sequence as the only trigger mitigates it.[^c6] The mechanism, in my reading, is that a `{` can appear inside ordinary reasoning text, whereas end-of-sequence marks the model's own decision to stop.

## Why it beats a second extraction pass

Because the mask limits the answer to the schema, it also repairs a sloppy final sentence. In the paper's example the model writes "Helga" and the masked field is forced to the option letter A.[^c7] An overlap analysis shows the gated method recovering many NL-to-Format failures, with up to an 11.8% improvement, while the reverse case is much rarer. The authors attribute this to token masking.

Token cost is small. NL-to-Format adds 2–5 tokens and the gated method adds 5–20.[^c8] Vanilla constrained decoding instead puts JSON syntax at the start and so alters the reasoning trace itself.

## Limits

- Models tested are 1.5B–14B parameters, on classification and reasoning benchmarks with short answers. Long structured outputs with many fields are discussed as a motivation but the main tables score a single answer.
- JSON-style constraints sometimes help under identical prompts, but the paper attributes that to more tokens generated.[^c9] So reasoning length is a confound in any comparison of constrained and free methods.
- The parse guarantee covers syntax. A masked field still can pick the wrong member, and the reasoning stays unverified.
- The cause of premature triggering is my inference above; the paper shows the effect of the trigger choice, not an analysis of why `{` fires early.
- Comparisons with the earlier numbers of Tam et al. reuse their reported results; the paper does not rerun all of them.

## Related

- [[constrained-decoding]] — the mask being deferred; this note changes when it applies
- [[structured-output]] — the four-way split; this method is a fifth hybrid arrangement
- [[format-restriction-effect]] — the accuracy cost of formatting that this method avoids paying early
- [[deferred-answer-exposure]] — another design that holds the answer back until reasoning is done

[^c1]: doi-10-48550-arxiv-2601-07525 — "The model first performs unconstrained reasoning and only applies structured decoding after a trigger token is generated, explicitly decoupling reasoning from formatting."
[^c2]: doi-10-48550-arxiv-2601-07525 — "share identical reasoning traces; performance differences stem solely from answer extraction."
[^c3]: doi-10-48550-arxiv-2601-07525 — "Table 1: Zero-shot results for GSM8K, Last Letter and"
[^c4]: doi-10-48550-arxiv-2601-07525 — "In-Writing achieves 100% parse rate"
[^c5]: doi-10-48550-arxiv-2601-07525 — "In-Writing-Base results indicate that premature triggering truncates reasoning"
[^c6]: doi-10-48550-arxiv-2601-07525 — "By simply setting <eos> as the unique trigger token, In-Writing*"
[^c7]: doi-10-48550-arxiv-2601-07525 — "In-Writing additionally generates an easily parsable final answer with syntactic corrections"
[^c8]: doi-10-48550-arxiv-2601-07525 — "NL-to-Format adds 2–5 tokens, while In-Writing* adds"
[^c9]: doi-10-48550-arxiv-2601-07525 — "In some cases, JSON-style constraints improve performance under identical prompts, but this gain is"
