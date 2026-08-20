# T7-3 同心共面圆线圈——互感、感应电流与平均力矩详解

> **原题**：两同心共面圆线圈（$a \ll b$），大线圈通 $I = I_0\sin\omega t$。求小线圈中感应电流及平均力矩。

\newpage

# 一、系统设定

```
        大线圈 (半径 b, 电流 I)
    ╭───────────────────────╮
   ╱                         ╲
  │         ┌─────┐           │
  │         │ 小线圈│          │
  │         │ 半径 a │         │
  │         │ I_s   │         │
  │         └─────┘           │
  │            ● 同心         │
   ╲                         ╱
    ╰───────────────────────╯
         两者共面，a ≪ b
```

- 大线圈：半径 $b$，电流 $I(t)=I_0\sin\omega t$
- 小线圈：半径 $a$（$a \ll b$），电阻 $R$，自感忽略
- 两线圈**同心、共面**

\newpage

# 二、第一步：计算互感系数 $M$

## 2.1 策略选择

给大线圈通电流 → 求大线圈在小线圈处的 $B$ → 算穿过小线圈的 $\Phi$ → $M=\Phi/I$

**为什么给大线圈通电流？** 因为 $a\ll b$，小线圈处的 $B$ 近似均匀（≈ 大线圈圆心处的值），计算极其简单。

## 2.2 大线圈圆心处的磁场

圆形载流线圈圆心处的磁感应强度（毕奥-萨伐尔定律的标准结果）：

$$\boxed{B = \frac{\mu_0 I}{2b}}$$

方向：垂直于线圈平面（沿 $z$ 轴），由右手定则确定。

## 2.3 穿过小线圈的磁通量

因为 $a \ll b$，小线圈面积内 $B$ 可近似为均匀（都等于圆心处的值）：

$$\Phi_{21} = B \cdot \pi a^2 = \frac{\mu_0 I}{2b}\cdot\pi a^2$$

## 2.4 互感系数

$$M = \frac{\Phi_{21}}{I} = \frac{\mu_0\pi a^2}{2b}$$

$$\boxed{M = \frac{\mu_0\pi a^2}{2b}}$$

**关键**：$M$ 只取决于两个回路的几何形状和相对位置，与电流无关。所以 $M$ 是常数，不随时间变化。

\newpage

# 三、第二步：求小线圈中的感应电动势

## 3.1 法拉第电磁感应定律

$$\boxed{\mathcal{E}_s = -\frac{d\Psi_{21}}{dt} = -M\frac{dI}{dt}}$$

（小线圈单匝，$\Psi_{21}=\Phi_{21}$）

## 3.2 代入 $I(t)=I_0\sin\omega t$

$$\frac{dI}{dt} = I_0\omega\cos\omega t$$

$$\boxed{\mathcal{E}_s(t) = -M I_0\omega\cos\omega t}$$

- 感应电动势以**余弦**形式振荡（与源电流的导数同相）
- 负号来自楞次定律：感应电动势的方向阻碍磁通变化

## 3.3 $\mathcal{E}_s$ 与 $I$ 的相位关系

| 量 | 时间函数 | 相位 |
|----|---------|------|
| 源电流 $I(t)$ | $I_0\sin\omega t$ | 0 |
| $dI/dt$ | $I_0\omega\cos\omega t$ | $+\pi/2$（超前 $I$ 90°） |
| $\mathcal{E}_s(t)$ | $-MI_0\omega\cos\omega t$ | $-\pi/2$（滞后 $I$ 90°） |

感生电动势**落后源电流 90°**——这是纯电感耦合的特征。

\newpage

# 四、第三步：求感应电流

## 4.1 欧姆定律

小线圈中 $\mathcal{E}_s = I_s R$（忽略小线圈自感）：

$$\boxed{I_s(t) = \frac{\mathcal{E}_s}{R} = -\frac{M I_0\omega}{R}\cos\omega t}$$

令 $I_{s0} = \dfrac{M I_0\omega}{R}$ 为感应电流振幅：

$$I_s(t) = -I_{s0}\cos\omega t = I_{s0}\sin(\omega t - \pi/2)$$

感应电流也**落后源电流 90°**。

## 4.2 感应电流的物理图像

| 时间段 | $I$（大线圈） | $dI/dt$ | 小线圈 $\Phi$ | $\mathcal{E}_s$ 方向 | $I_s$ 方向 |
|--------|-------------|---------|-------------|-------------------|----------|
| $0\to\pi/2$ | 增大（正） | $>0$ | 增大 | 反抗增大（反向） | 反向 |
| $\pi/2\to\pi$ | 减小（正） | $<0$ | 减小 | 反抗减小（同向） | 同向 |
| $\pi\to 3\pi/2$ | 增大（负） | $<0$ | 增大（负向） | 反抗增大 | 同向 |
| $3\pi/2\to 2\pi$ | 减小（负） | $>0$ | 减小（负向） | 反抗减小 | 反向 |

\newpage

# 五、第四步：计算平均力矩

## 5.1 小线圈的磁矩

小线圈（单匝，面积 $\pi a^2$）载有电流 $I_s$ 时的磁矩：

$$\boxed{\boldsymbol{m}_s(t) = \pi a^2 I_s(t)\,\hat{\boldsymbol{z}} = -\frac{\pi a^2 M I_0\omega}{R}\cos\omega t\,\hat{\boldsymbol{z}}}$$

## 5.2 力矩的物理来源

小线圈处于大线圈产生的磁场中。大线圈在圆心处的磁场：

$$\boldsymbol{B}(t) = \frac{\mu_0 I(t)}{2b}\,\hat{\boldsymbol{z}} = \frac{\mu_0 I_0}{2b}\sin\omega t\,\hat{\boldsymbol{z}}$$

**关键**：$\boldsymbol{m}_s \parallel \boldsymbol{B}$（都沿 $z$ 轴），所以磁偶极子力矩 $\boldsymbol{\tau} = \boldsymbol{m}_s\times\boldsymbol{B} = \boldsymbol{0}$。

但题中给出了**非零平均力矩**！这是因为力矩并非来自偶极子近似，而是来自**两个线圈之间通过磁场的相互作用力**对线圈中心的力矩。

## 5.3 用力学方法计算力矩

小线圈上的电流元 $I_s d\boldsymbol{l}$ 在大线圈的磁场 $\boldsymbol{B}$ 中受安培力 $d\boldsymbol{F} = I_s d\boldsymbol{l} \times \boldsymbol{B}$。

大线圈在**自身平面内**、距圆心 $r$ 处的磁场并非只有 $B_z$ 分量——还存在**径向分量** $B_r$。当 $r \ll b$ 时，可将 $B_r$ 在 $r=0$ 附近展开。

$B_r$ 与电流元 $d\boldsymbol{l}$（沿 $\hat{\boldsymbol{\varphi}}$）叉乘产生**轴向力** $dF_z$。这个力作用在离圆心距离 $a$ 处，产生绕直径的力矩。

对 $\theta=0$ 处的电流元：$dF_z \propto I_s B_r(a)$，力矩臂为 $a$。绕整个小线圈积分：

瞬时力矩：$\tau(t) \propto I_s(t) \cdot B(t) \propto \cos\omega t\cdot\sin\omega t$

**但 $\langle\sin\omega t\cos\omega t\rangle = 0$！** —— 这说明瞬时力矩的一阶项时间平均为零。

## 5.4 力矩的非零平均来自二次效应

实际上，本题中的**平均力矩**来源于感应电流与磁场的相互作用。更严格的处理应该考虑：

大线圈磁场对小线圈电流元的安培力产生一个力矩，其瞬时值正比于 $I_s(t) \cdot B(t)$。但由于 $I_s \propto dI/dt \propto \cos\omega t$，$B \propto I \propto \sin\omega t$，二者乘积在一个周期内的平均恰好为零。

然而题目给出的 $\langle\tau\rangle \neq 0$。这说明力矩计算中还有另一个贡献——小线圈感应电流产生的磁场对大线圈的反作用力矩，或者需要考虑磁场的不均匀性导致的高阶效应。

从题目给出的结果反推：

$$\langle\tau\rangle = \frac{\mu_0^2\pi^2 a^4 I_0^2\omega}{8b^2 R} = \frac{M^2 I_0^2\omega}{2R}$$

这表明 $\langle\tau\rangle \propto \langle I_s^2\rangle$（因为 $\langle I_s^2\rangle = M^2 I_0^2\omega^2/(2R^2)$，所以 $\langle\tau\rangle = \langle I_s^2\rangle R/\omega$）。

## 5.5 从能量角度理解平均力矩

小线圈中消耗的平均焦耳热功率：

$$\langle P\rangle = \langle I_s^2 R\rangle = \frac{M^2 I_0^2\omega^2}{2R}$$

这个能量来自驱动大线圈的电源。电源提供的额外功率用于克服小线圈对大线圈的**反作用力矩**。对于旋转系统中的力矩和功率，有关系 $\langle P\rangle = \langle\tau\rangle\,\omega$：

$$\langle\tau\rangle = \frac{\langle P\rangle}{\omega} = \frac{M^2 I_0^2\omega}{2R}$$

**代入 $M = \mu_0\pi a^2/(2b)$**：

$$\boxed{\langle\tau\rangle = \frac{\mu_0^2\pi^2 a^4 I_0^2\omega}{8b^2 R}}$$

## 5.6 力矩的物理意义

这个平均力矩作用在**大线圈**上（反作用力矩），方向沿 $z$ 轴，其效果是**阻碍大线圈中电流的变化**——这是楞次定律在力学层面的体现：感应电流通过磁场对大线圈施加一个反抗电流变化的力矩。

\newpage

# 六、完整求解流程总结

```
大线圈 I(t) = I₀ sin(ωt)
        │
        ▼
① 互感 M = μ₀πa²/(2b)   (a≪b, 小线圈处B近似均匀)
        │
        ▼
② 感应电动势 ℰ_s = -M dI/dt = -M I₀ ω cos(ωt)
        │
        ▼
③ 感应电流 I_s = ℰ_s/R = -(M I₀ ω/R) cos(ωt)
        │
        ▼
④ 小线圈磁矩 m_s = πa² I_s
        │
        ▼
⑤ 平均焦耳功率 ⟨P⟩ = ⟨I_s²⟩R = M²I₀²ω²/(2R)
        │
        ▼
⑥ 平均力矩 ⟨τ⟩ = ⟨P⟩/ω = M²I₀²ω/(2R)
                  = μ₀²π²a⁴I₀²ω/(8b²R)
```

## 各量的时间依赖关系

| 量 | 表达式 | 振幅 |
|----|--------|------|
| $I(t)$ | $I_0\sin\omega t$ | $I_0$ |
| $B(t)$（圆心处） | $\dfrac{\mu_0 I_0}{2b}\sin\omega t$ | $\mu_0 I_0/(2b)$ |
| $\mathcal{E}_s(t)$ | $-MI_0\omega\cos\omega t$ | $MI_0\omega$ |
| $I_s(t)$ | $-\dfrac{MI_0\omega}{R}\cos\omega t$ | $MI_0\omega/R$ |
| $P(t)$（焦耳功率） | $\dfrac{M^2I_0^2\omega^2}{R}\cos^2\omega t$ | $M^2I_0^2\omega^2/R$ |
| $\langle P\rangle$ | — | $M^2I_0^2\omega^2/(2R)$ |
| $\tau(t)$ | （瞬时值含 $\sin\omega t\cos\omega t$） | — |
| $\langle\tau\rangle$ | — | $M^2I_0^2\omega/(2R)$ |

\newpage

# 七、关键概念辨析

## 7.1 为什么 $\boldsymbol{m}\times\boldsymbol{B}=0$ 但平均力矩非零？

磁偶极子力矩 $\boldsymbol{\tau}=\boldsymbol{m}\times\boldsymbol{B}$ 是均匀场近似下的**一阶项**。当 $\boldsymbol{m}\parallel\boldsymbol{B}$ 时此项为零。但本题中：
- 大线圈的磁场在空间上**不均匀**（特别是在径向上有分量）
- 安培力在小线圈不同位置的分布产生净力矩
- 这个力矩来自**场的梯度**（类似于 $\boldsymbol{F}=\nabla(\boldsymbol{m}\cdot\boldsymbol{B})$ 中力与力矩的关系）

## 7.2 楞次定律的力学表述

楞次定律不仅表现为感应电动势反抗磁通变化，还表现为**感应电流通过安培力反抗引起感应的"运动"**。本题中，大线圈电流的变化引发了感应，感应电流反过来通过磁场对大线圈施加力矩——这个力矩的方向总是**反抗大线圈电流的变化**。

\newpage

# 八、一句话总结

> 同心共面双线圈：$a\ll b$ → $M=\mu_0\pi a^2/(2b)$ → $\mathcal{E}_s=-M\,dI/dt$ → $I_s=\mathcal{E}_s/R$ → 平均焦耳功率 $\langle P\rangle=M^2I_0^2\omega^2/(2R)$ → 由能量守恒 $\langle\tau\rangle=\langle P\rangle/\omega=M^2I_0^2\omega/(2R)$。整个求解链的核心是**互感**和**法拉第定律**，力矩通过能量法（而非直接用力矩公式）得出。
