# $D$ 为平面区域，$L = \partial D$ 的含义与推论

## 直接信息

这个条件告诉我们三件事：

| 信息 | 含义 |
|------|------|
| $D$ 是**平面区域** | $D \subset \mathbb{R}^2$，有面积，通常是有界闭区域 |
| $L$ 是 $D$ 的**边界** | $L$ 是一条**闭合曲线**（区域的边界必然是闭的） |
| $L = \partial D$ | $D$ 和 $L$ 是一一对应的——$L$ 围出 $D$，$D$ 填满 $L$ 内部 |

> 💡 通俗理解：$D$ 是"馅饼"，$L$ 是"饼皮"。给出饼皮就确定了馅饼的范围。

---

## 核心推论

### 1. Green 公式可以直接用

对 $D$ 上任意有一阶连续偏导数的 $P(x,y), Q(x,y)$：

$$\boxed{\oint_L Pdx + Qdy = \iint_D \left(\frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y}\right)dxdy}$$

$L$ 取**正向**（逆时针，使 $D$ 始终在左侧）。

### 2. 面积可以由线积分算

取 $(P,Q) = (0,x)$ 或 $(P,Q) = (-y,0)$ 或 $(P,Q) = \frac{1}{2}(-y,x)$：

$$\boxed{S_D = \oint_L x\,dy = -\oint_L y\,dx = \frac{1}{2}\oint_L (xdy - ydx)}$$

这是 Green 公式最直接的推论——**用绕一圈的线积分得到内部面积**。

### 3. 保守场的判定方法

若在 $D$ 内 $\frac{\partial Q}{\partial x} = \frac{\partial P}{\partial y}$，则对 $D$ 内任意闭曲线 $\Gamma$（完全含于 $D$）：

$$\oint_\Gamma Pdx + Qdy = 0$$

进而**积分与路径无关**。

但这里有个坑——只有当 $D$ 是**单连通**时才能推出积分与路径无关。如果 $D$ 有洞（比如挖去一点），即使旋度处处为零，绕洞一圈的积分也可能非零（见 0.4 题）。

### 4. 边界条件可以消除线积分

如果题中额外给出**在 $L$ 上 $f=0$**（如 0.10 题），则任何含 $f$ 因子的线积分自动为零：

$$\oint_L xf\,dy = 0,\quad \oint_L f\,dx = 0,\quad \oint_L f\frac{\partial g}{\partial n}ds = 0 \text{（不一定，需看具体形式）}$$

这是因为线积分沿 $L$ 进行，而被积函数在 $L$ 上恒为零。

### 5. Green 第一/第二公式

对 $u,v$ 有二阶连续偏导数：

**Green 第一公式**（二维散度定理）：
$$\iint_D (u\Delta v + \nabla u \cdot \nabla v)dxdy = \oint_L u\frac{\partial v}{\partial n}ds$$

**Green 第二公式**（对称形式）：
$$\iint_D (u\Delta v - v\Delta u)dxdy = \oint_L \left(u\frac{\partial v}{\partial n} - v\frac{\partial u}{\partial n}\right)ds$$

---

## 考试中的典型信号

看到题中出现 "$D$ 为平面区域，$L = \partial D$"，立刻想到：

| 信号 | 反应 |
|------|------|
| 边界 $L$ 上 $f=0$ | 线积分为零 → 用 Green 得到积分恒等式 |
| $\partial D$ 或 $\oint_{\partial D}$ | 可直接转成二重积分 |
| 求法向导数积分 $\oint \frac{\partial f}{\partial n}ds$ | Green 第一公式：$= \iint_D \Delta f$ |
| $d = \max_D \sqrt{x^2+y^2}$ | $x^2 \leq d^2$ 放缩（见 0.10 题的不等式证明） |
| 单连通 | 旋度为零 → 保守场 |
| 非单连通（有洞） | 旋度为零 ≠ 保守场，需检查绕洞环量 |

---

## 一句话总结

> **$L = \partial D$ 的本质是把"绕边界的线积分"和"内部区域的面（体）积分"架起了桥梁。这个桥梁就是 Green 公式（以及它衍生的面积公式、Green 第一/第二公式），是整个第 11 章所有计算的基础。**
