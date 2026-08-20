# Jacobian 行列式的计算方法

## 它是什么？

做变量替换 $(x,y) \to (u,v)$ 时，面积微元的转换：

$$dxdy = |J| \, dudv, \quad J = \frac{\partial(x,y)}{\partial(u,v)}$$

**$|J|$ 就是"新坐标下一个单位正方形对应原坐标下的面积放大倍数"。**

---

## 二维 Jacobian

变量替换 $\begin{cases} x = x(u,v) \\ y = y(u,v) \end{cases}$：

$$J = \frac{\partial(x,y)}{\partial(u,v)} = \begin{vmatrix} \dfrac{\partial x}{\partial u} & \dfrac{\partial x}{\partial v} \\[8pt] \dfrac{\partial y}{\partial u} & \dfrac{\partial y}{\partial v} \end{vmatrix} = \frac{\partial x}{\partial u} \cdot \frac{\partial y}{\partial v} - \frac{\partial x}{\partial v} \cdot \frac{\partial y}{\partial u}$$

**二阶行列式口诀**：左上 × 右下 $-$ 右上 × 左下。

---

## 三维 Jacobian

变量替换 $\begin{cases} x = x(u,v,w) \\ y = y(u,v,w) \\ z = z(u,v,w) \end{cases}$：

$$J = \frac{\partial(x,y,z)}{\partial(u,v,w)} = \begin{vmatrix} \dfrac{\partial x}{\partial u} & \dfrac{\partial x}{\partial v} & \dfrac{\partial x}{\partial w} \\[8pt] \dfrac{\partial y}{\partial u} & \dfrac{\partial y}{\partial v} & \dfrac{\partial y}{\partial w} \\[8pt] \dfrac{\partial z}{\partial u} & \dfrac{\partial z}{\partial v} & \dfrac{\partial z}{\partial w} \end{vmatrix}$$

$$dV = |J| \, du dv dw$$

**三阶行列式展开**（按第一行）：

$$\begin{vmatrix} a & b & c \\ d & e & f \\ g & h & i \end{vmatrix} = a\begin{vmatrix} e & f \\ h & i \end{vmatrix} - b\begin{vmatrix} d & f \\ g & i \end{vmatrix} + c\begin{vmatrix} d & e \\ g & h \end{vmatrix}$$

$$= a(ei-fh) - b(di-fg) + c(dh-eg)$$

---

## 考试中最重要的三个 Jacobian

### 1. 极坐标（$r, \theta$）

$$\begin{cases} x = r\cos\theta \\ y = r\sin\theta \end{cases}$$

$$J = \begin{vmatrix} \dfrac{\partial x}{\partial r} & \dfrac{\partial x}{\partial \theta} \\[8pt] \dfrac{\partial y}{\partial r} & \dfrac{\partial y}{\partial \theta} \end{vmatrix} = \begin{vmatrix} \cos\theta & -r\sin\theta \\ \sin\theta & r\cos\theta \end{vmatrix}$$

$$= \cos\theta \cdot r\cos\theta - (-r\sin\theta) \cdot \sin\theta = r(\cos^2\theta + \sin^2\theta) = r$$

$$\boxed{dxdy = r \, dr d\theta}$$

### 2. 柱坐标（$r, \theta, z$）

$$\begin{cases} x = r\cos\theta \\ y = r\sin\theta \\ z = z \end{cases}$$

$$J = \begin{vmatrix} \cos\theta & -r\sin\theta & 0 \\ \sin\theta & r\cos\theta & 0 \\ 0 & 0 & 1 \end{vmatrix} = 1 \cdot \begin{vmatrix} \cos\theta & -r\sin\theta \\ \sin\theta & r\cos\theta \end{vmatrix} = r$$

$$\boxed{dV = r \, dr d\theta dz}$$

> 💡 柱坐标就是极坐标 $+z$，$z$ 不变，$J$ 同样是 $r$。

### 3. 球坐标（$\rho, \varphi, \theta$）

$$\begin{cases} x = \rho\sin\varphi\cos\theta \\ y = \rho\sin\varphi\sin\theta \\ z = \rho\cos\varphi \end{cases}$$

$$\frac{\partial(x,y,z)}{\partial(\rho,\varphi,\theta)} = \begin{vmatrix} \sin\varphi\cos\theta & \rho\cos\varphi\cos\theta & -\rho\sin\varphi\sin\theta \\ \sin\varphi\sin\theta & \rho\cos\varphi\sin\theta & \rho\sin\varphi\cos\theta \\ \cos\varphi & -\rho\sin\varphi & 0 \end{vmatrix}$$

按第三行展开最方便（因为有两个零不好，实际上按第三行展开）：

$$= \cos\varphi \cdot \begin{vmatrix} \rho\cos\varphi\cos\theta & -\rho\sin\varphi\sin\theta \\ \rho\cos\varphi\sin\theta & \rho\sin\varphi\cos\theta \end{vmatrix} - (-\rho\sin\varphi) \cdot \begin{vmatrix} \sin\varphi\cos\theta & -\rho\sin\varphi\sin\theta \\ \sin\varphi\sin\theta & \rho\sin\varphi\cos\theta \end{vmatrix} + 0$$

第一项二阶行列式：
$$= \rho^2\sin\varphi\cos\varphi(\cos^2\theta + \sin^2\theta) = \rho^2\sin\varphi\cos\varphi$$

第二项二阶行列式：
$$= \rho\sin^2\varphi(\cos^2\theta + \sin^2\theta) = \rho\sin^2\varphi$$

代入：
$$J = \cos\varphi \cdot \rho^2\sin\varphi\cos\varphi + \rho\sin\varphi \cdot \rho\sin^2\varphi = \rho^2\sin\varphi(\cos^2\varphi + \sin^2\varphi) = \rho^2\sin\varphi$$

$$\boxed{dV = \rho^2\sin\varphi \, d\rho d\varphi d\theta}$$

> 💡 这个推导考试不需要重现，但必须记住结果。

---

## 实际计算示例

### 例：验证极坐标 Jacobian

$$\begin{cases} x = 2r\cos\theta \\ y = 3r\sin\theta \end{cases}$$

（椭圆坐标）

$$J = \begin{vmatrix} 2\cos\theta & -2r\sin\theta \\ 3\sin\theta & 3r\cos\theta \end{vmatrix} = 2\cos\theta \cdot 3r\cos\theta - (-2r\sin\theta) \cdot 3\sin\theta$$

$$= 6r\cos^2\theta + 6r\sin^2\theta = 6r$$

$$dxdy = 6r \, dr d\theta$$

---

## 逆变换公式

$$\frac{\partial(x,y)}{\partial(u,v)} \cdot \frac{\partial(u,v)}{\partial(x,y)} = 1$$

即 $J_{x,y \to u,v} = \dfrac{1}{J_{u,v \to x,y}}$。

**例**：$u = x+y, v = x-y$

正向 Jacobian：$\frac{\partial(u,v)}{\partial(x,y)} = \begin{vmatrix} 1 & 1 \\ 1 & -1 \end{vmatrix} = -2$

反向 Jacobian：$\frac{\partial(x,y)}{\partial(u,v)} = \dfrac{1}{-2} = -\dfrac{1}{2}$，$|J| = \dfrac{1}{2}$

$$dxdy = \frac{1}{2} \, dudv$$

---

## 考试速记表

| 坐标 | 新变量 | $|J|$ | $dxdy$ 或 $dV$ |
|------|--------|------|-----------------|
| 极坐标 | $r, \theta$ | $r$ | $dxdy = r\,drd\theta$ |
| 柱坐标 | $r, \theta, z$ | $r$ | $dV = r\,drd\theta dz$ |
| 球坐标 | $\rho, \varphi, \theta$ | $\rho^2\sin\varphi$ | $dV = \rho^2\sin\varphi\,d\rho d\varphi d\theta$ |
| 线性变换 | $u=ax+by, v=cx+dy$ | $|ad-bc|$ | $dxdy = \frac{1}{|ad-bc|}dudv$ |

---

## 一句总结

> **Jacobian 行列式 = 新坐标偏导数排成矩阵的行列式。二级行列式用"左上×右下 − 右上×左下"；三级行列式按一行展开。考试只需记住极坐标 $r$、柱坐标 $r$、球坐标 $\rho^2\sin\varphi$ 这三个结果。**
