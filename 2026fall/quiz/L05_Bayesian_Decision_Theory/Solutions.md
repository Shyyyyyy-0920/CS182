# Lecture 05: Bayesian Decision Theory

## Worked Solutions

**100 marks: 12 True/False × 1; 12 multiple response × 2; 4 proofs/derivations × 10; 2 applications × 12.**

Answer in English. Every multiple-response question has four options and 1–3 correct answers. Exact set: 2 marks; nonempty proper correct subset: 1; any wrong option or no answer: 0. Use `Quiz.tex` to type your responses in its marked regions.

Primary source: [Bayesian_Decision_Theory.pdf](../../lecture/Bayesian_Decision_Theory.pdf). Page numbers start at the cover.

## A. True/False

**1.** A class-conditional density $p(x\mid C_i)$ must lie between 0 and 1 at every $x$.

**False.** A continuous density can exceed 1; its integral, rather than its height, is normalized. Class posterior probabilities $P(C_i\mid x)$ do lie in $[0,1]$.

*PDF pp.11-12.*

**2.** With unequal misclassification costs, a class whose posterior is below one half can still be the minimum-risk classification action.

**True.** For example, if $P(C_1\mid x)=0.3$, the loss of predicting $C_1$ when $C_2$ is true is 1, and the opposite error costs 4, then $R(\alpha_1\mid x)=0.7<1.2=R(\alpha_2\mid x)$.

*PDF p.15; supplementary numerical illustration.*

**3.** Every point satisfying $g_i(x)=g_j(x)$ belongs to a decision boundary between $C_i$ and $C_j$.

**False.** The tied scores must also be largest. If another class has a strictly larger score, the equality is hidden inside that class's decision region.

*PDF p.23.*

**4.** Replacing every discriminant by $a(x)g_i(x)+b(x)$, using the same $a(x)>0$ and $b(x)$ for all classes, preserves the entire set of maximizing classes.

**True.** Every pairwise difference is multiplied by the same positive number $a(x)$. Its sign and any zero difference are preserved pointwise.

*PDF p.21; supplementary pointwise extension.*

**5.** Under 0-1 loss, if no features are observed, always predicting a class with the largest prior probability minimizes the probability of error.

**True.** The error of choosing $C_i$ is $1-P(C_i)$; minimizing it is equivalent to maximizing the prior. Ties allow several optimal constant decisions.

*PDF pp.6-7,16.*

**6.** Applying a different strictly increasing function to each class discriminant always preserves the classifier.

**False.** Within-class monotonicity does not preserve comparisons across classes. Scores $g_1=2,g_2=1$ choose $C_1$, whereas $f_1(t)=t$ and $f_2(t)=t+10$ choose $C_2$. The same increasing function must be used for all classes.

*PDF p.21.*

**7.** Because the evidence $p(x)$ cancels when comparing classes, it can also be omitted when reporting normalized posterior probabilities.

**False.** For a fixed $x$, the same positive denominator does not change the maximizing class. It is still required to make $\sum_iP(C_i\mid x)=1$.

*PDF pp.11-12,21.*

**8.** Under 0-1 loss, choosing the largest class likelihood always gives the Bayes decision, even with unequal class priors.

**False.** The relevant scores are $p(x\mid C_i)P(C_i)$. Maximum likelihood classification agrees automatically with MAP when the priors are equal; unequal priors can reverse the ordering.

*PDF pp.11-12,16.*

**9.** Randomly mixing classification actions at a fixed $x$ can give conditional risk strictly below the smallest risk of those actions.

**False.** The mixed risk is a weighted average of the action risks and cannot be below their minimum. Randomization among minimizers can tie that minimum.

*PDF p.15; supplementary randomization argument.*

**10.** If two classes tie for the largest posterior probability, choosing either one has the same conditional 0-1 risk.

**True.** Their risks are both $1-\max_kP(C_k\mid x)$. A tie-breaking convention determines the output label without changing this minimum risk.

*PDF pp.12,16.*

**11.** With unit error cost and rejection cost $\lambda$, classification is strictly preferred to rejection exactly when the largest posterior exceeds $1-\lambda$.

**True.** The best classification risk is $1-\max_iP(C_i\mid x)$, while rejection has risk $\lambda$. The strict comparison gives the stated threshold; equality is a risk tie.

*PDF pp.17-18.*

**12.** Naive Bayes requires the features to be independent in the unconditional feature distribution.

**False.** The required factorization is $p(x\mid C_i)=\prod_jp(x_j\mid C_i)$, separately within each class. Mixing classes can produce dependent features even if this conditional factorization holds.

*PDF p.13.*

## B. Multiple Response

**13.** For $x\in\mathbb R$, define $g_1(x)=1-x^2$, $g_2(x)=0$, and $g_3(x)=1/2$. Use the largest score and allow ties on boundaries. Select every correct statement.

- **A.** Class $C_2$ has a nonempty decision region. **Incorrect:** Its score is always strictly smaller than $g_3$.
- **B.** The region where $C_3$ is the unique winner has two disconnected components. **Correct:** It is $x<-1/\sqrt2$ or $x>1/\sqrt2$.
- **C.** The actual class changes occur at $x=\pm1/\sqrt2$. **Correct:** These solve $g_1=g_3=1/2$, and those tied scores exceed $g_2=0$.
- **D.** The equation $g_1=g_2$ produces $x=\pm1$, but neither point is a decision boundary. **Correct:** At both points $g_3=1/2$ exceeds the tied value 0.

**Correct set: B, C, D.** *PDF p.23; supplementary algebraic example.*

**14.** Let the true joint distribution be known, and use 0-1 loss. Select every correct statement about using features.

- **A.** The Bayes error using $X$ is no larger than the error of always predicting a class with largest prior. **Correct:** The constant rule is available among all rules using $X$, so optimization cannot have a larger risk.
- **B.** Any rule that depends on $X$ must outperform every constant rule. **Incorrect:** A feature-dependent rule may ignore useful posterior information or deliberately choose a low-posterior class.
- **C.** If each observed input identifies its class with posterior probability 1 almost surely, the Bayes error is zero. **Correct:** The pointwise minimum error $1-\max_iP(C_i\mid X)$ is zero almost surely.
- **D.** If the posterior equals the prior almost surely, observing $X$ cannot improve the minimum error. **Correct:** Then $E[1-\max_iP(C_i\mid X)]=1-\max_iP(C_i)$.

**Correct set: A, C, D.** *PDF pp.7,9-12,15-16; supplementary comparison of rule classes.*

**15.** A three-class posterior is $(0.46,0.34,0.20)$. Correct classifications cost 0 and mistakes cost 1. Select every correct statement about a constant rejection cost.

- **A.** At rejection cost $0.55$, acceptance requires the largest posterior to exceed $0.55$. **Incorrect:** The acceptance threshold is $1-0.55=0.45$, not $0.55$.
- **B.** At rejection cost $0.50$, rejection is strictly preferable to every class action. **Correct:** The best class risk $0.54$ already exceeds $0.50$.
- **C.** At rejection cost $0.55$, predicting $C_1$ is strictly preferable to rejection. **Correct:** The best classification risk is $1-0.46=0.54<0.55$.
- **D.** Increasing the rejection cost cannot enlarge the set where rejection is strictly optimal. **Correct:** Rejection is strictly optimal when $1-\max_iP(C_i\mid x)>\lambda$; increasing $\lambda$ makes this condition harder to satisfy.

**Correct set: B, C, D.** *PDF pp.17-18.*

**16.** Assume all discriminants are finite. Which transformations preserve the full maximizing-class set at every $x$, for arbitrary original scores?

- **A.** Multiply every score by the same negative constant. **Incorrect:** A negative multiplier reverses strict order, making maximizers into minimizers.
- **B.** Add a different constant $b_i$ to each class score. **Incorrect:** Class-dependent offsets can reverse cross-class comparisons.
- **C.** Apply one common strictly increasing function $f$ to every score. **Correct:** Strict monotonicity preserves both strict order and ties across all classes.
- **D.** Replace every $g_i(x)$ by $a(x)g_i(x)+b(x)$, with common $a(x)>0$ and $b(x)$. **Correct:** The pairwise differences become $a(x)[g_i(x)-g_j(x)]$, preserving their signs.

**Correct set: C, D.** *PDF p.21; supplementary pointwise extension.*

**17.** Consider any finite loss matrix $\lambda_{ik}$. Which modifications preserve all minimum-risk actions for every posterior?

- **A.** Add one state-dependent number $b_k$ to every entry in column $k$. **Correct:** Every action risk gains the same $\sum_kb_kP(C_k\mid x)$.
- **B.** Replace risks by their negatives and choose the largest resulting score. **Correct:** Maximizing $-R(\alpha_i\mid x)$ is equivalent to minimizing $R(\alpha_i\mid x)$.
- **C.** Multiply the entire loss matrix by one positive constant. **Correct:** All action risks are multiplied by that constant, preserving order and ties.
- **D.** Add a different arbitrary constant to every row. **Incorrect:** Each action then gains a different offset, which can change the minimizing action.

**Correct set: A, B, C.** *PDF pp.15,20; supplementary loss transformations.*

**18.** For two classes with positive priors and positive likelihoods, let $P(C_1)=1/4$, $P(C_2)=3/4$, and $L(x)=p(x\mid C_1)/p(x\mid C_2)$. Under 0-1 loss, select every correct statement.

- **A.** For the given priors, a log discriminant is $\log L(x)-\log3$. **Correct:** The log posterior odds equal $\log L(x)+\log(1/3)$.
- **B.** Predicting $C_1$ is strictly optimal when $L(x)>3$. **Correct:** The joint-score comparison is $L(x)>P(C_2)/P(C_1)=3$.
- **C.** The evidence is needed to determine which posterior is larger. **Incorrect:** It is the same positive denominator for both posteriors and cancels.
- **D.** Replacing the priors by $0.1$ and $0.9$ changes the likelihood-ratio threshold to 9. **Correct:** The threshold is the prior odds $0.9/0.1$.

**Correct set: A, B, D.** *PDF pp.11-12,21-22.*

**19.** Which statements about the naive Bayes assumption are correct?

- **A.** It is sufficient that the features be mutually independent conditional on each class. **Correct:** This is exactly the factorization $p(x\mid C_i)=\prod_jp(x_j\mid C_i)$.
- **B.** Unconditional independence alone guarantees the required class-conditional factorization. **Incorrect:** Conditioning can introduce dependence; independence in the mixture does not establish independence within each class.
- **C.** The class prior is unnecessary once the likelihood is factorized. **Incorrect:** Bayes scores remain $P(C_i)\prod_jp(x_j\mid C_i)$, so unequal priors still matter.
- **D.** The factorization makes $P(C_i\mid x)$ equal to $\prod_jP(C_i\mid x_j)$ without any normalization or prior correction. **Incorrect:** Naive Bayes factors feature likelihoods, not posteriors of the class. Repeated posterior factors also repeatedly include the prior.

**Correct set: A.** *PDF pp.11-13.*

**20.** For three classes, let the priors be $(0.2,0.3,0.5)$ and the class likelihoods at one observed $x$ be $(0.9,0.4,0.2)$. Under 0-1 loss, select every correct statement.

- **A.** The Bayes action predicts $C_1$. **Correct:** The posterior vector is $(0.45,0.30,0.25)$, so $C_1$ has the largest posterior.
- **B.** The minimum conditional probability of error is $0.45$. **Incorrect:** The maximum posterior is $0.45$; the error is its complement, $0.55$.
- **C.** The posterior probability of $C_1$ is $0.60$. **Incorrect:** It is $0.18/0.40=0.45$; the likelihood alone is not the posterior.
- **D.** The evidence is $p(x)=0.40$. **Correct:** Summing the joint scores gives $0.18+0.12+0.10=0.40$.

**Correct set: A, D.** *PDF pp.11-12,16.*

**21.** A posterior is $(0.4,0.4,0.2)$, unit error loss is used, and rejection costs $0.6$. Select every correct statement.

- **A.** Any random mixture of rejection and predictions of $C_1$ or $C_2$ also has risk $0.6$. **Correct:** A convex combination of their equal risks remains $0.6$.
- **B.** Predicting $C_3$ is also optimal because all posterior values are below $0.6$. **Incorrect:** Its risk is $1-0.2=0.8$. The rejection threshold is $1-0.6=0.4$, not $0.6$.
- **C.** The minimum conditional risk is $0.6$. **Correct:** Predicting either of the first two classes costs $0.6$, as does rejection.
- **D.** Rejection is the unique risk-minimizing action. **Incorrect:** The two largest-posterior class actions tie with rejection. A reject-on-equality convention selects one of several minimizers.

**Correct set: A, C.** *PDF pp.15-18; supplementary tie/randomization interpretation.*

**22.** Write $q=P(C_1\mid x)=0.55$. Correct decisions cost 0; predicting $C_1$ when $C_2$ is true costs 8, and predicting $C_2$ when $C_1$ is true costs 2. Select every correct statement.

- **A.** Predicting $C_1$ has risk $3.6$. **Correct:** This error occurs when $C_2$ is true, giving $8(1-0.55)=3.6$.
- **B.** Predicting $C_2$ minimizes conditional risk. **Correct:** Its risk is $2(0.55)=1.1<3.6$.
- **C.** Without rejection, predicting $C_1$ is strictly optimal when $q>0.8$. **Correct:** The inequality $8(1-q)<2q$ is equivalent to $q>0.8$.
- **D.** The larger posterior must determine the minimum-risk action. **Incorrect:** Posterior maximization minimizes unit error loss; these asymmetric costs produce a different threshold.

**Correct set: A, B, C.** *PDF pp.15-16; supplementary asymmetric-loss specialization.*

**23.** At a fixed input, suppose the risks of three available actions are $0.2,0.5,0.2$. Select every correct statement about randomized actions.

- **A.** Assigning positive probability to the second action can still yield risk below $0.2$. **Incorrect:** The mixed risk is $0.2+0.3w_2$, which is at least $0.2$.
- **B.** Every minimum-risk randomization must put zero probability on the second action. **Correct:** Equality at the minimum requires $w_2=0$, because its risk is strictly larger.
- **C.** A half-and-half mixture of the first and third actions has risk $0.2$. **Correct:** Its expected risk is $(0.2+0.2)/2=0.2$.
- **D.** The existence of two minimizing actions forces a unique optimal randomization. **Incorrect:** Any mixture supported on the first and third actions is optimal.

**Correct set: B, C.** *PDF p.15; supplementary randomization derivation.*

**24.** At an observed point, two continuous class densities have values $4$ and $1$, and their priors are $0.1$ and $0.9$. Under 0-1 loss, select every correct statement.

- **A.** The evidence density is $1.3$. **Correct:** It is $4(0.1)+1(0.9)=1.3$; a density value may exceed 1.
- **B.** The posterior of $C_1$ is $4/13$. **Correct:** It is $0.4/1.3=4/13$.
- **C.** The Bayes action predicts $C_2$. **Correct:** Its joint score $0.9$ exceeds $0.4$, so its posterior is $9/13$.
- **D.** The larger likelihood proves that $C_1$ is the Bayes choice. **Incorrect:** The prior-weighted likelihoods determine the posterior ordering.

**Correct set: A, B, C.** *PDF pp.11-12,16.*

## 25. Why pointwise decisions minimize total risk [10 marks]

**(a) [4 marks]** Let $A$ be a finite action set, let $\lambda_{ak}$ be finite nonnegative losses, and let $X$ have density or mass function $p(x)$. Define a deterministic rule $\delta(x)$. Starting from $E[\lambda_{\delta(X),C}]$, derive the total-risk formula and prove that choosing a minimum-conditional-risk action at each $x$ minimizes total risk. State the almost-sure qualification.

**Worked solution:** Conditioning first on $X$ gives

$$

\mathcal R(\delta)=E_X\!\left[\sum_k\lambda_{\delta(X),k}P(C_k\mid X)\right]
=\int R(\delta(x)\mid x)p(x)\,dx.

$$

Use a sum instead of an integral for discrete $X$. For a measurable minimizing selector $\delta^*$, $R(\delta^*(x)\mid x)\le R(\delta(x)\mid x)$ wherever posteriors are defined. Multiplication by $p(x)\ge0$ and integration prove $\mathcal R(\delta^*)\le\mathcal R(\delta)$. Choices on sets of $X$-probability zero do not affect total risk; ties can be resolved arbitrarily. Marking: conditional expectation (2), pointwise inequality and integration (1), ties/null sets (1).

**(b) [3 marks]** Specialize to $K$ classification actions and 0-1 loss. Derive the MAP rule and the Bayes error expression in terms of the largest posterior.

**Worked solution:** For action $\alpha_i$,

$$

R(\alpha_i\mid x)=\sum_{k\ne i}P(C_k\mid x)=1-P(C_i\mid x).

$$

Thus any largest-posterior class is a conditional-risk minimizer. Substitution into the total-risk formula yields

$$

\mathcal R^*=E_X[1-\max_iP(C_i\mid X)].

$$

Marking: risk simplification (1), MAP minimizer (1), expected minimum error (1).

**(c) [3 marks]** Prove that this Bayes error is at most $1-\max_iP(C_i)$, the best constant-rule error. Explain why this does not guarantee that every fitted classifier improves on the constant rule.

**Worked solution:** Choose $j\in\arg\max_iP(C_i)$. Pointwise $\max_iP(C_i\mid X)\ge P(C_j\mid X)$. Taking expectations and using the law of total probability gives $E[\max_iP(C_i\mid X)]\ge E[P(C_j\mid X)]=P(C_j)$. Subtracting from 1 proves the bound. The result concerns the true Bayes rule; an estimated or poorly chosen classifier need not minimize true risk. Marking: pointwise bound (1), expectation and final inequality (1), scope of guarantee (1).

*Source: PDF pp.15-16; supplementary integration and information comparison.*

## 26. Asymmetric errors and rejection thresholds [10 marks]

**(a) [4 marks]** For two classes, write $q=P(C_1\mid x)$. Correct decisions cost 0, predicting $C_1$ when $C_2$ is true costs $a>0$, and predicting $C_2$ when $C_1$ is true costs $b>0$. Derive the optimal posterior threshold without rejection and the equivalent likelihood-ratio threshold when priors and likelihoods are positive.

**Worked solution:** The risks are $R_1=a(1-q)$ and $R_2=bq$. Therefore $R_1<R_2$ exactly when $q>a/(a+b)$; reverse the inequality for $C_2$, with a tie at equality. Equivalently $q/(1-q)>a/b$. Bayes' rule gives

$$

\frac{q}{1-q}=\frac{p(x\mid C_1)P(C_1)}{p(x\mid C_2)P(C_2)},

$$

so predict $C_1$ when

$$

\frac{p(x\mid C_1)}{p(x\mid C_2)}>
\frac{aP(C_2)}{bP(C_1)}.

$$

Marking: risks (1), posterior threshold and tie (1), posterior odds (1), likelihood-ratio threshold (1).

**(b) [3 marks]** Add a reject action with constant loss $r>0$ for either true class. Derive the interval where rejection is strictly optimal and determine when that interval has positive width.

**Worked solution:** Rejection is strictly optimal precisely when both $r<a(1-q)$ and $r<bq$, hence

$$

\frac rb<q<1-\frac ra.

$$

This interval has positive width exactly when $r/b<1-r/a$, or $r<ab/(a+b)$. At either endpoint rejection ties a class action; at $r=ab/(a+b)$ it only ties at the original class threshold. For larger $r$, rejection is never strictly optimal. Marking: two risk comparisons (1), interval (1), width condition and ties (1).

**(c) [3 marks]** Return to $K$ classes, unit cost for any error, and reject cost $\lambda$. Derive the acceptance rule. Then show that if $\lambda>1-1/K$, rejection cannot be strictly optimal at any input.

**Worked solution:** The best class risk is $1-M(x)$, where $M(x)=\max_iP(C_i\mid x)$, and reject risk is $\lambda$. Classification is strictly preferable exactly when $M(x)>1-\lambda$; rejection is strictly preferable when $M(x)<1-\lambda$. Since the $K$ posteriors sum to 1, $M(x)\ge1/K$. If $\lambda>1-1/K$, then $1-\lambda<1/K\le M(x)$, so a class action strictly beats rejection everywhere. At equality of the costs, the uniform posterior can produce a tie. Marking: risks (1), threshold/tie distinction (1), $1/K$ bound and consequence (1).

*Source: PDF pp.15-18; supplementary asymmetric-cost extension.*

## 27. Equivalent discriminants and the role of strict monotonicity [10 marks]

**(a) [4 marks]** Prove that applying one common strictly increasing function to all finite discriminants preserves their full argmax set. Explain why merely nondecreasing is insufficient for preserving the argmax set, using a concrete counterexample.

**Worked solution:** For any two scores $u,v$, strict monotonicity gives $u>v\iff f(u)>f(v)$, and injectivity gives $u=v\iff f(u)=f(v)$. Thus a class is at least as large as every competitor before transformation exactly when it is afterward. The full argmax set is unchanged. If $f$ is merely nondecreasing, it can merge different scores: take $g_1=2,g_2=1$ and $f(t)=0$ for all $t$. The original argmax is only $C_1$, whereas both classes maximize transformed scores. Marking: order/tie argument (2), argmax conclusion (1), counterexample (1).

**(b) [3 marks]** For $p(x)>0$ and positive class joint scores, derive the equivalence of posterior, prior-weighted likelihood, and log prior-weighted likelihood discriminants. Identify the qualification needed for zero joint scores.

**Worked solution:** Bayes' rule gives $P(C_i\mid x)=p(x\mid C_i)P(C_i)/p(x)$. Multiplying all scores by common $p(x)>0$ preserves their ordering and ties, so the posterior and joint scores have identical argmax sets. Applying the common strictly increasing logarithm yields $\log p(x\mid C_i)+\log P(C_i)$, with the same maximizers. If a joint score is zero, the finite logarithm is undefined; one may compare the original scores or use the extended value $\log0=-\infty$. At least one score is positive when $p(x)>0$. Marking: common denominator (1), log decomposition (1), zero-score qualification (1).

**(c) [3 marks]** For two classes with positive priors and likelihoods, derive a single scalar log discriminant. Show how its sign determines the 0-1 decision, and explain why a negative-risk discriminant rather than posterior probability is needed for arbitrary losses.

**Worked solution:** Subtract the two log joint scores:

$$

g(x)=\log\frac{p(x\mid C_1)}{p(x\mid C_2)}
+\log\frac{P(C_1)}{P(C_2)}.

$$

If $g>0$, the posterior of $C_1$ is larger; if $g<0$, that of $C_2$ is larger; $g=0$ is a tie. For arbitrary losses, the optimal action minimizes $\sum_k\lambda_{ik}P(C_k\mid x)$, which need not be the maximum-posterior class. Scores $h_i(x)=-R(\alpha_i\mid x)$ give the correct maximizing action. Marking: log-ratio derivation (1), sign/tie rule (1), general-loss argument (1).

*Source: PDF pp.20-22; supplementary tie-preserving conditions.*

## 28. What a decision boundary actually represents [10 marks]

**(a) [4 marks]** Suppose $g_i(x)=w_i^\mathsf Tx+b_i$ on $\mathbb R^d$. Show that the weak decision region $\mathcal R_i=\{x:g_i(x)\ge g_j(x)\text{ for all }j\}$ is convex. Describe the supporting equality between two competing classes.

**Worked solution:** Each comparison is

$$

(w_i-w_j)^\mathsf Tx+(b_i-b_j)\ge0,

$$

a closed half-space (possibly the whole space or empty). Thus $\mathcal R_i$ is an intersection of half-spaces. If $u,v$ satisfy every inequality, then for $0\le t\le1$ each left side at $tu+(1-t)v$ is the corresponding convex combination of nonnegative values, so the segment also lies in $\mathcal R_i$. Equality $g_i=g_j$ is a hyperplane when $w_i\ne w_j$, but only its portions where these scores are maximal can be decision boundaries. Marking: inequalities (1), intersection/segment proof (2), equality and maximality condition (1).

**(b) [3 marks]** Give an explicit two-class example on $\mathbb R$ with a disconnected decision region, and derive the regions and boundaries. Use $g_1(x)=x^2-4$ and $g_2(x)=0$.

**Worked solution:** Class $C_1$ wins strictly when $x^2>4$, that is, $x<-2$ or $x>2$. These are two disconnected components. Class $C_2$ wins strictly when $-2<x<2$. At $x=\pm2$, the two scores tie for the maximum and form the boundaries. The weak regions include the endpoints, and any tie convention assigns them without affecting the disconnected strict regions. Marking: exterior region (1), interior and boundaries (1), disconnectedness/ties (1).

**(c) [3 marks]** For $g_1(x)=2-x^2$, $g_2(x)=0$, and $g_3(x)=1$, identify all pairwise equality points and determine which are actual decision boundaries. Use the result to disprove the claim that every discriminant equality is a boundary.

**Worked solution:** The equality $g_1=g_2$ gives $x=\pm\sqrt2$, while $g_1=g_3$ gives $x=\pm1$; $g_2=g_3$ has no solution. At $\pm\sqrt2$, the tied first two scores are 0 but $g_3=1$, so these points lie strictly in $C_3$'s region. At $\pm1$, $g_1=g_3=1>0=g_2$, and the winner changes between $C_1$ and $C_3$. The only boundaries are $\pm1$. Marking: pairwise equalities (1), largest-score check (1), actual boundaries and counterexample conclusion (1).

*Source: PDF p.23; supplementary affine and quadratic examples.*

## 29. A sensor with asymmetric mistakes and a review action [12 marks]

**(a) [4 marks]** A sensor reports $A,B,$ or $C$. The class priors are $P(C_1)=0.35$, $P(C_2)=0.65$, and the class-conditional probabilities for $(A,B,C)$ are $(0.50,0.30,0.20)$ in $C_1$ and $(0.10,0.40,0.50)$ in $C_2$. Compute each report probability and each posterior $q_s=P(C_1\mid s)$.

**Worked solution:** The two joint probabilities at $A$ are $0.175,0.065$; at $B$, $0.105,0.260$; at $C$, $0.070,0.325$. Therefore

$$

P(A)=0.240,\quad P(B)=0.365,\quad P(C)=0.395,

$$

which sum to 1. The posteriors are

$$

q_A=\frac{35}{48}\approx0.729167,\quad
q_B=\frac{21}{73}\approx0.287671,\quad
q_C=\frac{14}{79}\approx0.177215.

$$

Marking: joint scores (1), report probabilities (1), posterior values (2).

**(b) [4 marks]** Correct classifications cost 0. Predicting $C_1$ when $C_2$ is true costs 3; predicting $C_2$ when $C_1$ is true costs 9. A human review action costs 1.7 regardless of class. Compute all three conditional risks for each report and choose the optimal action.

**Worked solution:** For posterior $q$, the risks are $3(1-q)$, $9q$, and $1.7$. At $A$, these are $13/16=0.8125$, $105/16=6.5625$, and $1.7$, so predict $C_1$. At $B$, they are $156/73\approx2.136986$, $189/73\approx2.589041$, and $1.7$, so review. At $C$, they are $195/79\approx2.468354$, $126/79\approx1.594937$, and $1.7$, so predict $C_2$. Equivalently, review is preferred for $17/90<q<13/30$. Marking: risk formulas (1), three risk triples with correct actions (3).

**(c) [4 marks]** Compute the expected loss of your review-enabled rule. Compare it with the best rule forced to classify every report and with the MAP rule that ignores the asymmetric costs.

**Worked solution:** The review-enabled expected loss is

$$

0.240(0.8125)+0.365(1.7)+0.395\left(\frac{126}{79}\right)
=0.195+0.6205+0.630=1.4455.

$$

Without review, the posterior threshold is $3/(3+9)=0.25$, giving $C_1$ at $A,B$ and $C_2$ at $C$. Its loss is $3(0.065)+3(0.260)+9(0.070)=1.605$. MAP uses threshold $0.5$, giving $C_1$ only at $A$; its loss is $3(0.065)+9(0.105)+9(0.070)=1.770$. Review reduces the forced minimum loss by $0.1595$. Marking: review expectation (2), forced-cost rule/loss (1), MAP rule/loss and comparison (1).

*Source: PDF pp.11-12,15-18; supplementary asymmetric review-cost application.*

## 30. Conditional independence, posterior decisions, and rejection [12 marks]

**(a) [4 marks]** Two binary features are independent conditional on class. Let $P(C_1)=0.4$, $P(C_2)=0.6$; within $C_1$, the probabilities $P(X_1=1\mid C_1)$, $P(X_2=1\mid C_1)$ are $0.8,0.3$; within $C_2$, they are $0.25,0.7$. For every binary pair $(00,01,10,11)$, compute the two joint class-feature scores, give the MAP class, and find the overall 0-1 Bayes error.

**Worked solution:** The joint-score pairs $(P(x,C_1),P(x,C_2))$ are

$$

00:(0.056,0.135),\quad01:(0.024,0.315),\quad
10:(0.224,0.045),\quad11:(0.096,0.105).

$$

For example, the $C_1$ score at $10$ is $0.4(0.8)(0.7)=0.224$. The winning classes are $C_2,C_2,C_1,C_2$, respectively. Summing each losing joint score gives the error

$$

0.056+0.024+0.045+0.096=0.221.

$$

Marking: four joint-score pairs (2), decisions (1), error sum (1).

**(b) [4 marks]** Add a rejection action costing $0.30$, with unit misclassification costs. Determine which feature pairs are accepted and compute the total expected risk including rejected inputs.

**Worked solution:** The feature-pair probabilities are $0.191,0.339,0.269,0.201$. Their maximum posteriors are

$$

\frac{0.135}{0.191}\approx0.706806,\quad
\frac{0.315}{0.339}\approx0.929204,\quad
\frac{0.224}{0.269}\approx0.832714,\quad
\frac{0.105}{0.201}\approx0.522388.

$$

The acceptance threshold is $1-0.30=0.70$. Accept $00,01,10$ with the previous MAP labels; reject $11$. Total risk is

$$

0.056+0.024+0.045+0.30(0.201)=0.1853.

$$

This includes review cost on all rejected inputs rather than treating them as free. Marking: posterior maxima/threshold (2), accepted/rejected pairs (1), expected risk (1).

**(c) [4 marks]** Are $X_1$ and $X_2$ independent without conditioning on class? Establish your answer by computing the necessary marginal and joint probabilities.

**Worked solution:** The marginal probabilities are

$$

P(X_1=1)=0.4(0.8)+0.6(0.25)=0.47,\quad
P(X_2=1)=0.4(0.3)+0.6(0.7)=0.54.

$$

Their joint probability is $P(11)=0.096+0.105=0.201$, whereas $0.47(0.54)=0.2538$. Since these differ, the features are dependent marginally. This is compatible with the stated conditional independence: both features respond to the shared, unobserved class variable. Marking: marginals (2), joint-versus-product comparison (1), conditional/marginal distinction (1).

*Source: PDF pp.11-13,16-18; supplementary marginal-dependence calculation.*

