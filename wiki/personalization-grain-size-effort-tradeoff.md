---
description: "With a teacher in the loop, LLM task personalization stays at class-level grain because each rewrite costs minutes; students prefer individual-level references and the cost did not fall."
aliases: ["teacher-in-the-loop context personalization", "grain size of personalization"]
sources: ["arxiv-2602-15876"]
---
# Personalization grain-size and effort trade-off

Context personalization adapts a task (here, a middle-school math problem) to student interests. The work names three design dimensions: depth (how well the interest is truly reflected, including realism), grain size (whole-class interests versus an individual's), and ownership (who controls the connection). In a study of 7 teachers using ChatGPT to personalize problems for 521 seventh graders, the teacher-in-the-loop setup forced a trade-off among them.[^c1]

## Mechanism

Personalizing one problem took about four minutes, and a ten-problem set about forty minutes. Forty minutes yields only one alternate version of each problem, whereas the plan was four versions per problem for four interests. The four-minute figure showed no evidence of falling as teachers gained expertise.[^c2] The authors conclude the only realistic option is broad grain, enacted at the level of the class's perceived interests.[^c3]

Students, however, valued small-grain connections to their own interests, and disliked specific references that did not match their taste (one likes music but hates a given artist).[^c4] Students rarely noticed depth problems (13 cases), though the researchers found many, so grain mattered more to students than depth; the authors still argue depth matters for seeing mathematics as a way to model the world.[^c5]

For asking and answering, the transferable point is my own reading: an asker (or generator) that tailors a question to an answerer pays an effort cost per tailoring, and that cost may not amortize. Coarse tailoring is cheap but mismatches individuals. Smaller grain is more feasible when the LLM faces the individual student directly.[^c4]

## Limits

One curriculum, one grade, one country, GPT-4-era tools and popular-culture interests only. Student reactions were feedback, not a measured learning or interest outcome compared against a no-personalization control, so the claim that students "want" finer grain is attitudinal. The time estimate comes from design sessions with researchers present, which may inflate it. Teacher-out-of-the-loop designs were not tested here.

## Related

- [[target-aware-query-construction]] — another case where who holds knowledge of the target changes what question construction costs

[^c1]: arxiv-2602-15876 — "We find that having a teacher-in-theloop results in generative AI-enhanced personalization being enacted at a relatively broad grain"
[^c2]: arxiv-2602-15876 — "We also did not find evidence that the 4-minute time"
[^c3]: arxiv-2602-15876 — "Thus, the only realistic option is for teachers to enact the"
[^c4]: arxiv-2602-15876 — "students appreciate specific, small-grain-size"
[^c5]: arxiv-2602-15876 — "we might"
