# Lecture 01: Introduction

## Worked Solutions

**100 marks: 12 True/False × 1; 12 multiple response × 2; 4 proofs/derivations × 10; 2 applications × 12.**

Answer in English. Every multiple-response question has four options and 1–3 correct answers. Exact set: 2 marks; nonempty proper correct subset: 1; any wrong option or no answer: 0. Use `Quiz.tex` to type your responses in its marked regions.

Primary source: [Introduction.pdf](../../lecture/Introduction.pdf). Page numbers start at the cover.

## A. True/False

**1.** In reinforcement learning, an action can be assessed through a reward received later rather than through an immediate correct-action label.

**True.** The lecture distinguishes delayed reward or penalty and the credit assignment problem from supervised outputs.

*PDF p.18.*

**2.** Unsupervised learning can discover structure even when no target output is supplied for each example.

**True.** Clustering, density estimation, and dimensionality reduction are examples of finding structure without supplied outputs.

*PDF p.17.*

**3.** Data science, as described in the lecture, includes machine learning and also activities such as visualization.

**True.** The lecture describes data science or data analytics as a broader concept including statistics, machine learning, data mining, and data visualization.

*PDF p.4.*

**4.** A useful learned model must exactly reproduce the complete process that generated the data.

**False.** The lecture allows a useful approximation; exact replication of the complete process is unnecessary.

*PDF p.7.*

**5.** Zero empirical classification error guarantees that all consistent hypotheses agree on every future input.

**False.** Different hypotheses can fit the same observed labels perfectly and make different predictions outside the training sample.

*PDF p.39.*

**6.** The fact that a stored target is a number is sufficient to classify the learning task as regression.

**False.** Numbers may encode categories, such as 0 and 1 for class labels. The meaning and prediction task determine whether this is classification or regression.

*PDF pp.15,36,45.*

**7.** The model $h(x,w)=w_0+w_1x+w_2x^2$ is linear in its parameters even though it is nonlinear in $x$.

**True.** Each parameter multiplies a fixed feature of the input; there are no products or nonlinear transformations of the parameters.

*PDF p.21.*

**8.** Once a hypothesis class and loss have been fixed, every possible optimization procedure must return the same predictor.

**False.** An algorithm may stop early, find a local solution, or choose among multiple minimizers. Optimization is a separate dimension of a learning algorithm.

*PDF p.52.*

**9.** If axis-aligned rectangles have VC dimension four, every configuration of four planar points must be shattered.

**False.** VC dimension requires the existence of a shattered configuration of that size. Some configurations of four points cannot be shattered.

*PDF p.41.*

**10.** Choosing squared loss rather than another loss can express an inductive bias, even after the model family has been fixed.

**True.** The lecture identifies both the assumed function family and the squared-error selection criterion as inductive biases.

*PDF p.48.*

**11.** Increasing the sample size guarantees a strictly smaller error on every particular realized test set.

**False.** The triple tradeoff describes a general statistical tendency. A particular finite test error can stay unchanged or increase.

*PDF p.49.*

**12.** For a fixed dataset and hypothesis class, replacing a squared-error objective by twice that objective leaves its set of global minimizers unchanged.

**True.** Multiplication by a strictly positive constant preserves every comparison of objective values. This does not assert that an arbitrary numerical optimizer follows the same path.

*PDF pp.22,45.*

## B. Multiple Response

**13.** Suppose $N$ training inputs are pairwise distinct real numbers. Select every valid statement about unregularized polynomial fitting.

- **A.** Exact interpolation removes the random noise from each target. **Incorrect:** An interpolant matches the observed noisy values and may fit the noise itself.
- **B.** A polynomial of degree at most $N-1$ can interpolate any assigned real targets. **Correct:** The square Vandermonde system is invertible for distinct input values.
- **C.** An interpolating polynomial is guaranteed to have the smallest expected test error among all candidate models. **Incorrect:** Zero training error does not guarantee generalization.
- **D.** Allowing degree above $N-1$ can give different interpolating polynomials with identical training predictions. **Correct:** Add a nonzero multiple of the polynomial that vanishes at every training input.

**Correct set: B, D.** *PDF pp.23-24; supplementary derivation from PDF pp.21-24.*

**14.** A classifier mislabels exactly 3 of 12 training examples. Use the classification empirical-error definition on slide 39. Select every correct statement.

- **A.** Its empirical error under that definition is $1/4$. **Incorrect:** One quarter is the error rate, which includes an additional division by N.
- **B.** Its empirical error $E(h\mid X)$ is $3$. **Correct:** That slide defines a sum of misclassification indicators.
- **C.** Nonzero empirical error proves that the learning code contains an arithmetic bug. **Incorrect:** Noise, limited model capacity, or imperfect optimization can produce nonzero empirical error without an arithmetic bug.
- **D.** Hidden attributes can never contribute to apparent noise because they are absent from the feature vector. **Incorrect:** The lecture explicitly lists hidden or latent attributes as a source of noise.

**Correct set: B.** *PDF pp.39,42.*

**15.** For a nonnegative integer $M$, let $\mathcal H_M=\{\sum_{j=0}^M w_jx^j:w_j\in\mathbb R\}$. Select every correct statement.

- **A.** $\mathcal H_M\subseteq\mathcal H_{M+1}$. **Correct:** Set the extra coefficient to zero to represent every old polynomial.
- **B.** The coefficient vector has $M+1$ entries. **Correct:** There is one coefficient for each power from zero through M.
- **C.** Different coefficient vectors always give different predictions on a fixed finite training set. **Incorrect:** A finite evaluation map may have a nontrivial nullspace, especially when there are more coefficients than distinct input points.
- **D.** A member of $\mathcal H_M$ must have degree exactly $M$. **Incorrect:** Its leading coefficients may vanish; constants are also members.

**Correct set: A, B.** *PDF pp.21-23.*

**16.** Select every statement supported by the discussion of when machine learning is useful and how it is evaluated.

- **A.** A descriptive model is useless unless it also predicts a future target. **Incorrect:** Descriptive models may provide knowledge about data without a future-target task.
- **B.** An application is suitable for machine learning only if its data generation mechanism is already fully known. **Incorrect:** The mechanism may be partly unknown while containing exploitable regularities.
- **C.** Computation time and storage requirements can matter alongside prediction accuracy. **Correct:** The lecture lists accuracy, time complexity, and space complexity as performance criteria.
- **D.** Machine learning can be useful when humans possess expertise but cannot explain it as explicit rules. **Correct:** Speech and vision illustrate expertise that is difficult to articulate.

**Correct set: C, D.** *PDF pp.6-8.*

**17.** Two fixed candidate coefficient vectors have $(E(w_A),\|w_A\|_2^2)=(2,18)$ and $(E(w_B),\|w_B\|_2^2)=(5,2)$. Compare only these two candidates under $E(w)+\lambda\|w\|_2^2/2$, with $\lambda\geq0$. Select every correct statement.

- **A.** For every $\lambda>3/8$, candidate $B$ has the smaller objective. **Correct:** Its smaller squared norm gives it the smaller objective slope.
- **B.** At $\lambda=0$, candidate $A$ has the smaller objective. **Correct:** The data-fitting errors are 2 and 5.
- **C.** These comparisons prove that one of these two candidates is the global minimizer over every coefficient vector. **Incorrect:** Comparing two supplied candidates excludes no third candidate with a still lower objective.
- **D.** The candidates tie at $\lambda=3/8$. **Correct:** Solve 2+9 lambda=5+lambda.

**Correct set: A, B, D.** *PDF p.28.*

**18.** Select every task that matches the learning role stated in the lecture.

- **A.** Grouping unlabeled customers by similarity is an unsupervised task. **Correct:** Customer segmentation is a clustering example.
- **B.** Assigning an email to spam or non-spam must be unsupervised learning because the email is text. **Incorrect:** The input medium does not determine the paradigm; labeled spam detection is classification.
- **C.** Predicting a steering wheel angle from a camera image can be a regression task. **Correct:** The output is a numerical control angle, matching the regression examples.
- **D.** Learning a policy to maximize delayed game rewards is a reinforcement learning task. **Correct:** The policy is learned through rewards and trial and error.

**Correct set: A, C, D.** *PDF pp.14,16-18.*

**19.** In a transaction sample, 80 customers buy tea, 50 buy biscuits, and 30 buy both. Select every correct statement about the sample conditional probabilities.

- **A.** Conditioning additionally on customer attributes must leave both conditional probabilities unchanged. **Incorrect:** Customer attributes can distinguish groups with different purchasing behavior, so adding them to the conditioning variables can change the probabilities.
- **B.** The two conditional probabilities must be equal because the intersection event is the same. **Incorrect:** The intersection counts agree, but the conditioning populations have different sizes.
- **C.** $P(\text{tea}\mid\text{biscuits})=3/5$. **Correct:** Conditioning on biscuits uses the 50 biscuit buyers as the denominator.
- **D.** $P(\text{biscuits}\mid\text{tea})=3/8$. **Correct:** The denominator is the 80 customers who buy tea, so the fraction is 30/80.

**Correct set: C, D.** *PDF p.11.*

**20.** Consider closed axis-aligned rectangles as positive-class regions. Assume at least one positive training example. Select every correct statement.

- **A.** If a negative example lies inside that smallest rectangle, the version space is empty. **Correct:** Every rectangle containing the positives also contains that negative example.
- **B.** The smallest rectangle containing all positive examples must be contained in every consistent rectangle. **Correct:** Every consistent rectangle must extend to each coordinate extreme of the positive examples.
- **C.** Every rectangle consistent with the training sample must have the same area. **Incorrect:** Several boundary positions can preserve the observed labels while changing the area.
- **D.** There is always a unique largest consistent rectangle. **Incorrect:** Negative examples can force tradeoffs between expansion in different directions, giving multiple incomparable maximal rectangles.

**Correct set: A, B.** *PDF pp.37-40.*

**21.** The lecture uses $E(w)=\tfrac12\sum_{n=1}^N(h(x_n,w)-y_n)^2$. Suppose $E(w)=18$ for $N=9$. Select every correct statement.

- **A.** The mean squared error is $4$. **Correct:** The sum of squared residuals is 36, divided by 9.
- **B.** The RMS error has the same physical units as the target. **Correct:** Taking the square root restores the units of a residual.
- **C.** Doubling every residual doubles the mean squared error. **Incorrect:** Squaring makes the mean squared error four times as large; RMS doubles.
- **D.** The RMS error is $2$. **Correct:** Its square is 2E/N=36/9=4.

**Correct set: A, B, D.** *PDF pp.22,24,45.*

**22.** Consider the fixed family $h(x;w)=w_0+w_1x$. Select every change that alters one of the three dimensions of a supervised learning algorithm.

- **A.** Replacing squared loss by absolute loss changes the error-function dimension. **Correct:** The way prediction errors are scored changes.
- **B.** Renaming the coefficient vector without changing any formula necessarily changes the hypothesis class. **Incorrect:** A purely notational renaming leaves the same prediction functions available.
- **C.** Adding a feature $x^2$ with its own coefficient changes only the loss function while leaving the model family fixed. **Incorrect:** Adding a freely weighted feature expands the model family; the same squared loss may still be used.
- **D.** Keeping the objective but replacing exact minimization by a finite number of gradient steps necessarily changes the hypothesis class. **Incorrect:** This changes the optimization procedure; the set of allowable prediction functions can remain the same.

**Correct set: A.** *PDF p.52.*

**23.** A team chooses polynomial degree by comparing validation errors. Select every sound statement about evaluation.

- **A.** A separate test set can assess the final selected procedure after model selection. **Correct:** Keeping test cases outside selection avoids adapting the choice to their observed errors.
- **B.** The validation set helps compare candidate model choices. **Correct:** Model selection needs an estimate of performance beyond the training examples.
- **C.** Repeatedly choosing hyperparameters to reduce the reported test error preserves the test set as an untouched final evaluation. **Incorrect:** Those test outcomes have then influenced the selected model.
- **D.** The example 50/25/25 training/validation/test split is a compulsory ratio for every problem. **Incorrect:** The lecture presents those percentages as an example, and also mentions resampling.

**Correct set: A, B.** *PDF pp.48-50.*

**24.** A four-class classifier is implemented through four one-versus-rest binary classifiers. Select every correct statement.

- **A.** The reduction implies that one learning algorithm is universally best for every dataset. **Incorrect:** The no-free-lunch discussion rejects a universally best algorithm.
- **B.** Every binary classifier is guaranteed to have zero empirical error merely because the task was decomposed. **Incorrect:** The reduction does not make the subproblems perfectly separable.
- **C.** Several binary classifiers may predict positive on the same new example, so a final decision rule can be necessary. **Correct:** Independently learned binary decisions need not be mutually exclusive.
- **D.** Each binary target indicates whether an example belongs to its associated class. **Correct:** The reduction compares one class against the other classes.

**Correct set: C, D.** *PDF pp.43,52; supplementary interpretation from PDF p.43.*

## 25. Least squares as orthogonality, including redundant features [10 marks]

**(a) [3 marks]** Let $\Phi\in\mathbb R^{N\times d}$, $y\in\mathbb R^N$, and $E(w)=\tfrac12\|\Phi w-y\|_2^2$. Show that a minimizer $w_*$ must satisfy $\Phi^T(\Phi w_*-y)=0$, by examining perturbations rather than quoting an inverse formula.

**Worked solution:** For any direction $v$ and real $t$, set $r=\Phi w_*-y$. Expanding gives 
$$
E(w_*+tv)-E(w_*)=t\,v^T\Phi^Tr+\tfrac12t^2\|\Phi v\|_2^2.
$$
 At a minimum the linear coefficient must vanish for every $v$, since otherwise one sufficiently small choice of the sign of $t$ decreases the objective. Thus $v^T\Phi^Tr=0$ for every direction, giving $\Phi^Tr=0$. Award one mark for the expansion, one for the sign-of-perturbation argument, and one for the normal equations.

**(b) [4 marks]** Prove that these normal equations are sufficient for global optimality. Interpret them geometrically and justify that a minimizer exists even if $\Phi$ has dependent columns.

**Worked solution:** If $\Phi^T(\Phi w_*-y)=0$, the same expansion with $t=1$ yields 
$$
E(w_*+v)=E(w_*)+\tfrac12\|\Phi v\|_2^2\geq E(w_*).
$$
 Hence the condition is sufficient. It says that the residual is orthogonal to every vector in the column space of $\Phi$. This column space is a finite-dimensional, closed subspace of $\mathbb R^N$. An orthonormal basis $q_1,\ldots,q_r$ gives the closest vector $p=\sum_i q_i(q_i^Ty)$, whose residual is orthogonal to the subspace. Since $p$ is in the column space, there exists a coefficient vector with $\Phi w_*=p$. This establishes existence without invertibility. Award two marks for sufficiency, one for orthogonality, and one for existence.

**(c) [3 marks]** If $u$ and $v$ are both minimizers, prove that $\Phi u=\Phi v$. State exactly when their coefficient vectors can differ.

**Worked solution:** Apply the sufficient-condition expansion at $u$ with perturbation $v-u$: 
$$
0=E(v)-E(u)=\tfrac12\|\Phi(v-u)\|_2^2.
$$
 Therefore the fitted training predictions are unique. The coefficient vectors can differ precisely by vectors in $\operatorname{null}(\Phi)$: adding such a vector preserves all predictions and the objective, and the preceding identity shows every pair of minimizers differs this way. Coefficients are unique if and only if $\Phi$ has full column rank. Award one mark each for the equality, the nullspace characterization, and the uniqueness condition.

*Source: Supplementary derivation from PDF pp.21-22,45.*

## 26. Why a larger polynomial class cannot worsen optimal training RMS [10 marks]

**(a) [3 marks]** For a fixed nonempty training set, define $E_M^*=\min_{h\in\mathcal H_M}\tfrac12\sum_n(h(x_n)-y_n)^2$, with $\mathcal H_M$ as in the multiple-response section. Prove $E_{M+1}^*\leq E_M^*$ and the corresponding inequality for optimal training RMS.

**Worked solution:** Every polynomial in $\mathcal H_M$ is also in $\mathcal H_{M+1}$ by setting the new coefficient to zero. Thus an optimizer from the smaller class is a feasible candidate for the larger class, so its minimum cannot be smaller than the larger minimum: $E_{M+1}^*\leq E_M^*$. Because $N>0$, the map $a\mapsto\sqrt{2a/N}$ is increasing for nonnegative $a$, giving $\mathrm{RMS}_{M+1}^*\leq\mathrm{RMS}_M^*$. Award one mark for inclusion and one for each inequality.

**(b) [4 marks]** Let $\Phi_M$ be the degree-$M$ design matrix, $\phi=(x_1^{M+1},\ldots,x_N^{M+1})^T$, and $r=\Phi_M w_*-y$ at a smaller-class minimizer. Prove that the two optimal errors are equal if and only if $\phi^Tr=0$. Explain why an added feature already in $\operatorname{col}(\Phi_M)$ cannot improve training error.

**Worked solution:** The old residual satisfies $\Phi_M^Tr=0$. If also $\phi^Tr=0$, the zero-extended vector $(w_*^T,0)^T$ satisfies the normal equations for $[\Phi_M\ \phi]$, so it is a larger-class minimizer with the same objective. Conversely, if the optimal errors agree, this zero-extended vector attains the larger optimum and must satisfy its normal equations, including $\phi^Tr=0$. If $\phi=\Phi_Ma$, then $\phi^Tr=a^T\Phi_M^Tr=0$, so equality follows. Award one mark for the old orthogonality, two for the two implications, and one for the column-space consequence.

**(c) [3 marks]** For the three observations $(-1,1),(0,0),(1,1)$, find the optimal constant, show that adding a linear term does not improve its error, and exhibit a quadratic with zero training error. Why does the monotonicity proof say nothing comparable about test RMS?

**Worked solution:** The best constant is $2/3$: completing the square in $(c-1)^2+c^2+(c-1)^2$ yields $3(c-2/3)^2+2/3$. Its residual is $(-1/3,2/3,-1/3)^T$ for prediction minus target, and its inner product with the added feature $(-1,0,1)^T$ is zero. Thus the best affine model has the same $E=1/3$ and RMS $\sqrt2/3$. The polynomial $h(x)=x^2$ interpolates all three observations and gives zero error. Test error is evaluated on other points and is not the objective minimized over the nested training classes, so it need not decrease. Award one mark for the constant and error, one for the linear/quadratic comparison, and one for the test-error explanation.

*Source: Supplementary derivation from PDF pp.21-24,48-49.*

## 27. Regularization: prove the tradeoff without an inverse formula [10 marks]

**(a) [4 marks]** Let $F(w)=\tfrac12\|\Phi w-y\|_2^2$, $R(w)=\tfrac12\|w\|_2^2$, and $w_i$ be a global minimizer of $F(w)+\lambda_iR(w)$, where $0\leq\lambda_1<\lambda_2$. Prove $R(w_2)\leq R(w_1)$. Do not use a closed-form minimizer.

**Worked solution:** Optimality at the two parameter values gives 
$$
F(w_1)+\lambda_1R(w_1)\leq F(w_2)+\lambda_1R(w_2),
$$

$$
F(w_2)+\lambda_2R(w_2)\leq F(w_1)+\lambda_2R(w_1).
$$
 Adding and rearranging yields $(\lambda_2-\lambda_1)(R(w_2)-R(w_1))\leq0$. The coefficient is strictly positive, so $R(w_2)\leq R(w_1)$. The proof allows nonunique minimizers. Award one mark for each optimality inequality and two for the conclusion with the correct sign.

**(b) [3 marks]** Prove $F(w_1)\leq F(w_2)$. Does either result imply a monotone test error or a strictly changing coefficient norm?

**Worked solution:** The first optimality inequality rearranges to 
$$
F(w_1)-F(w_2)\leq\lambda_1\bigl(R(w_2)-R(w_1)\bigr)\leq0.
$$
 Thus the unpenalized training error cannot decrease as the penalty increases. Equality is possible; for example, if $y=0$, $w=0$ minimizes the objective for every parameter. Test error is a different quantity and can first fall and then rise; neither inequality controls it. Award one mark for the data-fit inequality, one for the equality example, and one for the test-error limitation.

**(c) [3 marks]** For $\lambda>0$, prove that the penalized squared-error objective has a unique minimizer even if $\Phi$ has dependent columns. Use a strict-convexity or midpoint argument.

**Worked solution:** Existence follows because the objective is continuous and at least $\lambda\|w\|_2^2/2$, so it tends to infinity as $\|w\|_2\to\infty$. For distinct $u,v$, the squared-norm midpoint identity gives 
$$
J((u+v)/2)=\tfrac12J(u)+\tfrac12J(v)-\tfrac18\|\Phi(u-v)\|_2^2-\tfrac{\lambda}{8}\|u-v\|_2^2.
$$
 The final term is strictly negative. Two distinct minimizers would therefore have a midpoint with smaller objective, a contradiction. Award one mark for existence, one for the identity or strict-convexity argument, and one for uniqueness.

*Source: Supplementary derivation from PDF pp.28-32.*

## 28. The VC dimension of axis-aligned rectangles [10 marks]

**(a) [5 marks]** Let $\mathcal R$ contain all closed axis-aligned rectangles in $\mathbb R^2$, with label 1 inside and 0 outside. Prove that $\mathcal R$ shatters $\{(-1,0),(1,0),(0,-1),(0,1)\}$. Cover all possible subsets, including the empty subset.

**Worked solution:** For a nonempty subset $S$ of these four points, take its coordinatewise bounding rectangle. Each omitted point is the unique extreme in one coordinate: the left point has x=-1, the right point x=1, the lower point y=-1, and the upper point y=1. If that point is omitted, the corresponding extreme bound of the rectangle moves strictly inward, excluding it. Every selected point is included by construction. Singleton subsets may use degenerate rectangles; if strictly positive side lengths are required, expand the bounding box slightly without reaching any omitted point. For the empty subset, use a small rectangle far from the four points. Thus each of the 16 labelings is realizable. Award two marks for the bounding-box construction, two for exclusion of omitted extremes, and one for the empty/singleton cases.

**(b) [5 marks]** Prove that no set of five distinct planar points is shattered, allowing ties in coordinate extremes. Deduce the exact VC dimension.

**Worked solution:** From any five-point set, select one point attaining minimum x, one attaining maximum x, one attaining minimum y, and one attaining maximum y. Some selections may coincide, so their union $T$ has at most four points. Choose a remaining point $z\notin T$. Label every point of $T$ positive and every point outside $T$ negative. Any closed axis-aligned rectangle containing the positive extremes must contain the entire bounding box of the five-point set, including $z$. It therefore cannot realize this labeling. This argument remains valid when extremes are tied because one selected representative at each extreme is sufficient to force the bound. Hence no five-point set is shattered. Any larger shattered set would have a shattered five-point subset, so the VC dimension is at most four; the construction in the first part makes it exactly four. Award two marks for selecting the at-most-four extremes, two for the impossible labeling, and one for the conclusion.

*Source: PDF p.41; supplementary proof from PDF pp.37-41.*

## 29. Compare candidate polynomials, regularization, and validation [12 marks]

**(a) [3 marks]** Two supplied candidate models are $h_A(x)=\tfrac12+\tfrac12x$ and $h_B(x)=x^2$. The training sample is $(0,0),(1,1),(2,4)$. Compute each model\'s half-sum squared error and training RMS. You are comparing these two candidates only.

**Worked solution:** Model A predicts $(1/2,1,3/2)$, so its residuals are $(1/2,0,-5/2)$. The squared-residual sum is $1/4+25/4=13/2$, giving $E_A=13/4$ and RMS $\sqrt{13/6}$. Model B predicts $(0,1,4)$, so $E_B=0$ and RMS is zero. Award one mark for the predictions or residuals, one for the half-sum errors, and one for the RMS values.

**(b) [3 marks]** The validation sample is $(1/2,1),(3/2,3/2)$. Compute validation RMS for both candidates and choose the candidate using this criterion.

**Worked solution:** Model A predicts $(3/4,5/4)$, giving residuals $(-1/4,-1/4)$; its mean squared error is $1/16$ and RMS is $1/4$. Model B predicts $(1/4,9/4)$, giving residuals $(-3/4,3/4)$; its mean squared error is $9/16$ and RMS is $3/4$. Select A. The zero training error of B did not give the better validation result. Award one mark per RMS and one for the selection.

**(c) [4 marks]** Embed both models in the degree-two coefficient space ordered as $(1,x,x^2)$, and compare $E+\lambda\|w\|_2^2/2$. Find the value of $\lambda$ at which they tie, and identify the better candidate at $\lambda=14$. Does this comparison establish a global ridge solution?

**Worked solution:** The vectors are $w_A=(1/2,1/2,0)^T$ and $w_B=(0,0,1)^T$, with squared norms $1/2$ and 1. Therefore 
$$
J_A=13/4+\lambda/4,\qquad J_B=\lambda/2.
$$
 They tie at $\lambda=13$. At 14, $J_A=27/4=6.75$ and $J_B=7$, so A wins among these candidates. This does not establish the global minimizer over all degree-two coefficient vectors, because other coefficients have not been optimized. Award one mark for the vectors/norms, one for the objectives, one for the threshold and numerical comparison, and one for the limitation.

**(d) [2 marks]** Describe a valid use of an additional test set after choosing the candidate. Explain why the validation RMS of the selected candidate is not automatically an unbiased final assessment of the entire selection process.

**Worked solution:** Freeze the candidate choice and evaluate it once on test examples that influenced neither fitting nor selection. Comparing candidates used the validation outcomes to guide the choice, so the selected validation score can benefit from selection and is not an untouched final assessment. Award one mark for the test protocol and one for recognizing selection on validation outcomes.

*Source: PDF pp.21-24,28,48-50.*

## 30. Consistent rectangles and predictions that data do not determine [12 marks]

**(a) [3 marks]** The positive examples are $(2,3),(4,5)$; the negative examples are $(1,4),(5,4),(3,6)$. Find the smallest closed axis-aligned rectangle containing the positives and verify its training error.

**Worked solution:** The coordinate extrema of the positives give $S=[2,4]\times[3,5]$. Both positives lie on its boundary and are included. The negative at x=1 lies left, the negative at x=5 lies right, and the negative at y=6 lies above. Thus all five examples are correctly labeled, and the empirical error count is zero. Award one mark for the bounds and two for the verification.

**(b) [4 marks]** Construct a second consistent rectangle that disagrees with $S$ at $q=(1.7,4)$. State what this proves about predicting $q$ from consistency alone.

**Worked solution:** Take $R=[1.5,4.5]\times[2.5,5.5]$. It includes both positives, excludes x=1 and x=5, and excludes y=6, so it is consistent. It contains q, whereas S excludes q because 1.7<2. Thus two zero-error hypotheses disagree on q; consistency alone leaves its class undetermined. Award two marks for a valid second rectangle and its consistency, one for the disagreement, and one for the conclusion.

**(c) [3 marks]** Which label is forced by all consistent rectangles at $a=(3,4)$? Which label is forced at the already observed negative point $b=(1,4)$? Explain using the geometry and the definition of consistency.

**Worked solution:** Every rectangle containing the positives must contain their entire bounding box S, so a=(3,4) is forced positive. Every consistent hypothesis must respect the observed negative label at b, so b is forced negative. The reason for a is geometric containment, and the reason for b is its explicit training constraint. Award two marks for a with its reasoning and one for b with its reasoning.

**(d) [2 marks]** An additional training record gives $(3,4)$ a negative label while keeping all previous labels. Determine the new version space and explain why optimizing rectangle boundaries cannot obtain zero training error.

**Worked solution:** The version space is empty. Every rectangle containing both positive examples contains (3,4), so it must violate the new negative label; excluding that point requires violating at least one positive. No boundary search can remove this incompatibility within the stated hypothesis class. Award one mark for emptiness and one for the bounding-box explanation.

*Source: PDF pp.37-40,48.*

