---
description: "A displacement of one point spreads over several coordinate differences, so a moved point can pass as stable (masking) and a stable one as unstable (swamping)."
aliases: ["masking and swamping", "masking", "swamping", "displacement smear"]
sources: ["doi-10-1007-s00190-026-02043-y"]
---
# Smear effect (masking and swamping)

A least-squares test for unstable points in a monitoring network does not see one displacement at one point. The paper names the mechanism the smear effect, and defines it as "the influence of a true displacement spreads over several coordinate differences."[^s1] The error it produces has two faces: "a displaced point classified as stable (masking) and a stable point classified as unstable (swamping)."[^s2] Masking is a moved point that the test passes as stable. Swamping is a still point that the test flags, because the differences it is tested through carry some other point's motion.

The problem grows with the number of moving points. The abstract says it becomes "more severe when several points move simultaneously."[^s3]

The text gives the mechanism only in projector terms. The observation differences are linear in the displacement through a design matrix, and the statistic for each candidate displacement set is a quadratic form in the data, built from the projector onto that set's range (eqs. 21 to 24 in the paper). When two candidate sets have overlapping ranges, the data fit one about as well as the other, and the identification can land on the wrong set. That link from overlapping ranges to wrong identifications is my inference from the projector formulation, not a result the text states in those words.

How the paper treats it: SEQCUP "excludes models that share the same projector, and uses a normalized distance between projectors to avoid stages with potentially weak separability and pronounced smear effects."[^s4] The gain is reported for identification more than for detection. The paper says "Identification constitutes a more difficult task than detection,"[^s5] and in a network with high geometric separability, reliable identification appears once "the displacement magnitude exceeds approximately" about twice the average standard deviation of the two-epoch differences.[^s6]

## Limits

- The masking and swamping rates of the competing procedures are not restated in the slices read. The comparison claim is qualitative: the method "performs at least as well as classical procedures."[^s8]
- The evidence is simulation on trilateration, GNSS baseline and levelling networks, plus one literature scenario. One experiment uses Gaussian errors: "Measurement errors followed a normal distribution with standard deviation σ = 1."[^s9]
- Geometric separation is not enough to remove the effect. The paper says "this geometrical distinction does not guarantee unique statistical outcomes."[^s7]
- The roughly twice-the-standard-deviation threshold comes from one network. No general threshold is claimed in the slices read.
- The paper treats robust estimators as outside its scope: "but they are beyond the scope of this work."[^s10] Whether a robust method shrinks the smear effect is not tested here.

## Related

- [[hypothesis-testing]] — masking and swamping are identification errors, distinct from the false-alarm rate α that a test controls.
- [[post-selection-monte-carlo-calibration]] — keeps the false-alarm rate near its nominal level while the procedure searches over displacement sets, a search the smear effect makes ambiguous.
- [[shared-projector-indistinguishability]] — one geometric route into masking and swamping: two models with the same projector cannot be told apart.

[^s1]: doi-10-1007-s00190-026-02043-y — "the influence of a true displacement spreads over several coordinate differences"
[^s2]: doi-10-1007-s00190-026-02043-y — "a displaced point classified as stable (masking) and a stable point classified as unstable (swamping)"
[^s3]: doi-10-1007-s00190-026-02043-y — "more severe when several points move simultaneously."
[^s4]: doi-10-1007-s00190-026-02043-y — "uses a normalized distance between projectors to avoid stages with potentially weak separability and"
[^s5]: doi-10-1007-s00190-026-02043-y — "Identification constitutes a more difficult task than detection,"
[^s6]: doi-10-1007-s00190-026-02043-y — "when the displacement magnitude exceeds approximately"
[^s7]: doi-10-1007-s00190-026-02043-y — "this geometrical distinction does not guarantee unique statistical outcomes."
[^s8]: doi-10-1007-s00190-026-02043-y — "The method performs at least as well as classical procedures and"
[^s9]: doi-10-1007-s00190-026-02043-y — "Measurement errors followed a normal distribution with standard deviation σ = 1"
[^s10]: doi-10-1007-s00190-026-02043-y — "but they are beyond the scope of this work."
