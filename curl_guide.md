# 旋度的计算 — 电磁学中的核心数学工具

> 电磁学四大方程中两个是旋度方程：$\nabla\times\boldsymbol{E}=-\partial\boldsymbol{B}/\partial t$ 和 $\nabla\times\boldsymbol{H}=\boldsymbol{j}+\partial\boldsymbol{D}/\partial t$。掌握旋度计算是理解电磁学的数学基础。

\newpage

# 一、旋度的物理意义

## 1.1 定义

旋度衡量矢量场在某点附近的**"旋转程度"**：

$$\nabla\times\boldsymbol{F} = \lim_{\Delta S\to 0}\frac{1}{\Delta S}\oint_L\boldsymbol{F}\cdot d\boldsymbol{l}$$

即：围绕该点取一小面元 $\Delta S$，$\boldsymbol{F}$ 沿面元边界的环量除以面积，当面积趋于零时的极限。

## 1.2 如何"看出来"旋度是否为零

```
旋度 ≠ 0（有旋场）              旋度 = 0（无旋场）
┌───→───→───┐                    ─→─→─→─→─→─→─
│           ↓                   
↑           ↓                   所有箭头同方向
│           ↓                   且大小均匀 →
└←───←───←──┘                   
箭头形成漩涡状                  箭头不形成漩涡
```

**电磁学中最重要的例子**：

| 场 | 旋度 | 物理意义 |
|----|------|---------|
| 静电场 $\boldsymbol{E}$ | $\nabla\times\boldsymbol{E}=0$ | **无旋场**（可定义标量势 $\varphi$） |
| 涡旋电场 $\boldsymbol{E}$ | $\nabla\times\boldsymbol{E}=-\partial\boldsymbol{B}/\partial t\neq 0$ | **有旋场**（不能定义标量势！） |
| 磁场 $\boldsymbol{B}$（有电流处） | $\nabla\times\boldsymbol{B}=\mu_0\boldsymbol{j}$ | 电流是磁场的"旋度源" |

## 1.3 散度 vs. 旋度（一眼区分）

| | 散度 $\nabla\cdot\boldsymbol{F}$ | 旋度 $\nabla\times\boldsymbol{F}$ |
|--|-------------------------------|-------------------------------|
| 衡量 | "源"的强弱（向外发散的程度） | "旋转"的强弱（环绕的程度） |
| 结果 | 标量 | 矢量 |
| 电磁学例子 | $\nabla\cdot\boldsymbol{D}=\rho_f$ | $\nabla\times\boldsymbol{H}=\boldsymbol{j}_f$ |
| 场的类型 | 有散场（电力线有起点终点） | 有旋场（磁力线是闭合的） |

\newpage

# 二、直角坐标系中的旋度公式（最常用）

## 2.1 行列式记忆法

$$\nabla\times\boldsymbol{F} = \begin{vmatrix} \hat{\boldsymbol{x}} & \hat{\boldsymbol{y}} & \hat{\boldsymbol{z}} \\ \frac{\partial}{\partial x} & \frac{\partial}{\partial y} & \frac{\partial}{\partial z} \\ F_x & F_y & F_z \end{vmatrix}$$

展开（按第一行）：

$$\nabla\times\boldsymbol{F} = \hat{\boldsymbol{x}}\left(\frac{\partial F_z}{\partial y}-\frac{\partial F_y}{\partial z}\right) + \hat{\boldsymbol{y}}\left(\frac{\partial F_x}{\partial z}-\frac{\partial F_z}{\partial x}\right) + \hat{\boldsymbol{z}}\left(\frac{\partial F_y}{\partial x}-\frac{\partial F_x}{\partial y}\right)$$

## 2.2 循环记忆法（推荐！）

记住三条规则——它们是循环对称的：

| 分量 | 公式 | 循环关系 |
|------|------|---------|
| $(\nabla\times\boldsymbol{F})_x$ | $\dfrac{\partial F_z}{\partial y} - \dfrac{\partial F_y}{\partial z}$ | $x\to y\to z\to x$ |
| $(\nabla\times\boldsymbol{F})_y$ | $\dfrac{\partial F_x}{\partial z} - \dfrac{\partial F_z}{\partial x}$ | 上一行的 $x,y,z$ 各后移一位 |
| $(\nabla\times\boldsymbol{F})_z$ | $\dfrac{\partial F_y}{\partial x} - \dfrac{\partial F_x}{\partial y}$ | 再后移一位 |

**口诀**：$x$ 分量 = $\partial F_z/\partial y - \partial F_y/\partial z$（"后减前"，按 $x\to y\to z\to x$ 循环）

## 2.3 例题：验证静电场无旋

点电荷电场 $\boldsymbol{E} = \dfrac{q}{4\pi\varepsilon_0}\dfrac{\boldsymbol{r}}{r^3}$，分量形式 $E_x=\dfrac{q}{4\pi\varepsilon_0}\dfrac{x}{(x^2+y^2+z^2)^{3/2}}$。

计算 $(\nabla\times\boldsymbol{E})_z = \dfrac{\partial E_y}{\partial x} - \dfrac{\partial E_x}{\partial y}$：

$$\frac{\partial E_y}{\partial x} = \frac{q}{4\pi\varepsilon_0}\frac{-3xy}{r^5},\quad \frac{\partial E_x}{\partial y} = \frac{q}{4\pi\varepsilon_0}\frac{-3xy}{r^5}$$

两者相等 → $(\nabla\times\boldsymbol{E})_z=0$。同理各分量均为零 → $\nabla\times\boldsymbol{E}=0$。**任何球对称径向场的旋度都为零。**

\newpage

# 三、柱坐标和球坐标系中的旋度

## 3.1 柱坐标系 $(s,\varphi,z)$

$$\nabla\times\boldsymbol{F} = \hat{\boldsymbol{s}}\left(\frac{1}{s}\frac{\partial F_z}{\partial\varphi}-\frac{\partial F_\varphi}{\partial z}\right) + \hat{\boldsymbol{\varphi}}\left(\frac{\partial F_s}{\partial z}-\frac{\partial F_z}{\partial s}\right) + \hat{\boldsymbol{z}}\frac{1}{s}\left(\frac{\partial(sF_\varphi)}{\partial s}-\frac{\partial F_s}{\partial\varphi}\right)$$

**电磁学中最常用的情况**（轴对称：$F_z=0$，$F_s=0$，$F_\varphi$ 只依赖于 $s$）：

$$(\nabla\times\boldsymbol{F})_z = \frac{1}{s}\frac{\partial(sF_\varphi)}{\partial s}$$

## 3.2 球坐标系 $(r,\theta,\varphi)$

$$\nabla\times\boldsymbol{F} = \hat{\boldsymbol{r}}\frac{1}{r\sin\theta}\left(\frac{\partial(\sin\theta F_\varphi)}{\partial\theta}-\frac{\partial F_\theta}{\partial\varphi}\right) + \hat{\boldsymbol{\theta}}\frac{1}{r}\left(\frac{1}{\sin\theta}\frac{\partial F_r}{\partial\varphi}-\frac{\partial(rF_\varphi)}{\partial r}\right) + \hat{\boldsymbol{\varphi}}\frac{1}{r}\left(\frac{\partial(rF_\theta)}{\partial r}-\frac{\partial F_r}{\partial\theta}\right)$$

# 四、电磁学中旋度的三大应用

## 4.1 验证静电场无旋 → 可定义电势

判断 $\nabla\times\boldsymbol{E}=0$ 是否成立，是区分"静电场"和"涡旋电场"的关键。

$$\nabla\times\boldsymbol{E}=0 \Rightarrow \boldsymbol{E}=-\nabla\varphi \quad\text{（电势存在）}$$
$$\nabla\times\boldsymbol{E}\neq 0 \Rightarrow \text{不能定义标量势 } \varphi$$

## 4.2 由磁矢势计算磁场 $\boldsymbol{B}=\nabla\times\boldsymbol{A}$

这是旋度在电磁学中最直接的应用。给定 $\boldsymbol{A}$，求旋度即得 $\boldsymbol{B}$。

**经典例题**：磁偶极子的矢势 $\boldsymbol{A} = \dfrac{\mu_0}{4\pi}\dfrac{\boldsymbol{m}\times\hat{\boldsymbol{r}}}{r^2}$。通过计算 $\boldsymbol{B}=\nabla\times\boldsymbol{A}$ 可得磁偶极子场：

$$\boldsymbol{B} = \frac{\mu_0}{4\pi r^3}[3(\boldsymbol{m}\cdot\hat{\boldsymbol{r}})\hat{\boldsymbol{r}}-\boldsymbol{m}]$$

## 4.3 验证安培环路定理的微分形式 $\nabla\times\boldsymbol{B}=\mu_0\boldsymbol{j}$

已知磁场分布，求旋度即可得到电流分布。反之亦然。

\newpage

# 五、手把手例题演示

## 例题1：无限长直导线的磁场旋度

已知 $B_\varphi = \dfrac{\mu_0 I}{2\pi s}$（柱坐标，仅 $\varphi$ 分量，只依赖于 $s$）。

用柱坐标旋度公式（轴对称简化版）：

$$(\nabla\times\boldsymbol{B})_z = \frac{1}{s}\frac{\partial(sB_\varphi)}{\partial s} = \frac{1}{s}\frac{\partial}{\partial s}\left(s\cdot\frac{\mu_0 I}{2\pi s}\right) = \frac{1}{s}\frac{\partial}{\partial s}\left(\frac{\mu_0 I}{2\pi}\right) = 0 \quad (s>0)$$

$s>0$ 处 $\nabla\times\boldsymbol{B}=0$——导线外部无电流，旋度为零。导线所在处（$s\to 0$）$\nabla\times\boldsymbol{B}$ 发散，对应 $\delta$ 函数型的电流分布。这正是安培环路定理 $\nabla\times\boldsymbol{B}=\mu_0\boldsymbol{j}$ 的体现——旋度只在有电流处非零。

## 例题2：均匀变化磁场产生的涡旋电场

螺线管内 $B_z = \mu_0 n I(t)$，$dB/dt = k$（常数）。涡旋电场只有 $\varphi$ 分量，轴对称。

法拉第定律微分形式：$\nabla\times\boldsymbol{E} = -\partial\boldsymbol{B}/\partial t = -k\hat{\boldsymbol{z}}$。

在柱坐标中轴对称的 $\boldsymbol{E}=E_\varphi(s)\hat{\boldsymbol{\varphi}}$，其旋度：

$$(\nabla\times\boldsymbol{E})_z = \frac{1}{s}\frac{\partial(sE_\varphi)}{\partial s} = -k$$

$$\frac{\partial(sE_\varphi)}{\partial s} = -ks \quad\Rightarrow\quad sE_\varphi = -\frac{1}{2}ks^2 + C$$

$s=0$ 处 $E_\varphi$ 应为有限值→$C=0$：

$$E_\varphi = -\frac{1}{2}ks = -\frac{1}{2}\mu_0 n\frac{dI}{dt}s$$

与法拉第定律积分形式所得结果完全一致。

## 例题3：磁化电流 $\boldsymbol{j}'=\nabla\times\boldsymbol{M}$

均匀磁化圆柱 $\boldsymbol{M}=M_0\hat{\boldsymbol{z}}$（$s<a$），$\boldsymbol{M}=0$（$s>a$）。

柱坐标中 $\boldsymbol{M}$ 只有 $z$ 分量且只依赖于 $s$，旋度：

$$\nabla\times\boldsymbol{M} = \hat{\boldsymbol{\varphi}}\left(-\frac{\partial M_z}{\partial s}\right)$$

体磁化电流 $\boldsymbol{j}'=\nabla\times\boldsymbol{M}$：
- $s<a$（均匀磁化）：$\partial M_z/\partial s=0$ → $\boldsymbol{j}'=0$
- $s=a$（表面，$M_z$ 突变）：产生面磁化电流 $\boldsymbol{i}'=\boldsymbol{M}\times\hat{\boldsymbol{n}}=M_0\hat{\boldsymbol{z}}\times\hat{\boldsymbol{s}}=M_0\hat{\boldsymbol{\varphi}}$

这与用 $\boldsymbol{i}'=\boldsymbol{M}\times\hat{\boldsymbol{n}}$ 计算的结果一致——旋度公式自动包含了表面不连续性的贡献。

\newpage

# 六、考试中旋度的计算速查

## 常见矢量场的旋度（值得记住！）

| 矢量场 | 旋度 | 何时用到 |
|--------|------|---------|
| 径向场 $\boldsymbol{F}=f(r)\hat{\boldsymbol{r}}$ | $\boldsymbol{0}$（球对称径向场恒无旋） | 验证静电场无旋 |
| 环向场 $\boldsymbol{F}=f(s)\hat{\boldsymbol{\varphi}}$（柱坐标） | $\hat{\boldsymbol{z}}\frac{1}{s}\frac{d(sf)}{ds}$ | 直线电流磁场、涡旋电场 |
| 轴向均匀场 $\boldsymbol{F}=C\hat{\boldsymbol{z}}$ | $\boldsymbol{0}$ | 螺线管内磁场 |
| $y\hat{\boldsymbol{x}}$ 或 $x\hat{\boldsymbol{y}}$ | $\pm\hat{\boldsymbol{z}}$ | 剪切流场示例 |

## 哪些场的旋度一定为零？

以下矢量场的旋度恒为零，**无需计算即可判断**：
1. 任何球对称的径向场 $\boldsymbol{F}=f(r)\hat{\boldsymbol{r}}$
2. 任何均匀矢量场 $\boldsymbol{F}=\text{const}$
3. 任何可写成梯度的场 $\boldsymbol{F}=\nabla\psi$（$\nabla\times(\nabla\psi)\equiv 0$——旋度的梯度恒为零）

## 考试技巧

1. **判断坐标系**：看场的对称性——球对称→球坐标；轴对称→柱坐标；无对称性→直角坐标
2. **简化分量**：大多数EM问题中，场只有一个或两个非零分量，大大简化旋度计算
3. **先判断再计算**：如果场是标量势的梯度（$\boldsymbol{E}=-\nabla\varphi$），那旋度必为零，不用算
4. **利用积分形式**：如果只需求环量 $\oint\boldsymbol{F}\cdot d\boldsymbol{l}$，直接用对称性+定理，不必先求旋度再面积分

\newpage

# 七、一句话总结

> **旋度 = 场的"涡旋强度"**。直角坐标用行列式展开，柱坐标记 $\frac{1}{s}\frac{\partial(sF_\varphi)}{\partial s}$，球对称径向场旋度恒为零。
>
> 电磁学中：**静电场无旋**（$\nabla\times\boldsymbol{E}=0$）所以有电势；**磁场有旋**（$\nabla\times\boldsymbol{B}=\mu_0\boldsymbol{j}$）所以电流是磁场的旋度源；**变化磁场产生有旋电场**（$\nabla\times\boldsymbol{E}=-\partial\boldsymbol{B}/\partial t$）所以涡旋电场不能定义标量势。
