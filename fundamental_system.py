#!/usr/bin/env python3
"""生成线性代数基础解系求解详解"""

content = r"""# 线性代数——基础解系的求解方法详解

> **基础解系**（fundamental system of solutions）是齐次线性方程组 $A\boldsymbol{x}=\boldsymbol{0}$ 解空间的一组基。掌握了它，就掌握了齐次方程组所有解的"生成元"。

\newpage

# 一、基础解系是什么？

## 1.1 定义

对于 $m\times n$ 矩阵 $A$，齐次方程组 $A\boldsymbol{x}=\boldsymbol{0}$ 的所有解构成一个**向量空间**（解空间/零空间）。这个空间的一组基就称为**基础解系**。

$$\boxed{\text{基础解系} = \text{解空间的一组基}}$$

## 1.2 解空间的维数

$$\boxed{\dim(\text{解空间}) = n - r}$$

其中 $n$ = 未知数个数（$A$ 的列数），$r = \text{rank}(A)$（$A$ 的秩）。

**直觉**：$n$ 个未知数，$r$ 个独立方程 → $n-r$ 个"自由度"。

## 1.3 基础解系包含几个向量？

**$n-r$ 个线性无关的解向量。** 任何解都可以写成这组基向量的线性组合。

\newpage

# 二、求解基础解系的标准步骤

## 四步法

| 步骤 | 操作 | 目的 |
|------|------|------|
| **① 化行最简形** | 对 $A$ 做初等行变换 → 行最简形（RREF） | 区分主元列和自由列 |
| **② 确定自由变量** | 非主元列对应的变量 = 自由变量 | 共 $n-r$ 个自由变量 |
| **③ 逐次赋值** | 每次让一个自由变量 = 1，其余 = 0 | 构造 $n-r$ 个线性无关的特解 |
| **④ 回代求主变量** | 代入方程，解出主变量的值 | 得到完整的基础解系向量 |

## 核心原则

> **自由变量逐个取 1，其余自由变量取 0，回代解出主变量。** 这样保证产生的 $n-r$ 个向量线性无关。

\newpage

# 三、手把手例题

## 例1：$3\times 4$ 矩阵，秩为 2

解方程组：

$$\begin{cases}
x_1 + x_2 - x_3 + 2x_4 = 0 \\
2x_1 + 2x_2 + x_3 + 3x_4 = 0 \\
x_1 + x_2 + 2x_3 + x_4 = 0
\end{cases}$$

### 第①步：写增广矩阵并化行最简形

系数矩阵 $A = \begin{pmatrix} 1 & 1 & -1 & 2 \\ 2 & 2 & 1 & 3 \\ 1 & 1 & 2 & 1 \end{pmatrix}$

初等行变换（$R_2-2R_1$，$R_3-R_1$，然后 $R_3-R_2$……）：

$$\begin{pmatrix} 1 & 1 & -1 & 2 \\ 2 & 2 & 1 & 3 \\ 1 & 1 & 2 & 1 \end{pmatrix} \xrightarrow{R_2-2R_1} \begin{pmatrix} 1 & 1 & -1 & 2 \\ 0 & 0 & 3 & -1 \\ 1 & 1 & 2 & 1 \end{pmatrix}$$

$$\xrightarrow{R_3-R_1} \begin{pmatrix} 1 & 1 & -1 & 2 \\ 0 & 0 & 3 & -1 \\ 0 & 0 & 3 & -1 \end{pmatrix} \xrightarrow{R_3-R_2} \begin{pmatrix} 1 & 1 & -1 & 2 \\ 0 & 0 & 3 & -1 \\ 0 & 0 & 0 & 0 \end{pmatrix}$$

$$\xrightarrow{R_2/3} \begin{pmatrix} 1 & 1 & -1 & 2 \\ 0 & 0 & 1 & -1/3 \\ 0 & 0 & 0 & 0 \end{pmatrix} \xrightarrow{R_1+R_2} \begin{pmatrix} \boxed{1} & 1 & 0 & 5/3 \\ 0 & 0 & \boxed{1} & -1/3 \\ 0 & 0 & 0 & 0 \end{pmatrix}$$

行最简形（RREF）：
$$\begin{pmatrix} \boxed{1} & 1 & 0 & 5/3 \\ 0 & 0 & \boxed{1} & -1/3 \\ 0 & 0 & 0 & 0 \end{pmatrix}$$

### 第②步：识别主元和自由变量

- 主元位置：第 1 列和第 3 列（方框标记）
- **主变量**：$x_1$、$x_3$
- **自由变量**：$x_2$、$x_4$

$n=4$，$r=2$，自由变量个数 $= 4-2 = 2$ → 基础解系含 **2 个向量**。

### 第③④步：逐个赋值，回代求解

**第一组：$x_2 = 1,\; x_4 = 0$**

从行最简形回代：

第二行：$x_3 - \frac{1}{3}x_4 = 0$ → $x_3 = 0$

第一行：$x_1 + x_2 + 0 + \frac{5}{3}x_4 = 0$ → $x_1 + 1 + 0 = 0$ → $x_1 = -1$

$$\boxed{\boldsymbol{\xi}_1 = \begin{pmatrix} -1 \\ 1 \\ 0 \\ 0 \end{pmatrix}}$$

**第二组：$x_2 = 0,\; x_4 = 1$**

第二行：$x_3 - \frac{1}{3}(1) = 0$ → $x_3 = \frac{1}{3}$

第一行：$x_1 + 0 + 0 + \frac{5}{3}(1) = 0$ → $x_1 = -\frac{5}{3}$

$$\boxed{\boldsymbol{\xi}_2 = \begin{pmatrix} -5/3 \\ 0 \\ 1/3 \\ 1 \end{pmatrix}}$$

### 验证

$$A\boldsymbol{\xi}_1 = \begin{pmatrix} 1 & 1 & -1 & 2 \\ 2 & 2 & 1 & 3 \\ 1 & 1 & 2 & 1 \end{pmatrix}\begin{pmatrix} -1 \\ 1 \\ 0 \\ 0 \end{pmatrix} = \begin{pmatrix} -1+1+0+0 \\ -2+2+0+0 \\ -1+1+0+0 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \\ 0 \end{pmatrix} \;\checkmark$$

$$A\boldsymbol{\xi}_2 = \begin{pmatrix} -5/3+0-1/3+2 \\ -10/3+0+1/3+3 \\ -5/3+0+2/3+1 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \\ 0 \end{pmatrix} \;\checkmark$$

### 通解

$$\boxed{\boldsymbol{x} = c_1\begin{pmatrix} -1 \\ 1 \\ 0 \\ 0 \end{pmatrix} + c_2\begin{pmatrix} -5/3 \\ 0 \\ 1/3 \\ 1 \end{pmatrix},\quad c_1,c_2 \in \mathbb{R}}$$

如果嫌分数难看，$\boldsymbol{\xi}_2$ 乘以 3 仍是基础解系的向量（基可以缩放）：

$$\boldsymbol{\xi}_2' = \begin{pmatrix} -5 \\ 0 \\ 1 \\ 3 \end{pmatrix}$$

\newpage

## 例2：$2\times 5$ 矩阵，秩为 2

解方程组：

$$\begin{cases}
x_1 + 2x_2 - x_3 + 3x_4 + x_5 = 0 \\
2x_1 + 4x_2 + x_3 + x_4 - 2x_5 = 0
\end{cases}$$

### 行最简形

$$\begin{pmatrix} 1 & 2 & -1 & 3 & 1 \\ 2 & 4 & 1 & 1 & -2 \end{pmatrix} \xrightarrow{R_2-2R_1} \begin{pmatrix} 1 & 2 & -1 & 3 & 1 \\ 0 & 0 & 3 & -5 & -4 \end{pmatrix}$$

$$\xrightarrow{R_2/3} \begin{pmatrix} 1 & 2 & -1 & 3 & 1 \\ 0 & 0 & 1 & -5/3 & -4/3 \end{pmatrix} \xrightarrow{R_1+R_2} \begin{pmatrix} \boxed{1} & 2 & 0 & 4/3 & -1/3 \\ 0 & 0 & \boxed{1} & -5/3 & -4/3 \end{pmatrix}$$

### 主变量与自由变量

- 主元在第 1 列和第 3 列 → 主变量：$x_1$、$x_3$
- 自由变量：$x_2$、$x_4$、$x_5$

$n=5$，$r=2$ → 自由变量 3 个 → 基础解系含 **3 个向量**。

### 逐次赋值

| 赋值 | $x_2$ | $x_4$ | $x_5$ | 回代得 $x_3$ | 回代得 $x_1$ | 基础解系向量 |
|------|-------|-------|-------|-------------|-------------|------------|
| 第1组 | 1 | 0 | 0 | $x_3=0$ | $x_1=-2$ | $\boldsymbol{\xi}_1 = (-2,1,0,0,0)^T$ |
| 第2组 | 0 | 1 | 0 | $x_3=5/3$ | $x_1=-4/3$ | $\boldsymbol{\xi}_2 = (-4/3,0,5/3,1,0)^T$ |
| 第3组 | 0 | 0 | 1 | $x_3=4/3$ | $x_1=1/3$ | $\boldsymbol{\xi}_3 = (1/3,0,4/3,0,1)^T$ |

乘以 3 化简：

$$\boxed{\boldsymbol{\xi}_1 = \begin{pmatrix} -2 \\ 1 \\ 0 \\ 0 \\ 0 \end{pmatrix},\quad \boldsymbol{\xi}_2 = \begin{pmatrix} -4 \\ 0 \\ 5 \\ 3 \\ 0 \end{pmatrix},\quad \boldsymbol{\xi}_3 = \begin{pmatrix} 1 \\ 0 \\ 4 \\ 0 \\ 3 \end{pmatrix}}$$

### 通解

$$\boldsymbol{x} = c_1\boldsymbol{\xi}_1 + c_2\boldsymbol{\xi}_2 + c_3\boldsymbol{\xi}_3,\quad c_1,c_2,c_3 \in \mathbb{R}$$

\newpage

# 四、"逐个赋 1"为什么保证线性无关？

设我们有三个自由变量 $x_2,x_4,x_5$，构造的三个向量取值为：

| 向量 | $x_2$ | $x_4$ | $x_5$ |
|------|-------|-------|-------|
| $\boldsymbol{\xi}_1$ | **1** | 0 | 0 |
| $\boldsymbol{\xi}_2$ | 0 | **1** | 0 |
| $\boldsymbol{\xi}_3$ | 0 | 0 | **1** |

只看自由变量部分，这三个向量分别是 $\boldsymbol{e}_1,\boldsymbol{e}_2,\boldsymbol{e}_3$（标准单位向量）。它们显然线性无关。加上主变量分量后，**如果存在线性关系在自由分量上的投影也是同一个线性关系**——所以整个向量组也线性无关。

> 这就是"逐个赋 1"的数学原理——构造出的向量在自由变量部分形成**单位矩阵**的列，自然线性无关。

\newpage

# 五、常见错误

| 错误 | 纠正 |
|------|------|
| 自由变量全部赋 0 | 得到零向量，不是基础解系 |
| 忘记先化行最简形 | 行阶梯形不够，必须化到**行最简形**才能直接读出主变量与自由变量的关系 |
| 自由变量个数数错 | 自由变量数 = $n - r$，不是 $n$ 减去"非零行数"（非零行数 = $r$） |
| 多个自由变量时不知如何赋值 | 每次**只让一个**自由变量为 1，其余为 0 |
| 基础解系不唯一就认为算错 | 基础解系不唯一！任何一组基都可以。通常取上述构造的"最整齐"的那组 |

\newpage

# 六、步骤速查卡

```
A x = 0   (m个方程，n个未知数)
    │
    ▼
① 初等行变换 → 行最简形 (RREF)
    │  主元列标方框，其余为自由列
    ▼
② r = 主元个数 = rank(A)
   自由变量数 = n - r
    │
    ▼
③ 循环 i = 1, 2, ..., n-r:
   ├─ 第 i 个自由变量 = 1
   ├─ 其余自由变量 = 0
   ├─ 从行最简形回代，逐个解出主变量
   └─ 得到一个基础解系向量 ξᵢ
    │
    ▼
④ 通解: x = c₁ξ₁ + c₂ξ₂ + ... + c_{n-r}ξ_{n-r}
```

## 一句话总结

> 基础解系 = 自由变量逐个取 1、其余取 0、回代求主变量。本质是把 $n-r$ 维自由空间的标准基"拉回"到原方程的解空间中。$n-r$ 个向量线性无关，张成整个解空间。
"""

with open(r"d:\辰辰\first CC\fundamental_system.md", "w", encoding="utf-8") as f:
    f.write(content)

print("Markdown 已生成")
