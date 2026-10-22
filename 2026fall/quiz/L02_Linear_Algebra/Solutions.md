# Lecture 02: Linear Algebra

## Worked Solutions

**100 marks: 12 True/False × 1; 12 multiple response × 2; 4 proofs/derivations × 10; 2 applications × 12.**

Answer in English. Every multiple-response question has four options and 1–3 correct answers. Exact set: 2 marks; nonempty proper correct subset: 1; any wrong option or no answer: 0. Use `Quiz.tex` to type your responses in its marked regions.

Primary source: [Linear_Algebra.pdf](../../lecture/Linear_Algebra.pdf). Page numbers start at the cover.

## A. True/False

**1.** Under the lecture convention, the gradient of a scalar function of $x\in\mathbb R^n$ is an $n\times1$ column vector.

**True.** The listed partial derivatives are transposed into a column.

*PDF p.16.*

**2.** If $f$ is twice continuously differentiable on an open neighborhood of $x$, then its Hessian at $x$ is symmetric.

**True.** Continuity of the second partial derivatives ensures equality of mixed partial derivatives. The regularity condition makes the symmetry statement precise.

*PDF p.18; regularity clarification.*

**3.** Every pair of eigenvectors of a real symmetric matrix is automatically orthogonal, including pairs with the same eigenvalue.

**False.** Eigenvectors for distinct eigenvalues are orthogonal. Within a repeated eigenspace, vectors may be nonorthogonal, although an orthonormal basis can be chosen; the identity matrix is a counterexample to the unconditional claim.

*PDF p.15; clarification of repeated eigenvalues.*

**4.** A square matrix has an inverse if and only if its determinant is nonzero.

**True.** A zero determinant characterizes singularity; the cofactor inverse is defined when the determinant is nonzero.

*PDF pp.7,9.*

**5.** The correct transpose rule for a product is $(AB)^T=A^TB^T$.

**False.** The order reverses: $(AB)^T=B^TA^T$. The stated right side can even have incompatible dimensions.

*PDF p.6.*

**6.** Every real symmetric positive semidefinite matrix is invertible.

**False.** The zero matrix and a diagonal matrix with diagonal entries 1 and 0 are positive semidefinite but singular.

*PDF pp.12,14.*

**7.** A real $m\times n$ matrix represents a linear map from $\mathbb R^n$ to $\mathbb R^m$.

**True.** Its n columns multiply the n input coordinates, producing m output coordinates.

*PDF p.4.*

**8.** For $x,y\in\mathbb R^3$, the outer product $xy^T$ is a scalar.

**False.** The outer product is $3\times3$; the inner product $x^Ty$ is a scalar.

*PDF p.11.*

**9.** Every invertible real symmetric matrix has only positive eigenvalues.

**False.** Invertibility excludes zero eigenvalues but allows negative ones; for example, the diagonal matrix with entries 1 and -1 is invertible and indefinite.

*PDF pp.12,14-15.*

**10.** If two real vectors have zero inner product, at least one of them must be the zero vector.

**False.** Nonzero perpendicular vectors, such as the two coordinate vectors in the plane, have zero inner product.

*PDF p.11.*

**11.** If $A\in\mathbb R^{2\times4}$ has full rank, then $Ax=0$ has only the zero solution.

**False.** Full rank here means rank 2, not full column rank 4. Rank-nullity gives a two-dimensional nullspace.

*PDF p.8; supplementary consequence from PDF pp.4,8.*

**12.** If both $AB$ and $BA$ are defined and have the same shape, they must be equal.

**False.** Equal shape does not imply equality. For example, $A=\begin{pmatrix}1&0\\0&0\end{pmatrix}$ and $B=\begin{pmatrix}0&1\\0&0\end{pmatrix}$ give $AB=B$ but $BA=0$.

*PDF p.5.*

## B. Multiple Response

**13.** Let $A,B$ be invertible real square matrices of the same size. Select every valid formula.

- **A.** $\det(AB)=\det(A)+\det(B)$. **Incorrect:** The determinant is multiplicative for square matrices, rather than additive across a product.
- **B.** $(A^T)^{-1}=(A^{-1})^T$. **Correct:** Transpose the identities defining the inverse.
- **C.** $(AB)^{-1}=A^{-1}B^{-1}$ for all such matrices. **Incorrect:** The general inverse rule reverses the order. The stated expression works under additional commutation conditions, not in general.
- **D.** $(2A)^{-1}=2A^{-1}$. **Incorrect:** The correct scalar factor is one half.

**Correct set: B.** *PDF pp.7,9.*

**14.** For $x=(-2,1,2)^T$, select every correct norm value.

- **A.** $\|x\|_\infty=3$. **Incorrect:** The largest absolute entry is 2; 3 is the Euclidean norm in this example.
- **B.** $\|x\|_2=3$. **Correct:** The sum of squared entries is 4+1+4=9.
- **C.** $\|x\|_1=5$. **Correct:** The sum of absolute entries is 2+1+2.
- **D.** $\|x\|_1=|-2+1+2|=1$. **Incorrect:** Absolute values must be applied to individual coordinates before summation.

**Correct set: B, C.** *PDF p.10.*

**15.** A Cholesky factorization is given as $C=T^TT$, where $T$ is a nonsingular upper triangular real matrix. Select every correct conclusion.

- **A.** C is positive definite. **Correct:** For nonzero $z$, $z^TCz=\|Tz\|_2^2>0$.
- **B.** The same factor always also satisfies $C=TT^T$. **Incorrect:** For T with rows (1,1) and (0,1), T transpose T differs from T T transpose.
- **C.** The diagonal entry $c_{ii}$ always equals the squared length of row $i$ of $T$. **Incorrect:** In $T^TT$, $c_{ii}$ is the squared length of column $i$ of $T$. Row lengths instead form the diagonal of $TT^T$.
- **D.** $\det(C)=\prod_i t_{ii}$ always holds. **Incorrect:** The product of the diagonal entries is $\det T$; $\det C$ is its square. For $T=2I_2$, the two claimed quantities are 16 and 4.

**Correct set: A.** *PDF pp.7,13; supplementary determinant and column consequences.*

**16.** Consider a proposed eigendecomposition $A=Q\Lambda Q^{-1}$, with diagonal $\Lambda$. Select every correct statement.

- **A.** The columns of Q must be linearly independent. **Correct:** The inverse of Q exists only when its columns form a basis.
- **B.** Normalizing every column of Q to length one is sufficient to replace the inverse by its transpose. **Incorrect:** Unit lengths do not ensure mutual orthogonality.
- **C.** Every real square matrix has such a decomposition with a real invertible Q and a real diagonal Lambda. **Incorrect:** A real matrix can have nonreal eigenvalues or fail to have enough independent eigenvectors.
- **D.** A real symmetric matrix permits an orthogonal choice of Q and real diagonal entries in the decomposition. **Correct:** The spectral theorem supplies an orthonormal eigenbasis.

**Correct set: A, D.** *PDF pp.14-15.*

**17.** For fixed $A\in\mathbb R^{m\times n}$, let $f(u,v)=u^TAv$, with $u\in\mathbb R^m$ and $v\in\mathbb R^n$. Select every correct statement.

- **A.** When $v$ is fixed, $\nabla_u f=Av$. **Correct:** The coefficient of the differential du is Av.
- **B.** When $u$ is fixed, $\nabla_v f=A^Tu$. **Correct:** Write the scalar as v transpose A transpose u and differentiate.
- **C.** When $v$ is fixed, the Hessian with respect to $u$ is the zero $m\times m$ matrix. **Correct:** The function is linear in u, so its gradient does not depend on u.
- **D.** When $u$ is fixed, $\nabla_v f=Au$ regardless of dimensions. **Incorrect:** The transpose is required, and Au may not even be defined.

**Correct set: A, B, C.** *PDF pp.16-18.*

**18.** Let $Q\in\mathbb R^{n\times n}$ satisfy $Q^TQ=I$. Select every statement that holds for all real $x,y\in\mathbb R^n$.

- **A.** If x and y are nonzero, their angle is preserved by Q. **Correct:** The inner product and both Euclidean lengths are preserved, so the cosine of the angle is preserved.
- **B.** $\|Qx\|_1=\|x\|_1$. **Incorrect:** A rotation can turn (1,0) into (1/sqrt(2),1/sqrt(2)), changing its 1-norm.
- **C.** $(Qx)^T(Qy)=x^Ty$. **Correct:** Insert Q transpose Q between x transpose and y.
- **D.** $\|Qx-Qy\|_2=\|x-y\|_2$. **Correct:** The squared distance is preserved by the same inner-product identity.

**Correct set: A, C, D.** *PDF pp.6,10-11; supplementary consequence.*

**19.** Let $A\in\mathbb R^{m\times n}$ and $B\in\mathbb R^{n\times m}$. Select every correct trace identity.

- **A.** $\operatorname{tr}(A^TA)=\sum_{i=1}^m\sum_{j=1}^n a_{ij}^2$. **Correct:** The diagonal entry indexed by j is the squared Euclidean norm of column j.
- **B.** For square $C$, $\operatorname{tr}(C^T)=\operatorname{tr}(C)$. **Correct:** Transposition leaves every diagonal entry unchanged.
- **C.** $\operatorname{tr}(AB)=\operatorname{tr}(BA)$. **Correct:** Both equal $\sum_{i=1}^m\sum_{j=1}^n a_{ij}b_{ji}$, even when the square products have different sizes.
- **D.** When $A,B$ are square, $\operatorname{tr}(AB)=\operatorname{tr}(A)\operatorname{tr}(B)$. **Incorrect:** For two 2 by 2 identity matrices the left side is 2 and the right side is 4.

**Correct set: A, B, C.** *Supplementary derivation from PDF pp.2,5-6.*

**20.** Let $C$ be a real symmetric positive definite matrix and $g(C)=\log\det C$. Matrix gradients use $dg=\operatorname{tr}((\nabla_Cg)^T\,dC)$. Select every correct statement.

- **A.** The real logarithm of the determinant is defined for every invertible real matrix. **Incorrect:** An invertible matrix can have a negative determinant, whose real logarithm is undefined.
- **B.** For a symmetric perturbation $H$, the directional derivative is $\operatorname{tr}(C^{-1}H)$. **Correct:** Substitute H for dC in the differential.
- **C.** For positive scalar $c$, if $C=cI_n$, then $g(C)=n\log c$. **Correct:** The determinant is c to the nth power.
- **D.** $\nabla_C g=C^{-1}$ at such a matrix. **Correct:** The general inverse-transpose expression equals the inverse for symmetric C.

**Correct set: B, C, D.** *PDF pp.7,12,17; supplementary differential interpretation.*

**21.** Let $A=\begin{pmatrix}1&2&0\\-1&0&3\end{pmatrix}$, with columns $a_1,a_2,a_3$, and $x=(2,-1,1)^T$. Select every correct statement.

- **A.** $Ax=2a_1-a_2+a_3$. **Correct:** Matrix-vector multiplication weights the columns by the coordinates of x.
- **B.** Every vector $Ax$, as $x$ varies, lies in the span of the columns of $A$. **Correct:** The column expansion proves membership in that span.
- **C.** $Ax=(0,1)^T$. **Correct:** The first row gives 2-2=0; the second gives -2+3=1.
- **D.** $A^Tx$ is defined for this $x$. **Incorrect:** A transpose is 3 by 2 and requires a two-dimensional input.

**Correct set: A, B, C.** *PDF pp.4-6.*

**22.** Let $f(x_1,x_2)=x_1^2x_2+3x_2^2$. Select every correct statement.

- **A.** $\nabla f(1,1)=(2,7)^T$. **Correct:** The partial derivatives are $2x_1x_2$ and $x_1^2+6x_2$.
- **B.** $\nabla^2f(1,0)=\begin{pmatrix}0&2\\2&6\end{pmatrix}$ is indefinite. **Correct:** Its determinant is -4; directly its form is positive at (0,1) and negative at (2,-1).
- **C.** The Hessian is constant because f is a polynomial. **Incorrect:** The general Hessian has entries $2x_2,2x_1,2x_1,6$, so it depends on $x$.
- **D.** $\nabla^2f(1,1)=\begin{pmatrix}2&2\\2&6\end{pmatrix}$ is positive definite. **Correct:** Its quadratic form is 2(a+b) squared plus 4 b squared, positive away from zero.

**Correct set: A, B, D.** *PDF pp.12,16-18; supplementary worked example.*

**23.** Let $A,B$ be real symmetric PSD matrices of the same size. Select every statement that always holds.

- **A.** $x^TABx\geq0$ for every real vector $x$. **Incorrect:** Take $A=\operatorname{diag}(1,0)$, $B=\begin{pmatrix}1&2\\2&4\end{pmatrix}$, and $x=(1,-1)^T$. Both matrices are PSD, but the quadratic value is -1.
- **B.** A+B is PSD. **Correct:** Its quadratic form is the sum of two nonnegative quadratic forms.
- **C.** AB is symmetric. **Incorrect:** The transpose of AB is BA, and PSD matrices need not commute.
- **D.** For every real matrix $R$ with compatible dimensions, $R^TAR$ is PSD. **Correct:** It is symmetric and $z^TR^TARz=(Rz)^TA(Rz)\geq0$.

**Correct set: B, D.** *PDF pp.6,12; supplementary consequences.*

**24.** Let $x,y\in\mathbb R^n$ both be nonzero. Select every correct statement about outer products.

- **A.** $xy^T=yx^T$ for all such $x,y$. **Incorrect:** For distinct coordinate vectors these matrices have their single nonzero entry in different positions.
- **B.** $xy^T$ has rank one. **Correct:** Every column is a multiple of x and at least one column is nonzero.
- **C.** $xx^T$ is symmetric positive semidefinite. **Correct:** Its transpose is itself, and $z^Txx^Tz=(x^Tz)^2\geq0$.
- **D.** $\operatorname{tr}(xy^T)=x^Ty$. **Correct:** Sum the diagonal entries $x_i y_i$.

**Correct set: B, C, D.** *PDF pp.2,8,11-12; supplementary consequences.*

## 25. The nullspace and definiteness of a Gram matrix [10 marks]

**(a) [3 marks]** For any real $A\in\mathbb R^{m\times n}$, prove $\operatorname{null}(A^TA)=\operatorname{null}(A)$. Your proof must establish both inclusions without assuming $A$ is square.

**Worked solution:** If $Ax=0$, then $A^TAx=A^T0=0$, proving one inclusion. Conversely, if $A^TAx=0$, left-multiply by $x^T$ to get 
$$
0=x^TA^TAx=(Ax)^T(Ax)=\|Ax\|_2^2.
$$
 A sum of squares is zero only when every coordinate vanishes, so $Ax=0$. This gives the other inclusion for any rectangular shape. Award one mark for the first inclusion and two for the norm argument in the second.

**(b) [4 marks]** Use the result to prove that $A^TA$ is PSD, that its rank equals the rank of $A$, and that it is PD if and only if $A$ has full column rank. Explain the case $m<n$.

**Worked solution:** The matrix is symmetric because $(A^TA)^T=A^TA$, and $x^TA^TAx=\|Ax\|_2^2\geq0$, so it is PSD. Both maps have domain $\mathbb R^n$ and the same nullspace. Rank-nullity therefore gives $\operatorname{rank}(A^TA)=n-\dim\operatorname{null}(A)=\operatorname{rank}(A)$. Its quadratic form is strictly positive for every nonzero x exactly when $Ax=0$ has no nonzero solution, equivalently rank A=n. If m<n, rank A is at most m<n; hence the Gram matrix is necessarily singular and cannot be PD, even if A has full rank in the rectangular sense. Award one mark each for PSD, rank equality, the PD equivalence, and the wide-matrix case.

**(c) [3 marks]** For $\mu>0$, prove $A^TA+\mu I_n$ is PD for every $A$. Give a lower bound on its quadratic form and explain why its inverse exists.

**Worked solution:** For every nonzero x, 
$$
x^T(A^TA+\mu I_n)x=\|Ax\|_2^2+\mu\|x\|_2^2\geq\mu\|x\|_2^2>0.
$$
 The matrix is symmetric, so it is PD. If it had a nonzero null vector, its quadratic form there would be zero, contradicting this bound. Thus its nullspace is trivial and, being square, it is invertible. Award one mark for the expansion, one for the strict bound, and one for invertibility.

*Source: PDF pp.8,12-13; supplementary full proof.*

## 26. Differentiate a nonsymmetric quadratic and a bilinear form [10 marks]

**(a) [4 marks]** Let $A\in\mathbb R^{n\times n}$ be fixed, with no symmetry assumption, and $f(x)=x^TAx$. Expand $f(x+h)-f(x)$ and derive its gradient and Hessian. Explain precisely why the formula $2Ax$ need not be correct.

**Worked solution:** The exact expansion is 
$$
f(x+h)-f(x)=h^TAx+x^TAh+h^TAh=((A+A^T)x)^Th+h^TAh.
$$
 The last term is quadratic in h and is the higher-order remainder. Thus $df=((A+A^T)x)^Tdx$, giving $\nabla f=(A+A^T)x$ and $\nabla^2 f=A+A^T$. The expression 2Ax agrees for all x if and only if A is symmetric; otherwise one must account for both appearances of x in the quadratic. Award one mark for expansion, one for identifying the linear differential, and one each for the gradient and Hessian with the symmetry qualification.

**(b) [3 marks]** Decompose $A=S+K$, where $S=(A+A^T)/2$ and $K=(A-A^T)/2$. Prove $x^TKx=0$, and show that knowledge of $x^TAx$ for every real $x$ cannot identify $K$.

**Worked solution:** K is skew-symmetric. The scalar $s=x^TKx$ equals its transpose, which is $x^TK^Tx=-x^TKx=-s$; hence s=0 over the real numbers. Therefore $x^TAx=x^TSx$ for all x. Adding any skew-symmetric matrix to A changes K but leaves every quadratic-form value unchanged, so those values cannot identify K. Award one mark for skew symmetry, one for the scalar-transpose proof, and one for the identification conclusion.

**(c) [3 marks]** For fixed $B\in\mathbb R^{m\times n}$, derive the first differential of $g(u,v)=u^TBv$ and both partial gradients. Then state the derivative along differentiable paths $u(t),v(t)$.

**Worked solution:** Expanding the perturbed bilinear form gives 
$$
dg=(du)^TBv+u^TB(dv)=(Bv)^Tdu+(B^Tu)^Tdv.
$$
 The product $(du)^TB(dv)$ is second order and does not enter the first differential. Thus $\nabla_u g=Bv$ and $\nabla_v g=B^Tu$. Along paths, both arguments vary and the chain rule gives 
$$
\frac{d}{dt}g(u(t),v(t))=u'(t)^TBv(t)+u(t)^TBv'(t).
$$
 Award one mark for the differential, one for both gradients, and one for the two-term path derivative.

*Source: PDF pp.16-18; supplementary derivation.*

## 27. Orthogonal eigenspaces and quadratic-form bounds [10 marks]

**(a) [3 marks]** Let $A=A^T$, $Au=\alpha u$, and $Av=\beta v$, with nonzero eigenvectors and $\alpha\neq\beta$. Prove $u^Tv=0$. Explain what must be changed when the eigenvalues are equal.

**Worked solution:** Symmetry yields 
$$
\alpha u^Tv=(Au)^Tv=u^TA^Tv=u^TAv=\beta u^Tv.
$$
 Hence $(\alpha-\beta)u^Tv=0$, and distinct eigenvalues imply orthogonality. When the eigenvalues coincide, this equation imposes no orthogonality condition; for A=I any nonzero vector is an eigenvector. One can choose an orthonormal basis within each repeated eigenspace, producing the orthogonal Q in the spectral theorem. Award two marks for the equality and conclusion, and one for the repeated-eigenvalue qualification.

**(b) [4 marks]** Using the spectral theorem for real symmetric matrices, prove that $A$ is PSD if and only if all its eigenvalues are nonnegative, and PD if and only if all are positive. Also establish the relation between rank and nonzero eigenvalues.

**Worked solution:** Write $A=Q\Lambda Q^T$ with Q orthogonal, and put $z=Q^Tx$. Then 
$$
x^TAx=z^T\Lambda z=\sum_i\lambda_i z_i^2.
$$
 If all eigenvalues are nonnegative this is nonnegative, proving PSD; if all are positive and x is nonzero then z is nonzero, so the sum is strictly positive, proving PD. Conversely, using a unit eigenvector $q_i$ gives $q_i^TAq_i=\lambda_i$, forcing nonnegative or strictly positive eigenvalues under PSD or PD respectively. Multiplication by invertible Q and Q transpose preserves rank, so rank A=rank Lambda, the number of nonzero diagonal eigenvalues counted with multiplicity. Award one mark for the diagonal quadratic form, one for sufficiency, one for necessity, and one for rank.

**(c) [3 marks]** For nonzero $x$, derive the Rayleigh quotient bounds $\lambda_{\min}\leq x^TAx/(x^Tx)\leq\lambda_{\max}$. Characterize equality at each endpoint.

**Worked solution:** Orthogonality gives $x^Tx=z^Tz$, so 
$$
\frac{x^TAx}{x^Tx}=\sum_i\lambda_i\frac{z_i^2}{\sum_j z_j^2}.
$$
 The weights are nonnegative and sum to one, making this a weighted average of the eigenvalues and proving the bounds. Equality with the smallest eigenvalue holds exactly when all nonzero z coordinates belong to that eigenspace; equivalently x lies in the minimum-eigenvalue eigenspace. The analogous statement holds at the maximum. These conditions also cover repeated extremes and scalar multiples of the identity. Award one mark for the weighted average, one for the bounds, and one for the endpoint characterization.

*Source: PDF pp.12,14-15; supplementary proof.*

## 28. Build an orthogonal projector from an orthonormal basis [10 marks]

**(a) [3 marks]** Let $Q\in\mathbb R^{m\times r}$ have orthonormal columns, with $1\leq r\leq m$. Define $P=QQ^T$. Prove $P^T=P$, $P^2=P$, and $Pz=z$ for every $z\in\operatorname{col}(Q)$.

**Worked solution:** Transposition gives $P^T=(QQ^T)^T=QQ^T=P$. Orthonormality means $Q^TQ=I_r$, so $P^2=Q(Q^TQ)Q^T=QQ^T=P$. If $z=Qc$, then $Pz=QQ^TQc=Qc=z$. Each identity follows from the stated shapes and does not require the rectangular Q to have a two-sided inverse. Award one mark for each identity.

**(b) [4 marks]** For an arbitrary $y\in\mathbb R^m$, show that $y=Py+(I-P)y$ is a decomposition into a vector in $\operatorname{col}(Q)$ and a vector orthogonal to that space. Derive a Pythagorean norm identity.

**Worked solution:** The sum equals y by direct cancellation, and $Py=Q(Q^Ty)$ is in the column space. Let $r_y=(I-P)y$. Then 
$$
Q^Tr_y=Q^Ty-Q^TQQ^Ty=0,
$$
 so the residual is orthogonal to every vector Qc in the space, including Py. Expanding the squared norm and using the zero cross term yields 
$$
\|y\|_2^2=\|Py\|_2^2+\|(I-P)y\|_2^2.
$$
 Award one mark each for the sum/membership, residual orthogonality, the zero cross term, and the norm identity.

**(c) [3 marks]** Prove that $Py$ is the unique nearest vector to $y$ in $\operatorname{col}(Q)$. Then prove $\|Py\|_2\leq\|y\|_2$ and give its equality condition.

**Worked solution:** For any z in the column space, write $y-z=(I-P)y+(Py-z)$. The summands are orthogonal, hence 
$$
\|y-z\|_2^2=\|(I-P)y\|_2^2+\|Py-z\|_2^2.
$$
 The minimum is attained exactly at z=Py, so the nearest vector is unique. The Pythagorean identity from the previous part gives $\|Py\|_2\leq\|y\|_2$, with equality exactly when $(I-P)y=0$, equivalently y lies in the column space. Award one mark for the distance identity, one for uniqueness, and one for the norm bound and equality condition.

*Source: Supplementary derivation from PDF pp.4,6,10-11.*

## 29. A rectangular sensor map: rank, Cholesky, and residual geometry [12 marks]

**(a) [3 marks]** A sensor model is $Az$, where $A=\begin{pmatrix}1&0\\1&1\\0&1\end{pmatrix}$, and the observed vector is $b=(2,0,1)^T$. Compute $G=A^TA$ and $A^Tb$, establish the column rank of $A$, and decide whether $G$ is PD.

**Worked solution:** Direct multiplication gives 
$$
G=\begin{pmatrix}2&1\\1&2\end{pmatrix},\qquad A^Tb=\begin{pmatrix}2\\1\end{pmatrix}.
$$
 The two columns (1,1,0) and (0,1,1) are independent: their first and third coordinates force both coefficients of a zero linear combination to vanish. Thus rank A=2, its full column rank. G is PD by the Gram result; directly its quadratic form is $(z_1+z_2)^2+z_1^2+z_2^2>0$ for nonzero z. Award one mark for both products, one for column independence, and one for PD.

**(b) [3 marks]** Find an upper triangular $T$ with positive diagonal such that $G=T^TT$, and verify the product.

**Worked solution:** Write $T=\begin{pmatrix}a&c\\0&d\end{pmatrix}$. Matching entries requires $a^2=2$, $ac=1$, and $c^2+d^2=2$. Positive diagonal entries give 
$$
T=\begin{pmatrix}\sqrt2&1/\sqrt2\\0&\sqrt{3/2}\end{pmatrix}.
$$
 The resulting product has entries 2,1,1, and $1/2+3/2=2$, matching G. Award one mark for the matching equations, one for T, and one for verification.

**(c) [4 marks]** Find $z_*$ by solving $Gz_*=A^Tb$. Compute $r=b-Az_*$, verify $A^Tr=0$, and use a squared-distance expansion to show that this solution gives the unique best least-squares fit.

**Worked solution:** The equations are $2z_1+z_2=2$ and $z_1+2z_2=1$, yielding $z_*=(1,0)^T$. Its fitted vector is $(1,1,0)^T$, and $r=(1,-1,1)^T$. Then $A^Tr=(1-1,-1+1)^T=0$. For any perturbation d, 
$$
\|b-A(z_*+d)\|_2^2=\|r-Ad\|_2^2=3+\|Ad\|_2^2,
$$
 because the cross term vanishes. Full column rank means $Ad=0$ only when d=0, establishing the unique minimizer and minimum squared error 3. Award one mark each for z, residual/orthogonality, the expansion, and uniqueness.

**(d) [2 marks]** Find the eigenvalues of $G$ and an orthonormal eigenbasis. Express $\|Ad\|_2^2$ using the coordinates of $d$ in that basis.

**Worked solution:** The normalized vectors $q_+=(1,1)^T/\sqrt2$ and $q_-=(1,-1)^T/\sqrt2$ have eigenvalues 3 and 1. If $d=\alpha q_++\beta q_-$, then $\|Ad\|_2^2=d^TGd=3\alpha^2+\beta^2$. Thus equal-sized coefficient changes along the first direction create three times the squared sensor-output change. Award one mark for the eigenpairs and one for the expression.

*Source: PDF pp.4,8-9,11-15; supplementary least-squares application.*

## 30. A nonsymmetric representation of a quadratic objective [12 marks]

**(a) [3 marks]** Let $f(x)=\tfrac12x^TBx-c^Tx$, where $B=\begin{pmatrix}4&5\\-1&6\end{pmatrix}$, $c=(6,8)^T$, and $x\in\mathbb R^2$. Compute its gradient and Hessian. Identify the symmetric matrix governing its quadratic part.

**Worked solution:** Its symmetric part is 
$$
S=(B+B^T)/2=\begin{pmatrix}4&2\\2&6\end{pmatrix}.
$$
 Because the skew part contributes zero to a quadratic form, $f(x)=\tfrac12x^TSx-c^Tx$. Differentiating gives $\nabla f(x)=Sx-c$ and $\nabla^2f(x)=S$. Using Bx-c would be incorrect because B is not symmetric. Award one mark each for S, the gradient, and the Hessian.

**(b) [3 marks]** Find the eigenvalues of the Hessian and decide whether it is PD, PSD but not PD, or indefinite. Give a quadratic-form verification of strict positivity as an independent check.

**Worked solution:** The characteristic polynomial is 
$$
(4-\lambda)(6-\lambda)-4=\lambda^2-10\lambda+20,
$$
 with roots $5-\sqrt5$ and $5+\sqrt5$, both positive. The Hessian is PD. Independently, for $u=(u_1,u_2)^T$, 
$$
u^TSu=4u_1^2+4u_1u_2+6u_2^2=4(u_1+u_2/2)^2+5u_2^2,
$$
 which is strictly positive for every nonzero u. Award one mark for the eigenvalues, one for the classification, and one for the completed-square check.

**(c) [3 marks]** Solve for the stationary point, compute its objective value, and prove that it is the unique global minimizer.

**Worked solution:** Solving $Sx=c$ gives $4x_1+2x_2=6$ and $2x_1+6x_2=8$, hence $x_*=(1,1)^T$. Its value is $f(x_*)=7-14=-7$. Using $Sx_*=c$, an exact expansion gives 
$$
f(x)-f(x_*)=\tfrac12(x-x_*)^TS(x-x_*).
$$
 Positive definiteness makes this quantity positive for every $x\ne x_*$, proving the unique global minimum. Award one mark for the point, one for its value, and one for the expansion and uniqueness.

**(d) [3 marks]** Start at $x_0=0$ and take one gradient step $x_1=x_0-\eta\nabla f(x_0)$, with $\eta>0$. Find the complete range of step sizes that strictly decreases the objective on this first step. Also find the best step size along this direction.

**Worked solution:** At zero the gradient is -c, so $x_1=\eta c=(6\eta,8\eta)^T$. Since $c^Tc=100$ and $c^TSc=720$, 
$$
f(x_1)=360\eta^2-100\eta.
$$
 As f(0)=0, strict decrease holds exactly when $0<\eta<100/360=5/18$. Differentiating this scalar quadratic gives the best step $\eta=100/720=5/36$, giving $x_1=(5/6,10/9)^T$ and value $-125/18$. This is a one-step calculation along the specified direction. Award one mark for the quadratic expression, one for the strict interval, and one for the optimal step.

*Source: PDF pp.12,14-18; supplementary quadratic-optimization application.*

