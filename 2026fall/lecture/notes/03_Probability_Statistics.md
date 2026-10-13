# 03 · Mathematical Foundations: Probability and Statistics（概率与统计基础）

> 主来源：[Probability_Statistics.pdf](../Probability_Statistics.pdf)，页码从封面起算。本讲义在课件基础上补出必要的中间步骤；标 **【补充理解】** 的内容不是额外考试范围声明。

## 0. 这节课到底在解决什么问题？

面对一位只知道部分信息的顾客，我们无法肯定他属于哪类；面对一批样本，我们也无法肯定未来样本会怎样。概率（probability）把这种不确定性写成可计算的数，统计（statistics）则帮助我们由有限样本推断未知规律。课件以“25 名男生、15 名女生中随机选一人”开头：未看到具体学生时可以描述类别比例；一旦观察到新线索，判断可能改变。（PDF p.2）

本讲的主线是：事件及条件概率 → 随机变量及其分布 → 多变量联合、边缘和条件分布 → 期望与变异 → 常用分布与样本统计量。后面的 [Bayesian Decision Theory](05_Bayesian_Decision_Theory.md) 需要从 \(P(C_i)\) 更新到 \(P(C_i\mid x)\)；[Parameter Estimation](06_Parameter_Estimation.md) 则要从数据估计这些量。

## 1. 前置知识与符号

会分数、求和与基本积分即可。\(S\) 表示 sample space（样本空间），\(A,B\subseteq S\) 表示事件；大写 \(X,Y\) 是 random variables（随机变量），小写 \(x,y\) 是它们可能取得的数值。课件用 \(P(\cdot)\) 表示事件概率，也用 \(p(x)\) 表示 PMF 或 PDF；**同一个字母 \(p\) 的意义取决于变量是离散还是连续**。（PDF p.2、10–12）

## 2. 核心直觉：知道信息前后，候选范围变了

**【补充理解：筛选盒类比】** 想象 40 张学生卡片装在盒中。事件 \(A\) 是“抽到男生”，共有 25 张；事件 \(B\) 是“卡片上写着某项特征”。\(P(A)\) 看完整盒，\(P(A\mid B)\) 则先筛出满足 \(B\) 的卡片，再看其中 \(A\) 的比例。类比中的“盒”对应样本空间，“筛选”对应条件事件；它适合有限、等可能的卡片，不意味着所有连续型概率都能靠简单计数计算。

先有 \(P(A)\)，再观察 \(B\) 才有 \(P(A\mid B)\)。*Prior*（先验）按词义是观察新证据之前的判断，*posterior*（后验）是观察之后的判断。Bayes' rule 给出从前者到后者的正确更新方式；它并不凭空制造先验或数据模型。（PDF p.5–9）

## 3. 正式定义：从事件到条件概率

事件概率满足 \(0\le P(A)\le1\)、\(P(S)=1\)；对任意 \(A,B\)，\(P(A\cup B)=P(A)+P(B)-P(A\cap B)\)。减去交集，是因为前两项把同时发生部分数了两遍。若 mutually exclusive（互斥），\(A\cap B=\varnothing\)，则交集项为零。（PDF p.3–4）

条件概率（conditional probability）的定义为 \(P(B\mid A)=P(A\cap B)/P(A)\)，要求 \(P(A)>0\)。整理得 product rule（乘法法则）\(P(A\cap B)=P(B\mid A)P(A)\)。对更多事件反复使用，得到课件 p.6 的 chain rule（链式法则）。

independence（独立）要求知道一个事件不会改变另一个事件的概率；在相关条件概率有定义时，等价于 \(P(A\cap B)=P(A)P(B)\)。（PDF p.7）互斥与独立不同：两个概率都大于零的互斥事件不可能独立，因为其交集概率为零，而概率乘积大于零。

若 \(A_1,\ldots,A_K\) 两两互斥且覆盖 \(S\)，total probability（全概率公式）把 \(B\) 分成互不重叠的片：\(P(B)=\sum_iP(B\mid A_i)P(A_i)\)。（PDF p.6）

## 4. 数学推导：Bayes' rule 每一步从哪来？

**推导目标。** 已知 \(P(A_i)\) 和 \(P(B\mid A_i)\)，观察 \(B\) 后求 \(P(A_i\mid B)\)。假设 \(A_i\) 构成互斥且穷尽的类别划分，\(P(B)>0\)。

**Step 1：条件概率定义。** \(P(A_i\mid B)=P(A_i\cap B)/P(B)\)。分子表示“类别 \(A_i\) 与证据 \(B\) 同时发生”。

**Step 2：改写分子。** 按乘法法则，\(P(A_i\cap B)=P(B\mid A_i)P(A_i)\)。这是条件概率定义重新排列，并未假定独立。

**Step 3：展开分母。** 因类别互斥且穷尽，事件 \(B\) 可分为各个 \(B\cap A_j\)，所以 \(P(B)=\sum_jP(B\cap A_j)=\sum_jP(B\mid A_j)P(A_j)\)。第一处等号用互斥相加，第二处用乘法法则。

**Step 4：合并。**

\[
P(A_i\mid B)=\frac{P(B\mid A_i)P(A_i)}{\sum_{j=1}^K P(B\mid A_j)P(A_j)}.
\]

分子是“先验 × 在该类别下看到证据的可能性”；分母把所有类别的分子相加，使后验总和为 1。（PDF p.8）对连续特征 \(x\)，课件还写 \(P(C_i\mid x)=p(x\mid C_i)P(C_i)/p(x)\)；这里 \(p(x\mid C_i)\) 与 \(p(x)\) 是**密度值**，不是“恰好取 \(x\)”的点概率。

### 4.1 Numerical Example：课件的咳嗽例子

PDF p.9 给 \(P(\text{SARS})=0.005\)、\(P(\text{Cough}\mid\text{SARS})=0.8\)、\(P(\text{Cough})=0.05\)。代入得

\[
P(\text{SARS}\mid\text{Cough})
=\frac{0.8\times0.005}{0.05}
=0.08.
\]

也就是说，在这些假设概率成立时，观察咳嗽后该类的后验为 8%，**不是** 80%。分母已包含其他原因造成的咳嗽。这个例子只用于概率计算，不能用于真实诊断。

## 5. 随机变量：离散、连续、联合与边缘

random variable, RV（随机变量）是把随机实验的结果映射为数值的函数。CDF（cumulative distribution function，累积分布函数）统一写为 \(F(x)=P(X\le x)\)，因此 \(P(a<X\le b)=F(b)-F(a)\)。（PDF p.10）

离散 \(X\) 的 PMF（probability mass function，概率质量函数）为 \(p(x)=P(X=x)\)，各点质量相加为 1；其 CDF 是阶梯状累加。（PDF p.11）连续 \(X\) 的 PDF（probability density function，概率密度函数）满足 \(P(a<X\le b)=\int_a^b p(x)\,dx\)；单一点的概率通常为零，密度值甚至可以大于 1，只要求非负且整体积分为 1。在可微点 \(p(x)=F'(x)\)。（PDF p.12）**PMF 给点概率，PDF 给单位长度附近的概率密度，CDF 给累计概率。**

对离散变量 \(X,Y\)，joint PMF（联合质量函数）\(p(x,y)=P(X=x,Y=y)\) 描述“同时取值”；marginal PMF（边缘质量函数）\(p_X(x)=\sum_y p(x,y)\) 则把不关心的 \(Y\) 求和消去。联合 CDF 为 \(F(x,y)=P(X\le x,Y\le y)\)。（PDF p.13–14）连续情形将求和换为积分，例如 \(p_X(x)=\int_{-\infty}^{\infty}p(x,y)\,dy\)，矩形区域概率由二重积分得到；联合 CDF 的混合偏导在适当光滑条件下回到联合密度。（PDF p.15–16）

conditional distribution（条件分布）是在已知另一个变量后重新归一化的分布；离散情形 \(p(x\mid y)=p(x,y)/p_Y(y)\)，分母须大于零。若 \(X,Y\) 独立，则 \(p(x,y)=p_X(x)p_Y(y)\)；这比“相关系数为零”更强。（PDF p.17）对连续变量，形式类似但 \(p(x\mid y)\) 是条件**密度**，不能把 \(P(Y=y)\) 当作正数直接代入离散公式。

**【补充理解：likelihood 与 probability】** 当参数 \(\theta\) 固定而数据 \(x\) 尚未观察时，\(p(x\mid\theta)\) 是关于 \(x\) 的 PMF/PDF。观察到 \(x\) 后，把同一表达式视为参数 \(\theta\) 的函数 \(L(\theta;x)=p(x\mid\theta)\)，称 likelihood（似然）：问“哪个参数使这些已见数据更合理”。它不必作为 \(\theta\) 的函数积分为 1。课件 p.8 在分类场景也把 \(p(x\mid C_i)\) 称为 likelihood；详细参数似然会在 [Parameter Estimation](06_Parameter_Estimation.md) 展开。

## 6. 期望、变异与协方差

expectation（期望）是按概率加权的平均：离散型 \(E(X)=\sum_x x p(x)\)，连续型 \(E(X)=\int xp(x)\,dx\)。对函数 \(g\)，把 \(x\) 换成 \(g(x)\) 即可求 \(E[g(X)]\)。线性性给 \(E(aX+b)=aE(X)+b\)；课件 p.18 还列出 \(E(X+Y)=E(X)+E(Y)\)，此式**不要求独立**。（PDF p.18）

variance（方差）\(\operatorname{Var}(X)=E[(X-\mu)^2]=E(X^2)-\mu^2\)，其中 \(\mu=E(X)\)。第二个等号可展开：\(E[X^2-2\mu X+\mu^2]=E(X^2)-2\mu^2+\mu^2\)。标准差 \(\sigma\) 与 \(X\) 单位相同，方差则是单位的平方。\(\operatorname{Var}(aX+b)=a^2\operatorname{Var}(X)\)。（PDF p.19）课件把 \(E(X^r)\) 称 r-th moment，把 \(E[(X-\mu)^r]\) 称 r-th central moment。

covariance（协方差）\(\operatorname{Cov}(X,Y)=E[(X-\mu_X)(Y-\mu_Y)]=E(XY)-\mu_X\mu_Y\)。展开理由与方差相同。\(\operatorname{Var}(X+Y)=\operatorname{Var}(X)+\operatorname{Var}(Y)+2\operatorname{Cov}(X,Y)\)；独立可推出协方差为零，反向一般不成立。correlation（相关系数）\(\operatorname{Corr}(X,Y)=\operatorname{Cov}(X,Y)/(\sigma_X\sigma_Y)\) 去掉量纲，要求两标准差非零。（PDF p.20）

对 \(d\)-维随机向量 \(X\)，\(\mu=E(X)\in\mathbb R^d\)、\(\Sigma=E[(X-\mu)(X-\mu)^\mathsf T]\in\mathbb R^{d\times d}\)。第 \((i,j)\) 项是 \(\operatorname{Cov}(X_i,X_j)\)；对角线应为各分量方差。课件 p.22 的最后两行矩阵排版把左上角也写成 \(\sigma_{12}\)，应按 p.21 定义理解为 \(\sigma_{11}\)。进一步，任意 \(a\in\mathbb R^d\) 满足 \(a^\mathsf T\Sigma a=E[(a^\mathsf T(X-\mu))^2]\ge0\)，所以协方差矩阵是 PSD；这连接 [Linear Algebra](02_Linear_Algebra.md)。

## 7. 常用分布及其用途

| 课件页码 | 分布 | 典型问题与关键式 |
|---|---|---|
| p.24–25 | 离散均匀、Bernoulli | 公平骰子；一次成败试验 \(X\in\{0,1\}\)，\(P(X=x)=p^x(1-p)^{1-x}\)，\(E(X)=p\)。 |
| p.26–27 | Binomial、Multinomial | \(N\) 次独立成败的成功次数；\(K\) 类重复试验的各类计数。\(N=1\) 的多类别单次试验通常称 categorical。 |
| p.28–29 | 连续均匀、normal/Gaussian | 有界区间内等密度；围绕均值 \(\mu\) 的连续噪声，方差 \(\sigma^2\)。标准化 \(Z=(X-\mu)/\sigma\sim N(0,1)\)。 |
| p.31–36 | \(\chi^2\)、Student's t | 独立标准正态的平方和；总体方差未知时，样本均值的标准化不确定性。t 分布尾部比正态厚。 |
| p.38–39 | 多元 normal、多元 t | 向量特征的联合分布；均值向量、协方差或尺度矩阵决定位置、方向和扩散。 |

**【补充理解：一个必须补齐的条件】** 课件 p.32 在构造精确 t 统计量时先写“样本 i.i.d.、具有均值和方差”。若要得到后面的**精确**正态、\(\chi^2\)、样本均值与样本方差独立，并最终得到 t 分布，必须进一步假设原始样本来自正态总体。一般 i.i.d. 且有限方差只能借中央极限定理得到样本均值的渐近正态，不能直接声称有限样本的精确 t 结论。

### 7.1 大数定律与中央极限定理

课件 p.23 的 weak law of large numbers（弱大数定律）说：i.i.d. 且方差有限时，样本平均 \(\bar X_N=N^{-1}\sum_iX_i\) 偏离真实均值 \(\mu\) 超过任意固定 \(\varepsilon>0\) 的概率随 \(N\to\infty\) 趋于零。**【补充理解】** 因 \(\operatorname{Var}(\bar X_N)=\sigma^2/N\)，Chebyshev 不等式给 \(P(|\bar X_N-\mu|>\varepsilon)\le\sigma^2/(N\varepsilon^2)\to0\)。这里每个等号依次用了独立性、方差缩放与 Chebyshev。

central limit theorem, CLT（中央极限定理）讨论的不是“平均值会靠近哪里”，而是“合适标准化后的波动是什么形状”：i.i.d. 且方差有限时，\(\sqrt N(\bar X_N-\mu)/\sigma\) 的分布趋向标准正态。课件 p.30 把大 \(N\) 时的**和**近似写成 \(N(N\mu,N\sigma^2)\)，与这个表述相容。近似不代表原始 \(X_i\) 自身正态。

### 7.2 t 统计量的关键中间步骤

对正态总体 \(X_1,\ldots,X_N\)（这是精确结论所需条件），令 \(\bar X=N^{-1}\sum_iX_i\)、\(S^2=\sum_i(X_i-\bar X)^2/(N-1)\)。则

\[
Z=\frac{\bar X-\mu}{\sigma/\sqrt N}\sim N(0,1),
\quad U=\frac{(N-1)S^2}{\sigma^2}\sim\chi^2_{N-1},
\quad Z\perp U.
\]

把未知 \(\sigma\) 换成 \(S\) 后，分子分母同除 \(\sigma\)：

\[
\frac{\bar X-\mu}{S/\sqrt N}
=\frac{Z}{\sqrt{U/(N-1)}}\sim t_{N-1}.
\]

课件 p.33–34 用正交变换说明 \(U\) 为什么有 \(N-1\) 个自由度：标准化样本向量的一维被“平均值方向”占用，剩余正交方向的平方和就是 \(\chi^2_{N-1}\)。p.35–36 给 t 密度及均值、方差存在的自由度条件；p.37 重述样本统计量。注意 p.37 对 \(S^2\) 的缩放在文本提取中有排版问题，应以上式和 p.32–34 的推导为准。多元 t 在 p.39 由位置 \(\mu\)、尺度 \(\Sigma\) 和自由度控制；其 covariance 在自由度大于 2 时是 \(\frac{n}{n-2}\Sigma\)，故尺度矩阵不总等于协方差矩阵。

## 8. 易混淆概念与常见错误

| A 与 B | 一句话区分 | 容易犯的错 |
|---|---|---|
| joint 与 marginal | 同时描述多个变量 / 消去不关心变量 | 忘记对另一变量求和或积分。 |
| conditional 与 marginal | 已知条件后的分布 / 不附加该条件 | 把 \(P(A\mid B)\) 写成 \(P(B\mid A)\)。 |
| mutually exclusive 与 independent | 不能同时发生 / 一方不改变另一方概率 | 当二者都有正概率时，把互斥误认为独立。 |
| PMF 与 PDF | 离散点质量 / 连续密度 | 把 \(p(x)\) 的密度值当成点概率。 |
| PDF 与 CDF | 局部密度 / 到 \(x\) 为止的累计概率 | 忘记连续区间概率要对 PDF 积分。 |
| probability 与 likelihood | 固定模型看可能数据 / 固定已见数据比较参数 | 以为 likelihood 在参数上必须归一化。 |
| variance 与 covariance | 单变量离散程度 / 两变量共同变化 | 以为零协方差必然独立。 |
| prior 与 posterior | 观察当前证据前 / 后 | 忘记后验还取决于各类出现证据的可能性。 |

## 9. English Terminology

| English | 中文 | 一句话理解 |
|---|---|---|
| sample space / event | 样本空间 / 事件 | 所有可能结果 / 其中一组结果。 |
| conditional probability | 条件概率 | 已知某事件发生后重新计算。 |
| independence | 独立 | 得知一方不改变另一方的概率。 |
| random variable (RV) | 随机变量 | 把随机结果映射成数。 |
| PMF / PDF / CDF | 质量 / 密度 / 累积分布函数 | 点质量 / 区间密度 / 累计概率。 |
| joint / marginal distribution | 联合 / 边缘分布 | 多变量一起看 / 对其他变量求和或积分。 |
| prior / posterior | 先验 / 后验 | 看证据之前 / 之后的判断。 |
| likelihood | 似然 | 已见数据下比较参数的合理程度。 |
| expectation / variance / covariance | 期望 / 方差 / 协方差 | 平均位置 / 自身波动 / 共同波动。 |
| weak law / central limit theorem | 弱大数定律 / 中央极限定理 | 均值趋近 / 标准化波动趋向正态。 |

## 10. 本节知识地图

```text
样本空间与事件 → 条件概率 → 全概率公式 + Bayes' rule
                                  ↓
随机变量 → PMF/PDF/CDF → 联合、边缘、条件分布
                                  ↓
                   期望、方差、协方差
                                  ↓
           常用分布 + 样本统计量 → 后续决策与估计
```

## 11. 自测

1. 若 \(P(A)=0.2\)、\(P(B\mid A)=0.5\)，\(P(A\cap B)\) 是多少？仅凭这两数能求 \(P(A\mid B)\) 吗？
2. 为何两个有正概率的互斥事件不能独立？
3. 若连续变量的 \(p(1)=2\)，这是否违反概率不大于 1？
4. 写出从联合 \(p(x,y)\) 求离散 \(X\) 的边缘分布的操作。
5. 为何 \(E(X+Y)=E(X)+E(Y)\) 不要求独立，而 \(\operatorname{Var}(X+Y)=\operatorname{Var}(X)+\operatorname{Var}(Y)\) 通常要求额外条件？
6. 课件咳嗽例子中，为什么后验是 8% 而不是 80%？
7. \(p(x\mid\theta)\) 何时被称为 likelihood？对 \(\theta\) 是否必须积分为 1？
8. 为什么协方差矩阵必为 PSD？
9. 弱大数定律与中央极限定理各回答了样本均值的什么问题？
10. 从 \(Z\) 和 \(U\) 构造精确 t 统计量时，为什么不能只写“i.i.d. 且方差有限”？

<details><summary>展开答案要点</summary>

1. \(0.1\)；还缺 \(P(B)\)。2. 交集概率为零，而概率乘积大于零。3. 不违反；密度不是点概率，区间积分才是概率。4. \(p_X(x)=\sum_y p(x,y)\)。5. 方差展开多出 \(2\operatorname{Cov}(X,Y)\)。6. 还要除以总体咳嗽概率 \(0.05\)。7. 把已观察 \(x\) 固定、以 \(\theta\) 为变量时；不必。8. \(a^\mathsf T\Sigma a\) 是某随机变量的平方期望。9. 分别回答是否靠近真实均值、标准化波动趋向什么分布。10. 有限样本精确正态与样本均值、样本方差独立需要正态总体等条件。

</details>
