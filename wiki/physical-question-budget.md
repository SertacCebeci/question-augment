---
description: "Dividing an energy allocation by tokens per question gives a finite count of answerable queries; the count is dominated by response length, not by the thermodynamic floor of the information gained."
aliases: ["finite question budget", "token-energy question budget", "Photons = Tokens question budget"]
sources: ["arxiv-2603-06630"]
---
# Physical question budget

A question can be priced in physical units. The paper takes a projected 2028 US AI energy allocation of 326 TWh, converts it to tokens at an assumed 5 × 10^-4 Wh per token, and divides by tokens per question-answer pair.[^c1] At 100 tokens per question this gives about 6.5 quadrillion questions a year, roughly 2,200 per person per day for 8 billion people.[^c2]

## Two costs of a question

The information-theoretic floor: a question whose answer yields I bits of mutual information costs at least I · k_B T ln 2 (Landauer). The authors call this a floor, not a ceiling.[^c3] The practical cost is the tokens needed to formulate the question and generate the answer, typically 100-1,000 tokens for a substantive pair. The floor is about 19 orders of magnitude below actual cost (the paper's "efficiency gap"), so the binding quantity is length of exchange, not bits learned.

## Sensitivity

The count is a ratio, so it moves linearly with both inputs. At 1,000 tokens per question the 326 TWh figure falls to 225 questions per person per day.[^c4] Long outputs such as a differential diagnosis or legal memorandum (2,000-5,000 tokens) cut it a further 20-50x. A verbose answer therefore spends the budget in proportion to its length, whatever information it carries (my inference from the ratio form).

## What it does and does not say

The budget counts answerable questions; it does not rank them. The paper's own use is to frame allocation as an economic problem: which questions are asked, by whom, at what cost.[^c5]

## Limits

- Order-of-magnitude arithmetic from one energy projection and one assumed energy-per-token; the paper offers no empirical measurement of how people actually ask.
- Treats a "question" as a token count, so a trivial query and a deep one cost the same; it says nothing on question quality (see [[entropy-versus-bearing-on-action]]).
- Compute-side only. The scarce resource in [[question-budgets]] is the user's attention and the cost of asking the user; here it is machine energy. They are different budgets and should not be summed.
- The allocation claims (who should decide) are the authors' argument, not a result.

## Related

- [[question-budgets]] — budgets by source of answer (agent, user, world); this note is the compute-energy budget.
- [[entropy-versus-bearing-on-action]] — why the count does not decide which questions to spend it on.
- [[value-of-information]] — the per-question benefit side that a count of questions omits.
- [[throughput-pressure-on-asking]] — rate of answering as a pressure on how one asks.

[^c1]: arxiv-2603-06630 — "Given the projected 2028 AI energy budget of 326 TWh and an illustrative conversation"
[^c2]: arxiv-2603-06630 — "or roughly 6.5 quadrillion questions. Per person per day:"
[^c3]: arxiv-2603-06630 — "This is a floor, not a ceiling."
[^c4]: arxiv-2603-06630 — "the budget drops to 225"
[^c5]: arxiv-2603-06630 — "The allocation of questions is an economic problem: which questions are worth asking, who gets to ask them, and at what cost."
