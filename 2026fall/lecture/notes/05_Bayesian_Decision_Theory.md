# 05 · Bayesian Decision Theory（贝叶斯决策理论）

> 主来源：[Bayesian_Decision_Theory.pdf](../Bayesian_Decision_Theory.pdf)，页码从封面起算。**【补充理解】** 标记课件未给出的展开或数值例子。

## 0. 这节课到底在解决什么问题？

一个信贷申请人可能属于 low risk 或 high risk。若一无所知，只能按两类总体比例猜；若知道其收入和储蓄，就应更新判断。但“哪类更可能”仍不一定等于“应该采取什么行动”：若两种错误造成的损失不同，决定要看代价，而不只看概率。本课件按 **inference → posterior → decision → loss/risk → discriminant function** 的顺序解决这些问题。（PDF p.4–23）

读完后应能从 [Probability and Statistics](03_Probability_Statistics.md) 的 Bayes' rule 推出多类别后验，在 0–1 loss 下证明最大后验规则，用损失矩阵计算更一般的条件风险，并把同一决策写成判别函数。

## 1. 前置知识、对象与记号

假设 \(K\) 个类别 \(C_1,\ldots,C_K\) 互斥且穷尽。输入随机向量 \(X\in\mathbb R^d\)，观测值 \(x\in\mathbb R^d\)；课件信贷例子的 \(d=2\)，两项特征分别为收入与储蓄。\(P(C_i)\) 是在看此人的 \(x\) **之前**的类别 prior probability（先验概率）；\(P(C_i\mid x)\) 是看完之后的 posterior probability（后验概率）；\(p(x\mid C_i)\) 是 class-conditional density（类条件密度）。若特征连续，\(p(x\mid C_i)\) 是密度值，不是单一点的概率。（PDF p.7–12）

行动 \(\alpha_i\) 表示“判成 \(C_i\)”，\(\lambda_{ik}\) 表示采取 \(\alpha_i\) 但真实类别是 \(C_k\) 的 loss（损失）。注意损失矩阵的第一个下标是**行动**，第二个是真实状态。（PDF p.15）

## 2. 核心直觉：为何一个概念引出下一个？

课件先用抛硬币区分 **estimation（估计）** 和 **prediction（预测）**：估计未知正面概率 \(p_0\)，再用它判断下一次更可能是哪面。样本中正面的比例 \(\hat p_0=\#\text{heads}/\#\text{tosses}\) 是估计值；若两种猜错的代价相同，猜更可能的一面可使错误概率最低。（PDF p.5–6）

信贷分类若只看总体比例，每个顾客都会被判为同一类，完全没利用个人信息。（PDF p.7）因此观察 \(x=(\text{income},\text{savings})^\mathsf T\)，用它更新 \(P(C_i\mid x)\)。（PDF p.9–10）后验让我们知道“更像哪一类”；损失函数进一步告诉我们“哪种决定更合算”。最后判别函数把比较后验或风险写成便于计算的分数。（PDF p.15–23）

**【补充理解：审阅资料类比】** 类别先验是看申请材料前对总体的认识；\(x\) 是新材料；\(p(x\mid C_i)\) 衡量若 \(C_i\) 成立，这份材料有多常见；后验是看过材料后的概率判断；损失矩阵则说明不同决定的代价。类比不能推出这些概率已知或不会随时间改变；现实中它们还得从样本估计，正是下一讲的主题。

## 3. 正式定义：从 Bayes' rule 到最小错误率

对任意观测 \(x\)，全概率给出 \(p(x)=\sum_{k=1}^{K}p(x\mid C_k)P(C_k)\)。于是

\[
P(C_i\mid x)=\frac{p(x\mid C_i)P(C_i)}{\sum_{k=1}^{K}p(x\mid C_k)P(C_k)}.
\]

分子是该类的“类条件密度 × 先验”；分母把各类贡献加起来，称 evidence（证据或边缘密度），且对给定 \(x\) 不依赖候选类别 \(i\)。（PDF p.11–12）若各类的 \(p(x\mid C_i)\) 完全相同，选择仅由先验决定；若先验相同，选择仅由类条件密度决定。（PDF p.12）

在错误代价相同的情形，maximum posterior probability（最大后验概率）规则选择 \(i^*=\arg\max_iP(C_i\mid x)\)。为什么？若选择 \(C_i\)，只有真实类恰好为 \(C_i\) 才正确，所以条件正确概率是 \(P(C_i\mid x)\)，条件错误概率是 \(1-P(C_i\mid x)\)。要把后者最小，就把前者最大。（PDF p.10、12）二分类时若类别后验之和为 1，\(P(C_1\mid x)>0.5\) 等价于 \(P(C_1\mid x)>P(C_0\mid x)\)；多类别时不能把每类都与 0.5 比。

课件还给 naive Bayes（朴素贝叶斯）：若各特征 \(X_j\) **在给定类别 \(C_i\) 后相互独立**，则 \(p(x\mid C_i)=\prod_jp(x_j\mid C_i)\)。（PDF p.13）这里是 conditional independence（条件独立），不要求不同特征在总体上独立；“naive”指这一简化假设可能过强。

## 4. 数学推导：从 loss 到 risk，再回到最大后验

### 4.1 为什么仅比较后验还不够？

给定 \(x\) 并采取行动 \(\alpha_i\) 时，真实类仍可能是任意 \(C_k\)。每种情况的代价 \(\lambda_{ik}\) 应按其后验概率加权，故 conditional risk（条件风险）定义为

\[
R(\alpha_i\mid x)=\sum_{k=1}^{K}\lambda_{ik}P(C_k\mid x).
\]

决策目标是 \(i^*=\arg\min_iR(\alpha_i\mid x)\)。（PDF p.15）该式和期望的定义完全相同：固定行动，随机的是未知真实类别。所谓 Bayes' decision rule（贝叶斯决策规则）在此是使条件风险最小的规则。

### 4.2 0–1 loss 为什么退化为最大后验？

课件 p.16 设 \(\lambda_{ik}=0\) 当 \(i=k\)，否则为 1。逐项代入：

\[
R(\alpha_i\mid x)
=0\cdot P(C_i\mid x)+\sum_{k\ne i}1\cdot P(C_k\mid x)
=\sum_{k\ne i}P(C_k\mid x)
=1-P(C_i\mid x).
\]

最后一步因为全部类别后验之和为 1。\(1-P(C_i\mid x)\) 关于 \(i\) 最小时，\(P(C_i\mid x)\) 最大；所以最大后验规则是**等价结论**，不是另一条凭空出现的规则。若损失不等，不能再直接使用这个等价。

### 4.3 拒绝选项为何需要阈值？

课件 p.17–18 加入 reject action（拒绝作答）\(\alpha_{K+1}\)，每次拒绝付固定损失 \(\lambda\in(0,1)\)。在 0–1 分类损失下，判成最可能类别的最小风险是 \(1-\max_iP(C_i\mid x)\)，拒绝风险为 \(\lambda\)。因此只有

\[
1-\max_iP(C_i\mid x)<\lambda
\quad\Longleftrightarrow\quad
\max_iP(C_i\mid x)>1-\lambda
\]

才选择类别，否则拒绝。若恰好相等，课件规则把它归入拒绝；实际应用可另定平局规则。\(\lambda=0\) 时拒绝无代价，\(\lambda\ge1\) 时拒绝通常不再有价值。（PDF p.18）

## 5. Numerical Example：同一后验，不同损失，决定不同

**【补充理解】** 假设高风险 \(C_H\) 的先验为 0.1，低风险 \(C_L\) 为 0.9；观察到特征 \(x\) 的类条件密度分别为 \(p(x\mid C_H)=0.6\)、\(p(x\mid C_L)=0.2\)。这里为演示计算而给数值；若把它们看作连续密度，数值本身不是点概率。

先算证据 \(p(x)=0.6\times0.1+0.2\times0.9=0.24\)。再算 \(P(C_H\mid x)=0.06/0.24=0.25\)，\(P(C_L\mid x)=0.75\)。按 0–1 loss，判 \(C_L\) 的风险是 0.25，判 \(C_H\) 的风险是 0.75，因此选 \(C_L\)。

现在设“把高风险误判为低风险”的损失为 5，“把低风险误判为高风险”的损失为 1，正确判定损失为 0。判 \(C_L\) 时风险 \(R(\alpha_L\mid x)=5\times0.25=1.25\)；判 \(C_H\) 时风险 \(R(\alpha_H\mid x)=1\times0.75=0.75\)。最小风险规则改为判 \(C_H\)。改变的是**行动代价**，不是后验概率。

若恢复 0–1 loss 并允许固定拒绝损失 \(\lambda=0.2\)，最佳强制分类风险为 0.25，大于 0.2，因此拒绝。非对称损失下必须重新比较实际三种行动的风险，不能直接套用 \(1-\max P\) 的阈值。

## 6. 判别函数：把决策写成分数比较

discriminant function（判别函数）给每类一个分数 \(g_i(x)\)，规则是选择分数最大类。（PDF p.20）若想最小化一般条件风险，可取 \(g_i(x)=-R(\alpha_i\mid x)\)；若是 0–1 loss，可取 \(g_i(x)=P(C_i\mid x)\)。

判别函数不唯一。对所有类别**共同**乘正数、加同一个常数，或施加相同的严格递增变换，都不改变大小顺序；若给不同类各加不同常数，边界通常会变。课件 p.21 利用分母 \(p(x)\) 对各类相同，将 \(P(C_i\mid x)\) 的比较改成 \(p(x\mid C_i)P(C_i)\) 的比较；当值为正时再取 log，改成 \(\log p(x\mid C_i)+\log P(C_i)\)，便把乘积转为和。若某项为零，形式上可按 \(\log0=-\infty\) 处理，数值实现要小心。

二分类只需一个差值 \(g(x)=g_1(x)-g_2(x)\)：\(g(x)>0\) 选 \(C_1\)，否则选 \(C_2\)。用对数分数时，它是 log-likelihood ratio 加 log-prior odds：

\[
g(x)=\log\frac{p(x\mid C_1)}{p(x\mid C_2)}
+\log\frac{P(C_1)}{P(C_2)}.
\]

两项分别说明当前特征和原有类别比例怎样推动决策。（PDF p.22）decision region（决策区域）\(R_i\) 是使 \(g_i(x)\) 最大的输入集合；最大分数打平之处形成 decision boundary（决策边界）。同一类别区域可能不连通，不能预设它一定是一块简单形状。（PDF p.23）

## 7. 它在 Machine Learning 中为什么重要？

这一讲给出理论决策结构：如果 \(P(C_i)\)、\(p(x\mid C_i)\) 与损失已知，可以计算后验和最优行动。但现实中这些分布通常未知，课件 p.11 明确说会在后续估计。下一份 [Parameter Estimation](06_Parameter_Estimation.md) 便回答：给定训练样本，怎样估计类先验、类条件模型参数，并把估计结果代入这里的判别规则。

## 8. 易混淆概念和常见错误

| 概念 | 区别与边界 |
|---|---|
| prior 与 posterior | 先验是看当前 \(x\) 前，后验是看后；后验还取决于类条件密度。 |
| \(p(x\mid C_i)\) 与 \(P(C_i\mid x)\) | 前者描述该类下特征如何出现，后者是看到特征后的类别概率；方向不可倒置。 |
| 最大后验 与 最小风险 | 只在 0–1 loss 等合适损失条件下等价；非对称损失可能改变决定。 |
| conditional independence 与 independence | Naive Bayes 要求在给定类后独立，不要求总体独立。 |
| discriminant score 与 probability | 分数可为负且不必加总为 1；只要求比较顺序与目标决策一致。 |
| known model 与 estimated model | 本讲的最优性依赖真实概率和损失已知；用估计值时会有估计误差。 |

## 9. English Terminology

| English | 中文 | 一句话理解 |
|---|---|---|
| inference / estimation / prediction | 推断 / 估计 / 预测 | 由数据了解总体 / 求未知参数 / 判断新情况。 |
| prior / posterior probability | 先验 / 后验概率 | 看当前证据前 / 后的类别判断。 |
| class-conditional density / evidence | 类条件密度 / 证据 | 某类下特征的密度 / 所有类的总贡献。 |
| Bayes' decision rule | 贝叶斯决策规则 | 已知概率与损失时选择最低条件风险行动。 |
| loss / conditional risk | 损失 / 条件风险 | 某个结果的代价 / 按后验加权的平均代价。 |
| 0–1 loss / reject option | 零一损失 / 拒绝选项 | 错一次记 1 / 不确定时可暂不分类。 |
| discriminant function / decision region | 判别函数 / 决策区域 | 类别分数 / 该类分数最大的输入集合。 |

*Discriminant* 来自“区分”：它的用途是把不同类的候选决定排出顺序，并不要求输出本身是概率。

## 10. 本节知识地图

```text
分类目标 → prior + 观察 x → Bayes' rule → posterior
                                      ↓
                         0–1 loss → 最大后验
                         一般 loss → 条件风险最小
                         可拒绝 → 与拒绝风险比较
                                      ↓
                         discriminant → 决策区域
                                      ↓
                  未知概率从何而来？→ Parameter Estimation
```

## 11. 自测

1. 若只按 \(P(C_i)\) 分类，为什么同一批申请人会被判成同一类？
2. 课件 p.11 公式中的分母为何对所有候选类别相同？
3. 请逐行从 0–1 loss 推出 \(R(\alpha_i\mid x)=1-P(C_i\mid x)\)。
4. 本讲数值例子里，为什么后验较小的 \(C_H\) 在非对称损失下反而被选择？
5. 若最大后验为 0.9、拒绝损失为 0.15，按课件的 0–1 loss 规则会分类还是拒绝？
6. \(X_1,X_2\) 在总体上相关，是否就能断定朴素贝叶斯的条件独立假设必然错误？
7. 为什么取对数后 \(p(x\mid C_i)P(C_i)\) 仍给相同的类别排序？要注意什么条件？
8. 若未知 \(p(x\mid C_i)\)，本讲的规则能直接用于真实数据吗？下一讲要解决什么？

<details><summary>展开答案要点</summary>

1. 没用任何个人特征，同一先验排序对所有人相同。2. 它是对所有类别贡献求和得到的同一个 \(p(x)\)。3. 正确项损失零，其余后验相加为 1 减该类后验。4. 漏判该类的代价足够大，使该行动的平均损失更低。5. 分类，因 0.1 小于 0.15。6. 不能；总体相关仍可能在给定类别后条件独立。7. log 严格递增并把乘积变成和；正值与零值的处理须明确。8. 不能无误差地直接算；需要估计先验和类条件模型。

</details>
