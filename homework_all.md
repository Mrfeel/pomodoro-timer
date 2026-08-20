# 电磁学作业解答

**杨思辰  PB25992094  未来技术学院  物理学专业**

教材：胡友秋等《电磁学》（科学出版社，2024）

\newpage

# 第11周作业 — 第五章：真空中的静磁场

## 题目：教材习题 5.17, 5.18

### 5.17 题 — 磁场缓慢变化时带电粒子的运动

**题目**：设在一均匀磁场 $B_0$ 中有一带电粒子在与 $B_0$ 垂直的平面内做圆周运动，速率为 $v_0$，电荷为 $e$，质量为 $m$。当磁场由 $B_0$ 缓慢变化到 $B$ 时，求粒子的运动速率和回旋半径。

**解**：

**(1) 绝热不变量—轨道磁矩守恒**

当磁场变化的时间尺度远大于粒子的回旋周期时，系统存在一个绝热不变量—轨道磁矩 $\mu$。带电粒子做圆周运动等效于一个小电流环：

$$\mu = I \cdot S$$

回旋频率 $\omega_c = eB/m$，回旋周期 $T = 2\pi/\omega_c = 2\pi m/(eB)$。

等效电流 $I = e/T = e^2 B/(2\pi m)$

回路面积 $S = \pi r^2 = \pi(mv_\perp/eB)^2$

代入得轨道磁矩：

$$\mu = \frac{e^2 B}{2\pi m} \cdot \pi\left(\frac{mv_\perp}{eB}\right)^2 = \frac{m v_\perp^2}{2B}$$

也可写为 $\mu = W_\perp/B$，其中 $W_\perp = \frac{1}{2}mv_\perp^2$ 为横向动能。

**(2) 磁场变化时速率的变化**

由磁矩守恒 $\mu_0 = \mu$：

$$\frac{m v_0^2}{2B_0} = \frac{m v^2}{2B}$$

$$\Rightarrow v^2 = v_0^2 \frac{B}{B_0}$$

$$v = v_0 \sqrt{\frac{B}{B_0}}$$

**(3) 回旋半径的变化**

$r = mv/(eB)$，代入 $v$：

$$r = \frac{m}{eB} \cdot v_0\sqrt{\frac{B}{B_0}} = \frac{mv_0}{e\sqrt{BB_0}}$$

用初始半径 $r_0 = mv_0/(eB_0)$ 表示：

$$r = r_0 \sqrt{\frac{B_0}{B}}$$

**(4) 物理意义**：磁场增强时—(i) 速率增大（变化磁场的感应电场对粒子做功）；(ii) 回旋半径减小（磁力线收紧，约束增强）。

---

### 5.18 题 — 磁镜中粒子的逃逸比例

**题目**：有一磁镜装置，磁镜比为 $R_m=4$，在磁镜装置中心部位有一各向同性带电粒子源，问从磁镜中逃逸的粒子占多少比例？

**解**：

**(1) 磁镜约束的物理图像**

磁镜中磁场不均匀：中心弱（$B_0$），两端强（$B_m$）。带电粒子从中心向两端运动时：
- 磁矩守恒 $\mu = mv_\perp^2/(2B) = \text{const}$ → $B \uparrow$ 则 $v_\perp \uparrow$
- 动能守恒 $\frac{1}{2}m(v_\perp^2+v_\parallel^2) = \text{const}$ → $v_\perp \uparrow$ 则 $v_\parallel \downarrow$
- 当 $v_\parallel \to 0$ 时，粒子被「反射」回中心区

**(2) 逃逸条件**

设中心处粒子速率为 $v$，与磁力线夹角为 $\theta_0$：

$$v_{\perp 0} = v\sin\theta_0, \quad v_{\parallel 0} = v\cos\theta_0$$

由磁矩守恒，在磁镜处：

$$\frac{m(v\sin\theta_0)^2}{2B_0} = \frac{mv_{\perp m}^2}{2B_m}$$

$$v_{\perp m}^2 = v^2\sin^2\theta_0 \cdot \frac{B_m}{B_0}$$

粒子能到达磁镜的条件是 $v_{\perp m}^2 \leq v^2$（到达时横向动能不超过总动能）：

$$\sin^2\theta_0\cdot\frac{B_m}{B_0} \leq 1$$

$$\sin^2\theta_0 \leq \frac{B_0}{B_m} = \frac{1}{R_m}$$

**(3) 逃逸锥**

$$\sin^2\theta_c = \frac{1}{R_m} = \frac{1}{4}$$

$$\sin\theta_c = \frac{1}{2}, \quad \theta_c = 30^\circ$$

速度方向与磁力线夹角 $\theta_0 < 30^\circ$ 的粒子能逃逸。

**(4) 各向同性源的速度空间积分**

速度空间中方向 $\theta$ 处的立体角元 $d\Omega = \sin\theta\,d\theta\,d\varphi$。

一个逃逸锥（$0 \leq \theta \leq \theta_c$）的立体角：

$$\Omega_1 = \int_0^{2\pi}\int_0^{\theta_c}\sin\theta\,d\theta\,d\varphi = 2\pi(1-\cos\theta_c)$$

$$= 2\pi\left(1-\frac{\sqrt{3}}{2}\right)$$

两个逃逸锥（沿 $+B$ 和 $-B$ 方向各一个），总逃逸立体角：

$$\Omega_{\text{esc}} = 4\pi\left(1-\frac{\sqrt{3}}{2}\right)$$

**(5) 逃逸比例**

$$f = \frac{\Omega_{\text{esc}}}{4\pi} = 1 - \frac{\sqrt{3}}{2} \approx 1 - 0.866 = 0.134$$

**答案**：约 **13.4%** 逃逸，**86.6%** 被磁镜约束。

\newpage
# 第12周作业 (2025年5月15日)

## 题目1-3：教材习题 6.13, 6.17, 6.19

### 6.13 题 — 含磁介质的载流导线

**题目**：无限长直圆柱铜导线（半径 $R_1$）外包磁导率 $\mu$ 的圆筒形磁介质（外半径 $R_2$），导线内电流 $I$ 均匀分布。求 $H$、$B$ 分布及磁化面电流密度。

**解**：

**(1) 对称性**：轴对称，$H$ 仅有环向分量 $H(r)\hat{\boldsymbol{\varphi}}$。

**(2) 安培环路定理** $\oint\boldsymbol{H}\cdot d\boldsymbol{l}=I_{\text{enc}}$：

- **$r<R_1$（导线内）**：$I_{\text{enc}} = I\cdot r^2/R_1^2$

$$H_1 = \frac{Ir}{2\pi R_1^2}, \quad B_1 = \frac{\mu_0 Ir}{2\pi R_1^2}$$

- **$R_1<r<R_2$（磁介质）**：$I_{\text{enc}}=I$

$$H_2 = \frac{I}{2\pi r}, \quad B_2 = \frac{\mu I}{2\pi r}$$

- **$r>R_2$（介质外）**：$I_{\text{enc}}=I$

$$H_3 = \frac{I}{2\pi r}, \quad B_3 = \frac{\mu_0 I}{2\pi r}$$

**(3) 磁化强度**：$M = B/\mu_0 - H$

介质内：$M(r) = \frac{(\mu-\mu_0)I}{2\pi\mu_0 r}$

**(4) 磁化面电流** $\boldsymbol{i}'=\boldsymbol{M}\times\hat{\boldsymbol{n}}$：

- 内表面($r=R_1$)：$i'_{\text{内}}=\frac{(\mu-\mu_0)I}{2\pi\mu_0 R_1}$，沿 $+\hat{\boldsymbol{z}}$
- 外表面($r=R_2$)：$i'_{\text{外}}=\frac{(\mu-\mu_0)I}{2\pi\mu_0 R_2}$，沿 $-\hat{\boldsymbol{z}}$

验证：$i'_{\text{内}}\cdot 2\pi R_1 + i'_{\text{外}}\cdot 2\pi R_2 = 0$，净磁化电流为零。

---

### 6.17 题 — 均匀磁化永磁体的轴线上磁场

**解**：

**(1) 磁荷法**：均匀磁化 $\boldsymbol{M}$，体磁荷 $\rho_m=-\mu_0\nabla\cdot\boldsymbol{M}=0$。两端面出现面磁荷：$\sigma_m = \pm\mu_0 M$。

等效为两个相距 $l$、面磁荷密度分别为 $+\mu_0 M$ 和 $-\mu_0 M$ 的圆盘。

**(2) 单盘轴线上 $H$**（类比静电场均匀带电圆盘）：

$$H_{\text{单盘}}(d) = \frac{\sigma_m}{2\mu_0}\left[1-\frac{d}{\sqrt{a^2+d^2}}\right]$$

轴线上 $M=0$ 故 $B=\mu_0 H$。

**(3) 叠加**：中心为原点，端面在 $z=\pm l/2$：

$$B(x)=\frac{\mu_0 M}{2}\left[\frac{x+l/2}{\sqrt{a^2+(x+l/2)^2}}-\frac{x-l/2}{\sqrt{a^2+(x-l/2)^2}}\right]$$

**(4) 验证**：$x=0$ 时 $B(0)=\mu_0 M\frac{l}{\sqrt{4a^2+l^2}}$。$l\gg a$ 时 $B(0)\approx\mu_0 M$。

---

### 6.19 题 — 磁介质圆柱置于均匀外磁场中

**解**：

**(1) 定解问题**：无自由电流 → $\nabla\times\boldsymbol{H}=0$ → 引入磁标势 $\varphi_m$，$\boldsymbol{H}=-\nabla\varphi_m$。

均匀介质中 $\nabla\cdot\boldsymbol{B}=0 \Rightarrow \nabla^2\varphi_m=0$。

外场 $\boldsymbol{B}_0=B_0\hat{\boldsymbol{x}}$，$H_0=B_0/\mu_0$。极坐标 $(r,\varphi)$ 中，远处渐近行为 $\varphi_m\to -H_0 r\cos\varphi$。

**(2) 分离变量解**：
- 柱外($r>a$)：$\varphi_m^{\text{out}} = -H_0 r\cos\varphi + \frac{A\cos\varphi}{r}$
- 柱内($r<a$)：$\varphi_m^{\text{in}} = C r\cos\varphi$

**(3) $r=a$ 边界条件**：

$H_\varphi$ 连续：$-H_0\sin\varphi+\frac{A}{a^2}\sin\varphi = C\sin\varphi$

$$H_0 - \frac{A}{a^2} = -C \quad\cdots(1)$$

$B_r$ 连续：$\mu_0\left(H_0\cos\varphi+\frac{A}{a^2}\cos\varphi\right) = -\mu C\cos\varphi$

$$\mu_0\left(H_0+\frac{A}{a^2}\right) = -\mu C \quad\cdots(2)$$

**(4) 解系数**：联立(1)(2)：

$$A = H_0 a^2\frac{\mu-\mu_0}{\mu+\mu_0}, \quad C = -H_0\frac{2\mu_0}{\mu+\mu_0}$$

**(5) 结果**：

柱内（均匀场）：$\boldsymbol{B}_{\text{in}} = \frac{2\mu}{\mu+\mu_0}B_0\hat{\boldsymbol{x}}$

柱外（均匀场+线偶极子场）：

$$B_x^{\text{out}} = B_0\left[1+\frac{\mu-\mu_0}{\mu+\mu_0}\frac{a^2(x^2-y^2)}{(x^2+y^2)^2}\right]$$

$$B_y^{\text{out}} = B_0\frac{\mu-\mu_0}{\mu+\mu_0}\frac{2a^2xy}{(x^2+y^2)^2}$$

**(6) 讨论**：$\mu>\mu_0$（顺磁）时磁力线向柱内聚集($B_{\text{in}}>B_0$)；$\mu<\mu_0$（抗磁）时磁力线被排斥($B_{\text{in}}<B_0$)。

\newpage
## 题目4：三层磁介质边界

**解**：利用 $B_n$ 连续（法向）和 $H_t$ 连续（切向）。
- 法向磁场：$B_1=B_2=B_3=B$，$H_i=B/\mu_i$
- 切向磁场：$H_1=H_2=H_3=H_0$，$B_i=\mu_i H_0$
- 任意方向：分解后叠加

## 题目5-9：教材习题 6.22, 7.2, 7.4, 7.6, 7.7

### 6.22 — 环形铁芯自感

安培环路定理：$H(r)=\frac{NI}{2\pi r}$，$B=\mu H$。
单匝磁通 $\Phi_1=\frac{\mu NIh}{2\pi}\ln\frac{R_2}{R_1}$，$\Psi=N\Phi_1$。
$$L=\frac{\Psi}{I}=\frac{\mu N^2 h}{2\pi}\ln\frac{R_2}{R_1}$$

### 7.2 — 矩形线圈感应电动势

$I=I_0\sin\omega t$，$B(r)=\frac{\mu_0 I}{2\pi r}$。
$\Phi=\frac{\mu_0 Ib}{2\pi}\ln\frac{d+a}{d}$。
$\mathcal{E}=-\frac{d\Phi}{dt}=-\frac{\mu_0 b\omega I_0}{2\pi}\ln\frac{d+a}{d}\cos(\omega t)$。

### 7.4 — 旋转线圈发电机

$\Phi=NBS\cos\omega t$，$\mathcal{E}=NBS\omega\sin\omega t=\mathcal{E}_0\sin\omega t$。
$\mathcal{E}_0=NBS\omega$。

### 7.6 — 螺线管感生电场

管内($r<R$)：$E=\frac{1}{2}\mu_0 n\alpha I_0 r e^{-\alpha t}$（环向）。
管外($r>R$)：$E=\frac{\mu_0 n\alpha I_0 R^2}{2r}e^{-\alpha t}$。

### 7.7 — 金属圆盘涡流损耗

$r$ 处圆环感应电动势 $\mathcal{E}=\omega B\pi r^2$。
该环电阻 $dR=2\pi r/(\sigma d\cdot dr)$。
$dP=\mathcal{E}^2/dR=\frac{\pi\sigma\omega^2 B^2 d}{2}r^3dr$。
$P=\int_0^a dP=\frac{\pi\sigma\omega^2 B^2 d a^4}{8}$。

\newpage
# 第13周作业 (2026年6月2日)

## 题目1：教材习题 7.8, 7.9, 7.11, 7.12, 7.14, 7.15, 7.17

### 7.8 — 环形螺线管的自感与互感

**(1) 自感系数**：环形螺线管截面为矩形（$R-a$ 到 $R+a$ 径向，高度 $h$）。
铁芯中 $B=\frac{\mu NI}{2\pi r}$，$\Phi_1=\frac{\mu NI h}{2\pi}\ln\frac{R+a}{R-a}$
$$L=\frac{N\Phi_1}{I}=\frac{\mu N^2 h}{2\pi}\ln\frac{R+a}{R-a}$$

**(2) 与中心长直导线互感**：长直导线磁场 $B=\frac{\mu_0 I}{2\pi r}$，穿过螺线管每匝的磁通量为 $\Phi=\frac{\mu_0 I h}{2\pi}\ln\frac{R+a}{R-a}$。
$$M=\frac{N\Phi}{I}=\frac{\mu_0 N h}{2\pi}\ln\frac{R+a}{R-a}$$

### 7.9 — 带气隙铁环线圈

磁路定理：总磁动势 $\mathcal{F}=NI$。铁芯磁阻 $\mathcal{R}_c=\frac{l_c}{\mu S}$，气隙磁阻 $\mathcal{R}_g=\frac{l_g}{\mu_0 S}$。
总磁通 $\Phi=\frac{NI}{\mathcal{R}_c+\mathcal{R}_g}$。
气隙中 $B=\Phi/S$。$L=N\Phi/I=N^2/(\mathcal{R}_c+\mathcal{R}_g)$。
代入数据得 $B\approx 0.795\,\text{T}$，$L\approx 1.14\,\text{H}$。

### 7.11 — RL电路暂态过程

$$L\frac{dI}{dt}+RI=\mathcal{E}$$
一阶线性微分方程，初始条件 $I(0)=0$：
$$I(t)=\frac{\mathcal{E}}{R}\left(1-e^{-\frac{R}{L}t}\right)=I_0(1-e^{-t/\tau})$$
时间常数 $\tau=L/R$，稳态电流 $I_0=\mathcal{E}/R$。

### 7.12 — RC放电暂态过程

$$\frac{q}{C}+IR=0,\quad I=-\frac{dq}{dt}$$
$$\frac{dq}{dt}+\frac{q}{RC}=0,\quad q(0)=q_0$$
解：$q(t)=q_0 e^{-t/RC}$，$I(t)=\frac{q_0}{RC}e^{-t/RC}$。时间常数 $\tau=RC$。

### 7.14 — RLC电路微分方程

$$L\frac{d^2q}{dt^2}+R\frac{dq}{dt}+\frac{q}{C}=0$$
特征方程：$L\lambda^2+R\lambda+1/C=0$
特征根：$\lambda=-\frac{R}{2L}\pm\sqrt{\left(\frac{R}{2L}\right)^2-\frac{1}{LC}}$
定义 $\beta=R/(2L)$（阻尼系数），$\omega_0=1/\sqrt{LC}$（固有频率）：
- $\beta<\omega_0$：欠阻尼振荡，$q=q_0 e^{-\beta t}\cos(\omega_1 t+\varphi)$
- $\beta=\omega_0$：临界阻尼，$R=2\sqrt{L/C}$
- $\beta>\omega_0$：过阻尼，非振荡衰减

### 7.15 — RLC振荡衰减时间常数

欠阻尼时 $q(t)=q_0 e^{-\beta t}\cos(\omega_1 t+\varphi)$，$\beta=R/(2L)$。
振幅按 $e^{-\beta t}$ 衰减，时间常数 $\tau=1/\beta=2L/R$。

### 7.17 — RLC交流稳态响应

复数法：$Z=R+j(\omega L-1/(\omega C))$，$|Z|=\sqrt{R^2+(\omega L-1/(\omega C))^2}$。
$\varphi=\arctan\frac{\omega L-1/(\omega C)}{R}$。
$I(t)=\frac{\mathcal{E}_0}{|Z|}\cos(\omega t-\varphi)$。
谐振条件 $\omega L=1/(\omega C)$ 即 $\omega_0=1/\sqrt{LC}$。

\newpage
## 题目2：同心旋转线圈系统

**题目**：小线圈（半径 $a$，电阻 $R$）与大线圈（半径 $b\gg a$）同心共面。大线圈维持恒定电流 $I$，小线圈绕其直径以角速度 $\omega$ 旋转。求：(1)互感；(2)小线圈感应电流；(3)外力矩；(4)大线圈感应电动势。

**解**：

**(1) 互感系数**

$b\gg a$，小线圈区域内大线圈的磁场近似均匀（等于圆心处磁场）：
$$B_b = \frac{\mu_0 I}{2b}$$
小线圈面积 $S=\pi a^2$，大线圈电流 $I$ 在小线圈中产生的磁通：
$$\Phi_{ab}=B_b\cdot\pi a^2=\frac{\mu_0 I\pi a^2}{2b}$$
$$M=\frac{\Phi_{ab}}{I}=\frac{\mu_0\pi a^2}{2b}$$

**(2) 小线圈感应电流**

$t$ 时刻小线圈法线与 $\boldsymbol{B}_b$ 夹角 $\theta=\omega t$，通过小线圈的磁通：
$$\Phi_s(t)=MI\cos(\omega t)$$
感应电动势：$\mathcal{E}_s=-\frac{d\Phi_s}{dt}=MI\omega\sin(\omega t)$
感应电流：$I_s=\frac{\mathcal{E}_s}{R}=\frac{\mu_0\pi a^2 I\omega}{2bR}\sin(\omega t)$

**(3) 外力矩**

小线圈磁矩 $m_s=\pi a^2 I_s$，在磁场 $B_b$ 中受力矩：
$$\tau=|\boldsymbol{m}_s\times\boldsymbol{B}_b|=m_s B_b|\sin(\omega t)|$$
代入 $m_s$ 和 $B_b$，并取时间平均（$\langle\sin^2\omega t\rangle=1/2$）：
$$\langle\tau\rangle=\frac{\mu_0^2\pi^2 a^4 I^2\omega}{8b^2 R}$$
维持匀速旋转需要克服此平均电磁力矩。

**(4) 大线圈感应电动势**

小线圈电流变化通过互感在大线圈中产生感应电动势：
$$\mathcal{E}_b=-M\frac{dI_s}{dt}=-M\cdot\frac{\mu_0\pi a^2 I\omega}{2bR}\cdot\omega\cos(\omega t)$$
$$=-\frac{\mu_0^2\pi^2 a^4 I\omega^2}{4b^2 R}\cos(\omega t)$$

\newpage
## 题目3：超导圆柱体的电磁响应（选做）

**伦敦方程**：$\frac{\partial\boldsymbol{J}_s}{\partial t}=\frac{n_s e^2}{m_e}(\boldsymbol{E}+\boldsymbol{v}\times\boldsymbol{B})$，$\nabla\times\boldsymbol{J}_s=-\frac{n_s e^2}{m_e}\boldsymbol{B}$

**(1) 稳态 ($t<0$)**：$\omega=\omega_0$，利用 $\nabla\times(\nabla\times\boldsymbol{B})=-\nabla^2\boldsymbol{B}$ 和伦敦方程：
$$\nabla^2\boldsymbol{B}=\frac{1}{\lambda_L^2}\boldsymbol{B},\quad \lambda_L=\sqrt{\frac{m_e}{\mu_0 n_s e^2}}$$
圆柱对称解（零阶修正贝塞尔函数）：
$$B(r)=B_0\frac{I_0(kr)}{I_0(kR)},\quad k=1/\lambda_L$$

**(2) 暂态 ($t\geq 0$)**：$\omega(t)=\omega_0 e^{-t/\tau}$，含传导电流的修正方程：
$$\nabla^2\boldsymbol{B}=\frac{1}{\lambda_L^2}\boldsymbol{B}+\mu_0\sigma\frac{\partial\boldsymbol{B}}{\partial t}$$
设 $\boldsymbol{B}(r,t)=B(r)e^{-t/\tau}\hat{\boldsymbol{z}}$，代入：
$$\frac{d^2 B}{dr^2}+\frac{1}{r}\frac{dB}{dr}-(k^2-\mu_0\sigma/\tau)B=0$$
解为 $B(r)=A\cdot I_0(\alpha r)$，$\alpha=\sqrt{k^2-\mu_0\sigma/\tau}$。

\newpage
## 题目4：磁四极透镜（选做，50分）

四个理想磁偶极子 $m$ 构成正方形（边长 $L$），位于 $xOy$ 平面，方向与 $x$ 轴成 $45^\circ$。

**(1) 偶极子A所受外力和外力矩**

磁偶极子间相互作用力公式：
$$\boldsymbol{F}=\frac{3\mu_0}{4\pi r^4}[(\boldsymbol{m}_1\cdot\hat{\boldsymbol{r}})\boldsymbol{m}_2+(\boldsymbol{m}_2\cdot\hat{\boldsymbol{r}})\boldsymbol{m}_1+(\boldsymbol{m}_1\cdot\boldsymbol{m}_2)\hat{\boldsymbol{r}}-5(\boldsymbol{m}_1\cdot\hat{\boldsymbol{r}})(\boldsymbol{m}_2\cdot\hat{\boldsymbol{r}})\hat{\boldsymbol{r}}]$$

四个偶极子位置和方向：
$A(\frac{L}{2},\frac{L}{2}),\; \boldsymbol{m}_A=\frac{m}{\sqrt{2}}(\hat{\boldsymbol{x}}+\hat{\boldsymbol{y}})$
$B(-\frac{L}{2},\frac{L}{2}),\; \boldsymbol{m}_B=\frac{m}{\sqrt{2}}(-\hat{\boldsymbol{x}}+\hat{\boldsymbol{y}})$
$C(-\frac{L}{2},-\frac{L}{2}),\; \boldsymbol{m}_C=\frac{m}{\sqrt{2}}(-\hat{\boldsymbol{x}}-\hat{\boldsymbol{y}})$
$D(\frac{L}{2},-\frac{L}{2}),\; \boldsymbol{m}_D=\frac{m}{\sqrt{2}}(\hat{\boldsymbol{x}}-\hat{\boldsymbol{y}})$

对A受的力，分别计算B、C、D对A的力后叠加。由对称性：
- B和D的力在 $x$ 方向分量抵消
- 合力沿对角线向外：$\boldsymbol{F}=\frac{3\mu_0 m^2}{4\pi L^4}\cdot\frac{\sqrt{2}}{2}(\hat{\boldsymbol{x}}+\hat{\boldsymbol{y}})$
维持A静止需施加等大反向力。力矩通过 $\boldsymbol{\tau}=\boldsymbol{m}_A\times\boldsymbol{B}_{\text{others}}$ 计算。

**(2) 原点附近磁场**（保留线性项）：

已知 $|\boldsymbol{B}(\delta,0)|/\delta=g_0$。原点附近展到一阶：
$$\boldsymbol{B}(x,y)=g_0(y\hat{\boldsymbol{x}}+x\hat{\boldsymbol{y}})$$
磁力线方程 $dy/dx=B_y/B_x=x/y$，即 $x^2-y^2=\text{const}$（双曲线族）。

**(3) 薄透镜焦距**

$xOz$ 平面中粒子运动（$y=0$，$B_y=g_0 x$），洛伦兹力 $x$ 分量：
$$m\frac{d^2 x}{dt^2}=qv_z B_y=qv_z g_0 x$$
$dz=v_z dt$，化为 $\frac{d^2 x}{dz^2}=\frac{q g_0}{p}x$（$p=mv_z$）。
薄透镜近似下 $(dx/dz)_{\text{out}}-(dx/dz)_{\text{in}}=-x/f$，焦距：
$$f=\frac{p}{q g_0 l}$$
$l$ 为有效长度。$xOz$ 面聚焦（$f>0$），$yOz$ 面散焦。

**(4) F-D-F三合透镜**

聚焦平面($xOz$)：F($f_1$)-漂移($L_d$)-D($-f_2$)-漂移($L_d$)-F($f_1$)。
散焦平面($yOz$)：D($-f_1$)-漂移- F($f_2$)-漂移-D($-f_1$)。
由物理对称性，两平面等效焦距相同的条件：$L_d^2=f_1 f_2$。
系统等效焦距：$f_{\text{sys}}=f_1^2/L_d$。

\newpage
# 第14周作业 — 电磁感应例题复习

**本周内容**：复习 EM007A 课件全部例题 + EM007B 课件第14页例题。

## 一、EM007A 核心例题清单

### 法拉第电磁感应定律
- 磁棒插入/拉出线圈的感应电流方向和大小
- 楞次定理判断感应电流方向：感应电流的磁通总是**反抗**原磁通的变化
- 导体在磁场中切割磁力线：动生电动势 $\mathcal{E}=\oint(\boldsymbol{v}\times\boldsymbol{B})\cdot d\boldsymbol{l}$

### 互感的计算
- 密绕螺线管：$M=\mu_0 N_1 N_2 S/l$
- 螺绕管与中心直导线：$M=\frac{\mu_0 N h}{2\pi}\ln\frac{b}{a}$
- 同心共面圆线圈

### 自感的计算
- 长螺线管：$L=\mu_0 n^2\pi a^2 l$
- 矩形截面螺绕管：$L=\frac{\mu_0 N^2 h}{2\pi}\ln\frac{b}{a}$
- 同轴电缆：$L=\frac{\mu_0}{2\pi}\left(\frac{1}{4}+\ln\frac{b}{a}\right)$（内导体实心）

### 三种计算自感的方法
1. 磁通匝链法：$L=\Psi/I$
2. 磁能法：$W_m=\frac{1}{2}LI^2=\int\frac{B^2}{2\mu_0}dV$
3. 电动势法：$\mathcal{E}_L=-L\,dI/dt$（工程测量用）

### 线圈连接
- 串联顺串：$L=L_1+L_2+2M$
- 串联反串：$L=L_1+L_2-2M$
- 并联（同名端）：$L=\frac{L_1 L_2-M^2}{L_1+L_2-2M}$

## 二、EM007B 第14页例题（重点）

**题目**：小线圈（半径 $a$）在大线圈（半径 $b$）上方 $z$ 处，共轴。验证 $M_{ab}=M_{ba}$。

**解**：

**(1) $M_{ab}$ 的计算**：大线圈轴线上 $B_b(z)=\frac{\mu_0 I_b b^2}{2(b^2+z^2)^{3/2}}$。小线圈足够小，在其区域 $B_b$ 近似均匀。
$$\Phi_{ab}\approx B_b\cdot\pi a^2=\frac{\mu_0 I_b\pi a^2 b^2}{2(b^2+z^2)^{3/2}}$$
$$M_{ab}=\frac{\Phi_{ab}}{I_b}=\frac{\mu_0\pi a^2 b^2}{2(b^2+z^2)^{3/2}}$$

**(2) $M_{ba}$ 的计算**：小线圈视为磁偶极子 $\boldsymbol{m}=\pi a^2 I_a\hat{\boldsymbol{z}}$。以球冠计算通过大线圈的磁通：
$$\Phi_{ba}=\int_S\boldsymbol{B}_a\cdot d\boldsymbol{S}=\frac{\mu_0\pi a^2 I_a b^2}{2(b^2+z^2)^{3/2}}$$
$$M_{ba}=\frac{\Phi_{ba}}{I_a}=\frac{\mu_0\pi a^2 b^2}{2(b^2+z^2)^{3/2}}=M_{ab}$$
证毕。验证了互感系数的对称性。

\newpage
# 第15周作业 (2026年6月13日)

## 题目1-5：教材习题 8.1, 8.3, 8.5, 8.6, 8.7（磁能与磁力）

### 8.1 — 磁能与自感

单个载流线圈磁能：$W_m=\frac{1}{2}LI^2$。磁场能量密度 $w_m=\frac{1}{2}\boldsymbol{B}\cdot\boldsymbol{H}$。
$$W_m=\int_V\frac{B^2}{2\mu_0}dV=\frac{1}{2}LI^2\;\Rightarrow\;L=\frac{2W_m}{I^2}$$

### 8.3 — 同轴电缆自感（磁能法）

内外导体间 $a<r<b$：$B=\frac{\mu_0 I}{2\pi r}$。
单位长磁能：$W_m=\int_a^b\frac{B^2}{2\mu_0}2\pi r\,dr=\frac{\mu_0 I^2}{4\pi}\ln\frac{b}{a}$。
$$L=\frac{2W_m}{I^2}=\frac{\mu_0}{2\pi}\ln\frac{b}{a}$$

### 8.5 — 线圈系统的磁能

$W_m=\frac{1}{2}L_1 I_1^2+\frac{1}{2}L_2 I_2^2+M I_1 I_2$。
串联($I_1=I_2=I$)：顺串 $W_m=\frac{1}{2}(L_1+L_2+2M)I^2$，反串 $W_m=\frac{1}{2}(L_1+L_2-2M)I^2$。

### 8.6 — 虚功原理求磁力

两平行导线间距 $d$，单位长磁能 $W_m=\frac{\mu_0 I_1 I_2}{\pi}\ln\frac{d}{r_0}$。
虚功原理（保持电流不变）：$F=-\left.\frac{\partial W_m}{\partial d}\right|_I=-\frac{\mu_0 I_1 I_2}{\pi d}$。
负号表示吸引力（同向电流）。单位长力 $f=\frac{\mu_0 I_1 I_2}{2\pi d}$（与安培定律一致）。

### 8.7 — 电磁铁吸力

气隙中 $B\approx\mu_0 NI/(2x)$（$x$ 为气隙长度，$S$ 为截面积）。
气隙磁能 $W_m\approx\frac{B^2 S x}{\mu_0}$。
$F=-\left.\frac{\partial W_m}{\partial x}\right|_\Phi=-\frac{B^2 S}{\mu_0}$（保持磁通不变）。吸力与 $B^2$ 和 $S$ 成正比。

\newpage
## 题目6：含磁介质的同轴电缆电感

**题目**：中心实心导线（半径 $a$），外导体壳（内径 $b$，外径 $c$），介质区 $a<r<b$ 充满相对磁导率 $\mu_r$ 的介质。电流等大反向均匀分布。求单位长度电感。

**解**：

**(1) 磁场分布**（安培环路定理）：
- $r<a$：$H=\frac{Ir}{2\pi a^2}$，$B=\frac{\mu_0 Ir}{2\pi a^2}$
- $a<r<b$：$H=\frac{I}{2\pi r}$，$B=\frac{\mu_0\mu_r I}{2\pi r}$
- $b<r<c$：$H=\frac{I(c^2-r^2)}{2\pi r(c^2-b^2)}$，$B=\frac{\mu_0 I(c^2-r^2)}{2\pi r(c^2-b^2)}$
- $r>c$：$H=0$，$B=0$

**(2) 磁能积分**：
$$W_m=\int_0^a\frac{B_1^2}{2\mu_0}2\pi r\,dr+\int_a^b\frac{B_2^2}{2\mu_0\mu_r}2\pi r\,dr+\int_b^c\frac{B_3^2}{2\mu_0}2\pi r\,dr$$
主要贡献来自介质区域（$a<r<b$）：
$$W_m\approx\frac{\mu_0\mu_r I^2}{4\pi}\ln\frac{b}{a}$$
$$L=\frac{2W_m}{I^2}\approx\frac{\mu_0\mu_r}{2\pi}\ln\frac{b}{a}$$
若 $\mu_r=1$ 则退化为 8.3 题结果。

\newpage
## 题目7：同轴电缆阻抗匹配

**证**：内导体半径 $a$，外导体内半径 $b$，介质 $\varepsilon,\mu$。

**(1) 电场与电能**：设内导体单位长电荷 $\lambda$，高斯定理：
$$E(r)=\frac{\lambda}{2\pi\varepsilon r}$$
单位长电容：$C=\frac{2\pi\varepsilon}{\ln(b/a)}$
单位长电能：$W_e=\int_a^b\frac{1}{2}\varepsilon E^2\cdot 2\pi r\,dr=\frac{\lambda^2}{4\pi\varepsilon}\ln\frac{b}{a}$

**(2) 磁场与磁能**：通电流 $I$ 时 $B(r)=\frac{\mu I}{2\pi r}$。
由 $I=U/R=\lambda/(RC)$（$U$ 为电压，$RC$ 放电），得：
$$W_m=\int_a^b\frac{B^2}{2\mu}2\pi r\,dr=\frac{\mu I^2}{4\pi}\ln\frac{b}{a}=\frac{\mu}{4\pi}\left(\frac{\lambda}{RC}\right)^2\ln\frac{b}{a}$$

**(3) 令磁能等于电能**：$W_m=W_e$
$$\frac{\mu}{4\pi}\left(\frac{\lambda}{RC}\right)^2\ln\frac{b}{a}=\frac{\lambda^2}{4\pi\varepsilon}\ln\frac{b}{a}$$
$$\frac{\mu}{(RC)^2}=\frac{1}{\varepsilon}\;\Rightarrow\;R=\frac{1}{C}\sqrt{\frac{\mu}{\varepsilon}}$$
代入 $C$：$R=\frac{1}{2\pi}\sqrt{\frac{\mu}{\varepsilon}}\ln\frac{b}{a}$。证毕。
此时 $R$ 等于同轴电缆的特性阻抗 $Z_0$。

\newpage
# 第16周作业 (2026年6月30日)

## 题目1：麦克斯韦方程组

积分形式：
$$\oint_S\boldsymbol{D}\cdot d\boldsymbol{S}=Q_f,\quad\oint_S\boldsymbol{B}\cdot d\boldsymbol{S}=0$$
$$\oint_L\boldsymbol{E}\cdot d\boldsymbol{l}=-\int_S\frac{\partial\boldsymbol{B}}{\partial t}\cdot d\boldsymbol{S}$$
$$\oint_L\boldsymbol{H}\cdot d\boldsymbol{l}=I_f+\int_S\frac{\partial\boldsymbol{D}}{\partial t}\cdot d\boldsymbol{S}$$

微分形式：
$$\nabla\cdot\boldsymbol{D}=\rho_f,\quad\nabla\cdot\boldsymbol{B}=0$$
$$\nabla\times\boldsymbol{E}=-\frac{\partial\boldsymbol{B}}{\partial t},\quad\nabla\times\boldsymbol{H}=\boldsymbol{j}_f+\frac{\partial\boldsymbol{D}}{\partial t}$$

其中 $\boldsymbol{D}=\varepsilon_0\boldsymbol{E}+\boldsymbol{P}$，$\boldsymbol{H}=\boldsymbol{B}/\mu_0-\boldsymbol{M}$。

## 题目2：教材习题 10.3, 10.4, 10.7, 10.11

### 10.3 — 位移电流与磁场

平行板电容器 $Q=Q_0\sin(\omega t)$，位移电流密度 $j_D=\frac{\partial D}{\partial t}$。
板内 $H=\frac{\omega Q_0 r}{2\pi a^2}\cos(\omega t)$，板外 $H=\frac{\omega Q_0}{2\pi r}\cos(\omega t)$。

### 10.4 — 界面场线折射

边界条件 $D_{1n}=D_{2n}$、$E_{1t}=E_{2t}$ → $\varepsilon_1\cot\theta_1=\varepsilon_2\cot\theta_2$。
$B_{1n}=B_{2n}$、$H_{1t}=H_{2t}$ → $\mu_1\cot\varphi_1=\mu_2\cot\varphi_2$。

### 10.7 — 平面电磁波基本性质

由 $\nabla\times\boldsymbol{E}=-\partial\boldsymbol{B}/\partial t$ 得 $B=E_0/c$，$\langle S\rangle=\frac{E_0^2}{2\mu_0 c}$，$\langle w\rangle=\frac{1}{2}\varepsilon_0 E_0^2$，$\langle S\rangle=c\langle w\rangle$。

### 10.11 — 电磁动量与辐射压力

动量密度 $\boldsymbol{g}=\boldsymbol{S}/c^2$。辐射压力：全吸收 $p=I/c$，全反射 $p=2I/c$。

\newpage
## 题目3：品质因数Q（选做）

$Q=2\pi\times\frac{\text{最大储能}}{\text{每周期损耗}}$

**(1) RL串联电路**：$W_{\max}=\frac{1}{2}LI_0^2$，每周期损耗 $\Delta W=P\cdot T=(\frac{1}{2}I_0^2 R)(2\pi/\omega)=\pi I_0^2 R/\omega$。
$$Q=\frac{2\pi\cdot\frac{1}{2}LI_0^2}{\pi I_0^2 R/\omega}=\frac{\omega L}{R}$$

**(2) 螺线管Q**：$L=\mu_0 n^2\pi a^2\ell$，导线电阻 $R_{\text{coil}}$ 由导线长度和截面积决定。
$$Q=\frac{\omega L}{R_{\text{coil}}}$$

**(3) 等效电阻**：$R_{\text{eq}}=\omega L/Q$。

**(4) 外接 $R$**：$Q_{\text{total}}=\frac{\omega L}{R_{\text{coil}}+R}$。

**(5) 频率依赖关系**：纯 RL：$Q\propto\omega$（单调增长）。RLC 谐振：$Q=\omega_0 L/R$，在 $\omega_0$ 处最大。

\newpage
## 题目4：介质中平面电磁波（选做）

$\boldsymbol{E}=\boldsymbol{E}_0 e^{-i(\omega t-\boldsymbol{k}\cdot\boldsymbol{r})}$，$\boldsymbol{B}=\boldsymbol{B}_0 e^{-i(\omega t-\boldsymbol{k}\cdot\boldsymbol{r})}$

**(1) 横波性**：$\nabla\cdot\boldsymbol{E}=0\to i\boldsymbol{k}\cdot\boldsymbol{E}=0$，同理 $\boldsymbol{k}\cdot\boldsymbol{B}=0$。

**(2) 振幅关系**：由 $\nabla\times\boldsymbol{E}=-\partial\boldsymbol{B}/\partial t$：$i\boldsymbol{k}\times\boldsymbol{E}=i\omega\boldsymbol{B}$，取模 $kE_0=\omega B_0$，即 $E_0/B_0=v=\frac{c}{\sqrt{\mu_r\varepsilon_r}}$。
$$\sqrt{\varepsilon_0\varepsilon_r}E_0=\frac{B_0}{\sqrt{\mu_0\mu_r}}$$

**(3) 相速度与折射率**：波动方程 $\nabla^2\boldsymbol{E}-\mu_0\mu_r\varepsilon_0\varepsilon_r\frac{\partial^2\boldsymbol{E}}{\partial t^2}=0$。
$$v=\frac{\omega}{k}=\frac{1}{\sqrt{\mu_0\mu_r\varepsilon_0\varepsilon_r}}=\frac{c}{\sqrt{\mu_r\varepsilon_r}},\quad n=\frac{c}{v}=\sqrt{\mu_r\varepsilon_r}$$

**(4) 能量密度和能流密度**：$w=\frac{1}{2}(\varepsilon_0\varepsilon_r E^2+\frac{B^2}{\mu_0\mu_r})$，$\boldsymbol{S}=\frac{\boldsymbol{E}\times\boldsymbol{B}}{\mu_0\mu_r}$。

**(5) $\boldsymbol{S}=v\,w\,\hat{\boldsymbol{e}}_k$**：利用 $B=(n/c)(\hat{\boldsymbol{e}}_k\times E)$ 和 $v=c/n$，代入验证。

**(6) 波动方程**：对 $\nabla\times\boldsymbol{E}=-\partial\boldsymbol{B}/\partial t$ 取旋度，代入 $\nabla\times\boldsymbol{B}=\mu_0\mu_r\varepsilon_0\varepsilon_r\partial\boldsymbol{E}/\partial t$，得 $\nabla^2\boldsymbol{E}-(1/v^2)\partial^2\boldsymbol{E}/\partial t^2=0$。

**(7) 时间平均量**：$\langle w\rangle=\frac{1}{2}\varepsilon_0\varepsilon_r E_0^2$，$\langle\boldsymbol{S}\rangle=v\langle w\rangle\hat{\boldsymbol{e}}_k$。

\newpage
## 题目5：电容器放电与坡印亭矢量（选做）

平行板电容器：极板半径 $a$、间距 $d\ll a$，初始电荷 $\pm Q$，通过中心电阻 $R$ 放电。

**(1) 场量**：RC放电 $q=Qe^{-t/RC}$，$I=\frac{Q}{RC}e^{-t/RC}$。
电场：$E=\frac{q}{\varepsilon_0\pi a^2}=\frac{Q}{\varepsilon_0\pi a^2}e^{-t/RC}$（均匀、沿轴向）
位移电流密度：$j_D=\varepsilon_0\frac{\partial E}{\partial t}=-\frac{Q}{\pi a^2 RC}e^{-t/RC}$
安培-麦克斯韦定律：$B\cdot 2\pi r=\mu_0 j_D\pi r^2$ → $B=-\frac{\mu_0 Q r}{2\pi a^2 RC}e^{-t/RC}\hat{\boldsymbol{\varphi}}$

**(2) 能量变化率**：焦耳热 $P_J=I^2 R=\frac{Q^2}{RC^2}e^{-2t/RC}$。
圆柱面A内电场能 $W_e=\frac{1}{2}\varepsilon_0 E^2\cdot\pi r^2 d$，$\frac{dW_e}{dt}=-\frac{Q^2 r^2 d}{\varepsilon_0\pi a^4 RC}e^{-2t/RC}$。

**(3) 坡印亭矢量**：$\boldsymbol{S}=\boldsymbol{E}\times\boldsymbol{B}/\mu_0$ 沿径向向内。通过A面的总能流：$P_S=\oint_A\boldsymbol{S}\cdot d\boldsymbol{A}$。
由坡印亭定理验证能量守恒：流入能流=电磁能变化率+焦耳热损耗。
这展示了能量不是通过导线而是**通过电磁场从周围空间传入**电容器内部的。

\newpage
# 第17周作业 — 电磁能量/坡印亭矢量 + 第九章习题

## 第一部分：EM010C 全部例题总结

### 坡印亭定理
$$\frac{\partial w}{\partial t}+\nabla\cdot\boldsymbol{S}=-\boldsymbol{j}\cdot\boldsymbol{E}$$
$\boldsymbol{S}=\boldsymbol{E}\times\boldsymbol{H}$（坡印亭矢量），$w=\frac{1}{2}(\boldsymbol{E}\cdot\boldsymbol{D}+\boldsymbol{B}\cdot\boldsymbol{H})$。

### 平面电磁波能量
$w=\varepsilon_0 E_0^2\cos^2(kz-\omega t)$，$\langle w\rangle=\frac{1}{2}\varepsilon_0 E_0^2$。
$\boldsymbol{S}=c\varepsilon_0 E_0^2\cos^2(kz-\omega t)\hat{\boldsymbol{z}}$，$\langle S\rangle=\frac{1}{2}c\varepsilon_0 E_0^2$。

### 电容器充电过程的能量流动（关键）
坡印亭矢量从侧面流入极板间→能量不是通过导线传入，而是通过电磁场从空间传入。

### 载流导线表面的能流
表面 $E$ 沿轴向、$B$ 沿环向 → $S$ 沿径向向内 → 焦耳热能量由电磁场从周围传入。

### 电磁场动量与辐射压力
动量密度 $\boldsymbol{g}=\boldsymbol{S}/c^2$。太阳光对地球的辐射压力约 $5.8\times 10^8\,\text{N}$。

### 电磁角动量
角动量密度 $\boldsymbol{l}=\boldsymbol{r}\times\boldsymbol{S}/c^2$。带电球+磁偶极子系统电磁角动量 $L_{\text{em}}=\frac{2}{9}\mu_0 M Q a^2$。

\newpage
## 第二部分：教材第九章习题 9.1-9.6

### 9.1 — 电感和电容的阻抗

**(1) $L=10\,\text{H}$**：$Z_L=2\pi f L$

| $f$ | 50 Hz | 60 Hz | 600 Hz |
|-----|-------|-------|--------|
| $Z_L$ | $3.14\times 10^3\,\Omega$ | $3.77\times 10^3\,\Omega$ | $3.77\times 10^4\,\Omega$ |

**(2) $C=10\,\mu\text{F}$**：$Z_C=1/(2\pi f C)$

| $f$ | 50 Hz | 60 Hz | 600 Hz |
|-----|-------|-------|--------|
| $Z_C$ | $318\,\Omega$ | $265\,\Omega$ | $26.5\,\Omega$ |

**(3) 60 Hz 下 $Z=100\,\Omega$**：$L=100/(2\pi\times 60)=0.265\,\text{H}$，$C=1/(2\pi\times 60\times 100)=26.5\,\mu\text{F}$。

### 9.2 — 交流电路中电感和电容的电流

**(1) $L=31.8\,\text{mH}$，$U=220\,\text{V}$，$f=50\,\text{Hz}$**：
$Z_L=2\pi\times 50\times 0.0318=10\,\Omega$，$I=220/10=22\,\text{A}$。

**(2) $C=79.6\,\mu\text{F}$，$U=220\,\text{V}$，$f=50\,\text{Hz}$**：
$Z_C=1/(2\pi\times 50\times 79.6\times 10^{-6})=40\,\Omega$，$I=220/40=5.5\,\text{A}$。

### 9.3 — RLC串联电路

$R=40\,\Omega$，$L=0.1\,\text{H}$，$C=50\,\mu\text{F}$，$f=50\,\text{Hz}$，$V_m=1\,\text{V}$。
$\omega=314\,\text{rad/s}$。$X_L=31.4\,\Omega$，$X_C=63.7\,\Omega$。
$$Z=40+j(31.4-63.7)=40-j32.3\,\Omega$$
$$|Z|=\sqrt{40^2+32.3^2}=51.4\,\Omega,\quad\varphi=-38.9^\circ$$
各元件电压峰值：$V_{mL}=0.611\,\text{V}$，$V_{mC}=1.24\,\text{V}$，$V_{mR}=0.778\,\text{V}$。

### 9.4 — 滤波电路

$C_1=C_2=10\,\mu\text{F}$，$f=1000\,\text{Hz}$，$\omega=6283\,\text{rad/s}$。
$$\frac{1/(\omega C_2)}{\sqrt{(\omega L)^2+[1/(\omega C_2)]^2}}=\frac{1}{10}$$
解得 $L\approx 28\,\text{mH}$。

### 9.5 — RLC电路功率

$V_{\text{rms}}=100\,\text{V}$。$\cos\varphi=R/|Z|=40/51.4=0.778$。
$I_{\text{rms}}=100/51.4=1.95\,\text{A}$，$I_m=2.75\,\text{A}$。
$P=V_{\text{rms}}I_{\text{rms}}\cos\varphi=152\,\text{W}$。

### 9.6 — RLC电路频率响应

$R=300\,\Omega$，$L=0.9\,\text{H}$，$C=2.0\,\mu\text{F}$，$V_m=50\,\text{V}$。

**(1) 阻抗**：
$\omega=500$：$Z=300+j(450-1000)=300-j550\,\Omega$，$|Z|=626\,\Omega$。
$\omega=1000$：$Z=300+j(900-500)=300+j400\,\Omega$，$|Z|=500\,\Omega$。

**(2) 谐振频率** $\omega_0=1/\sqrt{LC}=745\,\text{rad/s}$（$f_0=119\,\text{Hz}$）。电流先增大后减小。

**(3) $\omega=500$**：$\varphi=-61.4^\circ$（电流超前电压）。

**(4) 谐振时 $\cos\varphi=1$。

**(5) $R=100\,\Omega$** 时谐振频率不变，$I_{\text{rms}}=50/(\sqrt{2}\times 100)=0.354\,\text{A}$。

