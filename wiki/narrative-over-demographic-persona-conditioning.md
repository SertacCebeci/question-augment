---
description: "Conditioning an LLM on a respondent's own interview raised its agreement with that person's survey answers more than adding demographics did, and longer interviews did not reliably help."
aliases: ["interview-informed persona prompting", "persona content versus length"]
sources: ["doi-10-5281-zenodo-18247291"]
---
# Narrative over demographic persona conditioning

When an LLM is asked to answer a questionnaire as a specific person, what the person-level part of the prompt contains decides how close its answers come to that person's real answers. In the BREQ study the prompts were assembled from four parts: research background, item content, the person's interview transcript, and demographics.[^n1] They were combined into four prompts, and the interview was the part that mattered. Prompts containing it "have relatively higher associations with humans than other prompts," and the paper concludes that "persona-based prompts containing personal interview data improved alignment in both response patterns and diversity."[^n2][^n3]

Demographics did little. Adding age, race and gender to the interview prompt gave "minimal improvement in alignment."[^n4] Demographics alone sat close to the no-person baseline: the demographic prompt "has slightly higher correlations than the baseline" for claude, gemini and gpt, a small gain.[^n9] The authors attribute the gap to the weaker link between demographics and survey answers: the relationship "is relatively weaker than the interview."[^n5] That is a reading of the result, not something the design isolates, since demographics and interview were never tested in every combination against a neutral control with matched length.

Length did not explain the gain. Across the 19 respondents, interview length in tokens was moderately correlated with person-level error but not significant (p = .086).[^n10] "Longer interviews (greater number of tokens in prompts) did not necessarily lead to better alignment."[^n6] The paper's reading is that "the relevance of interview content, rather than its length, plays a more critical role."[^n7] A person's transcript can be relevant without being long, and a long one can be off-topic; the paper does not separate those.

The same content shows up in the spread of the answers. Interview-containing prompts widened the spread for some chatbots, which is covered in [[simulated-respondent-variance-deficit]], and did not close the gap to human spread. Agreement and spread are separate measures and the interview helps one more clearly than the other.

## Limits

- Nineteen respondents, one interview each, and a single BREQ instrument. The length result is, in the authors' words, "inconclusive" at this sample size.[^n11]
- The prompt-length comparison is confounded. The paper admits that "the four prompts differ in both their length (number of tokens) and content,"[^n12] and its own length figures do not agree: it says "all prompts have same number of tokens, at 1,276,"[^n13] then reports prompt 1 as the shortest and prompts 2 and 3 as "middle level of number of tokens."[^n14] Prompt 3 has no interview, so its mean length of 5,917 tokens is hard to read. Until the lengths are reported per prompt, the length claim cannot be checked.
- The interview was tested as one whole transcript. The paper does not identify which parts of an interview carry the signal, so "relevant content" is a label the authors apply, not a measured feature.
- The effect varies by chatbot. Claude gained most from interviews; gemini was more diverse with demographics alone. The "interview helps" result is not uniform across models.
- Correlation with a person's answers is not evidence that the transcript explains those answers. The interview and the survey were collected from the same person in the same program, so shared emotional state could produce agreement that is not about the content of the interview. The paper raises this itself: "emotional inconsistencies across data collection modes" may contribute to the mismatch.[^n8]

## Related

- [[simulated-respondent-variance-deficit]] — the same prompts judged on spread rather than agreement; interview content widened spread for some models without closing the gap
- [[expert-persona-confidence-amplification]] — persona conditioning in general lowers answer entropy; this note asks which persona content keeps the answers close to one given person
- [[personal-representation-leakage]] — the personal content that makes a simulated answer fit a person is the content that can leak; the link is my inference, not the paper's

[^n1]: doi-10-5281-zenodo-18247291 — "Research Background, including program description and research"
[^n2]: doi-10-5281-zenodo-18247291 — "have relatively higher associations with humans than other prompts"
[^n3]: doi-10-5281-zenodo-18247291 — "persona-based prompts containing personal interview data improved alignment in both response patterns and diversity"
[^n4]: doi-10-5281-zenodo-18247291 — "additional demographic information in prompts showed minimal improvement in alignment"
[^n5]: doi-10-5281-zenodo-18247291 — "relatively weaker than the interview"
[^n6]: doi-10-5281-zenodo-18247291 — "did not necessarily lead to better alignment"
[^n7]: doi-10-5281-zenodo-18247291 — "the relevance of interview content, rather than its length, plays a more critical role"
[^n8]: doi-10-5281-zenodo-18247291 — "emotional inconsistencies across data collection modes"
[^n9]: doi-10-5281-zenodo-18247291 — "has slightly higher correlations than the baseline"
[^n10]: doi-10-5281-zenodo-18247291 — "the correlation between the number of tokens in individual interviews and the average person-level RMSE for Prompt 2 and Prompt 4 was moderate while not statistically significant"
[^n11]: doi-10-5281-zenodo-18247291 — "the impact of interview length on alignment remains inconclusive"
[^n12]: doi-10-5281-zenodo-18247291 — "the four prompts differ in both their length (number of tokens) and content"
[^n13]: doi-10-5281-zenodo-18247291 — "all prompts have same number of tokens, at 1,276"
[^n14]: doi-10-5281-zenodo-18247291 — "Prompt 2 and Prompt 3 have middle level of number of tokens"
