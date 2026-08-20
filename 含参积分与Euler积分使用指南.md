# 含参积分与 Euler 积分使用指南

---

# 第一部分：什么是 Euler 积分？

Euler 积分是两个"万能积分"——**$\Gamma$ 函数**和 **$B$ 函数**。大量的反常积分、含参积分最终都归结为它们。

---

## $\Gamma$ 函数（Gamma 函数）

### 定义

$$\boxed{\Gamma(s) = \int_0^{+\infty} t^{s-1}e^{-t}\,dt \quad (s > 0)}$$

### 怎么识别？

看到被积函数包含 **$e^{-(\cdots)}$** + **幂函数**的组合 → 考虑 $\Gamma$ 函数。

### 核心性质

| 性质 | 公式 | 作用 |
|------|------|------|
| 递推（阶乘推广） | $\Gamma(s+1) = s\Gamma(s)$ | 降次/升次 |
| 正整数 | $\Gamma(n+1) = n!$ | $\Gamma$ 是阶乘的连续推广 |
| 半整数 | $\Gamma(\frac{1}{2}) = \sqrt{\pi}$ | 出现 $\sqrt{\pi}$ 最常见的原因 |
| 余元公式 | $\Gamma(s)\Gamma(1-s) = \frac{\pi}{\sin(\pi s)}$ | 连接 $\Gamma$ 与三角函数 |

### 关键值速查

| $s$ | $\Gamma(s)$ |
|-----|-------------|
| $1$ | $1$ |
| $\frac{1}{2}$ | $\sqrt{\pi}$ |
| $\frac{3}{2}$ | $\frac{1}{2}\sqrt{\pi}$ |
| $n+1$ | $n!$ |

---

## $B$ 函数（Beta 函数）

### 定义

$$\boxed{B(p,q) = \int_0^1 t^{p-1}(1-t)^{q-1}\,dt \quad (p>0,\; q>0)}$$

### 怎么识别？

看到**积分限为 $[0,1]$** + **$t$ 的幂和 $(1-t)$ 的幂** → $B$ 函数。

### 核心性质

| 性质 | 公式 |
|------|------|
| $\Gamma$ 联系 | $B(p,q) = \frac{\Gamma(p)\Gamma(q)}{\Gamma(p+q)}$ |
| 对称性 | $B(p,q) = B(q,p)$ |

---

## 二者关系（最重要！）

$$\boxed{B(p,q) = \frac{\Gamma(p)\Gamma(q)}{\Gamma(p+q)}}$$

> 💡 **$\Gamma$ 是原子，$B$ 是分子**——$B$ 可以拆成两个 $\Gamma$ 的乘积除以一个 $\Gamma$。所以最终所有 Euler 积分都能只用 $\Gamma$ 表示。

---

# 第二部分：如何识别与构造

## 识别 $\Gamma$ 函数的变体

### 变体 1：$\int_0^{+\infty} x^\alpha e^{-kx}\,dx$（多了个系数 $k$）

**构造方法**：令 $t = kx$，$x = t/k$，$dx = dt/k$。

$$\int_0^{+\infty} x^\alpha e^{-kx}dx = \frac{1}{k^{\alpha+1}}\int_0^{+\infty} t^\alpha e^{-t}dt = \frac{\Gamma(\alpha+1)}{k^{\alpha+1}}$$

### 变体 2：$\int_0^{+\infty} e^{-x^n}dx$（指数上是 $x$ 的幂）

**构造方法**：令 $t = x^n$，$x = t^{1/n}$，$dx = \frac{1}{n}t^{1/n-1}dt$。

$$\int_0^{+\infty} e^{-x^n}dx = \frac{1}{n}\int_0^{+\infty} t^{1/n-1}e^{-t}dt = \frac{1}{n}\Gamma\!\left(\frac{1}{n}\right) = \Gamma\!\left(1 + \frac{1}{n}\right)$$

（复习讲义 0.24(1) 就是这个。）

### 变体 3：$\int_0^{+\infty} x^\alpha e^{-\beta x^\gamma}dx$

**通用换元**：$t = \beta x^\gamma$，化简后必出 $\Gamma$ 函数。

---

## 识别 $B$ 函数的变体

### 变体 1：三角形式（最重要！）

令 $t = \sin^2\theta$（或 $t = \cos^2\theta$），$dt = 2\sin\theta\cos\theta\,d\theta$：

$$\boxed{B(p,q) = 2\int_0^{\pi/2} \sin^{2p-1}\theta \cos^{2q-1}\theta\,d\theta}$$

反过来，看到 $\int_0^{\pi/2} \sin^\alpha \cos^\beta$ 就想到 $B$：

$$\boxed{\int_0^{\pi/2} \sin^\alpha\theta \cos^\beta\theta\,d\theta = \frac{1}{2}B\!\left(\frac{\alpha+1}{2}, \frac{\beta+1}{2}\right)}$$

**实例**：$\int_0^{\pi/2} \sin^2\theta\cos^2\theta\,d\theta$

$\alpha=2, \beta=2$ → $B(\frac{3}{2},\frac{3}{2})/2 = \frac{\Gamma(3/2)^2}{2\Gamma(3)} = \frac{(\sqrt{\pi}/2)^2}{2\cdot 2} = \frac{\pi/4}{4} = \frac{\pi}{16}$

### 变体 2：有理函数形式（$\int_0^{+\infty} \frac{t^{p-1}}{1+t}dt$）

这是最重要的**非 $[0,1]$ 区间**的 $B$ 函数变体：

$$\boxed{\int_0^{+\infty} \frac{t^{p-1}}{1+t}\,dt = B(p, 1-p) = \frac{\pi}{\sin(\pi p)} \quad (0 < p < 1)}$$

推导：令 $t = \frac{x}{1-x}$（$x = \frac{t}{1+t}$），将 $[0,+\infty)$ 映射到 $[0,1]$。

**实例**（复习讲义 0.23(1)）：$\int_0^{+\infty} \frac{dx}{1+x^4}$

令 $t = x^4$ → $\frac{1}{4}\int_0^{+\infty} \frac{t^{-3/4}}{1+t}dt = \frac{1}{4}\cdot\frac{\pi}{\sin(\pi/4)} = \frac{\pi}{2\sqrt{2}}$

### 变体 3：$\int_0^{+\infty} \frac{t^{p-1}}{(1+t)^{p+q}}dt$

$$\boxed{\int_0^{+\infty} \frac{t^{p-1}}{(1+t)^{p+q}}\,dt = B(p,q)}$$

（令 $u = \frac{t}{1+t}$ 可化为标准 $B$ 函数。）

---

## 识别流程图

```
看到反常积分 ↓
├─ 被积函数有 e^{-(...)} + 幂函数
│   → 换元把指数变干净 → Γ 函数
│
├─ 积分限 [0,1]，被积函数是 t^{...}(1-t)^{...}
│   → B 函数
│
├─ 积分限 [0, π/2]，被积函数是 sin^α cos^β
│   → 三角形式 → B 函数
│
├─ 积分限 [0, +∞)，被积函数是 t^{...}/(1+t)^{...}
│   → 有理形式 → B 函数 → 余元公式
│
└─ 积分限 [0, +∞)，被积函数分母是 1+t^2 或类似
    → 换元 t = x^n → B 函数有理形式
```

---

# 第三部分：含参积分怎么用？

## 核心技巧：引入参数 → 积分号下求导 → 积回去

### 标准套路（三步走）

**步骤1**：把要求的积分设为某个参数 $\alpha$ 的函数 $I(\alpha)$，使得 $I(\alpha_0)$ 是要求的积分，$I(0)$（或其他值）是已知的简单积分。

**步骤2**：积分号下对 $\alpha$ 求导，$I'(\alpha)$ 往往能积出来。

**步骤3**：$I(\alpha) = I(0) + \int_0^\alpha I'(t)dt$，得到原积分。

### 经典例子（复习讲义 0.33）

求 $I = \int_0^{+\infty} \frac{\ln(1+4x^2)}{1+x^2}dx$。

**步骤1**：令 $I(\alpha) = \int_0^{+\infty} \frac{\ln(1+\alpha x^2)}{1+x^2}dx$（$\alpha \geq 0$）。$I(0)=0$，$I = I(4)$。

**步骤2**：积分号下求导：
$$I'(\alpha) = \int_0^{+\infty} \frac{x^2}{(1+x^2)(1+\alpha x^2)}dx$$

用部分分式裂项 → 积出 $I'(\alpha) = \frac{\pi}{2\sqrt{\alpha}(1+\sqrt{\alpha})}$。

**步骤3**：$I = \int_0^4 I'(\alpha)d\alpha = \pi\ln 3$。

### 为什么这方法有效？

原来 $\ln(1+4x^2)$ 不好处理。引入参数 $\alpha$ 后，求导把 $\ln$ 变成了有理函数，就好积了。积回去就得到答案。

> 💡 本质：**用求导把复杂函数（$\ln$, $\arctan$）变成有理函数，积出来后再积回去。**

---

# 第四部分：都有什么用？

## Euler 积分的四大用途

| 用途 | 说明 | 例子 |
|------|------|------|
| **① 计算反常积分** | 大量反常积分可化为 $B/\Gamma$ | $\int_0^{\pi/2} \sin^3\theta d\theta = \frac{2}{3}$ |
| **② 求极限** | $\Gamma$ 连续，可交换极限与积分 | $\lim_{n\to\infty} \int_0^\infty e^{-x^n}dx = \Gamma(1) = 1$ |
| **③ 表示含参积分的值** | 含参积分用 $\Gamma$ 写闭式 | $\int_0^\infty \frac{x^\alpha}{1+x^2}dx = \frac{\pi}{2\cos(\pi\alpha/2)}$ |
| **④ 判断收敛域** | 借 $B/\Gamma$ 的性质判断参数范围 | $\int_0^\infty \frac{x^\alpha}{1+x^2}dx$ 定义域：$-1<\alpha<1$ |

## 含参积分的三大用途

| 用途 | 说明 |
|------|------|
| **① 计算复杂定积分** | 引入参数 → 求导 → 积回去（0.33, 0.36 的标准套路） |
| **② 判断一致收敛性** | Weierstrass / Dirichlet / Abel 用于含参情形 |
| **③ 交换次序求值** | 积分号下求导、交换积分次序（0.31 Frullani） |

---

# 第五部分：必背公式清单

## $\Gamma$ 函数

$$\Gamma(s) = \int_0^{+\infty} t^{s-1}e^{-t}dt \quad (s>0)$$

$$\Gamma(s+1) = s\Gamma(s),\quad \Gamma(n+1) = n!$$

$$\Gamma\!\left(\frac{1}{2}\right) = \sqrt{\pi}$$

$$\Gamma(s)\Gamma(1-s) = \frac{\pi}{\sin(\pi s)} \quad (0<s<1)$$

## $B$ 函数

$$B(p,q) = \int_0^1 t^{p-1}(1-t)^{q-1}dt \quad (p,q>0)$$

$$B(p,q) = \frac{\Gamma(p)\Gamma(q)}{\Gamma(p+q)}$$

$$B(p,q) = 2\int_0^{\pi/2} \sin^{2p-1}\theta \cos^{2q-1}\theta\,d\theta$$

$$\int_0^{\pi/2} \sin^\alpha\theta \cos^\beta\theta\,d\theta = \frac{1}{2}B\!\left(\frac{\alpha+1}{2}, \frac{\beta+1}{2}\right)$$

$$\int_0^{+\infty} \frac{t^{p-1}}{1+t}dt = \frac{\pi}{\sin(\pi p)} \quad (0<p<1)$$

---

## 一句话总结

> **$\Gamma$ 函数处理 $e^{-x}$ 型，$B$ 函数处理幂函数型。遇到 $\sin^\alpha\cos^\beta$ 用 $B$ 的三角形式，遇到 $t^{p-1}/(1+t)$ 用 $B$ 的有理形式。含参积分的核心技巧是"引入参数 → 求导消复杂函数 → 积回去"。**
