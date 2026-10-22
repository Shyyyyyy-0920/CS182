# Lecture 07: Linear Discrimination

## Practice Quiz

**100 marks: 12 True/False × 1; 12 multiple response × 2; 4 proofs/derivations × 10; 2 applications × 12.**

Answer in English. Every multiple-response question has four options and 1–3 correct answers. Exact set: 2 marks; nonempty proper correct subset: 1; any wrong option or no answer: 0. Use `Quiz.tex` to type your responses in its marked regions.

Primary source: [Linear_Discrimination.pdf](../../lecture/Linear_Discrimination.pdf). Page numbers start at the cover.

## A. True/False

**1.** A multiclass argmax classifier with affine scores can have a nonconvex class region even when there are no ties.

**2.** For any fixed $w$ and $w_0$, the set $\{x:w^{\mathsf T}x+w_0=0\}$ is a separating hyperplane of dimension $d-1$.

**3.** Multiplying both the weights and intercept of a binary linear score by a positive constant preserves the predicted labels but generally changes its sigmoid probabilities.

**4.** The batch algorithm shown in the lecture accumulates errors over all samples before updating the weight vector.

**5.** For finite binary logits and no numerical rounding, sigmoid produces probabilities strictly between zero and one.

**6.** For one-hot softmax cross-entropy, a sample generally contributes a gradient to the weights of classes other than its true class.

**7.** Training $K$ independent one-vs.-rest sigmoid models automatically makes their $K$ outputs sum to one.

**8.** Adding the same input-dependent affine function to every softmax class score leaves every predicted class probability unchanged.

**9.** Two learning procedures that both produce a linear class boundary must estimate their parameters by the same statistical objective.

**10.** When training a one-vs.-one classifier for classes $C_i$ and $C_j$, examples from other classes are excluded from that particular binary training problem.

**11.** A standard linear logistic-regression model requires every input feature to have a Gaussian class-conditional distribution.

**12.** Convexity of unregularized logistic cross-entropy guarantees a finite maximum-likelihood parameter vector on every strictly linearly separable dataset.

## B. Multiple Response

**13.** Let a batch contain four samples. Compare summed cross-entropy and average cross-entropy at exactly the same weights. Which statements are correct?

- **A.** At the same learning rate, the average-loss gradient step is one quarter of the summed-loss step.
- **B.** Choosing the average-loss learning rate four times as large reproduces the summed-loss update.
- **C.** Zero initialization forces the binary logistic gradient to be zero for every labeled dataset.
- **D.** Updating weights after every sample is necessarily identical to accumulating the four gradients at fixed weights.

**14.** Three independently trained affine scores at one test point are $(-2,-1,-3)$. The specified decision rule is argmax over these scores, with no rejection option. Which statements are correct?

- **A.** Adding ten to every score changes the argmax class.
- **B.** The point must be rejected because every score is negative.
- **C.** No label can be assigned until the scores have been individually transformed to probabilities.
- **D.** The predicted class is $C_2$.

**15.** Correct decisions cost zero. Predicting $C_1$ when the truth is $C_2$ costs three; the reverse error costs two. At a point with $y=P(C_1\mid x)=0.55$, which statements are correct?

- **A.** The risk of predicting $C_2$ at the point is $0.9$.
- **B.** The rule must predict $C_1$ at the given point because $0.55>0.5$.
- **C.** The risk-minimizing rule predicts $C_1$ when $y>3/5$.
- **D.** The equivalent logit threshold is $\log(2/3)$.

**16.** Consider adding $\lambda\|\theta\|_2^2/2$, with $\lambda>0$, to a finite-sample linear binary logistic loss, where $\theta$ includes the intercept. Which statements are correct?

- **A.** The added Hessian is $\lambda I$.
- **B.** The penalty weight can be selected using validation data.
- **C.** The penalty necessarily sets some fitted coefficients exactly to zero.
- **D.** The penalized objective has a unique finite minimizer.

**17.** For $\sigma(a)=1/(1+e^{-a})$, which statements are correct?

- **A.** The derivative equals zero at every finite positive logit.
- **B.** The largest derivative value is $1/4$, attained at $a=0$.
- **C.** $\sigma(a+b)=\sigma(a)+\sigma(b)$ for all real $a,b$.
- **D.** $\sigma(\log9)=0.9$.

**18.** A binary logistic model predicts $y=1/4$ for a sample with label $r=1$ and feature vector $x=(1,-2)^{\mathsf T}$. Which statements are correct?

- **A.** The intercept gradient is $-3/4$.
- **B.** The negative-gradient update decreases the intercept when the learning rate is positive.
- **C.** The feature-weight gradient is $(-3/4,-3/2)^{\mathsf T}$.
- **D.** The sample cross-entropy is $\log4$.

**19.** Two Gaussian classes have means $1$ and $-1$, shared variance two, and equal priors. Which statements are correct?

- **A.** This derivation proves that all logistic input distributions must be Gaussian.
- **B.** The posterior probability of $C_1$ is $\sigma(x)$.
- **C.** Changing only the priors, with means and variance fixed, changes only the logit intercept.
- **D.** Two distinct Gaussian variances always yield the same linear logit.

**20.** At a point where softmax probabilities are $(0.2,0.5,0.3)$, which statements are correct?

- **A.** $\partial y_2/\partial a_1=-0.1$.
- **B.** Every column of the Jacobian sums to one.
- **C.** $\partial y_2/\partial a_2=0.5$.
- **D.** The Jacobian is diagonal because each numerator uses one score.

**21.** Consider $g(x)=x_1^2+x_2^2-1$, with $C_1$ predicted for $g(x)>0$. Which statements are correct?

- **A.** The score is affine in the transformed feature $z=x_1^2+x_2^2$.
- **B.** The boundary is a straight line in the original input plane because the coefficients enter linearly.
- **C.** The boundary is a unit circle in the original input plane.
- **D.** The model requires $x$ to have a Gaussian distribution.

**22.** Let $w=(4,-3)^{\mathsf T}$, $w_0=-5$, and $x=(2,0)^{\mathsf T}$. Which statements are correct?

- **A.** The ordinary distance from the origin to the boundary equals minus one.
- **B.** The Euclidean distance from $x$ to the boundary equals three.
- **C.** The score at $x$ equals three.
- **D.** The orthogonal projection is $(38/25,9/25)^{\mathsf T}$.

**23.** Three softmax logits are $(0,\log3,\log2)$. Which statements are correct?

- **A.** The second class has probability $1/2$.
- **B.** Adding seven to every logit preserves all three probabilities.
- **C.** The predicted class must be rejected because its probability does not strictly exceed $1/2$.
- **D.** The posterior odds of $C_2$ against $C_3$ equal $3/2$.

**24.** A four-class softmax model has two original input features and an intercept per class. Which statements are correct?

- **A.** Adding the same three-component augmented weight vector to every class changes the probabilities.
- **B.** Fixing the reference-class score to zero leaves nine free coefficients.
- **C.** The symmetric parameterization has twelve coefficients.
- **D.** For a row-weight matrix $B\in\mathbb R^{4\times3}$, the gradient has the same $4\times3$ shape.

## 25. Derive the geometry rather than treating the score as a distance [10 marks]

**(a) [2 marks]** Let $g(x)=w^{\mathsf T}x+b$, with $w\ne0$. Prove that $w$ is normal to its zero hyperplane by comparing two points on that hyperplane.

**(b) [4 marks]** Write a point as $x=x_p+r w/\|w\|_2$, where $x_p$ is its orthogonal projection. Derive both the signed-distance formula and an explicit formula for $x_p$. Explain the corresponding unsigned distance.

**(c) [4 marks]** Prove what happens to the hyperplane, signed distance, and predicted class when $(w,b)$ is multiplied by $c>0$. Does the corresponding sigmoid probability remain fixed? Include the degenerate case $w=0$.

## 26. Derive the LDA-to-logistic bridge with its assumptions [10 marks]

**(a) [5 marks]** Assume $x\mid C_i\sim\mathcal N(\mu_i,\Sigma)$ for two classes, with shared positive-definite $\Sigma$ and positive priors $\pi_i$. Derive $\log[P(C_1\mid x)/P(C_2\mid x)]=w^{\mathsf T}x+b$, explicitly finding $w,b$.

**(b) [2 marks]** Solve $a=\log[y/(1-y)]$ for $y$, and prove the equivalence between the equal-cost posterior threshold and the zero-score threshold.

**(c) [3 marks]** Identify the canceled term that generally remains with unequal class covariances. Explain why the Gaussian derivation does not impose a Gaussian-input requirement on discriminatively fitted logistic regression.

## 27. Derive Bernoulli cross-entropy, its gradient, and its limits [10 marks]

**(a) [3 marks]** For conditionally independent labels $r^t\in\{0,1\}$ with $y^t=\sigma(\theta^{\mathsf T}\widetilde x^t)$, derive the conditional likelihood and its negative log-likelihood. Here $\widetilde x^t$ contains the intercept feature.

**(b) [5 marks]** Use the chain rule to derive $\nabla_\theta E=\sum_t(y^t-r^t)\widetilde x^t$. Then derive the Hessian and prove convexity without treating sigmoid itself as a linear function.

**(c) [2 marks]** For the two observations $(x,r)=(-2,0),(2,1)$, set intercept zero and slope $c>0$. Prove that the unregularized minimum need not be attained at a finite parameter, although the classification error is already zero.

## 28. Derive softmax normalization and the coupled learning rule [10 marks]

**(a) [3 marks]** Take $C_K$ as reference and assume $\log[P(C_i\mid x)/P(C_K\mid x)]=a_i$ for $i<K$. Derive all class probabilities from normalization, then express them in symmetric softmax form.

**(b) [4 marks]** Derive $\partial y_i/\partial a_j$, then derive $\partial\ell/\partial a_j=y_j-r_j$ for one-hot cross-entropy. Give feature-weight and intercept gradients for affine scores.

**(c) [3 marks]** Prove softmax invariance to a common affine score shift, give the free parameter count after fixing a reference class, and explain why a nontrue class still receives a gradient.

## 29. Audit one binary batch update and the resulting decision [12 marks]

**(a) [4 marks]** Train on $(x,r)=(-2,0),(1,1),(3,1)$, starting from slope $w=0$ and intercept $b=0$. Use summed cross-entropy and one batch gradient step with learning rate $0.1$. Compute the gradients and new parameters.

**(b) [4 marks]** Compute the new probabilities and total cross-entropy. Compare it to the initial loss; exact logarithmic expressions are acceptable.

**(c) [2 marks]** Using the equal-cost threshold, classify all three training points. Does a zero classification error here imply that further loss reduction is impossible?

**(d) [2 marks]** Now suppose predicting $C_1$ when the truth is $C_2$ costs four, while the reverse error costs one, with zero correct-decision loss. Derive the posterior threshold and classify the same points under this cost rule.

## 30. Train a three-class model and check the normalization [12 marks]

**(a) [3 marks]** Consider one training sample $x=(2,-1)^{\mathsf T}$ in class $C_3$. Use augmented input $\widetilde x=(1,2,-1)^{\mathsf T}$ and a row-weight matrix $B\in\mathbb R^{3\times3}$, initially zero. Compute the one-hot target, probabilities, and loss.

**(b) [5 marks]** Compute the full gradient matrix and update $B$ using learning rate $1/2$. Display every entry and state its dimension.

**(c) [2 marks]** Recompute the logits, the probability of $C_3$, and the new loss at this sample. Identify the predicted class.

**(d) [2 marks]** Add the row vector $(10,0,0)$ to each fitted row of $B$. Prove whether probabilities change, and describe a numerically stable way to compute the original softmax.

