# 特征向量的几何重数——计算与理解

> **几何重数**（geometric multiplicity）= 某个特征值 $\lambda$ 对应的**线性无关特征向量的个数** = 特征子空间的维数。

\newpage

# 一、定义与公式

## 1.1 定义

$$\boxed{\text{几何重数 } g_\lambda = \dim E_\lambda = \dim\{\boldsymbol{x} \mid (A-\lambda I)\boldsymbol{x} = \boldsymbol{0}\}}$$

其中 $E_\lambda$ 是 $\lambda$ 的**特征子空间**（所有属于 $\lambda$ 的特征向量加上零向量构成的子空间）。

## 1.2 核心公式

$$\boxed{g_\lambda = n - \text{rank}(A - \lambda I)}$$

$n$ = 矩阵阶数，$\text{rank}(A-\lambda I)$ = 矩阵 $A-\lambda I$ 的秩。

这是**计算几何重数最直接的方法**——不需要先求特征向量，只需做初等行变换求 $\text{rank}(A-\lambda I)$。

## 1.3 代数重数 vs. 几何重数

| | 代数重数 $a_\lambda$ | 几何重数 $g_\lambda$ |
|--|-------------------|-------------------|
| 含义 | 特征多项式中 $(\lambda-\lambda_i)$ 的幂次 | 线性无关特征向量的个数 |
| 来源 | $|\lambda I - A| = 0$ 的根的重数 | $\dim\text{null}(A-\lambda I)$ |
| 关系 | — | **$1 \leq g_\lambda \leq a_\lambda$** |
| 对角化 | — | $g_\lambda = a_\lambda$（对所有 $\lambda$）⇔ 可对角化 |

> **关键不等式**：几何重数**永远不会超过**代数重数。几何重数 $\geq 1$ 恒成立（特征值至少有一个特征向量）。

\newpage

# 二、手把手计算——两个例子

## 例1：可对角化矩阵

$$A = \begin{pmatrix} 3 & 1 & 0 \\ 0 & 3 & 0 \\ 0 & 0 & 2 \end{pmatrix}$$

**特征值**：$|\lambda I - A| = (\lambda-3)^2(\lambda-2) = 0$

- $\lambda_1 = 3$，代数重数 $a_3 = 2$
- $\lambda_2 = 2$，代数重数 $a_2 = 1$

### 算 $\lambda=3$ 的几何重数

$$A - 3I = \begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & -1 \end{pmatrix}$$

化行最简形：

$$\xrightarrow{R_3\cdot(-1)} \begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 1 \end{pmatrix} \xrightarrow{\text{交换行}} \begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \\ 0 & 0 & 0 \end{pmatrix}$$

$\text{rank}(A-3I) = 2$（两个非零行）

$$\boxed{g_3 = n - \text{rank}(A-3I) = 3 - 2 = 1}$$

几何重数 = 1，但代数重数 = 2 → $g_3 < a_3$ → **矩阵不可对角化！**

若尔当结构：$\lambda=3$ 对应一个 $2\times 2$ 若尔当块（只有一个特征向量）。

### 算 $\lambda=2$ 的几何重数

$$A - 2I = \begin{pmatrix} 1 & 1 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 0 \end{pmatrix}$$

$\text{rank}(A-2I) = 2$ → $g_2 = 3-2 = 1 = a_2$ ✓

---

## 例2：可对角化矩阵

$$B = \begin{pmatrix} 2 & 0 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & 3 \end{pmatrix}$$

**特征值**：$\lambda=2$（代数重数 2），$\lambda=3$（代数重数 1）。

### 算 $\lambda=2$ 的几何重数

$$B - 2I = \begin{pmatrix} 0 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 1 \end{pmatrix}$$

$\text{rank}(B-2I) = 1$ → $\boxed{g_2 = 3 - 1 = 2 = a_2}$ ✓

### 算 $\lambda=3$ 的几何重数

$$B - 3I = \begin{pmatrix} -1 & 0 & 0 \\ 0 & -1 & 0 \\ 0 & 0 & 0 \end{pmatrix}$$

$\text{rank}(B-3I) = 2$ → $g_3 = 3-2 = 1 = a_3$ ✓

所有特征值均有 $g_\lambda = a_\lambda$ → **$B$ 可对角化**。

\newpage

# 三、几何重数 = 若尔当块的个数

这是几何重数最深刻的含义：

$$\boxed{g_\lambda = \lambda \text{ 对应的若尔当块个数}}$$

| 矩阵 | $\lambda$ | $a_\lambda$ | $g_\lambda$ | 若尔当结构 |
|------|----------|------------|------------|----------|
| 例1 | 3 | 2 | 1 | 一个 $2\times 2$ 块 |
| 例2 | 2 | 2 | 2 | 两个 $1\times 1$ 块（可对角化） |

**每条若尔当链贡献一个特征向量**（链首那个），所以特征向量个数 = 若尔当块个数。

\newpage

# 四、怎样判断矩阵是否可对角化？

## 四步判断法

| 步骤 | 操作 |
|------|------|
| ① 求所有特征值 $\lambda_i$ 及代数重数 $a_i$ | $|\lambda I - A|=0$ |
| ② 对每个 $\lambda_i$，算 $g_i = n - \text{rank}(A-\lambda_i I)$ | 化 $A-\lambda_i I$ 为行阶梯形 |
| ③ 检查是否 $g_i = a_i$ | 对所有 $\lambda_i$ |
| ④ 全都相等 → 可对角化；有一个不相等 → 不可对角化 |

## 典型模式

| 矩阵类型 | 几何重数特征 | 是否可对角化 |
|---------|------------|------------|
| 对称矩阵（实对称） | $g_\lambda = a_\lambda$ 恒成立 | ✅ 永远可正交对角化 |
| $n$ 个互异特征值 | 每个 $a_\lambda = 1$，$g_\lambda=1$ | ✅ 可对角化 |
| 若尔当块 $> 1\times 1$ | 存在 $g_\lambda < a_\lambda$ | ❌ 不可对角化 |
| 三角矩阵对角全相同但非标量阵 | 通常 $g_\lambda < a_\lambda$ | ❌ 通常不可对角化 |

\newpage

# 五、计算口诀

$$\boxed{g_\lambda = n - \text{rank}(A-\lambda I)}$$

**三步**：
1. 写出 $A-\lambda I$
2. 初等行变换 → 行阶梯形
3. 数非零行 = $\text{rank}(A-\lambda I)$，几何重数 = $n$ 减去这个数

**常见陷阱**：不要混淆代数重数和几何重数。代数重数看**特征多项式**，几何重数看**$A-\lambda I$ 的秩**。

## 一句话总结

> $g_\lambda = n - \text{rank}(A-\lambda I)$ = 零空间维数 = 若尔当块个数。$g_\lambda = a_\lambda$（对所有特征值）是矩阵可对角化的充要条件。几何重数决定了有多少个独立特征方向——它永远不会超过代数重数，也不会少于 1。
