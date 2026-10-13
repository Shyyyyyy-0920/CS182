# 06 · Parameter Estimation for Generative Models（生成模型的参数估计）

> 主来源：[Parameter_Estimation.pdf](../Parameter_Estimation.pdf)，PDF 页码从封面算起。本文件对应完整的 90 页课件；**【补充理解】** 表示我为教学补出的例子、推导或严谨条件。建议按章节分次学，每次做末尾对应的自测，而不是一次读完。

## 0. 这节课到底在解决什么问题？

上一讲 [Bayesian Decision Theory](05_Bayesian_Decision_Theory.md) 告诉我们：知道类先验 \(P(C_i)\) 和类条件密度 \(p(x\mid C_i)\) 后，便能算后验并选风险最低的行动。现实却不会把这些分布直接交给我们。我们只拿到一批观测值和标签，必须从中**估计**分布的参数，然后才能使用决策规则。课件 p.4–6 正是以这道缺口引出 parametric approach（参数化方法）。

参数化方法先假定一个分布族，例如“每类数据近似正态”，再用有限维参数 \(\theta\) 指定族中的某个成员。**【补充理解：旋钮类比】** 分布族像一台可调的机器，均值、方差、类别比例是旋钮；观测数据是机器产出的样品；估计就是依据样品倒推旋钮位置。对应关系是“分布族 ↔ 模型假设”“旋钮 ↔ 参数 \(\theta\)”“样品 ↔ 数据”。类比不能保证机器假设正确；若真实数据不是所假设的族，估计再精确也可能产生错误决策。

本讲有两大部分：单变量数据中建立 MLE、Bayesian Estimation、分类、回归和模型选择；多变量数据中处理协方差、多元正态、QDA/LDA、离散特征及多元回归。术语很多，但始终围绕同一问题：**用样本建立可泛化的概率或预测模型**。

## 1. 前置知识、对象和全局记号

需要 [Probability and Statistics](03_Probability_Statistics.md) 的 PMF/PDF、条件概率、正态分布、期望与方差；[Linear Algebra](02_Linear_Algebra.md) 的矩阵、正定、行列式与梯度；[Optimization Primer](04_Optimization_Primer.md) 的极值与 Lagrange multiplier。

课件单变量部分记训练样本 \(X=\{x^t\}_{t=1}^N\)，其中 \(t\) 是样本编号；多变量部分 \(x^t\in\mathbb R^d\)，整个数据矩阵有 \(N\) 行、\(d\) 列（PDF p.55）。分类时 \(r_i^t\in\{0,1\}\) 是第 \(t\) 个样本属于第 \(i\) 类的指示量，并满足 \(\sum_i r_i^t=1\)；\(N_i=\sum_t r_i^t\) 是第 \(i\) 类样本数。回归时 \(r^t\in\mathbb R\) 是目标输出。\(m\) 常记样本均值，\(S\) 常记以 \(1/N\) 为分母的样本协方差；二者与真实 \(\mu,\Sigma\) 不同。

## 2. 参数化方法：为什么先选分布族？（PDF p.4–6）

课件区分 parametric、nonparametric 和 semiparametric 三种路线，此处只研究 parametric。假设 \(x^t\) 通常为 i.i.d. 样本且 \(x^t\sim p(x\mid\theta)\)。\(\theta\) 的维度通常不随样本数 \(N\) 增长：收集更多数据的目的，是更准确地确定同一组旋钮，而非每来一条数据就增加一个新旋钮。（PDF p.5）这个固定分布形状本身就是 inductive bias（归纳偏置）。

生成式分类器（generative classifier）对每个类估计 \(p(x\mid C_i)\)，再估计 \(P(C_i)\)，从而规定“先抽类别、再按该类别生成特征”的联合模型 \(p(x,C_i)=p(x\mid C_i)P(C_i)\)。于是 Bayes' rule 给出后验。相比之下，discriminative approach（判别式方法）可直接学习后验或判别边界，不必先拟合每类完整的特征分布；课件 p.36 预告后续学习。

## 3. Maximum Likelihood Estimation, MLE（最大似然估计）（PDF p.9–20）

### 3.1 概率与似然究竟差在哪？

给定 \(\theta\) 后，\(p(x\mid\theta)\) 描述可能观察值 \(x\) 的概率质量或密度。已经观察到样本 \(X\) 后，把同一表达式当成 \(\theta\) 的函数，称 likelihood（似然）：\(L(\theta\mid X)=p(X\mid\theta)\)。这里问的是“哪组参数让**这些已见数据**最合理”，不是“参数本身的概率是多少”。似然函数对 \(\theta\) 不必归一化。

若样本在给定 \(\theta\) 后独立同分布，联合似然为 \(L(\theta\mid X)=\prod_{t=1}^Np(x^t\mid\theta)\)。独立性允许乘积，同分布让每项使用相同形式。取 log 后得到 \(\ell(\theta\mid X)=\sum_t\log p(x^t\mid\theta)\)；正数上的 log 严格递增，故不改变 \(\arg\max\)，却把乘积变成更易求导且更不易下溢的和。MLE 为 \(\hat\theta_{\rm ML}=\arg\max_\theta\ell(\theta\mid X)\)。（PDF p.9–10）若某候选参数使观测数据的概率为零，它的对数似然为 \(-\infty\)。

### 3.2 Bernoulli 参数的完整推导（PDF p.11–12）

**推导目标。** 求一次成功概率 \(p\) 的 MLE。

**已知条件。** \(x^1,\ldots,x^N\in\{0,1\}\) 独立同分布，\(P(x\mid p)=p^x(1-p)^{1-x}\)，\(0\le p\le1\)。令 \(s=\sum_t x^t\) 为成功次数。

**Step 1：乘积。** \(L(p)=\prod_t p^{x^t}(1-p)^{1-x^t}=p^s(1-p)^{N-s}\)；相同底数指数相加。

**Step 2：取 log。** 对内点 \(0<p<1\)，\(\ell(p)=s\log p+(N-s)\log(1-p)\)。log 不改变最优位置，乘法也变成了加法。

**Step 3：求导。** \(\ell'(p)=s/p-(N-s)/(1-p)\)，因为 \(d\log(1-p)/dp=-1/(1-p)\)。

**Step 4：令导数为零并整理。** \(s(1-p)-(N-s)p=0\Rightarrow s-Np=0\Rightarrow\hat p=s/N=N^{-1}\sum_t x^t\)。\(\ell''(p)=-s/p^2-(N-s)/(1-p)^2\le0\)，内点驻点是最大值。若 \(s=0\) 或 \(s=N\)，最优落在边界 \(p=0\) 或 \(p=1\)，不可只依赖内点求导。

**解释。** 0/1 数据的样本平均恰好等于成功比例。\(\hat p\) 随抽到的样本改变，因而**估计量** \(\hat p(X)\) 本身也是随机变量。（PDF p.12）

### 3.3 Binomial、多类别与正态的 MLE（PDF p.13–16）

若每个 \(x^t\) 是 \(M\) 次 Bernoulli 试验的成功次数，\(x^t\sim\operatorname{Binomial}(M,p)\)，则 \(\ell(p)\) 中与 \(p\) 有关的部分是 \((\sum_t x^t)\log p+(NM-\sum_t x^t)\log(1-p)\)。同样求导得 \(\hat p=\sum_t x^t/(NM)\)：总成功数除以总试验数。组合数只由数据决定，求 \(p\) 的最大值时可作为常数略去。（PDF p.13）

多类别单次试验用 \(x_i^t\in\{0,1\}\) 表示第 \(t\) 次是否为类 \(i\)，\(\sum_i x_i^t=1\)。参数 \(p_i\ge0,\sum_i p_i=1\)，似然 \(\prod_{t,i}p_i^{x_i^t}\)。令 \(N_i=\sum_t x_i^t\)，log 似然 \(\sum_iN_i\log p_i\)。用等式约束的 Lagrangian \(\mathcal L=\sum_iN_i\log p_i+\gamma(1-\sum_i p_i)\)，对内点求导得 \(N_i/p_i-\gamma=0\)，即 \(p_i=N_i/\gamma\)；加总并用 \(\sum_iN_i=N\) 得 \(\gamma=N\)，故 \(\hat p_i=N_i/N\)。若某类从未出现，其 MLE 可在边界 \(p_i=0\)。（PDF p.14–15）

对 \(x^t\sim N(\mu,\sigma^2)\)，\(\sigma^2>0\)，正态 log 似然为

\[
\ell(\mu,\sigma^2)
=-\frac N2\log(2\pi)-\frac N2\log\sigma^2
-\frac1{2\sigma^2}\sum_t(x^t-\mu)^2.
\]

固定 \(\sigma^2\) 对 \(\mu\) 求导，得 \(\partial\ell/\partial\mu=\sigma^{-2}\sum_t(x^t-\mu)\)；令零得到 \(\hat\mu=m=N^{-1}\sum_t x^t\)。令 \(v=\sigma^2\)，则 \(\partial\ell/\partial v=-N/(2v)+\sum_t(x^t-m)^2/(2v^2)\)；令零并乘 \(2v^2\)，得 \(Nv=\sum_t(x^t-m)^2\)，故 \(\hat\sigma^2_{\rm ML}=N^{-1}\sum_t(x^t-m)^2\)。（PDF p.16）这和用于无偏样本方差的 \(1/(N-1)\) 不是同一个目标。

### 3.4 估计量如何评价？

课件把估计量写作 \(d(X)\)，真实参数为 \(\theta\)。bias（偏差）\(b(d)=E[d]-\theta\)，variance（方差）\(\operatorname{Var}(d)=E[(d-E[d])^2]\)；均方误差 \(E[(d-\theta)^2]\) 展开 \(d-\theta=(d-E[d])+(E[d]-\theta)\)，交叉项因 \(E[d-E[d]]=0\) 消失，得到 \(\operatorname{MSE}(d)=b(d)^2+\operatorname{Var}(d)\)。（PDF p.17–18）

样本均值无偏，因为 \(E[m]=N^{-1}\sum_tE[x^t]=\mu\)。若样本 i.i.d.、方差有限，\(\operatorname{Var}(m)=\sigma^2/N\to0\)，故它 consistent（一致）：样本增多时靠近真均值。（PDF p.19–20）正态方差的上述 MLE 则有 \(E[\hat\sigma^2_{\rm ML}]=(N-1)\sigma^2/N\)，偏低；可乘 \(N/(N-1)\) 得无偏估计。无偏不等于在每个样本上更接近真实值，也不自动拥有最小 MSE。

## 4. Bayesian Estimation（贝叶斯估计）（PDF p.22–28）

MLE 把 \(\theta\) 当作固定但未知的值；Bayesian approach（贝叶斯方法）用 prior density \(p(\theta)\) 表达看数据前对参数的不确定性。观察 \(X\) 后，

\[
p(\theta\mid X)=\frac{p(X\mid\theta)p(\theta)}{p(X)},
\qquad p(X)=\int p(X\mid\theta')p(\theta')\,d\theta'.
\]

分母对 \(\theta\) 归一化，\(\theta'\) 只是积分用的哑变量。（PDF p.22）若目标是预测新 \(x\)，full Bayesian prediction（完整贝叶斯预测）使用 \(p(x\mid X)=\int p(x\mid\theta)p(\theta\mid X)\,d\theta\)：把每种可能参数给出的预测按其后验权重平均。课件 p.23 的这一步用到“给定 \(\theta\) 后，旧样本 \(X\) 不再额外改变新 \(x\) 的分布”的模型条件。对函数预测也可对 \(g(x\mid\theta)\) 做相应后验平均；但非线性 \(g\) 时，\(E_\theta[g(x\mid\theta)]\) 一般不等于 \(g(x\mid E[\theta])\)。

积分有时难算，故课件区分两种点估计（PDF p.24–25）：MAP（maximum a posteriori，最大后验估计）取 \(\arg\max_\theta p(X\mid\theta)p(\theta)\)，即后验众数；在平方误差损失下，posterior mean（后验均值）\(E(\theta\mid X)\) 最小化后验平均平方误差。证明：令 \(\mu_*=E(\theta\mid X)\)，对任意常数 \(c\)，

\[
E[(\theta-c)^2\mid X]
=E[(\theta-\mu_*+\mu_*-c)^2\mid X]
=\operatorname{Var}(\theta\mid X)+(\mu_*-c)^2,
\]

交叉项为零，最小值在 \(c=\mu_*\)。所以“后验均值最好”必须附上**平方损失**条件；MAP、后验均值与完整预测不是同一个概念。平坦先验在适当条件下使 MAP 与 MLE 相同，但不意味着所有先验都能被无条件视为均匀分布。（PDF p.24–25）

### 4.1 正态先验 + 正态观测：补全平方

课件 p.26–27 假设 \(x^t\mid\theta\sim N(\theta,\sigma^2)\)、\(\theta\sim N(\mu_0,\sigma_0^2)\)，两方差已知。后验中随 \(\theta\) 变化的指数部分为

\[
-\frac1{2\sigma^2}\sum_t(x^t-\theta)^2
-\frac1{2\sigma_0^2}(\theta-\mu_0)^2.
\]

展开平方并丢掉与 \(\theta\) 无关的项，等于

\[
-\frac12\left[
\left(\frac N{\sigma^2}+\frac1{\sigma_0^2}\right)\theta^2
-2\left(\frac{\sum_t x^t}{\sigma^2}+\frac{\mu_0}{\sigma_0^2}\right)\theta
\right]+\text{const}.
\]

令 \(a=N/\sigma^2+1/\sigma_0^2\)、\(b=\sum_t x^t/\sigma^2+\mu_0/\sigma_0^2\)，则 \(a\theta^2-2b\theta=a(\theta-b/a)^2-b^2/a\)。最后一项与 \(\theta\) 无关，因此后验是正态，后验方差 \(a^{-1}\)，后验均值与众数同为

\[
\mu_*=
\frac{(N/\sigma^2)m+(1/\sigma_0^2)\mu_0}{N/\sigma^2+1/\sigma_0^2}.
\]

权重按 precision（精度，即方差的倒数）分配：样本越多，样本均值权重越大；先验越集中，\(\mu_0\) 权重越大。（PDF p.27）**数值例子：** \(\mu_0=0,\sigma_0^2=1,\sigma^2=1\)，观察 \(1,2,3\) 后 \(m=2\)、\(a=4\)，所以 MLE 为 2，后验均值与 MAP 为 \(1.5\)，后验方差 \(1/4\)。它把小样本估计向先验 0 拉回，但随着 \(N\) 增长，数据会占更大权重。

点估计压缩了整个后验，可能丢失多峰、宽度等不确定性信息；课件 p.28 提到 Monte Carlo sampling（蒙特卡洛采样）和近似积分可保留更多信息。

## 5. 单变量参数化分类（PDF p.30–36）

设第 \(i\) 类特征服从 \(N(\mu_i,\sigma_i^2)\)。承接上一讲，选择使 \(g_i(x)=\log p(x\mid C_i)+\log P(C_i)\) 最大的类别。代入正态 PDF 并删掉对所有类相同的 \(-\tfrac12\log(2\pi)\)，得到

\[
g_i(x)=-\tfrac12\log\sigma_i^2
-\frac{(x-\mu_i)^2}{2\sigma_i^2}
+\log P(C_i).
\]

训练数据给 \(\hat P(C_i)=N_i/N\)、\(m_i=N_i^{-1}\sum_t r_i^tx^t\)、\(s_i^2=N_i^{-1}\sum_t r_i^t(x^t-m_i)^2\)，再代入上式。（PDF p.30–31）若某类没有数据或估计方差为零，直接代入会失效，需更多数据或合适平滑/正则化；这是**【补充理解】**。

不同方差时 \(g_i(x)\) 对 \(x\) 是二次式，决策边界可有不止一个阈值，称 QDA（quadratic discriminant analysis，二次判别分析）。PDF p.33 的上图横轴是特征 \(x\)，纵轴是各类 likelihood；中图为 posterior，底图为条件风险，图中低置信度区按拒绝损失 \(\lambda=0.2\) 被标为 reject。它说明密度高度、后验、风险是**三个不同量**，不能只盯着上图的曲线高低。

若各类方差相同，\(-x^2/(2\sigma^2)\) 是各类共有项，可在 \(\arg\max\) 中消去，得到 linear discriminant（线性判别分数）；若先验也相同，只需选离 \(m_i\) 最近的均值，称 nearest centroid（最近类中心）。（PDF p.32）p.32 上图的两条正态密度相交处，对应下图两条后验相交处；先验相同、方差相同使阈值落在两均值中间。若先验不同，边界通常向**较少见的类的均值**移动，让较常见的类占更大区域。（PDF p.34）

**【补充理解：边界数值】** \(C_1:N(0,1),C_2:N(2,1)\)。相同先验时 \(x=1\) 是边界。若 \(P(C_1)=0.8,P(C_2)=0.2\)，对数分数差为 \(\log4+2-2x\)；令零得到 \(x=1+\tfrac12\log4\approx1.693\)，边界向较少见的 \(C_2\) 均值 2 靠近。此处 x 为一维特征，不是参数。

课件 p.34 的文字声称判别分数恒小于零，这不是一般性质；对数密度可因尺度变化取不同符号，真正重要的是各类分数的**相对大小**。p.36 提醒：若正态假设不符，估计出的阈值也可能错；这就是模型假设的实际代价。

## 6. 回归：为什么高斯噪声会导向平方损失？（PDF p.38–45）

回归假设 \(r=f(x)+\varepsilon\)，以 \(g(x\mid\theta)\) 近似 \(f\)，并假定噪声 \(\varepsilon\sim N(0,\sigma^2)\) 且与输入独立。（PDF p.38）于是 \(r^t\mid x^t,\theta\sim N(g(x^t\mid\theta),\sigma^2)\)。若输入分布 \(p(x^t)\) 不依赖 \(\theta\)，联合 log 似然的 \(\sum_t\log p(x^t)\) 对优化 \(\theta\) 是常数，可去掉。（PDF p.39–40）

每个条件正态密度取 log 后，随 \(\theta\) 变化的部分为 \(-[r^t-g(x^t\mid\theta)]^2/(2\sigma^2)\)。对 \(t\) 求和并最大化，与最小化 \(\tfrac12\sum_t[r^t-g(x^t\mid\theta)]^2\) 等价，因为 \(\sigma^2>0\) 是固定比例因子。（PDF p.41）所以“平方误差”可从高斯噪声假设推出来；若噪声模型或任务代价不同，适合的损失也可能不同。

线性回归 \(g(x)=w_0+w_1x\) 的导数为 \(\partial E/\partial w_0=-\sum_t(r^t-w_0-w_1x^t)\)、\(\partial E/\partial w_1=-\sum_t x^t(r^t-w_0-w_1x^t)\)。分别令零得

\[
\begin{bmatrix}N&\sum_t x^t\\\sum_t x^t&\sum_t(x^t)^2\end{bmatrix}
\begin{bmatrix}w_0\\w_1\end{bmatrix}
=\begin{bmatrix}\sum_t r^t\\\sum_t x^tr^t\end{bmatrix}.
\]

这是课件 p.42–43 的 \(Aw=y\)。若左矩阵可逆，可解 \(w=A^{-1}y\)。多项式回归把 \(1,x,\ldots,x^k\) 排成设计矩阵 \(D\in\mathbb R^{N\times(k+1)}\)，得到 \(D^\mathsf TD\hat w=D^\mathsf Tr\)；参数依旧线性。（PDF p.44）[Introduction](01_Introduction.md) 已从矩阵平方误差逐项推过同一正规方程。课件 p.45 还列 relative squared error、absolute error 和 \(\varepsilon\)-insensitive error；它们对大误差、尺度和小残差的处理不同，不能把“回归”与“平方损失”画等号。

## 7. Model Selection 与 bias–variance（PDF p.47–53）

模型阶数升高通常可更贴近训练集，却可能对抽样噪声更敏感。[Introduction](01_Introduction.md) 已用图展示这点；这里课件把预测误差拆开。令真实条件均值 \(f(x)=E[r\mid x]\)，对固定训练结果 \(g(x)\)，写 \(r-g(x)=(r-f(x))+(f(x)-g(x))\)。展开平方并对 \(r\mid x\) 取期望，交叉项因 \(E[r-f(x)\mid x]=0\) 消失：

\[
E[(r-g(x))^2\mid x]
=\operatorname{Var}(r\mid x)+(f(x)-g(x))^2.
\]

第一项是给定 \(x\) 后的不可约噪声；第二项是模型偏离条件均值的平方。（PDF p.48）再对可能抽到的训练集 \(X\) 取期望，令 \(\bar g(x)=E_X[g_X(x)]\)，在第二项中加减 \(\bar g(x)\)：

\[
E_X[(f(x)-g_X(x))^2]
=(f(x)-\bar g(x))^2+E_X[(g_X(x)-\bar g(x))^2].
\]

交叉项又因 \(E_X[g_X-\bar g]=0\) 消失。三项合起来是**噪声 + 平方偏差 + 方差**。（PDF p.49）模型更复杂时偏差可能下降、方差可能上升，这是课件 p.50 的学习直觉，不是对每个算法、每个数据分布都逐点严格单调的定理。

课件给出三类选择手段（PDF p.51–53）：cross-validation（交叉验证）用未参与当前拟合的数据估计泛化；regularization（正则化）在误差之外惩罚复杂度，\(\lambda\) 控制力度；Bayesian model selection（贝叶斯模型选择）给不同模型设先验 \(p(\text{model})\)，再按 \(p(\text{data}\mid\text{model})p(\text{model})\) 更新。某些正则化可解释成偏好简单参数的先验，但具体对应关系取决于损失、先验和缩放；交叉验证也不是“在所有情况下必然最好”。调参必须避免反复用最终测试集。

## 8. 多变量数据：均值、协方差与缺失值（PDF p.55–60）

对每个事件测 \(d\) 个特征，样本矩阵形状为 \(N\times d\)。（PDF p.55）真实均值 \(\mu=E[x]\in\mathbb R^d\)，真实协方差 \(\Sigma=E[(x-\mu)(x-\mu)^\mathsf T]\in\mathbb R^{d\times d}\)；\(\Sigma_{ij}=\operatorname{Cov}(x_i,x_j)\)，对角线是各特征方差。（PDF p.57–58）课件 p.58 协方差矩阵展示中的某些下标有排版错误，应以该定义及 \(\Sigma_{ii}=\sigma_i^2\) 为准。correlation（相关系数）\(\rho_{ij}=\Sigma_{ij}/(\sigma_i\sigma_j)\) 将线性关联标准化到 \([-1,1]\)；独立通常推出零相关，零相关一般不推出独立。

样本均值 \(m=N^{-1}\sum_tx^t\)，样本协方差的 ML 形式 \(S=N^{-1}\sum_t(x^t-m)(x^t-m)^\mathsf T\)，样本相关矩阵按 \(S_{ij}/(s_i s_j)\) 构造。（PDF p.59）\(S\) 必为 PSD；若 \(N\) 很小或特征冗余，\(S\) 可能不可逆，后续高斯密度的普通逆矩阵式便不能直接用。若有 missing values（缺失值），课件 p.60 比较删行、均值/众数填补、回归填补和矩阵分解；简单填补也可能改变相关性，不能把补出的值当成实测值。

## 9. 多元正态与 Mahalanobis distance（PDF p.62–68）

对 \(x,\mu\in\mathbb R^d\)，若 \(\Sigma\in\mathbb R^{d\times d}\) 正定，多元正态密度为

\[
p(x\mid\mu,\Sigma)=
\frac{1}{(2\pi)^{d/2}|\Sigma|^{1/2}}
\exp\!\left[-\tfrac12(x-\mu)^\mathsf T\Sigma^{-1}(x-\mu)\right].
\]

\(|\Sigma|\) 是行列式；\(\Sigma^{-1}\) 让不同方向按各自变异和相关性缩放。二次型 \(d_M^2=(x-\mu)^\mathsf T\Sigma^{-1}(x-\mu)\) 是 squared Mahalanobis distance（马氏距离平方），课件 p.64 有时把这整个二次型简称 distance。严格的距离是它的平方根。**【补充理解：数值】** \(\mu=(0,0)^\mathsf T\)、\(\Sigma=\operatorname{diag}(4,1)\)、\(x=(2,1)^\mathsf T\) 时，欧氏距离平方为 5，马氏距离平方为 \(2^2/4+1^2/1=2\)：第一维本来波动较大，因此偏离 2 的惩罚较轻。

课件 p.63 给多元正态 log 似然及 MLE：\(\hat\mu=m\)、\(\hat\Sigma=S\)。均值推导与一维相同：固定 \(\Sigma\) 时对 \(\mu\) 求梯度，\(\Sigma^{-1}\sum_t(x^t-\mu)=0\Rightarrow\mu=m\)；再对正定 \(\Sigma\) 优化可得以 \(1/N\) 为分母的协方差。这里需要相关逆和行列式有定义；小样本奇异协方差需另行处理。

二元正态 \(d=2\) 的等密度线是椭圆。PDF p.67 四格图横轴 \(x_1\)、纵轴 \(x_2\)：上左零协方差且两方差相等，轮廓近圆；上右零协方差但 \(x_1\) 方差较大，轮廓横向拉长；下左正协方差，主轴向右上倾斜；下右负协方差，主轴向右下倾斜。越靠内的等高线对应更高密度；图是 \(p(x)\) 的切片形状，不是决策边界。（PDF p.65–67）对**联合正态**，零协方差还可推出独立；一般分布不能这样推。（PDF p.66）

若特征在给定模型条件下独立，\(\Sigma\) 为对角矩阵，联合密度分解为各单变量密度的乘积；马氏二次型变成 \(\sum_j(x_j-\mu_j)^2/\sigma_j^2\)。若方差也全相同 \(s^2\)，它进一步成为 \(\|x-\mu\|_2^2/s^2\)。（PDF p.68）

## 10. 多变量分类：QDA、LDA 与复杂度（PDF p.70–83）

第 \(i\) 类若假设 \(x\mid C_i\sim N_d(\mu_i,\Sigma_i)\)，把密度代入 [Bayesian Decision Theory](05_Bayesian_Decision_Theory.md) 的对数判别式，去掉各类共有的 \(-\frac d2\log(2\pi)\) 后，

\[
g_i(x)=-\tfrac12\log|\Sigma_i|
-\tfrac12(x-\mu_i)^\mathsf T\Sigma_i^{-1}(x-\mu_i)
+\log P(C_i).
\]

用 \(r_i^t\) 从训练集分别估计 \(\hat P(C_i)=N_i/N\)、\(m_i=N_i^{-1}\sum_t r_i^tx^t\)、\(S_i=N_i^{-1}\sum_t r_i^t(x^t-m_i)(x^t-m_i)^\mathsf T\)。（PDF p.70–71）

### 10.1 各类有各自协方差：QDA

展开 \((x-m_i)^\mathsf TS_i^{-1}(x-m_i)\) 可得 \(x^\mathsf TS_i^{-1}x-2x^\mathsf TS_i^{-1}m_i+m_i^\mathsf TS_i^{-1}m_i\)；由于 \(S_i^{-1}\) 随类变化，二次项不能从类别比较中消去。故 \(g_i(x)=x^\mathsf TW_i x+w_i^\mathsf Tx+w_{i0}\)，其中 \(W_i=-S_i^{-1}/2\)、\(w_i=S_i^{-1}m_i\)、\(w_{i0}=-m_i^\mathsf TS_i^{-1}m_i/2-\log|S_i|/2+\log\hat P(C_i)\)。这是 QDA；类间决策边界一般为二次曲面。（PDF p.72）

PDF p.73 上图是两个二维类条件密度峰，中图是由它们合成的后验曲面，底图把椭圆等密度线与弯曲决策边界画在 \((x_1,x_2)\) 平面上；边界弯曲来自两类不同的 \(S_i\)，不是因为原始特征本身带有平方。p.74 指出协方差要估 \(K d(d+1)/2\) 个独立数，再加 \(Kd\) 个均值分量；\(d\) 大而每类样本少时容易不稳定。

### 10.2 共享协方差：LDA

若所有类共享 \(S\)，可用 \(S=\sum_i\hat P(C_i)S_i\) 进行 pooled estimate（合并估计）。（PDF p.75）此时各类分数中的 \(-x^\mathsf TS^{-1}x/2\) 与 \(-\log|S|/2\) 是共同项，可去掉，留下

\[
g_i(x)=w_i^\mathsf T x+w_{i0},
\quad w_i=S^{-1}m_i,
\quad w_{i0}=-\tfrac12m_i^\mathsf TS^{-1}m_i+\log\hat P(C_i).
\]

这就是 LDA（linear discriminant analysis，线性判别分析）。两类交界由 \(g_i(x)=g_j(x)\) 给出，即 \((w_i-w_j)^\mathsf T x+w_{i0}-w_{j0}=0\)，是超平面。（PDF p.75–76）PDF p.77 的椭圆仍表示两类各自的等密度线，斜直线才是分界；共享协方差使分数之差为线性，所以各类区域由线性不等式交集构成，因而为凸区域。等先验时选择马氏距离 \((x-m_i)^\mathsf TS^{-1}(x-m_i)\) 最近的类；不等先验会把边界推向先验较小的一类。（PDF p.76）

### 10.3 对角与球形假设

若共享 \(S\) 还是对角矩阵，特征在**每类条件正态模型下**独立，分数按各维的加权平方距离相加；每维权重为方差倒数。若更强地假定 \(S=s^2I\)，各维同尺度，等先验下便成为普通 Euclidean nearest-mean classifier（欧氏最近均值分类器）。（PDF p.78–81）PDF p.79、81 的图用于对比不同协方差限制下的分界形状；p.83 用多类密度峰和投影到特征平面的区域说明：每个类的等密度椭圆与最终决策区域并非同一种几何对象。

课件 p.82 按共享球形、共享对角、共享完整、各类完整排列协方差复杂度：分别需要 \(1,d,d(d+1)/2,Kd(d+1)/2\) 个协方差参数；各情形还需估类均值与先验。假设越弱，表达能力越大，但对数据量的要求通常越高。这个计数解释了为什么“小样本高维”时更愿意共享、对角化或正则化协方差，而不是机械地选最复杂 QDA。

## 11. Discrete Features（离散特征）（PDF p.85–86）

对二值特征 \(x_j\in\{0,1\}\)，定义 \(p_{ij}=P(x_j=1\mid C_i)\)。若给定类别后各维条件独立，则

\[
p(x\mid C_i)=\prod_{j=1}^{d}p_{ij}^{x_j}(1-p_{ij})^{1-x_j},
\quad
g_i(x)=\log P(C_i)+\sum_j[x_j\log p_{ij}+(1-x_j)\log(1-p_{ij})].
\]

展开每项得 \(x_j\log[p_{ij}/(1-p_{ij})]+\log(1-p_{ij})\)，所以对二值输入 \(x\)，\(g_i(x)\) 是线性的。ML 估计 \(\hat p_{ij}=\sum_t r_i^t x_j^t/N_i\)：第 \(i\) 类中该特征为 1 的比例。（PDF p.85）若样本里某事件没出现，MLE 为零会使 log 为 \(-\infty\)；可用平滑先验处理，但这是**【补充理解】**，须与课件原推导分开。

若第 \(j\) 个特征有 \(n_j\) 个可能取值 \(v_1,\ldots,v_{n_j}\)，设 \(z_{jk}=\mathbf1[x_j=v_k]\)、\(p_{ijk}=P(x_j=v_k\mid C_i)\)，则 \(p(x\mid C_i)=\prod_{j,k}p_{ijk}^{z_{jk}}\)，对数判别式 \(g_i(x)=\log P(C_i)+\sum_{j,k}z_{jk}\log p_{ijk}\)，估计量 \(\hat p_{ijk}=\sum_t r_i^t z_{jk}^t/N_i\)。（PDF p.86）这是把多类别特征编码成指示变量后的同一计数思想。

## 12. 多特征回归与 basis functions（PDF p.88–90）

课件将多个输入特征的一维数值输出写作 \(g(x\mid w)=w_0+\sum_{j=1}^{d}w_jx_j\)。令设计矩阵 \(X\in\mathbb R^{N\times(d+1)}\) 的第 \(t\) 行为 \((1,x_1^t,\ldots,x_d^t)\)，\(w\in\mathbb R^{d+1}\)、\(r\in\mathbb R^N\)；最小平方误差 \(E(w)=\tfrac12\|Xw-r\|_2^2\)。链式/矩阵求导给 \(\nabla E=X^\mathsf T(Xw-r)\)，令零得 \(X^\mathsf TX\hat w=X^\mathsf Tr\)；仅当 \(X^\mathsf TX\) 可逆时，课件 p.89 的逆矩阵表达式才可用。

课件 p.88 特别说明：统计文献通常称“多个输入、一个输出”为 **multiple linear regression**；*multivariate regression* 常指多个输出，术语不要只凭字面猜。若需要非线性输入关系，可新增 \(x_1^2,x_2^2,x_1x_2\)，甚至 \(\sin x_1\) 等 basis functions（基函数）形成新特征 \(z\)，再对新特征使用线性参数模型。（PDF p.90）这再次呼应 [Introduction](01_Introduction.md)：对原始 \(x\) 非线性，并不排斥对参数 \(w\) 线性。

## 13. 容易混淆的概念与常见错误

| A 与 B | 核心差别 | 检查方法 |
|---|---|---|
| probability 与 likelihood | 固定参数看可能数据 / 固定数据比较参数 | 问“现在谁是变量？” |
| MLE 与 MAP | 只最大化数据似然 / 再乘参数先验 | 写出优化目标。 |
| MAP 与 posterior mean | 后验众数 / 后验期望 | 偏斜或多峰后验中通常不同。 |
| 点估计 与 full Bayesian prediction | 只用一个参数 / 对整个后验积分 | 是否保留参数不确定性？ |
| ML 方差 与无偏样本方差 | 分母 \(N\) / 分母 \(N-1\) | 明确目标是似然还是无偏。 |
| estimator bias 与模型预测 bias | 参数估计量均值偏离真参数 / 多次训练平均预测偏离真函数 | 看 \(\theta\) 还是 \(f(x)\)。 |
| QDA 与 LDA | 各类独立协方差 / 各类共享协方差 | 二次项是否能从类间比较中消去？ |
| zero covariance 与 independence | 无线性关联 / 完全分解的联合分布 | 仅联合正态等特例可反推。 |
| covariance matrix 与 scale matrix | 正态模型中相同 / t 模型中通常有系数差 | 查看分布与自由度。 |

课件 p.30–34 的单变量高斯分数应从正态密度重新推：\(-\frac12\log\sigma_i^2\) 与 \(-\frac{(x-\mu_i)^2}{2\sigma_i^2}\) 同时出现；不要因个别幻灯片简写就漏掉 \(1/2\)。课件 p.58、65 的协方差矩阵图有下标排版问题，始终以 \(\Sigma_{ii}=\sigma_i^2\)、\(\Sigma_{ij}=\Sigma_{ji}\) 为准。PDF p.50 对模型复杂度与偏差/方差的方向性描述是常见教学图景，不应当作对所有数据分布严格单调的定理。

## 14. English Terminology

| English | 中文 | 一句话理解 |
|---|---|---|
| parametric / nonparametric | 参数化 / 非参数化 | 先选有限维分布族 / 不先限定同样形式。 |
| generative classifier | 生成式分类器 | 建模类先验和类条件数据分布。 |
| likelihood / log likelihood | 似然 / 对数似然 | 已见数据下比较参数 / 把乘积变成和。 |
| Maximum Likelihood Estimation (MLE) | 最大似然估计 | 找使已见数据最可能的参数。 |
| Bayesian Estimation / prior / posterior | 贝叶斯估计 / 先验 / 后验 | 把参数不确定性与数据合并更新。 |
| Maximum a posteriori (MAP) | 最大后验估计 | 选后验密度最高的参数点。 |
| posterior mean / predictive distribution | 后验均值 / 预测分布 | 参数的后验平均 / 对不确定参数积分后的新数据分布。 |
| bias / variance / consistency | 偏差 / 方差 / 一致性 | 系统偏离 / 抽样波动 / 样本增大时趋近真值。 |
| Gaussian / covariance / Mahalanobis distance | 正态 / 协方差 / 马氏距离 | 常用连续分布 / 联合波动 / 按波动结构标准化的距离。 |
| quadratic / linear discriminant analysis (QDA/LDA) | 二次 / 线性判别分析 | 各类协方差不同 / 共享协方差。 |
| homoscedasticity / heteroscedasticity | 同方差 / 异方差 | 类间共享协方差 / 各类不同协方差。 |
| basis function | 基函数 | 把原始输入变成可供线性参数模型使用的新特征。 |

*Likelihood* 的词义提醒你“给定这些数据，哪组参数更合理”；*posterior* 提醒“在数据之后”。但记忆词义不能代替分清究竟是 \(p(x\mid\theta)\) 还是 \(p(\theta\mid x)\)。

## 15. 整讲知识地图

```text
Bayes 决策需要 P(C_i)、p(x|C_i)
                  ↓
       假设参数化分布 p(x|θ)
                  ↓
       数据 X → MLE 或参数后验
                  ↓
   单变量分类 / 高斯噪声回归 / 模型选择
                  ↓
       多变量均值、协方差与正态密度
                  ↓
     QDA → 共享协方差 LDA → 对角/球形模型
                  ↓
     离散特征模型 / 多特征回归 / 基函数
                  ↓
       用独立数据检查估计与泛化
```

## 16. 自测：分三轮完成

**第一轮，估计基础。**

1. \(x^t\in\{0,1\}\) 为 i.i.d. Bernoulli 时，为什么 likelihood 是乘积？为什么取 log 不改 \(\arg\max\)？
2. 若 5 次试验结果为 \(1,0,1,1,0\)，\(\hat p_{\rm ML}\) 是多少？若五次全为零，为什么不能机械令导数为零？
3. 为什么正态方差的 MLE 分母是 \(N\)，而无偏估计常用 \(N-1\)？
4. MAP、后验均值和完整贝叶斯预测分别保留多少参数不确定性？
5. 正态先验数值例子里，若样本数持续增加而均值保持 2，后验均值将靠近多少？

**第二轮，分类与回归。**

6. 正态噪声怎样一步步把最大似然变成最小平方误差？若输入分布依赖 \(\theta\)，还能随意忽略 \(\sum_t\log p(x^t\mid\theta)\) 吗？
7. 两类高斯拥有不同协方差时，为何一般是二次边界？共享协方差时哪一项消失？
8. 如果特征维度很高、每类样本很少，QDA 为什么尤其容易出问题？
9. Bernoulli 特征的 \(p_{ij}\) 如何从第 \(i\) 类训练样本估计？为什么零频数会影响对数判别式？
10. 多特征回归的 \(X\) 若有 \(N\) 个样本、\(d\) 个原始特征且包含截距，\(X\)、\(w\)、\(r\) 形状各是什么？

**第三轮，贯通。**

11. \(\Sigma=\operatorname{diag}(4,1)\) 时，偏离第一维 2 与偏离第二维 1 对马氏距离平方各贡献多少？
12. 为什么 \(\operatorname{Cov}(X_1,X_2)=0\) 在一般情况下不能推出独立？
13. “模型更复杂必定更好”和“验证集上的最优模型必定在未来最优”各漏了什么条件？

<details><summary>展开自测要点</summary>

1. 给定参数后条件独立使联合密度分解；log 严格递增。2. \(3/5\)；全零时最优在边界 0。3. 两者优化目标不同；前者有有限样本向下偏差。4. MAP 与均值都压缩成一点，完整预测对后验积分。5. 趋近 2。6. 正态 log 密度的参数相关项是负的残差平方；若 \(p(x\mid\theta)\) 依赖 \(\theta\)，不能忽略。7. 各类的 \(x^\mathsf T\Sigma_i^{-1}x\) 不同；共享时为共同项。8. 每类协方差需估 \(d(d+1)/2\) 个独立数，还可能奇异。9. 类内该特征为 1 的比例；零概率取 log 导致 \(-\infty\)。10. \(N\times(d+1)\)、\((d+1)\times1\)、\(N\times1\)。11. 各为 1。12. 零协方差只排除了线性关联。13. 前者忽略估计方差与过拟合，后者忽略验证集有限、数据分布变化等不确定性。

</details>
