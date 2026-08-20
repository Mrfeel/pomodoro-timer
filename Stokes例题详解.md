# Stokes 公式例题完整详解（例1-10）

## 题目

计算 $I = \displaystyle \oint_L (y^2+z^2)dx + (z^2+x^2)dy + (x^2+y^2)dz$，

其中 $L$ 为 $\begin{cases} x^2+y^2+z^2 = 4x \\ x^2+y^2 = 2x, \; z \geq 0 \end{cases}$ 的交线，从 $z$ 轴正向看取逆时针。

---

## 第一步：理解 $L$ 是什么

两个曲面联立：
- $x^2+y^2+z^2 = 4x$ → 配方：$(x-2)^2 + y^2 + z^2 = 4$（球心 $(2,0,0)$，半径 $2$）
- $x^2+y^2 = 2x$ → 配方：$(x-1)^2 + y^2 = 1$（轴线平行于 $z$ 轴的圆柱面，底面是半径为 $1$ 的圆）

两式相减：$z^2 = 2x$，且 $z \geq 0$ → $z = \sqrt{2x}$。

所以 $L$ 是球面被圆柱面截出的"帽子边缘"——空间中的一条闭曲线。

```
        z ↑
          │   ╭――――――╮
          │  ╱  球面   ╲
          │ ╱  (帽子)    ╲
          │╱              ╲
      ────┼──────────────────→ x
          │  圆柱面 (壁)
          │      ┌──┐
          │      └──┘ 底面: (x-1)²+y²=1
```

---

## 第二步：选用哪个曲面？（关键决策）

Stokes 公式需要选一个以 $L$ 为边界的曲面 $S$。有两个候选：

| 候选曲面 | 选它？ | 理由 |
|----------|:---:|------|
| 圆柱面 $x^2+y^2=2x$ 上 $z \geq 0$ 部分 | ❌ | 法向量计算复杂，旋度点乘法向量后表达式繁琐 |
| **球冠**（球面 $x^2+y^2+z^2=4x$ 被圆柱截下的部分） | ✅ | 法向量有漂亮形式，投影计算大大简化 |

> 💡 **选曲面原则**：选法向量最简单、投影面积最好算的那个。球面的梯度正比于 $(x-2, y, z)$，非常简洁。

---

## 第三步：计算旋度

$$\mathbf{F} = (y^2+z^2,\; z^2+x^2,\; x^2+y^2)$$

$$\nabla \times \mathbf{F} = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ \frac{\partial}{\partial x} & \frac{\partial}{\partial y} & \frac{\partial}{\partial z} \\ y^2+z^2 & z^2+x^2 & x^2+y^2 \end{vmatrix}$$

$$= \left(\frac{\partial(x^2+y^2)}{\partial y} - \frac{\partial(z^2+x^2)}{\partial z},\; \frac{\partial(y^2+z^2)}{\partial z} - \frac{\partial(x^2+y^2)}{\partial x},\; \frac{\partial(z^2+x^2)}{\partial x} - \frac{\partial(y^2+z^2)}{\partial y}\right)$$

$$= (2y - 2z,\; 2z - 2x,\; 2x - 2y)$$

---

## 第四步：球面的法向量

球面方程 $F(x,y,z) = x^2+y^2+z^2-4x = 0$。

梯度：$\nabla F = (2x-4, 2y, 2z) = 2(x-2, y, z)$

**有向面积微元**（核心公式）：

$$\mathbf{n}\,dS = \frac{\nabla F}{|\nabla F|} \cdot \frac{|\nabla F|}{|F_z|}\,dxdy = \frac{\nabla F}{|F_z|}\,dxdy$$

$F_z = 2z$，所以：

$$\mathbf{n}\,dS = \frac{2(x-2, y, z)}{2z}\,dxdy = \frac{(x-2, y, z)}{z}\,dxdy$$

根据 $L$ 的方向（从 $z$ 轴正向看逆时针 → 右手定则 → 法向量应指向上方），取外法向量（指离球心）刚好对应 $z>0$ 时 $\mathbf{n}$ 的 $z$ 分量为正。加上一个负号使其满足右手定则：

$$\mathbf{n}\,dS = -\frac{(x-2, y, z)}{z}\,dxdy$$

---

## 第五步：旋度点乘法向量——最精彩的一步

$$\nabla \times \mathbf{F} \cdot \mathbf{n}\,dS = (2y-2z, 2z-2x, 2x-2y) \cdot \left(-\frac{x-2}{z}, -\frac{y}{z}, -1\right) dxdy$$

先算分子：

$$(2y-2z)(-(x-2)) + (2z-2x)(-y) + (2x-2y)(-z)$$

展开：

$$\begin{aligned}
&= -2y(x-2) + 2z(x-2) - 2zy + 2xy - 2xz + 2yz \\
&= -2xy + 4y + 2zx - 4z - 2zy + 2xy - 2xz + 2yz
\end{aligned}$$

同类项抵消：
- $-2xy + 2xy = 0$
- $2zx - 2xz = 0$
- $-2zy + 2yz = 0$

剩下：$4y - 4z = -4(z - y)$

除以 $z$（来自 $dS$ 中的分母）：

$$\nabla \times \mathbf{F} \cdot \mathbf{n}\,dS = -\frac{4(z-y)}{z}\,dxdy = -4\left(1 - \frac{y}{z}\right) dxdy$$

---

## 第六步：对称性消去 $y$ 项

投影区域 $D: (x-1)^2 + y^2 \leq 1$（单位圆盘）。

$z = \sqrt{4x - x^2 - y^2}$（球面的上半部分）。

对于 $D$ 上每一点 $(x,y)$，$\frac{y}{z(x,y)}$ 关于 $y$ 是奇函数：$\frac{-y}{z(x,-y)} = -\frac{y}{z(x,y)}$（因为 $z$ 只依赖于 $y^2$，是偶函数）。

$D$ 关于 $x$ 轴（$y=0$）对称 → $\iint_D \frac{y}{z}\,dxdy = 0$。

$$\iint_S (\nabla \times \mathbf{F}) \cdot \mathbf{n}\,dS = -4\iint_D 1\,dxdy = -4 \cdot \text{Area}(D)$$

$D$ 是半径为 $1$ 的圆 → $\text{Area}(D) = \pi$。

$$I = -4\pi$$

---

## 完整推导流程图

```
                 Stokes 公式
  ∮_L F·dr  ──────────────────→  ∬_S (∇×F)·n dS
                                        │
                                        ▼
                              选球面为 S（法向量简洁）
                                        │
                                        ▼
                              ∇×F = (2y-2z, 2z-2x, 2x-2y)
                              n dS = -(x-2, y, z)/z · dxdy
                                        │
                                        ▼
                          点乘展开 → 大量项相消
                          留下：-4(z-y)/z = -4(1 - y/z)
                                        │
                             对称性 ────┤
                             ∬ y/z = 0  │
                                        ▼
                              -4 ∬ 1 dxdy = -4π
```

---

## 关键技巧总结

| 步骤 | 技巧 |
|------|------|
| 选曲面 | **选球面而非柱面**——球面的法向量 $(x-2, y, z)$ 与旋度 $(2y-2z, 2z-2x, 2x-2y)$ 点乘后大量项恰好相消 |
| 点乘展开 | 耐心展开 3×3=9 项，不要跳步。同类项 $-xy+xy=0$，$xz-xz=0$，$yz-yz=0$ |
| $dS$ 投影 | $\mathbf{n}\,dS = \nabla F / |F_z| \cdot dxdy$，球面的 $F_z = 2z$ |
| 对称性 | $D$ 关于 $x$ 轴对称 + $y/z$ 是 $y$ 的奇函数 → 积分为零 |
| 面积计算 | 圆 $(x-1)^2+y^2 \leq 1$ 的面积 $= \pi \cdot 1^2 = \pi$ |

---

## 一句总结

> **Stokes 公式选曲面有讲究——选法向量"漂亮"的那个。本题选球面（而非柱面）的关键原因是旋度 $(y-z, z-x, x-y)$ 型的分量与球面法向量 $(x-2, y, z)$ 点乘后，交叉项恰好大量对消，只留下简洁的常数项。**
