# T6-3 磁路定理 与 T6-4 磁介质圆柱——详解

\newpage

# 第一部分：T6-3 磁路定理——带气隙的环形铁芯

> **原题**：环形铁芯（平均周长 $l$、截面积 $S$、相对磁导率 $\mu_r$、匝数 $N$）有一小气隙 $l_g$。求气隙中 $B$ 和线圈自感 $L$。

## 一、什么是磁路定理？

磁路定理是安培环路定理在实用工程中的改造——把磁场问题变成"磁路"问题，完全类比电路。

| 电路 | 磁路 |
|------|------|
| 电动势 $\mathcal{E}$ | 磁动势 $\mathcal{F} = NI$ |
| 电流 $I$ | 磁通量 $\Phi$ |
| 电阻 $R = \dfrac{l}{\sigma S}$ | 磁阻 $\mathcal{R} = \dfrac{l}{\mu S}$ |
| 欧姆定律 $I = \mathcal{E}/R$ | **磁路欧姆定律** $\Phi = \mathcal{F}/\mathcal{R}$ |
| 串联电阻 $R = R_1+R_2$ | 串联磁阻 $\mathcal{R} = \mathcal{R}_1+\mathcal{R}_2$ |

**对比记忆**：电阻公式中电导率 $\sigma$ 在分母，磁阻公式中磁导率 $\mu$ 也在分母——导得越好，阻越小。

## 二、本题的磁路分析

### 2.1 几何结构

```
    ╭──────────────────────────╮
    │         铁芯 μ_r          │
    │    ╭────────────────╮    │
    │    │   线圈 N 匝    │    │
    │    │  电流 I       │    │
    │    ╰────────────────╯    │
    │                          │
    │         ← l →            │  ← 平均周长（铁芯部分）
    │                          │
    ╰──┬──╯  ╰──┬──╯           │
       │  气隙  │               │
       │  l_g   │               │
       └───────┘               │
```

铁芯（长 $l$，截面 $S$，$\mu = \mu_0\mu_r$）和气隙（长 $l_g$，截面近似 $S$，$\mu = \mu_0$）**串联**。

### 2.2 串联磁阻

$$\boxed{\mathcal{R}_{\text{core}} = \frac{l}{\mu_0\mu_r S}} \qquad \boxed{\mathcal{R}_{\text{gap}} = \frac{l_g}{\mu_0 S}}$$

$$\boxed{\mathcal{R}_{\text{总}} = \mathcal{R}_{\text{core}} + \mathcal{R}_{\text{gap}} = \frac{l}{\mu_0\mu_r S} + \frac{l_g}{\mu_0 S}}$$

### 2.3 磁通量

磁动势（MMF）= $NI$，由磁路欧姆定律：

$$\boxed{\Phi = \frac{NI}{\mathcal{R}_{\text{总}}} = \frac{NI}{\dfrac{l}{\mu_0\mu_r S} + \dfrac{l_g}{\mu_0 S}}}$$

由于铁芯和气隙串联，磁通量相同（磁通连续，无漏磁）。

### 2.4 气隙中的 $B$

截面不变 → $B$ 在铁芯和气隙中相同（忽略边缘效应导致截面变化）：

$$\boxed{B = \frac{\Phi}{S} = \frac{NI}{\dfrac{l}{\mu_0\mu_r} + \dfrac{l_g}{\mu_0}} = \frac{\mu_0 NI}{\dfrac{l}{\mu_r} + l_g}}$$

**关键近似**：当 $\mu_r \gg 1$ 时，$l/\mu_r \ll l_g$（铁芯磁阻远小于气隙磁阻），则：

$$\boxed{B \approx \frac{\mu_0 NI}{l_g}}$$

### 2.5 物理直觉

虽然气隙很短（$l_g \ll l$），但因为 $\mu_r \gg 1$，气隙的磁阻 $l_g/\mu_0$ 远大于铁芯的磁阻 $l/(\mu_0\mu_r)$。**磁路中的"瓶颈"在气隙，不在铁芯。** 这就像串联电路中大电阻决定电流——气隙是磁路中的"高阻环节"。

### 2.6 自感

$$L = \frac{N\Phi}{I} = \frac{N^2}{\mathcal{R}_{\text{总}}}$$

$$\boxed{L = \frac{N^2}{\dfrac{l}{\mu_0\mu_r S} + \dfrac{l_g}{\mu_0 S}}}$$

**讨论**：
- 无气隙 ($l_g=0$)：$L = \dfrac{\mu_0\mu_r N^2 S}{l}$——铁芯电感很大
- 有气隙：分母变大 → $L$ 变小。气隙降低了电感，但带来了更线性的 $B$-$I$ 关系和更高的饱和电流

## 三、磁路定理的适用条件

| 条件 | 说明 |
|------|------|
| $\mu_r \gg 1$ | 磁通基本约束在铁芯内，漏磁可忽略 |
| 截面均匀 | 铁芯和气隙截面积近似相等 |
| 气隙小 | $l_g \ll \sqrt{S}$，否则边缘效应显著（磁力线在气隙中扩散） |
| 无饱和 | 铁芯工作在 $B$-$H$ 线性区 |

\newpage

# 第二部分：T6-4 磁介质圆柱在横向外磁场中

> **原题**：磁介质圆柱（半径 $a$，磁导率 $\mu$）置于均匀外磁场 $\boldsymbol{B}_0$ 中，$\boldsymbol{B}_0 \perp$ 柱轴。证明柱内 $\boldsymbol{B}_{\text{in}} = \dfrac{2\mu}{\mu+\mu_0}\boldsymbol{B}_0$。

## 一、物理图像

```
       B₀ (均匀外磁场，沿x方向)
    →→→→→→→→→→→→→→→→→→→→
    →→→→╭───────╮→→→→
    →→→→│  μ    │→→→→   ← 圆柱截面（半径为a）
    →→→→│ 圆柱  │→→→→
    →→→→╰───────╯→→→→
    →→→→→→→→→→→→→→→→→→→→
```

- 圆柱**无限长**，外磁场 $\boldsymbol{B}_0$ **垂直于柱轴**（设为 $x$ 方向）
- 这是二维问题——在 $xy$ 平面内求解
- 柱外：真空（$\mu_0$），柱内：介质（$\mu$）

## 二、求解框架——磁标势法

### 2.1 为什么能用磁标势？

柱内和柱外都**没有自由电流**（$\boldsymbol{J}_f = 0$），所以：

$$\nabla\times\boldsymbol{H} = 0$$

无旋场可写为标量势的梯度：

$$\boxed{\boldsymbol{H} = -\nabla\varphi_m}$$

其中 $\varphi_m$ 称为**磁标势**。

### 2.2 磁标势满足拉普拉斯方程

由 $\nabla\cdot\boldsymbol{B} = 0$ 和 $\boldsymbol{B} = \mu\boldsymbol{H}$：

$$\nabla\cdot(\mu\nabla\varphi_m) = 0$$

若 $\mu$ 为常数（分区均匀介质），在每一区域内：

$$\boxed{\nabla^2\varphi_m = 0}$$

这就是**拉普拉斯方程**——和静电学中完全相同的方程。

## 三、边界条件

### 3.1 无穷远处

$$\boldsymbol{H}(r\to\infty) = \boldsymbol{H}_0 = \frac{\boldsymbol{B}_0}{\mu_0}$$

$$\varphi_m(r\to\infty) = -H_0\,x = -H_0\,r\cos\theta$$
（取 $\boldsymbol{H}_0 = H_0\hat{\boldsymbol{x}}$，用平面极坐标 $(r,\theta)$）

### 3.2 柱面 $r=a$ 上

- $B_r$ 连续（磁场的法向分量连续）：$\mu_0\dfrac{\partial\varphi_m^{\text{out}}}{\partial r} = \mu\dfrac{\partial\varphi_m^{\text{in}}}{\partial r}$
- $H_\theta$ 连续（无自由面电流，$\boldsymbol{H}$ 切向分量连续）：$\dfrac{\partial\varphi_m^{\text{out}}}{\partial\theta} = \dfrac{\partial\varphi_m^{\text{in}}}{\partial\theta}$

## 四、分离变量法求解

### 4.1 通解形式

二维拉普拉斯方程在极坐标中的分离变量通解：

$$\varphi_m(r,\theta) = \sum_{n=1}^{\infty}\bigl(A_n r^n + B_n r^{-n}\bigr)\bigl(C_n\cos n\theta + D_n\sin n\theta\bigr)$$

由无穷远条件 $\varphi_m \to -H_0 r\cos\theta$ → 只有 $n=1$ 的 $\cos\theta$ 项。

### 4.2 柱外解 ($r>a$)

$$\varphi_m^{\text{out}}(r,\theta) = -H_0 r\cos\theta + \frac{A}{r}\cos\theta$$

- 第一项：均匀外场（$r\to\infty$ 的主导项）
- 第二项：圆柱对外场的"扰动"（$n=1$ 对应二维偶极子，$\propto 1/r$）

### 4.3 柱内解 ($r<a$)

$\varphi_m^{\text{in}}$ 在 $r=0$ 处必须有限 → 不能有 $r^{-n}$ 项：

$$\varphi_m^{\text{in}}(r,\theta) = C\,r\cos\theta$$

$$= -H_{\text{in}}\,r\cos\theta$$

其中 $H_{\text{in}} = -C$。柱内 $\boldsymbol{H}_{\text{in}} = -\nabla\varphi_m^{\text{in}} = H_{\text{in}}\hat{\boldsymbol{x}}$——**柱内磁场是均匀的！**

### 4.4 匹配边界条件

在 $r=a$ 处：

**(1) $H_\theta$ 连续**（等价于 $\varphi_m$ 连续）：

$$-H_0 a + \frac{A}{a} = C a$$

$$-H_0 + \frac{A}{a^2} = C \quad\Rightarrow\quad A = (H_0+C)a^2$$

**(2) $B_r$ 连续**：$\mu_0\dfrac{\partial\varphi_m^{\text{out}}}{\partial r} = \mu\dfrac{\partial\varphi_m^{\text{in}}}{\partial r}$

$$\mu_0\left(-H_0\cos\theta - \frac{A}{a^2}\cos\theta\right) = \mu\,C\cos\theta$$

$$\mu_0(-H_0 - (H_0+C)) = \mu\,C$$

（因为 $A = (H_0+C)a^2$ → $A/a^2 = H_0+C$）

$$\mu_0(-2H_0 - C) = \mu C$$

$$-2\mu_0 H_0 = (\mu+\mu_0)C$$

$$C = -\frac{2\mu_0}{\mu+\mu_0}H_0$$

### 4.5 结果

柱内磁场强度：

$$\boxed{H_{\text{in}} = -C = \frac{2\mu_0}{\mu+\mu_0}H_0}$$

柱内磁感应强度：

$$\boxed{B_{\text{in}} = \mu H_{\text{in}} = \frac{2\mu}{\mu+\mu_0}\mu_0 H_0 = \frac{2\mu}{\mu+\mu_0}B_0}$$

**证毕。**

## 五、结果讨论

### 5.1 两个极限

| | $\mu \gg \mu_0$（铁磁柱） | $\mu = \mu_0$（无介质） | $\mu \to 0$（理想抗磁） |
|--|--------------------------|----------------------|----------------------|
| $B_{\text{in}}/B_0$ | $\to 2$ | $1$ | $\to 0$ |
| 物理 | 磁力线**吸入**圆柱，柱内场增强 | 无介质，场不变 | 磁力线**排斥**出圆柱（迈斯纳效应） |

### 5.2 为什么 $\mu \gg \mu_0$ 时 $B_{\text{in}} \to 2B_0$？

高磁导率材料像磁力线的"吸管"——磁力线更喜欢走铁磁材料内部（磁阻低）。磁力线被吸入圆柱，导致内部磁通密度增大。但 $B_{\text{in}}$ 不会超过 $2B_0$——这是二维几何的极限。

### 5.3 与电介质圆柱的完整对比

| | 电介质圆柱 (2D) | 磁介质圆柱 (2D) |
|--|---------------|---------------|
| 外场 | $\boldsymbol{E}_0 \perp$ 柱轴 | $\boldsymbol{B}_0 \perp$ 柱轴 |
| 势方程 | $\nabla^2\varphi = 0$（电势） | $\nabla^2\varphi_m = 0$（磁标势） |
| 法向连续量 | $D_r$：$\varepsilon E_r$ | $B_r$：$\mu H_r$ |
| 切向连续量 | $E_\theta$ | $H_\theta$ |
| 柱内均匀场 | $\boldsymbol{E}_{\text{in}} = \dfrac{2\varepsilon_0}{\varepsilon+\varepsilon_0}\boldsymbol{E}_0$ | $\boldsymbol{H}_{\text{in}} = \dfrac{2\mu_0}{\mu+\mu_0}\boldsymbol{H}_0$ |
| $\boldsymbol{D}/\boldsymbol{B}$ 关系 | $\boldsymbol{D}_{\text{in}} = \dfrac{2\varepsilon}{\varepsilon+\varepsilon_0}\boldsymbol{D}_0$ | $\boldsymbol{B}_{\text{in}} = \dfrac{2\mu}{\mu+\mu_0}\boldsymbol{B}_0$ |

**完全对应的数学结构。** 只需做替换 $\varepsilon \leftrightarrow \mu$、$\boldsymbol{E}\leftrightarrow\boldsymbol{H}$、$\boldsymbol{D}\leftrightarrow\boldsymbol{B}$。

## 六、三维球 vs. 二维圆柱——退磁因子

| 几何 | 均匀外场中内部结果 | 退磁因子 $N$ |
|------|-------------------|-------------|
| **球体** (3D) | $H_{\text{in}} = \dfrac{3\mu_0}{\mu+2\mu_0}H_0$ | $N=1/3$ |
| **圆柱** (2D，横向) | $H_{\text{in}} = \dfrac{2\mu_0}{\mu+\mu_0}H_0$ | $N=1/2$ |
| **圆柱** (轴向) | $H_{\text{in}} = H_0$（无退磁场） | $N=0$ |

系数 $2$ vs $3$ 的区别来自于球（3D）和柱（2D）几何维度的不同。**维度越低，退磁因子越大。**

\newpage

# 七、两题的综合对比

| | T6-3 磁路定理 | T6-4 磁介质圆柱 |
|--|-------------|---------------|
| **核心方程** | 安培环路定理 → 磁路欧姆定律 | $\nabla^2\varphi_m=0$ → 分离变量 |
| **问题类型** | 给定电流 → 求 $B$（正问题） | 给定外场 → 求介质对场的响应 |
| **关键近似** | 无漏磁，截面均匀 | 柱无限长，$\mu$ 常数 |
| **结果形式** | $B = \mu_0 NI/l_g$（气隙主导） | $B_{\text{in}} = \frac{2\mu}{\mu+\mu_0}B_0$ |
| **数学本质** | 串联磁路的"分压" | 拉普拉斯方程边值问题 |
| **记忆方法** | 类比串联电阻 | 类比电介质圆柱 |

## 一句话总结

> **T6-3**：磁路就像电路——铁芯是导线，气隙是串联大电阻。铁芯磁阻 $\propto l/\mu_r$，气隙磁阻 $\propto l_g$。$\mu_r\gg 1$ 时气隙磁阻主导，$B\approx\mu_0 NI/l_g$。
>
> **T6-4**：横向磁介质圆柱 → 磁标势拉普拉斯方程 + 分离变量 → 柱内均匀场 $\boldsymbol{B}_{\text{in}} = \frac{2\mu}{\mu+\mu_0}\boldsymbol{B}_0$。和电介质圆柱的 $\boldsymbol{E}_{\text{in}} = \frac{2\varepsilon_0}{\varepsilon+\varepsilon_0}\boldsymbol{E}_0$ 是同一个数学骨架。
