# Lecture 05: Bayesian Decision Theory

## Practice Quiz

**100 marks: 12 True/False × 1; 12 multiple response × 2; 4 proofs/derivations × 10; 2 applications × 12.**

Answer in English. Every multiple-response question has four options and 1–3 correct answers. Exact set: 2 marks; nonempty proper correct subset: 1; any wrong option or no answer: 0. Use `Quiz.tex` to type your responses in its marked regions.

Primary source: [Bayesian_Decision_Theory.pdf](../../lecture/Bayesian_Decision_Theory.pdf). Page numbers start at the cover.

## A. True/False

**1.** A class-conditional density $p(x\mid C_i)$ must lie between 0 and 1 at every $x$.

**2.** With unequal misclassification costs, a class whose posterior is below one half can still be the minimum-risk classification action.

**3.** Every point satisfying $g_i(x)=g_j(x)$ belongs to a decision boundary between $C_i$ and $C_j$.

**4.** Replacing every discriminant by $a(x)g_i(x)+b(x)$, using the same $a(x)>0$ and $b(x)$ for all classes, preserves the entire set of maximizing classes.

**5.** Under 0-1 loss, if no features are observed, always predicting a class with the largest prior probability minimizes the probability of error.

**6.** Applying a different strictly increasing function to each class discriminant always preserves the classifier.

**7.** Because the evidence $p(x)$ cancels when comparing classes, it can also be omitted when reporting normalized posterior probabilities.

**8.** Under 0-1 loss, choosing the largest class likelihood always gives the Bayes decision, even with unequal class priors.

**9.** Randomly mixing classification actions at a fixed $x$ can give conditional risk strictly below the smallest risk of those actions.

**10.** If two classes tie for the largest posterior probability, choosing either one has the same conditional 0-1 risk.

**11.** With unit error cost and rejection cost $\lambda$, classification is strictly preferred to rejection exactly when the largest posterior exceeds $1-\lambda$.

**12.** Naive Bayes requires the features to be independent in the unconditional feature distribution.

## B. Multiple Response

**13.** For $x\in\mathbb R$, define $g_1(x)=1-x^2$, $g_2(x)=0$, and $g_3(x)=1/2$. Use the largest score and allow ties on boundaries. Select every correct statement.

- **A.** Class $C_2$ has a nonempty decision region.
- **B.** The region where $C_3$ is the unique winner has two disconnected components.
- **C.** The actual class changes occur at $x=\pm1/\sqrt2$.
- **D.** The equation $g_1=g_2$ produces $x=\pm1$, but neither point is a decision boundary.

**14.** Let the true joint distribution be known, and use 0-1 loss. Select every correct statement about using features.

- **A.** The Bayes error using $X$ is no larger than the error of always predicting a class with largest prior.
- **B.** Any rule that depends on $X$ must outperform every constant rule.
- **C.** If each observed input identifies its class with posterior probability 1 almost surely, the Bayes error is zero.
- **D.** If the posterior equals the prior almost surely, observing $X$ cannot improve the minimum error.

**15.** A three-class posterior is $(0.46,0.34,0.20)$. Correct classifications cost 0 and mistakes cost 1. Select every correct statement about a constant rejection cost.

- **A.** At rejection cost $0.55$, acceptance requires the largest posterior to exceed $0.55$.
- **B.** At rejection cost $0.50$, rejection is strictly preferable to every class action.
- **C.** At rejection cost $0.55$, predicting $C_1$ is strictly preferable to rejection.
- **D.** Increasing the rejection cost cannot enlarge the set where rejection is strictly optimal.

**16.** Assume all discriminants are finite. Which transformations preserve the full maximizing-class set at every $x$, for arbitrary original scores?

- **A.** Multiply every score by the same negative constant.
- **B.** Add a different constant $b_i$ to each class score.
- **C.** Apply one common strictly increasing function $f$ to every score.
- **D.** Replace every $g_i(x)$ by $a(x)g_i(x)+b(x)$, with common $a(x)>0$ and $b(x)$.

**17.** Consider any finite loss matrix $\lambda_{ik}$. Which modifications preserve all minimum-risk actions for every posterior?

- **A.** Add one state-dependent number $b_k$ to every entry in column $k$.
- **B.** Replace risks by their negatives and choose the largest resulting score.
- **C.** Multiply the entire loss matrix by one positive constant.
- **D.** Add a different arbitrary constant to every row.

**18.** For two classes with positive priors and positive likelihoods, let $P(C_1)=1/4$, $P(C_2)=3/4$, and $L(x)=p(x\mid C_1)/p(x\mid C_2)$. Under 0-1 loss, select every correct statement.

- **A.** For the given priors, a log discriminant is $\log L(x)-\log3$.
- **B.** Predicting $C_1$ is strictly optimal when $L(x)>3$.
- **C.** The evidence is needed to determine which posterior is larger.
- **D.** Replacing the priors by $0.1$ and $0.9$ changes the likelihood-ratio threshold to 9.

**19.** Which statements about the naive Bayes assumption are correct?

- **A.** It is sufficient that the features be mutually independent conditional on each class.
- **B.** Unconditional independence alone guarantees the required class-conditional factorization.
- **C.** The class prior is unnecessary once the likelihood is factorized.
- **D.** The factorization makes $P(C_i\mid x)$ equal to $\prod_jP(C_i\mid x_j)$ without any normalization or prior correction.

**20.** For three classes, let the priors be $(0.2,0.3,0.5)$ and the class likelihoods at one observed $x$ be $(0.9,0.4,0.2)$. Under 0-1 loss, select every correct statement.

- **A.** The Bayes action predicts $C_1$.
- **B.** The minimum conditional probability of error is $0.45$.
- **C.** The posterior probability of $C_1$ is $0.60$.
- **D.** The evidence is $p(x)=0.40$.

**21.** A posterior is $(0.4,0.4,0.2)$, unit error loss is used, and rejection costs $0.6$. Select every correct statement.

- **A.** Any random mixture of rejection and predictions of $C_1$ or $C_2$ also has risk $0.6$.
- **B.** Predicting $C_3$ is also optimal because all posterior values are below $0.6$.
- **C.** The minimum conditional risk is $0.6$.
- **D.** Rejection is the unique risk-minimizing action.

**22.** Write $q=P(C_1\mid x)=0.55$. Correct decisions cost 0; predicting $C_1$ when $C_2$ is true costs 8, and predicting $C_2$ when $C_1$ is true costs 2. Select every correct statement.

- **A.** Predicting $C_1$ has risk $3.6$.
- **B.** Predicting $C_2$ minimizes conditional risk.
- **C.** Without rejection, predicting $C_1$ is strictly optimal when $q>0.8$.
- **D.** The larger posterior must determine the minimum-risk action.

**23.** At a fixed input, suppose the risks of three available actions are $0.2,0.5,0.2$. Select every correct statement about randomized actions.

- **A.** Assigning positive probability to the second action can still yield risk below $0.2$.
- **B.** Every minimum-risk randomization must put zero probability on the second action.
- **C.** A half-and-half mixture of the first and third actions has risk $0.2$.
- **D.** The existence of two minimizing actions forces a unique optimal randomization.

**24.** At an observed point, two continuous class densities have values $4$ and $1$, and their priors are $0.1$ and $0.9$. Under 0-1 loss, select every correct statement.

- **A.** The evidence density is $1.3$.
- **B.** The posterior of $C_1$ is $4/13$.
- **C.** The Bayes action predicts $C_2$.
- **D.** The larger likelihood proves that $C_1$ is the Bayes choice.

## 25. Why pointwise decisions minimize total risk [10 marks]

**(a) [4 marks]** Let $A$ be a finite action set, let $\lambda_{ak}$ be finite nonnegative losses, and let $X$ have density or mass function $p(x)$. Define a deterministic rule $\delta(x)$. Starting from $E[\lambda_{\delta(X),C}]$, derive the total-risk formula and prove that choosing a minimum-conditional-risk action at each $x$ minimizes total risk. State the almost-sure qualification.

**(b) [3 marks]** Specialize to $K$ classification actions and 0-1 loss. Derive the MAP rule and the Bayes error expression in terms of the largest posterior.

**(c) [3 marks]** Prove that this Bayes error is at most $1-\max_iP(C_i)$, the best constant-rule error. Explain why this does not guarantee that every fitted classifier improves on the constant rule.

## 26. Asymmetric errors and rejection thresholds [10 marks]

**(a) [4 marks]** For two classes, write $q=P(C_1\mid x)$. Correct decisions cost 0, predicting $C_1$ when $C_2$ is true costs $a>0$, and predicting $C_2$ when $C_1$ is true costs $b>0$. Derive the optimal posterior threshold without rejection and the equivalent likelihood-ratio threshold when priors and likelihoods are positive.

**(b) [3 marks]** Add a reject action with constant loss $r>0$ for either true class. Derive the interval where rejection is strictly optimal and determine when that interval has positive width.

**(c) [3 marks]** Return to $K$ classes, unit cost for any error, and reject cost $\lambda$. Derive the acceptance rule. Then show that if $\lambda>1-1/K$, rejection cannot be strictly optimal at any input.

## 27. Equivalent discriminants and the role of strict monotonicity [10 marks]

**(a) [4 marks]** Prove that applying one common strictly increasing function to all finite discriminants preserves their full argmax set. Explain why merely nondecreasing is insufficient for preserving the argmax set, using a concrete counterexample.

**(b) [3 marks]** For $p(x)>0$ and positive class joint scores, derive the equivalence of posterior, prior-weighted likelihood, and log prior-weighted likelihood discriminants. Identify the qualification needed for zero joint scores.

**(c) [3 marks]** For two classes with positive priors and likelihoods, derive a single scalar log discriminant. Show how its sign determines the 0-1 decision, and explain why a negative-risk discriminant rather than posterior probability is needed for arbitrary losses.

## 28. What a decision boundary actually represents [10 marks]

**(a) [4 marks]** Suppose $g_i(x)=w_i^\mathsf Tx+b_i$ on $\mathbb R^d$. Show that the weak decision region $\mathcal R_i=\{x:g_i(x)\ge g_j(x)\text{ for all }j\}$ is convex. Describe the supporting equality between two competing classes.

**(b) [3 marks]** Give an explicit two-class example on $\mathbb R$ with a disconnected decision region, and derive the regions and boundaries. Use $g_1(x)=x^2-4$ and $g_2(x)=0$.

**(c) [3 marks]** For $g_1(x)=2-x^2$, $g_2(x)=0$, and $g_3(x)=1$, identify all pairwise equality points and determine which are actual decision boundaries. Use the result to disprove the claim that every discriminant equality is a boundary.

## 29. A sensor with asymmetric mistakes and a review action [12 marks]

**(a) [4 marks]** A sensor reports $A,B,$ or $C$. The class priors are $P(C_1)=0.35$, $P(C_2)=0.65$, and the class-conditional probabilities for $(A,B,C)$ are $(0.50,0.30,0.20)$ in $C_1$ and $(0.10,0.40,0.50)$ in $C_2$. Compute each report probability and each posterior $q_s=P(C_1\mid s)$.

**(b) [4 marks]** Correct classifications cost 0. Predicting $C_1$ when $C_2$ is true costs 3; predicting $C_2$ when $C_1$ is true costs 9. A human review action costs 1.7 regardless of class. Compute all three conditional risks for each report and choose the optimal action.

**(c) [4 marks]** Compute the expected loss of your review-enabled rule. Compare it with the best rule forced to classify every report and with the MAP rule that ignores the asymmetric costs.

## 30. Conditional independence, posterior decisions, and rejection [12 marks]

**(a) [4 marks]** Two binary features are independent conditional on class. Let $P(C_1)=0.4$, $P(C_2)=0.6$; within $C_1$, the probabilities $P(X_1=1\mid C_1)$, $P(X_2=1\mid C_1)$ are $0.8,0.3$; within $C_2$, they are $0.25,0.7$. For every binary pair $(00,01,10,11)$, compute the two joint class-feature scores, give the MAP class, and find the overall 0-1 Bayes error.

**(b) [4 marks]** Add a rejection action costing $0.30$, with unit misclassification costs. Determine which feature pairs are accepted and compute the total expected risk including rejected inputs.

**(c) [4 marks]** Are $X_1$ and $X_2$ independent without conditioning on class? Establish your answer by computing the necessary marginal and joint probabilities.

