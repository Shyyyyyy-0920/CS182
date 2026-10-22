# Lecture 04: Optimization Primer

## Worked Solutions

**100 marks: 12 True/False × 1; 12 multiple response × 2; 4 proofs/derivations × 10; 2 applications × 12.**

Answer in English. Every multiple-response question has four options and 1–3 correct answers. Exact set: 2 marks; nonempty proper correct subset: 1; any wrong option or no answer: 0. Use `Quiz.tex` to type your responses in its marked regions.

Primary source: [Optimization_Primer.pdf](../../lecture/Optimization_Primer.pdf). Page numbers start at the cover.

## A. True/False

**1.** The feasible set defined by convex inequalities $f_i(x)\le0$ and affine equalities is convex.

**True.** Each convex sublevel set is convex, affine equality sets are convex, and intersections preserve convexity.

*PDF pp.16-18.*

**2.** For a symmetric matrix $Q$, the unconstrained quadratic $f(x)=\frac12x^TQx+c^Tx$ is convex if and only if $Q\succeq0$.

**True.** The Hessian is the constant matrix $Q$; apply the second-order convexity criterion on $\mathbb R^n$.

*PDF pp.18,20.*

**3.** The Lagrange dual function is concave even when the primal objective or inequality constraints are nonconvex.

**True.** For a fixed primal variable, the Lagrangian is affine in the multipliers. Taking its pointwise infimum produces a concave function, possibly with value $-\infty$.

*PDF pp.5,21.*

**4.** If a constraint is active at a KKT point, its multiplier must be strictly positive.

**False.** Complementary slackness only states $\lambda_if_i(x)=0$. For minimizing $x^2$ subject to $-x\le0$, $x=0$ is active and the KKT multiplier is zero.

*PDF pp.3,11-12.*

**5.** If a primal feasible point and a dual feasible point have the same finite objective value, they certify primal and dual optimality.

**True.** Weak duality gives $g(\lambda,\nu)\le d^*\le p^*\le f_0(x)$. Equality of the endpoints makes every inequality an equality.

*PDF pp.6-10,13-14.*

**6.** A differentiable function is convex whenever its gradient vanishes at at least one point.

**False.** For $f(x)=-x^2$, the gradient vanishes at zero, which is a global maximum. Convexity requires the global convexity inequality; for twice continuously differentiable functions on an open convex domain, it is equivalent to a positive semidefinite Hessian throughout that domain.

*PDF pp.18,22-24.*

**7.** Every local minimizer of a convex function over a convex feasible set is a global minimizer.

**True.** If a feasible point had a lower objective, points on the segment toward it would be feasible, arbitrarily close to the local minimizer, and have a lower objective by convexity.

*PDF pp.16-17,22.*

**8.** For differentiable convex objectives, every positive constant gradient-descent step size guarantees convergence from every starting point.

**False.** For $f(x)=x^2/2$, the update is $x_{k+1}=(1-\eta)x_k$. Taking $\eta=3$ makes nonzero iterates grow in magnitude. A step-size restriction is needed.

*PDF p.24.*

**9.** Equality multipliers may have either sign because the corresponding constraint values are zero at every primal feasible point.

**True.** If $h_j(x)=0$, then $\nu_jh_j(x)=0$ for every real $\nu_j$. Inequality multipliers have a different sign restriction.

*PDF pp.13-14.*

**10.** Every differentiable convex problem with an attained optimum has an optimal finite multiplier vector.

**False.** Consider minimizing $x$ subject to $x^2\le0$. The sole feasible point and optimum is zero, but stationarity would require $1+2\lambda\cdot0=0$, which no finite multiplier satisfies. Regularity conditions matter when asserting multiplier existence or dual attainment.

*PDF pp.8,12,14-18.*

**11.** At a KKT point, a strictly positive inequality multiplier implies that the corresponding inequality is active.

**True.** With $\lambda_i>0$, complementary slackness forces $f_i(x)=0$.

*PDF pp.11-12,15.*

**12.** For a minimization problem with constraints $f_i(x)\le0$, every real multiplier vector provides a valid dual lower bound.

**False.** The lower-bound proof uses $\lambda_i\ge0$, ensuring $\lambda_if_i(x)\le0$ at a feasible point. Negative inequality multipliers generally break that step.

*PDF pp.4-8.*

## B. Multiple Response

**13.** Let $f$ be differentiable and convex on $\mathbb R^n$. Select every conclusion that follows.

- **A.** The Hessian must be positive definite wherever it exists. **Incorrect:** Convexity requires positive semidefiniteness. A linear function has a zero Hessian.
- **B.** If $\nabla f(x)=0$, then $x$ is a global unconstrained minimizer. **Correct:** The first-order inequality reduces to $f(y)\ge f(x)$ for every $y$.
- **C.** $f(y)\ge f(x)+\nabla f(x)^T(y-x)$ for all $x,y$. **Correct:** The tangent affine function is a global lower bound by the first-order criterion.
- **D.** Every global minimizer is unique. **Incorrect:** A constant function is convex and has infinitely many global minimizers.

**Correct set: B, C.** *PDF pp.18,22.*

**14.** For a general primal minimization problem, select every statement justified without assuming convexity or strong duality.

- **A.** The dual function is concave on its effective domain. **Correct:** It is a pointwise infimum of affine functions of the multipliers.
- **B.** A zero gradient at a primal feasible point guarantees the global constrained optimum. **Incorrect:** For example, $(x^2-1)^2$ on the unconstrained real line has derivative zero at zero, yet lower values at $\pm1$.
- **C.** Any primal feasible $x$ and dual feasible multipliers satisfy $g(\lambda,\nu)\le f_0(x)$. **Correct:** Weak duality follows directly from feasibility and the infimum definition.
- **D.** If a differentiable Lagrangian has zero gradient at $x$, that point necessarily realizes its infimum. **Incorrect:** Without convexity, stationarity can describe a maximum or a saddle point.

**Correct set: A, C.** *PDF pp.6-8,12,21-24.*

**15.** Consider minimizing $(x-3)^2$ subject to $x\le1$, with $L(x,\lambda)=(x-3)^2+\lambda(x-1)$. Select every correct calculation.

- **A.** $g(\lambda)=2\lambda-\lambda^2/4$. **Correct:** Substituting $x=3-\lambda/2$ gives $\lambda^2/4+\lambda(2-\lambda/2)$.
- **B.** The unconstrained minimizer of $L(\cdot,\lambda)$ is $x=3-\lambda/2$. **Correct:** Stationarity gives $2(x-3)+\lambda=0$; the second derivative is positive.
- **C.** The dual optimum is attained at $\lambda=4$, with value $4$. **Correct:** The concave quadratic has derivative $2-\lambda/2$, so its maximum on $\lambda\ge0$ occurs at four.
- **D.** $\lambda=-2$ gives a valid dual certificate because the Lagrangian infimum is finite. **Incorrect:** It violates the nonnegative multiplier restriction for the inequality, even though its infimum is finite.

**Correct set: A, B, C.** *PDF pp.4-8,11-12.*

**16.** Which formulations satisfy the definition of a convex optimization problem? All variables shown are real.

- **A.** Minimize $-x^2$ subject to $-1\le x\le1$. **Incorrect:** The feasible set is convex, but the minimization objective is concave and not convex.
- **B.** Minimize $x$ subject to $x^2=1$. **Incorrect:** The equality produces the nonconvex feasible set $\{-1,1\}$; nonlinear equalities cannot generally be treated as affine constraints.
- **C.** Minimize $x^2+y^2$ subject to $x+y=1$ and $x\ge0$. **Correct:** The objective is convex, the equality is affine, and the inequality defines a half-space.
- **D.** Minimize $3x-y$ subject to $x^2+y^2\le4$. **Correct:** The objective is affine and the inequality is a sublevel set of the convex function $x^2+y^2-4$.

**Correct set: C, D.** *PDF pp.16-20.*

**17.** Let $G=\begin{pmatrix}2&6\\0&4\end{pmatrix}$ and $f(x)=\tfrac12x^TGx$ on $\mathbb R^2$. Select every correct statement.

- **A.** $\nabla f(x)=(2x_1+3x_2,\,3x_1+4x_2)^T$. **Correct:** The scalar quadratic uses the symmetric part $(G+G^T)/2$, giving the displayed derivative.
- **B.** $f$ is convex because the diagonal entries of $G$ are positive. **Incorrect:** The symmetric Hessian has determinant $8-9=-1$, so it is indefinite.
- **C.** The Hessian equals the nonsymmetric matrix $G$. **Incorrect:** The Hessian is $(G+G^T)/2=\begin{pmatrix}2&3\\3&4\end{pmatrix}$.
- **D.** The stationary point $x=0$ is a saddle point. **Correct:** The indefinite symmetric Hessian has both positive and negative eigenvalues, so the quadratic takes both signs arbitrarily close to zero.

**Correct set: A, D.** *PDF pp.18,20,24.*

**18.** Select every correct statement about stopping gradient descent or checking optimality.

- **A.** The norm $\|\nabla f(x)\|$ can be used as a scalar stationarity residual. **Correct:** A norm measures how close the gradient vector is to zero; its interpretation as an objective-error certificate requires extra assumptions.
- **B.** A small gradient norm alone gives a universal numerical bound on objective error for every differentiable convex function. **Incorrect:** For $f(x)=a x^2/2$, fixing a small nonzero gradient $g=ax$ gives objective error $g^2/(2a)$, which can be arbitrarily large as $a$ decreases.
- **C.** A zero gradient certifies a global unconstrained minimizer for a differentiable convex objective. **Correct:** The first-order lower bound gives $f(y)\ge f(x)$ for every $y$.
- **D.** For a constrained minimizer on the boundary, the objective gradient must itself be zero. **Incorrect:** The constraint gradients can balance the objective gradient through the KKT stationarity equation.

**Correct set: A, C.** *PDF pp.12,15,18,24.*

**19.** For minimizing $f_0(x)$ subject to $f_i(x)\le0$ and $h_j(x)=0$, select every correct Lagrangian or dual convention.

- **A.** The dual function is obtained by minimizing the Lagrangian only over primal feasible points. **Incorrect:** The dual function takes the infimum over the primal domain, without retaining the constraints that were moved into the Lagrangian.
- **B.** The dual problem maximizes $g(\lambda,\nu)$ over $\lambda\ge0$. **Correct:** It seeks the best lower bound on the primal minimization optimum.
- **C.** If the infimum of the Lagrangian is $-\infty$, that multiplier vector is dual feasible under the lecture definition. **Incorrect:** The lecture defines dual feasibility to require $g> -\infty$ in addition to nonnegative inequality multipliers.
- **D.** $L=f_0+\sum_i\lambda_if_i+\sum_j\nu_jh_j$, with $\lambda\ge0$ and unrestricted $\nu$. **Correct:** This sign convention makes each inequality term nonpositive at a feasible point.

**Correct set: B, D.** *PDF pp.4-8,13-14.*

**20.** The primal linear program is $\min_x c^Tx$ subject to $Ax\le b$, where $A\in\mathbb R^{m\times n}$ and $x$ is unrestricted. Select every correct statement.

- **A.** The dual has $n$ variables and $m$ equality constraints. **Incorrect:** There are $m$ multipliers, one for each primal inequality, and $n$ equality constraints.
- **B.** Its dual maximizes $-b^T\lambda$ subject to $A^T\lambda+c=0$ and $\lambda\ge0$. **Correct:** The Lagrangian is $(c+A^T\lambda)^Tx-b^T\lambda$; the unrestricted infimum is finite only when the coefficient of $x$ vanishes.
- **C.** If $A^T\lambda+c\ne0$, the dual function equals $-\infty$. **Correct:** Move $x$ arbitrarily far in the negative direction of its nonzero linear coefficient.
- **D.** The nonnegativity restriction on $\lambda$ can be dropped because $x$ is unrestricted. **Incorrect:** The sign of inequality multipliers follows from the primal inequality direction, independently of the domain of $x$.

**Correct set: B, C.** *PDF pp.5,9.*

**21.** For $f(x)=\tfrac12(x_1^2+4x_2^2)$, gradient descent uses a constant step size $\eta=0.6$. Select every correct conclusion.

- **A.** The iterates converge to zero from every starting point because the objective is strictly convex. **Incorrect:** The second-coordinate factor has magnitude $1.4>1$, so any nonzero second coordinate diverges.
- **B.** The update is $x_{k+1}=(0.4x_{1,k},-1.4x_{2,k})^T$. **Correct:** The gradient is $(x_1,4x_2)^T$; subtracting $0.6$ times it gives the factors.
- **C.** At any starting point with $x_{2,0}\ne0$, the second coordinate changes sign each iteration and grows in magnitude. **Correct:** The second-coordinate multiplier is the negative number $-1.4$.
- **D.** If $x_{2,0}=0$, the iterates converge to zero. **Correct:** The second coordinate stays zero and the first is multiplied repeatedly by $0.4$.

**Correct set: B, C, D.** *PDF pp.18,20,24.*

**22.** Let $f$ be convex and let $X$ be a finitely supported random vector in its convex domain. Select every valid use of convexity.

- **A.** The pointwise maximum of two convex functions is convex. **Correct:** It is a special case of the pointwise supremum rule.
- **B.** The pointwise minimum of any two convex functions is convex. **Incorrect:** The minimum of the affine functions $x$ and $-x$ is $-|x|$, which is not convex.
- **C.** Jensen's inequality requires independent coordinates of $X$. **Incorrect:** Only the weighted convexity inequality and existence of the expectations are needed.
- **D.** $f(E[X])\ge E[f(X)]$ for every such convex function and random vector. **Incorrect:** Jensen gives the reverse inequality. For $f(x)=x^2$ and a fair sign $X\in\{-1,1\}$, the displayed claim reads $0\ge1$, which is false.

**Correct set: A.** *PDF pp.17-18.*

**23.** Minimize $x^2$ subject to $-x\le0$ and $-2x\le0$. Select every correct statement at $x^*=0$.

- **A.** $(x^*,\lambda_1,\lambda_2)=(0,1,0)$ satisfies all KKT conditions. **Incorrect:** The point is feasible and complementary slackness holds, but stationarity fails: $2(0)-1-2(0)=-1\ne0$.
- **B.** Both inequalities are active. **Correct:** Both constraint values equal zero at the point.
- **C.** The stationarity equation is $2x-\lambda_1-\lambda_2=0$. **Incorrect:** The second constraint has gradient $-2$, so the correct equation is $2x-\lambda_1-2\lambda_2=0$.
- **D.** Both multipliers must be strictly positive. **Incorrect:** Stationarity requires $-\lambda_1-2\lambda_2=0$; nonnegativity then forces both multipliers to be zero.

**Correct set: B.** *PDF pp.3,11-12.*

**24.** An algorithm has a primal feasible point with objective $11.2$ and dual feasible multipliers with dual value $10.9$. Select every justified conclusion.

- **A.** The optimal value must equal the midpoint $11.05$. **Incorrect:** The interval bounds the optimum but does not identify its midpoint as optimal.
- **B.** The distance from the primal point to every minimizer is at most $0.3$. **Incorrect:** The gap bounds objective error. A distance guarantee needs additional curvature information and a corresponding conversion.
- **C.** The primal point is at most $0.3$ above the optimal objective value. **Correct:** From $p^*\ge10.9$, $11.2-p^*\le0.3$.
- **D.** The optimal primal value belongs to $[10.9,11.2]$. **Correct:** The dual value is a lower bound and the feasible primal value is an upper bound.

**Correct set: C, D.** *PDF pp.6-10.*

## 25. Proving the first-order characterization of convexity [10 marks]

**(a) [5 marks]** Let $f$ be differentiable on an open convex domain. Starting with the defining convexity inequality, prove that convexity implies $f(y)\ge f(x)+\nabla f(x)^T(y-x)$ for any $x,y$ in the domain.

**Worked solution:** For $0<t\le1$, convexity gives $f(x+t(y-x))\le(1-t)f(x)+tf(y)$. Rearranging yields 
$$
\frac{f(x+t(y-x))-f(x)}{t}\le f(y)-f(x).
$$
 Differentiability makes the left side converge to $\nabla f(x)^T(y-x)$ as $t\downarrow0$. Hence $f(y)\ge f(x)+\nabla f(x)^T(y-x)$. Convexity of the domain ensures the entire segment remains in the domain.

**(b) [5 marks]** Conversely, assume the first-order inequality holds for every pair $x,y$. Prove the defining convexity inequality using $z=(1-t)x+ty$, $0<t<1$, as the expansion point.

**Worked solution:** Applying the assumed inequality at $z$ gives $f(x)\ge f(z)+\nabla f(z)^T(x-z)$ and $f(y)\ge f(z)+\nabla f(z)^T(y-z)$. Multiply these by $1-t$ and $t$, respectively, and add. Since $(1-t)(x-z)+t(y-z)=0$, the gradient terms cancel: 
$$
(1-t)f(x)+tf(y)\ge f(z)=f((1-t)x+ty).
$$
 At $t=0$ or $t=1$, equality is immediate. This proves convexity.

*Source: PDF pp.17-18.*

## 26. Dual concavity, weak duality, and complementary slackness [10 marks]

**(a) [4 marks]** For $L(x,\lambda,\nu)=f_0(x)+\sum_i\lambda_if_i(x)+\sum_j\nu_jh_j(x)$, prove directly that $g(\lambda,\nu)=\inf_x L(x,\lambda,\nu)$ is concave, without imposing convexity on the primal functions. Work with multiplier pairs having finite dual values.

**Worked solution:** Write a combined multiplier vector as $u=(\lambda,\nu)$. For $0\le t\le1$, affinity in multipliers gives $L(x,tu+(1-t)v)=tL(x,u)+(1-t)L(x,v)$. For every $x$, the right side is at least $t\inf_zL(z,u)+(1-t)\inf_zL(z,v)=tg(u)+(1-t)g(v)$. Taking the infimum over $x$ yields 
$$
g(tu+(1-t)v)\ge tg(u)+(1-t)g(v).
$$
 No convexity of the functions in $x$ was used.

**(b) [3 marks]** For primal feasible $x$ and $\lambda\ge0$, derive $g(\lambda,\nu)\le f_0(x)$ and hence weak duality. Explain the different restrictions on inequality and equality multipliers.

**Worked solution:** Primal feasibility gives $f_i(x)\le0$ and $h_j(x)=0$. Thus 
$$
g(\lambda,\nu)\le L(x,\lambda,\nu)=f_0(x)+\sum_i\lambda_if_i(x)\le f_0(x).
$$
 The last inequality uses $\lambda_i\ge0$; equality terms vanish for every real $\nu_j$. Taking the infimum over feasible $x$ and the supremum over dual feasible multipliers gives $d^*\le p^*$.

**(c) [3 marks]** Suppose feasible $x^*,\lambda^*,\nu^*$ have finite values and $f_0(x^*)=g(\lambda^*,\nu^*)$. Derive complementary slackness term by term and show that $x^*$ minimizes the Lagrangian.

**Worked solution:** The inequalities from the preceding proof become 
$$
g(\lambda^*,\nu^*)\le L(x^*,\lambda^*,\nu^*)\le f_0(x^*)=g(\lambda^*,\nu^*).
$$
 Therefore both inequalities are equalities. In particular, $\sum_i\lambda_i^*f_i(x^*)=0$. Each summand is nonpositive, so each must be zero: $\lambda_i^*f_i(x^*)=0$. The other equality, $L(x^*,\lambda^*,\nu^*)=\inf_xL(x,\lambda^*,\nu^*)$, says precisely that $x^*$ globally minimizes the Lagrangian.

*Source: PDF pp.4-8,11,13-14,21.*

## 27. Why convex KKT conditions are sufficient [10 marks]

**(a) [4 marks]** Assume $f_0,f_i$ are differentiable convex functions on $\mathbb R^n$, and $h_j$ are affine. Suppose $(x^*,\lambda^*,\nu^*)$ satisfies primal feasibility, $\lambda^*\ge0$, complementary slackness, and stationarity. Prove that $x^*$ globally minimizes $L(\cdot,\lambda^*,\nu^*)$.

**Worked solution:** Because $\lambda_i^*\ge0$, the weighted sum $f_0+\sum_i\lambda_i^*f_i$ is convex. Each equality contribution $\nu_j^*h_j$ is affine even when $\nu_j^*$ is negative. Thus $L(\cdot,\lambda^*,\nu^*)$ is differentiable convex. Stationarity states that its gradient at $x^*$ is zero. Applying the first-order inequality gives 
$$
L(x,\lambda^*,\nu^*)\ge L(x^*,\lambda^*,\nu^*)+0^T(x-x^*)
$$
 for every $x$, proving global minimality.

**(b) [3 marks]** Use this Lagrangian minimum to prove primal and dual optimality and zero duality gap. State whether a constraint qualification is needed for this sufficiency implication once the displayed KKT point is given.

**Worked solution:** Feasibility and complementary slackness imply $L(x^*,\lambda^*,\nu^*)=f_0(x^*)$. Since the previous part establishes a global minimum, $g(\lambda^*,\nu^*)=L(x^*,\lambda^*,\nu^*)=f_0(x^*)$. The finite equality of a dual lower bound and a feasible primal upper bound proves both optimalities and zero gap by weak duality. No constraint qualification is needed for this sufficiency implication; such conditions are used to establish that suitable multipliers exist at an optimum.

**(c) [3 marks]** If $f_0$ is strictly convex, prove that the primal minimizer is unique. Identify the role of the convexity of the feasible set.

**Worked solution:** Convex inequalities and affine equalities define a convex feasible set. Suppose distinct feasible minimizers $u,v$ both have value $p^*$. Their midpoint $w=(u+v)/2$ is feasible. Strict convexity gives 
$$
f_0(w)<\tfrac12f_0(u)+\tfrac12f_0(v)=p^*,
$$
 contradicting optimality. The convex feasible set is needed to ensure the midpoint is an admissible competitor.

*Source: PDF pp.12-18,22; sufficiency and uniqueness are derived from the lecture conditions.*

## 28. Deriving a quadratic gradient-descent step-size bound [10 marks]

**(a) [3 marks]** Let $f(x)=\frac12x^TQx+c^Tx+r$, where $Q$ is symmetric. Derive its gradient and Hessian by expanding $f(x+h)$. State the condition for convexity on $\mathbb R^n$.

**Worked solution:** Symmetry gives 
$$
f(x+h)=f(x)+(Qx+c)^Th+\tfrac12h^TQh.
$$
 Therefore $\nabla f(x)=Qx+c$ and $\nabla^2f(x)=Q$. The second-order criterion gives convexity exactly when $Q\succeq0$.

**(b) [4 marks]** Assume $0\preceq Q\preceq LI$ with $L>0$, let $g=\nabla f(x)$, and define $x^+=x-\eta g$. Derive an upper bound on $f(x^+)-f(x)$, and give a range of $\eta$ guaranteeing strict decrease whenever $g\ne0$.

**Worked solution:** Substitute $h=-\eta g$ in the exact expansion: 
$$
f(x^+)-f(x)=-\eta\|g\|^2+\tfrac12\eta^2g^TQg.
$$
 Since $Q\preceq LI$, $g^TQg\le L\|g\|^2$, so 
$$
f(x^+)-f(x)\le-\eta\left(1-\frac{\eta L}{2}\right)\|g\|^2.
$$
 For $0<\eta<2/L$, the coefficient is strictly negative whenever the gradient is nonzero. At $\eta=2/L$, this estimate guarantees only nonincrease, not strict decrease or convergence.

**(c) [3 marks]** Now assume $Q\succ0$. Prove convergence of constant-step gradient descent for $0<\eta<2/\lambda_{\max}(Q)$ by diagonalizing $Q$. Give a one-dimensional counterexample at the upper endpoint.

**Worked solution:** The unique stationary point is $x^*=-Q^{-1}c$. The error satisfies $e_{k+1}=(I-\eta Q)e_k$. Diagonalize $Q=U\operatorname{diag}(\lambda_1,\ldots,\lambda_n)U^T$, with all $\lambda_i>0$. In coordinates $z_k=U^Te_k$, each error coordinate is multiplied by $1-\eta\lambda_i$. The stated interval ensures $|1-\eta\lambda_i|<1$ for every coordinate, so $z_k\to0$ and $x_k\to x^*$. At the endpoint for $f(x)=Lx^2/2$, the factor is $-1$, so a nonzero start alternates forever.

*Source: PDF pp.18,20,24; the descent bound and spectral convergence argument are supplemental derivations.*

## 29. Capacity planning with an active resource cap [12 marks]

**(a) [4 marks]** A planning model chooses nonnegative production amounts $x,y$ with total $x+y=4$, subject to the capacity cap $x\le2.5$. It minimizes $f(x,y)=(x-5)^2+2(y-2)^2$. Eliminate the equality constraint, determine the feasible interval, and find the unique minimizer and objective value.

**Worked solution:** The equality gives $y=4-x$. Nonnegativity and the cap give $0\le x\le2.5$. The restricted objective is $(x-5)^2+2(2-x)^2=3x^2-18x+33$, with derivative $6x-18$. Its unconstrained minimizer is $x=3$, outside the interval; the function is decreasing throughout the interval. Therefore $x^*=2.5$, $y^*=1.5$, and $f^*=(-2.5)^2+2(-0.5)^2=6.75=27/4$. The objective Hessian is $\operatorname{diag}(2,4)\succ0$, so this feasible minimizer is unique.

**(b) [4 marks]** Write the Lagrangian using multipliers $\alpha,\beta,\lambda\ge0$ for $-x,-y,x-2.5\le0$, respectively, and unrestricted $\nu$ for $x+y-4=0$. Find multipliers at the proposed optimum and give a dual certificate by evaluating the Lagrangian infimum.

**Worked solution:** The Lagrangian is 
$$
L=(x-5)^2+2(y-2)^2-\alpha x-\beta y+\lambda(x-2.5)+\nu(x+y-4).
$$
 Since $x^*,y^*>0$, complementary slackness gives $\alpha=\beta=0$. The stationarity equations at $(2.5,1.5)$ are $-5+\lambda+\nu=0$ and $-2+\nu=0$; hence $\nu=2$, $\lambda=3$. These multipliers have the required signs, and the cap is active. For these multipliers, minimizing the strictly convex Lagrangian over unrestricted $x,y$ gives the same $(2.5,1.5)$. The constraint contributions there vanish, so $g(0,0,3,2)=6.75=f(x^*,y^*)$, certifying optimality.

**(c) [4 marks]** Before convergence, a solver reports the feasible plan $(x,y)=(2,2)$ and multipliers $(\alpha,\beta,\lambda,\nu)=(0,0,2,2)$. Compute their dual value, a guaranteed interval for $p^*$, and an upper bound on the plan's objective error.

**Worked solution:** The primal objective is $f(2,2)=9$. With the reported multipliers, Lagrangian stationarity gives $2(x-5)+2+2=0$ and $4(y-2)+2=0$, so its unconstrained minimum occurs at $(3,1.5)$. This point need not satisfy the capacity cap when evaluating the dual function. Its objective is $4.5$; the multiplier terms are $2(3-2.5)+2(3+1.5-4)=1+1=2$. Thus $g=6.5$, and weak duality certifies $p^*\in[6.5,9]$. The reported plan is at most $9-6.5=2.5$ above optimum. Its actual error, using the optimum found earlier, is $9-6.75=2.25$, consistent with the bound.

*Source: PDF pp.2-15,17-20.*

## 30. Choosing a stable learning rate for a quadratic calibration loss [12 marks]

**(a) [4 marks]** A calibration model minimizes $f(u,v)=\tfrac12(2u^2+8v^2)-4u+8v$ on $\mathbb R^2$. Compute the gradient, Hessian, unique optimizer, and minimum value. Explain why a stationary point is sufficient here.

**Worked solution:** The gradient is $(2u-4,8v+8)^T$ and the Hessian is $Q=\operatorname{diag}(2,8)\succ0$. Solving the gradient equations gives $(u^*,v^*)=(2,-1)$. Substitution gives $f^*=\tfrac12(8+8)-8-8=-8$. Positive definiteness makes the objective strictly convex, so the stationary point is the unique global minimizer.

**(b) [4 marks]** From $(u_0,v_0)=(0,0)$, calculate one gradient-descent step and its objective for $\eta=0.2$ and for $\eta=0.3$. Compare each objective to the initial value and to the optimum.

**Worked solution:** The initial gradient is $(-4,8)^T$, so $(u_1,v_1)=(4\eta,-8\eta)$, and $f(0,0)=0$. For $\eta=0.2$, the point is $(0.8,-1.6)$ and the objective is $0.64+10.24-3.2-12.8=-5.12$, an improvement with objective error $2.88$. For $\eta=0.3$, the point is $(1.2,-2.4)$ and the objective is $1.44+23.04-4.8-19.2=0.48$, an increase with error $8.48$. Both comparisons use the same exact quadratic loss.

**(c) [4 marks]** Derive the constant-step interval guaranteeing convergence from every start. At the boundary step $\eta=0.25$, determine the behavior from $(0,0)$ and explain why a zero change in objective would not certify convergence.

**Worked solution:** The error updates are $u_{k+1}-2=(1-2\eta)(u_k-2)$ and $v_{k+1}+1=(1-8\eta)(v_k+1)$. Both contraction conditions require $0<\eta<2/8=0.25$. At $\eta=0.25$, $u_k=2-2(1/2)^k$ tends to two, while $v_k=-1+(-1)^k$ alternates between zero and minus two. Completing squares gives $f(u,v)=-8+(u-2)^2+4(v+1)^2$, so the objective tends to $-4$, with successive changes tending to zero, despite failure of the iterates to converge or reach the optimum. A small objective change alone can therefore miss an oscillating, nonoptimal state. For an exact constant-objective counterexample, start instead at $(u_0,v_0)=(2,0)$. Then $u_k=2$ and $v_k$ alternates between zero and $-2$, so $f(u_k,v_k)=-4$ at every step even though $f^*=-8$.

*Source: PDF pp.18,20,24; stability calculations apply the supplemental quadratic bound.*

