# 散度与旋度的计算方法详解

> 散度回答："场在某点是在向外发散，还是在向内汇聚？" → 结果是**标量**
> 
> 旋度回答："场在某点是在打转，还是不打转？" → 结果是**矢量**

\newpage

# 第一部分：散度 $\nabla\cdot\boldsymbol{F}$

## 1.1 直角坐标公式（最常用）

$$\boxed{\nabla\cdot\boldsymbol{F} = \frac{\partial F_x}{\partial x} + \frac{\partial F_y}{\partial y} + \frac{\partial F_z}{\partial z}}$$

**就这么简单**：分别对 $x,y,z$ 分量求各自方向的偏导数，然后加起来。

## 1.2 手把手计算

### 例1：$\boldsymbol{F} = x\,\hat{\boldsymbol{x}} + y\,\hat{\boldsymbol{y}} + z\,\hat{\boldsymbol{z}}$

$$F_x = x,\ F_y = y,\ F_z = z$$

$$\frac{\partial F_x}{\partial x} = \frac{\partial x}{\partial x} = 1$$
$$\frac{\partial F_y}{\partial y} = \frac{\partial y}{\partial y} = 1$$
$$\frac{\partial F_z}{\partial z} = \frac{\partial z}{\partial z} = 1$$

$$\nabla\cdot\boldsymbol{F} = 1 + 1 + 1 = 3$$

**物理意义**：这个场从原点均匀向外发散，每点散度都是 3（处处有"源"）。

### 例2：$\boldsymbol{F} = y\,\hat{\boldsymbol{x}} - x\,\hat{\boldsymbol{y}}$

$$F_x = y,\ F_y = -x,\ F_z = 0$$

$$\frac{\partial F_x}{\partial x} = \frac{\partial y}{\partial x} = 0 \quad\text{(y不是x的函数，偏导为0)}$$
$$\frac{\partial F_y}{\partial y} = \frac{\partial(-x)}{\partial y} = 0 \quad\text{(x不是y的函数)}$$
$$\frac{\partial F_z}{\partial z} = 0$$

$$\nabla\cdot\boldsymbol{F} = 0 + 0 + 0 = 0$$

**物理意义**：这个场是"打转"的（漩涡状），没有向外发散——散度为零。

**关键区别**：偏导数时，把其他变量当常数！$\frac{\partial(y)}{\partial x}=0$，因为 $y$ 和 $x$ 是独立变量。

### 例3：点电荷电场 $\boldsymbol{E} = \dfrac{q}{4\pi\varepsilon_0}\dfrac{\boldsymbol{r}}{r^3}$

直角分量：$E_x = \dfrac{q}{4\pi\varepsilon_0}\dfrac{x}{(x^2+y^2+z^2)^{3/2}}$

$$\frac{\partial E_x}{\partial x} = \frac{q}{4\pi\varepsilon_0}\frac{(x^2+y^2+z^2)^{3/2} - x\cdot\frac{3}{2}(x^2+y^2+z^2)^{1/2}\cdot 2x}{(x^2+y^2+z^2)^3}$$

$$= \frac{q}{4\pi\varepsilon_0}\frac{r^2 - 3x^2}{r^5}$$

同理 $\frac{\partial E_y}{\partial y} = \frac{q}{4\pi\varepsilon_0}\frac{r^2 - 3y^2}{r^5}$，$\frac{\partial E_z}{\partial z} = \frac{q}{4\pi\varepsilon_0}\frac{r^2 - 3z^2}{r^5}$

$$\nabla\cdot\boldsymbol{E} = \frac{q}{4\pi\varepsilon_0}\frac{3r^2 - 3(x^2+y^2+z^2)}{r^5} = \frac{q}{4\pi\varepsilon_0}\frac{3r^2 - 3r^2}{r^5} = 0 \quad (r>0)$$

**物理意义**：点电荷外空间散度为零——电荷在原点（$r=0$）处，那里散度是 $\delta$ 函数发散。这正对应 $\nabla\cdot\boldsymbol{E}=\rho/\varepsilon_0$：有电荷处散度才非零。

## 1.3 柱坐标和球坐标公式

**柱坐标** $(s,\varphi,z)$：
$$\nabla\cdot\boldsymbol{F} = \frac{1}{s}\frac{\partial(sF_s)}{\partial s} + \frac{1}{s}\frac{\partial F_\varphi}{\partial\varphi} + \frac{\partial F_z}{\partial z}$$

**球坐标** $(r,\theta,\varphi)$：
$$\nabla\cdot\boldsymbol{F} = \frac{1}{r^2}\frac{\partial(r^2 F_r)}{\partial r} + \frac{1}{r\sin\theta}\frac{\partial(\sin\theta\,F_\theta)}{\partial\theta} + \frac{1}{r\sin\theta}\frac{\partial F_\varphi}{\partial\varphi}$$

### 用球坐标重做例3

$\boldsymbol{E} = \dfrac{q}{4\pi\varepsilon_0 r^2}\hat{\boldsymbol{r}}$，$F_r = \dfrac{q}{4\pi\varepsilon_0 r^2}$，$F_\theta=F_\varphi=0$。

$$\nabla\cdot\boldsymbol{E} = \frac{1}{r^2}\frac{\partial}{\partial r}\left(r^2\cdot\frac{q}{4\pi\varepsilon_0 r^2}\right) = \frac{1}{r^2}\frac{\partial}{\partial r}\left(\frac{q}{4\pi\varepsilon_0}\right) = 0 \quad (r>0)$$

**球坐标比直角坐标简单得多！选对坐标系至关重要。**

\newpage

# 第二部分：旋度 $\nabla\times\boldsymbol{F}$

## 2.1 直角坐标公式 — 行列式法

$$\boxed{\nabla\times\boldsymbol{F} = \begin{vmatrix} \hat{\boldsymbol{x}} & \hat{\boldsymbol{y}} & \hat{\boldsymbol{z}} \\[3pt] \dfrac{\partial}{\partial x} & \dfrac{\partial}{\partial y} & \dfrac{\partial}{\partial z} \\[6pt] F_x & F_y & F_z \end{vmatrix}}$$

**展开方式**：像普通 $3\times 3$ 行列式一样展开：

$$\nabla\times\boldsymbol{F} = \hat{\boldsymbol{x}}\left(\frac{\partial F_z}{\partial y} - \frac{\partial F_y}{\partial z}\right) + \hat{\boldsymbol{y}}\left(\frac{\partial F_x}{\partial z} - \frac{\partial F_z}{\partial x}\right) + \hat{\boldsymbol{z}}\left(\frac{\partial F_y}{\partial x} - \frac{\partial F_x}{\partial y}\right)$$

## 2.2 循环记忆口诀

记住 $x$ 分量的公式，另外两个分量按 **$x \to y \to z \to x$** 循环：

| 分量 | 公式 | 口诀 |
|------|------|------|
| $(\nabla\times\boldsymbol{F})_x$ | $\dfrac{\partial F_z}{\partial y} - \dfrac{\partial F_y}{\partial z}$ | "后偏前减前偏后" |
| $(\nabla\times\boldsymbol{F})_y$ | $\dfrac{\partial F_x}{\partial z} - \dfrac{\partial F_z}{\partial x}$ | 上行的 $x,y,z$ 各**后移一位** |
| $(\nabla\times\boldsymbol{F})_z$ | $\dfrac{\partial F_y}{\partial x} - \dfrac{\partial F_x}{\partial y}$ | 再后移一位 |

## 2.3 手把手计算

### 例4：$\boldsymbol{F} = y\,\hat{\boldsymbol{x}}$（只随 $y$ 变化的 $x$ 方向场）

$$F_x = y,\ F_y = 0,\ F_z = 0$$

$$(\nabla\times\boldsymbol{F})_x = \frac{\partial(0)}{\partial y} - \frac{\partial(0)}{\partial z} = 0$$
$$(\nabla\times\boldsymbol{F})_y = \frac{\partial(y)}{\partial z} - \frac{\partial(0)}{\partial x} = 0$$
$$(\nabla\times\boldsymbol{F})_z = \frac{\partial(0)}{\partial x} - \frac{\partial(y)}{\partial y} = 0 - 1 = -1$$

$$\nabla\times\boldsymbol{F} = -\hat{\boldsymbol{z}}$$

**物理图像**：场 $y\hat{\boldsymbol{x}}$ 表示——越往上（$y$ 越大），$x$ 方向的"流速"越大。这形成**顺时针旋转**的趋势，旋度沿 $-z$（即垂直纸面向内）。

```
  y↑     →→→  (y=3, 大流速)
   │      →→   (y=2)
   │       →    (y=1, 小流速)
   └──────x
  旋度 = -z（垂直纸面向内 = 顺时针）
```

### 例5：$\boldsymbol{F} = -y\,\hat{\boldsymbol{x}} + x\,\hat{\boldsymbol{y}}$（漩涡场）

$$F_x = -y,\ F_y = x,\ F_z = 0$$

$$(\nabla\times\boldsymbol{F})_z = \frac{\partial(x)}{\partial x} - \frac{\partial(-y)}{\partial y} = 1 - (-1) = 2$$

$$\nabla\times\boldsymbol{F} = 2\hat{\boldsymbol{z}}$$

**物理意义**：这就是一个标准的"漩涡"——旋度为常向量 $2\hat{\boldsymbol{z}}$，说明每点的旋转强度相同。而我们在例2中已算出**它的散度为零**——它只打转，不向外发散。

### 例6：静电场 $\boldsymbol{E} = \dfrac{q}{4\pi\varepsilon_0}\dfrac{\boldsymbol{r}}{r^3}$

用直角坐标：$E_x \propto x/r^3$，$E_y \propto y/r^3$。计算 $(\nabla\times\boldsymbol{E})_z$：

$$\frac{\partial E_y}{\partial x} = \frac{q}{4\pi\varepsilon_0}\frac{-3xy}{r^5},\quad \frac{\partial E_x}{\partial y} = \frac{q}{4\pi\varepsilon_0}\frac{-3xy}{r^5}$$

两者相等 → $(\nabla\times\boldsymbol{E})_z = 0$。同理各分量均为零。

$$\nabla\times\boldsymbol{E} = \boldsymbol{0}$$

**物理意义**：任何球对称径向场的旋度为零——这对应了 $\nabla\times\boldsymbol{E}=0$（静电场无旋）。

## 2.4 柱坐标和球坐标旋度

**柱坐标** $(s,\varphi,z)$：
$$\nabla\times\boldsymbol{F} = \hat{\boldsymbol{s}}\left(\frac{1}{s}\frac{\partial F_z}{\partial\varphi}-\frac{\partial F_\varphi}{\partial z}\right) + \hat{\boldsymbol{\varphi}}\left(\frac{\partial F_s}{\partial z}-\frac{\partial F_z}{\partial s}\right) + \hat{\boldsymbol{z}}\,\frac{1}{s}\left(\frac{\partial(sF_\varphi)}{\partial s}-\frac{\partial F_s}{\partial\varphi}\right)$$

**球坐标** $(r,\theta,\varphi)$：
$$\nabla\times\boldsymbol{F} = \hat{\boldsymbol{r}}\frac{1}{r\sin\theta}\left[\frac{\partial(\sin\theta F_\varphi)}{\partial\theta}-\frac{\partial F_\theta}{\partial\varphi}\right] + \hat{\boldsymbol{\theta}}\frac{1}{r}\left[\frac{1}{\sin\theta}\frac{\partial F_r}{\partial\varphi}-\frac{\partial(rF_\varphi)}{\partial r}\right] + \hat{\boldsymbol{\varphi}}\frac{1}{r}\left[\frac{\partial(rF_\theta)}{\partial r}-\frac{\partial F_r}{\partial\theta}\right]$$

### 例7：用柱坐标计算例5的旋度

例5的场在柱坐标中：$F_s=0$，$F_\varphi = s$（因为 $x\hat{\boldsymbol{y}}-y\hat{\boldsymbol{x}} = s\hat{\boldsymbol{\varphi}}$），$F_z=0$。

$$(\nabla\times\boldsymbol{F})_z = \frac{1}{s}\frac{\partial(s\cdot s)}{\partial s} = \frac{1}{s}\frac{\partial(s^2)}{\partial s} = \frac{1}{s}\cdot 2s = 2$$

$$\nabla\times\boldsymbol{F} = 2\hat{\boldsymbol{z}}$$

**柱坐标一行就算出来了。** 比直角坐标三个分量分别算快得多。

\newpage

# 第三部分：散度与旋度的一眼区分法

| | 散度 $\nabla\cdot\boldsymbol{F}$ | 旋度 $\nabla\times\boldsymbol{F}$ |
|--|-------------------------------|-------------------------------|
| 衡量什么 | "发散"还是"汇聚" | "旋转"还是不转 |
| 结果类型 | **标量**（一个数） | **矢量**（有大小和方向） |
| 典型非零场 | 点电荷电场（$r\neq0$ 处为0） | 直线电流磁场、漩涡水流 |
| 典型零场 | 直线电流磁场（无散） | 点电荷电场（无旋） |
| **电磁学核心方程** | $\nabla\cdot\boldsymbol{D}=\rho_f$ | $\nabla\times\boldsymbol{H}=\boldsymbol{j}_f$ |

## 视觉判断

```
散度≠0（发散场）              旋度≠0（有旋场）
    ←  ●  →                      ↺↺↺
    ←  ●  →                      ↑   ↓
    ←  ●  →                      ↑   ↓
箭头从中心向外                    ↻↻↻
```

\newpage

# 第四部分：散度定理与斯托克斯定理

这两个定理将微分运算与积分联系起来，是电磁学四大定理的基础。

## 4.1 散度定理（高斯定理的数学基础）

$$\boxed{\oint_S \boldsymbol{F}\cdot d\boldsymbol{S} = \int_V (\nabla\cdot\boldsymbol{F})\,dV}$$

**通量 = 散度的体积分**。闭合面上的净流出量 = 内部所有"源"的总和。

**用法**：当你知道某点散度→可以求体积分；反过来，已知闭合面通量→可以反推散度（取小体积极限）。

## 4.2 斯托克斯定理

$$\boxed{\oint_L \boldsymbol{F}\cdot d\boldsymbol{l} = \int_S (\nabla\times\boldsymbol{F})\cdot d\boldsymbol{S}}$$

**环量 = 旋度的面积分**。沿闭合回路的累积投影 = 穿过回路面积所有"旋转"的总和。

**用法**：安培环路定理和法拉第定律都可以写成这种形式。$\oint\boldsymbol{H}\cdot d\boldsymbol{l}=I_f$ 等价于 $\nabla\times\boldsymbol{H}=\boldsymbol{j}_f$。

\newpage

# 第五部分：电磁学中散度与旋度的应用总览

| 场 | 散度 | 旋度 | 说明 |
|----|------|------|------|
| 静电场 $\boldsymbol{E}$ | $\nabla\cdot\boldsymbol{E}=\rho/\varepsilon_0$ | $\nabla\times\boldsymbol{E}=0$ | **有散无旋** |
| 电位移 $\boldsymbol{D}$ | $\nabla\cdot\boldsymbol{D}=\rho_f$ | — | 散度仅与自由电荷有关 |
| 静磁场 $\boldsymbol{B}$ | $\nabla\cdot\boldsymbol{B}=0$ | $\nabla\times\boldsymbol{B}=\mu_0\boldsymbol{j}$ | **无散有旋** |
| 磁场强度 $\boldsymbol{H}$ | — | $\nabla\times\boldsymbol{H}=\boldsymbol{j}_f$ | 旋度仅与自由电流有关 |
| 涡旋电场 $\boldsymbol{E}$ | — | $\nabla\times\boldsymbol{E}=-\partial\boldsymbol{B}/\partial t$ | 变磁场 → 有旋电场 |
| 磁矢势 $\boldsymbol{A}$ | $\nabla\cdot\boldsymbol{A}=0$（库仑规范） | $\nabla\times\boldsymbol{A}=\boldsymbol{B}$ | $\boldsymbol{A}$的旋度=$\boldsymbol{B}$ |
| 极化强度 $\boldsymbol{P}$ | $\rho'=-\nabla\cdot\boldsymbol{P}$ | — | 散度→束缚电荷 |
| 磁化强度 $\boldsymbol{M}$ | — | $\boldsymbol{j}'=\nabla\times\boldsymbol{M}$ | 旋度→束缚电流 |

## 关键结论

1. **电场有散（源于电荷）但无旋（静电场可定义电势）**
2. **磁场无散（无磁单极子）但有旋（源于电流）**
3. **变化的磁场使电场产生旋度**（涡旋电场，不能定义标量势）
4. **变化的电场使磁场产生旋度**（位移电流，麦克斯韦的伟大发现）

\newpage

# 第六部分：考试速查卡

## 哪些场散度为零？（无需计算，直接判断）

- 任何**磁感应强度 $\boldsymbol{B}$**——$\nabla\cdot\boldsymbol{B}=0$ 恒成立
- 任何**均匀场**——所有分量都是常数，偏导数为零
- 任何**可写为旋度的场** $\boldsymbol{F}=\nabla\times\boldsymbol{A}$——$\nabla\cdot(\nabla\times\boldsymbol{A})\equiv 0$

## 哪些场旋度为零？（无需计算，直接判断）

- 任何**静电场 $\boldsymbol{E}$**——$\nabla\times\boldsymbol{E}=0$ 
- 任何**球对称径向场** $\boldsymbol{F}=f(r)\hat{\boldsymbol{r}}$
- 任何**均匀场**
- 任何**可写为梯度的场** $\boldsymbol{F}=\nabla\psi$——$\nabla\times(\nabla\psi)\equiv 0$

## 两个恒等式（数学上恒成立）

$$\nabla\cdot(\nabla\times\boldsymbol{F}) \equiv 0 \quad\text{（旋度的散度恒为零）}$$
$$\nabla\times(\nabla\psi) \equiv 0 \quad\text{（梯度的旋度恒为零）}$$

这两个恒等式是电磁学中引入**标量势** $\varphi$ 和**矢量势** $\boldsymbol{A}$ 的数学基础：
- $\nabla\times\boldsymbol{E}=0 \Rightarrow \boldsymbol{E}=-\nabla\varphi$（静电场可写为标势的梯度）
- $\nabla\cdot\boldsymbol{B}=0 \Rightarrow \boldsymbol{B}=\nabla\times\boldsymbol{A}$（磁场可写为矢势的旋度）

## 计算步骤总结

**散度**：三个偏导数相加 → 一个数 → 判断有无"源"

**旋度**：六个偏导数按 $x\to y\to z\to x$ 循环 → 一个矢量 → 判断有无"旋转"

**共同技巧**：球对称→球坐标；柱对称→柱坐标；无对称性→直角坐标。选对坐标系，计算量天差地别。
