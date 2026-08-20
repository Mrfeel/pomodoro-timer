#!/usr/bin/env python3
"""生成线性代数B1期末复习提纲 —— 基于历年真题分析"""

content = r"""# 线性代数 B1 期末考试复习提纲

> 基于 2015-2025 年共 20 份真题（10 份期中 + 10 份期末）的系统分析
>
> 科大线性代数 B1 教材：前 6 章（行列式 → 欧式空间与二次型）

\newpage

# 第一部分：考试概述

## 一、试卷结构

| 题型 | 题量 | 每题分值 | 总分占比 |
|------|------|---------|---------|
| 填空题 | 约 6 题 | 5-6 分/题 | 约 30 分 |
| 判断题 | 约 5 题 | 2-4 分/题 | 约 15 分 |
| 解答题 | 约 5-6 题 | 8-15 分/题 | 约 55 分 |

## 二、各章节考查权重

| 章节 | 期中权重 | 期末权重 | 核心度 |
|------|---------|---------|--------|
| 第1章 行列式 | ★★★★★ | ★★ | 期中核心 |
| 第2章 矩阵 | ★★★★ | ★★ | 期中核心 |
| 第3章 线性方程组 | ★★★★★ | ★★★ | 必考 |
| 第4章 向量空间 | ★★★★ | ★★★ | 必考 |
| 第5章 特征值与对角化 | — | ★★★★★ | 期末核心 |
| 第6章 二次型与欧式空间 | — | ★★★★★ | 期末核心 |

\newpage

# 第二部分：各章核心考点与解题方法

## 第1章 行列式

### 1.1 必会公式

| 公式 | 用途 |
|------|------|
| $|A^T| = |A|$ | 转置不改变行列式 |
| $|AB| = |A||B|$ | 乘积的行列式 |
| $|A^{-1}| = 1/|A|$ | 逆矩阵的行列式 |
| $|A^*| = |A|^{n-1}$ | 伴随矩阵的行列式 |
| $|kA| = k^n|A|$ | 数乘（注意是指数 $n$！） |
| $|A| = \prod \lambda_i$ | 行列式 = 特征值之积 |
| $\text{tr}(A) = \sum a_{ii} = \sum \lambda_i$ | 迹 = 特征值之和 |

### 1.2 代数余子式

$$\boxed{A_{ij} = (-1)^{i+j}M_{ij}}$$

- 按行展开：$|A| = \sum_{j=1}^n a_{ij}A_{ij}$（固定 $i$）
- 按列展开：$|A| = \sum_{i=1}^n a_{ij}A_{ij}$（固定 $j$）

**高频考法**：$\sum A_{ij}$ 型 → **把 $A$ 中对应行/列换成全 1 后求行列式**。

### 1.3 特殊行列式的计算

| 类型 | 方法 | 出现频率 |
|------|------|---------|
| **Vandermonde 行列式** | 公式 $V = \prod_{1 \leq i < j \leq n}(x_j-x_i)$ | 高频 |
| **三对角行列式** | 递推法 $D_n = aD_{n-1} - bc D_{n-2}$ | 中频 |
| **加边法（升阶法）** | 加一行一列后消元 | 中频 |
| **箭形行列式** | 消去非对角元素 | 低频 |
| **分块行列式** | $\begin{vmatrix} A & B \\ C & D \end{vmatrix} = |A||D-CA^{-1}B|$（$A$ 可逆） | 中频 |

### 1.4 高频填空题

- 含 $x$ 行列式中求某次项系数：**按含 $x$ 的行/列展开**
- $|A^TA| = |A|^2$：利用 $|A^T|=|A|$

\newpage

## 第2章 矩阵

### 2.1 必会运算

| 运算 | 公式 | 注意事项 |
|------|------|---------|
| 逆矩阵 | $A^{-1} = \dfrac{A^*}{|A|}$ | 2阶：$\begin{pmatrix} a & b \\ c & d \end{pmatrix}^{-1} = \frac{1}{ad-bc}\begin{pmatrix} d & -b \\ -c & a \end{pmatrix}$ |
| 伴随矩阵 | $A^* = |A|A^{-1}$ | $A A^* = A^* A = |A|I$ |
| 矩阵方程 | $AX=B \Rightarrow X=A^{-1}B$ | $XA=B \Rightarrow X=BA^{-1}$（注意顺序！） |
| 转置 | $(AB)^T = B^T A^T$ | 注意逆序 |

### 2.2 矩阵幂次——三种方法

| 方法 | 适用条件 | 步骤 |
|------|---------|------|
| **秩1分解** | $A$ 可写成 $\boldsymbol{\alpha}\boldsymbol{\beta}^T$ | $A^k = (\boldsymbol{\beta}^T\boldsymbol{\alpha})^{k-1}A$ |
| **归纳法** | 低阶矩阵 | 算 $A^2,A^3$ 找规律 |
| **对角化** | $A=P\Lambda P^{-1}$ | $A^k = P\Lambda^k P^{-1}$ |
| **二项式展开** | $A = \lambda I + N$，且 $\lambda I$ 与 $N$ 可交换 | $( \lambda I + N)^k = \sum_{j=0}^k \binom{k}{j}\lambda^{k-j}N^j$ |

### 2.3 矩阵秩的重要结论

$$\boxed{\text{rank}(AB) \leq \min(\text{rank}(A), \text{rank}(B))}$$

$$\boxed{\text{rank}(A) + \text{rank}(B) - n \leq \text{rank}(AB) \quad\text{(Sylvester 不等式)}}$$

- 若 $A$ 可逆，则 $\text{rank}(AB) = \text{rank}(B)$
- 若 $B$ 可逆，则 $\text{rank}(AB) = \text{rank}(A)$

### 2.4 相抵标准型

每个 $m\times n$ 矩阵 $A$ 相抵于：

$$\begin{pmatrix} I_r & 0 \\ 0 & 0 \end{pmatrix},\quad r = \text{rank}(A)$$

通过初等变换实现：$PAQ = \text{相抵标准型}$。

\newpage

## 第3章 线性方程组

### 3.1 解的结构——必背

$$\boxed{\text{通解} = \text{特解} + \text{导出组通解}}$$

$$\boxed{\text{导出组通解} = c_1\boldsymbol{\xi}_1 + c_2\boldsymbol{\xi}_2 + \cdots + c_{n-r}\boldsymbol{\xi}_{n-r}}$$

其中 $\boldsymbol{\xi}_i$ 是基础解系，$n-r$ 是自由变量个数。

### 3.2 解的判定——每年必考

| 条件 | 结论 |
|------|------|
| $\text{rank}(A) = \text{rank}(A|\boldsymbol{b}) = n$ | **唯一解** |
| $\text{rank}(A) = \text{rank}(A|\boldsymbol{b}) < n$ | **无穷多解**（$n-r$ 个自由变量） |
| $\text{rank}(A) < \text{rank}(A|\boldsymbol{b})$ | **无解** |

### 3.3 含参数方程组的标准解法

> **这是期中解答题第1题，几乎每年必考！**

| 步骤 | 操作 |
|------|------|
| ① 写增广矩阵 $(A|\boldsymbol{b})$ |
| ② 初等行变换 → 行阶梯形 |
| ③ 讨论参数：何时 $\text{rank}(A) = \text{rank}(A|\boldsymbol{b})$？ |
| ④ 对每种情况写出解（无解/唯一解/通解） |

### 3.4 基础解系

自由变量个数 = $n - \text{rank}(A)$。逐个赋 1 法 → $n-r$ 个基向量。

\newpage

## 第4章 向量空间与线性相关性

### 4.1 核心概念关系图

```
线性相关 ←──────────→ 线性无关
    │                     │
    ▼                     ▼
存在不全为零的          只有全零组合
组合系数使和为0         使和为0
    │                     │
    ├─ 几何：共线/共面    ├─ 几何：不共线/不共面
    ├─ 代数：秩 < 个数    ├─ 代数：秩 = 个数
    └─ 行列式 |A|=0       └─ 行列式 |A|≠0 (方阵时)
```

### 4.2 线性相关/无关的判定方法

| 方法 | 操作 |
|------|------|
| **定义法** | 设 $k_1\boldsymbol{\alpha}_1+\cdots+k_m\boldsymbol{\alpha}_m=\boldsymbol{0}$，解出 $k_i$ |
| **秩法** | 向量组构成矩阵 $A$，$\text{rank}(A) < m$ ⇔ 相关 |
| **行列式法**（$m=n$ 时） | $|A|=0$ ⇔ 相关；$|A|\neq 0$ ⇔ 无关 |
| **Schmidt 正交化** | 若过程中出现零向量 → 原向量组相关 |

### 4.3 极大无关组与秩

- 秩 = 极大无关组中向量个数 = 矩阵经初等变换后的非零行数
- 求极大无关组：列向量 → 按列排矩阵 → 初等行变换 → 主元列对应的原向量

### 4.4 基、维数、坐标

| 概念 | 含义 | 计算 |
|------|------|------|
| 基 | 能张成全空间且线性无关的向量组 | 维数个线性无关向量 |
| 维数 | 基中向量的个数 | $\dim V = n$ |
| 坐标 | 向量在给定基下的表示系数 | 解线性方程组 $B\boldsymbol{x} = \boldsymbol{\alpha}$ |
| 过渡矩阵 | 两组基之间的变换 | $(\boldsymbol{\beta}_1,\ldots,\boldsymbol{\beta}_n) = (\boldsymbol{\alpha}_1,\ldots,\boldsymbol{\alpha}_n)P$ |

### 4.5 过渡矩阵与基变换

$$P = (\boldsymbol{\alpha}_1,\ldots,\boldsymbol{\alpha}_n)^{-1}(\boldsymbol{\beta}_1,\ldots,\boldsymbol{\beta}_n)$$

新坐标 = $P^{-1}\times$ 旧坐标。

\newpage

## 第5章 特征值与对角化

### 5.1 特征值与特征向量

$$\boxed{A\boldsymbol{x} = \lambda\boldsymbol{x}}$$

$$\boxed{|\lambda I - A| = 0 \;\Rightarrow\; \text{特征值}}$$

$$\boxed{(A-\lambda I)\boldsymbol{x} = \boldsymbol{0} \;\Rightarrow\; \text{特征向量}}$$

### 5.2 重要性质

| 性质 | 公式 |
|------|------|
| 迹 = 特征值之和 | $\text{tr}(A) = \sum \lambda_i = \sum a_{ii}$ |
| 行列式 = 特征值之积 | $|A| = \prod \lambda_i$ |
| $A$ 可逆 | ⇔ 所有 $\lambda_i \neq 0$ |
| $A$ 的特征值 | $\lambda$ |
| $A^k$ 的特征值 | $\lambda^k$ |
| $A^{-1}$ 的特征值 | $1/\lambda$ |
| $A^*$ 的特征值 | $|A|/\lambda$ |
| $A + kI$ 的特征值 | $\lambda + k$ |
| 不同特征值的特征向量 | **线性无关** |

### 5.3 代数重数与几何重数

| | 代数重数 $a_\lambda$ | 几何重数 $g_\lambda$ |
|--|-------------------|-------------------|
| 含义 | 特征多项式中 $(\lambda-\lambda_i)$ 的幂次 | 线性无关特征向量个数 |
| 计算 | 解特征多项式 | $n - \text{rank}(A-\lambda I)$ |
| 关系 | — | $1 \leq g_\lambda \leq a_\lambda$ |

$$\boxed{\text{可对角化} \;\Longleftrightarrow\; \forall\lambda,\; g_\lambda = a_\lambda}$$

### 5.4 相似对角化步骤

| 步骤 | 操作 |
|------|------|
| ① 求特征值 | 解 $|\lambda I - A| = 0$ |
| ② 对每个 $\lambda$，求特征向量 | 解 $(A-\lambda I)\boldsymbol{x} = \boldsymbol{0}$ |
| ③ 判断 | 是否有 $n$ 个线性无关特征向量？ |
| ④ 若是 | $P = (\boldsymbol{x}_1,\ldots,\boldsymbol{x}_n)$，$P^{-1}AP = \text{diag}(\lambda_1,\ldots,\lambda_n)$ |

### 5.5 可对角化的几种判定

| 条件 | 结论 |
|------|------|
| 有 $n$ 个互异特征值 | ✅ 可对角化 |
| 实对称矩阵 | ✅ 可正交相似对角化 |
| $A^2 = kA$ 型 | ✅ 可对角化（极小多项式无重根） |
| 每个特征值 $g_\lambda = a_\lambda$ | ✅ 可对角化 |
| 存在 $g_\lambda < a_\lambda$ | ❌ 不可对角化 |

\newpage

## 第6章 二次型与欧式空间

### 6.1 二次型及其矩阵表示

$$\boxed{f(x_1,\ldots,x_n) = \boldsymbol{x}^T A \boldsymbol{x}}$$

其中 $A$ 是**实对称矩阵**：$A^T = A$。

二次型 ↔ 实对称矩阵 —— **一一对应**。

### 6.2 正交变换化二次型为标准型——期末最核心大题

| 步骤 | 操作 |
|------|------|
| ① 写出对称矩阵 $A$ | $f = \boldsymbol{x}^T A\boldsymbol{x}$ |
| ② 求 $A$ 的特征值 | $|\lambda I - A|=0$ |
| ③ 求每个特征值的特征向量 | $(A-\lambda I)\boldsymbol{x}=0$ |
| ④ **正交化 + 单位化** | 施密特正交化（同一特征值内），再单位化 |
| ⑤ 写出正交矩阵 $Q$ | $Q = (\boldsymbol{q}_1,\ldots,\boldsymbol{q}_n)$，$Q^T=Q^{-1}$ |
| ⑥ 正交变换 | $\boldsymbol{x} = Q\boldsymbol{y}$，$f = \lambda_1 y_1^2 + \cdots + \lambda_n y_n^2$ |

### 6.3 施密特正交化

$$\boxed{\boldsymbol{\beta}_1 = \boldsymbol{\alpha}_1}$$

$$\boxed{\boldsymbol{\beta}_k = \boldsymbol{\alpha}_k - \sum_{j=1}^{k-1}\frac{(\boldsymbol{\alpha}_k,\boldsymbol{\beta}_j)}{(\boldsymbol{\beta}_j,\boldsymbol{\beta}_j)}\boldsymbol{\beta}_j}$$

再单位化：$\boldsymbol{q}_i = \boldsymbol{\beta}_i / \|\boldsymbol{\beta}_i\|$

### 6.4 正定性的判定

| 方法 | 判定条件 |
|------|---------|
| **顺序主子式**（最常用） | 所有顺序主子式 $> 0$ ⇔ 正定 |
| 特征值 | 所有特征值 $> 0$ ⇔ 正定 |
| 定义 | $\forall \boldsymbol{x}\neq\boldsymbol{0},\;\boldsymbol{x}^T A\boldsymbol{x} > 0$ |
| 合同于 $I$ | $A$ 与 $I$ 合同（存在可逆 $C$ 使 $C^TAC=I$） |

**高频填空题**：已知二次型正定 → 用顺序主子式法求参数取值范围。

### 6.5 二次曲面分类

通过正交变换 + 平移，将二次曲面方程化为标准形式：

| 特征值符号 | 曲面类型 |
|-----------|---------|
| +++=1 | 椭球面 |
| ++-=1 | **单叶双曲面**（出现频率最高！） |
| +--=1 | 双叶双曲面 |
| ++=z | 椭圆抛物面 |
| +-=z | 双曲抛物面（马鞍面） |
| ++=1 (缺 z) | 椭圆柱面 |

### 6.6 相似不变量汇总

| 不变量 | 是否相同 | 说明 |
|--------|---------|------|
| 特征值 + 重数 | ✅ | 从特征多项式来 |
| 行列式 | ✅ | $=\prod\lambda_i$ |
| 迹 | ✅ | $=\sum\lambda_i$ |
| 秩 | ✅ | |
| 特征多项式 | ✅ | |
| 最小多项式 | ✅ | |
| 若尔当标准形 | ✅ | 相似的最高判据 |
| 特征向量 | ❌ | $B$ 的特征向量 = $P^{-1}\times$（$A$ 的特征向量） |

\newpage

# 第三部分：判断题高频易错点

## 必背陷阱清单

| 序号 | 常见错误陈述 | 正确答案 |
|------|------------|---------|
| 1 | $\det(AB)=\det(BA)$ 总是成立 | ❌ **非方阵时不成立！** $m\neq n$ 时阶数不同 |
| 2 | $A^2=I \Rightarrow A=\pm I$ | ❌ 反例 $\text{diag}(1,-1)$，只有特征值 $\pm 1$ |
| 3 | 若 $A_1\sim B_1$，$A_2\sim B_2$，则 $A_1+A_2\sim B_1+B_2$ | ❌ **相似对加法不封闭** |
| 4 | 奇异矩阵构成子空间 | ❌ $|A|=0$ 对加法不封闭 |
| 5 | 顺序主子式非负 → 半正定 | ❌ 仅对实对称阵成立 |
| 6 | $A\boldsymbol{x}=\boldsymbol{0}$ 只有零解 → $A\boldsymbol{x}=\boldsymbol{b}$ 有唯一解 | ❌ $A\boldsymbol{x}=\boldsymbol{b}$ 可能无解（$\boldsymbol{b}$ 不在列空间中） |
| 7 | 正交矩阵一定正交相似于对角阵 | ❌ 只有实对称阵才能保证正交相似对角化 |
| 8 | 上三角正交阵 → 对角阵 | ✅ 正确，非对角元通过正交条件可推为 0 |
| 9 | 0 是特征值 → 矩阵不可逆 | ✅ $\det A = \prod\lambda_i = 0$ |
| 10 | 正定阵对角元全正 | ✅ 正确（但逆命题不成立！） |
| 11 | 基础解系的线性组合仍是基础解系 | ❌ 需要验证是否仍线性无关 |
| 12 | $AB-BA=\mu I$（$\mu\neq 0$）可能存在 | ❌ 两边取迹得 $0 = n\mu$，矛盾 |

\newpage

# 第四部分：必会证明与重要结论

## 4.1 秩不等式链

$$\text{rank}(A) = \text{rank}(A^T) = \text{rank}(A^TA) = \text{rank}(AA^T)$$

$$\text{rank}(AB) \leq \min(\text{rank}(A),\text{rank}(B))$$

$$\text{rank}(A+B) \leq \text{rank}(A) + \text{rank}(B)$$

$$\text{rank}(A) + \text{rank}(B) - n \leq \text{rank}(AB)$$

## 4.2 $A^2=kA$ 型证明可对角化

若 $A^2 = kA$（$k\neq 0$），则 $A$ 可对角化。

**证明思路**：利用 $\text{rank}(A) + \text{rank}(A-kI) = n$（Sylvester 不等式），说明 $\mathbb{R}^n$ 是 $A$ 和 $A-kI$ 的零空间的直和 → 特征向量张成全空间。

## 4.3 实对称矩阵的正交相似对角化

实对称矩阵特征值全为实数，不同特征值的特征向量正交，必可正交相似对角化。

\newpage

# 第五部分：考前速查卡

## 矩阵运算速查

| 运算 | 公式 |
|------|------|
| $|AB|$ | $=|A||B|$ |
| $|A^{-1}|$ | $=1/|A|$ |
| $|A^*|$ | $=|A|^{n-1}$ |
| $|kA|$ | $=k^n|A|$ |
| $(AB)^{-1}$ | $=B^{-1}A^{-1}$ |
| $(AB)^T$ | $=B^T A^T$ |
| $\text{tr}(AB)$ | $=\text{tr}(BA)$ |
| $\text{rank}(A)$ | $=\text{rank}(A^T)=\text{rank}(A^TA)$ |

## 特征值关系速查

若 $A\boldsymbol{x} = \lambda\boldsymbol{x}$，则：

| 矩阵 | 特征值 |
|------|--------|
| $A$ | $\lambda$ |
| $A^k$ | $\lambda^k$ |
| $A^{-1}$ | $1/\lambda$ |
| $A^*$ | $|A|/\lambda$ |
| $A+kI$ | $\lambda+k$ |
| $P^{-1}AP$ | $\lambda$（不变！） |

## 考试最后检查清单

- [ ] 行列式：$|kA|=k^n|A|$，不是 $k|A|$
- [ ] 矩阵方程：$AX=B \Rightarrow X=A^{-1}B$，$XA=B \Rightarrow X=BA^{-1}$
- [ ] 秩：$\text{rank}(AB) \leq \min(\text{rank}(A),\text{rank}(B))$，等式不一定成立
- [ ] 基础解系：自由变量数 = $n - \text{rank}(A)$，不是 $n$ 减非零行数
- [ ] 可对角化：$g_\lambda = a_\lambda$ 对所有 $\lambda$ 成立
- [ ] 正交化：先正交化再单位化，顺序不能反
- [ ] 正定性：用顺序主子式法时，矩阵必须是对称的
- [ ] $\det(AB)=\det(BA)$：$A,B$ 必须都是 $n\times n$

\newpage

# 第六部分：推荐复习顺序

```
第1天：行列式 + 矩阵（计算题基础）
   └─ 重点：n阶行列式、矩阵幂次、矩阵方程
第2天：线性方程组 + 向量空间
   └─ 重点：含参数方程组、基础解系、秩、基与坐标
第3天：特征值与对角化
   └─ 重点：特征值/向量计算、代数vs几何重数、对角化判定
第4天：二次型 + 欧式空间
   └─ 重点：正交变换化标准型、施密特正交化、正定性、曲面分类
第5天：真题模拟 + 判断题专项
   └─ 重点：近年期末真题至少做3套，判断题易错点反复看
```

## 一句话总结

> 线性代数 B1 期末考试每年题型高度重复。行列式 + 矩阵为基础，含参方程组和二次型正交标准化为两大核心解答题，特征值/对角化/正定性为填空判断高频考点。把 10 年真题做透，足以应对考试。
"""

with open(r"d:\辰辰\first CC\线性代数B1复习提纲.md", "w", encoding="utf-8") as f:
    f.write(content)

print("复习提纲 Markdown 已生成")
