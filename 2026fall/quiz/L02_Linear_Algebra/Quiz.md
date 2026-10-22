# Lecture 02: Linear Algebra

## Practice Quiz

**100 marks: 12 True/False × 1; 12 multiple response × 2; 4 proofs/derivations × 10; 2 applications × 12.**

Answer in English. Every multiple-response question has four options and 1–3 correct answers. Exact set: 2 marks; nonempty proper correct subset: 1; any wrong option or no answer: 0. Use `Quiz.tex` to type your responses in its marked regions.

Primary source: [Linear_Algebra.pdf](../../lecture/Linear_Algebra.pdf). Page numbers start at the cover.

## A. True/False

**1.** Under the lecture convention, the gradient of a scalar function of $x\in\mathbb R^n$ is an $n\times1$ column vector.

**2.** If $f$ is twice continuously differentiable on an open neighborhood of $x$, then its Hessian at $x$ is symmetric.

**3.** Every pair of eigenvectors of a real symmetric matrix is automatically orthogonal, including pairs with the same eigenvalue.

**4.** A square matrix has an inverse if and only if its determinant is nonzero.

**5.** The correct transpose rule for a product is $(AB)^T=A^TB^T$.

**6.** Every real symmetric positive semidefinite matrix is invertible.

**7.** A real $m\times n$ matrix represents a linear map from $\mathbb R^n$ to $\mathbb R^m$.

**8.** For $x,y\in\mathbb R^3$, the outer product $xy^T$ is a scalar.

**9.** Every invertible real symmetric matrix has only positive eigenvalues.

**10.** If two real vectors have zero inner product, at least one of them must be the zero vector.

**11.** If $A\in\mathbb R^{2\times4}$ has full rank, then $Ax=0$ has only the zero solution.

**12.** If both $AB$ and $BA$ are defined and have the same shape, they must be equal.

## B. Multiple Response

**13.** Let $A,B$ be invertible real square matrices of the same size. Select every valid formula.

- **A.** $\det(AB)=\det(A)+\det(B)$.
- **B.** $(A^T)^{-1}=(A^{-1})^T$.
- **C.** $(AB)^{-1}=A^{-1}B^{-1}$ for all such matrices.
- **D.** $(2A)^{-1}=2A^{-1}$.

**14.** For $x=(-2,1,2)^T$, select every correct norm value.

- **A.** $\|x\|_\infty=3$.
- **B.** $\|x\|_2=3$.
- **C.** $\|x\|_1=5$.
- **D.** $\|x\|_1=|-2+1+2|=1$.

**15.** A Cholesky factorization is given as $C=T^TT$, where $T$ is a nonsingular upper triangular real matrix. Select every correct conclusion.

- **A.** C is positive definite.
- **B.** The same factor always also satisfies $C=TT^T$.
- **C.** The diagonal entry $c_{ii}$ always equals the squared length of row $i$ of $T$.
- **D.** $\det(C)=\prod_i t_{ii}$ always holds.

**16.** Consider a proposed eigendecomposition $A=Q\Lambda Q^{-1}$, with diagonal $\Lambda$. Select every correct statement.

- **A.** The columns of Q must be linearly independent.
- **B.** Normalizing every column of Q to length one is sufficient to replace the inverse by its transpose.
- **C.** Every real square matrix has such a decomposition with a real invertible Q and a real diagonal Lambda.
- **D.** A real symmetric matrix permits an orthogonal choice of Q and real diagonal entries in the decomposition.

**17.** For fixed $A\in\mathbb R^{m\times n}$, let $f(u,v)=u^TAv$, with $u\in\mathbb R^m$ and $v\in\mathbb R^n$. Select every correct statement.

- **A.** When $v$ is fixed, $\nabla_u f=Av$.
- **B.** When $u$ is fixed, $\nabla_v f=A^Tu$.
- **C.** When $v$ is fixed, the Hessian with respect to $u$ is the zero $m\times m$ matrix.
- **D.** When $u$ is fixed, $\nabla_v f=Au$ regardless of dimensions.

**18.** Let $Q\in\mathbb R^{n\times n}$ satisfy $Q^TQ=I$. Select every statement that holds for all real $x,y\in\mathbb R^n$.

- **A.** If x and y are nonzero, their angle is preserved by Q.
- **B.** $\|Qx\|_1=\|x\|_1$.
- **C.** $(Qx)^T(Qy)=x^Ty$.
- **D.** $\|Qx-Qy\|_2=\|x-y\|_2$.

**19.** Let $A\in\mathbb R^{m\times n}$ and $B\in\mathbb R^{n\times m}$. Select every correct trace identity.

- **A.** $\operatorname{tr}(A^TA)=\sum_{i=1}^m\sum_{j=1}^n a_{ij}^2$.
- **B.** For square $C$, $\operatorname{tr}(C^T)=\operatorname{tr}(C)$.
- **C.** $\operatorname{tr}(AB)=\operatorname{tr}(BA)$.
- **D.** When $A,B$ are square, $\operatorname{tr}(AB)=\operatorname{tr}(A)\operatorname{tr}(B)$.

**20.** Let $C$ be a real symmetric positive definite matrix and $g(C)=\log\det C$. Matrix gradients use $dg=\operatorname{tr}((\nabla_Cg)^T\,dC)$. Select every correct statement.

- **A.** The real logarithm of the determinant is defined for every invertible real matrix.
- **B.** For a symmetric perturbation $H$, the directional derivative is $\operatorname{tr}(C^{-1}H)$.
- **C.** For positive scalar $c$, if $C=cI_n$, then $g(C)=n\log c$.
- **D.** $\nabla_C g=C^{-1}$ at such a matrix.

**21.** Let $A=\begin{pmatrix}1&2&0\\-1&0&3\end{pmatrix}$, with columns $a_1,a_2,a_3$, and $x=(2,-1,1)^T$. Select every correct statement.

- **A.** $Ax=2a_1-a_2+a_3$.
- **B.** Every vector $Ax$, as $x$ varies, lies in the span of the columns of $A$.
- **C.** $Ax=(0,1)^T$.
- **D.** $A^Tx$ is defined for this $x$.

**22.** Let $f(x_1,x_2)=x_1^2x_2+3x_2^2$. Select every correct statement.

- **A.** $\nabla f(1,1)=(2,7)^T$.
- **B.** $\nabla^2f(1,0)=\begin{pmatrix}0&2\\2&6\end{pmatrix}$ is indefinite.
- **C.** The Hessian is constant because f is a polynomial.
- **D.** $\nabla^2f(1,1)=\begin{pmatrix}2&2\\2&6\end{pmatrix}$ is positive definite.

**23.** Let $A,B$ be real symmetric PSD matrices of the same size. Select every statement that always holds.

- **A.** $x^TABx\geq0$ for every real vector $x$.
- **B.** A+B is PSD.
- **C.** AB is symmetric.
- **D.** For every real matrix $R$ with compatible dimensions, $R^TAR$ is PSD.

**24.** Let $x,y\in\mathbb R^n$ both be nonzero. Select every correct statement about outer products.

- **A.** $xy^T=yx^T$ for all such $x,y$.
- **B.** $xy^T$ has rank one.
- **C.** $xx^T$ is symmetric positive semidefinite.
- **D.** $\operatorname{tr}(xy^T)=x^Ty$.

## 25. The nullspace and definiteness of a Gram matrix [10 marks]

**(a) [3 marks]** For any real $A\in\mathbb R^{m\times n}$, prove $\operatorname{null}(A^TA)=\operatorname{null}(A)$. Your proof must establish both inclusions without assuming $A$ is square.

**(b) [4 marks]** Use the result to prove that $A^TA$ is PSD, that its rank equals the rank of $A$, and that it is PD if and only if $A$ has full column rank. Explain the case $m<n$.

**(c) [3 marks]** For $\mu>0$, prove $A^TA+\mu I_n$ is PD for every $A$. Give a lower bound on its quadratic form and explain why its inverse exists.

## 26. Differentiate a nonsymmetric quadratic and a bilinear form [10 marks]

**(a) [4 marks]** Let $A\in\mathbb R^{n\times n}$ be fixed, with no symmetry assumption, and $f(x)=x^TAx$. Expand $f(x+h)-f(x)$ and derive its gradient and Hessian. Explain precisely why the formula $2Ax$ need not be correct.

**(b) [3 marks]** Decompose $A=S+K$, where $S=(A+A^T)/2$ and $K=(A-A^T)/2$. Prove $x^TKx=0$, and show that knowledge of $x^TAx$ for every real $x$ cannot identify $K$.

**(c) [3 marks]** For fixed $B\in\mathbb R^{m\times n}$, derive the first differential of $g(u,v)=u^TBv$ and both partial gradients. Then state the derivative along differentiable paths $u(t),v(t)$.

## 27. Orthogonal eigenspaces and quadratic-form bounds [10 marks]

**(a) [3 marks]** Let $A=A^T$, $Au=\alpha u$, and $Av=\beta v$, with nonzero eigenvectors and $\alpha\neq\beta$. Prove $u^Tv=0$. Explain what must be changed when the eigenvalues are equal.

**(b) [4 marks]** Using the spectral theorem for real symmetric matrices, prove that $A$ is PSD if and only if all its eigenvalues are nonnegative, and PD if and only if all are positive. Also establish the relation between rank and nonzero eigenvalues.

**(c) [3 marks]** For nonzero $x$, derive the Rayleigh quotient bounds $\lambda_{\min}\leq x^TAx/(x^Tx)\leq\lambda_{\max}$. Characterize equality at each endpoint.

## 28. Build an orthogonal projector from an orthonormal basis [10 marks]

**(a) [3 marks]** Let $Q\in\mathbb R^{m\times r}$ have orthonormal columns, with $1\leq r\leq m$. Define $P=QQ^T$. Prove $P^T=P$, $P^2=P$, and $Pz=z$ for every $z\in\operatorname{col}(Q)$.

**(b) [4 marks]** For an arbitrary $y\in\mathbb R^m$, show that $y=Py+(I-P)y$ is a decomposition into a vector in $\operatorname{col}(Q)$ and a vector orthogonal to that space. Derive a Pythagorean norm identity.

**(c) [3 marks]** Prove that $Py$ is the unique nearest vector to $y$ in $\operatorname{col}(Q)$. Then prove $\|Py\|_2\leq\|y\|_2$ and give its equality condition.

## 29. A rectangular sensor map: rank, Cholesky, and residual geometry [12 marks]

**(a) [3 marks]** A sensor model is $Az$, where $A=\begin{pmatrix}1&0\\1&1\\0&1\end{pmatrix}$, and the observed vector is $b=(2,0,1)^T$. Compute $G=A^TA$ and $A^Tb$, establish the column rank of $A$, and decide whether $G$ is PD.

**(b) [3 marks]** Find an upper triangular $T$ with positive diagonal such that $G=T^TT$, and verify the product.

**(c) [4 marks]** Find $z_*$ by solving $Gz_*=A^Tb$. Compute $r=b-Az_*$, verify $A^Tr=0$, and use a squared-distance expansion to show that this solution gives the unique best least-squares fit.

**(d) [2 marks]** Find the eigenvalues of $G$ and an orthonormal eigenbasis. Express $\|Ad\|_2^2$ using the coordinates of $d$ in that basis.

## 30. A nonsymmetric representation of a quadratic objective [12 marks]

**(a) [3 marks]** Let $f(x)=\tfrac12x^TBx-c^Tx$, where $B=\begin{pmatrix}4&5\\-1&6\end{pmatrix}$, $c=(6,8)^T$, and $x\in\mathbb R^2$. Compute its gradient and Hessian. Identify the symmetric matrix governing its quadratic part.

**(b) [3 marks]** Find the eigenvalues of the Hessian and decide whether it is PD, PSD but not PD, or indefinite. Give a quadratic-form verification of strict positivity as an independent check.

**(c) [3 marks]** Solve for the stationary point, compute its objective value, and prove that it is the unique global minimizer.

**(d) [3 marks]** Start at $x_0=0$ and take one gradient step $x_1=x_0-\eta\nabla f(x_0)$, with $\eta>0$. Find the complete range of step sizes that strictly decreases the objective on this first step. Also find the best step size along this direction.

