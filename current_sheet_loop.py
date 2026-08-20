#!/usr/bin/env python3
"""生成无限大薄板面电流安培环路选择详解"""

content = r"""# 无限大载流薄板的安培环路选择——手把手分析

> **原题**：一宽为 $2a$ 的无限长薄板载有均匀面电流，求空间中 $\boldsymbol{B}$ 的分布。
>
> **已知结论**：$B = \mu_0 K/2 = \mu_0 I/(4a)$，两侧 $\boldsymbol{B}$ 大小相等、方向相反，平行于板面且垂直于电流方向。

\newpage

# 一、先看清楚这个系统长什么样

## 1.1 几何设定

```
        z（电流方向 ⊙ 流出纸面）
        ↑
        │
   ←──────────→  x（板的宽度方向，-a 到 +a）
        │
        │   薄板在 xz 平面，无限延伸
        │   厚度可忽略（→0），宽度 2a
        │   长度无限（沿 z）
        │
        y（垂直板面方向）
```

- 薄板位于 $y=0$ 平面，$x \in [-a, a]$，$z$ 无限延伸
- 电流沿 $+z$ 方向，面电流密度 $K = I/(2a)$（单位宽度上的电流）
- $K$ 的单位：A/m

## 1.2 什么是"面电流"？

面电流密度 $\boldsymbol{K}$：流过单位宽度的电流。对于宽 $2a$、总电流 $I$ 的薄板：

$$\boxed{K = \frac{I}{2a}}$$

形象地说：把总电流 $I$ 均匀"摊"在 $2a$ 的宽度上，每米宽度流过 $K$ 安培。

\newpage

# 二、对称性分析——选择安培环路的前提

在动手选环路之前，**必须先分析对称性**。安培环路定理只有在能判断 $\boldsymbol{B}$ 的方向和依赖关系时才有效。

## 2.1 三种对称性

| 对称性 | 来源 | 结论 |
|--------|------|------|
| **$z$ 方向平移** | 板无限长 | $B$ 与 $z$ 无关，$\partial/\partial z = 0$ |
| **$x$ 方向平移**（板宽内） | 板无限宽？**不！** 板宽度有限 | $B$ 与 $x$ 有关（靠近边缘 vs. 正中央不同） |
| **$y\to -y$ 反射** | 板无限薄 | $B_x(-y) = -B_x(y)$？需要具体分析 |

**关键认识**：$x$ 方向不是平移对称的——板宽度是 $2a$，边缘效应存在。安培环路定理只能处理无限大平板（$a\to\infty$），或者我们求的是**远离边缘的中间区域**的近似解。

实际上，这道题的"标准解"假设了**板在 $x$ 方向也是无限的**（$a\to\infty$），或者我们只关心 $x \approx 0$ 附近、远小于 $a$ 的区域。此时：

$$\boxed{\text{有效对称性：板在 } xz \text{ 平面无限延伸}}$$

## 2.2 由对称性推断 $\boldsymbol{B}$ 的形式

**步骤①**：$\boldsymbol{B}$ 的方向

用右手定则：电流沿 $+z$，磁场环绕电流方向。对于 $y>0$（板上方），环绕方向是顺时针（从 $+z$ 往下看），即 $\boldsymbol{B}$ 沿 $+x$ 方向。

类似地，$y<0$（板下方），$\boldsymbol{B}$ 沿 $-x$ 方向。

$$\boxed{\boldsymbol{B} = B(y)\,\hat{\boldsymbol{x}}\;\;(\text{板上方}),\qquad \boldsymbol{B} = -B(y)\,\hat{\boldsymbol{x}}\;\;(\text{板下方})}$$

其中 $B(y) > 0$ 是待求的大小。

也可以统一写作：

$$\boldsymbol{B}(y) = B(y)\,\text{sgn}(-y)\,\hat{\boldsymbol{x}}$$

或更简单地：上方 $\to +x$，下方 $\to -x$。

**步骤②**：$B$ 的依赖关系

由于 $x$ 和 $z$ 方向的平移对称性（无限大板的假设），$B$ 只依赖于 $y$——到板面的垂直距离。

由 $y\to -y$ 的对称性：$|B(-y)| = |B(y)|$（板上方和下方磁场大小对称）。

## 2.3 为什么 $\boldsymbol{B}$ 平行于板面？

```
          板上方
    ←─────●─────→  B 方向
    ════════════  薄板（电流 ⊙ 流出）
    →─────●─────←  B 方向
          板下方
```

每个电流微元（沿 $z$）在空间产生的 $d\boldsymbol{B}$ 是以电流为轴的同心圆。对于无限大平板，所有电流微元叠加后：
- 垂直于板面的分量（$B_y$）：上方和下方的微元贡献**相互抵消**
- 平行于板面的分量（$B_x$）：所有微元贡献**同向叠加**

这类似于无限大均匀带电平面——电场垂直于板面。而这里是磁场平行于板面，方向由右手定则确定。

\newpage

# 三、安培环路的选择——"为什么是矩形？"

## 3.1 安培环路定理回顾

$$\boxed{\oint_L \boldsymbol{B} \cdot d\boldsymbol{l} = \mu_0 I_{\text{enc}}}$$

环路 $L$ 包围的净电流为 $I_{\text{enc}}$。

## 3.2 选择环路的原则

选择安培环路的三个黄金原则：

| 原则 | 说明 |
|------|------|
| **① $\boldsymbol{B} \parallel d\boldsymbol{l}$ 或 $\boldsymbol{B} \perp d\boldsymbol{l}$** | 环路上每段的 $\boldsymbol{B}$ 要么与路径平行（点积简单），要么垂直（点积为零） |
| **② $B$ 的大小在 $\boldsymbol{B}\parallel d\boldsymbol{l}$ 的段上恒定** | 这样 $\int B\,dl = B\int dl = B\cdot\text{长度}$，把积分退化为乘法 |
| **③ 环路包围的电流可计算** | $I_{\text{enc}}$ 要简单 |

## 3.3 为什么本题选矩形？

因为由对称性已知：
- $\boldsymbol{B} = \pm B(y)\hat{\boldsymbol{x}}$（沿 $x$ 方向，板上方和下方相反）
- $B$ 只依赖于 $y$

所以：
- **水平段**（平行于 $x$ 轴，即平行于板面）：$\boldsymbol{B} \parallel d\boldsymbol{l}$ → 点积 = $\pm B\,dl$
- **竖直段**（平行于 $y$ 轴，即垂直于板面）：$\boldsymbol{B} \perp d\boldsymbol{l}$ → 点积 = $0$

矩形环路的四条边**恰好满足这两个条件**！

## 3.4 矩形的具体构造

```
         y
         ↑
    ┌────●────┐  y = +h    ← 水平段②，长 l，B∥dl
    │    │    │
    │    │    │  竖直段①，B⊥dl → 贡献为0
    │    │    │
 ═══╪════╪════╪══  y = 0   ← 薄板位置
    │    │    │
    │    │    │  竖直段③，B⊥dl → 贡献为0
    │    │    │
    └────●────┘  y = -h    ← 水平段④，长 l，B∥dl
         │
         → x
    |← l →|  矩形宽度（沿 x 方向）
```

**矩形环路的四条边**：

| 段 | 位置 | 方向 | $\boldsymbol{B}$ 方向 | $\boldsymbol{B}\cdot d\boldsymbol{l}$ | 贡献 |
|----|------|------|---------------------|-------------------------------------|------|
| ① 右竖直段 | $x = +l/2$ | 从 $+h$ 到 $-h$（↓） | $\pm\hat{\boldsymbol{x}}$ | $0$（$\boldsymbol{B}\perp d\boldsymbol{l}$） | 0 |
| ② 上水平段 | $y = +h$ | 从右到左（←） | $+B(h)\hat{\boldsymbol{x}}$ | $-B(h)\,dl$（注意方向！） | $-B(h)\,l$ |
| ③ 左竖直段 | $x = -l/2$ | 从 $-h$ 到 $+h$（↑） | $\pm\hat{\boldsymbol{x}}$ | $0$（$\boldsymbol{B}\perp d\boldsymbol{l}$） | 0 |
| ④ 下水平段 | $y = -h$ | 从左到右（→） | $-B(h)\hat{\boldsymbol{x}}$ | $-B(h)\,dl$（注意！） | $-B(h)\,l$ |

## 3.5 点积符号的细致说明

这是最容易出错的地方！我们约定环路方向为逆时针，逐一检查：

**上水平段**（$y = +h$）：环路方向 ←（沿 $-x$），$\boldsymbol{B} = +B(h)\hat{\boldsymbol{x}}$（沿 $+x$）。

$$d\boldsymbol{l} = -dl\,\hat{\boldsymbol{x}},\quad \boldsymbol{B}\cdot d\boldsymbol{l} = B(h)\hat{\boldsymbol{x}}\cdot(-dl\,\hat{\boldsymbol{x}}) = -B(h)\,dl$$

**下水平段**（$y = -h$）：环路方向 →（沿 $+x$），$\boldsymbol{B} = -B(h)\hat{\boldsymbol{x}}$（沿 $-x$）。

$$d\boldsymbol{l} = +dl\,\hat{\boldsymbol{x}},\quad \boldsymbol{B}\cdot d\boldsymbol{l} = -B(h)\hat{\boldsymbol{x}}\cdot(+dl\,\hat{\boldsymbol{x}}) = -B(h)\,dl$$

**两根水平段贡献等大同号！都是 $-B(h)l$。**

## 3.6 代入安培环路定理

$$\oint \boldsymbol{B}\cdot d\boldsymbol{l} = -B(h)l - B(h)l = -2B(h)l$$

环路包围的电流：

矩形在 $x$ 方向跨度为 $l$，穿过板的这段宽度内，电流为 $K l$。

$$\mu_0 I_{\text{enc}} = \mu_0 K l$$

$$\Rightarrow -2B(h)l = \mu_0 K l$$

$$\Rightarrow B(h) = -\frac{\mu_0 K}{2}$$

负号只是表示方向约定（与环路取向有关）。大小：

$$\boxed{B = \frac{\mu_0 K}{2} = \frac{\mu_0 I}{4a}}$$

**这个结果不依赖于 $h$！** 说明在无限大平板近似下，磁场是均匀的——板上方是均匀场 $+x$ 方向，板下方是均匀场 $-x$ 方向。

\newpage

# 四、用更简单的矩形（对称放置）

上面的矩形有一条边穿过板面。更常见的做法是让矩形的两条竖直边都穿过板面：

```
         y
         ↑
    ┌────┼────┐  y = +h
    │    │    │
    │    │    │  竖直段穿过板面
    │    │    │
 ══╪════╪════╪══ y = 0
    │    │    │
    │    │    │  竖直段穿过板面
    │    │    │
    └────┼────┘  y = -h
    |← l →|
```

这种放置方式的分析完全相同：
- 两竖直段：$\boldsymbol{B} \perp d\boldsymbol{l}$ → 贡献为零
- 上水平段：$\boldsymbol{B} \parallel d\boldsymbol{l}$（但方向相反），贡献 $-B(h)l$
- 下水平段：$\boldsymbol{B} \parallel d\boldsymbol{l}$（但方向相反），贡献 $-B(h)l$
- 被包围的电流：$K l$

结果完全一致。

\newpage

# 五、为什么必须是矩形？其他形状行不行？

## 5.1 圆形环路（不行！）

圆环路上，$\boldsymbol{B}$ 的方向与 $d\boldsymbol{l}$ 的夹角不断变化——$\boldsymbol{B}\cdot d\boldsymbol{l}$ 不是常数，积分无法退化为简单乘法。而且 $\boldsymbol{B}$ 是均匀场（沿固定方向），不是环向场，圆形环路没有优势。

## 5.2 矩形环路为什么完美？

因为 $\boldsymbol{B}$ 是均匀的水平场：
- 竖直边上 $\boldsymbol{B} \perp d\boldsymbol{l}$ → 贡献为零（"免费"的边）
- 水平边上 $\boldsymbol{B} \parallel d\boldsymbol{l}$ → $B$ 的大小在这条边上处处相等 → 积分 = $B \times$ 边长

矩形环路的每条边都**恰好对齐或垂直于场的方向**——这就是安培环路选择的"艺术"。

## 5.3 类比：无限大带电平面用高斯面

| | 无限大带电平面 | 无限大载流平面 |
|--|-------------|-------------|
| 源 | 面电荷密度 $\sigma$ | 面电流密度 $K$ |
| 对称性 | 电场 $\perp$ 平面 | 磁场 $\parallel$ 平面 |
| 积分定理 | 高斯定理 | 安培环路定理 |
| 选择的面/环路 | **圆柱形高斯面**（底面∥平面） | **矩形环路**（长边∥平面） |
| 结果 | $E = \sigma/(2\varepsilon_0)$ | $B = \mu_0 K/2$ |

两者在数学结构上完全对偶——一个是"通量=源"，一个是"环量=源"。

\newpage

# 六、总结：环路选择的完整逻辑链

```
1. 对称性 → B 的方向和依赖关系
   ├── B ∥ 板面、⊥ 电流方向（±x̂方向）
   ├── B 只依赖于 y（到板的垂直距离）
   └── B(−y) = −B(y)（上方和下方大小相同、方向相反）

2. 选环路 → 让环路各边"对齐"B 的方向
   ├── B ∥ dl 的边 → 积分 = B × 边长（简单！）
   └── B ⊥ dl 的边 → 积分 = 0（更简单！）

3. 矩形 = 唯一合理选择
   ├── 水平边 ∥ 板面 = B 的方向 → B·dl 恒定
   ├── 竖直边 ⊥ 板面 = B ⊥ dl → 贡献为零
   └── 包围电流 = Kl → 简单可算

4. 代入定理 → B = μ₀K/2
```

## 一句话总结

> 矩形环路的**两条水平边平行于 $\boldsymbol{B}$**（点积简单），**两条竖直边垂直于 $\boldsymbol{B}$**（点积为零），环路包围的电流恰好是 $Kl$——三个条件同时满足，使安培环路定理的积分退化为 $2Bl = \mu_0 K l$，一步得解。
"""

with open(r"d:\辰辰\first CC\current_sheet_loop.md", "w", encoding="utf-8") as f:
    f.write(content)

print("Markdown 已生成")
