# 04 · Mathematical Foundations: Optimization Primer（优化基础）

> 主来源：[Optimization_Primer.pdf](../Optimization_Primer.pdf)，页码从封面起算。这里补出的数值例子与严格条件标 **【补充理解】**。

## 0. 这节课到底在解决什么问题？

一旦选定模型与损失，训练就变成“在允许的参数中找使目标最小的那个”。例如最小二乘找系数，分类器可能还要求某些间隔不低于阈值。optimization（优化）把“越好”写成目标函数，把“必须满足”写成约束，再研究怎样找到答案、怎样确认答案足够好。（PDF p.2）

本讲有两条相连的路线。第一条用 gradient（梯度）和 convexity（凸性）理解如何找最小值；第二条用 Lagrangian（拉格朗日函数）和 dual problem（对偶问题）为受约束问题构造下界与最优性检查。后续 SVM 和模型训练都需要这种语言。

## 1. 前置知识与记号

需会 [Linear Algebra](02_Linear_Algebra.md) 的向量、梯度与 PSD，以及单变量求导。决策变量 \(x\in\mathbb R^n\)，目标 \(f_0(x)\in\mathbb R\)；不等式约束 \(f_i(x)\le0\)，共 \(m\) 个；等式约束 \(h_j(x)=0\)，共 \(p\) 个。这里的 \(x\) 是**待优化变量**，在机器学习里常相当于参数 \(w\) 或 \(\theta\)，不一定是样本输入。（PDF p.2）

## 2. 核心直觉：约束是门槛，对偶给可核验的下界

设你想把模型损失降到最低，但某个参数必须不超过上限。unconstrained minimum（无约束最小值）可能在门槛外，于是最佳可行解被边界挡住。active constraint（活跃约束）在解处恰好取等号；不活跃约束留有余量。（PDF p.3）

**【补充理解：影子价格类比】** Lagrange multiplier（拉格朗日乘子）\(\lambda_i\) 像“放宽第 \(i\) 个门槛一小点能换来多少目标改善”的局部价格。类比成立于合适的最优性、可微和敏感性条件；\(\lambda_i\) 不是对所有违反约束的点直接收取的一笔真实费用。课件 p.4 把它直观称为违约代价。

对偶函数 \(g(\lambda)\) 给原问题最优值的一个下界；把 \(\lambda\) 调好，就是寻找最紧的可证明下界。若手里同时有一个可行解的目标值（上界）和对偶下界，就知道真正最优值被夹在哪个区间。（PDF p.5–10）

## 3. 正式定义：原问题、对偶与凸性

原问题（primal problem）：\(\min_x f_0(x)\)，使 \(f_i(x)\le0\)、\(h_j(x)=0\)。最优值记 \(p^*\)。只考虑不等式时，Lagrangian 为

\[
L(x,\lambda)=f_0(x)+\sum_{i=1}^{m}\lambda_i f_i(x),
\quad \lambda_i\ge0.
\]

这里 \(\lambda\in\mathbb R^m\)。固定 \(\lambda\) 后，让 \(x\) 自由变化并取下确界（infimum），得 dual function（对偶函数）\(g(\lambda)=\inf_x L(x,\lambda)\)。它可能是 \(-\infty\)。（PDF p.4–5）对偶问题是 \(\max_{\lambda\ge0}g(\lambda)\)，最优值记 \(d^*\)。总有 weak duality（弱对偶）\(d^*\le p^*\)；二者差值是 optimal duality gap（最优对偶间隙）。（PDF p.7–8）

等式约束加入 \(\sum_j\nu_jh_j(x)\)，\(\nu_j\in\mathbb R\) **没有符号限制**；不等式乘子仍须非负。（PDF p.13–15）

convex set（凸集）要求集合内任意两点的连线仍在集合内；convex function（凸函数）要求 \(f(\theta x+(1-\theta)y)\le\theta f(x)+(1-\theta)f(y)\)，其中 \(0\le\theta\le1\)。在凸集合上最小化凸函数构成 convex optimization（凸优化）；约束表述中，凸函数的 sublevel set \(\{x:f_i(x)\le0\}\) 是凸集，等式约束须为仿射式以保持可行域凸。（PDF p.16–17）

对可微凸函数，一阶条件是 \(f(y)\ge f(x)+\nabla f(x)^\mathsf T(y-x)\)：函数图像位于任一点的切平面之上。二次可微时，可在凸定义域内用 Hessian PSD 检验凸性。Jensen's inequality（Jensen 不等式）\(f(E[X])\le E[f(X)]\) 也是同一几何思想。课件还说明：对一组关于 \(x\) 凸的函数取逐点上确界，结果仍凸。（PDF p.18）

## 4. 数学推导：为何对偶函数一定给下界？

**推导目标。** 证明任意 \(\lambda\ge0\) 的 \(g(\lambda)\) 不会超过任何原问题可行点的 \(f_0(x)\)。

**已知条件。** 原问题可行点 \(x\) 满足 \(f_i(x)\le0\)；乘子 \(\lambda_i\ge0\)，所以每项 \(\lambda_i f_i(x)\le0\)。

**Step 1：加入非正项。** \(L(x,\lambda)=f_0(x)+\sum_i\lambda_i f_i(x)\le f_0(x)\)，因为加上的每项都非正。

**Step 2：取所有 \(z\) 中最小的 Lagrangian。** 按 infimum 定义，\(g(\lambda)=\inf_z L(z,\lambda)\le L(x,\lambda)\)。

**Step 3：合并。** 对任何可行 \(x\)，\(g(\lambda)\le L(x,\lambda)\le f_0(x)\)。再对右端所有可行 \(x\) 取最小值，\(g(\lambda)\le p^*\)；最后对所有对偶可行 \(\lambda\) 取最大值，\(d^*\le p^*\)。（PDF p.6–8）

这就是为何需要对偶问题：它不仅可能使求解更方便，还给出了可检验的**最优值下界**。在算法第 \(k\) 次迭代若同时有原问题可行 \(x^{(k)}\) 和对偶可行 \(\lambda^{(k)}\)，便有 \(p^*\in[g(\lambda^{(k)}),f_0(x^{(k)})]\)；区间够窄即可作为停止依据。（PDF p.10）

### 4.1 为什么对偶函数是凹的？

固定 \(x\) 时，\(L(x,\lambda,\nu)\) 是关于乘子 \((\lambda,\nu)\) 的仿射函数。\(g(\lambda,\nu)=\inf_xL(x,\lambda,\nu)\) 是这些仿射函数的逐点下确界，故为 concave（凹函数）；即使原问题非凸，这个结论仍成立。因此最大化凹的对偶函数、限制 \(\lambda\ge0\) 是一个凸优化形式。（PDF p.21）

## 5. Numerical Example：一维问题把对偶和 KKT 算到底

**【补充理解】** 考虑 \(\min_x(x-2)^2\)，约束 \(x\le1\)。无约束最小值在 \(x=2\)，不可行；在 \(( -\infty,1]\) 上最优 \(x^*=1\)，目标 \(p^*=1\)。把约束写为 \(f_1(x)=x-1\le0\)：

\[
L(x,\lambda)=(x-2)^2+\lambda(x-1),\quad \lambda\ge0.
\]

固定 \(\lambda\)，对 \(x\) 求导得 \(2(x-2)+\lambda=0\)，所以 \(x=2-\lambda/2\) 是 \(L\) 的最小点；代回并逐项合并，

\[
g(\lambda)=(-\lambda/2)^2+\lambda(1-\lambda/2)
=\lambda-\lambda^2/4.
\]

对 \(\lambda\ge0\) 最大化：\(g'(\lambda)=1-\lambda/2=0\Rightarrow\lambda^*=2\)；\(g''=-1/2<0\)，所以达到最大值 \(d^*=g(2)=1=p^*\)。这例子具有 strong duality（强对偶）。\(\lambda^*=2\) 的“价格”直觉也可检查：若放宽为 \(x\le1+\delta\) 且 \(0\le\delta<1\)，新最优值为 \((1-\delta)^2=1-2\delta+\delta^2\)，小幅放宽使目标约下降 \(2\delta\)。

## 6. 互补松弛与 KKT：怎样检验候选解？

若最优原、对偶解之间没有间隙，则课件 p.11 给 complementary slackness（互补松弛）\(\lambda_i^*f_i(x^*)=0\)。推导理由是：对可行 \(x^*\)，每项 \(\lambda_i^*f_i(x^*)\le0\)；零对偶间隙迫使这些项之和为零，因此每项都必须为零。约束若有余量 \(f_i(x^*)<0\)，则 \(\lambda_i^*=0\)；乘子若大于零，约束必活跃。

对可微问题，在课件设定的最优、零对偶间隙条件下，KKT（Karush–Kuhn–Tucker）条件包含四项（PDF p.12、15）：

1. **primal feasibility**：\(f_i(x^*)\le0\)，\(h_j(x^*)=0\)。
2. **dual feasibility**：\(\lambda_i^*\ge0\)，等式乘子 \(\nu_j^*\) 不限符号。
3. **complementary slackness**：\(\lambda_i^*f_i(x^*)=0\)。
4. **stationarity**：\(\nabla f_0(x^*)+\sum_i\lambda_i^*\nabla f_i(x^*)+\sum_j\nu_j^*\nabla h_j(x^*)=0\)。

在上一例中，\(x^*=1\)、\(\lambda^*=2\) 满足 \(1-1=0\)、\(\lambda^*\ge0\)、\(2(1-1)=0\)、\(2(1-2)+2=0\)。KKT 条件不是脱离前提的魔法清单；“凸”本身也不保证所有问题强对偶，仍需合适的约束资格条件，例如 Slater 条件。课件 p.8、14 用“通常”描述强对偶，不能删去这个限定。

## 7. 其他课件主题：LP、QP、局部方法与计算代价

linear programming, LP（线性规划）有仿射目标与仿射约束。课件 p.5、9 从 \(\min c^\mathsf T x\) 且 \(Ax\le b\) 推出对偶：\(\max_{\lambda\ge0}-b^\mathsf T\lambda\)，使 \(A^\mathsf T\lambda+c=0\)。原因是 \(L(x,\lambda)=(c+A^\mathsf T\lambda)^\mathsf T x-b^\mathsf T\lambda\)；若线性项系数非零，令 \(x\) 沿负方向无限移动便使 infimum 为 \(-\infty\)；唯有系数为零才得到有限值 \(-b^\mathsf T\lambda\)。

quadratic programming, QP（二次规划）目标可写成 \(\tfrac12x^\mathsf T Gx+c^\mathsf T x\)，配以仿射约束；若对称部分 \(G\) 为 PSD，则目标凸。（PDF p.20）LP 与 QP 是标准问题形式，许多模型训练可落入其中。课件 p.19 提及 LP 求解器。

凸问题的每个局部最小值也是全局最小值，但不保证能零成本找到；迭代、内存和算术运算仍要计算。（PDF p.22）非凸问题往往采用 local optimization（局部优化），但“非凸”本身不意味着每一个实例都 NP-hard，也不能保证从任意初值收敛到“最近的局部最小值”。课件 p.23–24 的这些话应理解为提示一般困难，而非对所有非凸函数的严格定理。

gradient descent（梯度下降）对可微目标按 \(x^{(t)}=x^{(t-1)}-\eta^{(t)}\nabla f(x^{(t-1)})\) 更新，其中 \(\eta^{(t)}>0\) 是 step size（步长）。（PDF p.24）**【补充理解】** 对 \(f(x)=(x-2)^2\)、\(x^{(0)}=0\)、\(\eta=1/4\)，因梯度 \(2(x-2)\)，有 \(x^{(1)}=1\)、\(x^{(2)}=1.5\)，逐步靠近 2。步长太大也可能振荡或发散。数值停止通常检查 \(\|\nabla f(x)\|\le\varepsilon\)，不是直接把向量写作“\(\nabla f\le\varepsilon\)”；梯度小也不总能证明全局最优。课件 p.25 还区分枚举、直接和迭代方法，并以迭代次数及每次运算量衡量效率。

## 8. 易混淆概念

| 概念 | 区别或条件 |
|---|---|
| feasible point 与 optimal point | 可行仅满足约束；最优还要在可行域内达到最低目标。 |
| active constraint 与 violated constraint | 活跃表示 \(f_i=0\)，违反表示 \(f_i>0\)；不是一回事。 |
| primal value 与 dual value | 可行原值给上界；对偶值给下界。 |
| weak 与 strong duality | 弱对偶始终 \(d^*\le p^*\)；强对偶要求差为零及相应条件。 |
| local 与 global minimum | 前者只在附近最低；凸问题下局部最低才自动是全局最低。 |
| gradient 与 step size | 一个给方向，一个决定更新距离。 |

## 9. English Terminology

| English | 中文 | 一句话理解 |
|---|---|---|
| objective / constraint | 目标 / 约束 | 要优化什么 / 哪些解允许。 |
| feasible / active | 可行 / 活跃 | 满足约束 / 某约束恰好取等号。 |
| Lagrangian / multiplier | 拉格朗日函数 / 乘子 | 把目标与约束合并 / 给约束赋权。 |
| primal / dual problem | 原问题 / 对偶问题 | 原始求解 / 寻找最紧的下界。 |
| duality gap | 对偶间隙 | 可行原值或最优原值与对偶下界之差。 |
| complementary slackness | 互补松弛 | 有余量的约束对应零乘子。 |
| KKT conditions | KKT 条件 | 可行、乘子、互补与驻点的联合检查。 |
| convexity / gradient descent | 凸性 / 梯度下降 | 保证局部最小即全局最小的结构 / 沿负梯度更新。 |

*Dual* 意为“对应的另一面”：它把原问题转成寻找最优下界的问题；名称本身不意味着两个最优值总相等。

## 10. 本节知识地图

```text
训练目标 + 约束 → 原问题 → Lagrangian → 对偶下界
                         ↓              ↓
                   凸性与可微性 → KKT / 最优性证据
                         ↓
                   梯度下降或标准求解器
```

## 11. 自测

1. 为什么 \(f_i(x)\le0\)、\(\lambda_i\ge0\) 能让 \(g(\lambda)\) 成为下界？
2. 上述一维例子里，为什么 \(\lambda^*=2\) 而不是 0？
3. 一个约束在最优点严格不等号成立，互补松弛对对应乘子有什么要求？反过来 \(\lambda_i=0\) 是否必然表示约束不活跃？
4. 等式乘子 \(\nu_j\) 为什么不要求非负？
5. \(g(\lambda)\) 可能为 \(-\infty\) 是什么意思？用 LP 的线性项解释。
6. 为什么 \(\tfrac12x^\mathsf T Gx+c^\mathsf T x\) 在 \(G\) PSD 时是凸的？
7. 只知道梯度等于零，能否宣布求得全局最小值？还要检查什么？
8. 训练中同时得到原问题可行值 12、对偶可行值 11.8，真正最优值在哪个区间？

<details><summary>展开答案要点</summary>

1. \(L(x,\lambda)\le f_0(x)\)，而 \(g=\inf_zL(z,\lambda)\le L(x,\lambda)\)。2. 最大化 \(g(\lambda)=\lambda-\lambda^2/4\) 得 2，且边界约束在最优解处起作用。3. 乘子必须为零；反向不一定，活跃约束可对应零乘子。4. 等式在可行点为零，乘任何实数仍不改变下界论证。5. 固定乘子后，Lagrangian 沿某方向可无限下降。6. Hessian 为 \(G\)（或其对称部分），PSD。7. 不能；可能是鞍点或局部极值，还需凸性、边界与可行性等条件。8. \([11.8,12]\)。

</details>
