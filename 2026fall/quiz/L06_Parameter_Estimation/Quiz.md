# Lecture 06: Parameter Estimation

## Practice Quiz

**100 marks: 12 True/False × 1; 12 multiple response × 2; 4 proofs/derivations × 10; 2 applications × 12.**

Answer in English. Every multiple-response question has four options and 1–3 correct answers. Exact set: 2 marks; nonempty proper correct subset: 1; any wrong option or no answer: 0. Use `Quiz.tex` to type your responses in its marked regions.

Primary source: [Parameter_Estimation.pdf](../../lecture/Parameter_Estimation.pdf). Page numbers start at the cover.

## A. True/False

**1.** A full $d\times d$ empirical covariance estimated within a class from exactly $d$ observations is necessarily invertible if all feature sample variances are positive.

**2.** The posterior mean minimizes posterior expected loss for every possible loss function.

**3.** Zero covariance between two variables guarantees their independence without any assumption about their joint distribution.

**4.** With positive class priors and a shared positive-definite covariance, Gaussian log-discriminant differences are affine, even when the class priors are unequal.

**5.** If the posterior for an unknown Gaussian mean is normal, substituting its mean into the likelihood reproduces the full Bayesian posterior predictive variance.

**6.** Filling missing values of one feature with its observed sample mean leaves that feature's maximum-likelihood sample variance unchanged.

**7.** An unbiased estimator necessarily has smaller mean squared error than every biased estimator of the same parameter.

**8.** For an unrestricted categorical model on a closed probability simplex, a category observed zero times has maximum-likelihood probability zero.

**9.** For observed data $D$, the likelihood $L(\theta;D)$ is generally a probability density over $\theta$ and must integrate to 1 with respect to $\theta$.

**10.** If every Gaussian class has a diagonal covariance matrix, the classifier must have linear decision boundaries even when the diagonal variances differ across classes.

**11.** When the Gaussian mean is estimated from the same $N$ observations, the maximum-likelihood variance with denominator $N$ is unbiased for the population variance.

**12.** A regression model using fixed features $1,x,x^2,\sin x$ can still be linear in its unknown parameters.

## B. Multiple Response

**13.** A categorical variable has counts $(3,0,7)$ in a sample of size 10. The parameter space is the closed simplex. Select every correct statement.

- **A.** At the MLE, the zero-count term in the log-likelihood is interpreted as zero.
- **B.** The MLE is $(0.3,0,0.7)$.
- **C.** The simplex constraint can be discarded because the category likelihoods are independent functions of the parameters.
- **D.** A Lagrange-multiplier calculation that assumes every $p_i>0$ needs a separate boundary argument for the unseen category.

**14.** Select every correct statement about the regression likelihood and design matrix.

- **A.** Independent Gaussian errors with known unequal variances lead to weighting each squared residual by the inverse of its variance.
- **B.** In a joint likelihood, an input-density term $p(x\mid\theta)$ may always be dropped when fitting $\theta$.
- **C.** Independent Gaussian errors with one fixed, known common positive variance make maximum likelihood in the mean parameters equivalent to ordinary least squares.
- **D.** Fixed nonlinear basis functions of the inputs can be used while retaining a model linear in its coefficients.

**15.** A nonconstant Gaussian sample has $N=5$, sample mean $m=2$, and $\sum_t(x^t-m)^2=20$. Both the mean and variance are unknown. Select every correct statement.

- **A.** The usual unbiased variance estimate is 5.
- **B.** The denominator $N-1$ is required to maximize the Gaussian likelihood.
- **C.** The maximum-likelihood standard deviation is $\sqrt5$.
- **D.** The variance MLE is 4.

**16.** Assume a bivariate Gaussian with positive-definite covariance. Select every correct statement.

- **A.** For $\Sigma=\operatorname{diag}(9,1)$, the squared Mahalanobis distance from $\mu$ to $\mu+(3,1)^\mathsf T$ is 2.
- **B.** A zero off-diagonal covariance makes these two jointly Gaussian coordinates independent.
- **C.** For the same covariance and displacement, the squared Euclidean distance is also 2.
- **D.** A positive correlation tilts the long axis of the Gaussian contour ellipse toward positive slope.

**17.** A Gaussian mean has prior $\theta\sim N(1,4)$. Three conditionally independent observations have distribution $N(\theta,9)$ and sample mean 4. Select every correct statement.

- **A.** The posterior variance is $12/7$.
- **B.** The posterior mean is $19/7$.
- **C.** The posterior MAP estimate equals the sample mean 4.
- **D.** The full posterior predictive variance of a new observation is 9.

**18.** For two independent Bernoulli features conditional on class, use priors $0.6,0.4$, class $C_1$ feature probabilities $(0.5,0.8)$, and class $C_2$ probabilities $(0.9,0.3)$. Observe $x=(0,1)$. Select every correct statement.

- **A.** For probabilities strictly between 0 and 1, the log discriminant is affine in the binary coordinates.
- **B.** The zero-valued first feature contributes no likelihood factor.
- **C.** The joint class-feature scores are $0.24$ and $0.012$.
- **D.** The posterior probability of $C_1$ is $0.24$.

**19.** Select every correct statement about model selection.

- **A.** The model evidence is generally just the largest likelihood over that model's parameters.
- **B.** A validation fold should be included in fitting the very predictor whose error it is intended to assess.
- **C.** In a regularized objective, the penalty weight controls the strength of the preference for the penalized notion of simplicity.
- **D.** Bayesian model posterior probabilities are proportional to model evidence times model prior probabilities.

**20.** Five i.i.d. Bernoulli observations are all equal to 1. Select every correct statement about maximum likelihood.

- **A.** The absence of an interior stationary point proves that no MLE exists on the closed interval.
- **B.** On the closed parameter interval $0\le p\le1$, the MLE is $p=1$.
- **C.** The log-likelihood has a stationary point in $0<p<1$.
- **D.** On the open parameter interval $0<p<1$, the maximum occurs at $p=1-1/N=4/5$.

**21.** A Gaussian classifier has $K=3$ classes and $d=4$ features. Count independent covariance parameters only, unless stated otherwise. Select every correct statement.

- **A.** The three class priors add three independent parameters.
- **B.** One shared spherical covariance $s^2I$ requires 4 covariance parameters.
- **C.** Separate full covariance matrices require 30 parameters.
- **D.** One shared full covariance matrix requires 16 independent covariance parameters.

**22.** At a fixed test input, assume a new test response is independent of the training set and has conditional mean $f(x)$ and variance $\sigma^2(x)$. Select every correct statement.

- **A.** Increasing model complexity is a theorem that strictly increases estimator variance for every learning algorithm and distribution.
- **B.** The expected test error is noise variance plus squared prediction bias plus the variance over training sets of the predictor.
- **C.** If every trained predictor equals $f(x)$, the expected squared test error still equals $\sigma^2(x)$.
- **D.** The smallest error on a finite validation set identifies the population-optimal model with certainty.

**23.** For $N=4$ i.i.d. normal observations with true variance 1, let $Q=\sum_t(X_t-\bar X)^2$. You may use $E[Q]=3$ and $\operatorname{Var}(Q)=6$. Compare $V_{\mathrm{ML}}=Q/4$ and $V_{\mathrm U}=Q/3$. Select every correct statement.

- **A.** This example shows that the unbiased estimate must have the smaller MSE.
- **B.** Under i.i.d. sampling with finite variance, the sample mean is consistent even though an arbitrary single observation need not be close to the mean.
- **C.** The MSE of $V_{\mathrm{ML}}$ is $7/16$.
- **D.** The MSE of $V_{\mathrm U}$ is $2/3$.

**24.** There are $d=5$ features, $K=3$ classes, and four observations in each class. Covariances are computed by centering within class. Select every correct statement.

- **A.** Increasing a class to six observations is by itself sufficient to guarantee a nonsingular full covariance.
- **B.** The shared pooled full covariance must also be singular.
- **C.** Every separate full class covariance estimate is singular.
- **D.** A diagonal covariance approximation can be invertible even when every separate full covariance is singular.

## 25. Discrete likelihoods, constraints, and naive Bayes [10 marks]

**(a) [3 marks]** For $N\ge1$ i.i.d. Bernoulli observations, let $s=\sum_t x^t$. Derive the MLE on the closed interval $[0,1]$, treating $0<s<N$, $s=0$, and $s=N$ separately. Establish that your candidates are global maxima.

**(b) [4 marks]** For a categorical distribution with counts $n_1,\ldots,n_K$, $\sum_kn_k=N>0$, derive the constrained MLE. Include a justification for categories having zero counts rather than assuming an interior solution.

**(c) [3 marks]** For binary features conditionally independent given class, derive the class-conditional likelihood, the count-based class-specific MLEs, and an affine log discriminant in the binary input coordinates. State the condition for finite log coefficients.

## 26. Gaussian variance and two kinds of bias-variance decomposition [10 marks]

**(a) [3 marks]** Let $X_1,\ldots,X_N$ be i.i.d. $N(\mu,v)$, with unknown $\mu$, $v>0$, and $N\ge2$. Use $\sum_t(X_t-\mu)^2=\sum_t(X_t-\bar X)^2+N(\bar X-\mu)^2$ to profile out $\mu$, then derive the variance MLE when $T=\sum_t(X_t-\bar X)^2>0$. What happens if $T=0$?

**(b) [2 marks]** Assuming only i.i.d. observations with mean $\mu$ and finite variance $v$, prove $E[T]=(N-1)v$. Deduce the bias of $T/N$ and an unbiased correction.

**(c) [2 marks]** For a scalar estimator $d(D)$ of a fixed parameter $\theta$, derive $\operatorname{MSE}(d)=\operatorname{Var}(d)+[E(d)-\theta]^2$, and explain why unbiasedness alone does not rank estimators by MSE.

**(d) [3 marks]** At a fixed input $x$, let an independent future response $Y$ have conditional mean $f(x)$ and variance $\sigma^2(x)$. A predictor $g_D(x)$ is fitted to a random training set $D$. Derive the expected squared test-error decomposition over both $Y$ and $D$. Distinguish its bias from parameter-estimator bias.

## 27. A Gaussian prior is more than a point estimate [10 marks]

**(a) [4 marks]** Suppose $X_t\mid\theta$ are conditionally i.i.d. $N(\theta,\sigma^2)$, with known $\sigma^2>0$, and $\theta\sim N(m_0,\tau^2)$, $\tau^2>0$. Complete the square in the likelihood times prior to derive the posterior mean and variance, including their precision form.

**(b) [3 marks]** For a new conditionally independent observation $X_*\mid\theta\sim N(\theta,\sigma^2)$, derive the posterior predictive distribution. Compare its variance with the distribution obtained by substituting the posterior mean into the observation model.

**(c) [3 marks]** Derive the minimum-posterior-MSE point estimator of $\theta$, identify its relationship to MAP in this model, and find the limits of $m_N,v_N$ as the prior becomes diffuse with $N$ fixed. Does that limit make the finite-sample plug-in predictive distribution exact?

## 28. Gaussian discriminants and when covariance estimates can be used [10 marks]

**(a) [3 marks]** For Gaussian class models $N_d(m_i,S_i)$ with positive-definite $S_i$ and positive class priors $\pi_i$, derive the quadratic log discriminant from the density. Express it as $x^\mathsf TW_ix+w_i^\mathsf Tx+b_i$.

**(b) [3 marks]** Assume all classes share $S$. Derive the affine LDA scores, the pairwise boundary equation, and the nearest-mean interpretation for equal priors. State when this becomes ordinary Euclidean nearest mean.

**(c) [4 marks]** Let all $K$ classes be represented, with $N_i$ observations each and total $N$. Count free covariance parameters for separate full versus shared full covariances. Then prove the rank bounds for a class covariance and for $S=\sum_i(N_i/N)S_i$. Give necessary sample-size conditions for invertibility and explain why they are not sufficient.

## 29. Estimating a Gaussian classifier from rectangular samples [12 marks]

**(a) [4 marks]** Class $C_1$ contains the four observations $(-1,-2),(-1,2),(1,-2),(1,2)$. Class $C_2$ contains $(1,0),(1,4),(3,0),(3,4)$. Fit maximum-likelihood class priors, means, separate covariance matrices, and the pooled covariance used by LDA. Use the likelihood denominator rather than an unbiased denominator.

**(b) [3 marks]** Derive a simplified expression for $g_2(x)-g_1(x)$ and the decision boundary. State which side is assigned to $C_2$, and explain whether fitting QDA to these particular estimates changes the classifier.

**(c) [2 marks]** Classify $x_*=(0.5,2)^\mathsf T$. Compare its squared Mahalanobis distances and squared Euclidean distances to the two means, and explain any disagreement between the resulting nearest-mean decisions.

**(d) [3 marks]** For two classes in two dimensions, count covariance parameters in separate full, shared full, shared diagonal, and shared spherical models. Which of these covariance assumptions exactly matches the estimates above? Check the necessary class and pooled sample-size inequalities, and say whether those inequalities alone establish invertibility.

## 30. Gaussian regression, prediction error, and model selection [12 marks]

**(a) [3 marks]** A regression model is $Y=w_0+w_1x+\varepsilon$, with independent $\varepsilon\sim N(0,\sigma^2)$, $\sigma^2>0$, and an input distribution independent of the fitted parameters. Starting from the joint likelihood, derive the least-squares objective and its normal equations for the coefficient vector $w=(w_0,w_1)^\mathsf T$.

**(b) [3 marks]** For observations $(x,y)=(-1,0),(0,1),(1,2),(2,5)$, compute the fitted line, its residual sum of squares, and the Gaussian observation-variance MLE when variance is estimated jointly with the line.

**(c) [3 marks]** In a separate repeated-training study at a fixed input, the true conditional mean is 2 and test-noise variance is $0.25$. Degree-1, degree-2, and degree-3 polynomial learners have training-set-averaged predictions $1.7,1.9,2.0$, and prediction variances $0.09,0.12,0.50$, respectively. Compute each expected squared test error and choose the best learner at this input.

**(d) [3 marks]** Three equally sized validation folds give mean squared errors $(1.0,1.4,1.2)$ for degree 1, $(0.6,0.9,0.9)$ for degree 2, and $(0.4,1.5,1.7)$ for degree 3. Choose a degree by cross-validation, describe the fitting/validation separation required, and explain why a smaller training error for degree 3 would not settle the choice.

