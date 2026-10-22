# Lecture 04: Optimization Primer

## Practice Quiz

**100 marks: 12 True/False × 1; 12 multiple response × 2; 4 proofs/derivations × 10; 2 applications × 12.**

Answer in English. Every multiple-response question has four options and 1–3 correct answers. Exact set: 2 marks; nonempty proper correct subset: 1; any wrong option or no answer: 0. Use `Quiz.tex` to type your responses in its marked regions.

Primary source: [Optimization_Primer.pdf](../../lecture/Optimization_Primer.pdf). Page numbers start at the cover.

## A. True/False

**1.** The feasible set defined by convex inequalities $f_i(x)\le0$ and affine equalities is convex.

**2.** For a symmetric matrix $Q$, the unconstrained quadratic $f(x)=\frac12x^TQx+c^Tx$ is convex if and only if $Q\succeq0$.

**3.** The Lagrange dual function is concave even when the primal objective or inequality constraints are nonconvex.

**4.** If a constraint is active at a KKT point, its multiplier must be strictly positive.

**5.** If a primal feasible point and a dual feasible point have the same finite objective value, they certify primal and dual optimality.

**6.** A differentiable function is convex whenever its gradient vanishes at at least one point.

**7.** Every local minimizer of a convex function over a convex feasible set is a global minimizer.

**8.** For differentiable convex objectives, every positive constant gradient-descent step size guarantees convergence from every starting point.

**9.** Equality multipliers may have either sign because the corresponding constraint values are zero at every primal feasible point.

**10.** Every differentiable convex problem with an attained optimum has an optimal finite multiplier vector.

**11.** At a KKT point, a strictly positive inequality multiplier implies that the corresponding inequality is active.

**12.** For a minimization problem with constraints $f_i(x)\le0$, every real multiplier vector provides a valid dual lower bound.

## B. Multiple Response

**13.** Let $f$ be differentiable and convex on $\mathbb R^n$. Select every conclusion that follows.

- **A.** The Hessian must be positive definite wherever it exists.
- **B.** If $\nabla f(x)=0$, then $x$ is a global unconstrained minimizer.
- **C.** $f(y)\ge f(x)+\nabla f(x)^T(y-x)$ for all $x,y$.
- **D.** Every global minimizer is unique.

**14.** For a general primal minimization problem, select every statement justified without assuming convexity or strong duality.

- **A.** The dual function is concave on its effective domain.
- **B.** A zero gradient at a primal feasible point guarantees the global constrained optimum.
- **C.** Any primal feasible $x$ and dual feasible multipliers satisfy $g(\lambda,\nu)\le f_0(x)$.
- **D.** If a differentiable Lagrangian has zero gradient at $x$, that point necessarily realizes its infimum.

**15.** Consider minimizing $(x-3)^2$ subject to $x\le1$, with $L(x,\lambda)=(x-3)^2+\lambda(x-1)$. Select every correct calculation.

- **A.** $g(\lambda)=2\lambda-\lambda^2/4$.
- **B.** The unconstrained minimizer of $L(\cdot,\lambda)$ is $x=3-\lambda/2$.
- **C.** The dual optimum is attained at $\lambda=4$, with value $4$.
- **D.** $\lambda=-2$ gives a valid dual certificate because the Lagrangian infimum is finite.

**16.** Which formulations satisfy the definition of a convex optimization problem? All variables shown are real.

- **A.** Minimize $-x^2$ subject to $-1\le x\le1$.
- **B.** Minimize $x$ subject to $x^2=1$.
- **C.** Minimize $x^2+y^2$ subject to $x+y=1$ and $x\ge0$.
- **D.** Minimize $3x-y$ subject to $x^2+y^2\le4$.

**17.** Let $G=\begin{pmatrix}2&6\\0&4\end{pmatrix}$ and $f(x)=\tfrac12x^TGx$ on $\mathbb R^2$. Select every correct statement.

- **A.** $\nabla f(x)=(2x_1+3x_2,\,3x_1+4x_2)^T$.
- **B.** $f$ is convex because the diagonal entries of $G$ are positive.
- **C.** The Hessian equals the nonsymmetric matrix $G$.
- **D.** The stationary point $x=0$ is a saddle point.

**18.** Select every correct statement about stopping gradient descent or checking optimality.

- **A.** The norm $\|\nabla f(x)\|$ can be used as a scalar stationarity residual.
- **B.** A small gradient norm alone gives a universal numerical bound on objective error for every differentiable convex function.
- **C.** A zero gradient certifies a global unconstrained minimizer for a differentiable convex objective.
- **D.** For a constrained minimizer on the boundary, the objective gradient must itself be zero.

**19.** For minimizing $f_0(x)$ subject to $f_i(x)\le0$ and $h_j(x)=0$, select every correct Lagrangian or dual convention.

- **A.** The dual function is obtained by minimizing the Lagrangian only over primal feasible points.
- **B.** The dual problem maximizes $g(\lambda,\nu)$ over $\lambda\ge0$.
- **C.** If the infimum of the Lagrangian is $-\infty$, that multiplier vector is dual feasible under the lecture definition.
- **D.** $L=f_0+\sum_i\lambda_if_i+\sum_j\nu_jh_j$, with $\lambda\ge0$ and unrestricted $\nu$.

**20.** The primal linear program is $\min_x c^Tx$ subject to $Ax\le b$, where $A\in\mathbb R^{m\times n}$ and $x$ is unrestricted. Select every correct statement.

- **A.** The dual has $n$ variables and $m$ equality constraints.
- **B.** Its dual maximizes $-b^T\lambda$ subject to $A^T\lambda+c=0$ and $\lambda\ge0$.
- **C.** If $A^T\lambda+c\ne0$, the dual function equals $-\infty$.
- **D.** The nonnegativity restriction on $\lambda$ can be dropped because $x$ is unrestricted.

**21.** For $f(x)=\tfrac12(x_1^2+4x_2^2)$, gradient descent uses a constant step size $\eta=0.6$. Select every correct conclusion.

- **A.** The iterates converge to zero from every starting point because the objective is strictly convex.
- **B.** The update is $x_{k+1}=(0.4x_{1,k},-1.4x_{2,k})^T$.
- **C.** At any starting point with $x_{2,0}\ne0$, the second coordinate changes sign each iteration and grows in magnitude.
- **D.** If $x_{2,0}=0$, the iterates converge to zero.

**22.** Let $f$ be convex and let $X$ be a finitely supported random vector in its convex domain. Select every valid use of convexity.

- **A.** The pointwise maximum of two convex functions is convex.
- **B.** The pointwise minimum of any two convex functions is convex.
- **C.** Jensen's inequality requires independent coordinates of $X$.
- **D.** $f(E[X])\ge E[f(X)]$ for every such convex function and random vector.

**23.** Minimize $x^2$ subject to $-x\le0$ and $-2x\le0$. Select every correct statement at $x^*=0$.

- **A.** $(x^*,\lambda_1,\lambda_2)=(0,1,0)$ satisfies all KKT conditions.
- **B.** Both inequalities are active.
- **C.** The stationarity equation is $2x-\lambda_1-\lambda_2=0$.
- **D.** Both multipliers must be strictly positive.

**24.** An algorithm has a primal feasible point with objective $11.2$ and dual feasible multipliers with dual value $10.9$. Select every justified conclusion.

- **A.** The optimal value must equal the midpoint $11.05$.
- **B.** The distance from the primal point to every minimizer is at most $0.3$.
- **C.** The primal point is at most $0.3$ above the optimal objective value.
- **D.** The optimal primal value belongs to $[10.9,11.2]$.

## 25. Proving the first-order characterization of convexity [10 marks]

**(a) [5 marks]** Let $f$ be differentiable on an open convex domain. Starting with the defining convexity inequality, prove that convexity implies $f(y)\ge f(x)+\nabla f(x)^T(y-x)$ for any $x,y$ in the domain.

**(b) [5 marks]** Conversely, assume the first-order inequality holds for every pair $x,y$. Prove the defining convexity inequality using $z=(1-t)x+ty$, $0<t<1$, as the expansion point.

## 26. Dual concavity, weak duality, and complementary slackness [10 marks]

**(a) [4 marks]** For $L(x,\lambda,\nu)=f_0(x)+\sum_i\lambda_if_i(x)+\sum_j\nu_jh_j(x)$, prove directly that $g(\lambda,\nu)=\inf_x L(x,\lambda,\nu)$ is concave, without imposing convexity on the primal functions. Work with multiplier pairs having finite dual values.

**(b) [3 marks]** For primal feasible $x$ and $\lambda\ge0$, derive $g(\lambda,\nu)\le f_0(x)$ and hence weak duality. Explain the different restrictions on inequality and equality multipliers.

**(c) [3 marks]** Suppose feasible $x^*,\lambda^*,\nu^*$ have finite values and $f_0(x^*)=g(\lambda^*,\nu^*)$. Derive complementary slackness term by term and show that $x^*$ minimizes the Lagrangian.

## 27. Why convex KKT conditions are sufficient [10 marks]

**(a) [4 marks]** Assume $f_0,f_i$ are differentiable convex functions on $\mathbb R^n$, and $h_j$ are affine. Suppose $(x^*,\lambda^*,\nu^*)$ satisfies primal feasibility, $\lambda^*\ge0$, complementary slackness, and stationarity. Prove that $x^*$ globally minimizes $L(\cdot,\lambda^*,\nu^*)$.

**(b) [3 marks]** Use this Lagrangian minimum to prove primal and dual optimality and zero duality gap. State whether a constraint qualification is needed for this sufficiency implication once the displayed KKT point is given.

**(c) [3 marks]** If $f_0$ is strictly convex, prove that the primal minimizer is unique. Identify the role of the convexity of the feasible set.

## 28. Deriving a quadratic gradient-descent step-size bound [10 marks]

**(a) [3 marks]** Let $f(x)=\frac12x^TQx+c^Tx+r$, where $Q$ is symmetric. Derive its gradient and Hessian by expanding $f(x+h)$. State the condition for convexity on $\mathbb R^n$.

**(b) [4 marks]** Assume $0\preceq Q\preceq LI$ with $L>0$, let $g=\nabla f(x)$, and define $x^+=x-\eta g$. Derive an upper bound on $f(x^+)-f(x)$, and give a range of $\eta$ guaranteeing strict decrease whenever $g\ne0$.

**(c) [3 marks]** Now assume $Q\succ0$. Prove convergence of constant-step gradient descent for $0<\eta<2/\lambda_{\max}(Q)$ by diagonalizing $Q$. Give a one-dimensional counterexample at the upper endpoint.

## 29. Capacity planning with an active resource cap [12 marks]

**(a) [4 marks]** A planning model chooses nonnegative production amounts $x,y$ with total $x+y=4$, subject to the capacity cap $x\le2.5$. It minimizes $f(x,y)=(x-5)^2+2(y-2)^2$. Eliminate the equality constraint, determine the feasible interval, and find the unique minimizer and objective value.

**(b) [4 marks]** Write the Lagrangian using multipliers $\alpha,\beta,\lambda\ge0$ for $-x,-y,x-2.5\le0$, respectively, and unrestricted $\nu$ for $x+y-4=0$. Find multipliers at the proposed optimum and give a dual certificate by evaluating the Lagrangian infimum.

**(c) [4 marks]** Before convergence, a solver reports the feasible plan $(x,y)=(2,2)$ and multipliers $(\alpha,\beta,\lambda,\nu)=(0,0,2,2)$. Compute their dual value, a guaranteed interval for $p^*$, and an upper bound on the plan's objective error.

## 30. Choosing a stable learning rate for a quadratic calibration loss [12 marks]

**(a) [4 marks]** A calibration model minimizes $f(u,v)=\tfrac12(2u^2+8v^2)-4u+8v$ on $\mathbb R^2$. Compute the gradient, Hessian, unique optimizer, and minimum value. Explain why a stationary point is sufficient here.

**(b) [4 marks]** From $(u_0,v_0)=(0,0)$, calculate one gradient-descent step and its objective for $\eta=0.2$ and for $\eta=0.3$. Compare each objective to the initial value and to the optimum.

**(c) [4 marks]** Derive the constant-step interval guaranteeing convergence from every start. At the boundary step $\eta=0.25$, determine the behavior from $(0,0)$ and explain why a zero change in objective would not certify convergence.

