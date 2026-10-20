---
description: "A representation is judged on two axes: how succinct it is, and which queries and transformations it answers in polynomial time; the two trade off across target languages."
aliases: ["succinctness versus tractability", "knowledge compilation languages", "target compilation language analysis"]
sources: ["darwiche-2002"]
---
# Knowledge compilation map

Knowledge compilation moves work from answer time to preparation time: a knowledge base is translated once into a target language, and later queries run against the compiled form. Darwiche and Marquis (2002) propose that any such target language be analysed along two dimensions: "the succinctness of the target compilation language, and the class of queries and transformations that the language supports in polytime".[^c1]

The consequence for asking is that the cost of a question is not a property of the question alone. It depends on the form the knowledge is held in. A query that is cheap on one representation can be expensive on another, and the form that answers the most queries cheaply is generally larger. Choosing a representation therefore fixes which questions are affordable to answer. Succinctness measures how small a language can express a given knowledge base. The map ranks languages on this and on the set of queries each one supports in polynomial time.

The authors argue the analysis is needed to place a new compilation approach among existing ones: "We argue that such analysis is necessary for placing new compilation approaches within the context of existing ones."[^c2] They provide a map covering "a large number of existing target compilation languages".[^c3] They also go past flat CNF and DNF to a "richer, nested class based on directed acyclic graphs (such as OBDDs)", which they show includes many target languages.[^c4]

## Limits

The text available to the wiki is only the journal landing page with the abstract. The specific succinctness orderings and the query-by-language tables are not in it, so this note records the framing and none of the results. Nothing here is measured on question-asking or answering. Reading it as a rule for choosing a question representation is my own inference, not the paper's claim. Polynomial time is a worst-case, asymptotic criterion and says nothing about practical cost.

## Related

- [[backbone-of-a-formula]] — a query on a propositional formula whose cost depends on its representation
- [[dialogue-to-state-compilation]] — compiling dialogue into a state for later querying
- [[knowledge-based-design]] — representation choice shaping what can be asked
- [[agm-belief-revision]] — a transformation applied to a knowledge base

[^c1]: darwiche-2002 — "the succinctness of the target compilation language, and the class of queries and transformations that the language supports in polytime"
[^c2]: darwiche-2002 — "We argue that such analysis is necessary for placing new compilation approaches within the context of existing ones."
[^c3]: darwiche-2002 — "analyzes a large number of existing target compilation languages according to their succinctness and their polytime transformations and queries"
[^c4]: darwiche-2002 — "a richer, nested class based on directed acyclic graphs (such as OBDDs)"
