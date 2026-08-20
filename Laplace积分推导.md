# $\int_0^{+\infty} e^{-ux}\sin x\,dx = \frac{1}{1+u^2}$ 的推导

## 方法一：分部积分两次（最基本的做法）

令 $I = \displaystyle \int_0^{+\infty} e^{-ux}\sin x\,dx$（$u > 0$）。

### 第一次分部积分

取 $dv = \sin x\,dx$，$v = -\cos x$；$u$-替换用 $p = e^{-ux}$，$dp = -u e^{-ux}dx$。

$$I = \int_0^{+\infty} e^{-ux} \cdot \sin x\,dx$$

$$= \big[e^{-ux}(-\cos x)\big]_0^{+\infty} - \int_0^{+\infty} (-\cos x)(-u e^{-ux})\,dx$$

边界项：$x \to +\infty$ 时 $e^{-ux} \to 0$（$u>0$），$x=0$ 时 $e^{0}(-\cos 0) = -1$。

$$\big[e^{-ux}(-\cos x)\big]_0^{+\infty} = 0 - (-1) = 1$$

积分项：$-(-\cos x)(-u e^{-ux}) = -u e^{-ux}\cos x$

$$I = 1 - u\int_0^{+\infty} e^{-ux}\cos x\,dx$$

### 第二次分部积分

令 $J = \int_0^{+\infty} e^{-ux}\cos x\,dx$。取 $dv = \cos x\,dx$，$v = \sin x$。

$$J = \big[e^{-ux}\sin x\big]_0^{+\infty} - \int_0^{+\infty} \sin x \cdot (-u e^{-ux})\,dx$$

边界项：$\sin 0 = 0$，$x \to +\infty$ 时 $e^{-ux}\sin x \to 0$。所以边界项 $= 0$。

$$J = 0 + u\int_0^{+\infty} e^{-ux}\sin x\,dx = uI$$

### 联立求解

代入 $J = uI$：

$$I = 1 - u \cdot (uI) = 1 - u^2 I$$

移项：

$$I + u^2 I = 1 \;\Rightarrow\; I(1+u^2) = 1 \;\Rightarrow\; \boxed{I = \frac{1}{1+u^2}}$$

---

## 方法二：复数法（更快，推荐）

利用 Euler 公式 $e^{ix} = \cos x + i\sin x$：

$$\int_0^{+\infty} e^{-ux}\sin x\,dx = \operatorname{Im}\int_0^{+\infty} e^{-ux} \cdot e^{ix}\,dx = \operatorname{Im}\int_0^{+\infty} e^{-(u-i)x}\,dx$$

$$\int_0^{+\infty} e^{-(u-i)x}\,dx = \left[\frac{e^{-(u-i)x}}{-(u-i)}\right]_0^{+\infty} = 0 - \frac{1}{-(u-i)} = \frac{1}{u-i}$$

有理化分母：

$$\frac{1}{u-i} = \frac{u+i}{(u-i)(u+i)} = \frac{u+i}{u^2+1}$$

取虚部：

$$\operatorname{Im}\left(\frac{u+i}{u^2+1}\right) = \frac{1}{u^2+1}$$

---

## 方法对比

| 方法 | 步骤数 | 容易出错的地方 |
|------|:---:|------|
| 分部积分两次 | 较多 | 边界值符号、分部积分中符号正负 |
| 复数法 | 少 | 取虚部时别忘除以 $i$，有理化要正确 |

> 💡 考试推荐**复数法**——三步到位：合成指数 → 积出来 → 取虚部。

---

## 同理可得

$$\int_0^{+\infty} e^{-ux}\cos x\,dx = \operatorname{Re}\int_0^{+\infty} e^{-(u-i)x}dx = \frac{u}{1+u^2}$$

这是例3-2用到的公式（$u \to 1, x \to$ 积分变量）。

---

## 几何直观

$I(u) = \frac{1}{1+u^2}$ 在 $u>0$ 时递减——$u$ 越大（指数衰减越快），积分值越小：

| $u$ | $I(u)$ |
|-----|--------|
| 0 | $1$（$\int_0^\infty \sin x\,dx$ 条件收敛） |
| 1 | $\frac{1}{2}$ |
| 2 | $\frac{1}{5}$ |
| $\to \infty$ | $\to 0$ |

---

## 一句总结

> **分部积分两次 + 自循环：第一次出 $1$ 和 $\int e^{-ux}\cos x$，第二次 $\int e^{-ux}\cos x$ 变回 $\int e^{-ux}\sin x$，联立得到 $I = 1 - u^2 I$，解出 $I = \frac{1}{1+u^2}$。**
