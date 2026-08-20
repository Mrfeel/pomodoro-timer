# 电磁学复习提纲 — 自测题参考答案

> 对应《电磁学期末考试复习提纲》中全部48道章节自测题 + 5道综合模拟题的详细解答。

\newpage
# 第一章  真空中的静电场（5题）

## T1-1 无限长均匀带电圆柱体的电场

**解**：柱对称，电场沿径向。取半径为 $r$、高为 $l$ 的同轴圆柱高斯面。

侧面：$\oint\boldsymbol{E}\cdot d\boldsymbol{S}=E(r)\cdot 2\pi r l$；端面通量 $=0$。

$r<R$（柱内）：$Q_{\text{enc}}=\rho\cdot\pi r^2 l$
$$E\cdot 2\pi r l = \frac{\rho\pi r^2 l}{\varepsilon_0} \Rightarrow E=\frac{\rho r}{2\varepsilon_0}$$

$r>R$（柱外）：$Q_{\text{enc}}=\rho\cdot\pi R^2 l$
$$E\cdot 2\pi r l = \frac{\rho\pi R^2 l}{\varepsilon_0} \Rightarrow E=\frac{\rho R^2}{2\varepsilon_0 r}$$

**答案**：柱内 $E=\rho r/(2\varepsilon_0)$，柱外 $E=\rho R^2/(2\varepsilon_0 r)$

---

## T1-2 均匀带电半圆环圆心的电场

**解**：对称性→圆心处电场只有 $y$ 分量（$x$ 分量对称抵消）。

电荷元 $dq=\lambda R\,d\theta$，在圆心产生的电场：
$$dE = \frac{\lambda R\,d\theta}{4\pi\varepsilon_0 R^2} = \frac{\lambda\,d\theta}{4\pi\varepsilon_0 R}$$

$dE_y = dE\sin\theta$（只有 $y$ 分量，半圆环 $\theta$ 从 $0$ 到 $\pi$）：
$$E = E_y = \int_0^\pi \frac{\lambda\sin\theta}{4\pi\varepsilon_0 R}\,d\theta = \frac{\lambda}{4\pi\varepsilon_0 R}[-\cos\theta]_0^\pi = \frac{\lambda}{2\pi\varepsilon_0 R}$$

**答案**：$E = \dfrac{\lambda}{2\pi\varepsilon_0 R}$，方向沿对称轴（垂直于直径向下）。

---

## T1-3 均匀带电圆盘轴线上任意点的电势和电场

**解**：面电荷密度 $\sigma$，半径 $R$。轴线上距盘心 $z$ 处：

取半径 $r\to r+dr$ 的圆环，电荷 $dq=\sigma\cdot 2\pi r\,dr$，到该点距离 $\sqrt{r^2+z^2}$。

$$\varphi(z)=\int_0^R\frac{\sigma\cdot 2\pi r\,dr}{4\pi\varepsilon_0\sqrt{r^2+z^2}}=\frac{\sigma}{2\varepsilon_0}\left[\sqrt{R^2+z^2}-|z|\right]$$

由对称性 $\boldsymbol{E}$ 沿轴向：$E_z=-\partial\varphi/\partial z$
$$E(z)=\frac{\sigma}{2\varepsilon_0}\left[1-\frac{z}{\sqrt{R^2+z^2}}\right]\hat{\boldsymbol{z}}$$

$z>0$ 时向上；$z<0$ 时向下。$R\to\infty$ 时 $E\to\sigma/(2\varepsilon_0)$（无限大平面结果）。

---

## T1-4 带电球体内的球形空腔（补偿法）

**解**：大球（半径 $R$，密度 $\rho$）+ 小球（半径 $r_0$，密度 $-\rho$）叠加。

大球在腔内某点 $\boldsymbol{r}$ 的电场：$\boldsymbol{E}_1 = \dfrac{\rho}{3\varepsilon_0}\boldsymbol{r}$（均匀带电球内公式）

补球（负密度 $-\rho$）在同一点的电场：$\boldsymbol{E}_2 = -\dfrac{\rho}{3\varepsilon_0}(\boldsymbol{r}-\boldsymbol{a})$

叠加：$\boldsymbol{E}=\boldsymbol{E}_1+\boldsymbol{E}_2=\dfrac{\rho}{3\varepsilon_0}\boldsymbol{r}-\dfrac{\rho}{3\varepsilon_0}(\boldsymbol{r}-\boldsymbol{a})=\dfrac{\rho}{3\varepsilon_0}\boldsymbol{a}$

**结论**：空腔内为**匀强电场**，大小 $\rho a/(3\varepsilon_0)$，方向平行于 $\boldsymbol{a}$（从原球心指向空腔球心）。

---

## T1-5 电偶极子在点电荷电场中的力和力矩

**解**：$Q$ 在偶极子处的电场 $\boldsymbol{E}=\dfrac{Q}{4\pi\varepsilon_0 r^2}\hat{\boldsymbol{r}}$。设 $\boldsymbol{p}$ 与 $\hat{\boldsymbol{r}}$ 夹角为 $\theta$。

力矩：$\boldsymbol{\tau}=\boldsymbol{p}\times\boldsymbol{E}$，大小 $\tau=\dfrac{pQ\sin\theta}{4\pi\varepsilon_0 r^2}$

力：$\boldsymbol{F}=(\boldsymbol{p}\cdot\nabla)\boldsymbol{E}$。若 $\boldsymbol{p}\parallel\hat{\boldsymbol{r}}$：
$$\boldsymbol{F}=p\frac{\partial}{\partial r}\left(\frac{Q}{4\pi\varepsilon_0 r^2}\right)\hat{\boldsymbol{r}}=-\frac{2pQ}{4\pi\varepsilon_0 r^3}\hat{\boldsymbol{r}}$$

**答案**：力矩 $\tau=pQ\sin\theta/(4\pi\varepsilon_0 r^2)$；$\boldsymbol{p}\parallel\hat{\boldsymbol{r}}$ 时力 $\boldsymbol{F}=-2pQ\hat{\boldsymbol{r}}/(4\pi\varepsilon_0 r^3)$（吸引力）。

\newpage
# 第二章  静电场中的导体和电介质（6题）

## T2-1 平行板电容器插入介质板

**解**：原电容 $C_0=\varepsilon_0 S/d$。插入厚 $t$、$\varepsilon_r$ 的介质板。
等效为两真空间隙（总厚 $d-t$）与介质板（厚 $t$，$\varepsilon_r$）串联：
$$\frac{1}{C}=\frac{d-t}{\varepsilon_0 S}+\frac{t}{\varepsilon_0\varepsilon_r S} \Rightarrow C=\frac{\varepsilon_0 S}{d-t+t/\varepsilon_r}$$
极限1（介质充满 $t=d$）：$C=\varepsilon_r\cdot\varepsilon_0 S/d=\varepsilon_r C_0$（增大 $\varepsilon_r$ 倍）
极限2（介质紧贴一极板 $t<d$）：仍用上述串联公式。

---

## T2-2 球形电容器含两种同心介质

**解**：内导体半径 $a$，外导体半径 $b$，分界面半径 $d$（$a<d<b$），两介质 $\varepsilon_1,\varepsilon_2$。
设内导体带 $Q$，$D=Q/(4\pi r^2)$（球对称，$D$ 连续）。
$a<r<d$：$E_1=Q/(4\pi\varepsilon_1 r^2)$；$d<r<b$：$E_2=Q/(4\pi\varepsilon_2 r^2)$
$$U=\int_a^d E_1\,dr+\int_d^b E_2\,dr=\frac{Q}{4\pi}\left[\frac{1}{\varepsilon_1}\left(\frac{1}{a}-\frac{1}{d}\right)+\frac{1}{\varepsilon_2}\left(\frac{1}{d}-\frac{1}{b}\right)\right]$$
$$C=\frac{Q}{U}=4\pi\left[\frac{1}{\varepsilon_1}\left(\frac{1}{a}-\frac{1}{d}\right)+\frac{1}{\varepsilon_2}\left(\frac{1}{d}-\frac{1}{b}\right)\right]^{-1}$$
分界面极化电荷：$\sigma'_d=\boldsymbol{P}_1\cdot\hat{\boldsymbol{n}}-\boldsymbol{P}_2\cdot\hat{\boldsymbol{n}}$（两面极化电荷之差）。

---

## T2-3 双层介质的平行板电容器

**解**：$D$ 法向连续→两层介质中 $D$ 相同：$D_1=D_2=D$。
$E_1=D/\varepsilon_1$，$E_2=D/\varepsilon_2$。$U=E_1 d_1+E_2 d_2=D(d_1/\varepsilon_1+d_2/\varepsilon_2)$。
$$D=\frac{U}{d_1/\varepsilon_1+d_2/\varepsilon_2},\quad E_1=\frac{D}{\varepsilon_1},\quad E_2=\frac{D}{\varepsilon_2}$$
**关键**：$D$ 在两层中相同，但 $E$ 不同——$E$ 在 $\varepsilon_r$ 大的层中更小。

---

## T2-4 镜像法—接地导体平面

**解**：镜像电荷 $-q$ 位于对称位置（平面下方 $d$ 处）。
导体表面（$z=0$ 平面）电场：$E_z=-\dfrac{2qd}{4\pi\varepsilon_0(r^2+d^2)^{3/2}}$
面电荷密度：$\sigma=\varepsilon_0 E_z=-\dfrac{qd}{2\pi(r^2+d^2)^{3/2}}$
总感应电荷：$Q_{\text{ind}}=\int_0^\infty\sigma\cdot 2\pi r\,dr=-q$（等于镜像电荷）。

---

## T2-5 镜像法—接地导体球

**解**：镜像电荷 $q'=-\dfrac{R}{d}q$，位于球心到真实电荷连线上距球心 $r'=\dfrac{R^2}{d}$ 处。
点电荷受力=与镜像电荷的库仑力：
$$F=\frac{qq'}{4\pi\varepsilon_0(d-r')^2}=-\frac{q^2 Rd}{4\pi\varepsilon_0(d^2-R^2)^2}$$
负号表示吸引力（点电荷被拉向导体球）。
**注意**：$d\to R$ 时 $F\to\infty$——导体尖端效应。$d\gg R$ 时 $F\propto 1/d^3$。

---

## T2-6 导体球+同心介质球壳（综合）

**解**：$r<a$（导体内部）：$\boldsymbol{D}=0,\boldsymbol{E}=0$
$a<r<b$（介质壳中）：$D=Q/(4\pi r^2),\;E=Q/(4\pi\varepsilon_0\varepsilon_r r^2),\;P=(\varepsilon_r-1)Q/(4\pi\varepsilon_r r^2)$
$r>b$（真空中）：$D=Q/(4\pi r^2),\;E=Q/(4\pi\varepsilon_0 r^2),\;P=0$
介质壳内表面（$r=a$）：$\sigma'_a=-\boldsymbol{P}\cdot\hat{\boldsymbol{r}}=-(\varepsilon_r-1)Q/(4\pi\varepsilon_r a^2)$（负极化电荷）
介质壳外表面（$r=b$）：$\sigma'_b=\boldsymbol{P}\cdot\hat{\boldsymbol{r}}=(\varepsilon_r-1)Q/(4\pi\varepsilon_r b^2)$（正极化电荷）
系统电容：$C=4\pi\varepsilon_0\left[\frac{1}{\varepsilon_r}\left(\frac{1}{a}-\frac{1}{b}\right)+\frac{1}{b}\right]^{-1}$

\newpage
# 第三章  静电能（4题）

## T3-1 均匀带电球面的静电自能

**解**：$W=\frac{1}{2}\int\sigma\varphi\,dS=\frac{1}{2}Q\cdot\frac{Q}{4\pi\varepsilon_0 R}=\frac{Q^2}{8\pi\varepsilon_0 R}$
令此静电自能等于电子静能 $m_e c^2$：
$$\frac{e^2}{8\pi\varepsilon_0 r_e}=m_e c^2 \Rightarrow r_e=\frac{e^2}{8\pi\varepsilon_0 m_e c^2}\approx 1.4\times 10^{-15}\,\text{m}$$
若电荷均匀分布在球体内，结果略有不同：$r_e=3e^2/(20\pi\varepsilon_0 m_e c^2)\approx 2.8\times 10^{-15}\,\text{m}$（即所谓"电子经典半径"）。

---

## T3-2 拉开平行板电容器（接电源）

**解**：电容 $C=\varepsilon_0 S/d$。接电源→$U$ 恒定。
(1) 电场力 $F=+\partial W/\partial d|_U$。$W=\frac{1}{2}CU^2=\varepsilon_0 SU^2/(2d)$。
$F=\partial/\partial d[\varepsilon_0 SU^2/(2d)]=-\varepsilon_0 SU^2/(2d^2)$。电场力做的功 $A_F=\int_{d_1}^{d_2}F\,dd=\frac{\varepsilon_0 SU^2}{2}(\frac{1}{d_1}-\frac{1}{d_2})$。
(2) 电源供能 $\Delta W_{\text{电源}}=\int U\,dQ=U\Delta Q=U^2(C_2-C_1)=\varepsilon_0 SU^2(\frac{1}{d_2}-\frac{1}{d_1})$（注意符号：间距增大→电容减小→电荷回流→电源吸收能量）。
(3) 电场能变化 $\Delta W_e=\frac{1}{2}U^2(C_2-C_1)=\frac{1}{2}\varepsilon_0 SU^2(\frac{1}{d_2}-\frac{1}{d_1})$
**关系**：$A_F+\Delta W_{\text{电源}}+\Delta W_e=0$（能量守恒）。

---

## T3-3 平行板电容器吸引力（虚功原理）

**解**：$C=\varepsilon_0 S/x$。
$Q$=const：$W=Q^2/(2C)=Q^2 x/(2\varepsilon_0 S)$，$F=-\partial W/\partial x|_Q=-Q^2/(2\varepsilon_0 S)=-\varepsilon_0 SU^2/(2x^2)$
$U$=const：$W=\frac{1}{2}CU^2=\varepsilon_0 SU^2/(2x)$，$F=+\partial W/\partial x|_U=-\varepsilon_0 SU^2/(2x^2)$
**两种条件结果相同**（负号表示吸引力，力的大小为 $\varepsilon_0 SU^2/(2x^2)$）。

---

## T3-4 介质板拉入电容器所需的力

**解**：设介质板插入深度为 $x$（宽 $b$，板间距 $d$）。电容=介质部分+真空部分的并联：
$$C(x)=\frac{\varepsilon_0\varepsilon_r bx}{d}+\frac{\varepsilon_0 b(a-x)}{d}=\frac{\varepsilon_0 b}{d}[a+(\varepsilon_r-1)x]$$
接电源（$U$=const）：$W=\frac{1}{2}CU^2$
$$F=+\frac{\partial W}{\partial x}\bigg|_U=\frac{\varepsilon_0 b(\varepsilon_r-1)U^2}{2d}$$
力沿 $+x$ 方向（将介质板拉入电容器内部）。

\newpage
# 第四章  稳恒电流（3题）

## T4-1 同轴电缆漏电阻

**解**：$r$ 处电流密度 $j=I/(2\pi r l)$（径向漏电）。$E=j/\sigma=I/(2\pi\sigma r l)$。
$$U=\int_a^b E\,dr=\frac{I}{2\pi\sigma l}\ln\frac{b}{a} \Rightarrow R=\frac{U}{I}=\frac{\ln(b/a)}{2\pi\sigma l}$$
单位长电阻：$R/l = \dfrac{\ln(b/a)}{2\pi\sigma}$

## T4-2 基尔霍夫定律解电路

**解**：设网孔电流，列KVL方程求解。以 $R_1=2\Omega,R_2=2\Omega,R_3=4\Omega,\mathcal{E}_1=12\text{V},\mathcal{E}_2=6\text{V}$ 为例：KCL：$I_1+I_2=I_3$；左网孔KVL：$12-2I_1-4I_3=0$；右网孔KVL：$6-2I_2-4I_3=0$。解得 $I_1=2\text{A},I_2=1\text{A},I_3=3\text{A}$。具体数值取决于电路拓扑。

## T4-3 $RC=\varepsilon/\sigma$ 的证明

**解**：两导体嵌入导电介质中。电容 $C=\varepsilon\times$(几何因子)；电阻 $R=(1/\sigma)\times$(同一几何因子)。
$$RC = \varepsilon\cdot\frac{1}{\sigma} = \frac{\varepsilon}{\sigma}$$
量纲 $[\varepsilon/\sigma]=[\text{F/m}]/[\text{S/m}]=[\text{s}]$（时间量纲）。$\tau_{\text{弛豫}}=\varepsilon/\sigma$ 是导电介质中体电荷衰减的特征时间。铜：$\tau\approx 10^{-19}\,\text{s}$——极短！

\newpage
# 第五章  真空中的静磁场（6题）

## T5-1 正方形载流线圈中心的磁场

**解**：每边对中心的贡献 $B_1=\frac{\mu_0 I}{4\pi(a/2)}(\cos 45^\circ+\cos 45^\circ)=\frac{\sqrt{2}\mu_0 I}{2\pi a}$。四边叠加：$B=4B_1=\frac{2\sqrt{2}\mu_0 I}{\pi a}$。
正 $n$ 边形推广：$B=\frac{\mu_0 nI}{2\pi R}\sin\frac{\pi}{n}$（$R$ 为外接圆半径）。$n\to\infty$ 时 $B\to\mu_0 I/(2R)$（圆环极限）。

## T5-2 圆柱导体内外磁场

**电流均匀分布**：$r<a$：$B=\mu_0 Ir/(2\pi a^2)$；$r>a$：$B=\mu_0 I/(2\pi r)$。
**电流仅分布在表面**：$r<a$：$B=0$；$r>a$：$B=\mu_0 I/(2\pi r)$。

## T5-3 亥姆霍兹线圈

单线圈轴线上 $B(z)=\frac{\mu_0 IR^2}{2(R^2+z^2)^{3/2}}$。两线圈中心 $O$ 处（$z=\pm R/2$）$B_O=\frac{8\mu_0 I}{5\sqrt{5}R}$。
展开 $B(z)$ 到二阶：$a=R$ 时 $B'(0)=B''(0)=0$，即中心附近磁场最均匀。

## T5-4 带电粒子在磁场中的螺旋运动

$v_\perp=v_0\sin\theta$，$v_\parallel=v_0\cos\theta$。$r=mv_\perp/(qB)=mv_0\sin\theta/(qB)$。
螺距 $h=v_\parallel T=v_0\cos\theta\cdot 2\pi m/(qB)$。回旋频率 $\omega_c=qB/m$。

## T5-5 磁镜约束（绝热不变量）

磁矩 $\mu=mv_\perp^2/(2B)=\text{const}$。向强场区运动→$B\uparrow$→$v_\perp\uparrow$→$v_\parallel\downarrow$（动能守恒）→可能被反射。逃逸锥角 $\sin^2\theta_c=B_0/B_m$。逃逸比例 $f=1-\sqrt{3}/2\approx 13.4\%$（$R_m=4$ 时）。

## T5-6 无限大载流薄板的磁场

**解**：面电流密度 $K=I/(2a)$。取矩形安培环路跨板两侧：$B\cdot 2l=\mu_0 Kl\Rightarrow B=\mu_0 K/2=\mu_0 I/(4a)$。两侧 $B$ 方向相反、平行于板面、垂直于电流方向。

\newpage
# 第六章  磁介质（4题）

## T6-1 含磁介质载流导线
**解**：$r<a$：$H=Ir/(2\pi a^2),B=\mu_0 Ir/(2\pi a^2)$。$a<r<b$：$H=I/(2\pi r),B=\mu I/(2\pi r)$。$r>b$：$H=I/(2\pi r),B=\mu_0 I/(2\pi r)$。磁化面电流 $i'_a=(\mu-\mu_0)I/(2\pi\mu_0 a)$（$+z$），$i'_b=-(\mu-\mu_0)I/(2\pi\mu_0 b)$（$-z$）。

## T6-2 均匀磁化球
**解**：类比均匀极化介质球。球内 $\boldsymbol{H}_{\text{in}}=-\boldsymbol{M}/3$，$\boldsymbol{B}_{\text{in}}=\mu_0(\boldsymbol{H}_{\text{in}}+\boldsymbol{M})=\frac{2}{3}\mu_0\boldsymbol{M}$。球外等效于中心处磁偶极子 $\boldsymbol{m}=\frac{4\pi}{3}R^3\boldsymbol{M}$ 的场。

## T6-3 带气隙磁路
**解**：$\mathcal{F}=NI$。$\mathcal{R}_{\text{core}}=l/(\mu_0\mu_r S)$，$\mathcal{R}_{\text{gap}}=l_g/(\mu_0 S)$。$\Phi=\mathcal{F}/(\mathcal{R}_{\text{core}}+\mathcal{R}_{\text{gap}})$。气隙 $B=\Phi/S\approx\mu_0 NI/l_g$（若 $\mu_r\gg 1$，铁芯磁阻可忽略）。$L=N\Phi/I=N^2/(\mathcal{R}_{\text{core}}+\mathcal{R}_{\text{gap}})$。

## T6-4 磁介质圆柱在均匀外磁场中
**解**：分离变量法（同6.19题）。柱内 $\boldsymbol{H}_{\text{in}}=\frac{2\mu_0}{\mu+\mu_0}\boldsymbol{H}_0$。$\boldsymbol{B}_{\text{in}}=\mu\boldsymbol{H}_{\text{in}}=\frac{2\mu}{\mu+\mu_0}\boldsymbol{B}_0$。证毕。

\newpage
# 第七章  电磁感应（7题）

## T7-1 旋转导体棒的动生电动势
**解**：$d\mathcal{E}=(\boldsymbol{v}\times\boldsymbol{B})\cdot d\boldsymbol{l}=B\omega r\,dr$。$\mathcal{E}=\int_0^l B\omega r\,dr=\frac{1}{2}B\omega l^2$。方向：右手定则（$\boldsymbol{v}\times\boldsymbol{B}$ 方向）。

## T7-2 螺线管变化磁场产生的涡旋电场
**解**：$dB/dt=\mu_0 n\,dI/dt=\mu_0 nk$。管内 $r<R$：$E\cdot 2\pi r=-\pi r^2\cdot\mu_0 nk\Rightarrow E=-\frac{1}{2}\mu_0 nkr$。管外 $r>R$：$E=-\frac{\mu_0 nk R^2}{2r}$。管外放导体棒时，$\mathcal{E}=\int\boldsymbol{E}\cdot d\boldsymbol{l}$（与具体位置和方向有关）。

## T7-3 两同心圆线圈的互感感应
**解**：$M=\mu_0\pi a^2/(2b)$。$\mathcal{E}_s=-M dI/dt=-M I_0\omega\cos\omega t$。$I_s=\mathcal{E}_s/R$。小线圈磁矩 $m_s=\pi a^2 I_s$，平均力矩 $\langle\tau\rangle=\mu_0^2\pi^2 a^4 I_0^2\omega/(8b^2 R)$。

## T7-4 同轴电缆自感
**磁通法**：$a<r<b$ 时 $B=\mu_0 I/(2\pi r)$。$\Phi_1=\frac{\mu_0 I}{2\pi}\ln\frac{b}{a}$。单位长 $L=\frac{\mu_0}{2\pi}\ln\frac{b}{a}$。
**磁能法**：$W_m=\int_a^b\frac{B^2}{2\mu_0}2\pi r\,dr=\frac{\mu_0 I^2}{4\pi}\ln\frac{b}{a}$，$L=2W_m/I^2$，结果一致。
若内导体为实心，需加内部磁能贡献：$L=\frac{\mu_0}{2\pi}(\frac{1}{4}+\ln\frac{b}{a})$。

## T7-5 RL暂态过程
**解**：$\tau=L/R=0.5/10=0.05\,\text{s}$。$I(t)=1.2(1-e^{-20t})\,\text{A}$（稳态 $I_0=12/10=1.2\,\text{A}$）。$t=3\tau=0.15\,\text{s}$ 时 $I=1.2(1-e^{-3})=1.14\,\text{A}$。储能 $W_m=\frac{1}{2}LI_0^2=0.36\,\text{J}$。

## T7-6 RLC暂态分析
**解**：$\omega_0=1/\sqrt{LC}=1/\sqrt{0.1\times 10^{-5}}=1000\,\text{rad/s}$。临界阻尼 $R=2\sqrt{L/C}=2\sqrt{0.1/10^{-5}}=200\,\Omega$。$R=50\,\Omega<200\,\Omega$→欠阻尼振荡。$\beta=R/(2L)=250$，$\omega_1=\sqrt{1000^2-250^2}=968\,\text{rad/s}$。

## T7-7 导体框架在磁场中运动（能量守恒）
**解**：导体棒运动→切割磁力线→动生电动势 $\mathcal{E}=Blv$→感应电流 $I=\mathcal{E}/R$→安培力 $F=BIl=B^2 l^2 v/R$（阻碍运动）→机械功率 $Fv$=电功率 $I^2 R$。动能→电能→焦耳热，能量完全守恒。

\newpage
# 第八章  磁能（3题）

## T8-1 磁能法求同轴电缆自感
**解**：$B(r)=\frac{\mu_0 I}{2\pi r}\;(a<r<b)$。$W_m=\int_a^b\frac{B^2}{2\mu_0}2\pi r\,dr=\frac{\mu_0 I^2}{4\pi}\ln\frac{b}{a}$。$L=2W_m/I^2=\frac{\mu_0}{2\pi}\ln\frac{b}{a}$（空心内导体时需加 $\frac{\mu_0}{8\pi}$）。

## T8-2 平行载流导线间作用力
**解**：单位长磁能 $W_m=\frac{\mu_0 I_1 I_2}{\pi}\ln\frac{d}{r_0}$。$F=-\partial W_m/\partial d|_I=-\mu_0 I_1 I_2/(\pi d)$。同向电流时 $F<0$（吸引力），单位长力 $f=\mu_0 I_1 I_2/(2\pi d)$。

## T8-3 电磁铁衔铁受力
**解**：气隙磁能 $W_m=B^2 S x/(\mu_0)$（$x$ 为气隙总长）。$F=-\partial W_m/\partial x|_\Phi=-B^2 S/\mu_0$。代入实际数值即可计算吸力。

\newpage
# 第九章  交流电路（4题）

## T9-1 RLC串联电路分析
$\omega=2\pi\times 50=314\,\text{rad/s}$。$X_L=\omega L=31.4\Omega$，$X_C=1/(\omega C)=637\Omega$。$Z=20+j(31.4-637)=20-j605.6\Omega$，$|Z|=606\Omega$。$I=U/|Z|=220/606=0.363\,\text{A}$。$\cos\varphi=R/|Z|=20/606=0.033$。$U_R=IR=7.3\text{V}$，$U_L=IX_L=11.4\text{V}$，$U_C=IX_C=231\text{V}$。

## T9-2 谐振分析
$\omega_0=1/\sqrt{LC}=1/\sqrt{0.1\times 5\times 10^{-6}}=1414\,\text{rad/s}$，$f_0=225\,\text{Hz}$。谐振时 $Z=R=20\Omega$，$I=220/20=11\,\text{A}$。$U_L=U_C=QU=Q\times 220$，$Q=\omega_0 L/R=1414\times 0.1/20=7.07$。$U_L=U_C=1556\,\text{V}$（远大于电源电压！）。

## T9-3 谐振电路设计
$\omega_0=2\pi\times 10^6=6.28\times 10^6\,\text{rad/s}$。$L=1/(\omega_0^2 C)=1/((6.28\times 10^6)^2\times 100\times 10^{-12})=253\,\mu\text{H}$。$R=\omega_0 L/Q=6.28\times 10^6\times 253\times 10^{-6}/100=15.9\,\Omega$。

## T9-4 变压器
$U_2/U_1=N_2/N_1=100/1000=0.1$，$U_2=22\,\text{V}$（开路）。反射电阻 $R'=(N_1/N_2)^2 R_L=100\times 10=1000\,\Omega$。$I_1=U_1/R'=220/1000=0.22\,\text{A}$。

\newpage
# 第十章  麦克斯韦电磁理论（6题）

## T10-1 位移电流与磁场
$D=\varepsilon_0 E=\varepsilon_0 U/d$。$j_D=\partial D/\partial t=\varepsilon_0\omega U_0\cos\omega t/d$。安培-麦克斯韦：$B\cdot 2\pi r=\mu_0 j_D\cdot\pi r^2$ → $B=\frac{1}{2}\mu_0\varepsilon_0\omega U_0 r\cos\omega t/d$。

## T10-2 位移电流的必要性
以电容器充电为例：导线中有传导电流 $I$，但极板间无传导电流。若无位移电流，同一安培环路在导线处 $B\neq 0$，在极板间 $B=0$——矛盾！引入 $\boldsymbol{j}_D=\partial\boldsymbol{D}/\partial t$ 后，极板间 $I_D=I$，安培环路定理处处自洽。

## T10-3 波动方程推导
对 $\nabla\times\boldsymbol{E}=-\partial\boldsymbol{B}/\partial t$ 取旋度：$\nabla\times(\nabla\times\boldsymbol{E})=-\partial/\partial t(\nabla\times\boldsymbol{B})$。代入 $\nabla\times\boldsymbol{B}=\mu_0\varepsilon_0\partial\boldsymbol{E}/\partial t$（真空中 $\boldsymbol{j}=0$）：$\nabla(\nabla\cdot\boldsymbol{E})-\nabla^2\boldsymbol{E}=-\mu_0\varepsilon_0\partial^2\boldsymbol{E}/\partial t^2$。真空中 $\nabla\cdot\boldsymbol{E}=0$，得 $\nabla^2\boldsymbol{E}-\frac{1}{c^2}\frac{\partial^2\boldsymbol{E}}{\partial t^2}=0$，$c=1/\sqrt{\mu_0\varepsilon_0}$。

## T10-4 平面电磁波基本性质
$\boldsymbol{B}=\frac{1}{c}\hat{\boldsymbol{k}}\times\boldsymbol{E}=\frac{E_0}{c}\cos(kz-\omega t)\hat{\boldsymbol{y}}$。$\langle S\rangle=\frac{E_0^2}{2\mu_0 c}\hat{\boldsymbol{z}}$，$\langle w\rangle=\frac{1}{2}\varepsilon_0 E_0^2$。验证 $\langle S\rangle=c\langle w\rangle\hat{\boldsymbol{z}}$。

## T10-5 载流导线表面的坡印亭矢量
导线表面 $E_{\text{axial}}=IR/l$（轴向），$B_{\text{azimuthal}}=\mu_0 I/(2\pi a)$（环向）。$\boldsymbol{S}=\boldsymbol{E}\times\boldsymbol{B}/\mu_0$ 沿径向向内。总流入功率 $=S\cdot 2\pi a l=I^2 R$，等于焦耳热功率——能量通过电磁场从空间流入导线，而非沿导线内部传输。

## T10-6 激光辐射压力
$I=P/(\pi r^2)=3\times 10^{-3}/(\pi\times(10^{-3})^2)=955\,\text{W/m}^2$。$p=(1+R)I/c=(1+0.7)\times 955/(3\times 10^8)=5.4\times 10^{-6}\,\text{N/m}^2$。全吸收表面 $(R=0)$ 时 $p=I/c$；全反射 $(R=1)$ 时 $p=2I/c$。

\newpage
# 综合模拟题（5题）

## M1 导体球+同心介质球壳
**答**：同 T2-6 题解。$r<a$：$\boldsymbol{D}=0$。$a<r<b$：$D=Q/(4\pi r^2)$，$E=Q/(4\pi\varepsilon_0\varepsilon_r r^2)$。$r>b$：$D=Q/(4\pi r^2)$，$E=Q/(4\pi\varepsilon_0 r^2)$。$\sigma'_a=-(\varepsilon_r-1)Q/(4\pi\varepsilon_r a^2)$，$\sigma'_b=(\varepsilon_r-1)Q/(4\pi\varepsilon_r b^2)$。导体球电势 $V_a=Q/(4\pi\varepsilon_0)[1/(\varepsilon_r a)-1/(\varepsilon_r b)+1/b]$。

## M2 永磁体+线圈互感
(1) 永磁体轴线上 $B$ 用磁荷法（同 6.17 题）。(2) 互感 $M=\Psi/I$，其中 $\Psi$ 为永磁体磁场穿过线圈的磁通。若永磁体磁场固定，$M$ 由几何参数确定。(3) 交变电流产生交变磁场→永磁体中磁畴受力→若磁场幅值超过矫顽力→可能退磁。能量：线圈能量通过互感耦合到永磁体磁能中。

## M3 RLC振荡能量分析
$\omega_0=1/\sqrt{LC}=1/\sqrt{0.2\times 5\times 10^{-6}}=1000\,\text{rad/s}$。$\beta=R/(2L)=20/(0.4)=50$。$\beta<\omega_0$→欠阻尼振荡。$q(t)=Q_0 e^{-\beta t}\cos(\omega_1 t)$，$\omega_1=\sqrt{1000^2-50^2}=998.7\,\text{rad/s}$。半周期 $T/2=\pi/\omega_1\approx 3.15\,\text{ms}$。电阻消耗能量=初态总电磁能-半周期后剩余电磁能。

## M4 太阳光的电磁场与辐射压力
(1) $S_0=c\varepsilon_0 E_0^2/2$ → $E_0=\sqrt{2S_0/(c\varepsilon_0)}=\sqrt{2\times 1360/(3\times 10^8\times 8.85\times 10^{-12})}\approx 1010\,\text{V/m}$。$B_0=E_0/c=3.37\times 10^{-6}\,\text{T}$。
(2) $p=S_0/c=1360/(3\times 10^8)=4.5\times 10^{-6}\,\text{N/m}^2$。地球截面积 $\pi R_E^2$，总辐射压力 $F=p\pi R_E^2\approx 5.8\times 10^8\,\text{N}$。
(3) 电池板输出电功率 $=0.20\times 1360\times 1=272\,\text{W}$。

## M5 $\boldsymbol{D}$ 与 $\boldsymbol{H}$ 的对称性对比
**完全对称的部分**：引入动机相同（简化介质问题，通量/环量只与自由源有关）；高斯/安培定理形式对称；边界条件对称（$D_n$ 连续 ↔ $H_t$ 连续）。
**根本不同**：$\nabla\cdot\boldsymbol{D}=\rho_f$ 体现电荷为源（散度型）；$\nabla\cdot\boldsymbol{B}=0$ 体现无磁荷（磁场总是无散）。$\boldsymbol{D}$ 线的起止→自由电荷；$\boldsymbol{B}$ 线永远是闭合曲线。束缚源：$\rho'=-\nabla\cdot\boldsymbol{P}$（散度）vs $\boldsymbol{j}'=\nabla\times\boldsymbol{M}$（旋度）——因为自由电荷是标量而自由电流是矢量。

