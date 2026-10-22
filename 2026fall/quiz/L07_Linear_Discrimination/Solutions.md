# Lecture 07: Linear Discrimination

## Worked Solutions

**100 marks: 12 True/False × 1; 12 multiple response × 2; 4 proofs/derivations × 10; 2 applications × 12.**

Answer in English. Every multiple-response question has four options and 1–3 correct answers. Exact set: 2 marks; nonempty proper correct subset: 1; any wrong option or no answer: 0. Use `Quiz.tex` to type your responses in its marked regions.

Primary source: [Linear_Discrimination.pdf](../../lecture/Linear_Discrimination.pdf). Page numbers start at the cover.

## A. True/False

**1.** A multiclass argmax classifier with affine scores can have a nonconvex class region even when there are no ties.

**False.** Each class region is an intersection of score-comparison half-spaces and is convex. This statement concerns affine-score argmax, not arbitrary voting combinations.

*PDF p.18.*

**2.** For any fixed $w$ and $w_0$, the set $\{x:w^{\mathsf T}x+w_0=0\}$ is a separating hyperplane of dimension $d-1$.

**False.** This requires $w\ne0$. If $w=0$, the zero set is either the whole space or empty, depending on the intercept.

*PDF pp.11-15; supplementary degenerate case.*

**3.** Multiplying both the weights and intercept of a binary linear score by a positive constant preserves the predicted labels but generally changes its sigmoid probabilities.

**True.** The score sign is unchanged; sigmoid is strictly monotone but not invariant to multiplication of its argument. Classification geometry and probability calibration have different scale behavior.

*PDF pp.11,26,36; supplementary scale argument.*

**4.** The batch algorithm shown in the lecture accumulates errors over all samples before updating the weight vector.

**True.** The parameter update is outside the full sample loop. Updating after each sample would be a different, sequential optimization procedure.

*PDF pp.35,44.*

**5.** For finite binary logits and no numerical rounding, sigmoid produces probabilities strictly between zero and one.

**True.** For finite real $a$, both the exponential and the denominator are positive, and $0<1/(1+e^{-a})<1$. Values zero or one are limits rather than finite-logit outputs.

*PDF pp.26,36-37.*

**6.** For one-hot softmax cross-entropy, a sample generally contributes a gradient to the weights of classes other than its true class.

**True.** For a nontrue class $j$, the error is $y_j-0$, generally nonzero because its score competes in the shared normalization.

*PDF p.43.*

**7.** Training $K$ independent one-vs.-rest sigmoid models automatically makes their $K$ outputs sum to one.

**False.** Independent sigmoids do not share a denominator. Softmax imposes a joint normalization across all classes; independent binary probabilities need not sum to one.

*PDF pp.17-18,38-41; supplementary comparison.*

**8.** Adding the same input-dependent affine function to every softmax class score leaves every predicted class probability unchanged.

**True.** The common exponential factor cancels from numerator and denominator at each input. This also creates parameter non-identifiability in the symmetric parameterization.

*PDF pp.40-41; supplementary identifiability argument.*

**9.** Two learning procedures that both produce a linear class boundary must estimate their parameters by the same statistical objective.

**False.** Gaussian LDA estimates class-conditional distributions and priors, whereas logistic regression optimizes a conditional Bernoulli likelihood. The same form of boundary does not identify the training objective.

*PDF pp.4-6,22-31.*

**10.** When training a one-vs.-one classifier for classes $C_i$ and $C_j$, examples from other classes are excluded from that particular binary training problem.

**True.** The pairwise score constrains the relative classes only; samples from a third class have no required sign for this subproblem.

*PDF pp.19-20.*

**11.** A standard linear logistic-regression model requires every input feature to have a Gaussian class-conditional distribution.

**False.** The assumed affine quantity is the conditional log-odds. Gaussian shared-covariance distributions imply such a model, but they are not necessary to fit it; discrete features are allowed.

*PDF pp.29-31,47.*

**12.** Convexity of unregularized logistic cross-entropy guarantees a finite maximum-likelihood parameter vector on every strictly linearly separable dataset.

**False.** Along a separating direction the parameter norm can diverge while cross-entropy decreases toward zero without attaining zero at any finite vector. Convexity does not ensure attainment.

*PDF pp.32,36-37; supplementary existence analysis.*

## B. Multiple Response

**13.** Let a batch contain four samples. Compare summed cross-entropy and average cross-entropy at exactly the same weights. Which statements are correct?

- **A.** At the same learning rate, the average-loss gradient step is one quarter of the summed-loss step. **Correct:** Averaging divides the full gradient by four.
- **B.** Choosing the average-loss learning rate four times as large reproduces the summed-loss update. **Correct:** Then the scale factor in the learning rate cancels the factor $1/4$ in the gradient.
- **C.** Zero initialization forces the binary logistic gradient to be zero for every labeled dataset. **Incorrect:** Initial predictions are $1/2$, but the weighted label residuals generally do not cancel.
- **D.** Updating weights after every sample is necessarily identical to accumulating the four gradients at fixed weights. **Incorrect:** Sequential updates evaluate later gradients at changed weights.

**Correct set: A, B.** *PDF pp.32-35; supplementary sum/mean comparison.*

**14.** Three independently trained affine scores at one test point are $(-2,-1,-3)$. The specified decision rule is argmax over these scores, with no rejection option. Which statements are correct?

- **A.** Adding ten to every score changes the argmax class. **Incorrect:** A common shift preserves all pairwise score differences.
- **B.** The point must be rejected because every score is negative. **Incorrect:** The specified rule chooses the largest score and includes no reject action.
- **C.** No label can be assigned until the scores have been individually transformed to probabilities. **Incorrect:** Argmax on the raw scores is already a fully specified classification rule.
- **D.** The predicted class is $C_2$. **Correct:** Minus one is the largest of the three scores. Scores need not be positive to win an argmax.

**Correct set: D.** *PDF pp.17-18.*

**15.** Correct decisions cost zero. Predicting $C_1$ when the truth is $C_2$ costs three; the reverse error costs two. At a point with $y=P(C_1\mid x)=0.55$, which statements are correct?

- **A.** The risk of predicting $C_2$ at the point is $0.9$. **Incorrect:** The risk is $2(0.55)=1.10$.
- **B.** The rule must predict $C_1$ at the given point because $0.55>0.5$. **Incorrect:** The cost-sensitive threshold is $0.6$; at this point $C_2$ has lower risk.
- **C.** The risk-minimizing rule predicts $C_1$ when $y>3/5$. **Correct:** Compare $3(1-y)$ against $2y$.
- **D.** The equivalent logit threshold is $\log(2/3)$. **Incorrect:** The threshold is $\log((3/5)/(2/5))=\log(3/2)$.

**Correct set: C.** *PDF pp.24,30; supplementary application of lecture 05 loss rule.*

**16.** Consider adding $\lambda\|\theta\|_2^2/2$, with $\lambda>0$, to a finite-sample linear binary logistic loss, where $\theta$ includes the intercept. Which statements are correct?

- **A.** The added Hessian is $\lambda I$. **Correct:** The gradient of the full quadratic penalty is $\lambda\theta$.
- **B.** The penalty weight can be selected using validation data. **Correct:** This is a model-selection choice; the final test set should remain independent.
- **C.** The penalty necessarily sets some fitted coefficients exactly to zero. **Incorrect:** L2 shrinkage does not in general produce exact sparsity.
- **D.** The penalized objective has a unique finite minimizer. **Correct:** The positive quadratic penalty is coercive and makes the convex loss strongly convex.

**Correct set: A, B, D.** *PDF p.37; supplementary connection to regularization.*

**17.** For $\sigma(a)=1/(1+e^{-a})$, which statements are correct?

- **A.** The derivative equals zero at every finite positive logit. **Incorrect:** The derivative is strictly positive for every finite logit.
- **B.** The largest derivative value is $1/4$, attained at $a=0$. **Correct:** $\sigma'(a)=\sigma(a)(1-\sigma(a))$ is maximized at probability $1/2$.
- **C.** $\sigma(a+b)=\sigma(a)+\sigma(b)$ for all real $a,b$. **Incorrect:** For example, take both arguments zero: the two sides are $1/2$ and one.
- **D.** $\sigma(\log9)=0.9$. **Correct:** The odds are nine, so the probability is $9/(1+9)$.

**Correct set: B, D.** *PDF pp.26,33; supplementary maximum calculation.*

**18.** A binary logistic model predicts $y=1/4$ for a sample with label $r=1$ and feature vector $x=(1,-2)^{\mathsf T}$. Which statements are correct?

- **A.** The intercept gradient is $-3/4$. **Correct:** It equals $y-r=1/4-1$.
- **B.** The negative-gradient update decreases the intercept when the learning rate is positive. **Incorrect:** The gradient is negative, so a descent step increases the intercept.
- **C.** The feature-weight gradient is $(-3/4,-3/2)^{\mathsf T}$. **Incorrect:** Multiply the error $-3/4$ by each feature; the second entry is $+3/2$.
- **D.** The sample cross-entropy is $\log4$. **Correct:** For a positive label, the loss is $-\log y$.

**Correct set: A, D.** *PDF pp.31-34.*

**19.** Two Gaussian classes have means $1$ and $-1$, shared variance two, and equal priors. Which statements are correct?

- **A.** This derivation proves that all logistic input distributions must be Gaussian. **Incorrect:** It shows sufficiency of a shared-covariance Gaussian model, not necessity.
- **B.** The posterior probability of $C_1$ is $\sigma(x)$. **Correct:** The logit slope is $(1-(-1))/2=1$, and the intercept is zero.
- **C.** Changing only the priors, with means and variance fixed, changes only the logit intercept. **Correct:** The prior contribution is the additive log prior ratio.
- **D.** Two distinct Gaussian variances always yield the same linear logit. **Incorrect:** An unequal-variance log density ratio generally retains a quadratic term.

**Correct set: B, C.** *PDF pp.22-30,48.*

**20.** At a point where softmax probabilities are $(0.2,0.5,0.3)$, which statements are correct?

- **A.** $\partial y_2/\partial a_1=-0.1$. **Correct:** For different indices the derivative is $-y_2y_1$.
- **B.** Every column of the Jacobian sums to one. **Incorrect:** Every column sums to zero, since the total probability is the constant one.
- **C.** $\partial y_2/\partial a_2=0.5$. **Incorrect:** The derivative is $0.5(1-0.5)=0.25$.
- **D.** The Jacobian is diagonal because each numerator uses one score. **Incorrect:** The common denominator gives off-diagonal derivatives $-y_i y_j$.

**Correct set: A.** *PDF p.43.*

**21.** Consider $g(x)=x_1^2+x_2^2-1$, with $C_1$ predicted for $g(x)>0$. Which statements are correct?

- **A.** The score is affine in the transformed feature $z=x_1^2+x_2^2$. **Correct:** It becomes $g=z-1$, an affine function of the new feature.
- **B.** The boundary is a straight line in the original input plane because the coefficients enter linearly. **Incorrect:** Linearity in coefficients does not force a linear boundary in the original input.
- **C.** The boundary is a unit circle in the original input plane. **Correct:** The zero set is $x_1^2+x_2^2=1$.
- **D.** The model requires $x$ to have a Gaussian distribution. **Incorrect:** A fixed basis-function discriminant does not itself impose Gaussian input densities.

**Correct set: A, C.** *PDF pp.8-9,48; supplementary example.*

**22.** Let $w=(4,-3)^{\mathsf T}$, $w_0=-5$, and $x=(2,0)^{\mathsf T}$. Which statements are correct?

- **A.** The ordinary distance from the origin to the boundary equals minus one. **Incorrect:** Ordinary distance is nonnegative; its value is $|-5|/5=1$.
- **B.** The Euclidean distance from $x$ to the boundary equals three. **Incorrect:** The score must be divided by $\|w\|=5$, giving distance $3/5$.
- **C.** The score at $x$ equals three. **Correct:** $w^{\mathsf T}x+w_0=8-5=3$.
- **D.** The orthogonal projection is $(38/25,9/25)^{\mathsf T}$. **Correct:** Subtract $(3/25)(4,-3)^{\mathsf T}$ from $(2,0)^{\mathsf T}$.

**Correct set: C, D.** *PDF pp.13-15; supplementary numerical example.*

**23.** Three softmax logits are $(0,\log3,\log2)$. Which statements are correct?

- **A.** The second class has probability $1/2$. **Correct:** The exponentials are $(1,3,2)$, whose sum is six.
- **B.** Adding seven to every logit preserves all three probabilities. **Correct:** The same exponential factor cancels from the softmax.
- **C.** The predicted class must be rejected because its probability does not strictly exceed $1/2$. **Incorrect:** Multiclass argmax needs no universal $1/2$ threshold; rejection requires a separately specified rule.
- **D.** The posterior odds of $C_2$ against $C_3$ equal $3/2$. **Correct:** The common denominator cancels in the probability ratio.

**Correct set: A, B, D.** *PDF pp.38-41.*

**24.** A four-class softmax model has two original input features and an intercept per class. Which statements are correct?

- **A.** Adding the same three-component augmented weight vector to every class changes the probabilities. **Incorrect:** It adds a common affine score, which cancels.
- **B.** Fixing the reference-class score to zero leaves nine free coefficients. **Correct:** Three remaining classes each need two weights and one intercept.
- **C.** The symmetric parameterization has twelve coefficients. **Correct:** There are four rows, each with three coefficients.
- **D.** For a row-weight matrix $B\in\mathbb R^{4\times3}$, the gradient has the same $4\times3$ shape. **Correct:** With sample rows, it is $(Y-R)^{\mathsf T}\widetilde X$.

**Correct set: B, C, D.** *PDF pp.38-44; supplementary matrix and identifiability notation.*

## 25. Derive the geometry rather than treating the score as a distance [10 marks]

**(a) [2 marks]** Let $g(x)=w^{\mathsf T}x+b$, with $w\ne0$. Prove that $w$ is normal to its zero hyperplane by comparing two points on that hyperplane.

**Worked solution:** For boundary points $u,v$, subtract $w^{\mathsf T}u+b=0$ and $w^{\mathsf T}v+b=0$. This gives $w^{\mathsf T}(u-v)=0$. Every displacement within the affine hyperplane is of this form, so $w$ is perpendicular to it.

**(b) [4 marks]** Write a point as $x=x_p+r w/\|w\|_2$, where $x_p$ is its orthogonal projection. Derive both the signed-distance formula and an explicit formula for $x_p$. Explain the corresponding unsigned distance.

**Worked solution:** Substitution gives $g(x)=g(x_p)+r w^{\mathsf T}w/\|w\|_2=r\|w\|_2$. Hence $r=g(x)/\|w\|_2$, and rearranging the decomposition gives 
$$
x_p=x-\frac{w^{\mathsf T}x+b}{\|w\|_2^2}w.
$$
 The ordinary distance is $|r|$, not $r$. Substituting the projection in the boundary equation yields zero and verifies the formula.

**(c) [4 marks]** Prove what happens to the hyperplane, signed distance, and predicted class when $(w,b)$ is multiplied by $c>0$. Does the corresponding sigmoid probability remain fixed? Include the degenerate case $w=0$.

**Worked solution:** The new score is $cg(x)$, so its zero set and sign are unchanged. Its norm is $c\|w\|$, so $cg(x)/(c\|w\|)=g(x)/\|w\|$. The probability becomes $\sigma(cg(x))$, generally different when $c\ne1$ and $g(x)\ne0$. If $w=0$, the score is constant and the zero set is all of space when $b=0$, or empty otherwise; the distance formula is undefined.

*Source: PDF pp.11-15; supplementary projection and scale proof.*

## 26. Derive the LDA-to-logistic bridge with its assumptions [10 marks]

**(a) [5 marks]** Assume $x\mid C_i\sim\mathcal N(\mu_i,\Sigma)$ for two classes, with shared positive-definite $\Sigma$ and positive priors $\pi_i$. Derive $\log[P(C_1\mid x)/P(C_2\mid x)]=w^{\mathsf T}x+b$, explicitly finding $w,b$.

**Worked solution:** Bayes rule cancels the common evidence. The Gaussian normalizers also cancel because covariance is shared. Expanding both quadratic exponents gives 
$$
\log\frac{P(C_1\mid x)}{P(C_2\mid x)}=(\mu_1-\mu_2)^{\mathsf T}\Sigma^{-1}x-\frac12(\mu_1^{\mathsf T}\Sigma^{-1}\mu_1-\mu_2^{\mathsf T}\Sigma^{-1}\mu_2)+\log\frac{\pi_1}{\pi_2}.
$$
 The common $x^{\mathsf T}\Sigma^{-1}x$ cancels and symmetry combines the cross terms. Thus $w=\Sigma^{-1}(\mu_1-\mu_2)$ and $b=-\tfrac12(\mu_1^{\mathsf T}\Sigma^{-1}\mu_1-\mu_2^{\mathsf T}\Sigma^{-1}\mu_2)+\log(\pi_1/\pi_2)$.

**(b) [2 marks]** Solve $a=\log[y/(1-y)]$ for $y$, and prove the equivalence between the equal-cost posterior threshold and the zero-score threshold.

**Worked solution:** Exponentiating gives $e^a(1-y)=y$, so $y=e^a/(1+e^a)=\sigma(a)$. Since sigmoid is increasing and $\sigma(0)=1/2$, $y>1/2$ is equivalent to $a>0$.

**(c) [3 marks]** Identify the canceled term that generally remains with unequal class covariances. Explain why the Gaussian derivation does not impose a Gaussian-input requirement on discriminatively fitted logistic regression.

**Worked solution:** With unequal covariances, the difference contains $-\tfrac12 x^{\mathsf T}(\Sigma_1^{-1}-\Sigma_2^{-1})x$, generally quadratic. Shared Gaussian covariances are a sufficient generative explanation of affine posterior log-odds. Logistic regression instead assumes that conditional log-odds are affine and fits the conditional label likelihood directly, without requiring Gaussian class densities.

*Source: PDF pp.22-30.*

## 27. Derive Bernoulli cross-entropy, its gradient, and its limits [10 marks]

**(a) [3 marks]** For conditionally independent labels $r^t\in\{0,1\}$ with $y^t=\sigma(\theta^{\mathsf T}\widetilde x^t)$, derive the conditional likelihood and its negative log-likelihood. Here $\widetilde x^t$ contains the intercept feature.

**Worked solution:** Each label has probability $(y^t)^{r^t}(1-y^t)^{1-r^t}$. Conditional independence gives 
$$
L(\theta)=\prod_t(y^t)^{r^t}(1-y^t)^{1-r^t},\quad E(\theta)=-\sum_t[r^t\log y^t+(1-r^t)\log(1-y^t)].
$$
 This is binary cross-entropy; the inputs are held fixed during conditional fitting.

**(b) [5 marks]** Use the chain rule to derive $\nabla_\theta E=\sum_t(y^t-r^t)\widetilde x^t$. Then derive the Hessian and prove convexity without treating sigmoid itself as a linear function.

**Worked solution:** For one sample, $dy/da=y(1-y)$ and $\partial\ell/\partial y=-r/y+(1-r)/(1-y)$. Their product is $-r(1-y)+(1-r)y=y-r$. Because $\partial a/\partial\theta=\widetilde x$, summation gives the gradient. Differentiating again yields 
$$
H=\sum_t y^t(1-y^t)\widetilde x^t(\widetilde x^t)^{\mathsf T}.
$$
 For any $v$, $v^{\mathsf T}Hv=\sum_t y^t(1-y^t)(v^{\mathsf T}\widetilde x^t)^2\ge0$, establishing convexity. The descent increment is minus this gradient.

**(c) [2 marks]** For the two observations $(x,r)=(-2,0),(2,1)$, set intercept zero and slope $c>0$. Prove that the unregularized minimum need not be attained at a finite parameter, although the classification error is already zero.

**Worked solution:** Both samples have correct-label probability $\sigma(2c)$, so $E(c)=2\log(1+e^{-2c})$. This is positive for finite $c$ and tends to zero as $c\to\infty$. For every $c>0$ both labels are correct. Thus the infimum is zero, with no finite minimizing slope along this perfectly separating dataset.

*Source: PDF pp.31-37; supplementary Hessian and nonattainment proof.*

## 28. Derive softmax normalization and the coupled learning rule [10 marks]

**(a) [3 marks]** Take $C_K$ as reference and assume $\log[P(C_i\mid x)/P(C_K\mid x)]=a_i$ for $i<K$. Derive all class probabilities from normalization, then express them in symmetric softmax form.

**Worked solution:** Exponentiating yields $P_i=e^{a_i}P_K$. Summing probabilities gives $1=P_K[1+\sum_{i<K}e^{a_i}]$. Therefore $P_K=[1+\sum_{i<K}e^{a_i}]^{-1}$ and $P_i=e^{a_i}/[1+\sum_{j<K}e^{a_j}]$. This is softmax with reference score zero. Adding a common score to every class yields the symmetric form $y_i=e^{a_i}/\sum_j e^{a_j}$.

**(b) [4 marks]** Derive $\partial y_i/\partial a_j$, then derive $\partial\ell/\partial a_j=y_j-r_j$ for one-hot cross-entropy. Give feature-weight and intercept gradients for affine scores.

**Worked solution:** Let $Z=\sum_k e^{a_k}$. The quotient rule gives $\partial y_i/\partial a_j=(\delta_{ij}e^{a_i}Z-e^{a_i}e^{a_j})/Z^2=y_i(\delta_{ij}-y_j)$. Then 
$$
\frac{\partial\ell}{\partial a_j}=-\sum_i\frac{r_i}{y_i}y_i(\delta_{ij}-y_j)=-r_j+y_j\sum_i r_i=y_j-r_j.
$$
 This uses $\sum_i r_i=1$. Thus $\partial\ell/\partial w_{j0}=y_j-r_j$ and $\nabla_{w_j}\ell=(y_j-r_j)x$, with sums over samples for the full loss.

**(c) [3 marks]** Prove softmax invariance to a common affine score shift, give the free parameter count after fixing a reference class, and explain why a nontrue class still receives a gradient.

**Worked solution:** Adding $c(x)$ multiplies every numerator and the denominator by $e^{c(x)}$, which cancels. For $K$ classes with $d$ features and intercepts, fixing one class score to zero leaves $(K-1)(d+1)$ free coefficients instead of the redundant $K(d+1)$. A nontrue class has $r_j=0$ but generally $y_j>0$, so its error $y_j-r_j$ remains nonzero through the common probability normalization.

*Source: PDF pp.38-44; supplementary parameter-identifiability proof.*

## 29. Audit one binary batch update and the resulting decision [12 marks]

**(a) [4 marks]** Train on $(x,r)=(-2,0),(1,1),(3,1)$, starting from slope $w=0$ and intercept $b=0$. Use summed cross-entropy and one batch gradient step with learning rate $0.1$. Compute the gradients and new parameters.

**Worked solution:** All probabilities are $1/2$. The intercept gradient is $1/2-1/2-1/2=-1/2$. The slope gradient is $(1/2)(-2)+(-1/2)(1)+(-1/2)(3)=-3$. Hence $b_{\rm new}=0.05$ and $w_{\rm new}=0.3$.

**(b) [4 marks]** Compute the new probabilities and total cross-entropy. Compare it to the initial loss; exact logarithmic expressions are acceptable.

**Worked solution:** New logits are $(-0.55,0.35,0.95)$, with probabilities approximately $(0.3659,0.5866,0.7211)$. The loss is 
$$
\log(1+e^{-0.55})+\log(1+e^{-0.35})+\log(1+e^{-0.95})\approx1.3158,
$$
 below the initial $3\log2\approx2.0794$. The first term uses label zero and a negative score; the other two use positive labels.

**(c) [2 marks]** Using the equal-cost threshold, classify all three training points. Does a zero classification error here imply that further loss reduction is impossible?

**Worked solution:** The first probability is below $1/2$, and the other two are above it, so all three labels are correct. Positive correct-side logits can still increase in magnitude, raising correct-class probabilities and reducing cross-entropy; zero label error is not zero cross-entropy.

**(d) [2 marks]** Now suppose predicting $C_1$ when the truth is $C_2$ costs four, while the reverse error costs one, with zero correct-decision loss. Derive the posterior threshold and classify the same points under this cost rule.

**Worked solution:** Compare $4(1-y)$ with $y$: choose $C_1$ only if $y>4/5$. None of the three fitted probabilities exceeds $0.8$, so all are assigned to $C_2$. This changes the decision rule while retaining the same fitted probabilities.

*Source: PDF pp.31-37; new numerical application and cost-sensitive extension.*

## 30. Train a three-class model and check the normalization [12 marks]

**(a) [3 marks]** Consider one training sample $x=(2,-1)^{\mathsf T}$ in class $C_3$. Use augmented input $\widetilde x=(1,2,-1)^{\mathsf T}$ and a row-weight matrix $B\in\mathbb R^{3\times3}$, initially zero. Compute the one-hot target, probabilities, and loss.

**Worked solution:** The target is $r=(0,0,1)^{\mathsf T}$, all logits are zero, probabilities are $(1/3,1/3,1/3)$, and cross-entropy is $\log3$.

**(b) [5 marks]** Compute the full gradient matrix and update $B$ using learning rate $1/2$. Display every entry and state its dimension.

**Worked solution:** Each row is $(y_i-r_i)\widetilde x^{\mathsf T}$, so 
$$
\nabla_B\ell=\begin{bmatrix}1/3&2/3&-1/3\\1/3&2/3&-1/3\\-2/3&-4/3&2/3\end{bmatrix},\qquad B_{\rm new}=\begin{bmatrix}-1/6&-1/3&1/6\\-1/6&-1/3&1/6\\1/3&2/3&-1/3\end{bmatrix}.
$$
 Both are $3\times3$. The signs are from subtracting one half of the gradient.

**(c) [2 marks]** Recompute the logits, the probability of $C_3$, and the new loss at this sample. Identify the predicted class.

**Worked solution:** Multiplying each row by $\widetilde x$ gives logits $(-1,-1,2)$. Thus $y_3=e^3/(2+e^3)\approx0.9094$, each other probability is $1/(2+e^3)$, and loss is $\log(1+2e^{-3})\approx0.0949$. Class $C_3$ wins.

**(d) [2 marks]** Add the row vector $(10,0,0)$ to each fitted row of $B$. Prove whether probabilities change, and describe a numerically stable way to compute the original softmax.

**Worked solution:** The shared row adds ten to every logit, so all probabilities remain identical after cancellation. For stable evaluation, subtract the largest original logit, two, obtaining $(-3,-3,0)$, and normalize the exponentials $(e^{-3},e^{-3},1)$.

*Source: PDF pp.41-44; new numerical application.*

