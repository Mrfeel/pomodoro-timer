#!/usr/bin/env python3
"""生成无限长直导线外包磁介质详解"""

content = r"""# 无限长直导线外包磁介质——$\boldsymbol{H}$、$\boldsymbol{B}$ 与磁化面电流详解

> **原题**：无限长直导线（半径 $a$，电流 $I$ 均匀分布）外包磁导率 $\mu$ 的介质（外半径 $b$）。求 $\boldsymbol{H}$、$\boldsymbol{B}$ 和磁化面电流。

\newpage

# 一、先看清这个系统

## 1.1 几何结构

```
             真空 (μ₀)
               ↑
          ╭────╮────╮
         ╱     │     ╲
        │  磁介质 μ   │  ← r = b (介质外表面)
        │    ┌─┐     │
        │    │ │ 导线 │  ← r = a (导线表面)
        │    │I│  μ₀  │
        │    └─┘     │
        │            │
         ╲          ╱
          ╰────────╯
```

| 区域 | 范围 | 材料 | 磁导率 |
|------|------|------|--------|
| ① 导线内部 | $r < a$ | 导体（铜/铝） | $\mu_0$ |
| ② 磁介质层 | $a < r < b$ | 磁介质 | $\mu$ |
| ③ 外部真空 | $r > b$ | 真空 | $\mu_0$ |

## 1.2 已知条件

- 总电流 $I$，在导线截面内**均匀分布**
- 导线半径 $a$，介质外半径 $b$
- 磁介质磁导率为 $\mu$（常数，即线性各向同性介质）
- 系统**无限长**，**轴对称**

\newpage

# 二、核心原理：$\boldsymbol{H}$ 的安培环路定理

## 2.1 为什么先求 $\boldsymbol{H}$ 而不是 $\boldsymbol{B}$？

在有磁介质时，安培环路定理有两种形式：

| 形式 | 公式 | 右边是什么 |
|------|------|----------|
| $\boldsymbol{B}$ 的安培定理 | $\oint\boldsymbol{B}\cdot d\boldsymbol{l} = \mu_0(I_f + I')$ | 自由电流 + **磁化电流**（未知！） |
| $\boldsymbol{H}$ 的安培定理 | $\oint\boldsymbol{H}\cdot d\boldsymbol{l} = I_f$ | **只有自由电流**（已知！） |

磁化电流 $I'$ 事先不知道，所以用 $\boldsymbol{B}$ 的定理会陷入死循环。而 $\boldsymbol{H}$ 的定理只涉及自由电流 $I_f$——**我们已知的量**。

$$\boxed{\oint_L \boldsymbol{H} \cdot d\boldsymbol{l} = I_{f,\text{enc}}}$$

这就是为什么在有磁介质的问题中，**总是先求 $\boldsymbol{H}$，再由 $\boldsymbol{B}=\mu\boldsymbol{H}$ 求 $\boldsymbol{B}$**。

## 2.2 对称性分析

系统具有**轴对称性**（电流沿 $z$ 轴，磁场环绕 $z$ 轴）：

- $\boldsymbol{H}$ 只有 $\varphi$ 分量：$\boldsymbol{H} = H(r)\,\hat{\boldsymbol{\varphi}}$
- $H$ 只依赖于到轴线的距离 $r$
- 取半径为 $r$ 的圆形安培环路，$d\boldsymbol{l} \parallel \hat{\boldsymbol{\varphi}}$ → $H\cdot dl = H(r)\,dl$

$$\oint \boldsymbol{H}\cdot d\boldsymbol{l} = H(r)\cdot 2\pi r = I_{f,\text{enc}}$$

$$\boxed{H(r) = \frac{I_{f,\text{enc}}}{2\pi r}}$$

## 2.3 三个区域中 $\boldsymbol{H}$ 的求解

唯一需要小心的：**$I_{f,\text{enc}}$ 在不同区域不同**。

### 区域①：导线内部 ($r < a$)

电流均匀分布 → 半径为 $r$ 的环路只包围一部分电流：

$$\frac{I_{f,\text{enc}}}{I} = \frac{\pi r^2}{\pi a^2} = \frac{r^2}{a^2}$$

$$I_{f,\text{enc}} = I\frac{r^2}{a^2}$$

$$\boxed{H_1(r) = \frac{I_{f,\text{enc}}}{2\pi r} = \frac{I r}{2\pi a^2}}$$

### 区域②：磁介质层 ($a < r < b$)

环路包围了导线的全部电流：

$$I_{f,\text{enc}} = I$$

$$\boxed{H_2(r) = \frac{I}{2\pi r}}$$

### 区域③：外部真空 ($r > b$)

同样包围全部电流：

$$\boxed{H_3(r) = \frac{I}{2\pi r}}$$

**注意**：区域②和区域③的 $H$ 公式相同！因为自由电流的包围情况相同。

\newpage

# 三、由 $\boldsymbol{H}$ 求 $\boldsymbol{B}$

## 3.1 本构关系

对于线性各向同性介质：

$$\boxed{\boldsymbol{B} = \mu\boldsymbol{H}}$$

其中 $\mu$ 是所在区域的磁导率。

## 3.2 三个区域的 $\boldsymbol{B}$

| 区域 | $H$ | $\mu$ | $B = \mu H$ |
|------|-----|-------|------------|
| ① $r<a$ | $\dfrac{Ir}{2\pi a^2}$ | $\mu_0$ | $\boxed{B_1 = \dfrac{\mu_0 I r}{2\pi a^2}}$ |
| ② $a<r<b$ | $\dfrac{I}{2\pi r}$ | $\mu$ | $\boxed{B_2 = \dfrac{\mu I}{2\pi r}}$ |
| ③ $r>b$ | $\dfrac{I}{2\pi r}$ | $\mu_0$ | $\boxed{B_3 = \dfrac{\mu_0 I}{2\pi r}}$ |

## 3.3 关键观察：$\boldsymbol{B}$ 在界面处发生了什么？

如果 $\mu > \mu_0$（顺磁/铁磁介质），在 $r=a$ 处：

$$B_{\text{介质内}}(a^+) = \frac{\mu I}{2\pi a} > \frac{\mu_0 I}{2\pi a} = B_{\text{导线内}}(a^-)$$

**$\boldsymbol{B}$ 在 $r=a$ 处发生跳变！** 因为介质被磁化后产生了磁化电流，增强了磁场。

类似地，在 $r=b$ 处也有跳变（如果 $\mu \neq \mu_0$）。

而 **$\boldsymbol{H}$ 只取决于自由电流的分布**，在 $r=a$ 和 $r=b$ 处连续（因为 $I_{f,\text{enc}}$ 跨越界面时不变）。

\newpage

# 四、磁化强度的计算

## 4.1 磁化强度的定义

$$\boxed{\boldsymbol{M} = \frac{\boldsymbol{B}}{\mu_0} - \boldsymbol{H}}$$

或等价地，对于线性介质 $\boldsymbol{M} = \chi_m\boldsymbol{H}$，其中 $\chi_m = \mu/\mu_0 - 1$。

$$\boxed{\boldsymbol{M} = \left(\frac{\mu}{\mu_0} - 1\right)\boldsymbol{H} = \frac{\mu - \mu_0}{\mu_0}\boldsymbol{H}}$$

## 4.2 磁化强度只在介质中非零

区域①（导线，$\mu=\mu_0$）：$\boldsymbol{M}=0$

区域②（介质，$\mu$）：

$$\boldsymbol{M}_2 = \frac{\mu - \mu_0}{\mu_0}\boldsymbol{H}_2 = \frac{\mu - \mu_0}{\mu_0}\cdot\frac{I}{2\pi r}\,\hat{\boldsymbol{\varphi}}$$

方向：与 $\boldsymbol{H}$ 同向（$\hat{\boldsymbol{\varphi}}$ 方向），即环绕 $z$ 轴的圆周方向。这意味着介质中的**磁化电流沿 $z$ 方向**。

区域③（真空，$\mu=\mu_0$）：$\boldsymbol{M}=0$

\newpage

# 五、磁化面电流——最精妙的部分

## 5.1 磁化面电流的公式

在介质表面，$\boldsymbol{M}$ 的切向分量不连续 → 产生**磁化面电流**：

$$\boxed{\boldsymbol{i}' = \boldsymbol{M} \times \hat{\boldsymbol{n}}}$$

其中 $\hat{\boldsymbol{n}}$ 是**介质表面指向外的法向单位矢量**。

**物理图像**：磁化电流是介质内部微观分子电流回路的宏观等效。在介质内部，相邻分子的回路电流相互抵消；在介质表面，没有相邻分子来抵消 → 剩下的"净电流"就是磁化面电流。

## 5.2 内表面 ($r = a$)：$\boldsymbol{i}'_a$

在 $r=a$ 处，磁介质的内表面。$\hat{\boldsymbol{n}}$ 指向介质内部（即沿 $-\hat{\boldsymbol{r}}$ 方向，从 $r=a$ 向 $r<a$ 指）。

等等——需要仔细确定。$\hat{\boldsymbol{n}}$ 是**从介质指向外**的法向：
- 内表面 ($r=a$)：介质在 $r>a$，外部（导线）在 $r<a$，从介质指向外 → $\hat{\boldsymbol{n}} = -\hat{\boldsymbol{r}}$
- 外表面 ($r=b$)：介质在 $r<b$，外部（真空）在 $r>b$，从介质指向外 → $\hat{\boldsymbol{n}} = +\hat{\boldsymbol{r}}$

在 $r=a$ 处，介质中 $\boldsymbol{M}(a^+) = \dfrac{\mu - \mu_0}{\mu_0}\dfrac{I}{2\pi a}\,\hat{\boldsymbol{\varphi}}$：

$$\boldsymbol{i}'_a = \boldsymbol{M}(a^+) \times (-\hat{\boldsymbol{r}}) = -\,\boldsymbol{M}(a^+) \times \hat{\boldsymbol{r}}$$

$$\hat{\boldsymbol{\varphi}} \times \hat{\boldsymbol{r}} = -\hat{\boldsymbol{z}}$$

（因为柱坐标中 $\hat{\boldsymbol{\varphi}} \times \hat{\boldsymbol{r}} = -\hat{\boldsymbol{z}}$）

$$-(\hat{\boldsymbol{\varphi}} \times \hat{\boldsymbol{r}}) = -(-\hat{\boldsymbol{z}}) = +\hat{\boldsymbol{z}}$$

$$\boxed{\boldsymbol{i}'_a = \frac{\mu - \mu_0}{\mu_0}\frac{I}{2\pi a}\,\hat{\boldsymbol{z}}}$$

**大小**：

$$\boxed{i'_a = \frac{(\mu - \mu_0)I}{2\pi \mu_0 a}}$$

方向沿 $+z$（与导线内自由电流同向）。物理上：介质的磁化增强了导线表面的有效电流。

## 5.3 外表面 ($r = b$)：$\boldsymbol{i}'_b$

在 $r=b$ 处，介质中 $\boldsymbol{M}(b^-) = \dfrac{\mu - \mu_0}{\mu_0}\dfrac{I}{2\pi b}\,\hat{\boldsymbol{\varphi}}$，$\hat{\boldsymbol{n}} = +\hat{\boldsymbol{r}}$

$$\boldsymbol{i}'_b = \boldsymbol{M}(b^-) \times \hat{\boldsymbol{r}}$$

$$\hat{\boldsymbol{\varphi}} \times \hat{\boldsymbol{r}} = -\hat{\boldsymbol{z}}$$

$$\boxed{\boldsymbol{i}'_b = -\frac{\mu - \mu_0}{\mu_0}\frac{I}{2\pi b}\,\hat{\boldsymbol{z}}}$$

**大小**：

$$\boxed{i'_b = -\frac{(\mu - \mu_0)I}{2\pi \mu_0 b}}$$

方向沿 $-z$（与自由电流反向）！

## 5.4 磁化电流守恒验证

总的磁化电流（面电流）：

$$I'_{\text{面}} = i'_a \cdot 2\pi a + i'_b \cdot 2\pi b$$

$$= \frac{(\mu - \mu_0)I}{2\pi\mu_0 a}\cdot 2\pi a - \frac{(\mu - \mu_0)I}{2\pi\mu_0 b}\cdot 2\pi b$$

$$= \frac{(\mu - \mu_0)I}{\mu_0} - \frac{(\mu - \mu_0)I}{\mu_0} = 0$$

**净磁化电流为零！** 这是必然的——磁化电流是束缚电流，只能在介质内部闭合，净流出任何闭合面必须为零。内表面 $+z$ 方向的电流与外表面 $-z$ 方向的电流通过介质内部回流形成闭合回路。

\newpage

# 六、完整的求解链路图

```
安培环路定理（H形式）
    ∮H·dl = I_f
         │
         ▼
    ┌────────────────────────┐
    │  H(r) = I_f_enc/(2πr) │
    └────────────────────────┘
         │
    ┌────┴────┬────────┐
    ▼         ▼        ▼
  r<a       a<r<b     r>b
 I_f_enc   I_f_enc   I_f_enc
 =Ir²/a²   =I        =I
    │         │        │
    ▼         ▼        ▼
 H=Ir/(2πa²) H=I/(2πr) H=I/(2πr)
    │         │        │
    ▼  μ₀     ▼  μ     ▼  μ₀
 B=μ₀Ir/(2πa²) B=μI/(2πr) B=μ₀I/(2πr)
    │         │        │
    ▼         ▼        ▼
 M=0     M=(μ/μ₀-1)H   M=0
              │
         ┌────┴────┐
         ▼         ▼
    r=a: i'_a   r=b: i'_b
    =M×(-r̂)     =M×(+r̂)
    +z方向      -z方向
```

\newpage

# 七、关键概念辨析

## 7.1 $\boldsymbol{H}$ vs $\boldsymbol{B}$ 在介质问题中的分工

| | $\boldsymbol{H}$ | $\boldsymbol{B}$ |
|--|----------------|----------------|
| 由什么决定 | **只取决于自由电流** | 自由电流 + 磁化电流 |
| 安培环路定理 | $\oint\boldsymbol{H}\cdot d\boldsymbol{l}=I_f$ | $\oint\boldsymbol{B}\cdot d\boldsymbol{l}=\mu_0(I_f+I')$ |
| 在本题中 | 三个区域用同一公式，只需算 $I_{f,\text{enc}}$ | 不同区域乘不同的 $\mu$ |
| 界面行为 | 切向分量连续（无自由面电流时） | 法向分量连续 |

## 7.2 为什么 $H$ 在 $r=a$ 和 $r=b$ 处连续？

因为界面上没有**自由**面电流——只有**磁化**面电流。$H$ 的切向分量跳变条件是：

$$\hat{\boldsymbol{n}} \times (\boldsymbol{H}_2 - \boldsymbol{H}_1) = \boldsymbol{K}_f$$

本题中自由面电流 $\boldsymbol{K}_f = 0$，所以 $H$ 切向分量连续。而 $B$ 的跳变与磁化面电流有关，所以 $B$ 在界面可以不连续。

## 7.3 介质如何"增强"了磁场？

如果 $\mu > \mu_0$（例如铁氧体 $\mu \approx 1000\mu_0$）：

在介质区域 $a<r<b$：$B = \mu I/(2\pi r) \gg \mu_0 I/(2\pi r)$

原因是：介质内的分子磁矩在外磁场下定向排列，产生与自由电流同向的磁化电流，从而增强总磁场。内表面磁化电流沿 $+z$ 方向（与自由电流同向），对介质内部贡献了额外磁场。

\newpage

# 八、手把手验算：用 $\boldsymbol{B}$ 的安培定理反推

我们可以用 $\boldsymbol{B}$ 的安培定理验证结果的正确性。

在 $a<r<b$ 区域取环路半径为 $r$：

$$\oint\boldsymbol{B}\cdot d\boldsymbol{l} = B\cdot 2\pi r = \frac{\mu I}{2\pi r}\cdot 2\pi r = \mu I$$

根据 $\boldsymbol{B}$ 的安培定理：$\oint\boldsymbol{B}\cdot d\boldsymbol{l} = \mu_0(I_f + I'_{\text{enc}})$

$$\mu I = \mu_0(I + i'_a\cdot 2\pi a)$$

（内表面磁化电流被环路包围）

$$I'_{\text{内表面}} = i'_a\cdot 2\pi a = \frac{(\mu-\mu_0)I}{2\pi\mu_0 a}\cdot 2\pi a = \frac{(\mu-\mu_0)I}{\mu_0}$$

$$\mu I = \mu_0\left(I + \frac{(\mu-\mu_0)I}{\mu_0}\right) = \mu_0\left(\frac{\mu_0 I + \mu I - \mu_0 I}{\mu_0}\right) = \mu I \quad\checkmark$$

**两边恒等，验证通过。**

\newpage

# 九、思维导图总结

```
┌─ 第一步：分析对称性 → H = H(r)φ̂
│
├─ 第二步：用 ∮H·dl = I_f 求各区域 H
│   ├─ r<a: I_f_enc = I·r²/a² → H = Ir/(2πa²)
│   ├─ a<r<b: I_f_enc = I     → H = I/(2πr)
│   └─ r>b: I_f_enc = I       → H = I/(2πr)
│
├─ 第三步：B = μH
│   ├─ r<a: B = μ₀Ir/(2πa²)
│   ├─ a<r<b: B = μI/(2πr)       ← 介质增强
│   └─ r>b: B = μ₀I/(2πr)
│
├─ 第四步：M = (μ/μ₀ - 1)H（只在介质非零）
│
└─ 第五步：i' = M × n̂
    ├─ r=a: n̂ = -r̂ → i'_a = +ẑ = (μ-μ₀)I/(2πμ₀a)
    └─ r=b: n̂ = +r̂ → i'_b = -ẑ = -(μ-μ₀)I/(2πμ₀b)
                       净磁化电流 = 0 ✓
```

## 一句话总结

> 先 $\boldsymbol{H}$（安培环路定理 + 自由电流）→ 再 $\boldsymbol{B} = \mu\boldsymbol{H}$ → 再 $\boldsymbol{M} = \boldsymbol{B}/\mu_0 - \boldsymbol{H}$ → 最后 $\boldsymbol{i}' = \boldsymbol{M}\times\hat{\boldsymbol{n}}$。四个步骤，由已知推未知，绝不跳跃。
"""

with open(r"d:\辰辰\first CC\magnetic_medium_wire.md", "w", encoding="utf-8") as f:
    f.write(content)

print("Markdown 已生成")
