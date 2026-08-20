# 电偶极子专题讲义

> **电偶极子是电磁学中最重要的基本模型之一。** 它不仅是理解电介质极化的基础，也是从静电学到电磁辐射的重要桥梁。本节系统梳理电偶极子的所有考点与题型。

\newpage

# 一、基本概念

## 1.1 定义

**电偶极子**：一对等量异号的点电荷 $(+q, -q)$，相距 $l$。当 $l$ 远小于观察距离时，构成一个物理偶极子。

**电偶极矩**（核心物理量）：

$$\boldsymbol{p} = q\,\boldsymbol{l}$$

其中 $\boldsymbol{l}$ 是从 $-q$ 指向 $+q$ 的矢量。$[\boldsymbol{p}] = \text{C}\cdot\text{m}$。

## 1.2 为什么电偶极子如此重要？

1. **电介质的微观模型**：介质分子在电场中被极化 → 每个分子等效为一个感应电偶极子 → $\boldsymbol{P}$（极化强度）= 单位体积内的偶极矩之和
2. **远场展开**：任意中性电荷体系在远处的电场，领头阶就是偶极子场
3. **天线辐射**：振荡的电偶极子是最基本的电磁波辐射源

## 1.3 物理图像

```
         -q ●--------● +q
              l
              ← p 方向 →
```

外电场中：
- **力矩**倾向于使 $\boldsymbol{p}$ 转向与 $\boldsymbol{E}$ 平行（势能最低）
- **力**只在**非均匀**电场中出现，倾向于把偶极子拉向电场更强的区域

\newpage

# 二、核心公式速查

| 物理量 | 公式 | 适用条件 |
|--------|------|---------|
| 电势 | $\varphi = \dfrac{\boldsymbol{p}\cdot\hat{\boldsymbol{r}}}{4\pi\varepsilon_0 r^2}$ | 远场 ($r\gg l$) |
| 电场（一般方向） | $\boldsymbol{E} = \dfrac{3(\boldsymbol{p}\cdot\hat{\boldsymbol{r}})\hat{\boldsymbol{r}}-\boldsymbol{p}}{4\pi\varepsilon_0 r^3}$ | 远场 |
| 电场（轴线上，$\theta=0$） | $E = \dfrac{2p}{4\pi\varepsilon_0 r^3}$ | 沿 $\boldsymbol{p}$ 方向 |
| 电场（中垂面上，$\theta=90^\circ$） | $E = \dfrac{p}{4\pi\varepsilon_0 r^3}$ | 垂直于 $\boldsymbol{p}$ |
| 力矩 | $\boldsymbol{\tau} = \boldsymbol{p}\times\boldsymbol{E}$ | 均匀外场 |
| 势能 | $W = -\boldsymbol{p}\cdot\boldsymbol{E}$ | 均匀外场 |
| 力 | $\boldsymbol{F} = (\boldsymbol{p}\cdot\nabla)\boldsymbol{E}$ | 非均匀外场 |
| 力（分量形式） | $F_x = p_x\frac{\partial E_x}{\partial x} + p_y\frac{\partial E_x}{\partial y} + p_z\frac{\partial E_x}{\partial z}$ | 非均匀外场 |

## 关键比例关系

$$E_{\text{点电荷}} \propto \frac{1}{r^2}, \quad E_{\text{偶极子}} \propto \frac{1}{r^3}, \quad E_{\text{四极子}} \propto \frac{1}{r^4}$$

**记忆**：每增加一个"极"的阶数，场衰减快 $1/r$。

\newpage

# 三、公式推导（必须掌握的推导过程）

## 3.1 电势的远场近似

在 $r \gg l$ 处，取原点在偶极子中心：

$$\varphi(\boldsymbol{r})=\frac{q}{4\pi\varepsilon_0}\left[\frac{1}{|\boldsymbol{r}-\boldsymbol{l}/2|}-\frac{1}{|\boldsymbol{r}+\boldsymbol{l}/2|}\right]$$

对 $l/r$ 做泰勒展开：

$$\frac{1}{|\boldsymbol{r}\pm\boldsymbol{l}/2|} \approx \frac{1}{r}\left(1 \mp \frac{\boldsymbol{r}\cdot\boldsymbol{l}}{2r^2}\right)$$

$$\varphi \approx \frac{q}{4\pi\varepsilon_0 r}\left[\left(1+\frac{\boldsymbol{r}\cdot\boldsymbol{l}}{2r^2}\right) - \left(1-\frac{\boldsymbol{r}\cdot\boldsymbol{l}}{2r^2}\right)\right]$$

$$= \frac{q\,\boldsymbol{l}\cdot\hat{\boldsymbol{r}}}{4\pi\varepsilon_0 r^2} = \frac{\boldsymbol{p}\cdot\hat{\boldsymbol{r}}}{4\pi\varepsilon_0 r^2}$$

**推导要点**：分母展开保留到 $l/r$ 的一阶，分子中 $q$ 和 $\pm\boldsymbol{l}/2$ 的乘积给出偶极矩。

## 3.2 从电势到电场

$$\boldsymbol{E} = -\nabla\varphi = -\nabla\left(\frac{\boldsymbol{p}\cdot\hat{\boldsymbol{r}}}{4\pi\varepsilon_0 r^2}\right)$$

在球坐标中 $(\boldsymbol{p}$ 沿 $z$ 轴，$\boldsymbol{p}\cdot\hat{\boldsymbol{r}}=p\cos\theta)$：

$$E_r = -\frac{\partial\varphi}{\partial r} = \frac{2p\cos\theta}{4\pi\varepsilon_0 r^3}$$

$$E_\theta = -\frac{1}{r}\frac{\partial\varphi}{\partial\theta} = \frac{p\sin\theta}{4\pi\varepsilon_0 r^3}$$

写回矢量形式即得一般公式。

\newpage

# 四、四大题型分类详解

## 题型一：求偶极子的电势和电场分布

**典型问法**：已知 $\boldsymbol{p}$，求空间任意点的 $\varphi$ 和 $\boldsymbol{E}$。

**解题路径**：
1. 写出 $\varphi = \boldsymbol{p}\cdot\hat{\boldsymbol{r}}/(4\pi\varepsilon_0 r^2)$
2. 用 $\boldsymbol{E}=-\nabla\varphi$ 或直接用矢量公式求 $\boldsymbol{E}$

**例题1**：一电偶极子 $\boldsymbol{p}=p\hat{\boldsymbol{z}}$ 位于原点。求：
(1) $z$ 轴上各点的 $\varphi$ 和 $\boldsymbol{E}$；
(2) $x$ 轴上各点的 $\varphi$ 和 $\boldsymbol{E}$。

**解**：
(1) $z$ 轴上 $\hat{\boldsymbol{r}}=\hat{\boldsymbol{z}}$，$\boldsymbol{p}\cdot\hat{\boldsymbol{r}}=p$

$$\varphi(z)=\frac{p}{4\pi\varepsilon_0 z^2},\quad \boldsymbol{E}(z)=\frac{2p}{4\pi\varepsilon_0 z^3}\hat{\boldsymbol{z}}$$

(2) $x$ 轴上 $\hat{\boldsymbol{r}}=\hat{\boldsymbol{x}}$，$\boldsymbol{p}\cdot\hat{\boldsymbol{r}}=0$

$$\varphi(x)=0,\quad \boldsymbol{E}(x)=-\frac{p}{4\pi\varepsilon_0 x^3}\hat{\boldsymbol{z}}$$

**注意**：轴线上 $E=2p/(4\pi\varepsilon_0 r^3)$，中垂面上 $E=p/(4\pi\varepsilon_0 r^3)$，两者差2倍！这是偶极子场的标志性特征。

---

## 题型二：偶极子在均匀外电场中（力矩与势能）

**典型问法**：偶极子 $\boldsymbol{p}$ 放在均匀外场 $\boldsymbol{E}_0$ 中，求力矩和势能，讨论平衡。

**核心公式**：
$$\boldsymbol{\tau} = \boldsymbol{p}\times\boldsymbol{E}_0 \quad \text{（力矩）}$$
$$W = -\boldsymbol{p}\cdot\boldsymbol{E}_0 \quad \text{（势能）}$$

**例题2**：电偶极子 $\boldsymbol{p}$ 与均匀电场 $\boldsymbol{E}_0$ 夹角为 $\theta$。
(1) 求力矩大小和方向；
(2) 找出平衡位置并判断稳定性。

**解**：
(1) $\tau = pE_0\sin\theta$，方向由 $\boldsymbol{p}\times\boldsymbol{E}_0$（右手定则）→ 倾向于使 $\boldsymbol{p}$ 转向 $\boldsymbol{E}_0$。

(2) 平衡条件 $\tau=0$ → $\theta=0$ 或 $\theta=\pi$：
- $\theta=0$（$\boldsymbol{p}\parallel\boldsymbol{E}_0$）：$W=-pE_0$ 最小 → **稳定平衡**
- $\theta=\pi$（$\boldsymbol{p}\uparrow\downarrow\boldsymbol{E}_0$）：$W=+pE_0$ 最大 → **不稳定平衡**

---

## 题型三：偶极子在非均匀外电场中（受力）

**典型问法**：偶极子在点电荷的电场中、在另一偶极子的电场中所受的力。

**核心公式**：
$$\boldsymbol{F} = (\boldsymbol{p}\cdot\nabla)\boldsymbol{E} = \nabla(\boldsymbol{p}\cdot\boldsymbol{E})$$

**例题3**：电偶极子 $\boldsymbol{p}=p\hat{\boldsymbol{z}}$ 放在点电荷 $Q$ 的电场中，偶极子与 $Q$ 相距 $r$，$\boldsymbol{p}$ 沿径向（指向 $Q$）。求偶极子所受的力。

**解**：$Q$ 的电场 $\boldsymbol{E} = \dfrac{Q}{4\pi\varepsilon_0 r^2}\hat{\boldsymbol{r}}$。由 $\boldsymbol{F}=(\boldsymbol{p}\cdot\nabla)\boldsymbol{E}$：

沿径向 $\boldsymbol{p}=p\hat{\boldsymbol{r}}$，则：

$$\boldsymbol{F} = p\frac{\partial}{\partial r}\left(\frac{Q}{4\pi\varepsilon_0 r^2}\right)\hat{\boldsymbol{r}} = -\frac{2pQ}{4\pi\varepsilon_0 r^3}\hat{\boldsymbol{r}}$$

**负号表示吸引力**——偶极子被拉向点电荷。物理原因：$+q$ 端比 $-q$ 端离 $Q$ 更近（或更远），电场不均匀导致净力。

**例题4**（高频考题）：两电偶极子 $\boldsymbol{p}_1$ 和 $\boldsymbol{p}_2$ 相距 $r$（均沿连线方向）。求 $\boldsymbol{p}_2$ 对 $\boldsymbol{p}_1$ 的力。

**解**：$\boldsymbol{p}_1$ 在 $\boldsymbol{p}_2$ 的电场中。$\boldsymbol{p}_2$ 沿连线方向的电场为 $E = \dfrac{2p_2}{4\pi\varepsilon_0 r^3}$。

$$\boldsymbol{F} = (\boldsymbol{p}_1\cdot\nabla)\boldsymbol{E} = p_1\frac{\partial}{\partial r}\left(\frac{2p_2}{4\pi\varepsilon_0 r^3}\right)\hat{\boldsymbol{r}} = -\frac{6p_1 p_2}{4\pi\varepsilon_0 r^4}\hat{\boldsymbol{r}}$$

偶极子-偶极子力 $\propto 1/r^4$（比点电荷-点电荷力 $\propto 1/r^2$ 衰减快得多）。

---

## 题型四：电偶极子与介质的联系

**典型问法**：解释电介质的极化机制；已知极化强度求极化电荷分布。

**核心联系**：
- $\boldsymbol{P}$（极化强度）= 单位体积内的总电偶极矩 = $n\langle\boldsymbol{p}\rangle$
- 均匀极化的球体 → 球内 $\boldsymbol{E}$ 均匀（重要结论！）
- 极化电荷 $\sigma'=\boldsymbol{P}\cdot\hat{\boldsymbol{n}}$，$\rho'=-\nabla\cdot\boldsymbol{P}$

**例题5**：均匀极化的电介质球（半径 $R$，极化强度 $\boldsymbol{P}=P_0\hat{\boldsymbol{z}}$）。求球内外的电场。

**解**：
(1) 极化电荷面密度 $\sigma' = \boldsymbol{P}\cdot\hat{\boldsymbol{n}} = P_0\cos\theta$。

(2) 面电荷分布 $\sigma_0\cos\theta$ 在球内产生的电场是均匀的：

$$\boldsymbol{E}_{\text{in}}' = -\frac{\boldsymbol{P}}{3\varepsilon_0}$$

(3) 球外电场等效于中心处 $\boldsymbol{p} = \frac{4\pi}{3}R^3\boldsymbol{P}$ 的偶极子场。

**此结论的推论**：将均匀极化球放入均匀外场 $\boldsymbol{E}_0$，总电场 $\boldsymbol{E}_{\text{in}}=\boldsymbol{E}_0-\boldsymbol{P}/(3\varepsilon_0)$，结合 $\boldsymbol{P}=\chi_e\varepsilon_0\boldsymbol{E}_{\text{in}}$ 可求球内实际场。

\newpage

# 五、易错点与考试技巧

## 易错点

| 易错 | 正确 |
|------|------|
| 偶极子场 $\propto 1/r^3$ 但经常写成 $1/r^2$ | 记忆：点电荷 $1/r^2$，偶极子 $1/r^3$（多一极，快一倍） |
| 轴线上 $E=2p/(4\pi\varepsilon_0 r^3)$ 和中垂面上 $E=p/(4\pi\varepsilon_0 r^3)$ 搞混 | 轴线=2倍中垂面——中间有"**2**"倍就是"**轴**"（谐音记法） |
| $\boldsymbol{F}=(\boldsymbol{p}\cdot\nabla)\boldsymbol{E}$ 与 $\boldsymbol{F}=q\boldsymbol{E}$ 混淆 | $q\boldsymbol{E}$ 是点电荷的力；$(\boldsymbol{p}\cdot\nabla)\boldsymbol{E}$ 是偶极子的力 |
| 平衡位置稳定性判断反了 | $\boldsymbol{p}\parallel\boldsymbol{E}$ 势能最低=稳定；$\boldsymbol{p}\uparrow\downarrow\boldsymbol{E}$ 势能最高=不稳定 |

## 考试技巧

1. **看到"远场"或"r≫尺寸"**→立刻想到偶极子近似 $\varphi\propto 1/r^2$，$E\propto 1/r^3$
2. **看到电介质+求内部场**→联想到极化=偶极子模型，均匀极化球内 $\boldsymbol{E}'=-\boldsymbol{P}/(3\varepsilon_0)$
3. **求偶极子受的力**→先写出外场 $\boldsymbol{E}(\boldsymbol{r})$，再用 $\boldsymbol{F}=(\boldsymbol{p}\cdot\nabla)\boldsymbol{E}$
4. **验证方向**→偶极子被拉向强场区：正端受力 $q\boldsymbol{E}_+$，负端受力 $-q\boldsymbol{E}_-$，$\boldsymbol{E}_+\neq\boldsymbol{E}_-$ 时出现净力

\newpage

# 六、自测题

**T1**（基础计算）：一电偶极子 $\boldsymbol{p}=p\hat{\boldsymbol{z}}$ 位于原点。求点 $(x,0,z)$ 处的电势，并由此求该点的电场强度 $E_z$ 分量。

**T2**（力矩与平衡）：两电偶极子 $\boldsymbol{p}_1$ 和 $\boldsymbol{p}_2$ 分别固定在 $z$ 轴上 $z=0$ 和 $z=d$ 处，$\boldsymbol{p}_1$ 方向固定沿 $z$ 轴，$\boldsymbol{p}_2$ 可自由转动。求 $\boldsymbol{p}_2$ 的平衡方向，并判断稳定性。

**T3**（受力计算）：电偶极子 $\boldsymbol{p}$ 放在无限长均匀带电直线（线密度 $\lambda$）附近，$\boldsymbol{p}$ 沿径向。求偶极子所受的力。

**T4**（极化应用）：均匀极化球的极化强度为 $\boldsymbol{P}$。证明：球内退极化场 $\boldsymbol{E}' = -\boldsymbol{P}/(3\varepsilon_0)$。由此推导将一个电介质球（$\varepsilon_r$）放入均匀外场 $\boldsymbol{E}_0$ 中时，球内总电场为 $\boldsymbol{E}_{\text{in}} = \dfrac{3}{\varepsilon_r+2}\boldsymbol{E}_0$。

**T5**（综合）：一电偶极子 $\boldsymbol{p}$ 位于接地无限大导体平面前方 $d$ 处，方向垂直于平面。用镜像法求导体对偶极子的吸引力。
