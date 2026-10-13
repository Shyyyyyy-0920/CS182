# CS182（2026 Fall）课程地图与学习导航

> 来源：[Course_Overview.pdf](../Course_Overview.pdf)，PDF 页码从封面起算。本文只为 `E:\CS182\2026fall\lecture` 中的课件建立导航；学习要求以本学期后续发布的信息为准。

## 0. 这门课到底要学会什么？

机器学习（Machine Learning, ML）的目标，不是记住一份算法清单，而是面对一个实际问题，判断它能否表述为学习问题、该用什么方法、怎样比较方法，以及实验结果是否可信。课件明确把数学与计算原理放在中心，而不把模型当作只能调用的黑箱。（PDF p.4–8）

到课程结束，你应能完成一条闭环：

```text
实际任务 → 定义输入、输出和评价指标 → 选择模型与假设
       → 用数据训练 → 在未参与训练的数据上比较 → 解释结果与限制
```

这对应课件列出的四项 learning outcomes：问题形式化、选择常用方法、按性能标准比较、设计并解释符合科学与统计原则的实验。（PDF p.8）

## 1. 课程内容如何连接？

课件列出的主题是 Bayesian decision theory、生成模型的 parameter estimation、linear discrimination、multilayer perceptrons、support vector machines、dimensionality reduction、clustering and mixture models、nonparametric methods、ensemble learning，以及 model assessment and selection；另有六次基于 scikit-learn 的实践课，部分简单模型安排自学。（PDF p.9）

当前文件夹已提供的七份主题课件（另有 Course Overview），可以按以下依赖关系阅读：

1. [Introduction](01_Introduction.md)：先建立任务、模型、损失与泛化的共同语言。
2. [Linear Algebra](02_Linear_Algebra.md)：理解向量、矩阵、特征值、梯度和曲率。
3. [Probability and Statistics](03_Probability_Statistics.md)：理解数据不确定性及 Bayes' rule。
4. [Optimization Primer](04_Optimization_Primer.md)：理解“选出最好参数”到底如何计算。
5. [Bayesian Decision Theory](05_Bayesian_Decision_Theory.md)：用概率和错误代价制定分类决策。
6. [Parameter Estimation](06_Parameter_Estimation.md)：从数据估计决策规则需要的分布和参数。
7. [Linear Discrimination](07_Linear_Discrimination.md)：从直接学习线性边界走到 Logistic Regression、Softmax 与交叉熵梯度，连接几何、概率和优化。

第一遍读 Introduction 时，遇到多项式拟合的矩阵或优化细节可以先抓住问题与图像；学完三份数学基础课件后，再回来重推其公式。后续若增加官方课件，按其实际先修关系接在这张地图上，不预设尚未出现的课件内容。

## 2. 先修知识：需要会到什么程度？

课件列出多元微积分、线性代数与矩阵分析、概率统计、优化、信息论，以及面向对象编程、数据结构和算法分析。（PDF p.10）这是一张准备清单，不等于每项都必须先学完整本书。

开始前，可用四道小题检查：能否求 \(f(x,y)=x^2+xy\) 的梯度；能否判断 \((N\times d)(d\times 1)\) 的结果维度；能否由 \(P(A\mid B)\) 的定义解释 Bayes' rule；能否说出训练集与测试集各用于什么。如果某题卡住，就在相应数学讲义中补这一小块，再继续主线。

## 3. 怎样使用课件和讲义？

每个主题按四轮学习：

1. **问题轮**：不看公式，回答“要预测或估计什么？已知什么？”
2. **数学轮**：写清随机变量、样本、参数、维度和假设；自己复现关键推导。
3. **例子轮**：用极小数据手算一次，再用代码检验数值。
4. **评估轮**：解释训练误差、验证误差和测试误差的不同用途，记录模型何时失败。

英文考试要求你认识术语，故讲义首次出现关键概念时保留英文名称和缩写。每份讲义的页码指向原 PDF；标为“【补充理解】”的推导、类比和例子用于帮助理解，不应误当作课件原文或明确考试范围。

## 4. 教材、考核与学习节奏

本学期课件指定的教材是 Ethem Alpaydin, *Introduction to Machine Learning*, 4th ed. (2020)；另列 Duda、Hart、Stork 的 *Pattern Classification* 和 Bishop 的 *Pattern Recognition and Machine Learning* 作为参考。（PDF p.12）遇到讲义难点时按主题查阅，不必先通读整本书。

PDF p.14 记载 problem sets with programming 占 30%，final exam 占 40%，final project 占 30%；这些权重表明推导、动手实验与综合应用都要练。课件列出的时间安排只作为该 PDF 的记录，实际提交以本学期正式通知为准。学术诚信要求见 PDF p.16；做作业时保留自己的推导和实验记录。

## 5. 开始前的自测

1. 一个房价预测任务要怎样定义输入、输出和评价标准？
2. 为什么训练集上误差最低的模型不一定是最好的模型？
3. “模型”“损失函数”“优化算法”分别决定了什么？
4. 课件为何同时要求数学基础、编程能力和实验设计能力？
5. 在后面的 Bayesian classifier 中，若 \(P(C_i)\) 与 \(p(x\mid C_i)\) 未知，接下来要学习哪一讲来解决？

<details><summary>自测提示</summary>

1. 特征可以是面积、位置等，输出是价格；指标需事先确定且在未参与训练的数据上计算。2. 它可能记住样本噪声；目标是泛化。3. 分别规定可选函数、何为好坏、怎样寻找参数。4. 课程要求可解释的模型选择与可靠实验，而不仅是调用程序。5. Parameter Estimation。

</details>
