# Gauss 补面法中"散度 → 体积"这一步详解

## 问题回顾（例1-7）

$S$ 为 $y = \sqrt{x}$（$0 \leq x \leq 1$）绕 $x$ 轴旋转所得曲面，取 $x$ 正向侧。

计算：$I = \displaystyle \iint_S 2(1+x)\,dydz + yz\,dxdy$

补 $D: x=1, y^2+z^2 \leq 1$ 构成封闭曲面，Gauss 公式给出：

$$\oiint_{S+D} = \iiint_V (2 + y) \, dV = 2 \cdot \text{Vol}(V) = 2 \cdot \frac{\pi}{2} = \pi$$

要理解的关键是：**散度算出来是 $2+y$，为什么三重积分变成了 $2 \times$ 体积？**

---

## 第一步：Gauss 公式对照

Gauss 公式的标准形式：

$$\oiint P\,dydz + Q\,dzdx + R\,dxdy = \iiint_V \left(P_x + Q_y + R_z\right) dV$$

| 项 | 系数 | 分别对应 |
|----|------|----------|
| $dydz$ | $P = 2(1+x)$ | $\frac{\partial P}{\partial x}$ |
| $dzdx$ | $Q = 0$（原题没有这一项） | $\frac{\partial Q}{\partial y}$ |
| $dxdy$ | $R = yz$ | $\frac{\partial R}{\partial z}$ |

> ⚠️ **易错提醒**：$dxdy$ 前面的系数对应的是 **$R$**，散度中对应的是 **$\frac{\partial R}{\partial z}$**（不是 $\frac{\partial Q}{\partial y}$！）。

---

## 第二步：逐项求散度

$$\frac{\partial P}{\partial x} = \frac{\partial}{\partial x}\big(2+2x\big) = 2$$

$$\frac{\partial Q}{\partial y} = \frac{\partial}{\partial y}(0) = 0$$

$$\frac{\partial R}{\partial z} = \frac{\partial}{\partial z}(yz) = y$$

**散度 $= P_x + Q_y + R_z = 2 + 0 + y = 2 + y$**

> 📝 复习提纲原稿中写的是 "$2+z$"，这里以 $2+y$ 为准。不过因为对称性（见下一步），$y$ 换成 $z$ 也不影响最终答案。

---

## 第三步：利用对称性消去 $y$ 项

区域 $V$ 由 $y^2+z^2 \leq x$（$0 \leq x \leq 1$）定义。这个区域关于 **$Oxz$ 平面**对称——

把 $y$ 换成 $-y$，不等式 $(-y)^2+z^2 \leq x$ 不变，所以区域不变。

$y$ 作为被积函数是**奇函数**：$f(-y) = -y = -f(y)$。

**对称区域上奇函数的积分为零**：

$$\iiint_V y \, dV = 0$$

### 对称性判断方法

| 对称面 | 条件 | 奇函数举例 | 积分为零 |
|--------|------|-----------|:---:|
| $Oyz$（$x=0$） | 区域关于 $x \to -x$ 不变 | $x, x^3, xz$ | ✅ |
| $Oxz$（$y=0$） | 区域关于 $y \to -y$ 不变 | $y, y^3, yz$ | ✅ |
| $Oxy$（$z=0$） | 区域关于 $z \to -z$ 不变 | $z, z^3, xz$ | ✅ |

本题区域 $V$ 对 $y$ 和 $z$ 都是对称的（旋转体），所以 $\iiint_V y\,dV = \iiint_V z\,dV = 0$。

---

## 第四步：余下的 $2$ 项

$$\iiint_V (2 + y) \, dV = \iiint_V 2\,dV + \iiint_V y\,dV = 2\iiint_V dV + 0 = 2 \cdot \text{Vol}(V)$$

---

## 第五步：旋转体体积

$V$ 由 $y = \sqrt{x}$（$0 \leq x \leq 1$）绕 $x$ 轴旋转生成：

$$\text{Vol}(V) = \int_0^1 \pi \cdot (\text{半径})^2 \, dx = \int_0^1 \pi (\sqrt{x})^2 \, dx = \pi \int_0^1 x \, dx = \pi \cdot \frac{1}{2} = \frac{\pi}{2}$$

所以 $2 \cdot \frac{\pi}{2} = \pi$。

---

## 完整推导链

```
                     Gauss 公式
   ∯ (P dydz + Q dzdx + R dxdy)  ──────────→  ∭ (Pₓ + Q_y + R_z) dV
       S+D                                         V
                                                         │
                                                         ▼
                                                  2 + 0 + y = 2 + y
                                                         │
                                         对称性 ──────────┤
                                         y 是奇函数       │
                                                         ▼
                                                  2 + 0 = 2（常数！）
                                                         │
                                                         ▼
                                              2 × Vol(V) = 2 × π/2 = π
```

---

## 一句总结

> **散度 $= P_x + Q_y + R_z$（不是 $P_x + R_y$！），算出散度中的线性项（$y$ 或 $z$）因对称性积分为零，只剩常数项 $2$，再乘体积即得 $\pi$。**
