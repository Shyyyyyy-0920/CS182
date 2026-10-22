# CS182 — Quizzes by Lecture

Each lecture has a separate English 100-mark quiz: 12 misconception T/F questions, 12 multiple-response questions, 4 proof/formula-derivation problems, and 2 application problems. This design allows a complete check immediately after studying that lecture.

The multiple-response rule is unchanged: exactly four options, 1–3 correct; complete correct set = 2, nonempty proper correct subset = 1, any wrong selection or blank = 0. Proofs require intermediate steps, assumptions, and dimensions.

| Lecture | Editable TeX | Questions | Worked solutions |
|---|---|---|---|
| 01 · Introduction | [Quiz.tex](L01_Introduction/Quiz.tex) | [PDF](L01_Introduction/Quiz.pdf) · [MD](L01_Introduction/Quiz.md) | [PDF](L01_Introduction/Solutions.pdf) · [TeX](L01_Introduction/Solutions.tex) · [MD](L01_Introduction/Solutions.md) |
| 02 · Linear Algebra | [Quiz.tex](L02_Linear_Algebra/Quiz.tex) | [PDF](L02_Linear_Algebra/Quiz.pdf) · [MD](L02_Linear_Algebra/Quiz.md) | [PDF](L02_Linear_Algebra/Solutions.pdf) · [TeX](L02_Linear_Algebra/Solutions.tex) · [MD](L02_Linear_Algebra/Solutions.md) |
| 03 · Probability and Statistics | [Quiz.tex](L03_Probability_Statistics/Quiz.tex) | [PDF](L03_Probability_Statistics/Quiz.pdf) · [MD](L03_Probability_Statistics/Quiz.md) | [PDF](L03_Probability_Statistics/Solutions.pdf) · [TeX](L03_Probability_Statistics/Solutions.tex) · [MD](L03_Probability_Statistics/Solutions.md) |
| 04 · Optimization Primer | [Quiz.tex](L04_Optimization_Primer/Quiz.tex) | [PDF](L04_Optimization_Primer/Quiz.pdf) · [MD](L04_Optimization_Primer/Quiz.md) | [PDF](L04_Optimization_Primer/Solutions.pdf) · [TeX](L04_Optimization_Primer/Solutions.tex) · [MD](L04_Optimization_Primer/Solutions.md) |
| 05 · Bayesian Decision Theory | [Quiz.tex](L05_Bayesian_Decision_Theory/Quiz.tex) | [PDF](L05_Bayesian_Decision_Theory/Quiz.pdf) · [MD](L05_Bayesian_Decision_Theory/Quiz.md) | [PDF](L05_Bayesian_Decision_Theory/Solutions.pdf) · [TeX](L05_Bayesian_Decision_Theory/Solutions.tex) · [MD](L05_Bayesian_Decision_Theory/Solutions.md) |
| 06 · Parameter Estimation | [Quiz.tex](L06_Parameter_Estimation/Quiz.tex) | [PDF](L06_Parameter_Estimation/Quiz.pdf) · [MD](L06_Parameter_Estimation/Quiz.md) | [PDF](L06_Parameter_Estimation/Solutions.pdf) · [TeX](L06_Parameter_Estimation/Solutions.tex) · [MD](L06_Parameter_Estimation/Solutions.md) |
| 07 · Linear Discrimination | [Quiz.tex](L07_Linear_Discrimination/Quiz.tex) | [PDF](L07_Linear_Discrimination/Quiz.pdf) · [MD](L07_Linear_Discrimination/Quiz.md) | [PDF](L07_Linear_Discrimination/Solutions.pdf) · [TeX](L07_Linear_Discrimination/Solutions.tex) · [MD](L07_Linear_Discrimination/Solutions.md) |

## Type your answers

Open the corresponding `Quiz.tex`. Fill the second brace pair in `\SetAnswer{TF01}{}` ... `\SetAnswer{TF12}{}` and `\SetAnswer{MC13}{}` ... `\SetAnswer{MC24}{}`. Search `BEGIN ANSWER Q25(a)` and the analogous markers to type each proof/application subpart. Delete its `\AnswerBlank` after writing, or change `\BlankAnswerHeight` to `0mm`. Printed answers and reasoning should be in English; Chinese source comments identify the editing regions. Compile twice with pdfLaTeX. Each TeX file is standalone.

Solutions are separate and include a quick key, an explanation for each option, full mathematical steps, subpart point allocations, and lecture page references. `author_audit.json` also contains answer keys and is intended for checking after attempting the quiz.

The original integrated L1–L6 PDFs remain available as later review papers. The current series uses 30 focused questions per lecture rather than copying that integrated paper into seven files. The source JSONs are read from `source/`; rebuilding preserves an existing `Quiz.tex` so that typed answers are not erased.
