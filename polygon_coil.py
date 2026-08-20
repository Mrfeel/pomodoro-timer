#!/usr/bin/env python3
"""生成正多边形载流线圈中心磁场详解 — 毕奥-萨伐尔定律应用"""

content = r"""# 正方形载流线圈中心的磁场 —— 毕奥-萨伐尔定律手把手详解

> **题目**：边长为 $a$、通有电流 $I$ 的正方形线圈，求中心 $O$ 处的磁感应强度 $\boldsymbol{B}$。推广到正 $n$ 边形，并验证 $n\to\infty$ 时回归圆环结果。

\newpage

# 一、毕奥-萨伐尔定律回顾

## 1.1 基本公式

电流元 $I\,d\boldsymbol{l}$ 在场点 $P$ 产生的磁感应强度微元：

$$\boxed{d\boldsymbol{B} = \frac{\mu_0}{4\pi}\frac{I\,d\boldsymbol{l} \times \hat{\boldsymbol{r}}}{r^2}}$$

**大小**：$dB = \dfrac{\mu_0}{4\pi}\dfrac{I\,dl\,\sin\theta}{r^2}$，其中 $\theta$ 是 $d\boldsymbol{l}$ 与 $\hat{\boldsymbol{r}}$ 的夹角。

**方向**：右手定则——四指从 $d\boldsymbol{l}$ 弯向 $\hat{\boldsymbol{r}}$，拇指即 $d\boldsymbol{B}$ 方向。

## 1.2 有限长直导线的积分公式（关键！）

对于一段长为 $L$ 的直导线，在场点 $P$（到导线的垂直距离为 $d$）处产生的磁场：

```
        y
        ↑  导线从 y=-L/2 到 y=+L/2
        │  电流沿 +y 方向
        │
    ────●────  → x
        │ P    P点坐标 (d, 0)
        │
```

取电流元 $I\,dy\,\hat{\boldsymbol{y}}$ 位于 $(0, y)$：
- $\boldsymbol{r} = d\,\hat{\boldsymbol{x}} - y\,\hat{\boldsymbol{y}}$（从电流元指向 $P$）
- $r = \sqrt{d^2 + y^2}$
- $d\boldsymbol{l} \times \hat{\boldsymbol{r}} = dy\,\hat{\boldsymbol{y}} \times \dfrac{d\,\hat{\boldsymbol{x}} - y\,\hat{\boldsymbol{y}}}{r} = -\dfrac{d\,dy}{r}\,\hat{\boldsymbol{z}}$

（计算：$\hat{\boldsymbol{y}}\times\hat{\boldsymbol{x}}=-\hat{\boldsymbol{z}}$，$\hat{\boldsymbol{y}}\times\hat{\boldsymbol{y}}=0$）

$$\boxed{dB = \frac{\mu_0 I}{4\pi}\frac{d\,dy}{(d^2+y^2)^{3/2}}}$$

方向沿 $-\hat{\boldsymbol{z}}$（垂直纸面向内）。

**积分**：

$$B = \frac{\mu_0 I d}{4\pi}\int_{-L/2}^{L/2}\frac{dy}{(d^2+y^2)^{3/2}}$$

利用标准积分 $\displaystyle\int\frac{dy}{(d^2+y^2)^{3/2}} = \frac{y}{d^2\sqrt{d^2+y^2}}$：

$$B = \frac{\mu_0 I d}{4\pi}\left[\frac{y}{d^2\sqrt{d^2+y^2}}\right]_{-L/2}^{L/2}
= \frac{\mu_0 I d}{4\pi}\frac{L}{d^2\sqrt{d^2+(L/2)^2}}
= \frac{\mu_0 I}{4\pi d}\frac{L}{\sqrt{d^2+(L/2)^2}}$$

## 1.3 用角度表达的等价形式

定义角 $\alpha$ 为从垂足到场点的连线与导线端点的夹角：

$$\sin\alpha = \frac{L/2}{\sqrt{d^2+(L/2)^2}}$$

则：

$$\boxed{B = \frac{\mu_0 I}{4\pi d}\cdot 2\sin\alpha = \frac{\mu_0 I}{2\pi d}\sin\alpha}$$

其中 $2\alpha$ 是导线两端对场点 $P$ 的张角。这等价于教材中常用的形式：

$$\boxed{B = \frac{\mu_0 I}{4\pi d}(\sin\varphi_2 - \sin\varphi_1)}$$

其中 $\varphi_1,\varphi_2$ 是导线两端与垂线方向的夹角（从垂线逆时针为正）。

\newpage

# 二、正方形线圈的逐步计算

## 2.1 几何分析

```
         A ───────────── B
         │               │
         │       O       │  a
         │               │
         D ───────────── C
             边长 a
```

正方形四个顶点 $ABCD$，电流沿 $A\to B\to C\to D\to A$ 方向。

**关键几何量**：
- 中心 $O$ 到每条边的垂直距离：$d = a/2$
- 每条边的长度：$L = a$
- 从 $O$ 看每条边，两端与垂线方向的夹角：$\alpha = 45^\circ = \pi/4$

验证：$\tan\alpha = \dfrac{a/2}{a/2} = 1 \Rightarrow \alpha = 45^\circ$

## 2.2 单边贡献（以 $AB$ 边为例）

$AB$ 边：从 $y=-a/2$ 到 $y=+a/2$，场点 $O$ 在 $(a/2,\,0)$ 处。

### 第①步：写 $dB$ 大小

用上面推导的有限长直导线公式，$d = a/2$，$L = a$：

$$B_1 = \frac{\mu_0 I}{4\pi (a/2)}\frac{a}{\sqrt{(a/2)^2+(a/2)^2}}$$

$$= \frac{\mu_0 I}{2\pi a}\frac{a}{\sqrt{a^2/4 + a^2/4}} = \frac{\mu_0 I}{2\pi a}\frac{a}{\sqrt{a^2/2}}$$

$$= \frac{\mu_0 I}{2\pi a}\frac{a}{a/\sqrt{2}} = \frac{\mu_0 I}{2\pi a}\cdot\sqrt{2}$$

$$\boxed{B_1 = \frac{\sqrt{2}\,\mu_0 I}{2\pi a}}$$

### 第②步：用角度公式验证

$\alpha = 45^\circ$，$d = a/2$：

$$B_1 = \frac{\mu_0 I}{2\pi d}\sin\alpha = \frac{\mu_0 I}{2\pi(a/2)}\sin 45^\circ = \frac{\mu_0 I}{\pi a}\cdot\frac{\sqrt{2}}{2} = \frac{\sqrt{2}\,\mu_0 I}{2\pi a} \quad\checkmark$$

### 第③步：判断方向

$AB$ 边电流方向为 $\to$（$+y$ 方向），场点 $O$ 在导线下方（$+x$ 方向）。

用右手定则：$d\boldsymbol{l}$（沿 $+y$）弯向 $\hat{\boldsymbol{r}}$（从导线指向 $O$，即 $+x$ 偏 $-y$ 方向），拇指指向 $-\hat{\boldsymbol{z}}$（**垂直纸面向内**）。

方向记为 $\otimes$（进入纸面）。

## 2.3 四条边的叠加

**核心：四条边在中心产生的磁场大小相等、方向相同。**

| 边 | 电流方向 | 中心O在导线的 | $B$ 方向 |
|----|---------|-------------|---------|
| $AB$（上边） | 向右 | 下方 | $\otimes$（向内） |
| $BC$（右边） | 向下 | 左方 | $\otimes$（向内） |
| $CD$（下边） | 向左 | 上方 | $\otimes$（向内） |
| $DA$（左边） | 向上 | 右方 | $\otimes$（向内） |

**四条边产生的磁场方向全部一致！** 都垂直纸面向内。不存在分量抵消问题——这是正方形中心区别于轴线问题的关键。

$$\boxed{B_{\text{总}} = 4B_1 = 4\cdot\frac{\sqrt{2}\,\mu_0 I}{2\pi a} = \frac{2\sqrt{2}\,\mu_0 I}{\pi a}}$$

数值：$2\sqrt{2}/\pi \approx 0.9003$，即 $B \approx 0.900\,\dfrac{\mu_0 I}{a}$

\newpage

# 三、完整推导：从毕奥-萨伐尔原始积分出发

如果不使用有限长导线的现成公式，而是直接从毕奥-萨伐尔定律积分，同样可以验证。

## 3.1 对 $AB$ 边做原始积分

$AB$ 边在坐标系中沿 $y$ 轴，从 $y=-a/2$ 到 $y=+a/2$。中心 $O$ 在 $(a/2,\,0)$。

电流元 $I\,dy\,\hat{\boldsymbol{y}}$ 在 $(0,y)$，$\boldsymbol{r} = (a/2)\hat{\boldsymbol{x}} + (0-y)\hat{\boldsymbol{y}} = \frac{a}{2}\hat{\boldsymbol{x}} - y\hat{\boldsymbol{y}}$

$r = \sqrt{(a/2)^2 + y^2}$

$d\boldsymbol{l} \times \boldsymbol{r} = (0, dy, 0) \times (a/2, -y, 0)$

$$= \begin{vmatrix} \hat{\boldsymbol{x}} & \hat{\boldsymbol{y}} & \hat{\boldsymbol{z}} \\ 0 & dy & 0 \\ a/2 & -y & 0 \end{vmatrix}$$

$$= \hat{\boldsymbol{x}}(0-0) - \hat{\boldsymbol{y}}(0-0) + \hat{\boldsymbol{z}}(0\cdot(-y)-dy\cdot a/2)$$

$$= -\frac{a}{2}\,dy\,\hat{\boldsymbol{z}}$$

$$dB = \frac{\mu_0 I}{4\pi}\frac{|d\boldsymbol{l}\times\boldsymbol{r}|}{r^3} = \frac{\mu_0 I}{4\pi}\frac{(a/2)\,dy}{[(a/2)^2+y^2]^{3/2}}$$

$$B_1 = \frac{\mu_0 I a}{8\pi}\int_{-a/2}^{a/2}\frac{dy}{[(a/2)^2+y^2]^{3/2}}$$

换元：$y = \frac{a}{2}\tan\theta$，$dy = \frac{a}{2}\sec^2\theta\,d\theta$，$(a/2)^2+y^2 = (a/2)^2\sec^2\theta$

积分限：$y=-a/2 \to \theta=-\pi/4$，$y=+a/2 \to \theta=+\pi/4$

$$B_1 = \frac{\mu_0 I a}{8\pi}\int_{-\pi/4}^{\pi/4}\frac{(a/2)\sec^2\theta\,d\theta}{(a/2)^3\sec^3\theta}$$

$$= \frac{\mu_0 I a}{8\pi}\frac{a/2}{(a/2)^3}\int_{-\pi/4}^{\pi/4}\cos\theta\,d\theta$$

$$= \frac{\mu_0 I}{2\pi a}\int_{-\pi/4}^{\pi/4}\cos\theta\,d\theta$$

$$= \frac{\mu_0 I}{2\pi a}\bigl[\sin\theta\bigr]_{-\pi/4}^{\pi/4}$$

$$= \frac{\mu_0 I}{2\pi a}\left(\frac{\sqrt{2}}{2} - \left(-\frac{\sqrt{2}}{2}\right)\right)$$

$$\boxed{B_1 = \frac{\sqrt{2}\,\mu_0 I}{\pi a}\cdot\frac{1}{2} = \frac{\sqrt{2}\,\mu_0 I}{2\pi a}}$$

与前面结果一致 ✓

## 3.2 乘以4得最终结果

$$B_{\text{总}} = 4B_1 = \frac{2\sqrt{2}\,\mu_0 I}{\pi a}$$

\newpage

# 四、推广到正 $n$ 边形

## 4.1 几何设定

正 $n$ 边形内接于圆。设**中心到每条边的垂直距离**为 $R$（即边心距，apothem）。

```
         ╱  ╲
       ╱      ╲     正n边形
      │    ·   │    中心O
      │    O   │    ← R → 边心距
       ╲      ╱
         ╲  ╱
      每条边对中心张角 = 2π/n
```

**基本几何量**：
- 边心距：$d = R$
- 边长：$L_n = 2R\tan(\pi/n)$
- 半张角：$\alpha = \pi/n$

## 4.2 单边贡献

用有限长直导线公式，$d = R$，端点对中心的半张角为 $\pi/n$：

$$\sin\alpha = \sin\frac{\pi}{n}$$

$$B_1 = \frac{\mu_0 I}{2\pi R}\sin\frac{\pi}{n}$$

## 4.3 全部 $n$ 条边叠加

所有 $n$ 条边在中心产生的磁场大小相等、方向相同（均垂直纸面）。因此直接将单边贡献乘以 $n$：

$$\boxed{B_n = n\cdot B_1 = \frac{\mu_0 n I}{2\pi R}\sin\frac{\pi}{n}}$$

其中 $R$ 是**中心到每条边的垂直距离（边心距）**。

## 4.4 验证：$n=4$ 正方形

$R = a/2$（正方形中心到边的距离是边长一半）：

$$B_4 = \frac{\mu_0\cdot 4\cdot I}{2\pi\cdot(a/2)}\sin\frac{\pi}{4} = \frac{4\mu_0 I}{\pi a}\cdot\frac{\sqrt{2}}{2} = \frac{2\sqrt{2}\,\mu_0 I}{\pi a} \quad\checkmark$$

## 4.5 常见多边形的具体结果

| $n$ | 形状 | $\sin(\pi/n)$ | $R$（用边长 $a$ 表示） | $B$ |
|-----|------|--------------|----------------------|-----|
| 3 | 等边三角形 | $\sqrt{3}/2$ | $a/(2\sqrt{3})$ | $\dfrac{9\mu_0 I}{2\pi a}$ |
| 4 | 正方形 | $\sqrt{2}/2$ | $a/2$ | $\dfrac{2\sqrt{2}\,\mu_0 I}{\pi a}$ |
| 5 | 正五边形 | $\sqrt{10-2\sqrt{5}}/4$ | — | $\dfrac{5\mu_0 I}{2\pi R}\sin 36^\circ$ |
| 6 | 正六边形 | $1/2$ | $a\sqrt{3}/2$ | $\dfrac{3\mu_0 I}{2\pi R}$ |
| 8 | 正八边形 | $\sin 22.5^\circ$ | — | $\dfrac{4\mu_0 I}{\pi R}\sin 22.5^\circ$ |
| $\to\infty$ | 圆 | $\to\pi/n$ | $R$ | $\dfrac{\mu_0 I}{2R}$ |

## 4.6 极限 $n\to\infty$：回归圆环

当 $n\to\infty$ 时，$\sin(\pi/n) = \pi/n - (\pi/n)^3/6 + \cdots \approx \pi/n$

$$B_\infty = \lim_{n\to\infty}\frac{\mu_0 n I}{2\pi R}\sin\frac{\pi}{n} = \frac{\mu_0 n I}{2\pi R}\cdot\frac{\pi}{n} = \boxed{\frac{\mu_0 I}{2R}}$$

**这正是圆形载流线圈圆心处的磁场公式！** 边心距 $R$ 在 $n\to\infty$ 时变为圆的半径。

这一验证表明：**正 $n$ 边形中心磁场公式在 $n\to\infty$ 时连续地过渡到圆环公式**，说明推导正确。

\newpage

# 五、核心思路总结

## 5.1 逻辑链

```
毕奥-萨伐尔定律
       ↓
每个电流元产生 dB = (μ₀I/4π)(dl sinθ/r²)
       ↓
对有限长直导线做积分
       ↓
B₁ = (μ₀I/4πd)(sin φ₂ - sin φ₁) = (μ₀I/2πd) sin α
       ↓
对正n边形：d=R, α=π/n
       ↓
B₁ = (μ₀I/2πR) sin(π/n)
       ↓
n条边方向相同，直接叠加 → B = nB₁ = (μ₀nI/2πR) sin(π/n)
```

## 5.2 正方形 vs 圆环的对比

| | 正方形线圈中心 | 圆形线圈中心 |
|--|-------------|-----------|
| 单边/单弧贡献 | 需对直线做积分 | $dB$ 大小恒定，乘 $2\pi R$ |
| 分量抵消？ | **不存在**（所有边方向一致） | **不存在**（所有弧元方向一致） |
| 最终公式 | $B=\dfrac{2\sqrt{2}\mu_0 I}{\pi a}$ | $B=\dfrac{\mu_0 I}{2R}$ |
| 数值（同周长） | 周长 $4a=2\pi R$ → $a=\pi R/2$ | — |

同样周长下比较：正方形 $a=\pi R/2$：
- 正方形：$B=\dfrac{2\sqrt{2}\mu_0 I}{\pi\cdot\pi R/2}=\dfrac{4\sqrt{2}\mu_0 I}{\pi^2 R}\approx 0.573\dfrac{\mu_0 I}{R}$
- 圆环：$B=\dfrac{\mu_0 I}{2R}=0.500\dfrac{\mu_0 I}{R}$

正方形同周长下的磁场**略大于**圆环（因为边更靠近中心）。

## 5.3 这个方法为什么有效？

| 关键点 | 说明 |
|--------|------|
| **边是直的** | 每条边可用有限长直导线公式，不必重新积分 |
| **中心对称** | 各边到中心距离相等 → 贡献大小相同 |
| **方向一致** | 所有边的磁场都垂直纸面同方向 → 直接代数相加 |
| **无抵消分量** | 这比圆环轴线问题更简单——不存在需要对称性抵消的分量 |

## 5.4 一句话总结

> 正多边形线圈中心磁场的计算，本质是**有限长直导线公式的 $n$ 次叠加**：
> $$B = n \cdot \frac{\mu_0 I}{2\pi R}\sin\frac{\pi}{n}$$
> 取 $n=4$ 即得正方形结果 $\dfrac{2\sqrt{2}\mu_0 I}{\pi a}$；取 $n\to\infty$ 即回归圆环结果 $\dfrac{\mu_0 I}{2R}$。
"""

with open(r"d:\辰辰\first CC\polygon_coil.md", "w", encoding="utf-8") as f:
    f.write(content)

print("Markdown 已生成")
