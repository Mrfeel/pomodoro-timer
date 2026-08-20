# 均匀磁化球——$\boldsymbol{H}$ 与 $\boldsymbol{B}$ 的分布详解

> **原题**：均匀磁化球（磁化强度 $\boldsymbol{M} = M_0\hat{\boldsymbol{z}}$，半径 $R$），求球内外的 $\boldsymbol{H}$ 和 $\boldsymbol{B}$ 分布。
>
> **结论**：$\boldsymbol{H}_{\text{in}} = -\dfrac{\boldsymbol{M}}{3}$，$\boldsymbol{B}_{\text{in}} = \dfrac{2}{3}\mu_0\boldsymbol{M}$，球外等效中心磁偶极子 $\boldsymbol{m} = \dfrac{4\pi}{3}R^3\boldsymbol{M}$。

\newpage

# 一、这道题为什么重要？

均匀磁化球是磁介质理论中**最经典的边界值问题**。它的解法建立了两个核心概念：

1. **退磁场**（demagnetizing field）——磁化产生的 $\boldsymbol{H}$ 与 $\boldsymbol{M}$ 反向
2. **退磁因子**（demagnetizing factor）——对球体 $N = 1/3$

这两个概念在大学电磁学期末考试中出现频率极高。

\newpage

# 二、与均匀极化球的类比——最核心的理解方式

## 2.1 电与磁的对偶

这是理解本题最快的方式。你很可能已经学过**均匀极化介质球**：

| | 均匀极化球 | 均匀磁化球 |
|--|----------|----------|
| 极化/磁化 | $\boldsymbol{P} = P_0\hat{\boldsymbol{z}}$ | $\boldsymbol{M} = M_0\hat{\boldsymbol{z}}$ |
| 表面束缚源 | $\sigma' = \boldsymbol{P}\cdot\hat{\boldsymbol{n}} = P_0\cos\theta$ | $\boldsymbol{K}' = \boldsymbol{M}\times\hat{\boldsymbol{n}}$ |
| 内部退场 | $\boldsymbol{E}_{\text{dep}} = -\dfrac{\boldsymbol{P}}{3\varepsilon_0}$ | $\boldsymbol{H}_{\text{demag}} = -\dfrac{\boldsymbol{M}}{3}$ |
| 内部总场 | $\boldsymbol{E}_{\text{in}} = -\dfrac{\boldsymbol{P}}{3\varepsilon_0}$ | $\boldsymbol{H}_{\text{in}} = -\dfrac{\boldsymbol{M}}{3}$ |
| 外部场 | 等效中心电偶极子 $\boldsymbol{p} = \frac{4\pi}{3}R^3\boldsymbol{P}$ | 等效中心磁偶极子 $\boldsymbol{m} = \frac{4\pi}{3}R^3\boldsymbol{M}$ |

**数学结构完全相同**，把 $\boldsymbol{P}\to\boldsymbol{M}$、$\boldsymbol{E}\to\boldsymbol{H}$、$\varepsilon_0\to 1$、$1/\varepsilon_0\to\mu_0$ 即可。

## 2.2 为什么会有退磁场？

```
        z
        ↑  M (所有分子磁矩都沿z排列)
        │
    ╭───●───╮
   ╱    │    ╲
  │  ↻  │  ↻  │  ← 分子电流环（等效）
  │     │     │
  │  ↻  │  ↻  │
   ╲    │    ╱
    ╰───●───╯
        │
        │  表面磁化电流 K' 沿 φ̂ 方向
        │  （在球面上形成环流）
```

**物理图像**：均匀磁化意味着所有分子磁矩整齐排列。在球内部，相邻分子环流相互抵消；在球表面，没有相邻分子来抵消 → 形成**表面磁化电流** $\boldsymbol{K}' = \boldsymbol{M}\times\hat{\boldsymbol{n}}$。

这个表面环流产生一个与 $\boldsymbol{M}$ **方向相反**的磁场 $\boldsymbol{H}'$——这就是**退磁场**（demagnetizing field）。叫"退磁"是因为它倾向于削弱磁化。

\newpage

# 三、表面磁化电流的计算

## 3.1 公式

$$\boxed{\boldsymbol{K}' = \boldsymbol{M} \times \hat{\boldsymbol{n}}}$$

在球面上，$\hat{\boldsymbol{n}} = \hat{\boldsymbol{r}}$（外法向），$\boldsymbol{M} = M_0\hat{\boldsymbol{z}}$。

## 3.2 用球坐标计算

在球坐标中，$\hat{\boldsymbol{z}} = \cos\theta\,\hat{\boldsymbol{r}} - \sin\theta\,\hat{\boldsymbol{\theta}}$。

$$\boldsymbol{K}' = M_0\hat{\boldsymbol{z}} \times \hat{\boldsymbol{r}} = M_0(\cos\theta\,\hat{\boldsymbol{r}} - \sin\theta\,\hat{\boldsymbol{\theta}}) \times \hat{\boldsymbol{r}}$$

$$\hat{\boldsymbol{r}} \times \hat{\boldsymbol{r}} = 0,\quad \hat{\boldsymbol{\theta}} \times \hat{\boldsymbol{r}} = -\hat{\boldsymbol{\varphi}}$$

所以 $-\sin\theta\,\hat{\boldsymbol{\theta}} \times \hat{\boldsymbol{r}} = -(-\sin\theta\,\hat{\boldsymbol{\varphi}}) = \sin\theta\,\hat{\boldsymbol{\varphi}}$

等等，更简单地直接用直角分量：

$$\boldsymbol{M} = M_0\hat{\boldsymbol{z}},\quad \hat{\boldsymbol{n}} = \hat{\boldsymbol{r}} = \sin\theta\cos\varphi\,\hat{\boldsymbol{x}} + \sin\theta\sin\varphi\,\hat{\boldsymbol{y}} + \cos\theta\,\hat{\boldsymbol{z}}$$

$$\boldsymbol{K}' = M_0\hat{\boldsymbol{z}} \times \hat{\boldsymbol{r}} = M_0\begin{vmatrix} \hat{\boldsymbol{x}} & \hat{\boldsymbol{y}} & \hat{\boldsymbol{z}} \\ 0 & 0 & 1 \\ \sin\theta\cos\varphi & \sin\theta\sin\varphi & \cos\theta \end{vmatrix}$$

$$= M_0\bigl[-\sin\theta\sin\varphi\,\hat{\boldsymbol{x}} + \sin\theta\cos\varphi\,\hat{\boldsymbol{y}}\bigr]$$

$$= M_0\sin\theta\,\hat{\boldsymbol{\varphi}}$$

$$\boxed{\boldsymbol{K}' = M_0\sin\theta\,\hat{\boldsymbol{\varphi}}}$$

## 3.3 物理图像

$\boldsymbol{K}'$ 沿 $\hat{\boldsymbol{\varphi}}$ 方向——即环绕 $z$ 轴。而且 $\boldsymbol{K}' \propto \sin\theta$：

- 在北极 ($\theta=0$)：$K' = 0$（$\boldsymbol{M}\parallel\hat{\boldsymbol{n}}$，叉积为零）
- 在赤道 ($\theta=\pi/2$)：$K' = M_0$（最大，$\boldsymbol{M}\perp\hat{\boldsymbol{n}}$）
- 在南极 ($\theta=\pi$)：$K' = 0$

**球面上的磁化电流像一个"环带"**，赤道处最强，两极处消失。这个电流分布在球内产生均匀的磁场——这正是关键所在。

\newpage

# 四、球内 $\boldsymbol{B}$ 的计算

## 4.1 对磁化电流积分

球内一点的磁场，由球面上所有磁化电流元 $K'\,dS'$ 的贡献叠加得到。

由于球对称性和 $\boldsymbol{K}'\propto\sin\theta$ 的特殊分布，这个积分的结果出人意料地简洁——**球内磁场是均匀的**。

## 4.2 球内均匀磁场的推导思路

把球面分成无数个 $\theta$ 处的环带（纬线环），每个环带相当于一个半径为 $R\sin\theta$ 的圆形载流线圈，电流为 $dI = K' \cdot R\,d\theta = M_0 R\sin\theta\,d\theta$。

这个环带在球心产生的 $dB_z$ 可以用圆环轴线公式计算（取 $z=0$，到每个环带的距离为零，但环带不在同一平面上）。

**更简洁的方法**：利用圆形电流环在轴线上任意点的公式：

$$dB_z(0) = \frac{\mu_0\,dI\,(R\sin\theta)^2}{2[(R\sin\theta)^2 + (R\cos\theta)^2]^{3/2}} = \frac{\mu_0\,dI\,R^2\sin^2\theta}{2R^3} = \frac{\mu_0\,dI\,\sin^2\theta}{2R}$$

代入 $dI = K'R\,d\theta = M_0 R\sin\theta\,d\theta$：

$$dB_z = \frac{\mu_0 M_0 R\sin\theta \cdot \sin^2\theta}{2R}d\theta = \frac{\mu_0 M_0}{2}\sin^3\theta\,d\theta$$

对 $\theta$ 从 $0$ 积分到 $\pi$：

$$B_z(0) = \frac{\mu_0 M_0}{2}\int_0^\pi \sin^3\theta\,d\theta = \frac{\mu_0 M_0}{2}\cdot\frac{4}{3} = \frac{2}{3}\mu_0 M_0$$

$$\boxed{B_z(0) = \frac{2}{3}\mu_0 M_0}$$

实际上，球内各点的 $\boldsymbol{B}$ 都是均匀的（这里不展开逐点证明）。所以：

$$\boxed{\boldsymbol{B}_{\text{in}} = \frac{2}{3}\mu_0\boldsymbol{M}}$$

\newpage

# 五、由 $\boldsymbol{B}_{\text{in}}$ 求 $\boldsymbol{H}_{\text{in}}$

## 5.1 本构关系

$$\boxed{\boldsymbol{B} = \mu_0(\boldsymbol{H} + \boldsymbol{M})}$$

因此：

$$\boldsymbol{H}_{\text{in}} = \frac{\boldsymbol{B}_{\text{in}}}{\mu_0} - \boldsymbol{M} = \frac{2}{3}\boldsymbol{M} - \boldsymbol{M} = -\frac{1}{3}\boldsymbol{M}$$

$$\boxed{\boldsymbol{H}_{\text{in}} = -\frac{\boldsymbol{M}}{3}}$$

## 5.2 物理意义

$\boldsymbol{H}_{\text{in}}$ 与 $\boldsymbol{M}$ **反向**！这是退磁场的核心特征：

- $\boldsymbol{M}$ 沿 $+z$ → 分子磁矩整齐向上
- $\boldsymbol{H}_{\text{in}}$ 沿 $-z$ → 磁化产生的效果是削弱磁化方向的总场
- 系数 $1/3$ 是球体的**退磁因子**

## 5.3 退磁因子的一般概念

对于椭球体，均匀磁化产生的内部 $\boldsymbol{H}$ 也是均匀的：

$$\boldsymbol{H}_{\text{in}} = -N\,\boldsymbol{M}$$

其中 $N$ 是**退磁因子**（$0 \leq N \leq 1$），只取决于形状：

| 形状 | $N$（沿长轴磁化） | $N$（沿短轴磁化） |
|------|-------------------|-------------------|
| **球体** | $1/3$ | $1/3$ |
| 无限长圆柱（轴向磁化） | $0$ | $1/2$ |
| 无限大薄板（垂直磁化） | $1$ | $0$ |
| 细长针（沿轴向） | $\to 0$ | $\to 1/2$ |
| 扁圆盘（垂直盘面） | $\to 1$ | $\to 0$ |

**球体 $N=1/3$ 是最对称的情况，也是最常考的。**

\newpage

# 六、球外磁场——等效磁偶极子

## 6.1 远场近似

球外，磁场等价于一个位于球心的**磁偶极子**产生的场。

磁偶极矩 = 总磁化强度：

$$\boxed{\boldsymbol{m} = \frac{4\pi}{3}R^3\boldsymbol{M}}$$

即 $\boldsymbol{m} = V_{\text{球}} \cdot \boldsymbol{M}$——体积乘以磁化强度。

## 6.2 磁偶极子场

球外 $(r > R)$ 的磁场分布：

$$\boxed{\boldsymbol{B}_{\text{out}} = \frac{\mu_0}{4\pi r^3}\bigl[3(\boldsymbol{m}\cdot\hat{\boldsymbol{r}})\hat{\boldsymbol{r}} - \boldsymbol{m}\bigr]}$$

$$\boxed{\boldsymbol{H}_{\text{out}} = \frac{\boldsymbol{B}_{\text{out}}}{\mu_0} = \frac{1}{4\pi r^3}\bigl[3(\boldsymbol{m}\cdot\hat{\boldsymbol{r}})\hat{\boldsymbol{r}} - \boldsymbol{m}\bigr]}$$

## 6.3 为什么球外是偶极子场？

两个角度理解：

**角度一（数学）**：表面磁化电流 $K'=M_0\sin\theta\,\hat{\boldsymbol{\varphi}}$ 在球外的场，经积分后恰好等于一个中心磁偶极子的场。这不是巧合——任意局域电流分布的最低阶多极展开就是磁偶极子。

**角度二（物理）**：均匀磁化球的净磁矩 $\boldsymbol{m} = \int\boldsymbol{M}\,dV = V\boldsymbol{M}$。在远处看，球内所有分子磁矩的叠加等同于一个点磁偶极子。

\newpage

# 七、全空间场的完整总结

## 7.1 球内 ($r < R$)

$$\boxed{\boldsymbol{H}_{\text{in}} = -\frac{\boldsymbol{M}}{3}} \qquad \boxed{\boldsymbol{B}_{\text{in}} = \frac{2}{3}\mu_0\boldsymbol{M}}$$

- $\boldsymbol{H}_{\text{in}}$ 沿 $-z$（退磁场，与 $\boldsymbol{M}$ 反向）
- $\boldsymbol{B}_{\text{in}}$ 沿 $+z$（总磁场，与 $\boldsymbol{M}$ 同向）
- **两者都是均匀场！** 这是球体的特殊性质

## 7.2 球外 ($r > R$)

$$\boxed{\boldsymbol{H}_{\text{out}} = \frac{1}{4\pi r^3}\bigl[3(\boldsymbol{m}\cdot\hat{\boldsymbol{r}})\hat{\boldsymbol{r}} - \boldsymbol{m}\bigr]}$$

$$\boxed{\boldsymbol{B}_{\text{out}} = \mu_0\boldsymbol{H}_{\text{out}}}$$

其中 $\boldsymbol{m} = \dfrac{4\pi}{3}R^3\boldsymbol{M}$。

## 7.3 球面上 ($r = R$)

$\boldsymbol{B}$ 的法向分量（$B_r$）连续，$\boldsymbol{H}$ 的切向分量（$H_\theta$）连续（无自由面电流）。

## 7.4 对比图

```
       z
       ↑  M
       │
  球外：偶极子场（像条形磁铁）
  ╭     ↑     ╮
  │    ╱ ╲    │
  │   ╱   ╲   │
  │  ● 均匀 ●  │  ← 球内：H_in = -M/3 (↓), B_in = 2μ₀M/3 (↑)
  │   ╲   ╱   │
  │    ╲ ╱    │
  ╰     ↓     ╯
        │
  球外磁力线从北极出发，回到南极
  （与条形磁铁完全相同）
```

\newpage

# 八、与均匀极化介质球的逐项对比

这是记忆这道题的最佳方式——用电介质中已学的结果直接对应。

| 项目 | 均匀极化球（电） | 均匀磁化球（磁） |
|------|---------------|---------------|
| 体束缚源 | $\rho' = -\nabla\cdot\boldsymbol{P} = 0$ | $\boldsymbol{J}' = \nabla\times\boldsymbol{M} = 0$ |
| 面束缚源 | $\sigma' = \boldsymbol{P}\cdot\hat{\boldsymbol{n}} = P_0\cos\theta$ | $\boldsymbol{K}' = \boldsymbol{M}\times\hat{\boldsymbol{n}} = M_0\sin\theta\,\hat{\boldsymbol{\varphi}}$ |
| 内部退场 | $\boldsymbol{E}_{\text{in}} = -\dfrac{\boldsymbol{P}}{3\varepsilon_0}$ | $\boldsymbol{H}_{\text{in}} = -\dfrac{\boldsymbol{M}}{3}$ |
| 内部总场 | $\boldsymbol{D}_{\text{in}} = \varepsilon_0\boldsymbol{E}_{\text{in}}+\boldsymbol{P} = \dfrac{2}{3}\boldsymbol{P}$ | $\boldsymbol{B}_{\text{in}} = \mu_0(\boldsymbol{H}_{\text{in}}+\boldsymbol{M}) = \dfrac{2}{3}\mu_0\boldsymbol{M}$ |
| 外部场 | 等效中心电偶极子 $\boldsymbol{p}=V\boldsymbol{P}$ | 等效中心磁偶极子 $\boldsymbol{m}=V\boldsymbol{M}$ |
| 偶极子场公式 | $\boldsymbol{E}=\dfrac{1}{4\pi\varepsilon_0 r^3}[3(\boldsymbol{p}\cdot\hat{\boldsymbol{r}})\hat{\boldsymbol{r}}-\boldsymbol{p}]$ | $\boldsymbol{B}=\dfrac{\mu_0}{4\pi r^3}[3(\boldsymbol{m}\cdot\hat{\boldsymbol{r}})\hat{\boldsymbol{r}}-\boldsymbol{m}]$ |

## 记忆技巧

只需要记住**三个数字**：

$$\boxed{-\frac{1}{3},\quad \frac{2}{3},\quad \frac{4\pi}{3}}$$

- 球内 $\boldsymbol{H} = -1/3\,\boldsymbol{M}$（退磁场，负号！）
- 球内 $\boldsymbol{B} = 2/3\,\mu_0\boldsymbol{M}$（$1-1/3=2/3$）
- 球外磁偶极矩 $\boldsymbol{m} = 4\pi/3\,R^3\boldsymbol{M} = V\boldsymbol{M}$

\newpage

# 九、考试中可能出现的变体

## 9.1 变体1：改变磁化方向

若 $\boldsymbol{M}$ 沿 $+x$ 方向，内部退磁场仍为 $\boldsymbol{H}_{\text{in}} = -\boldsymbol{M}/3$（沿 $-x$），只需把对称轴从 $z$ 改为 $x$。

## 9.2 变体2：球壳磁化

若只有 $R_1<r<R_2$ 的球壳被磁化，内腔 ($r<R_1$) 中 $\boldsymbol{H}$ 和 $\boldsymbol{B}$ 的分布如何？——这需要叠加两个均匀磁化球的结果。

## 9.3 变体3：椭球体磁化

若为旋转椭球体（沿对称轴磁化），退磁因子 $N \neq 1/3$，需要用椭球坐标求解。但物理图像完全一致——内部 $\boldsymbol{H}$ 均匀、反向。

## 9.4 变体4：已知外磁场中的磁化球

将磁导率为 $\mu$ 的球放入均匀外磁场 $\boldsymbol{B}_0$ 中，球内 $\boldsymbol{B}$ 和 $\boldsymbol{H}$ 如何？——这是另一个经典问题，与本题密切相关但处理方式不同（需匹配边界条件）。

## 9.5 核验公式

用电偶极子来辅助记忆：
- 极化球表面束缚电荷 $\sigma' = P\cos\theta$ → 内部均匀退极化场
- 磁化球表面磁化电流 $K' = M\sin\theta$ → 内部均匀退磁场

**凡是球体内均匀极化/磁化，内部场必均匀，外部场必是偶极子场。**

\newpage

# 十、一句话总结

> 均匀磁化球 = 磁学版的均匀极化球。表面磁化电流 $\boldsymbol{K}' = \boldsymbol{M}\times\hat{\boldsymbol{n}} = M_0\sin\theta\,\hat{\boldsymbol{\varphi}}$ 产生均匀退磁场 $\boldsymbol{H}_{\text{in}} = -\boldsymbol{M}/3$，球内 $\boldsymbol{B}_{\text{in}} = \frac{2}{3}\mu_0\boldsymbol{M}$，球外等价于中心磁偶极子 $\boldsymbol{m} = \frac{4\pi}{3}R^3\boldsymbol{M}$。整道题只需记住三个分数：$-1/3$、$2/3$、$4\pi/3$。
