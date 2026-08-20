# Euler 积分与三角函数的关系

## 核心桥梁：$B$ 函数的三角形式

$B$ 函数的原始定义是代数形式：

$$B(p,q) = \int_0^1 t^{p-1}(1-t)^{q-1}\,dt$$

做变量代换 $t = \sin^2\theta$，立刻得到**三角形式**：

$$B(p,q) = 2\int_0^{\pi/2} \sin^{2p-1}\theta \cos^{2q-1}\theta\,d\theta$$

这就是 Euler 积分与三角函数之间的"桥梁公式"。

---

## 推导过程

令 $t = \sin^2\theta$，则：
- $dt = 2\sin\theta\cos\theta\,d\theta$
- $t=0$ 对应 $\theta=0$；$t=1$ 对应 $\theta=\pi/2$
- $1-t = 1-\sin^2\theta = \cos^2\theta$

代入：

$$B(p,q) = \int_0^{\pi/2} (\sin^2\theta)^{p-1}(\cos^2\theta)^{q-1} \cdot 2\sin\theta\cos\theta\,d\theta$$

$$= 2\int_0^{\pi/2} \sin^{2p-2}\theta \cdot \cos^{2q-2}\theta \cdot \sin\theta\cos\theta\,d\theta$$

$$= 2\int_0^{\pi/2} \sin^{2p-1}\theta \cos^{2q-1}\theta\,d\theta$$

---

## 最重要的推论

### 1. 一般 $\sin^\alpha \cos^\beta$ 的积分

令 $2p-1 = \alpha$，$2q-1 = \beta$，即 $p = \frac{\alpha+1}{2}$，$q = \frac{\beta+1}{2}$：

$$\boxed{\int_0^{\pi/2} \sin^\alpha\theta \cos^\beta\theta\,d\theta = \frac{1}{2}B\left(\frac{\alpha+1}{2}, \frac{\beta+1}{2}\right) = \frac{\Gamma(\frac{\alpha+1}{2})\Gamma(\frac{\beta+1}{2})}{2\Gamma(\frac{\alpha+\beta+2}{2})}}$$

**这是处理一切 $\sin^\alpha\cos^\beta$ 定积分的万能公式。**

### 2. 纯 $\sin^n$ 或纯 $\cos^n$

当 $\beta = 0$（即只有 $\sin$）：

$$\int_0^{\pi/2} \sin^\alpha\theta\,d\theta = \frac{1}{2}B\left(\frac{\alpha+1}{2}, \frac{1}{2}\right) = \frac{\sqrt{\pi}}{2}\frac{\Gamma(\frac{\alpha+1}{2})}{\Gamma(\frac{\alpha}{2}+1)}$$

### 3. Wallis 公式的 $\Gamma$ 函数表达

$$\int_0^{\pi/2} \sin^{2n}\theta\,d\theta = \frac{(2n-1)!!}{(2n)!!}\cdot\frac{\pi}{2} = \frac{\Gamma(n+\frac{1}{2})\Gamma(\frac{1}{2})}{2\Gamma(n+1)} = \frac{\pi}{2}\cdot\frac{(2n)!}{2^{2n}(n!)^2}$$

---

## 具体计算示例

### 例1：$\int_0^{\pi/2} \sin^3\theta\,d\theta$

$\alpha = 3, \beta = 0$：

$$\begin{aligned}
\int_0^{\pi/2} \sin^3\theta\,d\theta &= \frac{1}{2}B\left(\frac{3+1}{2}, \frac{0+1}{2}\right) = \frac{1}{2}B(2, \tfrac{1}{2}) \\[4pt]
&= \frac{1}{2}\cdot\frac{\Gamma(2)\Gamma(\frac{1}{2})}{\Gamma(\frac{5}{2})} = \frac{1}{2}\cdot\frac{1! \cdot \sqrt{\pi}}{\frac{3}{2}\cdot\frac{1}{2}\cdot\sqrt{\pi}} \\[4pt]
&= \frac{1}{2}\cdot\frac{\sqrt{\pi}}{\frac{3}{4}\sqrt{\pi}} = \frac{1}{2}\cdot\frac{4}{3} = \frac{2}{3}
\end{aligned}$$

验证（直接积分）：$\int_0^{\pi/2} (1-\cos^2\theta)\sin\theta\,d\theta = [-\cos\theta + \frac{\cos^3\theta}{3}]_0^{\pi/2} = 1 - \frac{1}{3} = \frac{2}{3}$ ✓

### 例2：$\int_0^{\pi/2} \sin^2\theta\cos^2\theta\,d\theta$

$\alpha = 2, \beta = 2$：

$$\begin{aligned}
\int_0^{\pi/2} \sin^2\theta\cos^2\theta\,d\theta &= \frac{1}{2}B\left(\tfrac{3}{2}, \tfrac{3}{2}\right) \\[4pt]
&= \frac{1}{2}\cdot\frac{\Gamma(\frac{3}{2})\Gamma(\frac{3}{2})}{\Gamma(3)} \\[4pt]
&= \frac{1}{2}\cdot\frac{(\frac{1}{2}\sqrt{\pi})^2}{2!} = \frac{1}{2}\cdot\frac{\frac{\pi}{4}}{2} = \frac{\pi}{16}
\end{aligned}$$

---

## 更深层的联系：余元公式

$$\Gamma(s)\Gamma(1-s) = \frac{\pi}{\sin(\pi s)} \quad (0 < s < 1)$$

当 $s = \frac{1}{2}$ 时：$\Gamma(\frac{1}{2})^2 = \frac{\pi}{\sin(\pi/2)} = \pi$，所以 $\Gamma(\frac{1}{2}) = \sqrt{\pi}$。

余元公式是 $\Gamma$ 函数与三角函数在**复平面**上的深层联系的体现，它说明 $\Gamma$ 函数和 $\sin$ 函数本质上是"同一类"的特殊函数。

---

## 另一个关键公式：$\int_0^\infty \frac{t^{p-1}}{1+t}\,dt$

这个积分可以化为 $B$ 函数：

$$\int_0^{+\infty} \frac{t^{p-1}}{1+t}\,dt = B(p, 1-p) = \frac{\pi}{\sin(\pi p)} \quad (0 < p < 1)$$

这是例3-7用到的核心公式，也是 Euler 积分与三角函数联系的又一体现。

---

## 知识图谱

```
                    B(p,q) = ∫₀¹ t^{p-1}(1-t)^{q-1} dt
                         │
         ┌───────────────┼───────────────┐
         │               │               │
    令 t = sin²θ     B = Γ(p)Γ(q)    令 t = x/(1+x)
         │            / Γ(p+q)           │
         ▼               │               ▼
  ∫₀^{π/2} sin^α cos^β    │      ∫₀^∞ t^{p-1}/(1+t) dt
  = ½B((α+1)/2,(β+1)/2)   │      = π/sin(πp)
                           │
                    余元公式: Γ(s)Γ(1-s) = π/sin(πs)
                           │
                    令 s=1/2: Γ(½) = √π
```

---

## 考试速记

| 公式 | 用途 |
|------|------|
| $B(p,q) = 2\int_0^{\pi/2}\sin^{2p-1}\theta\cos^{2q-1}\theta\,d\theta$ | $\sin, \cos$ 幂积分 → $B$ 函数 |
| $\int_0^{\pi/2}\sin^\alpha\cos^\beta = \frac{1}{2}B(\frac{\alpha+1}{2},\frac{\beta+1}{2})$ | 万能三角积分公式 |
| $\Gamma(s)\Gamma(1-s) = \frac{\pi}{\sin\pi s}$ | $\Gamma$ 与 $\sin$ 的深层联系 |
| $\int_0^\infty \frac{t^{p-1}}{1+t}dt = \frac{\pi}{\sin\pi p}$ | 含参积分 → 三角函数 |

---

## 一句总结

> **$B$ 函数是 $\sin$ 和 $\cos$ 幂次积分的"母函数"——通过 $t = \sin^2\theta$ 的代换，一切 $\int_0^{\pi/2}\sin^\alpha\cos^\beta$ 都可以用 $B$（进而用 $\Gamma$）表达。余元公式 $\Gamma(s)\Gamma(1-s) = \pi/\sin(\pi s)$ 则揭示了 $\Gamma$ 与三角函数在更深层次上的等价性。**
