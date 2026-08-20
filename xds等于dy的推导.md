# $x\,ds = dy$，$y\,ds = -dx$ 是怎么来的？

## 来源：单位圆的参数化

在**单位圆** $x^2+y^2=1$ 上，取标准参数化（逆时针方向）：

$$x = \cos\theta, \quad y = \sin\theta, \quad \theta \in [0, 2\pi]$$

---

## 推导

### 弧长微元

单位圆半径 $R=1$，$ds = 1 \cdot d\theta = d\theta$。

### 坐标微分

$$dx = \frac{dx}{d\theta}d\theta = -\sin\theta \cdot d\theta$$
$$dy = \frac{dy}{d\theta}d\theta = \cos\theta \cdot d\theta$$

### 关键替换

因为 $x = \cos\theta$，$y = \sin\theta$，且 $ds = d\theta$：

$$x \cdot ds = \cos\theta \cdot d\theta = dy \quad \Rightarrow \quad \boxed{x\,ds = dy}$$

$$y \cdot ds = \sin\theta \cdot d\theta = -(-\sin\theta \cdot d\theta) = -dx \quad \Rightarrow \quad \boxed{y\,ds = -dx}$$

---

## 一步到位

| 参数化 | 微分 | 用 $ds$ 表达 |
|--------|------|-------------|
| $x = \cos\theta$ | $dx = -\sin\theta\,d\theta$ | $dx = -y\,ds$ |
| $y = \sin\theta$ | $dy = \cos\theta\,d\theta$ | $dy = x\,ds$ |
| 弧长 | $ds = d\theta$ | — |

---

## 在例1-4中怎么用的？

原式：

$$\oint_{\partial D} \frac{\partial u}{\partial n} \, ds$$

在单位圆上 $\mathbf{n} = (x, y)$，所以 $\frac{\partial u}{\partial n} = \frac{\partial u}{\partial x} \cdot x + \frac{\partial u}{\partial y} \cdot y$。

于是：

$$\oint_{\partial D} \left(\frac{\partial u}{\partial x} \cdot x + \frac{\partial u}{\partial y} \cdot y\right) ds = \oint_{\partial D} \frac{\partial u}{\partial x} \cdot (x\,ds) + \frac{\partial u}{\partial y} \cdot (y\,ds)$$

用 $x\,ds = dy$，$y\,ds = -dx$ 替换：

$$= \oint_{\partial D} \frac{\partial u}{\partial x} \, dy + \frac{\partial u}{\partial y} \, (-dx) = \oint_{\partial D} \left(-\frac{\partial u}{\partial y}\right) dx + \frac{\partial u}{\partial x} \, dy$$

这就变成了第二型曲线积分的形式，可以直接套 Green 公式！

---

## 更几何的理解

在单位圆上逆时针走一小段弧 $ds$：

- 弧的 $x$ 方向投影 $= -y\,ds$（因为切线方向的 $x$ 分量是 $-\sin\theta = -y$）
- 弧的 $y$ 方向投影 $= x\,ds$（因为切线方向的 $y$ 分量是 $\cos\theta = x$）

所以 $dx = -y\,ds$，$dy = x\,ds$，反过来就是 $x\,ds = dy$，$y\,ds = -dx$。

---

## 推广到一般圆

对于半径为 $R$ 的圆 $x^2+y^2=R^2$：

$$x = R\cos\theta, \quad y = R\sin\theta, \quad ds = R\,d\theta$$

$$dx = -R\sin\theta\,d\theta = -y\,d\theta = -\frac{y}{R}\,ds$$

$$dy = R\cos\theta\,d\theta = x\,d\theta = \frac{x}{R}\,ds$$

所以：

$$\boxed{x\,ds = R\,dy, \quad y\,ds = -R\,dx}$$

单位圆是 $R=1$ 的特例。

---

## 一句总结

> **在单位圆上，$x\,ds = dy$ 和 $y\,ds = -dx$ 是参数化 $x=\cos\theta, y=\sin\theta$ 的直接推论。这个技巧把含 $ds$ 的第一型曲线积分瞬间转化为第二型曲线积分，从而可以用 Green 公式。**
