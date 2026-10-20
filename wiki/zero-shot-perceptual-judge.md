---
description: "A vision-language model asked to reason about differences between two images reproduces binary human 2AFC similarity judgments with no training, a candidate stand-in for a learned perceptual metric."
aliases: ["VLM perceptual judge", "vision-language model as 2AFC judge", "VLM as human-aligned similarity judge"]
sources: ["arxiv-2512-15701"]
---
# Zero-shot perceptual judge

A vision-language model (VLM) can be used as a judge of visual similarity without being trained for that task. Given an original image and two reconstructions of it, and asked to reason about how the two differ, it gives a verdict on which reconstruction is closer. The claim is that this verdict reproduces binary human two-alternative forced choice (2AFC) judgments: state-of-the-art VLMs "can replicate binary human two-alternative forced choice (2AFC) judgments zeroshot when asked to reason about the differences between" pairs of images.[^c1] The model tested is an off-the-shelf Gemini 2.5-Flash, which "can replicate human judgments on multiple" human-judgment datasets.[^c2]

The verdict is usable only because of three choices in how it is elicited. The reasoning comes first: "Prior to producing the numerical rating, the VLM" is asked to describe each image and note artifacts in both reconstructions, and only then to give a signed rating.[^c3] The pair is shown in both orders: "we rate each pair of reconstructed images in two orders, reversing the order the" second time, and the two ratings are combined by sign.[^c4] The judgment is also repeated over several random seeds, and the seeds are combined by majority: "computing the reward as the majority vote of multiple" captioning requests.[^c5]

## Measurement

The agreement is measured on BAPPS and on the authors' own "Compressed Images" set, which "contains 5401 tuples of compressed images from two random baselines or our method; each tuple is rated at least" three times by humans.[^c6] The human baseline is measured by leave-one-out: "one human judgment and measuring its agreement with the" average of the remaining raters on that tuple.[^c7] On the compressed images, both LPIPS and the VLM "exceed the performance of a single human". The authors attribute this to "the compressed images being highly similar to the original image", which makes human judgments noisier, so a single rater is a weak reference here.[^c8]

The judge's verdicts were then used as a training signal: "ranking them via a reward function to produce a winning" and losing decompression of the same latent code.[^c9] That training use is a separate matter from the judge. This note concerns the judge.

## Where it is weak

The judge is least reliable where the items differ least. The paper says "VLM judgments are less noisy when the images are more different".[^c10] For highly similar reconstructions, "the VLM fails to be self-consistent when the" order of the two images is reversed, and the authors call this noisiness "a serious issue".[^c11][^c12]

Repetition is the main remedy the paper reports. "Most helpful is self-ensembling", the majority vote over seeds, and "The VLM becomes more predictive of human judgment on BAPPS" as the number of seeds is scaled.[^c13] The main experiments use "n = 3 seeds", and more seeds would help "at the cost of more VLM queries".[^c14] The cost is real: "VLM-based rewards are more expensive to" "compute than evaluations of a small perceptual network".[^c15]

A second guard is agreement with a different metric. The authors "Ensemble the VLM reward with LPIPS", a traditional perceptual metric, and keep a pair "only if" they agree: "If they disagree, the example is discarded."[^c16] They report that "ensembling with LPIPS provides superior performance to using LPIPS or the VLM reward alone".[^c17] The paper also says why the guard is needed: "Since VLMs are prone to hallucination and to ignoring" the image contents, so the verdict is not taken at face value.[^c18]

## Limits

- The measured task is perceptual similarity between an original and its distorted or compressed versions, on BAPPS and one compression set. Agreement on semantic answer quality, on reasoning, or on pairs of unlike items is not tested in the sections I read. (My inference from the task set.)
- Agreement with raters is not the same as tracking what matters for the use. A judge can match raters on these pairs and still fail elsewhere; no adversarial or out-of-distribution test is reported in the sections read. (My inference.)
- One model, one preprint (December 2025). Other VLMs are not compared in the sections read. The authors expect that "improved automatic perceptual judges may result" as VLMs improve, which is their expectation, not a measured trend.
- The headline is dataset-dependent: the system is "competitive or" "state-of-the-art performance on human-aligned visual compression depending on the dataset".[^c19] The judge's own accuracy is not reported as one number in the text read here.
- Repetition raises agreement but multiplies the query cost, and the paper stops at three seeds.

## Related

- [[llm-judge-biases]] — the same order instability and near-tie weakness in text judges; swapping and majority votes are the usual remedies there too
- [[pairwise-judge-over-scalar-reward]] — a judge is more reliable choosing the better of two than scoring one item; this judge is pairwise by design
- [[pseudo-ensemble]] — repeated perturbed queries to one model as a stand-in for a trained ensemble; the seeds here play a similar role (my inference)
- [[cross-provider-judge-ensemble]] — a different route around one judge's noise, by mixing judges from several providers
- [[pessimistic-min-judge-aggregation]] — disagreement resolved downward; the paper instead discards a pair on which its two judges disagree

[^c1]: arxiv-2512-15701 — "can replicate binary human two-alternative forced choice (2AFC) judgments zeroshot when asked to reason about the differences between"
[^c2]: arxiv-2512-15701 — "can replicate human judgments on multiple"
[^c3]: arxiv-2512-15701 — "Prior to producing the numerical rating, the VLM"
[^c4]: arxiv-2512-15701 — "we rate each pair of reconstructed images in two orders, reversing the order the"
[^c5]: arxiv-2512-15701 — "computing the reward as the majority vote of multiple"
[^c6]: arxiv-2512-15701 — "contains 5401 tuples of compressed images from two random baselines or our method"
[^c7]: arxiv-2512-15701 — "one human judgment and measuring its agreement with the"
[^c8]: arxiv-2512-15701 — "the compressed images being highly similar to the original image"
[^c9]: arxiv-2512-15701 — "ranking them via a reward function to produce a winning"
[^c10]: arxiv-2512-15701 — "less noisy when the images are more different"
[^c11]: arxiv-2512-15701 — "the VLM fails to be self-consistent when the"
[^c12]: arxiv-2512-15701 — "highly similar images is a serious issue"
[^c13]: arxiv-2512-15701 — "Most helpful is self-ensembling"
[^c14]: arxiv-2512-15701 — "For our main experiments, we use n = 3 seeds"
[^c15]: arxiv-2512-15701 — "compute than evaluations of a small perceptual network"
[^c16]: arxiv-2512-15701 — "Ensemble the VLM reward with LPIPS"
[^c17]: arxiv-2512-15701 — "ensembling with LPIPS provides superior performance to using LPIPS or the VLM reward alone"
[^c18]: arxiv-2512-15701 — "Since VLMs are prone to hallucination and to ignoring"
[^c19]: arxiv-2512-15701 — "state-of-the-art performance on human-aligned visual compression depending on the dataset"
