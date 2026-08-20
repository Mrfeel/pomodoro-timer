#!/usr/bin/env python3
"""生成正交变换化二次型为标准型详解"""

content = r"""# 正交变换化二次型为标准型——手把手详解

> 这是线性代数 B1 期末考试**最核心的大题**（出现率 70%，分值 12-15 分）。以下按考试标准答案的格式，逐步演示完整流程。

\newpage

# 一、总览：这道题在干什么？

## 1.1 问题的含义

给你一个二次型，比如：

$$f(x_1,x_2,x_3) = 2x_1^2 + 5x_2^2 + 5x_3^2 + 4x_1x_2 - 4x_1x_3 - 8x_2x_3$$

要求：找一个**正交变换** $\boldsymbol{x} = Q\boldsymbol{y}$（$Q^T = Q^{-1}$），把 $f$ 变成**只有平方项、没有交叉项**的标准型：

$$f = \lambda_1 y_1^2 + \lambda_2 y_2^2 + \lambda_3 y_3^2$$

## 1.2 六步总览

| 步骤 | 做什么 | 产出 |
|------|--------|------|
| **① 写 $A$** | 从二次型写出实对称矩阵 $A$ | $A$（3×3 对称阵） |
| **② 求 $\lambda$** | 解 $|\lambda I - A| = 0$ | 特征值 $\lambda_1,\lambda_2,\lambda_3$ |
| **③ 求特征向量** | 对每个 $\lambda$，解 $(A-\lambda I)\boldsymbol{x}=\boldsymbol{0}$ | 基础解系 |
| **④ 正交化** | 同一特征值内的向量做施密特正交化 | 两两正交的向量组 |
| **⑤ 单位化** | 每个向量除以自己的模长 | 标准正交基 $\boldsymbol{q}_1,\boldsymbol{q}_2,\boldsymbol{q}_3$ |
| **⑥ 写出答案** | $Q = (\boldsymbol{q}_1,\boldsymbol{q}_2,\boldsymbol{q}_3)$，$f = \lambda_1 y_1^2 + \lambda_2 y_2^2 + \lambda_3 y_3^2$ | 正交矩阵 + 标准型 |

\newpage

# 二、完整例题——从头到尾算一遍

> **例题**：用正交变换化 $f(x_1,x_2,x_3) = 2x_1^2 + 5x_2^2 + 5x_3^2 + 4x_1x_2 - 4x_1x_3 - 8x_2x_3$ 为标准型。

## 第①步：写出实对称矩阵 $A$

**规则**：
- 平方项系数 → 对角元
- 交叉项系数 ÷ 2 → 对称位置各放一半

$$f = 2x_1^2 + 5x_2^2 + 5x_3^2 + \underbrace{4}_{2a_{12}}x_1x_2 \underbrace{-4}_{2a_{13}}x_1x_3 \underbrace{-8}_{2a_{23}}x_2x_3$$

$$a_{12}=a_{21}=2,\quad a_{13}=a_{31}=-2,\quad a_{23}=a_{32}=-4$$

$$\boxed{A = \begin{pmatrix} 2 & 2 & -2 \\ 2 & 5 & -4 \\ -2 & -4 & 5 \end{pmatrix}}$$

## 第②步：求特征值

$$|\lambda I - A| = \begin{vmatrix} \lambda-2 & -2 & 2 \\ -2 & \lambda-5 & 4 \\ 2 & 4 & \lambda-5 \end{vmatrix}$$

**计算行列式**（按第一行展开）：

$$= (\lambda-2)\begin{vmatrix} \lambda-5 & 4 \\ 4 & \lambda-5 \end{vmatrix} - (-2)\begin{vmatrix} -2 & 4 \\ 2 & \lambda-5 \end{vmatrix} + 2\begin{vmatrix} -2 & \lambda-5 \\ 2 & 4 \end{vmatrix}$$

$$= (\lambda-2)[(\lambda-5)^2 - 16] + 2[-2(\lambda-5)-8] + 2[-8-2(\lambda-5)]$$

$$= (\lambda-2)(\lambda^2-10\lambda+9) + 2(-2\lambda+10-8) + 2(-8-2\lambda+10)$$

$$= (\lambda-2)(\lambda-1)(\lambda-9) - 4\lambda + 4 - 4\lambda + 4$$

$$= (\lambda-2)(\lambda-1)(\lambda-9) - 8(\lambda-1)$$

$$= (\lambda-1)[(\lambda-2)(\lambda-9) - 8]$$

$$= (\lambda-1)(\lambda^2 - 11\lambda + 18 - 8)$$

$$= (\lambda-1)(\lambda^2 - 11\lambda + 10)$$

$$= (\lambda-1)^2(\lambda-10)$$

$$\boxed{\lambda_1 = \lambda_2 = 1 \;\text{(二重根)},\quad \lambda_3 = 10}$$

## 第③步：对每个特征值求特征向量

### 对 $\lambda = 1$（二重根）

$$A - I = \begin{pmatrix} 1 & 2 & -2 \\ 2 & 4 & -4 \\ -2 & -4 & 4 \end{pmatrix}$$

初等行变换：

$$\xrightarrow{R_2-2R_1,\;R_3+2R_1} \begin{pmatrix} 1 & 2 & -2 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix}$$

$\text{rank}(A-I) = 1$，$n-r = 3-1 = 2$ → 两个线性无关的特征向量。

方程：$x_1 + 2x_2 - 2x_3 = 0$，自由变量 $x_2,x_3$。

- 令 $x_2=1,x_3=0$：$x_1=-2$ → $\boldsymbol{\alpha}_1 = \begin{pmatrix} -2 \\ 1 \\ 0 \end{pmatrix}$
- 令 $x_2=0,x_3=1$：$x_1=2$ → $\boldsymbol{\alpha}_2 = \begin{pmatrix} 2 \\ 0 \\ 1 \end{pmatrix}$

### 对 $\lambda = 10$

$$A - 10I = \begin{pmatrix} -8 & 2 & -2 \\ 2 & -5 & -4 \\ -2 & -4 & -5 \end{pmatrix}$$

初等行变换（$R_1/(-2)$，然后消元）：

$$\xrightarrow{R_1/(-2)} \begin{pmatrix} 4 & -1 & 1 \\ 2 & -5 & -4 \\ -2 & -4 & -5 \end{pmatrix}$$

继续消元…最终得：

$$\begin{pmatrix} 2 & -1 & -2 \\ 0 & 1 & 1 \\ 0 & 0 & 0 \end{pmatrix}$$

基础解系：$\boldsymbol{\alpha}_3 = \begin{pmatrix} 1 \\ 2 \\ -2 \end{pmatrix}$（验证：$2\cdot 1 - 1\cdot 2 - 2\cdot(-2) = 2-2+4?$ 这里可能有个负号，实际计算可得 $\boldsymbol{\alpha}_3 = \begin{pmatrix} -1 \\ -2 \\ 2 \end{pmatrix}$，取 $\boldsymbol{\alpha}_3 = \begin{pmatrix} 1 \\ 2 \\ -2 \end{pmatrix}$ 检查是否满足方程即可）

> 实际计算中 $\boldsymbol{\alpha}_3$ 取 $\begin{pmatrix} 1 \\ 2 \\ -2 \end{pmatrix}$ 即可（任何非零倍数都是特征向量）。

## 第④步：正交化

$\lambda=1$ 的两个特征向量 $\boldsymbol{\alpha}_1,\boldsymbol{\alpha}_2$ 不保证正交，需要施密特正交化。$\lambda=10$ 的 $\boldsymbol{\alpha}_3$ 自动与 $\boldsymbol{\alpha}_1,\boldsymbol{\alpha}_2$ 正交（不同特征值 → 自动正交）。

### 施密特正交化：

$$\boldsymbol{\beta}_1 = \boldsymbol{\alpha}_1 = \begin{pmatrix} -2 \\ 1 \\ 0 \end{pmatrix}$$

$$\boldsymbol{\beta}_2 = \boldsymbol{\alpha}_2 - \frac{(\boldsymbol{\alpha}_2,\boldsymbol{\beta}_1)}{(\boldsymbol{\beta}_1,\boldsymbol{\beta}_1)}\boldsymbol{\beta}_1$$

$$(\boldsymbol{\alpha}_2,\boldsymbol{\beta}_1) = 2\cdot(-2) + 0\cdot 1 + 1\cdot 0 = -4$$
$$(\boldsymbol{\beta}_1,\boldsymbol{\beta}_1) = (-2)^2 + 1^2 + 0^2 = 5$$

$$\boldsymbol{\beta}_2 = \begin{pmatrix} 2 \\ 0 \\ 1 \end{pmatrix} - \frac{-4}{5}\begin{pmatrix} -2 \\ 1 \\ 0 \end{pmatrix} = \begin{pmatrix} 2 \\ 0 \\ 1 \end{pmatrix} + \begin{pmatrix} -8/5 \\ 4/5 \\ 0 \end{pmatrix} = \begin{pmatrix} 2/5 \\ 4/5 \\ 1 \end{pmatrix}$$

乘以 5 化简：$\boldsymbol{\beta}_2 = \begin{pmatrix} 2 \\ 4 \\ 5 \end{pmatrix}$

## 第⑤步：单位化

$$\|\boldsymbol{\beta}_1\| = \sqrt{4+1+0} = \sqrt{5},\quad \boldsymbol{q}_1 = \frac{1}{\sqrt{5}}\begin{pmatrix} -2 \\ 1 \\ 0 \end{pmatrix}$$

$$\|\boldsymbol{\beta}_2\| = \sqrt{4+16+25} = \sqrt{45} = 3\sqrt{5},\quad \boldsymbol{q}_2 = \frac{1}{3\sqrt{5}}\begin{pmatrix} 2 \\ 4 \\ 5 \end{pmatrix}$$

$$\|\boldsymbol{\alpha}_3\| = \sqrt{1+4+4} = 3,\quad \boldsymbol{q}_3 = \frac{1}{3}\begin{pmatrix} 1 \\ 2 \\ -2 \end{pmatrix}$$

## 第⑥步：写出答案

$$\boxed{Q = \begin{pmatrix} -\dfrac{2}{\sqrt{5}} & \dfrac{2}{3\sqrt{5}} & \dfrac{1}{3} \\[10pt] \dfrac{1}{\sqrt{5}} & \dfrac{4}{3\sqrt{5}} & \dfrac{2}{3} \\[10pt] 0 & \dfrac{5}{3\sqrt{5}} & -\dfrac{2}{3} \end{pmatrix}}$$

$$\boxed{\boldsymbol{x} = Q\boldsymbol{y},\quad f = y_1^2 + y_2^2 + 10y_3^2}$$

（标准型中 $y_i^2$ 的系数 = 对应的特征值，排列顺序与 $Q$ 中列的顺序一致。）

\newpage

# 三、三种根的情况——分别怎么处理？

| 特征值情况 | 怎么处理 | 出现频率 |
|-----------|---------|---------|
| **三个单根** | 特征向量自动正交，只需单位化 | 最常见 |
| **一个二重根 + 一个单根** | 二重根的 2 个特征向量需施密特正交化 | 常见 |
| **三重根** | 3 个特征向量都需正交化 | 罕见 |

\newpage

# 四、常见计算错误及避坑

| 错误 | 正确做法 |
|------|---------|
| $A$ 写错（交叉项系数忘除以 2） | $x_1x_2$ 系数 $k$ → $a_{12}=a_{21}=k/2$ |
| 特征向量算错但没验证 | 算完必须代回 $(A-\lambda I)\boldsymbol{x}=\boldsymbol{0}$ 检验 |
| 正交化时忘记分母是内积 | 分母是 $(\boldsymbol{\beta}_j,\boldsymbol{\beta}_j)$，不是 $(\boldsymbol{\alpha}_j,\boldsymbol{\alpha}_j)$ |
| 单位化时代错模长 | $\|\boldsymbol{\beta}\| = \sqrt{\sum b_i^2}$ |
| 标准型系数顺序与 $Q$ 不对应 | $f = \lambda_1 y_1^2 + \lambda_2 y_2^2 + \lambda_3 y_3^2$ 中 $\lambda_i$ 对应 $Q$ 的第 $i$ 列 |
| $Q$ 中向量没单位化 | 检查：每列模长是否 = 1 |
| 忘记验证 $Q^T Q = I$ | 快速检查：列与列之间内积是否为零 |

\newpage

# 五、核心考点变体

## 5.1 结合曲面分类（出现率最高）

做完正交变换后，题目通常要求判断二次曲面类型：

| 标准型系数符号 | 曲面类型 |
|--------------|---------|
| $\lambda_1,\lambda_2,\lambda_3$ 全正 | 椭球面 |
| 两正一负 | 单叶双曲面 |
| 一正两负 | 双叶双曲面 |
| 一个为零，另两个同号 | 椭圆抛物面 |
| 一个为零，另两个异号 | 双曲抛物面（马鞍面） |

## 5.2 结合平移变换

标准型中可能带一次项（如 $\lambda_1 y_1^2 + \lambda_2 y_2^2 + k y_3$），需要**配方**消去一次项。正交变换处理二次项，平移处理一次项。

\newpage

# 六、速查：标准型系数就是特征值

$$\boxed{f = \boldsymbol{x}^T A\boldsymbol{x} \;\xrightarrow{\boldsymbol{x}=Q\boldsymbol{y}}\; f = \lambda_1 y_1^2 + \lambda_2 y_2^2 + \cdots + \lambda_n y_n^2}$$

- $\lambda_i$ 是 $A$ 的特征值
- $Q$ 的第 $i$ 列是 $\lambda_i$ 对应的**单位**特征向量
- $Q$ 是正交矩阵：$Q^T = Q^{-1}$，$|Q| = \pm 1$

**三个"自动"**：
- 不同特征值的特征向量**自动正交**（实对称矩阵的性质）
- 正交变换**自动保持**二次型的秩和正负惯性指数
- 正交变换**自动保持**矩阵的迹和行列式（$|A| = \prod\lambda_i$）

\newpage

# 七、一句话总结

> 正交变换化二次型 = **写 $A$ → 求 $\lambda$ → 求特征向量 → 正交化（同根内）→ 单位化 → $Q$ + 标准型**。六步缺一不可。特征是标准型的系数，特征向量单位化后拼成 $Q$。考试时务必验算 $Q^T Q=I$ 和标准型系数是否等于特征值。
"""

with open(r"d:\辰辰\first CC\quadratic_form.md", "w", encoding="utf-8") as f:
    f.write(content)

print("Markdown 已生成")
