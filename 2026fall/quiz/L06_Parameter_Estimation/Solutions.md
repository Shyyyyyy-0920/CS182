# Lecture 06: Parameter Estimation

## Worked Solutions

**100 marks: 12 True/False × 1; 12 multiple response × 2; 4 proofs/derivations × 10; 2 applications × 12.**

Answer in English. Every multiple-response question has four options and 1–3 correct answers. Exact set: 2 marks; nonempty proper correct subset: 1; any wrong option or no answer: 0. Use `Quiz.tex` to type your responses in its marked regions.

Primary source: [Parameter_Estimation.pdf](../../lecture/Parameter_Estimation.pdf). Page numbers start at the cover.

## A. True/False

**1.** A full $d\times d$ empirical covariance estimated within a class from exactly $d$ observations is necessarily invertible if all feature sample variances are positive.

**False.** Centering gives rank at most $d-1$, so it is singular. Positive diagonal entries do not imply full rank because the columns may be linearly dependent.

*PDF pp.59,63,71,74; supplementary centered-rank argument.*

**2.** The posterior mean minimizes posterior expected loss for every possible loss function.

**False.** The posterior mean is optimal under squared error loss. Other losses can lead to other optimal estimates; for example, absolute error uses a posterior median.

*PDF pp.24-25; supplementary absolute-loss contrast.*

**3.** Zero covariance between two variables guarantees their independence without any assumption about their joint distribution.

**False.** Zero covariance only excludes linear association. Joint normality is a special case in which zero covariance implies independence.

*PDF pp.58,65-66.*

**4.** With positive class priors and a shared positive-definite covariance, Gaussian log-discriminant differences are affine, even when the class priors are unequal.

**True.** The common quadratic term and log determinant cancel across classes. Positive unequal priors change only the offsets. Distinct class means give a hyperplane equality boundary; identical means give a constant difference, with either no equality boundary or ties everywhere.

*PDF pp.70,75-76.*

**5.** If the posterior for an unknown Gaussian mean is normal, substituting its mean into the likelihood reproduces the full Bayesian posterior predictive variance.

**False.** The plug-in variance is the observation variance $\sigma^2$. Full prediction also includes posterior uncertainty in the mean, giving $\sigma^2+\operatorname{Var}(\theta\mid D)$. Normality makes posterior mean and mode coincide; it does not remove uncertainty.

*PDF pp.23-28; supplementary evaluated predictive variance.*

**6.** Filling missing values of one feature with its observed sample mean leaves that feature's maximum-likelihood sample variance unchanged.

**False.** If $n$ values were observed and $m>0$ were missing, the filled entries add zero centered squared deviation. The centered sum of squares stays the same but the denominator becomes $n+m$, shrinking a nonzero ML variance by $n/(n+m)$.

*PDF pp.59-60; supplementary imputation calculation.*

**7.** An unbiased estimator necessarily has smaller mean squared error than every biased estimator of the same parameter.

**False.** MSE is squared bias plus variance. A biased estimator can have enough smaller variance to obtain lower MSE.

*PDF pp.17-19.*

**8.** For an unrestricted categorical model on a closed probability simplex, a category observed zero times has maximum-likelihood probability zero.

**True.** The MLE is its count divided by $N$. Assigning positive mass to an unseen category would remove mass from observed categories and reduce their product likelihood. An imposed positive-probability restriction or a prior changes this conclusion.

*PDF pp.14-15; supplementary boundary condition.*

**9.** For observed data $D$, the likelihood $L(\theta;D)$ is generally a probability density over $\theta$ and must integrate to 1 with respect to $\theta$.

**False.** The likelihood is $p(D\mid\theta)$ viewed as a function of $\theta$, with $D$ fixed. It is normalized over possible data for each parameter, not generally over the parameter. A posterior over $\theta$ requires a prior and a normalizing evidence.

*PDF pp.9,22.*

**10.** If every Gaussian class has a diagonal covariance matrix, the classifier must have linear decision boundaries even when the diagonal variances differ across classes.

**False.** Different diagonal variances leave different coefficients of $x_j^2$ in the score differences. Conditional independence removes cross-products, but shared covariance is what cancels all quadratic terms.

*PDF pp.70-72,75,78.*

**11.** When the Gaussian mean is estimated from the same $N$ observations, the maximum-likelihood variance with denominator $N$ is unbiased for the population variance.

**False.** Its expectation is $(N-1)\sigma^2/N$, so it has downward bias. The denominator $N-1$ gives the usual unbiased estimator for $N>1$.

*PDF pp.16,19.*

**12.** A regression model using fixed features $1,x,x^2,\sin x$ can still be linear in its unknown parameters.

**True.** The model $w_0+w_1x+w_2x^2+w_3\sin x$ is linear in the coefficients $w$, even though its dependence on the original input is nonlinear.

*PDF pp.42,44,90.*

## B. Multiple Response

**13.** A categorical variable has counts $(3,0,7)$ in a sample of size 10. The parameter space is the closed simplex. Select every correct statement.

- **A.** At the MLE, the zero-count term in the log-likelihood is interpreted as zero. **Correct:** The absent category contributes no observations, so its likelihood factor is 1; the notation $0\log0=0$ represents this limiting convention.
- **B.** The MLE is $(0.3,0,0.7)$. **Correct:** The categorical likelihood is maximized at relative category counts.
- **C.** The simplex constraint can be discarded because the category likelihoods are independent functions of the parameters. **Incorrect:** The probabilities must sum to 1. Independent unconstrained optimization would not produce a normalized categorical model.
- **D.** A Lagrange-multiplier calculation that assumes every $p_i>0$ needs a separate boundary argument for the unseen category. **Correct:** The maximum has $p_2=0$, outside that assumed interior. Positive-count probabilities can be derived on their face of the simplex.

**Correct set: A, B, D.** *PDF pp.14-15; supplementary zero-count handling.*

**14.** Select every correct statement about the regression likelihood and design matrix.

- **A.** Independent Gaussian errors with known unequal variances lead to weighting each squared residual by the inverse of its variance. **Correct:** The log-density contribution is $-[r^t-g(x^t)]^2/(2\sigma_t^2)$, up to terms independent of the mean parameters.
- **B.** In a joint likelihood, an input-density term $p(x\mid\theta)$ may always be dropped when fitting $\theta$. **Incorrect:** It can only be dropped when it does not depend on the fitted parameters; the slides use that assumption explicitly.
- **C.** Independent Gaussian errors with one fixed, known common positive variance make maximum likelihood in the mean parameters equivalent to ordinary least squares. **Correct:** The parameter-dependent log likelihood is a negative positive-scaled sum of squared residuals.
- **D.** Fixed nonlinear basis functions of the inputs can be used while retaining a model linear in its coefficients. **Correct:** The design columns may be $x_j^2$, interactions, or $\sin x_j$; linearity here concerns the unknown coefficients.

**Correct set: A, C, D.** *PDF pp.38-44,88-90; supplementary known unequal-variance extension.*

**15.** A nonconstant Gaussian sample has $N=5$, sample mean $m=2$, and $\sum_t(x^t-m)^2=20$. Both the mean and variance are unknown. Select every correct statement.

- **A.** The usual unbiased variance estimate is 5. **Correct:** Its denominator is $N-1=4$, giving $20/4=5$.
- **B.** The denominator $N-1$ is required to maximize the Gaussian likelihood. **Incorrect:** That denominator corrects finite-sample bias; the likelihood optimum uses $N$.
- **C.** The maximum-likelihood standard deviation is $\sqrt5$. **Incorrect:** The standard deviation MLE is the positive square root of the variance MLE: $\sqrt4=2$. The number five is the unbiased variance estimate.
- **D.** The variance MLE is 4. **Correct:** The Gaussian maximum-likelihood variance is the centered sum of squares divided by $N$: $20/5=4$.

**Correct set: A, D.** *PDF pp.16-19.*

**16.** Assume a bivariate Gaussian with positive-definite covariance. Select every correct statement.

- **A.** For $\Sigma=\operatorname{diag}(9,1)$, the squared Mahalanobis distance from $\mu$ to $\mu+(3,1)^\mathsf T$ is 2. **Correct:** The quadratic form is $3^2/9+1^2/1=2$.
- **B.** A zero off-diagonal covariance makes these two jointly Gaussian coordinates independent. **Correct:** A diagonal Gaussian covariance factorizes the joint normal density into univariate normal densities.
- **C.** For the same covariance and displacement, the squared Euclidean distance is also 2. **Incorrect:** It is $3^2+1^2=10$; Mahalanobis distance rescales the coordinates.
- **D.** A positive correlation tilts the long axis of the Gaussian contour ellipse toward positive slope. **Correct:** The positive covariance aligns larger simultaneous deviations along the rising direction.

**Correct set: A, B, D.** *PDF pp.64-68.*

**17.** A Gaussian mean has prior $\theta\sim N(1,4)$. Three conditionally independent observations have distribution $N(\theta,9)$ and sample mean 4. Select every correct statement.

- **A.** The posterior variance is $12/7$. **Correct:** The posterior precision is $1/4+3/9=7/12$, so its variance is $12/7$.
- **B.** The posterior mean is $19/7$. **Correct:** The precision-weighted numerator is $1/4+(3/9)4=19/12$; dividing by $7/12$ gives $19/7$.
- **C.** The posterior MAP estimate equals the sample mean 4. **Incorrect:** The Gaussian posterior mode equals its posterior mean $19/7$; the value four is the likelihood maximizer before incorporating the prior.
- **D.** The full posterior predictive variance of a new observation is 9. **Incorrect:** It is $9+12/7=75/7$; variance 9 belongs to the plug-in distribution.

**Correct set: A, B.** *PDF pp.22-28; supplementary predictive evaluation.*

**18.** For two independent Bernoulli features conditional on class, use priors $0.6,0.4$, class $C_1$ feature probabilities $(0.5,0.8)$, and class $C_2$ probabilities $(0.9,0.3)$. Observe $x=(0,1)$. Select every correct statement.

- **A.** For probabilities strictly between 0 and 1, the log discriminant is affine in the binary coordinates. **Correct:** Expanding each term gives $x_j\log[p_{ij}/(1-p_{ij})]+\log(1-p_{ij})$, plus the log prior.
- **B.** The zero-valued first feature contributes no likelihood factor. **Incorrect:** For a zero-valued Bernoulli feature, the factor is $1-p_{ij}$, which is essential to the likelihood.
- **C.** The joint class-feature scores are $0.24$ and $0.012$. **Correct:** They are $0.6(1-0.5)(0.8)=0.24$ and $0.4(1-0.9)(0.3)=0.012$.
- **D.** The posterior probability of $C_1$ is $0.24$. **Incorrect:** The value $0.24$ is an unnormalized joint score. Normalize both scores to obtain $0.24/(0.24+0.012)=20/21$.

**Correct set: A, C.** *PDF p.85.*

**19.** Select every correct statement about model selection.

- **A.** The model evidence is generally just the largest likelihood over that model's parameters. **Incorrect:** For uncertain parameters it averages likelihood over a normalized parameter prior: $p(D\mid M)=\int p(D\mid\theta,M)p(\theta\mid M)\,d\theta$. A maximum is a different operation.
- **B.** A validation fold should be included in fitting the very predictor whose error it is intended to assess. **Incorrect:** Validation estimates generalization by evaluating data unused in that predictor's training.
- **C.** In a regularized objective, the penalty weight controls the strength of the preference for the penalized notion of simplicity. **Correct:** The objective is data error plus $\lambda$ times a complexity penalty; changing $\lambda$ changes this tradeoff.
- **D.** Bayesian model posterior probabilities are proportional to model evidence times model prior probabilities. **Correct:** Bayes' rule gives $p(M\mid D)\propto p(D\mid M)p(M)$.

**Correct set: C, D.** *PDF pp.22-23,47,51-53; supplementary evidence integral.*

**20.** Five i.i.d. Bernoulli observations are all equal to 1. Select every correct statement about maximum likelihood.

- **A.** The absence of an interior stationary point proves that no MLE exists on the closed interval. **Incorrect:** A maximizer can occur on the boundary; derivative-zero conditions only locate interior candidates.
- **B.** On the closed parameter interval $0\le p\le1$, the MLE is $p=1$. **Correct:** The likelihood is $p^5$, which increases up to the right endpoint.
- **C.** The log-likelihood has a stationary point in $0<p<1$. **Incorrect:** Its derivative is $5/p>0$, so no interior stationary point exists.
- **D.** On the open parameter interval $0<p<1$, the maximum occurs at $p=1-1/N=4/5$. **Incorrect:** The likelihood $p^5$ is strictly increasing throughout the open interval. Its supremum is approached as $p\to1$ and is never attained; $4/5$ is not a maximizer.

**Correct set: B.** *PDF pp.9-11; supplementary boundary analysis.*

**21.** A Gaussian classifier has $K=3$ classes and $d=4$ features. Count independent covariance parameters only, unless stated otherwise. Select every correct statement.

- **A.** The three class priors add three independent parameters. **Incorrect:** They sum to 1, leaving $K-1=2$ free parameters. Means additionally require $Kd=12$ parameters.
- **B.** One shared spherical covariance $s^2I$ requires 4 covariance parameters. **Incorrect:** All coordinate variances share one scalar $s^2$, so only one covariance parameter is free.
- **C.** Separate full covariance matrices require 30 parameters. **Correct:** Each symmetric $4\times4$ matrix has $4(5)/2=10$ independent entries; three require 30.
- **D.** One shared full covariance matrix requires 16 independent covariance parameters. **Incorrect:** A covariance matrix is symmetric. Its $4(5)/2=10$ independent entries are fewer than its 16 displayed matrix entries.

**Correct set: C.** *PDF pp.14-15,74-75,78,80,82.*

**22.** At a fixed test input, assume a new test response is independent of the training set and has conditional mean $f(x)$ and variance $\sigma^2(x)$. Select every correct statement.

- **A.** Increasing model complexity is a theorem that strictly increases estimator variance for every learning algorithm and distribution. **Incorrect:** The lecture's bias-variance discussion is a common tendency, not a universal strict monotonicity result.
- **B.** The expected test error is noise variance plus squared prediction bias plus the variance over training sets of the predictor. **Correct:** Two centered square expansions give $\sigma^2(x)+[E_Dg_D(x)-f(x)]^2+\operatorname{Var}_D(g_D(x))$.
- **C.** If every trained predictor equals $f(x)$, the expected squared test error still equals $\sigma^2(x)$. **Correct:** Both prediction bias and training-sample variance vanish, leaving response noise.
- **D.** The smallest error on a finite validation set identifies the population-optimal model with certainty. **Incorrect:** Validation estimates generalization from a finite sample and therefore has sampling uncertainty.

**Correct set: B, C.** *PDF pp.48-53,82; supplementary precise probabilistic conditions.*

**23.** For $N=4$ i.i.d. normal observations with true variance 1, let $Q=\sum_t(X_t-\bar X)^2$. You may use $E[Q]=3$ and $\operatorname{Var}(Q)=6$. Compare $V_{\mathrm{ML}}=Q/4$ and $V_{\mathrm U}=Q/3$. Select every correct statement.

- **A.** This example shows that the unbiased estimate must have the smaller MSE. **Incorrect:** Here $7/16<2/3$, so the biased maximum-likelihood variance has lower MSE.
- **B.** Under i.i.d. sampling with finite variance, the sample mean is consistent even though an arbitrary single observation need not be close to the mean. **Correct:** The sample mean has expectation $\mu$ and variance $\sigma^2/N$; Chebyshev's inequality makes its deviation probability tend to zero.
- **C.** The MSE of $V_{\mathrm{ML}}$ is $7/16$. **Correct:** Its bias is $3/4-1=-1/4$, its variance is $6/16$, and their MSE sum is $1/16+6/16=7/16$.
- **D.** The MSE of $V_{\mathrm U}$ is $2/3$. **Correct:** It is unbiased and has variance $6/9=2/3$.

**Correct set: B, C, D.** *PDF pp.17-20; supplementary supplied Gaussian residual moments.*

**24.** There are $d=5$ features, $K=3$ classes, and four observations in each class. Covariances are computed by centering within class. Select every correct statement.

- **A.** Increasing a class to six observations is by itself sufficient to guarantee a nonsingular full covariance. **Incorrect:** It makes full rank possible, but the centered observations may still occupy a lower-dimensional subspace.
- **B.** The shared pooled full covariance must also be singular. **Incorrect:** Its rank is at most $\min(d,N-K)=\min(5,9)=5$; pooled within-class directions can span all five dimensions.
- **C.** Every separate full class covariance estimate is singular. **Correct:** Its rank is at most $N_i-1=3<5$.
- **D.** A diagonal covariance approximation can be invertible even when every separate full covariance is singular. **Correct:** If all estimated coordinate variances are positive, the diagonal matrix is invertible even though the centered sample vectors span fewer than $d$ dimensions.

**Correct set: C, D.** *PDF pp.59,63,71,74-75,78; supplementary rank constraints.*

## 25. Discrete likelihoods, constraints, and naive Bayes [10 marks]

**(a) [3 marks]** For $N\ge1$ i.i.d. Bernoulli observations, let $s=\sum_t x^t$. Derive the MLE on the closed interval $[0,1]$, treating $0<s<N$, $s=0$, and $s=N$ separately. Establish that your candidates are global maxima.

**Worked solution:** The likelihood is $L(p)=p^s(1-p)^{N-s}$. For $0<s<N$,

$$

\ell'(p)=\frac{s}{p}-\frac{N-s}{1-p}=0
\quad\Longrightarrow\quad \hat p=s/N.

$$

The second derivative $-s/p^2-(N-s)/(1-p)^2<0$ gives strict concavity on the interior, and the likelihood is zero at both endpoints, so this is the unique global maximum. If $s=0$, $L=(1-p)^N$ is maximized at 0; if $s=N$, $L=p^N$ is maximized at 1. Marking: likelihood/derivative (1), interior global maximum (1), both boundary cases (1).

**(b) [4 marks]** For a categorical distribution with counts $n_1,\ldots,n_K$, $\sum_kn_k=N>0$, derive the constrained MLE. Include a justification for categories having zero counts rather than assuming an interior solution.

**Worked solution:** The log likelihood is $\ell(p)=\sum_kn_k\log p_k$, with $p_k\ge0$ and $\sum_kp_k=1$. First suppose all counts are positive. The Lagrangian $\ell+\eta(1-\sum_kp_k)$ gives $n_k/p_k=\eta$; summing $p_k=n_k/\eta$ yields $\eta=N$, hence $\hat p_k=n_k/N$. Strict concavity on the positive-count simplex proves global maximality. For zero-count categories, let their total probability be $z$. Write the observed-category probabilities as $p_k=(1-z)q_k$, with the $q_k$ summing to 1. Then

$$

\ell(p)=N\log(1-z)+\sum_{n_k>0}n_k\log q_k.

$$

This is maximized at $z=0$; any positive mass on unseen categories reduces the likelihood. Applying the previous derivation on the observed categories gives the same formula for all $k$, including zeros. Marking: constrained objective (1), multiplier derivation (1), global maximum (1), zero-count argument (1).

**(c) [3 marks]** For binary features conditionally independent given class, derive the class-conditional likelihood, the count-based class-specific MLEs, and an affine log discriminant in the binary input coordinates. State the condition for finite log coefficients.

**Worked solution:** For class $C_i$,

$$

p(x\mid C_i)=\prod_{j=1}^d p_{ij}^{x_j}(1-p_{ij})^{1-x_j}.

$$

With $N_i>0$ class-$i$ observations, the log likelihood separates over $j$, giving $\hat p_{ij}=(1/N_i)\sum_{t:C^t=C_i}x_j^t$. The class prior MLE is $N_i/N$. For $0<p_{ij}<1$,

$$

g_i(x)=\log P(C_i)+\sum_j\log(1-p_{ij})
+\sum_jx_j\log\frac{p_{ij}}{1-p_{ij}},

$$

which is affine in $x$. A zero or unit estimate requires handling zero likelihoods or infinite logs; finite coefficients cannot simply be assumed. Marking: likelihood (1), MLEs (1), affine expansion and boundary qualification (1).

*Source: PDF pp.9-15,85-86; supplementary boundary analysis.*

## 26. Gaussian variance and two kinds of bias-variance decomposition [10 marks]

**(a) [3 marks]** Let $X_1,\ldots,X_N$ be i.i.d. $N(\mu,v)$, with unknown $\mu$, $v>0$, and $N\ge2$. Use $\sum_t(X_t-\mu)^2=\sum_t(X_t-\bar X)^2+N(\bar X-\mu)^2$ to profile out $\mu$, then derive the variance MLE when $T=\sum_t(X_t-\bar X)^2>0$. What happens if $T=0$?

**Worked solution:** For each $v>0$, the identity shows that the squared-deviation term is minimized at $\mu=\bar X$. The profile log likelihood is

$$

\ell(v)=\text{constant}-\frac N2\log v-\frac{T}{2v},
\quad
\ell'(v)=\frac{T-Nv}{2v^2}.

$$

It increases for $v<T/N$ and decreases for $v>T/N$, so $\hat v=T/N$ is the global maximum. If $T=0$, $\ell(v)=\text{constant}-(N/2)\log v\to+\infty$ as $v\downarrow0$. No maximizer exists within the ordinary positive-variance model. Marking: profiling (1), derivative/global maximum (1), degeneracy (1).

**(b) [2 marks]** Assuming only i.i.d. observations with mean $\mu$ and finite variance $v$, prove $E[T]=(N-1)v$. Deduce the bias of $T/N$ and an unbiased correction.

**Worked solution:** The identity $T=\sum_t(X_t-\mu)^2-N(\bar X-\mu)^2$ gives

$$

E[T]=Nv-N\operatorname{Var}(\bar X)
=Nv-N(v/N)=(N-1)v.

$$

Thus $E[T/N]=(N-1)v/N$, with bias $-v/N$. For $N>1$, $T/(N-1)$ is unbiased. Marking: expectation calculation using $v/N$ (1), bias and correction (1).

**(c) [2 marks]** For a scalar estimator $d(D)$ of a fixed parameter $\theta$, derive $\operatorname{MSE}(d)=\operatorname{Var}(d)+[E(d)-\theta]^2$, and explain why unbiasedness alone does not rank estimators by MSE.

**Worked solution:** Write $d-\theta=(d-E[d])+(E[d]-\theta)$. Squaring and taking expectations gives the variance plus squared bias, because $E[d-E[d]]=0$ makes the cross term vanish. Removing bias does not control variance; a biased estimator can have smaller variance by more than its added squared bias. Marking: centered expansion/cross term (1), identity and comparison implication (1).

**(d) [3 marks]** At a fixed input $x$, let an independent future response $Y$ have conditional mean $f(x)$ and variance $\sigma^2(x)$. A predictor $g_D(x)$ is fitted to a random training set $D$. Derive the expected squared test-error decomposition over both $Y$ and $D$. Distinguish its bias from parameter-estimator bias.

**Worked solution:** First condition on $D$:

$$

E_Y[(Y-g_D(x))^2\mid x,D]
=\sigma^2(x)+(f(x)-g_D(x))^2,

$$

since $E[Y-f(x)\mid x,D]=0$ by independent test sampling. Let $\bar g(x)=E_D[g_D(x)]$. Expanding $f-g_D=(f-\bar g)+(\bar g-g_D)$ and averaging over $D$ removes the second cross term. Therefore

$$

E_{D,Y}[(Y-g_D(x))^2\mid x]
=\sigma^2(x)+[f(x)-\bar g(x)]^2+
\operatorname{Var}_D(g_D(x)).

$$

This bias concerns the average fitted prediction relative to $f(x)$; parameter-estimator bias instead compares $E[d]$ with a fixed parameter $\theta$. Marking: response-noise decomposition (1), training-set decomposition (1), final identity and distinction (1).

*Source: PDF pp.16-20,48-49; supplementary degenerate-sample qualification.*

## 27. A Gaussian prior is more than a point estimate [10 marks]

**(a) [4 marks]** Suppose $X_t\mid\theta$ are conditionally i.i.d. $N(\theta,\sigma^2)$, with known $\sigma^2>0$, and $\theta\sim N(m_0,\tau^2)$, $\tau^2>0$. Complete the square in the likelihood times prior to derive the posterior mean and variance, including their precision form.

**Worked solution:** Ignoring factors independent of $\theta$, the posterior kernel is

$$

\exp\left\{-\frac12\left[
\frac{\sum_t(X_t-\theta)^2}{\sigma^2}
+\frac{(\theta-m_0)^2}{\tau^2}\right]\right\}.

$$

The coefficient of $\theta^2$ is $A=N/\sigma^2+1/\tau^2$; the linear coefficient is $-2B$, where $B=\sum_tX_t/\sigma^2+m_0/\tau^2$. Since $A\theta^2-2B\theta=A(\theta-B/A)^2-B^2/A$, the normalized posterior is

$$

\theta\mid D\sim N(m_N,v_N),\qquad
v_N=A^{-1},\quad
m_N=v_N\left(\frac{N\bar X}{\sigma^2}+\frac{m_0}{\tau^2}\right).

$$

Thus posterior precision is the sum of data and prior precisions, and the mean is their normalized precision-weighted average. Marking: kernel (1), quadratic coefficients/completion (1), variance (1), mean/weights (1).

**(b) [3 marks]** For a new conditionally independent observation $X_*\mid\theta\sim N(\theta,\sigma^2)$, derive the posterior predictive distribution. Compare its variance with the distribution obtained by substituting the posterior mean into the observation model.

**Worked solution:** Conditional on the data, represent $X_*=\theta+\varepsilon_*$, where $\theta\sim N(m_N,v_N)$ and $\varepsilon_*\sim N(0,\sigma^2)$ are independent. Hence

$$

p(X_*\mid D)=\int p(X_*\mid\theta)p(\theta\mid D)\,d\theta
=N(m_N,\sigma^2+v_N).

$$

Equivalently, the laws of total expectation and variance give mean $m_N$ and variance $\sigma^2+v_N$, and Gaussian convolution identifies the normal distribution. Plugging in $\theta=m_N$ gives $N(m_N,\sigma^2)$, omitting posterior parameter uncertainty $v_N>0$. Marking: posterior averaging/convolution (1), predictive distribution (1), plug-in comparison (1).

**(c) [3 marks]** Derive the minimum-posterior-MSE point estimator of $\theta$, identify its relationship to MAP in this model, and find the limits of $m_N,v_N$ as the prior becomes diffuse with $N$ fixed. Does that limit make the finite-sample plug-in predictive distribution exact?

**Worked solution:** For any point estimate $a$,

$$

E[(\theta-a)^2\mid D]=v_N+(m_N-a)^2,

$$

so the unique squared-loss minimizer is $a=m_N$. The normal posterior also has its mode at $m_N$, so MAP and the posterior mean agree here. As $\tau^2\to\infty$, prior precision vanishes: $m_N\to\bar X$ and $v_N\to\sigma^2/N$. This variance remains positive for finite $N$; full prediction has limiting variance $\sigma^2(1+1/N)$, whereas the plug-in variance remains $\sigma^2$. Marking: squared-loss argument (1), MAP relationship (1), diffuse limits and predictive consequence (1).

*Source: PDF pp.22-28; supplementary evaluated predictive distribution.*

## 28. Gaussian discriminants and when covariance estimates can be used [10 marks]

**(a) [3 marks]** For Gaussian class models $N_d(m_i,S_i)$ with positive-definite $S_i$ and positive class priors $\pi_i$, derive the quadratic log discriminant from the density. Express it as $x^\mathsf TW_ix+w_i^\mathsf Tx+b_i$.

**Worked solution:** Taking logs and removing only the common $-d\log(2\pi)/2$ gives

$$

g_i(x)=-\frac12\log|S_i|-\frac12(x-m_i)^\mathsf TS_i^{-1}(x-m_i)+\log\pi_i.

$$

Using symmetry of $S_i^{-1}$, expand the quadratic form to obtain

$$

W_i=-\tfrac12S_i^{-1},\quad
w_i=S_i^{-1}m_i,\quad
b_i=-\tfrac12m_i^\mathsf TS_i^{-1}m_i-\tfrac12\log|S_i|+\log\pi_i.

$$

Different $S_i^{-1}$ generally leave quadratic terms in pairwise score differences, producing QDA boundaries. Marking: log density (1), expansion/coefficients (1), boundary implication (1).

**(b) [3 marks]** Assume all classes share $S$. Derive the affine LDA scores, the pairwise boundary equation, and the nearest-mean interpretation for equal priors. State when this becomes ordinary Euclidean nearest mean.

**Worked solution:** The terms $-x^\mathsf TS^{-1}x/2$ and $-\log|S|/2$ are common and cancel. Equivalent scores are

$$

\tilde g_i(x)=m_i^\mathsf TS^{-1}x-\tfrac12m_i^\mathsf TS^{-1}m_i+\log\pi_i.

$$

A boundary between distinct means satisfies

$$

(m_i-m_j)^\mathsf TS^{-1}x
-\tfrac12(m_i^\mathsf TS^{-1}m_i-m_j^\mathsf TS^{-1}m_j)
+\log(\pi_i/\pi_j)=0,

$$

a hyperplane. For equal priors, maximizing the original scores minimizes $(x-m_i)^\mathsf TS^{-1}(x-m_i)$, a squared Mahalanobis distance. This agrees with ordinary Euclidean nearest mean when $S=s^2I$ with common $s^2>0$. A shared diagonal matrix generally gives unequal coordinate weights. Marking: cancellation/affine score (1), boundary (1), metric interpretations (1).

**(c) [4 marks]** Let all $K$ classes be represented, with $N_i$ observations each and total $N$. Count free covariance parameters for separate full versus shared full covariances. Then prove the rank bounds for a class covariance and for $S=\sum_i(N_i/N)S_i$. Give necessary sample-size conditions for invertibility and explain why they are not sufficient.

**Worked solution:** A symmetric $d\times d$ covariance has $d(d+1)/2$ free entries. Separate matrices need $Kd(d+1)/2$, shared full covariance needs $d(d+1)/2$; both also need $Kd$ mean entries and $K-1$ free priors. Form $Z_i\in\mathbb R^{N_i\times d}$ with centered observations as rows. Its rows sum to zero, so $\operatorname{rank}(Z_i)\le N_i-1$. Since $S_i=Z_i^\mathsf TZ_i/N_i$,

$$

\operatorname{rank}(S_i)\le\min(d,N_i-1).

$$

Thus $N_i\ge d+1$ is necessary for a class covariance to be invertible. Stacking all $Z_i$ gives $Z$ and

$$

S=\frac1N Z^\mathsf TZ,\qquad
\operatorname{rank}(S)\le\min\!\left(d,\sum_i(N_i-1)\right)=\min(d,N-K).

$$

Hence $N-K\ge d$ is necessary for pooled invertibility. These inequalities only allow full rank: the centered observations must also span $\mathbb R^d$. Redundant features or samples confined to a subspace still cause singularity, invalidating the ordinary inverse/determinant density formula. Marking: counts (1), class rank/condition (1), pooled rank/condition (1), spanning and insufficiency (1).

*Source: PDF pp.59,63,70-82; supplementary centered-rank conditions.*

## 29. Estimating a Gaussian classifier from rectangular samples [12 marks]

**(a) [4 marks]** Class $C_1$ contains the four observations $(-1,-2),(-1,2),(1,-2),(1,2)$. Class $C_2$ contains $(1,0),(1,4),(3,0),(3,4)$. Fit maximum-likelihood class priors, means, separate covariance matrices, and the pooled covariance used by LDA. Use the likelihood denominator rather than an unbiased denominator.

**Worked solution:** Both classes contain four of eight observations, giving $\hat\pi_1=\hat\pi_2=1/2$. The means are $m_1=(0,0)^\mathsf T$, $m_2=(2,2)^\mathsf T$. Within either class, centered vectors are $(\pm1,\pm2)$ with all four sign combinations. Their centered outer products sum to $\operatorname{diag}(4,16)$, since the cross-products cancel. Dividing by 4 gives

$$

S_1=S_2=\begin{pmatrix}1&0\\0&4\end{pmatrix}.

$$

The pooled estimate $(1/2)S_1+(1/2)S_2$ is the same matrix. Marking: priors/means (1), centered outer-product computation (2), pooled estimate (1).

**(b) [3 marks]** Derive a simplified expression for $g_2(x)-g_1(x)$ and the decision boundary. State which side is assigned to $C_2$, and explain whether fitting QDA to these particular estimates changes the classifier.

**Worked solution:** Here $S^{-1}=\operatorname{diag}(1,1/4)$. With equal priors,

$$

g_2-g_1=(m_2-m_1)^\mathsf TS^{-1}x
-\tfrac12(m_2^\mathsf TS^{-1}m_2-m_1^\mathsf TS^{-1}m_1)
=2x_1+\tfrac12x_2-\tfrac52.

$$

Thus the boundary is $4x_1+x_2=5$, with $C_2$ preferred where $4x_1+x_2>5$. The separately fitted covariances happen to be equal, so the QDA quadratic terms cancel and produce this same classifier. Marking: score difference (1), boundary/side (1), QDA comparison (1).

**(c) [2 marks]** Classify $x_*=(0.5,2)^\mathsf T$. Compare its squared Mahalanobis distances and squared Euclidean distances to the two means, and explain any disagreement between the resulting nearest-mean decisions.

**Worked solution:** The squared Mahalanobis distances are $0.5^2+2^2/4=1.25$ to $m_1$ and $(-1.5)^2+0^2/4=2.25$ to $m_2$, so LDA chooses $C_1$. Euclidean distances squared are $4.25$ and $2.25$, so ordinary nearest mean chooses $C_2$. LDA discounts deviations in the second coordinate because its within-class variance is four times as large. Marking: distances and choices (1), covariance-based explanation (1).

**(d) [3 marks]** For two classes in two dimensions, count covariance parameters in separate full, shared full, shared diagonal, and shared spherical models. Which of these covariance assumptions exactly matches the estimates above? Check the necessary class and pooled sample-size inequalities, and say whether those inequalities alone establish invertibility.

**Worked solution:** The covariance counts are $2[2(3)/2]=6$, $2(3)/2=3$, $d=2$, and 1, respectively. The fitted covariance is shared diagonal with unequal coordinate variances, so the shared diagonal model matches it exactly; shared full and separate full also contain it. A shared spherical matrix cannot equal $\operatorname{diag}(1,4)$. Here each $N_i=4\ge d+1=3$, and $N-K=8-2=6\ge d=2$. These are necessary conditions only; the directly computed determinant $1(4)=4>0$ establishes invertibility for this sample. Marking: counts (1), exact covariance assumptions (1), sample-size checks versus determinant (1).

*Source: PDF pp.59,63-64,70-82; supplementary numerical sample.*

## 30. Gaussian regression, prediction error, and model selection [12 marks]

**(a) [3 marks]** A regression model is $Y=w_0+w_1x+\varepsilon$, with independent $\varepsilon\sim N(0,\sigma^2)$, $\sigma^2>0$, and an input distribution independent of the fitted parameters. Starting from the joint likelihood, derive the least-squares objective and its normal equations for the coefficient vector $w=(w_0,w_1)^\mathsf T$.

**Worked solution:** The joint likelihood factors as $\prod_t p(y^t\mid x^t,w,\sigma^2)p(x^t)$. Its log is

$$

-\frac N2\log(2\pi\sigma^2)-\frac{1}{2\sigma^2}\|y-Xw\|^2+\sum_t\log p(x^t),

$$

where row $t$ of $X$ is $(1,x^t)$. At any fixed positive $\sigma^2$, maximizing in $w$ is equivalent to minimizing $E(w)=\tfrac12\|y-Xw\|^2$. Differentiating gives $\nabla E=X^\mathsf T(Xw-y)$, so every optimum satisfies $X^\mathsf TXw=X^\mathsf Ty$. The inverse expression requires full column rank. Marking: likelihood and parameter-independent input term (1), squared-error equivalence (1), normal equations/rank condition (1).

**(b) [3 marks]** For observations $(x,y)=(-1,0),(0,1),(1,2),(2,5)$, compute the fitted line, its residual sum of squares, and the Gaussian observation-variance MLE when variance is estimated jointly with the line.

**Worked solution:** The sums are $N=4$, $\sum x=2$, $\sum x^2=6$, $\sum y=8$, and $\sum xy=12$. Thus

$$

\begin{pmatrix}4&2\\2&6\end{pmatrix}
\begin{pmatrix}\hat w_0\\\hat w_1\end{pmatrix}
=\begin{pmatrix}8\\12\end{pmatrix}.

$$

The determinant is 20, and the solution is $\hat w_0=1.2,\hat w_1=1.6$. The residuals $y-\hat y$ are $0.4,-0.2,-0.8,0.6$, giving SSE $=0.16+0.04+0.64+0.36=1.20$. The Gaussian variance MLE is SSE/$N=0.30$; a degrees-of-freedom correction addresses unbiasedness rather than likelihood maximization. Marking: normal system/solution (1), residuals and SSE (1), variance MLE (1).

**(c) [3 marks]** In a separate repeated-training study at a fixed input, the true conditional mean is 2 and test-noise variance is $0.25$. Degree-1, degree-2, and degree-3 polynomial learners have training-set-averaged predictions $1.7,1.9,2.0$, and prediction variances $0.09,0.12,0.50$, respectively. Compute each expected squared test error and choose the best learner at this input.

**Worked solution:** The squared biases are $(1.7-2)^2=0.09$, $(1.9-2)^2=0.01$, and 0. Adding variance and irreducible noise gives

$$

E_1=0.25+0.09+0.09=0.43,\quad
E_2=0.25+0.01+0.12=0.38,\quad
E_3=0.25+0+0.50=0.75.

$$

Degree 2 is best at this input. Degree 3 removes this bias but pays a larger training-sample variance. Marking: squared biases (1), three total errors (1), choice and explanation (1).

**(d) [3 marks]** Three equally sized validation folds give mean squared errors $(1.0,1.4,1.2)$ for degree 1, $(0.6,0.9,0.9)$ for degree 2, and $(0.4,1.5,1.7)$ for degree 3. Choose a degree by cross-validation, describe the fitting/validation separation required, and explain why a smaller training error for degree 3 would not settle the choice.

**Worked solution:** The equally weighted validation means are $1.2,0.8,1.2$, so cross-validation selects degree 2. For each fold, fit only on the other folds and score the held-out observations; after choosing the degree, refit that model on the available training data. A final test set should remain unused during tuning. More flexible nested polynomial models can reduce training SSE while fitting sampling noise, so their training-error ordering does not determine future error. Finite-fold validation is an estimate rather than a guarantee of the population ranking. Marking: fold averages/choice (1), correct separation and refit (1), training-versus-generalization explanation (1).

*Source: PDF pp.38-44,47-53,88-90; supplementary numerical model comparison.*

