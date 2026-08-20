# 为什么 $\ln x$ 不影响 $p$ 值？

## 核心原因

$\ln x$ 的增长速度比**任何**幂函数都慢。

用极限语言表述：对任意 $\varepsilon > 0$，

$$\lim_{x \to +\infty} \frac{\ln x}{x^\varepsilon} = 0, \quad \lim_{x \to 0^+} x^\varepsilon \ln x = 0$$

---

## 这意味着什么？

### $x \to +\infty$ 时

$$\frac{\ln x}{x^p} = \frac{1}{x^{p-\varepsilon}} \cdot \underbrace{\frac{\ln x}{x^\varepsilon}}_{\to 0}$$

$\ln x$ 可以"吃掉"任意小的 $\varepsilon$，使分母的指数从 $p$ 变成 $p - \varepsilon$。

### $x \to 0^+$ 时

$$\frac{\ln x}{x^p} = \frac{1}{x^{p+\varepsilon}} \cdot \underbrace{x^\varepsilon \ln x}_{\to 0}$$

$\ln x$ 同样可以被 $x^\varepsilon$ "压制"。

---

## 具体例子

### 例1：$\int_2^{+\infty} \frac{dx}{x\ln x}$

被积函数 $\sim \frac{1}{x\ln x}$。

拿 $\frac{1}{x^p}$ 比较，$p=1$。加上 $\ln x$ 在分母，直觉上应该更快衰减？

**判断**：令 $u = \ln x$，$du = \frac{dx}{x}$：

$$\int_2^{+\infty} \frac{dx}{x\ln x} = \int_{\ln 2}^{+\infty} \frac{du}{u}$$

这是 $\int^{+\infty} \frac{du}{u}$，$p = 1$（$u \to +\infty$），**发散**！

所以 $\ln x$ 确实没有"救"这个积分——$p=1$ 时还是发散。

### 例2：$\int_2^{+\infty} \frac{dx}{x(\ln x)^2}$

同样换元 $u = \ln x$：

$$\int_2^{+\infty} \frac{dx}{x(\ln x)^2} = \int_{\ln 2}^{+\infty} \frac{du}{u^2}$$

$p = 2 > 1$，**收敛**！

关键：$\frac{1}{x(\ln x)^q}$ 型积分，$x \to +\infty$ 时：
- $q > 1$：收敛
- $q \leq 1$：发散
- **$x^p$ 中的 $p=1$ 没变**，变得是 $\ln x$ 自己的指数 $q$

### 例3：$\int_2^{+\infty} \frac{dx}{x^{1.1}\ln x}$

$p = 1.1 > 1$，即使分母有个 $\ln x$（使衰减变慢），积分仍收敛。

因为对足够大的 $x$，$x^{0.05} > \ln x$（$\varepsilon = 0.05$），所以 $\frac{1}{x^{1.1}\ln x} < \frac{1}{x^{1.05}}$，$p=1.05 > 1$，收敛。

---

## 判断准则

对于 $\int^{+\infty} \frac{(\ln x)^q}{x^p}dx$：

| $p$ 值 | 结论 | 原因 |
|:---:|------|------|
| $p > 1$ | **收敛** | 幂函数已经够"狠"，$\ln x$ 添乱也救不了发散… 其实是 $x^p$ 衰减够快，$\ln x$ 拖不了后腿 |
| $p < 1$ | **发散** | 幂函数本身就不够"狠"，$\ln x$ 帮不了忙 |
| $p = 1$ | **取决于 $q$** | 这是边界情况！$q < -1$ 收敛，$q \geq -1$ 发散 |

> 💡 $\ln x$ 只在 $p=1$ 的**临界情况**才起决定作用。其他时候，看 $p$ 就够了。

---

## 为什么 $\ln x$ 比任何幂函数都弱？

直观理解：

| $x$ | $x^{0.01}$ | $\ln x$ |
|-----|-----------|---------|
| $10^3$ | $\approx 1.07$ | $\approx 6.9$ |
| $10^6$ | $\approx 1.15$ | $\approx 13.8$ |
| $10^9$ | $\approx 1.23$ | $\approx 20.7$ |
| $10^{100}$ | $\approx 10$ | $\approx 230$ |

$x^{0.01}$ 尽管指数极小，最终增长仍远超 $\ln x$（当 $x$ 足够大时）。

用 L'Hôpital 法则证明：

$$\lim_{x \to +\infty} \frac{\ln x}{x^\varepsilon} = \lim_{x \to +\infty} \frac{1/x}{\varepsilon x^{\varepsilon-1}} = \lim_{x \to +\infty} \frac{1}{\varepsilon x^\varepsilon} = 0$$

---

## 一句话总结

> **$\ln x$ 对收敛性的影响等价于常数——它比任何 $x^\varepsilon$ 都弱，所以不影响 $p$ 值。唯一的例外是 $p$ 恰好等于 $1$ 的临界情况，此时需要看 $\ln x$ 自身在分母上的幂次 $q$。**
