# 安培-麦克斯韦定律——从矛盾到统一

> 安培-麦克斯韦定律是麦克斯韦方程组中最"精彩"的一个方程——它记录了麦克斯韦如何发现原版安培环路定理的内在矛盾，并创造性地引入**位移电流**来修复它。这一步直接预言了电磁波的存在。

\newpage

# 一、原版安培环路定理出了什么问题？

## 1.1 原版定理

$$\oint_L \boldsymbol{H} \cdot d\boldsymbol{l} = I_f$$

$\boldsymbol{H}$ 沿闭合环路的环量 = 穿过该环路的自由电流。

## 1.2 致命矛盾：对同一个环路，穿过它的"电流"竟然不唯一！

考虑一个正在充电的平行板电容器：

```
        导线中的传导电流 I
    ───→─────┬───────→───
             │    +Q
          ═══╪═══════     电容器极板
             │
          ═══╪═══════
             │    -Q
    ───→─────┴───────→───
        导线中的传导电流 I
```

取一个环绕导线的圆形安培环路 $L$。现在以 $L$ 为边界，选**两个不同的面**：

**面 $S_1$**（穿过导线）：导线穿过 $S_1$ → $I_f = I$（传导电流）

**面 $S_2$**（穿过电容器两极板之间）：没有导线穿过 $S_2$ → $I_f = 0$！

**同一个环路 $L$ 为边界，$\oint\boldsymbol{H}\cdot d\boldsymbol{l}$ 到底等于 $\mu_0 I$ 还是 $0$？**

这是原版安培环路定理的**内在矛盾**——它不满足连续性方程。

## 1.3 矛盾的本质

$$\nabla\times\boldsymbol{H} = \boldsymbol{J}_f \quad\Rightarrow\quad \nabla\cdot(\nabla\times\boldsymbol{H}) = \nabla\cdot\boldsymbol{J}_f$$

左边恒为零（旋度的散度 $\equiv 0$），所以必须有 $\nabla\cdot\boldsymbol{J}_f = 0$。

但在非稳态（如电容器充放电）中，**电荷在积累**，连续性方程要求：

$$\nabla\cdot\boldsymbol{J}_f = -\frac{\partial\rho_f}{\partial t} \neq 0$$

**矛盾！** 原版定理只在稳态（$\partial\rho_f/\partial t = 0$）下成立。

\newpage

# 二、麦克斯韦的天才修正——位移电流

## 2.1 修复方法

由高斯定理 $\nabla\cdot\boldsymbol{D} = \rho_f$，代入连续性方程：

$$\nabla\cdot\boldsymbol{J}_f = -\frac{\partial\rho_f}{\partial t} = -\frac{\partial}{\partial t}(\nabla\cdot\boldsymbol{D}) = -\nabla\cdot\frac{\partial\boldsymbol{D}}{\partial t}$$

$$\nabla\cdot\left(\boldsymbol{J}_f + \frac{\partial\boldsymbol{D}}{\partial t}\right) = 0$$

**$\boldsymbol{J}_f + \partial\boldsymbol{D}/\partial t$ 的散度恒为零！** 它可以合法地出现在旋度方程的右边。

麦克斯韦将原版 $\nabla\times\boldsymbol{H} = \boldsymbol{J}_f$ 修改为：

$$\boxed{\nabla\times\boldsymbol{H} = \boldsymbol{J}_f + \frac{\partial\boldsymbol{D}}{\partial t}}$$

## 2.2 积分形式

$$\boxed{\oint_L \boldsymbol{H} \cdot d\boldsymbol{l} = I_f + \int_S \frac{\partial\boldsymbol{D}}{\partial t} \cdot d\boldsymbol{S}}$$

两项的物理解释：

| 项 | 名称 | 物理含义 |
|----|------|---------|
| $I_f$ | **传导电流** | 自由电荷的定向运动（导线中的电流） |
| $\int_S \dfrac{\partial\boldsymbol{D}}{\partial t}\cdot d\boldsymbol{S}$ | **位移电流** | 电场随时间的变化率穿过面 $S$ 的通量 |
| $I_f + I_d$ | **全电流** | 两者之和，永远连续 |

## 2.3 位移电流 $I_d$ 究竟是什么？

$$\boxed{I_d = \int_S \frac{\partial\boldsymbol{D}}{\partial t} \cdot d\boldsymbol{S}}$$

在电容器极板之间：$\boldsymbol{D} = \sigma_f$（电位移大小等于极板上的自由电荷面密度）。

$$I_d = \frac{\partial}{\partial t}\int_S \boldsymbol{D}\cdot d\boldsymbol{S} = \frac{\partial}{\partial t}(D\cdot A) = \frac{\partial Q_f}{\partial t}$$

而导线中的传导电流 $I = dQ_f/dt$ —— **位移电流恰好等于传导电流！**

**矛盾化解了**：对 $S_1$（穿过导线）→ 全电流 $= I$；对 $S_2$（穿过电容缝隙）→ 全电流 $= I_d = I$。**两个面给出同样的全电流！**

\newpage

# 三、物理意义——位移电流为什么能产生磁场？

## 3.1 变化的电场激发磁场

这是麦克斯韦最深刻的洞见。安培-麦克斯韦定律告诉我们的不止是数学修补，而是一个全新的物理：

$$\boxed{\text{变化的电场} \;\xrightarrow{\text{激发}}\; \text{磁场}}$$

与法拉第定律 $\nabla\times\boldsymbol{E} = -\partial\boldsymbol{B}/\partial t$（变化的磁场激发电场）形成完美的对称：

```
         法拉第定律
     ∂B/∂t ────→ E (涡旋电场)

       安培-麦克斯韦定律
     ∂D/∂t ────→ H (磁场)
```

这两个对称项联立 → **电磁波**。变化的电场激发磁场，变化的磁场激发电场 → 电磁扰动以波的形式在空间中传播。

## 3.2 位移电流不是"真正的电流"

位移电流 $\partial\boldsymbol{D}/\partial t$ 并不涉及电荷的宏观运动——它是**电场的时间变化率**。但它和传导电流一样，会在周围空间产生环向磁场。

在电容器两极板之间，没有电荷流动，但有变化的电场 → 变化的电场就像"电流"一样产生环绕的磁场。

\newpage

# 四、回到电容器矛盾——用安培-麦克斯韦定律重新看

## 4.1 对环路 $L$，选面 $S_1$（穿过导线）

$$\oint_L \boldsymbol{H}\cdot d\boldsymbol{l} = I_f + \underbrace{\int_{S_1}\frac{\partial\boldsymbol{D}}{\partial t}\cdot d\boldsymbol{S}}_{\approx\,0} = I$$

（导线中 $\partial\boldsymbol{D}/\partial t$ 通常可忽略，传导电流主导）

## 4.2 对环路 $L$，选面 $S_2$（穿过电容缝隙）

$$\oint_L \boldsymbol{H}\cdot d\boldsymbol{l} = \underbrace{I_f}_{=\,0} + \int_{S_2}\frac{\partial\boldsymbol{D}}{\partial t}\cdot d\boldsymbol{S} = I_d = I$$

（极板间无传导电流，位移电流主导）

## 4.3 结论

$$\boxed{\oint_L \boldsymbol{H}\cdot d\boldsymbol{l} = I \quad\text{（无论选哪个面！）}}$$

全电流 $I + I_d$ 在任何位置都连续——从导线流入极板的传导电流"接棒"给极板间的位移电流，再在对面极板"交棒"回传导电流。全电流像一条完整的"链"，永不中断。

\newpage

# 五、麦克斯韦方程组的对称之美

| 方程 | 微分形式 | 物理内容 |
|------|---------|---------|
| 高斯电定律 | $\nabla\cdot\boldsymbol{D} = \rho_f$ | 电荷产生电场（散度源） |
| 高斯磁定律 | $\nabla\cdot\boldsymbol{B} = 0$ | 无磁单极子 |
| 法拉第定律 | $\nabla\times\boldsymbol{E} = -\dfrac{\partial\boldsymbol{B}}{\partial t}$ | 变磁场 → 涡旋电场 |
| **安培-麦克斯韦** | $\nabla\times\boldsymbol{H} = \boldsymbol{J}_f + \dfrac{\partial\boldsymbol{D}}{\partial t}$ | 电流 + **变电场** → 磁场 |

注意后两个方程的对称：

- $\nabla\times\boldsymbol{E}$ 由 $-\partial\boldsymbol{B}/\partial t$ 驱动
- $\nabla\times\boldsymbol{H}$ 由 $+\partial\boldsymbol{D}/\partial t$ 驱动（外加传导电流）

**如果没有 $\partial\boldsymbol{D}/\partial t$ 这一项，麦克斯韦方程组就不对称，电磁波就不可能存在。** 麦克斯韦正是通过添加这一项，从方程中导出了电磁波的波速恰好等于光速，从而预言了"光就是电磁波"。

\newpage

# 六、考试中位移电流的常见考法

## 6.1 平行板电容器充放电

**典型题**：圆形平行板电容器（极板半径 $R$），充电电流 $I$。求两极板间距离轴 $r$ 处的磁感应强度。

**解**：两极板间 $D = \sigma = Q/(\pi R^2)$，$dD/dt = I/(\pi R^2)$。

位移电流密度：$j_d = \dfrac{\partial D}{\partial t} = \dfrac{I}{\pi R^2}$（均匀）。

取半径 $r$ 的圆形安培环路：

- $r < R$：全电流穿过 $= j_d\cdot\pi r^2 = I r^2/R^2$

$$H\cdot 2\pi r = I\frac{r^2}{R^2} \;\Rightarrow\; B = \frac{\mu_0 I r}{2\pi R^2}$$

- $r > R$：全电流穿过 $= I$（全部位移电流）

$$B = \frac{\mu_0 I}{2\pi r}$$

## 6.2 位移电流与传导电流的相位关系

在交流电路中，$D = \varepsilon E$，$E = V/d$，$\partial D/\partial t \propto dV/dt$。

位移电流**超前**电压 $90^\circ$（与电容性电流同相）——这解释了为什么电容器能"通交流"：交流下极板间位移电流接续了导线中的传导电流。

\newpage

# 七、总结

## 核心逻辑链

```
原版安培定理
  ∇×H = J_f
      │
      ▼ 取散度
  ∇·J_f = 0  ← 与连续性方程矛盾！（非稳态时 ∇·J_f = -∂ρ/∂t ≠ 0）
      │
      ▼ 麦克斯韦修正
  ∇×H = J_f + ∂D/∂t
      │
      ▼ 取散度
  ∇·(J_f + ∂D/∂t) = -∂ρ/∂t + ∂ρ/∂t = 0  ← 一致！
      │
      ▼ 物理后果
  变电场激发磁场 → 与法拉第定律对称 → 电磁波
```

## 三个必须记住的公式

| | 微分形式 | 积分形式 |
|--|---------|---------|
| 安培-麦克斯韦 | $\nabla\times\boldsymbol{H} = \boldsymbol{J}_f + \dfrac{\partial\boldsymbol{D}}{\partial t}$ | $\displaystyle\oint\boldsymbol{H}\cdot d\boldsymbol{l} = I_f + \int\dfrac{\partial\boldsymbol{D}}{\partial t}\cdot d\boldsymbol{S}$ |
| 全电流连续性 | $\nabla\cdot(\boldsymbol{J}_f + \boldsymbol{J}_d) = 0$ | $I_f + I_d = \text{const}$（沿电路不变） |
| 位移电流密度 | — | $\boldsymbol{J}_d = \dfrac{\partial\boldsymbol{D}}{\partial t}$ |

## 一句话总结

> 安培-麦克斯韦定律 = 传导电流 + 位移电流共同产生磁场。位移电流 $\partial\boldsymbol{D}/\partial t$ 是麦克斯韦为了修复连续性方程矛盾而引入的天才创造——它使变化的电场能够激发磁场，从而让麦克斯韦方程组孕育出了电磁波。
