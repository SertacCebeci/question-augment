---
description: "Harmful and legitimate scenarios can share underlying principles while differing in surface category, so a judgment keyed to surface category can be moved across the boundary."
aliases: ["semantic isomorphism", "principle isomorphism", "principle transfer across scenarios"]
sources: ["arxiv-2512-13703"]
---
# Principle isomorphism across category

Two scenarios can sit on opposite sides of a surface category line, one
harmful and one legitimate, and still be built on the same technical
principles. The claim of Yang (2025) is that this is common rather than
rare: "many harmful scenarios are highly consistent with legitimate ones in
terms of underlying principles."[^c1] A judgment that reads the scenario's
surface category, and not its principle, will then treat the two as
different things, even though the knowledge they touch is the same.

The mechanism the paper proposes is a gap between two levels of
judgment. The surface level looks at what a request is about. The principle
level looks at what it requires to be understood or done. The argument is
that "the commonality of technical principles implies that if harmful
requests can be associated with the principle framework of legitimate
scenarios, it may be possible to evade the model's semantic-level
interception."[^c2] In the paper's words, placing a request inside the
principle framework of a legitimate scenario leads "the safety mechanisms to
misjudge them as compliant requests."[^c3] So the blind spot is located in
the level at which the safety judgment operates, not in the knowledge the
model holds.

The paper reports this as an attack finding. Across "7 mainstream LLMs and
three types of benchmark datasets," the method "exhibits strong jailbreaking
capability, and its overall performance is superior to existing methods."[^c4]
Its success labels come from a vote: a response is "preliminarily labeled as
harmful only when the majority" of several judge models agree.[^c5] The
measure is therefore a judged rate, and it depends on the judges as much as
on the target.

For the asking and answering transformation, the concept locates a failure
(my inference from the paper's account, not a finding of the paper). An
answerer who judges by surface category may refuse a request whose content
is harmless and pass one whose content is not, because the label, not the
structure of the scenario, is what it reads. A questioner whose wanted
knowledge sits under a sensitive label can be stopped by that label and not
by the principles involved. The concept says where that failure sits: in the
level at which the category is read.

I am extending the claim one step (my inference, not the paper's): if the
surface category is what the judgment reads, then the same blind spot should
appear in any judgment keyed to a salient frame. [[frame-activation]] reports
that a prompt can make one relation the criterion of judgment, which is the
same kind of shift from content to a foregrounded feature. Whether a
principle-level reading would close the gap is not tested here.

## Limits

- The concept is shown for one attack method on LLMs. The paper says the
  "current study only verifies the attack effect of Safe2Harm on Large"[^c7]
  language models, and it does not test vision-language models.
- The phenomenon, that many harmful scenarios match legitimate ones in
  principle, is asserted in the introduction. The sections read do not
  measure how common the match is, nor across which domains.
- Success is a judge's label. The paper does not report agreement between
  the judges and human raters in the sections read, so the rates are the
  judges' readings.
- The effect is not uniform across requests. The paper says that "for
  extremely harmful requests such as" explicit content "current attacks often
  fail because the theme conversion" stage is rejected by the model.[^c6]
  The principle-level route is therefore not free of the surface level: the
  conversion itself can be caught.
- No ablation in the text read separates the principle-level account from
  other causes of the success rate, such as the length or polish of the
  output. The explanation is the authors' reading.

## Related

- [[frame-activation]] — a prompt can make one relation the criterion of judgment; the same surface-versus-criterion shift, in a labelling task
- [[script-level-obfuscation]] — another surface-level attack on refusal, which keeps the intent and changes the form; here the change is in the category, with the principle kept
- [[llm-red-teaming]] — the generate-and-judge loop in which attack success is measured; its judge sets the rate, as here
- [[extended-reasoning-framing-resistance]] — a framing effect on refusal that changes with the reasoning mode, the other side of the same surface-judgment question

[^c1]: arxiv-2512-13703 — "many harmful scenarios are highly consistent with legitimate ones in terms of underlying principles"
[^c2]: arxiv-2512-13703 — "the commonality of technical principles implies that if harmful requests can be associated"
[^c3]: arxiv-2512-13703 — "leading the safety mechanisms to misjudge"
[^c4]: arxiv-2512-13703 — "exhibits strong jailbreaking capability"
[^c5]: arxiv-2512-13703 — "for voting-based judgment, where a response is preliminarily labeled as harmful only when the majority"
[^c6]: arxiv-2512-13703 — "current attacks often fail because the theme conversion"
[^c7]: arxiv-2512-13703 — "current study only verifies the attack effect of Safe2Harm on Large"
