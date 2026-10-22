# Lecture 03: Probability and Statistics

## Practice Quiz

**100 marks: 12 True/False × 1; 12 multiple response × 2; 4 proofs/derivations × 10; 2 applications × 12.**

Answer in English. Every multiple-response question has four options and 1–3 correct answers. Exact set: 2 marks; nonempty proper correct subset: 1; any wrong option or no answer: 0. Use `Quiz.tex` to type your responses in its marked regions.

Primary source: [Probability_Statistics.pdf](../../lecture/Probability_Statistics.pdf). Page numbers start at the cover.

## A. True/False

**1.** If two events have positive probabilities and are mutually exclusive, then they are independent.

**2.** For iid nonnormal observations with finite positive variance, the central limit theorem makes the standardized sample mean exactly standard normal at every finite sample size.

**3.** If $T\sim t_3$, its variance is one because it is a standardized ratio.

**4.** If two variables each have a normal marginal distribution and have zero covariance, they must be independent.

**5.** The identity $E(X+Y)=E(X)+E(Y)$ requires independence.

**6.** The weak law of large numbers says that, for a sufficiently large finite sample, the sample mean equals the population mean with probability one.

**7.** For iid observations with finite variance $\sigma^2$, the variance of their sample mean is $\sigma^2/n$.

**8.** For a random variable with a probability density, the density value $p(x)$ may exceed one even though $P(X=x)=0$.

**9.** For finite-variance variables, $\operatorname{Var}(X-Y)=\operatorname{Var}(X)+\operatorname{Var}(Y)-2\operatorname{Cov}(X,Y)$.

**10.** For iid $N(\mu,\sigma^2)$ observations with $n\ge2$, $(n-1)S^2/\sigma^2\sim\chi^2_{n-1}$, where $S^2=\sum_i(X_i-\bar X)^2/(n-1)$.

**11.** If $Z_1,\ldots,Z_k$ are independent standard normal variables, then $\sum_i Z_i^2$ has a chi-square distribution with $k$ degrees of freedom.

**12.** For events with $P(A),P(B)>0$, the identity $P(A\mid B)=P(B\mid A)$ holds even when the prior probabilities differ.

## B. Multiple Response

**13.** Let $X_1,\ldots,X_n$ be iid with mean $7$ and finite variance $9$. Select every justified conclusion.

- **A.** For every finite $n$, $\sum_iX_i\sim N(7n,9n)$.
- **B.** $P(|\bar X_n-7|>0.1)\to0$ as $n\to\infty$.
- **C.** $\operatorname{Var}(\bar X_n)=9/n^2$.
- **D.** For large $n$, $\bar X_n$ is approximately $N(7,9/n)$.

**14.** Select every valid probability identity. Assume all conditional probabilities displayed are defined.

- **A.** $P(A\cap B\cap C)=P(A)P(B\mid A)P(C\mid B)$.
- **B.** $P(A\mid B)=P(A\cap B)/P(A)$.
- **C.** If $A_1,A_2$ partition the sample space, then $P(B)=P(B\mid A_1)+P(B\mid A_2)$.
- **D.** $P(A\cup B)=P(A)+P(B)-P(A\cap B)$.

**15.** A joint density is $p(x,y)=2$ on $0<x<y<1$, and zero elsewhere. Select every correct statement.

- **A.** $p_X(x)=2(1-x)$ for $0<x<1$.
- **B.** $X$ and $Y$ are independent because their joint density is constant on its support.
- **C.** The density integrates to one.
- **D.** For $0<y<1$, $p_{X\mid Y}(x\mid y)=1$ on $0<x<y$.

**16.** Let $X$ take values $-1,0,1$ with equal probabilities and let $Y=X^2$. Select every correct claim.

- **A.** $E[X]=0$ and $E[Y]=2/3$.
- **B.** $X$ and $Y$ are independent.
- **C.** $\operatorname{Corr}(X,Y)$ is undefined because $E[X]=0$.
- **D.** $\operatorname{Cov}(X,Y)=2/9$.

**17.** The counts $(N_1,N_2,N_3)$ come from $10$ independent categorical trials with probabilities $(0.2,0.3,0.5)$. Select every correct statement.

- **A.** Each count is Bernoulli distributed.
- **B.** $N_1+N_2+N_3=10$ with probability one.
- **C.** $N_1,N_2,N_3$ are independent because the ten trials are independent.
- **D.** $P(N_1=2,N_2=3,N_3=5)=\frac{10!}{2!3!5!}(0.2)^2(0.3)^3(0.5)^5$.

**18.** For a variable with finite second moment, select every correct moment formula.

- **A.** $\operatorname{Var}(3X-7)=9\operatorname{Var}(X)$.
- **B.** $E[X^2]=(E X)^2$ for every random variable.
- **C.** $\operatorname{Cov}(2X+1,-Y+4)=-2\operatorname{Cov}(X,Y)$.
- **D.** $E[(X-E X)^2]=E[X^2]-(E X)^2$.

**19.** A nonsingular bivariate Gaussian has mean $(1,-2)^T$ and covariance $\Sigma=\begin{pmatrix}4&0\\0&9\end{pmatrix}$. Select every correct statement.

- **A.** The two coordinates are independent.
- **B.** The exponent contains $(x_1-1)^2/4+(x_2+2)^2/9$, multiplied by $-1/2$.
- **C.** The density normalization contains $|\Sigma|^{1/2}=6$.
- **D.** The density at its mean equals the probability that the vector equals its mean.

**20.** A count $K$ records successes in $20$ independent Bernoulli trials with success probability $0.15$. Select every correct formula.

- **A.** The fraction $K/20$ has variance $2.55/20$.
- **B.** $P(K=2)=\binom{20}{2}(0.15)^2(0.85)^{18}$.
- **C.** $E[K]=3$.
- **D.** $\operatorname{Var}(K)=3$.

**21.** For iid $X_i\sim N(\mu,\sigma^2)$, $n\ge3$, let $S^2=\sum_i(X_i-\bar X)^2/(n-1)$. Select every correct distribution statement.

- **A.** $\bar X$ and $S^2$ are independent.
- **B.** $\sqrt n(\bar X-\mu)/S\sim t_n$.
- **C.** $nS^2/\sigma^2\sim\chi^2_n$.
- **D.** $\sqrt n(\bar X-\mu)/\sigma\sim N(0,1)$.

**22.** Let $T\sim t_5$ and $W=4+2T$. Select every correct claim.

- **A.** $T$ is exactly standard normal because its degrees of freedom exceed two.
- **B.** $W$ has a general t distribution with location $4$ and scale $2$.
- **C.** $\operatorname{Var}(W)=4$.
- **D.** $E[W]=4$.

**23.** Two independent fair bits $U,V$ are drawn. Let $A=\{U=1\}$, $B=\{V=1\}$, and $C=\{U=V\}$. Select every correct claim.

- **A.** $P(C\mid A\cap B)=1$.
- **B.** Pairwise independence always implies independence of every triple intersection.
- **C.** $A$ and $C$ are independent.
- **D.** $A,B,C$ are mutually independent.

**24.** A binary joint distribution is $p(0,0)=0.30$, $p(0,1)=0.10$, $p(1,0)=0.20$, $p(1,1)=0.40$. Select every correct conclusion.

- **A.** $P(X=1)=0.60$.
- **B.** $P(X=0\mid Y=0)=0.30$.
- **C.** $X$ and $Y$ are independent.
- **D.** $P(Y=1\mid X=1)=2/3$.

## 25. Deriving total probability, Bayes' rule, and posterior odds [10 marks]

**(a) [3 marks]** Let $A_1,\ldots,A_k$ be a finite partition with $P(A_i)>0$. Starting from disjoint events and the product rule, derive a formula for $P(B)$. State the additional condition needed to condition on $B$.

**(b) [3 marks]** Use the result to derive $P(A_i\mid B)$, and prove that these posterior probabilities sum to one.

**(c) [4 marks]** For two hypotheses $H_1,H_0$ with positive priors, derive posterior odds after observing events $E$ and $F$. Assume the relevant likelihoods are positive. Show when the evidence contribution factors into $P(E\mid H_i)P(F\mid H_i)$.

## 26. Variance formulas and the effect of shared noise [10 marks]

**(a) [3 marks]** For finite-second-moment variables, derive $\operatorname{Cov}(X,Y)=E[XY]-E[X]E[Y]$ and the variance of $aX+bY+c$.

**(b) [4 marks]** Let $X_1,\ldots,X_n$ have common mean $\mu$ and finite variance $\sigma^2$. Derive the mean and variance of $\bar X_n$ in terms of all pairwise covariances. Specialize to independent observations.

**(c) [3 marks]** Suppose measurements have the form $X_i=\mu+B+\epsilon_i$, where $B,\epsilon_1,\ldots,\epsilon_n$ are independent, centered, and have variances $\tau^2,\sigma_\epsilon^2,\ldots,\sigma_\epsilon^2$. Derive $\operatorname{Var}(\bar X_n)$ and explain why the iid variance formula would fail.

## 27. Constructing the binomial distribution from trials [10 marks]

**(a) [3 marks]** Let $I_1,\ldots,I_n$ be independent Bernoulli variables with common success probability $p\in(0,1)$. For $K=\sum_i I_i$, derive $P(K=k)$ by counting disjoint outcomes.

**(b) [3 marks]** Derive the mean and variance of one Bernoulli variable directly from its two possible values. Then derive $E[K]$ without differentiating a generating function.

**(c) [4 marks]** Derive $\operatorname{Var}(K)$ and $\operatorname{Var}(K/n)$. Identify precisely where independence is used, and state the variance formula if the indicators are dependent but retain the same marginal success probability.

## 28. An exact Gaussian mean and residual decomposition [10 marks]

**(a) [3 marks]** Let $X_i$ be iid $N(\mu,\sigma^2)$, $\sigma>0$, $n\ge2$, and set $Z_i=(X_i-\mu)/\sigma$. Choose an orthogonal matrix $A$ whose first row is $(1,\ldots,1)/\sqrt n$, and let $Y=AZ$. Using the joint standard normal density, prove that the coordinates of $Y$ are independent standard normals.

**(b) [4 marks]** Express $\sqrt n(\bar X-\mu)/\sigma$ and $\sum_i(X_i-\bar X)^2/\sigma^2$ using these coordinates. Derive the chi-square law and prove independence of the sample mean and sample variance.

**(c) [3 marks]** For $S^2=\sum_i(X_i-\bar X)^2/(n-1)$, derive the exact distribution of $\sqrt n(\bar X-\mu)/S$. Explain why the same exact assertion does not follow merely from iid sampling with finite variance.

## 29. Two inspections and the base rate of defective components [12 marks]

**(a) [4 marks]** A manufacturer draws components from a stable production stream. A component is defective with probability $0.03$. One inspection flags a defective component with probability $0.90$, and flags a nondefective component with probability $0.04$. Compute the flag probability and the probability a flagged component is defective.

**(b) [4 marks]** The component is inspected twice. Assume the inspection outcomes are independent conditional on whether that component is defective, with the same sensitivity and false-flag probability each time. Compute the probability of two flags and the defect probability given two flags. Explain the factorization you used.

**(c) [4 marks]** A separate batch contains $200$ independently drawn components, each inspected once, with independent inspection noise across components. Let $K$ be its flag count. State its exact distribution, mean, variance, and the variance of its flag fraction $K/200$.

## 30. Exact inference for a normally distributed calibration error [12 marks]

**(a) [4 marks]** Nine independent calibration measurements, in millimeters, are 
$$
498,\ 502,\ 501,\ 499,\ 500,\ 503,\ 497,\ 500,\ 500.
$$
 Assume an iid $N(\mu,\sigma^2)$ model with both parameters unknown. Compute $\bar x$, the residual sum of squares, the unbiased sample variance $s^2$, and the estimated standard error of the mean.

**(b) [4 marks]** Compute the t statistic for the target mean $\mu_0=499$. Using $t_{8,0.975}=2.306$, derive and calculate a central $95\%$ confidence interval for $\mu$. State the exact sampling assumption behind this interval.

**(c) [4 marks]** For the reference variance $\sigma_0^2=4$, compute the chi-square statistic. Use $\chi^2_{8,0.025}=2.180$ and $\chi^2_{8,0.975}=17.535$ to derive and calculate a central $95\%$ confidence interval for $\sigma^2$.

