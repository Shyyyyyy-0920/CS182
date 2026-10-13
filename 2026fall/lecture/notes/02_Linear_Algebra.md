# 02 · Mathematical Foundations: Linear Algebra（线性代数基础）

> 主来源：[Linear_Algebra.pdf](../Linear_Algebra.pdf)，页码从封面算起。带 **【补充理解】** 的例子和推导用于解释课件，没有改变课程记号。

## 0. 这节课到底在解决什么问题？

机器学习常把一个样本写成特征向量 \(x\)，把许多样本放进矩阵。模型要对它们做变换，损失函数要衡量预测差距，训练则要改变参数。矩阵乘法、范数、梯度和特征值分别回答“如何变换”“差多少”“往哪改”“哪些方向重要”。例如 [Introduction](01_Introduction.md) 的正规方程 \(\Phi^\mathsf T\Phi w=\Phi^\mathsf T y\) 几乎把本讲工具连在一起。

本讲目标是能检查每个矩阵式的维度、把 \(Ax\) 看成列向量组合、用 \(x^\mathsf T A x\) 判断曲率，并亲手算一个小模型的梯度。

## 1. 前置知识与统一记号

只需熟悉实数、求和、函数导数。下文默认列向量：\(x\in\mathbb R^n\)，\(A\in\mathbb R^{m\times n}\)，所以 \(Ax\in\mathbb R^m\)。上标 \(\mathsf T\) 表示 transpose（转置），不是样本编号。若一个式子的内侧维度不相等，例如 \((m\times n)(p\times1)\) 且 \(n\ne p\)，乘法就未定义。

## 2. 核心直觉：矩阵是变换，也是“列向量仓库”

课件将矩阵写为 \(A=[a_1\;a_2\;\cdots\;a_n]\)，其中每列 \(a_j\in\mathbb R^m\)。于是（PDF p.2–5）

\[
Ax=\sum_{j=1}^n x_j a_j,
\quad (Ax)_i=\sum_{j=1}^n a_{ij}x_j.
\]

右边说明：\(x_j\) 是取第 \(j\) 列的权重，输出是这些列的加权和。这并不只是记忆乘法规则；若 \(A\) 是模型权重矩阵，输入特征的大小就在控制每列对预测的贡献。**【补充理解】** 同一个 \(A\) 也定义从 \(\mathbb R^n\) 到 \(\mathbb R^m\) 的线性变换：它对加法和数乘保持结构，即 \(A(u+v)=Au+Av\)、\(A(cu)=cAu\)。这个“变换”视角在降维与特征分析中有用。

矩阵加减要求形状相同；乘法 \(A_{m\times p}B_{p\times n}\) 的结果是 \(m\times n\)。课件给出结合律、分配律，但一般 \(AB\ne BA\)。（PDF p.3–5）转置交换行列，\((AB)^\mathsf T=B^\mathsf T A^\mathsf T\)，乘积顺序反过来。（PDF p.6）

## 3. 正式定义：模型计算时最常遇到的对象

### 3.1 矩阵、秩、行列式与逆

对角矩阵 \(\operatorname{diag}(a_{11},\ldots,a_{nn})\) 只有主对角线可非零；单位矩阵 \(I\) 在主对角线为 1；迹 \(\operatorname{tr}(A)=\sum_i a_{ii}\) 是对角元素之和。（PDF p.2）

若存在不全为零的 \(c_j\) 使 \(\sum_j c_j a_j=0\)，这些列线性相关（linearly dependent）。rank（秩）是独立列的最大数，也等于独立行的最大数；若 \(\operatorname{rank}(A)=\min(m,n)\)，称 full rank（满秩）。（PDF p.8）秩告诉我们是否有冗余方向。例如两列完全相同，数据只能识别两系数的**和**，无法单独识别它们。

方阵 \(A\in\mathbb R^{n\times n}\) 的逆 \(A^{-1}\) 满足 \(A^{-1}A=AA^{-1}=I\)。二阶矩阵 \(\begin{bmatrix}a&b\\c&d\end{bmatrix}\) 的 determinant（行列式）是 \(ad-bc\)；方阵行列式为零时不可逆。（PDF p.7、9）\((AB)^{-1}=B^{-1}A^{-1}\) 同样反序，前提是相关方阵可逆。课件给了余子式逆矩阵公式；实际求大矩阵解时通常不逐项计算余子式。

### 3.2 长度、夹角与两种乘积

norm（范数）度量向量大小，距离可由 \(\|x-y\|\) 构造。课件列出（PDF p.10）

\[
\|x\|_1=\sum_i|x_i|,\qquad
\|x\|_2=\sqrt{\sum_i x_i^2},\qquad
\|x\|_\infty=\max_i|x_i|,
\]

以及一般的 \(p\)-norm（\(p\ge1\)）。同一对样本在不同范数下的距离可能不同，因此“最近”要先说明采用哪种度量。

inner product（内积）\(x^\mathsf T y=\sum_i x_i y_i\) 是标量；对非零向量还等于 \(\|x\|_2\|y\|_2\cos\theta\)，所以归一化后可表示方向相似性，内积为零表示正交。（PDF p.11）outer product（外积）\(xy^\mathsf T\) 则是矩阵：若 \(x\in\mathbb R^m,y\in\mathbb R^n\)，结果为 \(m\times n\)，第 \((i,j)\) 项是 \(x_i y_j\)。后面协方差矩阵就会用到这种结构。

### 3.3 正定、特征方向与曲率

对称矩阵 \(A\in\mathbb R^{n\times n}\) 若对所有 \(x\) 有 \(x^\mathsf T A x\ge0\)，称 positive semidefinite, PSD（半正定）；若对所有非零 \(x\) 严格大于零，称 positive definite, PD（正定）。若存在方向使二次型为正、另有方向为负，就属于课件的 indefinite（不定）情形。（PDF p.12）

**【补充理解：曲率类比】** \(x^\mathsf T A x\) 可看作沿方向 \(x\) 的二次代价。PSD 允许平坦方向，PD 在每个非零方向都有正代价。这解释了为何 [Introduction](01_Introduction.md) 的 \(\Phi^\mathsf T\Phi\) 总是 PSD：\(z^\mathsf T\Phi^\mathsf T\Phi z=\|\Phi z\|_2^2\ge0\)。若 \(\Phi\) 列满秩，\(z\ne0\Rightarrow\Phi z\ne0\)，所以它是 PD。课件也介绍 PD 矩阵的 Cholesky factorization（Cholesky 分解）。（PDF p.13）

若 \(Av=\lambda v\) 且 \(v\ne0\)，\(v\) 是 eigenvector（特征向量），\(\lambda\) 是 eigenvalue（特征值）：变换后方向不变，只被缩放。由 \((A-\lambda I)v=0\) 可知，非零解要求 \(\det(A-\lambda I)=0\)。（PDF p.14）对称 \(A\) 可写成 \(A=Q\Lambda Q^\mathsf T\)，\(Q\) 的列是互相正交的单位特征向量，\(\Lambda\) 的对角线是相应特征值；PD 的特征值全正，PSD 的特征值非负。（PDF p.14–15）这给我们一组互不干扰的方向来理解变换，也为后续降维提供基础。

### 3.4 梯度与 Hessian

对标量函数 \(f:\mathbb R^n\to\mathbb R\)，gradient（梯度）是 \(\nabla_x f=(\partial f/\partial x_1,\ldots,\partial f/\partial x_n)^\mathsf T\in\mathbb R^n\)。（PDF p.16）**【补充理解】** 在可微且梯度非零的点，单位方向 \(u\) 的一阶变化率为 \(\nabla f(x)^\mathsf T u\)；由 Cauchy–Schwarz 不等式可知它在 \(u=\nabla f/\|\nabla f\|\) 时最大，所以梯度指向局部最快上升方向。

Hessian matrix（Hessian 矩阵）\(H_{ij}=\partial^2 f/(\partial x_i\partial x_j)\in\mathbb R^{n\times n}\) 收集二阶导数，描述局部曲率。（PDF p.18）课件说 Hessian 对称；严谨条件是相关二阶混合偏导在邻域连续，此时 \(H_{ij}=H_{ji}\)。

## 4. 数学推导：梯度公式为何适用于模型训练？

**推导目标。** 从分量而非背诵公式，推导 \(f(w)=\tfrac12\|Aw-b\|_2^2\) 的梯度与 Hessian；其中 \(A\in\mathbb R^{m\times n}\)，\(w\in\mathbb R^n\)，\(b\in\mathbb R^m\)。这是课件 p.17 的矩阵求导规则在最小二乘中的应用。

**Step 1：写成分量。** \(f(w)=\tfrac12\sum_{i=1}^m(\sum_{j=1}^n a_{ij}w_j-b_i)^2\)。每个括号是第 \(i\) 个预测残差。

**Step 2：对第 \(k\) 个参数求导。** 链式法则给出

\[
\frac{\partial f}{\partial w_k}
=\sum_{i=1}^m\left(\sum_j a_{ij}w_j-b_i\right)
\frac{\partial(\sum_j a_{ij}w_j-b_i)}{\partial w_k}
=\sum_{i=1}^m a_{ik}(Aw-b)_i.
\]

最后一步是因为括号内只有 \(a_{ik}w_k\) 对 \(w_k\) 的导数为 \(a_{ik}\)。把所有 \(k\) 的结果堆成列向量，恰好是

\[
\nabla_w f=A^\mathsf T(Aw-b)\in\mathbb R^n.
\]

**Step 3：再求一次导数。** 第 \(k\) 个梯度分量对 \(w_\ell\) 求导得到 \(\sum_i a_{ik}a_{i\ell}\)，故 \(H=A^\mathsf T A\in\mathbb R^{n\times n}\)。它始终 PSD；若 \(A\) 列满秩则 PD。这样“正规方程是否有唯一解”与“曲率有没有平坦方向”连在了一起。

课件 p.17 还列出 \(\nabla_x(x^\mathsf T y)=y\)、\(\nabla_x(x^\mathsf T x)=2x\)、\(\nabla_x(x^\mathsf T A x)=(A+A^\mathsf T)x\)。上面的分量法同样可以逐项验证这些式子。\(\nabla_A\log|A|=A^{-1}\) 在课件的 PD、对称条件下成立；不要脱离条件把矩阵导数公式机械套用。

## 5. Numerical Example：实际算一次

取 \(A=\begin{bmatrix}1&2\\3&4\end{bmatrix}\)、\(x=(2,-1)^\mathsf T\)。把列按权重组合：\(Ax=2(1,3)^\mathsf T-(2,4)^\mathsf T=(0,2)^\mathsf T\)。从逐行点积计算也得到相同结果。\(\det A=1\cdot4-2\cdot3=-2\ne0\)，因此 \(A\) 可逆。（PDF p.4、7）

再取对称矩阵 \(B=\begin{bmatrix}2&1\\1&2\end{bmatrix}\)。\(v_1=(1,1)^\mathsf T\) 满足 \(Bv_1=3v_1\)，\(v_2=(1,-1)^\mathsf T\) 满足 \(Bv_2=v_2\)。两特征值 3 和 1 都正，所以 \(B\) 是 PD；对应二次代价在 \((1,1)\) 方向增长更快。相反 \(D=\operatorname{diag}(1,-1)\) 在 \((1,0)\) 上给正值，在 \((0,1)\) 上给负值，是 indefinite。这个反例说明“对称”不等于“正定”。

## 6. 它在 Machine Learning 中为什么重要？

- **矩阵乘法与维度**：一批样本乘权重矩阵可一次计算多项预测；维度检查能在写代码前发现错误。（PDF p.4–5）
- **秩、逆与正定**：决定最小二乘解是否唯一；重复或冗余特征会造成秩不足。（PDF p.8–9、12–13）
- **范数与内积**：分别进入距离、正则化和方向相似度计算。（PDF p.10–11）
- **特征值**：揭示线性变换在不同方向上的缩放；在协方差分析和降维中会再次出现。（PDF p.14–15）
- **梯度、Hessian**：梯度给出参数改变的局部方向，Hessian 描述损失的曲率；后续 [Optimization Primer](04_Optimization_Primer.md) 将用它们讨论最优性和梯度下降。（PDF p.16–18）

## 7. 容易混淆的概念

| A | B | 区别 |
|---|---|---|
| \(x^\mathsf T y\) | \(xy^\mathsf T\) | 前者为标量，后者为矩阵；维度决定意义。 |
| \(A^\mathsf T\) | \(A^{-1}\) | 前者交换行列，后者撤销线性变换；仅正交方阵满足二者相等。 |
| full rank | invertible | 非方阵也可满秩；只有方阵满秩才有普通逆。 |
| PSD | PD | PSD 允许非零平坦方向；PD 对每个非零方向严格为正。 |
| eigenvector | eigenvalue | 前者是方向，后者是该方向的缩放倍数。 |
| gradient | Hessian | 前者是一阶变化向量，后者是二阶变化矩阵。 |

## 8. 常见错误

1. 只看数字，不检查 \((m\times n)(n\times p)=(m\times p)\) 的维度。
2. 把 \(AB\) 和 \(BA\) 当成同一个式子，或把 \((AB)^\mathsf T\) 写成 \(A^\mathsf T B^\mathsf T\)。（PDF p.5–6）
3. 以为 PSD 一定可逆：\(\operatorname{diag}(1,0)\) 是 PSD，但行列式为零。
4. 以为“协方差有负的非对角元素”就不是 PSD；PSD 判断的是整个二次型，不要求每一项非负。
5. 以为梯度就是函数值：梯度是和输入同维的向量；函数值是标量。

## 9. English Terminology

| English | 中文含义 | 一句话理解 |
|---|---|---|
| matrix / column vector | 矩阵 / 列向量 | 一组线性变换系数 / 一组有序特征。 |
| transpose | 转置 | 交换行与列。 |
| rank / full rank | 秩 / 满秩 | 独立方向数 / 达到形状允许的最大值。 |
| determinant / inverse | 行列式 / 逆 | 方阵是否可逆的判据之一 / 撤销变换。 |
| norm / inner product / outer product | 范数 / 内积 / 外积 | 长度 / 标量相似性 / 矩阵构造。 |
| positive semidefinite (PSD) | 半正定 | 所有方向的二次代价非负。 |
| positive definite (PD) | 正定 | 每个非零方向的二次代价都严格为正。 |
| eigenvalue / eigenvector | 特征值 / 特征向量 | 不变方向的缩放倍数 / 那个方向。 |
| gradient / Hessian | 梯度 / Hessian 矩阵 | 一阶变化方向 / 二阶曲率。 |

*Eigen* 常被译成“特征”；应记住的数学含义是 \(Av=\lambda v\)，即该方向经变换后仍沿同一直线，而不是把词源当作证明。

## 10. 本节知识地图

```text
样本 → 列向量 → 矩阵乘法形成预测
                 ↓
             范数度量误差
                 ↓
          梯度/Hessian 优化参数
                 ↓
       秩、正定、特征值解释解与曲率
```

## 11. 自测

1. \(A\in\mathbb R^{5\times3}\)、\(x\in\mathbb R^3\)，\(Ax\) 是什么维度？每个分量由什么构成？
2. 如果 \(A\) 的第 2 列恰好是第 1 列的两倍，为什么无法从 \(Ax\) 唯一区分相应两个系数的作用？
3. \(\|x\|_2^2\) 与 \(x^\mathsf T x\) 有何关系？\(x^\mathsf T y\) 与 \(xy^\mathsf T\) 的输出分别是什么？
4. 用 \(\|Az\|^2\) 证明 \(A^\mathsf T A\) 总是 PSD；加什么条件才是 PD？
5. 为什么 PSD Hessian 与“局部没有向下弯的方向”有关？
6. 证明二阶矩阵 \(D=\operatorname{diag}(1,-1)\) 不是 PSD。
7. 在给定 \(\nabla f\ne0\) 时，为什么 \(-\nabla f\) 是局部下降方向？

<details><summary>展开答案要点</summary>

1. \(\mathbb R^5\)；每个分量是某一行与 \(x\) 的内积。2. 两列线性相关，例如两系数一增一减可保持输出不变。3. 相等；前者内积为标量，后者外积为矩阵。4. \(z^\mathsf T A^\mathsf T A z=\|Az\|^2\ge0\)；\(A\) 列满秩时非零 \(z\) 不会映到零。5. 二阶近似的方向项为 \(\tfrac12u^\mathsf T H u\)。6. 取 \(z=(0,1)^\mathsf T\) 得 \(z^\mathsf T D z=-1\)。7. 方向导数 \(\nabla f^\mathsf T(-\nabla f)=-\|\nabla f\|^2<0\)。

</details>
