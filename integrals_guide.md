# 电磁学中面积分与环路积分的计算方法

> 电磁学的四大定理全依赖面积分（通量）和环路积分（环量）。掌握它们的计算方法是解题的核心技能。

\newpage

# 第一部分：面积分（通量积分）

## 1.1 电磁学中哪些定理用到面积分？

| 定理 | 面积分形式 | 计算什么？ |
|------|-----------|-----------|
| 电场高斯定理 | $\displaystyle\oint_S\boldsymbol{D}\cdot d\boldsymbol{S}=Q_f$ | 电位移矢量的通量 |
| 磁场高斯定理 | $\displaystyle\oint_S\boldsymbol{B}\cdot d\boldsymbol{S}=0$ | 磁感应强度的通量 |
| 法拉第定律 | $\displaystyle\mathcal{E}=-\frac{d}{dt}\int_S\boldsymbol{B}\cdot d\boldsymbol{S}$ | 通过回路的磁通量 |
| 安培-麦克斯韦定律 | $\displaystyle\int_S\frac{\partial\boldsymbol{D}}{\partial t}\cdot d\boldsymbol{S}$ | 位移电流 |

## 1.2 面积分的本质

$$\Phi = \int_S \boldsymbol{F}\cdot d\boldsymbol{S}$$

**物理图像**：矢量场 $\boldsymbol{F}$ 穿过曲面 $S$ 的"总量"。

- $d\boldsymbol{S} = \hat{\boldsymbol{n}}\,dS$：面积元矢量——**大小**为面积 $dS$，**方向**为法向 $\hat{\boldsymbol{n}}$
- $\boldsymbol{F}\cdot d\boldsymbol{S} = F\cos\theta\,dS$：只计算**垂直穿过**该面积元的分量
- 对**闭合曲面**，$\hat{\boldsymbol{n}}$ 约定取**外法向**

## 1.3 计算面积分的三种策略

### 策略一：对称性+高斯定理反推（最常用！）

当矢量场在某个闭合曲面上的**大小恒定**且**方向处处平行于法向**时，面积分瞬间简化：

$$\oint_S \boldsymbol{F}\cdot d\boldsymbol{S} = F \cdot \oint_S dS = F \cdot S$$

这就是为什么电磁学中几乎所有计算题都从对称性分析开始的根本原因。

**三种经典对称性：**

| 对称性 | 选什么高斯面 | $S$（面积） | $F$ 的性质 | 典型场景 |
|--------|------------|-----------|-----------|---------|
| **球对称** | 同心球面 | $4\pi r^2$ | $F$ 只依赖于 $r$，沿径向 | 点电荷、均匀带电球体/球面 |
| **柱对称** | 同轴圆柱面（含侧面+端面） | $2\pi r l$（侧面） | $F$ 只依赖于 $r$，沿径向 | 无限长带电直线/圆柱 |
| **面对称** | 柱形高斯面（两底面+侧面） | $2S$（两底面） | $F$ 垂直于平面，大小恒定 | 无限大均匀带电平面 |

### 策略二：已知场→直接积分求通量

当已知 $\boldsymbol{F}$ 的表达式，需要求通过某曲面的通量时：

**步骤**：① 写出 $d\boldsymbol{S}$ 的表达式 ② 计算点积 $\boldsymbol{F}\cdot d\boldsymbol{S}$ ③ 积分

**典型例题**：已知点电荷电场 $\boldsymbol{E}=\dfrac{q}{4\pi\varepsilon_0 r^2}\hat{\boldsymbol{r}}$，求通过某指定曲面的电通量。

### 策略三：投影法

将曲面向坐标平面投影，用 $dx\,dy$ 或 $r\,dr\,d\varphi$ 等表示 $dS$：

$$dS = \frac{dx\,dy}{|\hat{\boldsymbol{n}}\cdot\hat{\boldsymbol{k}}|} \quad\text{（向 $xy$ 平面投影）}$$

或在柱坐标中：侧面 $dS = r\,d\varphi\,dz$，上/下底面 $dS = r\,dr\,d\varphi$

\newpage

# 第二部分：环路积分（环量积分）

## 2.1 电磁学中哪些定理用到环路积分？

| 定理 | 环路积分形式 | 计算什么？ |
|------|-------------|-----------|
| 安培环路定理 | $\displaystyle\oint_L\boldsymbol{H}\cdot d\boldsymbol{l}=I_f$ | 磁场强度环量 |
| 静电环路定理 | $\displaystyle\oint_L\boldsymbol{E}\cdot d\boldsymbol{l}=0$ | 静电场环量恒为零 |
| 法拉第定律 | $\displaystyle\oint_L\boldsymbol{E}\cdot d\boldsymbol{l}=-\frac{d\Phi}{dt}$ | 涡旋电场环量 |
| 电动势定义 | $\displaystyle\mathcal{E}=\oint_L\boldsymbol{K}\cdot d\boldsymbol{l}$ | 非静电力环量 |

## 2.2 环路积分的本质

$$\oint_L \boldsymbol{F}\cdot d\boldsymbol{l}$$

**物理图像**：矢量场 $\boldsymbol{F}$ 沿闭合路径 $L$ 的"累积投影"——走完一整圈，$\boldsymbol{F}$ 在路径切线方向的分量累加起来。

- $d\boldsymbol{l}$：路径的线元矢量——**大小**为弧长 $dl$，**方向**为路径切向
- $\boldsymbol{F}\cdot d\boldsymbol{l} = F\cos\theta\,dl$：只取**沿路径方向**的分量
- **积分方向约定**：右手定则——拇指指向面法向，四指方向为环路正方向

## 2.3 计算环路积分的三种策略

### 策略一：对称性+安培环路定理反推（最常用！）

当矢量场沿闭合环路的**切向分量大小恒定**时，环路积分瞬间简化：

$$\oint_L \boldsymbol{F}\cdot d\boldsymbol{l} = F \cdot \oint_L dl = F \cdot L$$

其中 $L$ 是环路周长（如圆形回路 $L=2\pi r$）。

**四种经典对称性（对应安培环路定理的使用）：**

| 对称性 | 安培环路形状 | $L$（周长） | $F$ 的性质 | 典型场景 |
|--------|------------|-----------|-----------|---------|
| **轴向电流+轴对称** | 同心圆 | $2\pi r$ | $F$ 沿环向，大小只依赖于 $r$ | 无限长直导线、圆柱导体 |
| **长直螺线管** | 矩形回路（部分在管内、部分在管外） | — | 管内 $F$ 均匀沿轴向 | 螺线管内部 $B$ |
| **螺绕环** | 环内同心圆 | $2\pi r$ | $F$ 沿环向 | 螺绕环内部 $B$ |
| **无限大面电流** | 矩形回路（对称跨于面两侧） | — | $F$ 平行于面、垂直于电流 | 无限大载流平板 |

### 策略二：已知场→直接参数化积分

**步骤**：① 将路径参数化 $\boldsymbol{r}(t)$ ② $d\boldsymbol{l} = \boldsymbol{r}'(t)\,dt$ ③ 计算 $\boldsymbol{F}(\boldsymbol{r}(t))\cdot\boldsymbol{r}'(t)$ ④ 对 $t$ 积分

### 策略三：分段计算+叠加

将复杂回路拆分为直线段+圆弧段，逐段计算后求和。

\newpage

# 第三部分：正负号与方向约定（最容易出错的地方）

## 3.1 面积分的法向

- **闭合曲面**（高斯定理）：$\hat{\boldsymbol{n}}$ 永远取**外法向**（指向曲面外部）
- **开曲面**（磁通量计算）：$\hat{\boldsymbol{n}}$ 取与**回路绕行方向**成右手螺旋的方向

## 3.2 环路积分的方向

**右手定则**：右手四指沿积分路径方向弯曲，拇指所指方向即为正法向。

**法拉第定律中的负号（楞次定律）**：

$$\mathcal{E} = -\frac{d\Phi}{dt}$$

如果选定回路绕行方向为 $L$，则：
- $\hat{\boldsymbol{n}}$ 由右手定则确定
- $\Phi = \int\boldsymbol{B}\cdot d\boldsymbol{S}$ 以 $\hat{\boldsymbol{n}}$ 为正向
- $\mathcal{E} = \oint\boldsymbol{E}\cdot d\boldsymbol{l}$ 以 $L$ 方向为正

**负号的意义**：$\mathcal{E}$ 为正 → 感应电流沿 $L$ 方向；$\mathcal{E}$ 为负 → 感应电流逆 $L$ 方向。

## 3.3 常见错误汇总

| 错误 | 纠正 |
|------|------|
| 高斯面选得不对称 | 面必须反映场的对称性（球面配球对称，圆柱面配柱对称） |
| 忘记端面通量（柱形高斯面） | 柱形高斯面=侧面+两端面！只有侧面有贡献时才可忽略端面 |
| 安培环路方向随意选 | 必须用右手定则与电流方向自洽 |
| 闭合面与开曲面混淆 | 高斯定理用**闭合**面；磁通量用**开**曲面（以回路为边界的面） |
| $d\boldsymbol{S}$ 和 $d\boldsymbol{l}$ 的方向弄反 | $d\boldsymbol{S}\perp$ 曲面，$d\boldsymbol{l}\parallel$ 路径；二者成右手螺旋关系 |

\newpage

# 第四部分：电磁学四大定理的积分选择速查表

| 问题 | 选什么面/回路 | 为什么？ | 得到什么？ |
|------|-------------|---------|-----------|
| 点电荷/球对称电荷的 $E$ | 同心球面 | $E$ 处处 $\perp$ 球面且大小恒定 | $E\cdot 4\pi r^2=Q/\varepsilon_0$ |
| 无限长直线/圆柱电荷的 $E$ | 同轴圆柱面 | $E$ 处处 $\perp$ 侧面（端面平行，通量为零） | $E\cdot 2\pi rl=\lambda l/\varepsilon_0$ |
| 无限大带电平面的 $E$ | 柱形高斯面（两底面跨平面两侧） | $E\perp$ 底面，侧面平行于 $E$ | $E\cdot 2S=\sigma S/\varepsilon_0$ |
| 无限长直载流导线的 $B$ | 同心圆形安培环路 | $B$ 沿环向，大小恒定 | $B\cdot 2\pi r=\mu_0 I$ |
| 长直螺线管内的 $B$ | 矩形回路（管内一段+管外一段） | 管内 $B$ 沿轴向均匀 | $Bl=\mu_0 nIl$ → $B=\mu_0 nI$ |
| 螺绕环内的 $B$ | 环内同心圆 | $B$ 沿环向，大小只依赖于 $r$ | $B\cdot 2\pi r=\mu_0 NI$ |
| 螺线管内 $dB/dt$ 产生的 $E$ | 同心圆形回路 | $E$ 沿环向，轴对称 | $E\cdot 2\pi r=-d\Phi/dt$ |

\newpage

# 第五部分：典型例题手把手演示

## 例题1：无限长均匀带电直线的电场（面积分/高斯定理）

**题目**：线电荷密度 $\lambda$，求距线 $r$ 处的电场。

**第一步——分析对称性**：无限长直线 → 柱对称。$\boldsymbol{E}$ 沿径向，大小只依赖于 $r$。

**第二步——选择高斯面**：半径为 $r$、高为 $l$ 的同轴圆柱面。

- 侧面：$d\boldsymbol{S}\parallel\hat{\boldsymbol{r}}$，$E\parallel\hat{\boldsymbol{r}}$ → $\boldsymbol{E}\cdot d\boldsymbol{S}=E\,dS$
- 两端面：$d\boldsymbol{S}\perp\hat{\boldsymbol{r}}$，$E\parallel\hat{\boldsymbol{r}}$ → $\boldsymbol{E}\cdot d\boldsymbol{S}=0$

**第三步——计算通量**：

$$\oint\boldsymbol{E}\cdot d\boldsymbol{S}=E(r)\times(\text{侧面面积})=E(r)\cdot 2\pi rl$$

**第四步——高斯定理**：

$$E(r)\cdot 2\pi rl = \frac{\lambda l}{\varepsilon_0}$$

$$E(r)=\frac{\lambda}{2\pi\varepsilon_0 r}$$

## 例题2：无限长直载流导线的磁场（环路积分/安培环路定理）

**题目**：导线载流 $I$，求距线 $r$ 处的磁感应强度。

**第一步——分析对称性**：无限长直线电流 → 柱对称。$\boldsymbol{B}$ 沿环向，大小只依赖于 $r$。

**第二步——选择安培环路**：半径为 $r$ 的同心圆。

$$d\boldsymbol{l}\parallel\boldsymbol{B}\ \Rightarrow\ \boldsymbol{B}\cdot d\boldsymbol{l}=B\,dl$$

**第三步——计算环量**：

$$\oint\boldsymbol{B}\cdot d\boldsymbol{l}=B(r)\times(\text{圆周长})=B(r)\cdot 2\pi r$$

**第四步——安培环路定理**：

$$B(r)\cdot 2\pi r = \mu_0 I$$

$$B(r)=\frac{\mu_0 I}{2\pi r}$$

## 例题3：螺线管内部磁场（矩形安培环路）

**题目**：长直螺线管 $n$ 匝/米，电流 $I$。求管内 $B$。

**第一步——分析对称性**：理想螺线管内 $\boldsymbol{B}$ 沿轴向且均匀，管外 $B\approx 0$。

**第二步——选择安培环路**：矩形 $abcd$，$ab$ 在管内平行于轴线（长 $l$），$cd$ 在管外。

**第三步——分段计算环量**：

$$\oint\boldsymbol{B}\cdot d\boldsymbol{l}=\underbrace{\int_a^b\boldsymbol{B}\cdot d\boldsymbol{l}}_{Bl}+\underbrace{\int_b^c\boldsymbol{B}\cdot d\boldsymbol{l}}_{0\ (\boldsymbol{B}\perp d\boldsymbol{l})}+\underbrace{\int_c^d\boldsymbol{B}\cdot d\boldsymbol{l}}_{0\ (B_{\text{外}}\approx 0)}+\underbrace{\int_d^a\boldsymbol{B}\cdot d\boldsymbol{l}}_{0\ (\boldsymbol{B}\perp d\boldsymbol{l})}=Bl$$

**第四步——安培环路定理**：环路包围 $nl$ 匝导线，$I_{\text{enc}}=nlI$

$$Bl=\mu_0 nlI \ \Rightarrow\ B=\mu_0 nI$$

## 例题4：螺线管中变化磁场产生的涡旋电场（法拉第定律+环路积分）

**题目**：长直螺线管半径 $R$，$dB/dt=k$（常数）。求管内外的涡旋电场。

**第一步——对称性**：轴对称 → $\boldsymbol{E}$ 沿环向，大小只依赖于 $r$。

**第二步——选圆形安培环路（半径 $r$）**：

$$\oint\boldsymbol{E}\cdot d\boldsymbol{l}=E(r)\cdot 2\pi r$$

**第三步——法拉第定律**：

- 管内 $r<R$：$\Phi=B\cdot\pi r^2$，$d\Phi/dt=\pi r^2\cdot k$
- 管外 $r>R$：$\Phi=B\cdot\pi R^2$（磁场只在管内），$d\Phi/dt=\pi R^2\cdot k$

**第四步**：

$$r<R:\ E\cdot 2\pi r=-\pi r^2 k\ \Rightarrow\ E=-\frac{kr}{2}$$
$$r>R:\ E\cdot 2\pi r=-\pi R^2 k\ \Rightarrow\ E=-\frac{kR^2}{2r}$$

\newpage

# 第六部分：一句话口诀

> **面积分**：选对高斯面，通量变乘法（$\oint\boldsymbol{F}\cdot d\boldsymbol{S}=F\cdot S$）。
>
> **环路积分**：选对安培环，环量变乘法（$\oint\boldsymbol{F}\cdot d\boldsymbol{l}=F\cdot L$）。
>
> **共同前提**：对称性！没有对称性，不能用这招。
