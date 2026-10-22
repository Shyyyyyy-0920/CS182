# Lecture 01: Introduction

## Practice Quiz

**100 marks: 12 True/False × 1; 12 multiple response × 2; 4 proofs/derivations × 10; 2 applications × 12.**

Answer in English. Every multiple-response question has four options and 1–3 correct answers. Exact set: 2 marks; nonempty proper correct subset: 1; any wrong option or no answer: 0. Use `Quiz.tex` to type your responses in its marked regions.

Primary source: [Introduction.pdf](../../lecture/Introduction.pdf). Page numbers start at the cover.

## A. True/False

**1.** In reinforcement learning, an action can be assessed through a reward received later rather than through an immediate correct-action label.

**2.** Unsupervised learning can discover structure even when no target output is supplied for each example.

**3.** Data science, as described in the lecture, includes machine learning and also activities such as visualization.

**4.** A useful learned model must exactly reproduce the complete process that generated the data.

**5.** Zero empirical classification error guarantees that all consistent hypotheses agree on every future input.

**6.** The fact that a stored target is a number is sufficient to classify the learning task as regression.

**7.** The model $h(x,w)=w_0+w_1x+w_2x^2$ is linear in its parameters even though it is nonlinear in $x$.

**8.** Once a hypothesis class and loss have been fixed, every possible optimization procedure must return the same predictor.

**9.** If axis-aligned rectangles have VC dimension four, every configuration of four planar points must be shattered.

**10.** Choosing squared loss rather than another loss can express an inductive bias, even after the model family has been fixed.

**11.** Increasing the sample size guarantees a strictly smaller error on every particular realized test set.

**12.** For a fixed dataset and hypothesis class, replacing a squared-error objective by twice that objective leaves its set of global minimizers unchanged.

## B. Multiple Response

**13.** Suppose $N$ training inputs are pairwise distinct real numbers. Select every valid statement about unregularized polynomial fitting.

- **A.** Exact interpolation removes the random noise from each target.
- **B.** A polynomial of degree at most $N-1$ can interpolate any assigned real targets.
- **C.** An interpolating polynomial is guaranteed to have the smallest expected test error among all candidate models.
- **D.** Allowing degree above $N-1$ can give different interpolating polynomials with identical training predictions.

**14.** A classifier mislabels exactly 3 of 12 training examples. Use the classification empirical-error definition on slide 39. Select every correct statement.

- **A.** Its empirical error under that definition is $1/4$.
- **B.** Its empirical error $E(h\mid X)$ is $3$.
- **C.** Nonzero empirical error proves that the learning code contains an arithmetic bug.
- **D.** Hidden attributes can never contribute to apparent noise because they are absent from the feature vector.

**15.** For a nonnegative integer $M$, let $\mathcal H_M=\{\sum_{j=0}^M w_jx^j:w_j\in\mathbb R\}$. Select every correct statement.

- **A.** $\mathcal H_M\subseteq\mathcal H_{M+1}$.
- **B.** The coefficient vector has $M+1$ entries.
- **C.** Different coefficient vectors always give different predictions on a fixed finite training set.
- **D.** A member of $\mathcal H_M$ must have degree exactly $M$.

**16.** Select every statement supported by the discussion of when machine learning is useful and how it is evaluated.

- **A.** A descriptive model is useless unless it also predicts a future target.
- **B.** An application is suitable for machine learning only if its data generation mechanism is already fully known.
- **C.** Computation time and storage requirements can matter alongside prediction accuracy.
- **D.** Machine learning can be useful when humans possess expertise but cannot explain it as explicit rules.

**17.** Two fixed candidate coefficient vectors have $(E(w_A),\|w_A\|_2^2)=(2,18)$ and $(E(w_B),\|w_B\|_2^2)=(5,2)$. Compare only these two candidates under $E(w)+\lambda\|w\|_2^2/2$, with $\lambda\geq0$. Select every correct statement.

- **A.** For every $\lambda>3/8$, candidate $B$ has the smaller objective.
- **B.** At $\lambda=0$, candidate $A$ has the smaller objective.
- **C.** These comparisons prove that one of these two candidates is the global minimizer over every coefficient vector.
- **D.** The candidates tie at $\lambda=3/8$.

**18.** Select every task that matches the learning role stated in the lecture.

- **A.** Grouping unlabeled customers by similarity is an unsupervised task.
- **B.** Assigning an email to spam or non-spam must be unsupervised learning because the email is text.
- **C.** Predicting a steering wheel angle from a camera image can be a regression task.
- **D.** Learning a policy to maximize delayed game rewards is a reinforcement learning task.

**19.** In a transaction sample, 80 customers buy tea, 50 buy biscuits, and 30 buy both. Select every correct statement about the sample conditional probabilities.

- **A.** Conditioning additionally on customer attributes must leave both conditional probabilities unchanged.
- **B.** The two conditional probabilities must be equal because the intersection event is the same.
- **C.** $P(\text{tea}\mid\text{biscuits})=3/5$.
- **D.** $P(\text{biscuits}\mid\text{tea})=3/8$.

**20.** Consider closed axis-aligned rectangles as positive-class regions. Assume at least one positive training example. Select every correct statement.

- **A.** If a negative example lies inside that smallest rectangle, the version space is empty.
- **B.** The smallest rectangle containing all positive examples must be contained in every consistent rectangle.
- **C.** Every rectangle consistent with the training sample must have the same area.
- **D.** There is always a unique largest consistent rectangle.

**21.** The lecture uses $E(w)=\tfrac12\sum_{n=1}^N(h(x_n,w)-y_n)^2$. Suppose $E(w)=18$ for $N=9$. Select every correct statement.

- **A.** The mean squared error is $4$.
- **B.** The RMS error has the same physical units as the target.
- **C.** Doubling every residual doubles the mean squared error.
- **D.** The RMS error is $2$.

**22.** Consider the fixed family $h(x;w)=w_0+w_1x$. Select every change that alters one of the three dimensions of a supervised learning algorithm.

- **A.** Replacing squared loss by absolute loss changes the error-function dimension.
- **B.** Renaming the coefficient vector without changing any formula necessarily changes the hypothesis class.
- **C.** Adding a feature $x^2$ with its own coefficient changes only the loss function while leaving the model family fixed.
- **D.** Keeping the objective but replacing exact minimization by a finite number of gradient steps necessarily changes the hypothesis class.

**23.** A team chooses polynomial degree by comparing validation errors. Select every sound statement about evaluation.

- **A.** A separate test set can assess the final selected procedure after model selection.
- **B.** The validation set helps compare candidate model choices.
- **C.** Repeatedly choosing hyperparameters to reduce the reported test error preserves the test set as an untouched final evaluation.
- **D.** The example 50/25/25 training/validation/test split is a compulsory ratio for every problem.

**24.** A four-class classifier is implemented through four one-versus-rest binary classifiers. Select every correct statement.

- **A.** The reduction implies that one learning algorithm is universally best for every dataset.
- **B.** Every binary classifier is guaranteed to have zero empirical error merely because the task was decomposed.
- **C.** Several binary classifiers may predict positive on the same new example, so a final decision rule can be necessary.
- **D.** Each binary target indicates whether an example belongs to its associated class.

## 25. Least squares as orthogonality, including redundant features [10 marks]

**(a) [3 marks]** Let $\Phi\in\mathbb R^{N\times d}$, $y\in\mathbb R^N$, and $E(w)=\tfrac12\|\Phi w-y\|_2^2$. Show that a minimizer $w_*$ must satisfy $\Phi^T(\Phi w_*-y)=0$, by examining perturbations rather than quoting an inverse formula.

**(b) [4 marks]** Prove that these normal equations are sufficient for global optimality. Interpret them geometrically and justify that a minimizer exists even if $\Phi$ has dependent columns.

**(c) [3 marks]** If $u$ and $v$ are both minimizers, prove that $\Phi u=\Phi v$. State exactly when their coefficient vectors can differ.

## 26. Why a larger polynomial class cannot worsen optimal training RMS [10 marks]

**(a) [3 marks]** For a fixed nonempty training set, define $E_M^*=\min_{h\in\mathcal H_M}\tfrac12\sum_n(h(x_n)-y_n)^2$, with $\mathcal H_M$ as in the multiple-response section. Prove $E_{M+1}^*\leq E_M^*$ and the corresponding inequality for optimal training RMS.

**(b) [4 marks]** Let $\Phi_M$ be the degree-$M$ design matrix, $\phi=(x_1^{M+1},\ldots,x_N^{M+1})^T$, and $r=\Phi_M w_*-y$ at a smaller-class minimizer. Prove that the two optimal errors are equal if and only if $\phi^Tr=0$. Explain why an added feature already in $\operatorname{col}(\Phi_M)$ cannot improve training error.

**(c) [3 marks]** For the three observations $(-1,1),(0,0),(1,1)$, find the optimal constant, show that adding a linear term does not improve its error, and exhibit a quadratic with zero training error. Why does the monotonicity proof say nothing comparable about test RMS?

## 27. Regularization: prove the tradeoff without an inverse formula [10 marks]

**(a) [4 marks]** Let $F(w)=\tfrac12\|\Phi w-y\|_2^2$, $R(w)=\tfrac12\|w\|_2^2$, and $w_i$ be a global minimizer of $F(w)+\lambda_iR(w)$, where $0\leq\lambda_1<\lambda_2$. Prove $R(w_2)\leq R(w_1)$. Do not use a closed-form minimizer.

**(b) [3 marks]** Prove $F(w_1)\leq F(w_2)$. Does either result imply a monotone test error or a strictly changing coefficient norm?

**(c) [3 marks]** For $\lambda>0$, prove that the penalized squared-error objective has a unique minimizer even if $\Phi$ has dependent columns. Use a strict-convexity or midpoint argument.

## 28. The VC dimension of axis-aligned rectangles [10 marks]

**(a) [5 marks]** Let $\mathcal R$ contain all closed axis-aligned rectangles in $\mathbb R^2$, with label 1 inside and 0 outside. Prove that $\mathcal R$ shatters $\{(-1,0),(1,0),(0,-1),(0,1)\}$. Cover all possible subsets, including the empty subset.

**(b) [5 marks]** Prove that no set of five distinct planar points is shattered, allowing ties in coordinate extremes. Deduce the exact VC dimension.

## 29. Compare candidate polynomials, regularization, and validation [12 marks]

**(a) [3 marks]** Two supplied candidate models are $h_A(x)=\tfrac12+\tfrac12x$ and $h_B(x)=x^2$. The training sample is $(0,0),(1,1),(2,4)$. Compute each model\'s half-sum squared error and training RMS. You are comparing these two candidates only.

**(b) [3 marks]** The validation sample is $(1/2,1),(3/2,3/2)$. Compute validation RMS for both candidates and choose the candidate using this criterion.

**(c) [4 marks]** Embed both models in the degree-two coefficient space ordered as $(1,x,x^2)$, and compare $E+\lambda\|w\|_2^2/2$. Find the value of $\lambda$ at which they tie, and identify the better candidate at $\lambda=14$. Does this comparison establish a global ridge solution?

**(d) [2 marks]** Describe a valid use of an additional test set after choosing the candidate. Explain why the validation RMS of the selected candidate is not automatically an unbiased final assessment of the entire selection process.

## 30. Consistent rectangles and predictions that data do not determine [12 marks]

**(a) [3 marks]** The positive examples are $(2,3),(4,5)$; the negative examples are $(1,4),(5,4),(3,6)$. Find the smallest closed axis-aligned rectangle containing the positives and verify its training error.

**(b) [4 marks]** Construct a second consistent rectangle that disagrees with $S$ at $q=(1.7,4)$. State what this proves about predicting $q$ from consistency alone.

**(c) [3 marks]** Which label is forced by all consistent rectangles at $a=(3,4)$? Which label is forced at the already observed negative point $b=(1,4)$? Explain using the geometry and the definition of consistency.

**(d) [2 marks]** An additional training record gives $(3,4)$ a negative label while keeping all previous labels. Determine the new version space and explain why optimizing rectangle boundaries cannot obtain zero training error.

