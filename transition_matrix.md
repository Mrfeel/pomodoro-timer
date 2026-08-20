# 过渡矩阵的求法——纯计算实用指南

> 过渡矩阵连接两组基，是基变换和坐标变换的核心工具。以下只讲怎么算。

\newpage

# 一、过渡矩阵是什么？

## 1.1 一句话定义

$$\boxed{(\boldsymbol{\beta}_1,\ldots,\boldsymbol{\beta}_n) = (\boldsymbol{\alpha}_1,\ldots,\boldsymbol{\alpha}_n)P}$$

$P$ 是**旧基 $\{\boldsymbol{\alpha}_i\}$ 到新基 $\{\boldsymbol{\beta}_i\}$** 的过渡矩阵。

- $P$ 的第 $j$ 列 = $\boldsymbol{\beta}_j$ 在旧基 $\{\boldsymbol{\alpha}_i\}$ 下的**坐标**

## 1.2 记法（避免方向搞反）

$$\boxed{\text{新基} = \text{旧基} \times P \quad\Rightarrow\quad P = \text{旧基}^{-1} \times \text{新基}}$$

> **口诀**：旧基乘 P 得新基，P = 旧基逆乘新基。

\newpage

# 二、标准求法——两矩阵法

## 方法一：公式法（最直接）

把两组基的向量**按列排成矩阵**：

$$A = (\boldsymbol{\alpha}_1,\ldots,\boldsymbol{\alpha}_n),\quad B = (\boldsymbol{\beta}_1,\ldots,\boldsymbol{\beta}_n)$$

$$\boxed{P = A^{-1}B}$$

## 方法二：增广矩阵法（推荐，避免求逆）

对 $(A \mid B)$ 做初等行变换，将左边化为 $I$，右边即为 $P$：

$$\boxed{(A \mid B) \;\xrightarrow{\text{行变换}}\; (I \mid P)}$$

**两步合一**：行变换做 $A^{-1}B$ 比先求 $A^{-1}$ 再乘 $B$ 更快。

\newpage

# 三、手把手例题

## 例1：$\mathbb{R}^3$ 中数字向量基

旧基：$\boldsymbol{\alpha}_1=\begin{pmatrix} 1 \\ 1 \\ 0 \end{pmatrix},\;\boldsymbol{\alpha}_2=\begin{pmatrix} 0 \\ 1 \\ 1 \end{pmatrix},\;\boldsymbol{\alpha}_3=\begin{pmatrix} 1 \\ 0 \\ 1 \end{pmatrix}$

新基：$\boldsymbol{\beta}_1=\begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix},\;\boldsymbol{\beta}_2=\begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix},\;\boldsymbol{\beta}_3=\begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix}$

求旧基到新基的过渡矩阵 $P$。

### 列矩阵

$$A = \begin{pmatrix} 1 & 0 & 1 \\ 1 & 1 & 0 \\ 0 & 1 & 1 \end{pmatrix},\quad B = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix} = I$$

$$P = A^{-1}B = A^{-1}I = A^{-1}$$

$$A^{-1} = \frac{1}{2}\begin{pmatrix} 1 & 1 & -1 \\ -1 & 1 & 1 \\ 1 & -1 & 1 \end{pmatrix}$$

$$\boxed{P = \frac{1}{2}\begin{pmatrix} 1 & 1 & -1 \\ -1 & 1 & 1 \\ 1 & -1 & 1 \end{pmatrix}}$$

**验证**：$AP = I = B$ ✓

### 当新基是标准基时

**$P = A^{-1}$**，即旧基矩阵的逆。这是一个重要的特例！

\newpage

## 例2：$\mathbb{R}^{2\times 2}$ 矩阵空间

基1：$E_{11}=\begin{pmatrix}1&0\\0&0\end{pmatrix},\;E_{12}=\begin{pmatrix}0&1\\0&0\end{pmatrix},\;E_{21}=\begin{pmatrix}0&0\\1&0\end{pmatrix},\;E_{22}=\begin{pmatrix}0&0\\0&1\end{pmatrix}$

基2：$F_1=\begin{pmatrix}1&0\\1&0\end{pmatrix},\;F_2=\begin{pmatrix}0&1\\0&1\end{pmatrix},\;F_3=\begin{pmatrix}1&0\\0&1\end{pmatrix},\;F_4=\begin{pmatrix}0&1\\1&0\end{pmatrix}$

求基 1 到基 2 的过渡矩阵。

### 关键：先把矩阵"拉直"成向量

将 $2\times 2$ 矩阵按列（或按行）排成 4 维向量。这里按列排：

$$E_{11}\to\begin{pmatrix}1\\0\\0\\0\end{pmatrix},\;E_{12}\to\begin{pmatrix}0\\1\\0\\0\end{pmatrix},\;E_{21}\to\begin{pmatrix}0\\0\\1\\0\end{pmatrix},\;E_{22}\to\begin{pmatrix}0\\0\\0\\1\end{pmatrix}$$

（这恰好是 $\mathbb{R}^4$ 的标准基，$A = I_4$）

$$F_1\to\begin{pmatrix}1\\0\\1\\0\end{pmatrix},\;F_2\to\begin{pmatrix}0\\1\\0\\1\end{pmatrix},\;F_3\to\begin{pmatrix}1\\0\\0\\1\end{pmatrix},\;F_4\to\begin{pmatrix}0\\1\\1\\0\end{pmatrix}$$

$$A = I_4,\quad B = \begin{pmatrix} 1 & 0 & 1 & 0 \\ 0 & 1 & 0 & 1 \\ 1 & 0 & 0 & 1 \\ 0 & 1 & 1 & 0 \end{pmatrix}$$

$$P = A^{-1}B = B = \begin{pmatrix} 1 & 0 & 1 & 0 \\ 0 & 1 & 0 & 1 \\ 1 & 0 & 0 & 1 \\ 0 & 1 & 1 & 0 \end{pmatrix}$$

\newpage

# 四、过渡矩阵与坐标变换——容易混淆！

## 4.1 基变换 vs 坐标变换

| | 基变换 | 坐标变换 |
|--|--------|---------|
| 关系 | $B = AP$ | $\boldsymbol{x} = A\boldsymbol{x}_A = B\boldsymbol{x}_B$ |
| 公式 | 新基 = 旧基 $\times P$ | $\boldsymbol{x}_B = P^{-1}\boldsymbol{x}_A$ |
| 口诀 | 旧到新乘 $P$ | 旧坐标到新坐标**乘 $P^{-1}$** |

## 4.2 为什么坐标变换是 $P^{-1}$？

同一个向量在两组基下的表示：

$$\boldsymbol{x} = (\boldsymbol{\alpha}_1,\ldots,\boldsymbol{\alpha}_n)\begin{pmatrix} x_1 \\ \vdots \\ x_n \end{pmatrix}_{\text{旧}} = (\boldsymbol{\beta}_1,\ldots,\boldsymbol{\beta}_n)\begin{pmatrix} y_1 \\ \vdots \\ y_n \end{pmatrix}_{\text{新}}$$

$$A\boldsymbol{x}_{\text{旧}} = B\boldsymbol{x}_{\text{新}} = AP\boldsymbol{x}_{\text{新}}$$

$$A\boldsymbol{x}_{\text{旧}} = AP\boldsymbol{x}_{\text{新}} \;\Rightarrow\; \boldsymbol{x}_{\text{旧}} = P\boldsymbol{x}_{\text{新}} \;\Rightarrow\; \boxed{\boldsymbol{x}_{\text{新}} = P^{-1}\boldsymbol{x}_{\text{旧}}}$$

> **基变换乘 $P$，坐标变换乘 $P^{-1}$。两者方向相反！**

\newpage

# 五、线性变换在不同基下的矩阵

这是期末考试的热门题型。已知线性变换 $\mathcal{A}$ 在旧基下的矩阵为 $A$，$P$ 是旧基到新基的过渡矩阵，则：

$$\boxed{B = P^{-1}AP}$$

$B$ 是 $\mathcal{A}$ 在新基下的矩阵。

**三个量之间的关系**：

```
    旧基下的矩阵 A
         │
    P⁻¹AP│  （相似变换）
         ▼
    新基下的矩阵 B = P⁻¹AP
```

\newpage

# 六、考试速查

| 问题 | 公式 | 注意事项 |
|------|------|---------|
| 求过渡矩阵 $P$ | $P = A^{-1}B$ | 增广矩阵法：$(A\mid B) \to (I\mid P)$ |
| 旧坐标 → 新坐标 | $\boldsymbol{x}_{\text{新}} = P^{-1}\boldsymbol{x}_{\text{旧}}$ | 是 $P^{-1}$ 不是 $P$！ |
| 新坐标 → 旧坐标 | $\boldsymbol{x}_{\text{旧}} = P\boldsymbol{x}_{\text{新}}$ | |
| 旧基下矩阵 → 新基下矩阵 | $B = P^{-1}AP$ | 相似关系 |
| 新基是标准基时 | $P = A^{-1}$ | 旧基矩阵的逆 |

## 一句话总结

> $P = A^{-1}B$（旧基矩阵的逆 × 新基矩阵）。增广矩阵法一行变换到底，省去单独求逆。坐标变换是 $P^{-1}$（不是 $P$），线性变换矩阵是 $P^{-1}AP$。
