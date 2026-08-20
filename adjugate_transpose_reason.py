#!/usr/bin/env python3
"""解释为什么伴随矩阵是代数余子式的转置"""

content = r"""# 为什么伴随矩阵是代数余子式的"转置"？

> 这是很多人初学伴随矩阵时最困惑的地方——为什么 $A^*$ 不是直接把代数余子式按原位排列，而是要转置？

\newpage

# 一、答案就一句话

> **因为行列式按行展开公式中，$a_{ik}$ 乘的是同行（第 $i$ 行）的代数余子式 $A_{ik}$，而不是同列的。如果不转置，$AA^*$ 的对角元就不再是行列式的展开式了。**

下面来拆解这个"为什么"。

\newpage

# 二、先回顾两个展开公式

## 2.1 按行展开

$$|A| = a_{i1}A_{i1} + a_{i2}A_{i2} + \cdots + a_{in}A_{in}$$

固定第 $i$ 行，元素 $a_{ik}$ 乘的是**同一行**的代数余子式 $A_{ik}$。

## 2.2 按列展开

$$|A| = a_{1j}A_{1j} + a_{2j}A_{2j} + \cdots + a_{nj}A_{nj}$$

固定第 $j$ 列，元素 $a_{kj}$ 乘的是**同一列**的代数余子式 $A_{kj}$。

## 2.3 错位展开恒为零

$$\boxed{a_{i1}A_{k1} + a_{i2}A_{k2} + \cdots + a_{in}A_{kn} = 0 \quad (i \neq k)}$$

用第 $i$ 行的元素去乘**第 $k$ 行**的代数余子式，结果为零（等价于把矩阵第 $k$ 行替换成第 $i$ 行，行列式有两行相同 → 为零）。

\newpage

# 三、$AA^*$ 的对角元需要什么？

考虑矩阵乘积 $AA^*$ 的第 $i$ 行第 $j$ 列元素 $(AA^*)_{ij}$：

$$(AA^*)_{ij} = \sum_{k=1}^n a_{ik}\,(A^*)_{kj}$$

我们想要的结果是：

$$\boxed{AA^* = |A|I = \begin{pmatrix} |A| & 0 & \cdots & 0 \\ 0 & |A| & \cdots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \cdots & |A| \end{pmatrix}}$$

即：
- **对角元** $(AA^*)_{ii}$ = $|A|$
- **非对角元** $(AA^*)_{ij}$ = $0$（$i \neq j$）

\newpage

# 四、如果不转置会怎样？

假设我们不转置，直接定义 $C_{ij} = A_{ij}$（代数余子式按原位放置），那么：

$$(AC)_{ii} = \sum_{k=1}^n a_{ik}\,C_{ki} = \sum_{k=1}^n a_{ik}\,A_{ki}$$

这是用第 $i$ 行的元素去乘**第 $k$ 行、第 $i$ 列的代数余子式**。下标混乱——$a_{ik}$ 是第 $i$ 行的，$A_{ki}$ 的第一下标 $k$ 才是行号。

这个求和**不等于行列式按行展开的形式**（展开要求同行：$a_{ik}$ 配 $A_{ik}$，两个下标第一个必须相同）。所以不对角元不会恰好等于 $|A|$。

\newpage

# 五、转置之后——完美匹配

定义 $(A^*)_{ij} = A_{ji}$（转置！），则：

$$(AA^*)_{ii} = \sum_{k=1}^n a_{ik}\,(A^*)_{ki} = \sum_{k=1}^n a_{ik}\,A_{ik}$$

这正是**第 $i$ 行按行展开的行列式公式**：

$$\boxed{(AA^*)_{ii} = \sum_{k=1}^n a_{ik}A_{ik} = |A| \;\checkmark}$$

对于非对角元 $i \neq j$：

$$(AA^*)_{ij} = \sum_{k=1}^n a_{ik}\,(A^*)_{kj} = \sum_{k=1}^n a_{ik}\,A_{jk}$$

这是用第 $i$ 行的元素去乘**第 $j$ 行**的代数余子式：

$$\boxed{(AA^*)_{ij} = \sum_{k=1}^n a_{ik}A_{jk} = 0 \quad (i \neq j) \;\checkmark}$$

**行列式中某行元素乘另一行的代数余子式，和为零。**

\newpage

# 六、用具体矩阵验证（3 阶）

$$A = \begin{pmatrix} 1 & 2 & 3 \\ 0 & 1 & 4 \\ 5 & 6 & 0 \end{pmatrix}$$

计算代数余子式：

$$A_{11} = +\begin{vmatrix} 1 & 4 \\ 6 & 0 \end{vmatrix} = -24,\; A_{12} = -\begin{vmatrix} 0 & 4 \\ 5 & 0 \end{vmatrix} = 20,\; A_{13} = +\begin{vmatrix} 0 & 1 \\ 5 & 6 \end{vmatrix} = -5$$

$$A_{21} = -\begin{vmatrix} 2 & 3 \\ 6 & 0 \end{vmatrix} = 18,\; A_{22} = +\begin{vmatrix} 1 & 3 \\ 5 & 0 \end{vmatrix} = -15,\; A_{23} = -\begin{vmatrix} 1 & 2 \\ 5 & 6 \end{vmatrix} = 4$$

$$A_{31} = +\begin{vmatrix} 2 & 3 \\ 1 & 4 \end{vmatrix} = 5,\; A_{32} = -\begin{vmatrix} 1 & 3 \\ 0 & 4 \end{vmatrix} = -4,\; A_{33} = +\begin{vmatrix} 1 & 2 \\ 0 & 1 \end{vmatrix} = 1$$

**按转置排列**（正确的 $A^*$）：

$$A^* = \begin{pmatrix} A_{11} & A_{21} & A_{31} \\ A_{12} & A_{22} & A_{32} \\ A_{13} & A_{23} & A_{33} \end{pmatrix} = \begin{pmatrix} -24 & 18 & 5 \\ 20 & -15 & -4 \\ -5 & 4 & 1 \end{pmatrix}$$

**验证** $AA^*$：

$$AA^* = \begin{pmatrix} 1 & 2 & 3 \\ 0 & 1 & 4 \\ 5 & 6 & 0 \end{pmatrix}\begin{pmatrix} -24 & 18 & 5 \\ 20 & -15 & -4 \\ -5 & 4 & 1 \end{pmatrix}$$

算 $(AA^*)_{11}$：$1\cdot(-24) + 2\cdot 20 + 3\cdot(-5) = -24+40-15 = 1$

这是否等于 $|A|$？$|A| = 1\cdot(1\cdot 0-4\cdot 6) - 2\cdot(0\cdot 0-4\cdot 5) + 3\cdot(0\cdot 6-1\cdot 5) = -24+40-15 = 1 \;\checkmark$

算 $(AA^*)_{12}$：$1\cdot 18 + 2\cdot(-15) + 3\cdot 4 = 18-30+12 = 0 \;\checkmark$

**如果按原位排列**（不转置，错误做法）：

$$C = \begin{pmatrix} A_{11} & A_{12} & A_{13} \\ A_{21} & A_{22} & A_{23} \\ A_{31} & A_{32} & A_{33} \end{pmatrix} = \begin{pmatrix} -24 & 20 & -5 \\ 18 & -15 & 4 \\ 5 & -4 & 1 \end{pmatrix}$$

算 $(AC)_{11}$：$1\cdot(-24) + 2\cdot 18 + 3\cdot 5 = -24+36+15 = 27$，这**不是** $|A|=1$！❌

\newpage

# 七、一句话总结

> 行列式按**行**展开时，第 $i$ 行的元素 $a_{ik}$ 搭配的代数余子式是 $A_{ik}$（同行同列下标）。为了让矩阵乘法 $AA^*$ 的对角元恰好等于这个展开式，$(A^*)_{ki}$ 必须等于 $A_{ik}$——即 $A^*$ 必须是代数余子式矩阵的**转置**。不转置的话，乘法配错对，对角元不再是 $|A|$，整个 $AA^*=|A|I$ 的核心公式就废了。
"""

with open(r"d:\辰辰\first CC\adjugate_transpose_reason.md", "w", encoding="utf-8") as f:
    f.write(content)

print("Markdown 已生成")
