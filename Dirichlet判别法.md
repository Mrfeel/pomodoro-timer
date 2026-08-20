# Dirichlet 判别法（反常积分收敛性）

## 一句话回答

> **"积分有界 + 单调趋于零 → 收敛"。处理含 $\sin x, \cos x$ 等振荡函数的反常积分。**

---

## 定理内容

对于反常积分 $\displaystyle \int_a^{+\infty} f(x)g(x)dx$，若满足：

| 条件 | 含义 |
|------|------|
| ① $\left|\int_a^A f(x)dx\right| \leq M$（对任意 $A \geq a$） | $f$ 的原函数（变上限积分）**一致有界** |
| ② $g(x)$ 单调且 $\lim_{x\to+\infty} g(x) = 0$ | $g$ 单调衰减到零 |

则 $\int_a^{+\infty} f(x)g(x)dx$ **收敛**。

---

## 经典例子：$\int_0^{+\infty} \frac{\sin x}{x}dx$

这就是著名的 **Dirichlet 积分**，值等于 $\frac{\pi}{2}$。

**套 Dirichlet 判别法**：

取 $f(x) = \sin x$，$g(x) = \frac{1}{x}$。

条件①：$\left|\int_0^A \sin x\,dx\right| = |1 - \cos A| \leq 2$（对任意 $A$ 有界）✓

条件②：$g(x) = \frac{1}{x}$ 单调递减，$\lim_{x\to+\infty} \frac{1}{x} = 0$ ✓

→ 积分**收敛**。

> ⚠️ 但 $\int_0^{+\infty} \left|\frac{\sin x}{x}\right|dx$ 发散！Dirichlet 判别法给的是**条件收敛**，不是绝对收敛。

---

## 三个判别法对比

| 判别法 | 条件 | 适用场景 |
|--------|------|----------|
| **Weierstrass (M-判别法)** | $\|f(x,u)\| \leq F(x)$，$\int F$ 收敛 | 找**控制函数**，最强 → 一致收敛 + 绝对收敛 |
| **Dirichlet** | $\int f$ 有界 + $g$ 单调趋于 $0$ | $\int \frac{\sin x}{x}$、$\int \frac{\cos(ux)}{x}$ 型 |
| **Abel** | $\int f$ 收敛 + $g$ 单调有界 | Dirichlet 的"补集"，如 $\int \frac{\sin x}{x}\arctan x$ |

---

## 怎么选判别法？——判断流程图

```
被积函数能写成 f(x) × g(x) 吗？
         │
    ┌────┴────┐
   是         否 → 用比较判别法 / Weierstrass
    │
    ▼
∫f 的原函数是否有界？
    │
┌───┴───┐
是       否 → 试试积分号下交换次序或比较判别法
│
▼
g(x) 是否单调趋于 0？
    │
┌───┴───┐
是       否 → g 单调有界吗？→ 是 → Abel 判别法
│
▼
Dirichlet 判别法 → 收敛！
```

---

## 含参版本的 Dirichlet 判别法

对于含参积分 $\int_a^{+\infty} f(x,u)g(x,u)dx$ 关于 $u \in I$ **一致收敛**：

| 条件 | 含义 |
|------|------|
| ① $\left|\int_a^A f(x,u)dx\right| \leq M$ | 对 $A$ 和 $u$ **一致**有界 |
| ② $g(x,u)$ 关于 $x$ 单调，且 $x\to+\infty$ 时关于 $u$ **一致**趋于 $0$ |

### 例子：$\int_0^{+\infty} \frac{\sin(ux)}{x}dx$

在 $u \in [\delta, +\infty)$（$\delta > 0$）上：

$f(x,u) = \sin(ux)$，$\left|\int_0^A \sin(ux)dx\right| = \left|\frac{1-\cos(uA)}{u}\right| \leq \frac{2}{\delta}$（对 $u$ 一致有界）

$g(x) = \frac{1}{x}$ 单调趋于 $0$（与 $u$ 无关，自然"一致"）

→ 积分关于 $u \in [\delta, +\infty)$ **一致收敛**。

但在 $u \in [0, +\infty)$ 上，$u=0$ 时 $\int_0^A \sin(0)dx = 0$ 破坏了有界性 → 不一致收敛。

---

## 与 Dirichlet 定理的区别（再次提醒）

| | Dirichlet 判别法 | Dirichlet 定理 |
|------|------|------|
| 章节 | 第13章（含参积分） | 第12章（Fourier 级数） |
| 判断什么 | 反常积分**收敛/一致收敛** | Fourier 级数**收敛到哪个值** |
| 关键条件 | $\int f$ 有界 + $g$ 单调 → $0$ | $f$ 分段单调 |
| 结论 | 积分收敛 | $S(x) = \frac{f(x^+)+f(x^-)}{2}$ |

> 💡 记忆技巧：**判别法**是用来**判**的（yes/no），**定理**是告诉你**结果**是什么（收敛到哪儿）。

---

## 一句话总结

> **Dirichlet 判别法 = "振荡 × 衰减"型积分的判据。振荡部分（$\sin, \cos$）的原函数有界，衰减部分单调趋于零，积分就收敛。含参时要求"一致"——所有参数共用一个界。**
