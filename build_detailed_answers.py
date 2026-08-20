# -*- coding: utf-8 -*-
"""生成复习讲义习题答案详细版"""

parts = []

# ============ 文件头 ============
parts.append(r"""# 2026春 数分B2 期末复习讲义 —— 习题与解答（详细版）

> 题目来源：2026春数分B2期末复习讲义（第11-13章）
> 每题先列题目，后附**分步骤**详细解答，所有中间计算过程全部展示，不跳步。

---

# 第十一章：曲线积分与曲面积分

---

## 0.1 第一型曲线/曲面积分计算

**题目**（2024真题(2)(3)，2021真题(1)）：

(1) 计算 $I = \int_L y\,ds$，其中 $L: x = t - \sin t,\; y = 1 - \cos t$，$0 \leq t \leq \pi$。

(2) 计算 $\int_L e^{\sqrt{x^2+y^2}}\,ds$，$L$ 为 $x^2+y^2=4$ 与 $y=x$ 在第一象限的交线。

(3) 计算 $I = \iint_S z\,dS$，$S$ 由参数方程 $\mathbf{r}(u,v) = (u\cos v, u\sin v, v)$ 给出，$0 \leq u \leq 1$，$0 \leq v \leq 2\pi$。

---

**解答**：

### (1) 摆线弧上的第一型曲线积分

**步骤1**：第一型曲线积分的公式：
$$\int_L f(x,y)ds = \int_a^b f(x(t),y(t)) \cdot \sqrt{[x'(t)]^2 + [y'(t)]^2}\,dt$$

先求参数方程的导数：
$$x'(t) = \frac{d}{dt}(t - \sin t) = 1 - \cos t$$
$$y'(t) = \frac{d}{dt}(1 - \cos t) = \sin t$$

**步骤2**：计算弧长微元 $ds$：
$$\begin{aligned}
ds &= \sqrt{[x'(t)]^2 + [y'(t)]^2}\,dt \\
&= \sqrt{(1-\cos t)^2 + \sin^2 t}\,dt \\
&= \sqrt{1 - 2\cos t + \cos^2 t + \sin^2 t}\,dt \\
&= \sqrt{2 - 2\cos t}\,dt \quad (\text{利用 }\cos^2 t + \sin^2 t = 1) \\
&= \sqrt{2(1-\cos t)}\,dt
\end{aligned}$$

**步骤3**：利用半角公式 $1 - \cos t = 2\sin^2\frac{t}{2}$：
$$ds = \sqrt{2 \cdot 2\sin^2\frac{t}{2}}\,dt = \sqrt{4\sin^2\frac{t}{2}}\,dt = 2\left|\sin\frac{t}{2}\right|dt$$

在 $t \in [0, \pi]$ 上，$\frac{t}{2} \in [0, \frac{\pi}{2}]$，$\sin\frac{t}{2} \geq 0$，故绝对值可去掉：
$$ds = 2\sin\frac{t}{2}\,dt$$

**步骤4**：被积函数 $f(x,y) = y = 1 - \cos t$。再用半角公式：
$$y = 1 - \cos t = 2\sin^2\frac{t}{2}$$

**步骤5**：代入积分：
$$\begin{aligned}
I &= \int_0^\pi (1-\cos t) \cdot 2\sin\frac{t}{2}\,dt \\
&= \int_0^\pi 2\sin^2\frac{t}{2} \cdot 2\sin\frac{t}{2}\,dt \\
&= 4\int_0^\pi \sin^3\frac{t}{2}\,dt
\end{aligned}$$

**步骤6**：换元 $u = \frac{t}{2}$，则 $t = 2u$，$dt = 2du$。积分限：$t=0 \to u=0$，$t=\pi \to u=\frac{\pi}{2}$。
$$I = 4\int_0^{\pi/2} \sin^3 u \cdot 2\,du = 8\int_0^{\pi/2} \sin^3 u\,du$$

**步骤7**：计算 $\int_0^{\pi/2} \sin^3 u\,du$。拆分为 $\sin^3 u = \sin u \cdot \sin^2 u = \sin u(1 - \cos^2 u)$：
$$\begin{aligned}
\int_0^{\pi/2} \sin^3 u\,du &= \int_0^{\pi/2} \sin u\,du - \int_0^{\pi/2} \sin u \cos^2 u\,du
\end{aligned}$$

第一项：$\int_0^{\pi/2} \sin u\,du = \left[-\cos u\right]_0^{\pi/2} = -\cos\frac{\pi}{2} - (-\cos 0) = 0 + 1 = 1$

第二项：换元 $w = \cos u$，$dw = -\sin u\,du$。积分限：$u=0 \to w=1$，$u=\frac{\pi}{2} \to w=0$：
$$\begin{aligned}
\int_0^{\pi/2} \sin u \cos^2 u\,du &= \int_1^0 (-w^2)\,dw = \int_0^1 w^2\,dw \\
&= \left[\frac{w^3}{3}\right]_0^1 = \frac{1}{3}
\end{aligned}$$

故 $\int_0^{\pi/2} \sin^3 u\,du = 1 - \frac{1}{3} = \frac{2}{3}$

**步骤8**：代回：
$$I = 8 \times \frac{2}{3} = \frac{16}{3}$$

$$\boxed{I = \frac{16}{3}}$$

---

### (2) 圆弧上的第一型曲线积分

**步骤1**：$L$ 是圆 $x^2+y^2=4$（半径 $R=2$）在第一象限内从 $x$ 轴到直线 $y=x$ 的弧段。

参数化：$x = 2\cos\theta, \; y = 2\sin\theta$。起于 $x$ 轴正半轴（$\theta = 0$），止于 $y=x$（即 $2\cos\theta = 2\sin\theta \Rightarrow \tan\theta = 1 \Rightarrow \theta = \frac{\pi}{4}$）。

参数范围：$\theta \in [0, \frac{\pi}{4}]$。

**步骤2**：计算弧长微元 $ds$：
$$x'(\theta) = -2\sin\theta, \quad y'(\theta) = 2\cos\theta$$
$$ds = \sqrt{(-2\sin\theta)^2 + (2\cos\theta)^2}\,d\theta = \sqrt{4\sin^2\theta + 4\cos^2\theta}\,d\theta = \sqrt{4(\sin^2\theta+\cos^2\theta)}\,d\theta = \sqrt{4}\,d\theta = 2\,d\theta$$

**步骤3**：被积函数在圆弧上化简：
$$e^{\sqrt{x^2+y^2}} = e^{\sqrt{4\cos^2\theta + 4\sin^2\theta}} = e^{\sqrt{4}} = e^2$$

（在整个圆弧上 $\sqrt{x^2+y^2} = 2$ 是常数，所以被积函数恒为 $e^2$。）

**步骤4**：代入积分：
$$\begin{aligned}
\int_L e^{\sqrt{x^2+y^2}}\,ds &= \int_0^{\pi/4} e^2 \cdot 2\,d\theta \\
&= 2e^2 \int_0^{\pi/4} d\theta \\
&= 2e^2 \cdot \left[\theta\right]_0^{\pi/4} \\
&= 2e^2 \cdot \frac{\pi}{4} \\
&= \frac{\pi e^2}{2}
\end{aligned}$$

$$\boxed{\int_L e^{\sqrt{x^2+y^2}}\,ds = \frac{\pi e^2}{2}}$$

---

### (3) 参数曲面上的第一型曲面积分

**步骤1**：第一型曲面积分公式：
$$\iint_S f(x,y,z)dS = \iint_D f(\mathbf{r}(u,v)) \cdot |\mathbf{r}_u \times \mathbf{r}_v|\,du dv$$

参数方程：$\mathbf{r}(u,v) = (u\cos v, \; u\sin v, \; v)$

被积函数：$f(x,y,z) = z = v$（在参数曲面上 $z = v$）

**步骤2**：求偏导数 $\mathbf{r}_u$ 和 $\mathbf{r}_v$：
$$\mathbf{r}_u = \frac{\partial}{\partial u}(u\cos v, u\sin v, v) = (\cos v, \; \sin v, \; 0)$$
$$\mathbf{r}_v = \frac{\partial}{\partial v}(u\cos v, u\sin v, v) = (-u\sin v, \; u\cos v, \; 1)$$

**步骤3**：计算叉积 $\mathbf{r}_u \times \mathbf{r}_v$。用行列式法：
$$\begin{aligned}
\mathbf{r}_u \times \mathbf{r}_v &= \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ \cos v & \sin v & 0 \\ -u\sin v & u\cos v & 1 \end{vmatrix} \\[6pt]
&= \mathbf{i}\begin{vmatrix}\sin v & 0 \\ u\cos v & 1\end{vmatrix} - \mathbf{j}\begin{vmatrix}\cos v & 0 \\ -u\sin v & 1\end{vmatrix} + \mathbf{k}\begin{vmatrix}\cos v & \sin v \\ -u\sin v & u\cos v\end{vmatrix} \\[6pt]
&= \mathbf{i}(\sin v \cdot 1 - 0 \cdot u\cos v) - \mathbf{j}(\cos v \cdot 1 - 0 \cdot (-u\sin v)) + \mathbf{k}(\cos v \cdot u\cos v - \sin v \cdot (-u\sin v)) \\[6pt]
&= \mathbf{i}(\sin v) - \mathbf{j}(\cos v) + \mathbf{k}(u\cos^2 v + u\sin^2 v) \\[6pt]
&= (\sin v, \; -\cos v, \; u(\cos^2 v + \sin^2 v)) \\[6pt]
&= (\sin v, \; -\cos v, \; u)
\end{aligned}$$

**步骤4**：计算面积微元 $|\mathbf{r}_u \times \mathbf{r}_v|$：
$$|\mathbf{r}_u \times \mathbf{r}_v| = \sqrt{\sin^2 v + (-\cos v)^2 + u^2} = \sqrt{\sin^2 v + \cos^2 v + u^2} = \sqrt{1 + u^2}$$

**步骤5**：代入积分。参数域 $D$：$0 \leq u \leq 1$，$0 \leq v \leq 2\pi$：
$$\begin{aligned}
I &= \iint_S z\,dS = \int_0^{2\pi} \int_0^1 v \cdot \sqrt{1+u^2}\; du\,dv \\
&= \int_0^{2\pi} v\,dv \cdot \int_0^1 \sqrt{1+u^2}\,du
\end{aligned}$$

（因为被积函数可分离：$v\sqrt{1+u^2}$ 是 $v$ 的函数乘 $u$ 的函数，二重积分化为两个一维积分的乘积。）

**步骤6**：分别计算两个积分。

**对 $v$ 的积分**：
$$\int_0^{2\pi} v\,dv = \left[\frac{v^2}{2}\right]_0^{2\pi} = \frac{(2\pi)^2}{2} - 0 = \frac{4\pi^2}{2} = 2\pi^2$$

**对 $u$ 的积分** $\int_0^1 \sqrt{1+u^2}\,du$：

换元 $u = \tan\theta$，则 $du = \sec^2\theta\,d\theta$，$\sqrt{1+u^2} = \sqrt{1+\tan^2\theta} = \sec\theta$。

积分限：$u = 0 \to \theta = 0$；$u = 1 \to \theta = \frac{\pi}{4}$。

$$\begin{aligned}
\int_0^1 \sqrt{1+u^2}\,du &= \int_0^{\pi/4} \sec\theta \cdot \sec^2\theta\,d\theta \\
&= \int_0^{\pi/4} \sec^3\theta\,d\theta
\end{aligned}$$

已知积分公式：
$$\int \sec^3\theta\,d\theta = \frac{1}{2}\left(\sec\theta\tan\theta + \ln|\sec\theta + \tan\theta|\right) + C$$

代入上下限：
$$\begin{aligned}
\int_0^{\pi/4} \sec^3\theta\,d\theta &= \frac{1}{2}\left[\sec\theta\tan\theta + \ln|\sec\theta + \tan\theta|\right]_0^{\pi/4} \\[4pt]
&= \frac{1}{2}\left[\left(\sec\frac{\pi}{4}\tan\frac{\pi}{4} + \ln\left|\sec\frac{\pi}{4} + \tan\frac{\pi}{4}\right|\right) - \left(\sec 0 \tan 0 + \ln|\sec 0 + \tan 0|\right)\right] \\[4pt]
&= \frac{1}{2}\left[\left(\sqrt{2} \cdot 1 + \ln(\sqrt{2}+1)\right) - \left(1 \cdot 0 + \ln|1+0|\right)\right] \\[4pt]
&= \frac{1}{2}\left(\sqrt{2} + \ln(1+\sqrt{2}) - 0\right) \\[4pt]
&= \frac{\sqrt{2} + \ln(1+\sqrt{2})}{2}
\end{aligned}$$

**步骤7**：合起来：
$$I = 2\pi^2 \cdot \frac{\sqrt{2} + \ln(1+\sqrt{2})}{2} = \pi^2\left(\sqrt{2} + \ln(1+\sqrt{2})\right)$$

$$\boxed{I = \pi^2\left(\sqrt{2} + \ln(1+\sqrt{2})\right)}$$

---

## 0.2 势函数与保守场

**题目**（2024真题）：

设 $\mathbf{v} = (x^2,\; yz,\; \frac{y^2}{2})$。判断 $\mathbf{v}$ 是否为保守场（即是否存在势函数 $\varphi$ 使得 $\nabla\varphi = \mathbf{v}$）。

---

**解答**：

**步骤1**：保守场的判定条件。在单连通区域上，
$$\mathbf{v} = (P, Q, R) \text{ 为保守场} \iff \nabla \times \mathbf{v} = \mathbf{0}$$

记 $P = x^2$，$Q = yz$，$R = \frac{y^2}{2}$。

**步骤2**：计算旋度 $\nabla \times \mathbf{v}$：
$$\nabla \times \mathbf{v} = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ \frac{\partial}{\partial x} & \frac{\partial}{\partial y} & \frac{\partial}{\partial z} \\ P & Q & R \end{vmatrix}$$

逐分量计算：

$x$-分量（$i$ 方向）：
$$\frac{\partial R}{\partial y} - \frac{\partial Q}{\partial z} = \frac{\partial}{\partial y}\left(\frac{y^2}{2}\right) - \frac{\partial}{\partial z}(yz) = \frac{2y}{2} - y = y - y = 0$$

$y$-分量（$j$ 方向，注意符号！$j$ 分量是 $-\left(\frac{\partial R}{\partial x} - \frac{\partial P}{\partial z}\right) = \frac{\partial P}{\partial z} - \frac{\partial R}{\partial x}$）：
$$\frac{\partial P}{\partial z} - \frac{\partial R}{\partial x} = \frac{\partial}{\partial z}(x^2) - \frac{\partial}{\partial x}\left(\frac{y^2}{2}\right) = 0 - 0 = 0$$

$z$-分量（$k$ 方向）：
$$\frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y} = \frac{\partial}{\partial x}(yz) - \frac{\partial}{\partial y}(x^2) = 0 - 0 = 0$$

$$\nabla \times \mathbf{v} = (0, 0, 0) = \mathbf{0}$$

**步骤3**：$\mathbf{v}$ 的定义域是全空间 $\mathbb{R}^3$，是单连通区域（没有挖去任何点、线）。

**步骤4**：在单连通区域上旋度为零 $\Rightarrow$ 保守场。

$$\boxed{\mathbf{v} \text{ 是保守场}}$$

**补充——求势函数**（虽然题目只要求判断）：

由 $\frac{\partial\varphi}{\partial x} = x^2$，积分得 $\varphi = \frac{x^3}{3} + g(y,z)$。

代入 $\frac{\partial\varphi}{\partial y} = \frac{\partial g}{\partial y} = yz$，得 $g = \frac{y^2 z}{2} + h(z)$。

代入 $\frac{\partial\varphi}{\partial z} = \frac{y^2}{2} + h'(z) = \frac{y^2}{2}$，得 $h'(z) = 0$，$h(z) = C$。

势函数：$\varphi(x,y,z) = \frac{x^3}{3} + \frac{y^2 z}{2} + C$。

验证：$\nabla\varphi = (x^2, yz, \frac{y^2}{2}) = \mathbf{v}$ ✓。

---

## 0.3 第二型曲线积分

**题目**（2022真题(1)(2)，2021真题(3)）：

(1) 计算 $I = \int_L \frac{1}{2}y^2dx + (x-1)y\,dy$，$L: y = 2x - x^2$，从 $(0,0)$ 到 $(1,1)$。

(2) 计算 $\int_{AMB} (x^2+2xy-y^2)dx + (x^2-2xy+y^2)dy$，其中 $AMB$ 由 $A(0,-1)$ 沿 $y=x-1$ 到 $M(1,0)$，再沿 $x^2+y^2=1$ 到 $B(0,1)$。

(3) 计算 $\int_L (y+z)dx + (z+x)dy + (x+y)dz$，$L: \mathbf{r}(t)=(\cos t, \sin t, t)$，$t \in [0, 2\pi]$。

---

**解答**：

### (1) 验证积分与路径无关后改走直线

**步骤1**：记 $P(x,y) = \frac{1}{2}y^2$，$Q(x,y) = (x-1)y$。

检验积分与路径无关的条件 $\frac{\partial Q}{\partial x} = \frac{\partial P}{\partial y}$：
$$\frac{\partial Q}{\partial x} = \frac{\partial}{\partial x}[(x-1)y] = 1 \cdot y = y$$
$$\frac{\partial P}{\partial y} = \frac{\partial}{\partial y}\left[\frac{1}{2}y^2\right] = \frac{1}{2} \cdot 2y = y$$

两者相等！因此在整个平面上积分与路径无关。

**步骤2**：既然与路径无关，可以选最方便的路径。取连接 $(0,0)$ 和 $(1,1)$ 的直线段 $y = x$（$x: 0 \to 1$）。

在直线 $y=x$ 上：$dy = dx$。被积表达式：
$$\begin{aligned}
P\,dx + Q\,dy &= \frac{1}{2}y^2 dx + (x-1)y\,dy \\
&= \frac{1}{2}x^2 dx + (x-1)x\,dx \quad (\text{代入 }y=x,\; dy=dx) \\
&= \left(\frac{1}{2}x^2 + x^2 - x\right)dx \\
&= \left(\frac{3}{2}x^2 - x\right)dx
\end{aligned}$$

**步骤3**：计算定积分：
$$\begin{aligned}
I &= \int_0^1 \left(\frac{3}{2}x^2 - x\right)dx \\
&= \frac{3}{2}\int_0^1 x^2 dx - \int_0^1 x\,dx \\
&= \frac{3}{2}\left[\frac{x^3}{3}\right]_0^1 - \left[\frac{x^2}{2}\right]_0^1 \\
&= \frac{3}{2} \cdot \frac{1}{3} - \frac{1}{2} \\
&= \frac{1}{2} - \frac{1}{2} = 0
\end{aligned}$$

$$\boxed{I = 0}$$

---

### (2) 验证积分与路径无关后改走直线

**步骤1**：记 $P(x,y) = x^2 + 2xy - y^2$，$Q(x,y) = x^2 - 2xy + y^2$。

检验 $\frac{\partial Q}{\partial x} = \frac{\partial P}{\partial y}$：
$$\frac{\partial Q}{\partial x} = \frac{\partial}{\partial x}(x^2 - 2xy + y^2) = 2x - 2y$$
$$\frac{\partial P}{\partial y} = \frac{\partial}{\partial y}(x^2 + 2xy - y^2) = 2x - 2y$$

两者相等！积分与路径无关。

**步骤2**：从 $A(0,-1)$ 到 $B(0,1)$，选最简单的路径——沿 $y$ 轴（$x=0$）直走。

在 $x=0$ 上：$dx = 0$。被积表达式：
$$\begin{aligned}
P\,dx + Q\,dy &= (0^2 + 0 - y^2) \cdot 0 + (0 - 0 + y^2)\,dy \\
&= y^2\,dy
\end{aligned}$$

**步骤3**：计算积分（$y: -1 \to 1$）：
$$I = \int_{-1}^1 y^2\,dy = \left[\frac{y^3}{3}\right]_{-1}^1 = \frac{1^3}{3} - \frac{(-1)^3}{3} = \frac{1}{3} - \left(-\frac{1}{3}\right) = \frac{2}{3}$$

$$\boxed{I = \frac{2}{3}}$$

---

### (3) 三维保守场——用势函数

**步骤1**：记 $P = y+z$，$Q = z+x$，$R = x+y$。

检验旋度 $\nabla \times \mathbf{F}$：
$$\begin{aligned}
\frac{\partial R}{\partial y} - \frac{\partial Q}{\partial z} &= \frac{\partial}{\partial y}(x+y) - \frac{\partial}{\partial z}(z+x) = 1 - 1 = 0 \\[4pt]
\frac{\partial P}{\partial z} - \frac{\partial R}{\partial x} &= \frac{\partial}{\partial z}(y+z) - \frac{\partial}{\partial x}(x+y) = 1 - 1 = 0 \\[4pt]
\frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y} &= \frac{\partial}{\partial x}(z+x) - \frac{\partial}{\partial y}(y+z) = 1 - 1 = 0
\end{aligned}$$

$\nabla \times \mathbf{F} = \mathbf{0}$，且定义域为全空间 $\mathbb{R}^3$（单连通），故 $\mathbf{F}$ 为保守场。

**步骤2**：求势函数 $\varphi(x,y,z)$，满足 $\nabla\varphi = \mathbf{F}$，即：
$$\frac{\partial\varphi}{\partial x} = y+z,\quad \frac{\partial\varphi}{\partial y} = z+x,\quad \frac{\partial\varphi}{\partial z} = x+y$$

对 $x$ 积分（把 $y,z$ 当常数）：
$$\varphi = \int (y+z)\,dx = xy + xz + g(y,z)$$

其中 $g(y,z)$ 是仅含 $y,z$ 的待定函数。

对 $y$ 求偏导并与 $Q$ 比较：
$$\frac{\partial\varphi}{\partial y} = x + \frac{\partial g}{\partial y} = z + x \quad\Rightarrow\quad \frac{\partial g}{\partial y} = z$$

对 $y$ 积分：$g(y,z) = yz + h(z)$，其中 $h(z)$ 仅含 $z$。

对 $z$ 求偏导并与 $R$ 比较：
$$\frac{\partial\varphi}{\partial z} = x + y + h'(z) = x + y \quad\Rightarrow\quad h'(z) = 0 \quad\Rightarrow\quad h(z) = C$$

势函数：$\varphi(x,y,z) = xy + yz + zx + C$。

**步骤3**：曲线 $L$ 的参数方程：$\mathbf{r}(t) = (\cos t, \sin t, t)$，$t \in [0, 2\pi]$。

起点（$t=0$）：$(x_0, y_0, z_0) = (\cos 0, \sin 0, 0) = (1, 0, 0)$
终点（$t=2\pi$）：$(x_1, y_1, z_1) = (\cos 2\pi, \sin 2\pi, 2\pi) = (1, 0, 2\pi)$

**步骤4**：保守场的线积分等于势函数在终起点之差：
$$\begin{aligned}
I &= \varphi(1, 0, 2\pi) - \varphi(1, 0, 0) \\
&= (1\cdot 0 + 0\cdot 2\pi + 2\pi\cdot 1) - (1\cdot 0 + 0\cdot 0 + 0\cdot 1) \\
&= (0 + 0 + 2\pi) - 0 \\
&= 2\pi
\end{aligned}$$

$$\boxed{I = 2\pi}$$
""")

# OK, that's just the first 3 problems and it's already very long.
# Let me continue with the rest.
print("Content generated, writing to file...")

with open(r'D:\辰辰\first CC\复习讲义习题答案.md', 'w', encoding='utf-8') as f:
    f.write(''.join(parts))

print("Part A (0.1-0.3) written successfully.")
