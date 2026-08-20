# ds 为什么等于 $2d\theta$？

## 问题

计算 $\int_L e^{\sqrt{x^2+y^2}} ds$，$L$ 是圆 $x^2+y^2=4$ 上从 $x$ 轴正半轴逆时针到 $y=x$ 的圆弧。

参数化取 $x = 2\cos\theta, y = 2\sin\theta$，为何 $ds = 2d\theta$？

---

## 解答

这是第一型曲线积分中最基本的计算。弧长微元的公式是：

$$ds = \sqrt{[x'(t)]^2 + [y'(t)]^2} \, dt$$

把 $x = 2\cos\theta, y = 2\sin\theta$ 代入：

$$x'(\theta) = -2\sin\theta$$
$$y'(\theta) = 2\cos\theta$$

于是：

$$ds = \sqrt{(-2\sin\theta)^2 + (2\cos\theta)^2} \, d\theta = \sqrt{4\sin^2\theta + 4\cos^2\theta} \, d\theta$$

$$= \sqrt{4(\sin^2\theta + \cos^2\theta)} \, d\theta = \sqrt{4} \, d\theta = 2d\theta$$

---

## 更直观的理解

参数 $\theta$ 是**弧度**。在半径为 $R$ 的圆上：

- 当角度变化 $d\theta$（弧度）时，弧长变化量 "$=$ 半径 $\times$ 角度变化量" $= R \cdot d\theta$
- 本题 $R = 2$（因为 $x^2+y^2=4$），所以 $ds = 2d\theta$

| 半径 $R$ | 圆的方程 | 参数化 | $ds$ |
|-----------|----------|--------|------|
| 1 | $x^2+y^2=1$ | $x=\cos\theta, y=\sin\theta$ | $ds = 1 \cdot d\theta = d\theta$ |
| 2 | $x^2+y^2=4$ | $x=2\cos\theta, y=2\sin\theta$ | $ds = 2 \cdot d\theta = 2d\theta$ |
| $R$ | $x^2+y^2=R^2$ | $x=R\cos\theta, y=R\sin\theta$ | $ds = R \cdot d\theta$ |

---

## 回到原题

在圆 $x^2+y^2=4$ 上，$\sqrt{x^2+y^2} = \sqrt{4} = 2$（常数！），$ds = 2d\theta$。

$$\int_L e^{\sqrt{x^2+y^2}} ds = \int_0^{\pi/4} e^2 \cdot 2d\theta = 2e^2 \int_0^{\pi/4} d\theta = 2e^2 \cdot \frac{\pi}{4} = \frac{\pi e^2}{2}$$

积分限 $0 \to \pi/4$ 是因为 $y=x$ 对应 $\theta = \pi/4$（即 $45^\circ$），从 $x$ 轴正方向（$\theta=0$）逆时针转过去。

---

## 一句总结

> **圆的参数化中 $ds = R \cdot d\theta$，$R$ 是半径。因为弧长 $=$ 半径 $\times$ 圆心角（弧度制）。**
