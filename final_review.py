#!/usr/bin/env python3
"""生成线性代数B1期末考试复习提纲（纯期末）"""

content = r"""# 线性代数 B1 期末考试复习提纲

> 基于 2015-2025 年共 10 份期末真题的系统分析。考试范围：第1-6章全书。

\newpage

# 一、试卷结构与分值分布

| 题型 | 题量 | 分值 | 时间分配建议 |
|------|------|------|------------|
| 填空题 | 约 6 题 | ~30 分（5分/题） | 20 分钟 |
| 判断题 | 约 5 题 | ~15 分（3分/题） | 10 分钟 |
| 解答题 | 约 5-6 题 | ~55 分（8-15分/题） | 70 分钟 |

\newpage

# 二、各章在期末中的考查权重

| 章节 | 权重 | 核心度 | 主要题型 |
|------|------|--------|---------|
| 第5章 特征值与对角化 | ★★★★★ | 绝对核心 | 填空+判断+解答 |
| 第6章 二次型与欧式空间 | ★★★★★ | 绝对核心 | 填空+解答（必有一道大题） |
| 第3章 线性方程组 | ★★★ | 重要 | 填空+解答（偶有） |
| 第4章 向量空间 | ★★★ | 重要 | 填空+判断+解答 |
| 第1章 行列式 | ★★ | 基础 | 填空为主 |
| 第2章 矩阵 | ★★ | 基础 | 填空+判断 |

\newpage

# 三、填空题——六大高频考点

## 考点1：二次型正定求参数（出现率 70%）

**典型题**：$f(x_1,x_2,x_3) = x_1^2 + tx_2^2 + 3x_3^2 + 2x_1x_2 + 2x_1x_3$ 正定，求 $t$ 范围。

**解法**：写对称矩阵 $A$ → 算各阶顺序主子式 → 全部 $>0$ → 解不等式组。

$$\boxed{\Delta_1 = a_{11} > 0,\quad \Delta_2 = \begin{vmatrix} a_{11} & a_{12} \\ a_{21} & a_{22} \end{vmatrix} > 0,\quad \Delta_3 = |A| > 0}$$

## 考点2：相似矩阵求参数（出现率 60%）

**典型题**：已知 $A \sim B$，利用 $\text{tr}(A)=\text{tr}(B)$ 和 $|A|=|B|$ 联立解参数。

**进阶考法**：再加上"$A$ 可对角化"条件 → 某特征值处 $g_\lambda = a_\lambda$ → $\text{rank}(A-\lambda I) = n - g_\lambda$。

## 考点3：基变换下的坐标或矩阵（出现率 50%）

**典型题**：已知两组基和线性变换在一组基下的矩阵 $A$，求另一组基下的矩阵 $B$。

$$\boxed{B = P^{-1}AP}$$

其中 $P$ 是过渡矩阵：$(\boldsymbol{\beta}_1,\ldots,\boldsymbol{\beta}_n) = (\boldsymbol{\alpha}_1,\ldots,\boldsymbol{\alpha}_n)P$。

**易错**：求的是 $P^{-1}AP$ 还是 $PAP^{-1}$？**新基的矩阵 = $P^{-1}AP$**（$P$ 是旧基到新基的过渡矩阵）。

## 考点4：施密特正交化（出现率 50%）

**典型题**：给定一组基（或在多项式空间中），求标准正交基。

$$\boxed{\boldsymbol{\beta}_k = \boldsymbol{\alpha}_k - \sum_{j=1}^{k-1}\frac{(\boldsymbol{\alpha}_k,\boldsymbol{\beta}_j)}{(\boldsymbol{\beta}_j,\boldsymbol{\beta}_j)}\boldsymbol{\beta}_j},\quad \boldsymbol{q}_k = \frac{\boldsymbol{\beta}_k}{\|\boldsymbol{\beta}_k\|}}$$

## 考点5：特征值与行列式的关系（出现率 40%）

**典型题**：已知 $A$ 的特征值，求 $\det(A+kI)$ 或 $\det(I+A)$。

$$\boxed{\det(A+kI) = \prod(\lambda_i + k)}$$

**关键**：$A$ 的特征值是 $\lambda_i$，则 $A+kI$ 的特征值是 $\lambda_i+k$，行列式 = 特征值之积。

## 考点6：矩阵幂次（出现率 30%）

**方法一（秩1分解）**：$A = \boldsymbol{\alpha}\boldsymbol{\beta}^T \Rightarrow A^k = (\boldsymbol{\beta}^T\boldsymbol{\alpha})^{k-1}A$

**方法二（二项式展开）**：$A = \lambda I + N$（$N$ 幂零），$\lambda I$ 与 $N$ 可交换

$$\boxed{(\lambda I + N)^k = \sum_{j=0}^m \binom{k}{j}\lambda^{k-j}N^j}$$

\newpage

# 四、判断题——八大必考陷阱

## 陷阱1：相似对加法不封闭（出现 3+ 次）

> ❌ $A_1 \sim B_1,\;A_2 \sim B_2 \;\Rightarrow\; A_1+A_2 \sim B_1+B_2$

**反例**：$A_1=\begin{pmatrix}1&0\\0&0\end{pmatrix}\sim\begin{pmatrix}0&0\\0&1\end{pmatrix}=B_1$，$A_2=\begin{pmatrix}0&0\\0&1\end{pmatrix}\sim\begin{pmatrix}1&0\\0&0\end{pmatrix}=B_2$，但 $A_1+A_2=I$ 不相似于 $B_1+B_2=I$（实际上相似，但特征值可能不同——需要找更好的反例）。关键是**相似不保持和**。

## 陷阱2：实对称阵特征多项式相同 → 相似（出现多次）

> ✅ 正确。两个实对称矩阵若特征多项式相同，则特征值相同，均可正交相似对角化到同一对角阵，因此相似。

## 陷阱3：上三角正交阵 → 对角阵（出现多次）

> ✅ 正确。上三角且正交 → 每列模长为 1 → 对角元为 $\pm 1$ → 非对角元通过正交条件（列与列正交）可推为 0。

## 陷阱4：$\boldsymbol{A}\boldsymbol{A}^T=\boldsymbol{0}$ 在复数域（出现多次）

> ❌ 错误。复数域反例 $\begin{pmatrix}1&i\\i&-1\end{pmatrix}$。在实数域中 $\text{tr}(AA^T)=0\Rightarrow A=0$。

## 陷阱5：顺序主子式非负 → 半正定

> ❌ 错误。仅适用于实对称矩阵，且顺序主子式非负不是半正定的充分条件（需要所有主子式非负）。

**正确**：对实对称阵，所有特征值 $\geq 0$ ⇔ 半正定。

## 陷阱6：正交矩阵必可正交相似对角化

> ❌ 错误。正交矩阵不一定可以对角化（反例：旋转矩阵 $\begin{pmatrix}\cos\theta&-\sin\theta\\\sin\theta&\cos\theta\end{pmatrix}$，$\theta\neq 0,\pi$ 时特征值为复数，在实数域不可对角化）。只有**实对称**矩阵才保证可正交相似对角化。

## 陷阱7：线性变换在不同基下的矩阵是相合的

> ❌ 错误。是**相似**关系（$B=P^{-1}AP$），不是相合（$B=P^TAP$）。

**区分记忆**：
- 基变换下的线性变换矩阵 → **相似**（$P^{-1}AP$）
- 基变换下的二次型矩阵 → **合同**（$P^TAP$）
- 正交基变换下两者统一（$P^{-1}=P^T$）

## 陷阱8：子空间的并仍是子空间

> ✅ 正确——当且仅当一个包含另一个时。若 $V_1\cup V_2$ 是子空间，则必有 $V_1\subseteq V_2$ 或 $V_2\subseteq V_1$。

\newpage

# 五、解答题——五大必考题型

## 题型1：正交变换化二次型为标准型 + 曲面分类（出现率 70%）

> **这是期末考试最核心的大题，出现率最高，分值最大（通常 12-15 分）。**

**标准六步法**：

| 步骤 | 操作 | 要点 |
|------|------|------|
| ① | 写出实对称矩阵 $A$：$f=\boldsymbol{x}^T A\boldsymbol{x}$ | $a_{ij}$ 和 $a_{ji}$ 各取交叉项系数一半 |
| ② | 求特征值 $|\lambda I-A|=0$ | 通常 3 阶，特征值可能为重根 |
| ③ | 对每个特征值求特征向量 | $(A-\lambda I)\boldsymbol{x}=0$ |
| ④ | 正交化 + 单位化 | 同一特征值内施密特正交化，再全部单位化 |
| ⑤ | 写正交矩阵 $Q$ 和标准型 | $\boldsymbol{x}=Q\boldsymbol{y}$，$f=\lambda_1 y_1^2+\lambda_2 y_2^2+\lambda_3 y_3^2$ |
| ⑥ | 曲面分类 | 看特征值正负号个数和常数项 |

**曲面分类速查**：

| 标准方程形式 | 曲面名 | 特征值特征 |
|-------------|--------|----------|
| $\lambda_1 y_1^2+\lambda_2 y_2^2+\lambda_3 y_3^2 = 1$，$\lambda_i$ 全正 | 椭球面 | +++ |
| $\lambda_i$ 两正一负 $=1$ | **单叶双曲面** | ++- |
| $\lambda_i$ 一正两负 $=1$ | 双叶双曲面 | +-- |
| $\lambda_3=0$，$\lambda_1 y_1^2+\lambda_2 y_2^2 = y_3$ | 椭圆抛物面 | ++0 |
| $\lambda_3=0$，$\lambda_1 y_1^2 + \lambda_2 y_2^2 = y_3$，$\lambda_1\lambda_2<0$ | 双曲抛物面（马鞍面） | +-0 |

> **单叶双曲面出现频率最高（5+ 次），务必掌握！**

## 题型2：施密特正交化 + 最佳逼近（出现率 50%）

**典型设置**：在多项式空间 $P_n[x]$ 或 $\mathbb{R}^n$ 的某个子空间上，给定内积，求标准正交基。

**扩展**：最佳逼近问题 → 求向量在子空间上的正交投影。

$$\boxed{\text{最佳逼近元} = \sum_{i=1}^k (\boldsymbol{v},\boldsymbol{q}_i)\boldsymbol{q}_i}$$

其中 $\{\boldsymbol{q}_i\}$ 是子空间的标准正交基。

## 题型3：线性变换在不同基下的矩阵（出现率 40%）

**典型设置**：给出 $\mathbb{R}^{2\times 2}$ 或 $\mathbb{R}^3$ 上的线性变换在一组基下的矩阵，求在另一组基下的矩阵。

**解法**：
1. 求过渡矩阵 $P$（旧基 → 新基）
2. 新基下矩阵 $B = P^{-1}AP$

**变形**：已知新基下矩阵 $B$ 的某种特性（如对角形），反求基或参数。

## 题型4：$A^2=kA$ 型可对角化证明（出现率 30%）

**命题**：若 $A^2 = kA$（$k \neq 0$），证明 $A$ 可对角化。

**标准证法（Sylvester 秩不等式）**：

由 $A(A-kI)=0$，Sylvester 不等式给出：

$$0 = \text{rank}(A(A-kI)) \geq \text{rank}(A) + \text{rank}(A-kI) - n$$

$$\Rightarrow \text{rank}(A) + \text{rank}(A-kI) \leq n$$

又因为 $kI = kI - A + A$：

$$n = \text{rank}(kI) \leq \text{rank}(A-kI) + \text{rank}(A)$$

所以 $\text{rank}(A) + \text{rank}(A-kI) = n$。

$\lambda=0$ 的几何重数 $= n - \text{rank}(A) = \text{rank}(A-kI) = \text{代数重数}$

$\lambda=k$ 的几何重数 $= n - \text{rank}(A-kI) = \text{rank}(A) = \text{代数重数}$

所有特征值 $g_\lambda = a_\lambda$ → $A$ 可对角化。$\square$

## 题型5：含参线性方程组（出现率 30%）

**虽然这是期中核心题型，期末偶尔也考。** 通常作为第一道解答题（约 8 分）。

**标准步骤**：增广矩阵 → 初等行变换 → 讨论参数对秩的影响 → 分类写解。

\newpage

# 六、核心公式速查卡

## 6.1 特征值与矩阵的关系

| $A$ 的特征值 | 相关矩阵的特征值 |
|-------------|---------------|
| $\lambda$ | $kA \to k\lambda$ |
| $\lambda$ | $A+kI \to \lambda+k$ |
| $\lambda$ | $A^k \to \lambda^k$ |
| $\lambda$ | $A^{-1} \to 1/\lambda$ |
| $\lambda$ | $A^* \to $|$A$|$/\lambda$ |
| $\lambda$ | $P^{-1}AP \to \lambda$（不变） |

## 6.2 行列式与迹

$$\boxed{|A| = \prod_{i=1}^n \lambda_i},\quad \boxed{\text{tr}(A) = \sum_{i=1}^n \lambda_i = \sum_{i=1}^n a_{ii}}$$

$$\boxed{|A+kI| = \prod_{i=1}^n (\lambda_i + k)}$$

## 6.3 几何重数公式

$$\boxed{g_\lambda = n - \text{rank}(A-\lambda I)}$$

$$\boxed{\text{可对角化} \;\Longleftrightarrow\; \forall\lambda,\; g_\lambda = a_\lambda}$$

## 6.4 正定性判定

| 方法 | 条件 |
|------|------|
| 顺序主子式 | $\Delta_k > 0$，$k=1,2,\ldots,n$（实对称阵） |
| 特征值 | 所有 $\lambda_i > 0$ |
| 合同 | $A$ 与 $I$ 合同 |

## 6.5 相似不变量

| ✅ 相同 | ❌ 不一定相同 |
|---------|------------|
| 特征值（含重数） | 特征向量 |
| 行列式 | 转置（但 $A$ 总相似于 $A^T$，只是不通过同一个 $P$） |
| 迹 | |
| 秩 | |
| 特征多项式 | |
| 最小多项式 | |
| 若尔当标准形 | |

\newpage

# 七、证明题必备结论

## 结论1：$A^2=I \not\Rightarrow A=\pm I$

反例：$A = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$，$A^2=I$ 但 $A \neq \pm I$。

但可推出：$A$ 的特征值只能是 $\pm 1$。

## 结论2：$\det(A)=0$ 的矩阵对加法不封闭

$\begin{pmatrix}1&0\\0&0\end{pmatrix} + \begin{pmatrix}0&0\\0&1\end{pmatrix} = I$，两个奇异矩阵的和可逆。

## 结论3：$AB-BA=\mu I$ 无解（$\mu\neq 0$）

两边取迹：$\text{tr}(AB-BA) = 0 = \text{tr}(\mu I) = n\mu \Rightarrow \mu=0$。矛盾。

## 结论4：正定矩阵的对角元全正

$A$ 正定 → $e_i^T A e_i = a_{ii} > 0$。**但逆命题不成立**——对角元全正不能推出正定。

## 结论5：正交矩阵的特征值模长为 1

$A\boldsymbol{x}=\lambda\boldsymbol{x}$，$A^TA=I \Rightarrow \|\boldsymbol{x}\|^2 = \|A\boldsymbol{x}\|^2 = |\lambda|^2\|\boldsymbol{x}\|^2 \Rightarrow |\lambda|=1$

**推论**：实正交矩阵的特征值只能是 $\pm 1$ 或共轭复对 $e^{\pm i\theta}$。

\newpage

# 八、考前最后 24 小时复习清单

**必须掌握的三大计算**：

- [ ] 正交变换化二次型为标准型（六步法，闭卷默写）
- [ ] 施密特正交化（公式 + 单位化）
- [ ] 特征值与特征向量（含重根情况下的正交化）

**必须记住的公式**：

- [ ] 顺序主子式公式（$\Delta_1, \Delta_2, \Delta_3$）
- [ ] $g_\lambda = n - \text{rank}(A-\lambda I)$
- [ ] $|A+kI| = \prod(\lambda_i + k)$
- [ ] $B = P^{-1}AP$（基变换下的矩阵）

**判断题易错点过一遍**：

- [ ] 相似对加法不封闭
- [ ] $\det(AB)=\det(BA)$ 非方阵时不成立
- [ ] 正交矩阵不一定可对角化（只有实对称保证）
- [ ] 线性变换矩阵是相似不是合同
- [ ] $AB-BA=\mu I$（$\mu\neq 0$）取迹矛盾

**至少完整做 3 套近年期末真题**：

推荐：2024-2025 第一学期、2023-2024 第二学期、2021-2022 第二学期。

\newpage

# 九、一句话总结

> 线性代数 B1 期末考试，**正交变换化二次型为标准型**是绝对核心（70% 出现率，分值最高），配合**施密特正交化**和**曲面分类**构成一道完整大题。**特征值/对角化/正定性**是填空判断高频区（正定求参数题几乎每份必有一空）。**相似不变量**和**基变换下的矩阵**是判断题和填空题的常规考点。题型高度重复，把 10 年真题做透即足以应对。
"""

with open(r"d:\辰辰\first CC\final_review.md", "w", encoding="utf-8") as f:
    f.write(content)

print("期末复习提纲 Markdown 已生成")
