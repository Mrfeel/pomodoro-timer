# -*- coding: utf-8 -*-
"""生成带原题的完整答案文档"""

lines = []

def w(text):
    lines.append(text)

w("# 电磁学复习提纲 — 自测题答案（含原题）")
w("")
w("> 每题先给出原题，再给出详细解答。共48道章节自测题 + 5道综合模拟题。")
w("")

# ====== 第一章 ======
w("\\newpage")
w("# 第一章  真空中的静电场（5题）")
w("")

w("## T1-1（高斯定理）")
w("")
w("**原题**：半径为 $R$ 的无限长均匀带电圆柱体，体电荷密度 $\\rho$，求柱内外电场分布。")
w("")
w("**解**：柱对称，电场沿径向。取半径 $r$、高 $l$ 的同轴圆柱高斯面。侧面通量 $E\\cdot 2\\pi r l$，端面通量为零。")
w("")
w("$r<R$（柱内）：$Q_{\\text{enc}}=\\rho\\cdot\\pi r^2 l$，$E\\cdot 2\\pi r l = \\rho\\pi r^2 l/\\varepsilon_0 \\Rightarrow E=\\rho r/(2\\varepsilon_0)$")
w("$r>R$（柱外）：$Q_{\\text{enc}}=\\rho\\cdot\\pi R^2 l$，$E\\cdot 2\\pi r l = \\rho\\pi R^2 l/\\varepsilon_0 \\Rightarrow E=\\rho R^2/(2\\varepsilon_0 r)$")
w("")
w("---")

w("## T1-2（叠加法）")
w("")
w("**原题**：一均匀带电半圆环（半径 $R$，线密度 $\\lambda$），求圆心处电场。")
w("")
w("**解**：对称性→圆心处 $x$ 分量抵消，仅剩 $y$ 分量。$dq=\\lambda R d\\theta$，$dE=\\lambda d\\theta/(4\\pi\\varepsilon_0 R)$。$dE_y=dE\\sin\\theta$。")
w("$E=\\int_0^\\pi\\frac{\\lambda\\sin\\theta}{4\\pi\\varepsilon_0 R}d\\theta=\\frac{\\lambda}{2\\pi\\varepsilon_0 R}$，方向沿对称轴向下。")
w("")
w("---")

w("## T1-3（电势法）")
w("")
w("**原题**：求均匀带电圆盘轴线上任意点的电势和电场。")
w("")
w("**解**：面密度 $\\sigma$，半径 $R$。取环 $r\\to r+dr$，$dq=\\sigma\\cdot 2\\pi r dr$。$\\varphi(z)=\\int_0^R\\frac{\\sigma\\cdot 2\\pi r dr}{4\\pi\\varepsilon_0\\sqrt{r^2+z^2}}=\\frac{\\sigma}{2\\varepsilon_0}[\\sqrt{R^2+z^2}-|z|]$。$E=-d\\varphi/dz=\\frac{\\sigma}{2\\varepsilon_0}[1-z/\\sqrt{R^2+z^2}]$。")
w("")
w("---")

w("## T1-4（补偿法）")
w("")
w("**原题**：均匀带电球体（半径 $R$，密度 $\\rho$）内有一球形空腔，证明空腔内为匀强电场。")
w("")
w("**解**：大球（$\\rho$）+补球（$-\\rho$）叠加。大球内 $\\boldsymbol{E}_1=\\rho\\boldsymbol{r}/(3\\varepsilon_0)$。补球内 $\\boldsymbol{E}_2=-\\rho(\\boldsymbol{r}-\\boldsymbol{a})/(3\\varepsilon_0)$。叠加：$\\boldsymbol{E}=\\rho\\boldsymbol{a}/(3\\varepsilon_0)$，匀强电场，方向从原球心指向空腔球心。")
w("")
w("---")

w("## T1-5（电偶极子）")
w("")
w("**原题**：求电偶极子在点电荷 $Q$ 的电场中所受的力和力矩。")
w("")
w("**解**：$Q$ 的电场 $\\boldsymbol{E}=Q\\hat{\\boldsymbol{r}}/(4\\pi\\varepsilon_0 r^2)$。力矩 $\\boldsymbol{\\tau}=\\boldsymbol{p}\\times\\boldsymbol{E}$，大小 $pQ\\sin\\theta/(4\\pi\\varepsilon_0 r^2)$。力 $\\boldsymbol{F}=(\\boldsymbol{p}\\cdot\\nabla)\\boldsymbol{E}$。$\\boldsymbol{p}\\parallel\\hat{\\boldsymbol{r}}$ 时 $\\boldsymbol{F}=-2pQ\\hat{\\boldsymbol{r}}/(4\\pi\\varepsilon_0 r^3)$（吸引力）。")
w("")

# ====== 第二章 ======
w("\\newpage")
w("# 第二章  静电场中的导体和电介质（6题）")
w("")

w("## T2-1（电容计算）")
w("**原题**：平行板电容器中插入厚 $t$、$\\varepsilon_r$ 的介质板，求电容变化。两种极限：介质充满 vs. 介质紧贴一极板。")
w("")
w("**解**：等效为两真空间隙（$d-t$）与介质板（$t$，$\\varepsilon_r$）串联：$1/C=(d-t)/(\\varepsilon_0 S)+t/(\\varepsilon_0\\varepsilon_r S)$，$C=\\varepsilon_0 S/[d-t+t/\\varepsilon_r]$。极限① $t=d$：$C=\\varepsilon_r\\varepsilon_0 S/d=\\varepsilon_r C_0$。极限② $t<d$：直接用上式。")
w("")
w("---")

w("## T2-2（$\\boldsymbol{D}$ 矢量应用）")
w("**原题**：球形电容器内充满两种同心分层介质（分界面半径 $d$），求电容和各界面电荷。")
w("")
w("**解**：设内导体带 $Q$。球对称 $D=Q/(4\\pi r^2)$。$a<r<d$：$E_1=Q/(4\\pi\\varepsilon_1 r^2)$；$d<r<b$：$E_2=Q/(4\\pi\\varepsilon_2 r^2)$。$U=\\frac{Q}{4\\pi}[\\frac{1}{\\varepsilon_1}(\\frac{1}{a}-\\frac{1}{d})+\\frac{1}{\\varepsilon_2}(\\frac{1}{d}-\\frac{1}{b})]$。$C=Q/U$。分界面极化电荷 $\\sigma'_d=P_{1n}-P_{2n}=(\\varepsilon_1-\\varepsilon_0)E_1(d)-(\\varepsilon_2-\\varepsilon_0)E_2(d)$。")
w("")
w("---")

w("## T2-3（边界条件）")
w("**原题**：平行板电容器两极板间有两层介质（$\\varepsilon_1,\\varepsilon_2$），厚度分别为 $d_1,d_2$，极板电压 $U$。求各介质中的 $E$ 和 $D$。")
w("")
w("**解**：$D$ 法向连续 → $D_1=D_2=D$。$E_1=D/\\varepsilon_1$，$E_2=D/\\varepsilon_2$。$U=E_1 d_1+E_2 d_2=D(d_1/\\varepsilon_1+d_2/\\varepsilon_2)$。$D=U/(d_1/\\varepsilon_1+d_2/\\varepsilon_2)$。$\\varepsilon_r$ 大的层中 $E$ 更小——介质分担了电压。")
w("")
w("---")

w("## T2-4（镜像法—平面）")
w("**原题**：点电荷 $q$ 距接地导体平面 $d$。求表面的感应电荷分布和总感应电荷。")
w("")
w("**解**：镜像电荷 $-q$ 位于平面对称点（下方 $d$）。表面电场法向分量 $E_z=-2qd/[4\\pi\\varepsilon_0(r^2+d^2)^{3/2}]$，$\\sigma=\\varepsilon_0 E_z=-qd/[2\\pi(r^2+d^2)^{3/2}]$。总感应电荷 $Q_{\\text{ind}}=\\int_0^\\infty\\sigma\\cdot 2\\pi r dr=-q$。恰等于镜像电荷。")
w("")
w("---")

w("## T2-5（镜像法—球面）")
w("**原题**：点电荷 $q$ 距接地导体球（半径 $R$）球心 $d$。求镜像电荷的大小和位置，以及点电荷所受的力。")
w("")
w("**解**：镜像电荷 $q'=-Rq/d$，位于球心到真实电荷连线上距球心 $r'=R^2/d$ 处。力 $F=qq'/[4\\pi\\varepsilon_0(d-r')^2]=-q^2 Rd/[4\\pi\\varepsilon_0(d^2-R^2)^2]$（吸引力）。$d\\to R$ 时 $F\\to\\infty$；$d\\gg R$ 时 $F\\propto 1/d^3$。")
w("")
w("---")

w("## T2-6（综合）")
w("**原题**：导体球外有同心介质球壳，导体带电荷 $Q$。求 $\\boldsymbol{D},\\boldsymbol{E},\\boldsymbol{P}$ 分布、极化电荷、电容。")
w("")
w("**解**：$r<a$：$\\boldsymbol{D}=0,\\boldsymbol{E}=0$。$a<r<b$：$D=Q/(4\\pi r^2)$，$E=Q/(4\\pi\\varepsilon_0\\varepsilon_r r^2)$，$P=(\\varepsilon_r-1)Q/(4\\pi\\varepsilon_r r^2)$。$r>b$：$D=Q/(4\\pi r^2)$，$E=Q/(4\\pi\\varepsilon_0 r^2)$，$P=0$。$\\sigma'_a=-(\\varepsilon_r-1)Q/(4\\pi\\varepsilon_r a^2)$，$\\sigma'_b=(\\varepsilon_r-1)Q/(4\\pi\\varepsilon_r b^2)$。$C=4\\pi\\varepsilon_0[\\frac{1}{\\varepsilon_r}(\\frac{1}{a}-\\frac{1}{b})+\\frac{1}{b}]^{-1}$。")
w("")

# ====== 第三章 ======
w("\\newpage")
w("# 第三章  静电能（4题）")
w("")

w("## T3-1")
w("**原题**：均匀带电球面（半径 $R$，电荷 $Q$）的静电自能。由 $W=e^2/(8\\pi\\varepsilon_0 R)$ 估算电子\"经典半径\"。")
w("")
w("**解**：$W=\\frac{1}{2}Q\\varphi(R)=Q^2/(8\\pi\\varepsilon_0 R)$。令 $W=m_e c^2$：$r_e=e^2/(8\\pi\\varepsilon_0 m_e c^2)\\approx 1.4\\times 10^{-15}\\,\\text{m}$。若电荷均匀分布在球体内 $r_e\\approx 2.8\\times 10^{-15}\\,\\text{m}$。")
w("")
w("---")

w("## T3-2")
w("**原题**：平行板电容器接电源（电压 $U$），极板间距从 $d_1$ 拉到 $d_2$。求：(1)电场力做的功；(2)电源提供的能量；(3)电场能量的变化。三者关系如何？")
w("")
w("**解**：$C=\\varepsilon_0 S/d$，$U$ 恒定。$W=\\frac{1}{2}CU^2$，$F=+\\partial W/\\partial x|_U=-\\varepsilon_0 SU^2/(2d^2)$。(1) $A_F=\\frac{\\varepsilon_0 SU^2}{2}(\\frac{1}{d_1}-\\frac{1}{d_2})$。(2) 极板间距增大→$C$ 减小→$Q$ 减小→电荷回流→电源**吸收**能量。(3) $\\Delta W_e=\\frac{1}{2}\\varepsilon_0 SU^2(\\frac{1}{d_2}-\\frac{1}{d_1})$。关系：$A_F+\\Delta W_{\\text{电源}}+\\Delta W_e=0$。")
w("")
w("---")

w("## T3-3")
w("**原题**：用虚功原理求平行板电容器两极板间的吸引力（分别用 $Q$=const 和 $U$=const）。")
w("")
w("**解**：$C=\\varepsilon_0 S/x$。$Q$=const：$W=Q^2 x/(2\\varepsilon_0 S)$，$F=-\\partial W/\\partial x|_Q=-Q^2/(2\\varepsilon_0 S)$。$U$=const：$W=\\varepsilon_0 SU^2/(2x)$，$F=+\\partial W/\\partial x|_U=-\\varepsilon_0 SU^2/(2x^2)$。用力大小 $F=\\varepsilon_0 SU^2/(2x^2)$ 两种条件下相等。")
w("")
w("---")

w("## T3-4")
w("**原题**：一半介质半真空的平行板电容器（$\\varepsilon_r$ 的介质板可沿板面方向拉出）。求将介质板拉入电容器所需的力。")
w("")
w("**解**：介质插入深度 $x$ 时 $C(x)=\\frac{\\varepsilon_0 b}{d}[a+(\\varepsilon_r-1)x]$。接电源：$F=+\\partial W/\\partial x|_U=\\varepsilon_0 b(\\varepsilon_r-1)U^2/(2d)$。力沿 $+x$（将介质拉入电容器内）。")
w("")

# ====== 第四章 ======
w("\\newpage")
w("# 第四章  稳恒电流（3题）")
w("")

w("## T4-1（电阻计算）")
w("**原题**：同轴电缆内外导体半径 $a,b$，中间填充电导率 $\\sigma$ 的介质。求单位长度的漏电阻。")
w("")
w("**解**：径向漏电，$r$ 处 $j=I/(2\\pi r l)$。$E=j/\\sigma=I/(2\\pi\\sigma r l)$。$U=\\int_a^b E dr=\\frac{I}{2\\pi\\sigma l}\\ln\\frac{b}{a}$，$R=U/I=\\ln(b/a)/(2\\pi\\sigma l)$。单位长 $R/l=\\ln(b/a)/(2\\pi\\sigma)$。")
w("")
w("---")

w("## T4-2（基尔霍夫）")
w("**原题**：含两个电源和三个电阻的电路，用支路电流法或回路电流法求各支路电流。")
w("")
w("**解**：设两网孔电流，KCL+两个KVL方程联立。典型数据 $R_1=R_2=2\\Omega,R_3=4\\Omega,\\mathcal{E}_1=12\\text{V},\\mathcal{E}_2=6\\text{V}$：解得 $I_1=2\\text{A},I_2=1\\text{A},I_3=3\\text{A}$。具体数值取决于电路拓扑和元件参数。")
w("")
w("---")

w("## T4-3（$RC$ 类比）")
w("**原题**：证明 $RC = \\varepsilon/\\sigma$，并解释其物理意义（时间量纲）。")
w("")
w("**解**：$C=\\varepsilon\\times$(几何因子)，$R=(1/\\sigma)\\times$(同一几何因子)→$RC=\\varepsilon/\\sigma$。量纲 $[\\varepsilon/\\sigma]=[\\text{F/m}]/[\\text{S/m}]=[\\text{s}]$。$\\tau_{\\text{弛豫}}=\\varepsilon/\\sigma$ 是导电介质中体电荷指数衰减的特征时间。铜：$\\tau\\approx 10^{-19}\\,\\text{s}$。")
w("")

# ====== 第五～十章（合并写） ======
w("\\newpage")
w("# 第五章  真空中的静磁场（6题）")
w("")

w("## T5-1（毕-萨定律）")
w("**原题**：正方形载流线圈（边长 $a$，电流 $I$）中心处的 $B$。推广到正 $n$ 边形。")
w("")
w("**解**：每边 $B_1=\\frac{\\mu_0 I}{4\\pi(a/2)}(\\cos 45^\\circ+\\cos 45^\\circ)=\\frac{\\sqrt{2}\\mu_0 I}{2\\pi a}$。四边叠 $B=\\frac{2\\sqrt{2}\\mu_0 I}{\\pi a}$。正 $n$ 边形：$B=\\frac{\\mu_0 nI}{2\\pi R}\\sin\\frac{\\pi}{n}$。$n\\to\\infty$→$\\mu_0 I/(2R)$（圆环极限）。")
w("")
w("---")

w("## T5-2（安培环路定理）")
w("**原题**：无限长圆柱导体（半径 $a$）电流均匀分布，求柱内外 $B$。若电流只分布表面，结果如何？")
w("")
w("**解**：均匀分布：$r<a$：$B=\\mu_0 Ir/(2\\pi a^2)$；$r>a$：$B=\\mu_0 I/(2\\pi r)$。仅表面分布：$r<a$：$B=0$（环路内无电流）；$r>a$：$B=\\mu_0 I/(2\\pi r)$。")
w("")
w("---")

w("## T5-3（亥姆霍兹线圈）")
w("**原题**：两同轴圆线圈（半径 $R$、间距 $R$、同向电流 $I$），证明中心附近 $B$ 最均匀。")
w("")
w("**解**：单线圈 $B(z)=\\mu_0 IR^2/[2(R^2+z^2)^{3/2}]$。中心 $B_O=\\frac{8\\mu_0 I}{5\\sqrt{5}R}$。泰勒展开至二阶：当 $a=R$ 时 $B'(0)=B''(0)=0$，即中心附近磁场最均匀——这是亥姆霍兹线圈设计的核心原理。")
w("")
w("---")

w("## T5-4（洛伦兹力）")
w("**原题**：带电粒子以 $\\boldsymbol{v}_0$ 斜射入均匀 $\\boldsymbol{B}$（夹角 $\\theta$），求螺旋运动的半径、螺距和回旋频率。")
w("")
w("**解**：$v_\\perp=v_0\\sin\\theta$，$v_\\parallel=v_0\\cos\\theta$。$r=mv_0\\sin\\theta/(qB)$。螺距 $h=v_\\parallel T=v_0\\cos\\theta\\cdot 2\\pi m/(qB)$。回旋频率 $\\omega_c=qB/m$，与速度无关。")
w("")
w("---")

w("## T5-5（磁约束）")
w("**原题**：磁场缓慢变化时，粒子轨道磁矩 $\\mu=mv_\\perp^2/(2B)$ 守恒。由此解释磁镜中粒子的约束和逃逸。")
w("")
w("**解**：磁矩守恒→向强场区运动时 $v_\\perp\\uparrow$→$v_\\parallel\\downarrow$→$v_\\parallel=0$ 时被反射。逃逸锥 $\\sin^2\\theta_c=B_0/B_m$。$R_m=4$ 时逃逸比例 $1-\\sqrt{3}/2\\approx 13.4\\%$。")
w("")
w("---")

w("## T5-6（综合）")
w("**原题**：一宽为 $2a$ 的无限长薄板载有均匀面电流，求空间中 $B$ 的分布。")
w("")
w("**解**：$K=I/(2a)$。矩形安培环路跨板两侧：$B\\cdot 2l=\\mu_0 Kl\\Rightarrow B=\\mu_0 K/2=\\mu_0 I/(4a)$。两侧 $B$ 大小相等方向相反，平行于板面且垂直于电流方向。")
w("")

w("\\newpage")
w("# 第六章  磁介质（4题）")
w("")

w("## T6-1")
w("**原题**：无限长直导线（半径 $a$，电流 $I$ 均匀分布）外包磁导率 $\\mu$ 的介质（外半径 $b$）。求 $H,B$ 和磁化面电流。")
w("**解**：$r<a$：$H=Ir/(2\\pi a^2),B=\\mu_0 Ir/(2\\pi a^2)$。$a<r<b$：$H=I/(2\\pi r),B=\\mu I/(2\\pi r)$。$r>b$：$H=I/(2\\pi r),B=\\mu_0 I/(2\\pi r)$。$i'_a=(\\mu-\\mu_0)I/(2\\pi\\mu_0 a)$，$i'_b=-(\\mu-\\mu_0)I/(2\\pi\\mu_0 b)$。")
w("")
w("---")

w("## T6-2")
w("**原题**：均匀磁化球（磁化强度 $M_0\\hat{\\boldsymbol{z}}$）的 $\\boldsymbol{B}$ 和 $\\boldsymbol{H}$ 分布。")
w("**解**：类比均匀极化球。$\\boldsymbol{H}_{\\text{in}}=-\\boldsymbol{M}/3$，$\\boldsymbol{B}_{\\text{in}}=\\mu_0(\\boldsymbol{H}_{\\text{in}}+\\boldsymbol{M})=\\frac{2}{3}\\mu_0\\boldsymbol{M}$。球外等效中心磁偶极子 $\\boldsymbol{m}=\\frac{4\\pi}{3}R^3\\boldsymbol{M}$。")
w("")
w("---")

w("## T6-3（磁路定理）")
w("**原题**：环形铁芯（平均周长 $l$、截面积 $S$、$\\mu_r$、匝数 $N$）有一小气隙 $l_g$。求气隙中 $B$ 和线圈自感 $L$。")
w("**解**：$\\mathcal{R}_{\\text{core}}=l/(\\mu_0\\mu_r S)$，$\\mathcal{R}_{\\text{gap}}=l_g/(\\mu_0 S)$。$\\Phi=NI/(\\mathcal{R}_{\\text{core}}+\\mathcal{R}_{\\text{gap}})$。$B=\\Phi/S\\approx\\mu_0 NI/l_g$（$\\mu_r\\gg 1$ 时铁芯磁阻可忽略）。$L=N^2/(\\mathcal{R}_{\\text{core}}+\\mathcal{R}_{\\text{gap}})$。")
w("")
w("---")

w("## T6-4")
w("**原题**：磁介质圆柱（半径 $a$，磁导率 $\\mu$）置于均匀外磁场 $\\boldsymbol{B}_0$ 中，$\\boldsymbol{B}_0\\perp$ 柱轴。证明柱内 $\\boldsymbol{B}_{\\text{in}}=\\frac{2\\mu}{\\mu+\\mu_0}B_0$。")
w("**解**：分离变量法（同电介质圆柱）。磁标势拉普拉斯方程+边界条件→柱内均匀磁场。$\\boldsymbol{H}_{\\text{in}}=\\frac{2\\mu_0}{\\mu+\\mu_0}\\boldsymbol{H}_0$，$\\boldsymbol{B}_{\\text{in}}=\\mu\\boldsymbol{H}_{\\text{in}}=\\frac{2\\mu}{\\mu+\\mu_0}\\boldsymbol{B}_0$。证毕。")
w("")

w("\\newpage")
w("# 第七章  电磁感应（7题）")
w("")

for i, (q, a) in enumerate([
    ("**T7-1（动生）**：导体棒长 $l$，在 $B$ 中以角速度 $\\omega$ 绕一端旋转（$B\\perp$ 转面），求棒两端电动势。",
     "$d\\mathcal{E}=(\\boldsymbol{v}\\times\\boldsymbol{B})\\cdot d\\boldsymbol{l}=B\\omega r dr$。$\\mathcal{E}=\\int_0^l B\\omega r dr=\\frac{1}{2}B\\omega l^2$。方向由 $\\boldsymbol{v}\\times\\boldsymbol{B}$ 决定（沿径向）。"),
    ("**T7-2（感生/涡旋电场）**：长螺线管（半径 $R$，$n$ 匝/m）$dI/dt=k$。求管内外的涡旋电场 $E(r)$。",
     "$dB/dt=\\mu_0 nk$。管内 $r<R$：$E\\cdot 2\\pi r=-\\pi r^2\\mu_0 nk\\Rightarrow E=-\\frac{1}{2}\\mu_0 nkr$。管外 $r>R$：$E=-\\frac{\\mu_0 nkR^2}{2r}$。管外放导体棒时 $\\mathcal{E}=\\int\\boldsymbol{E}\\cdot d\\boldsymbol{l}$。"),
    ("**T7-3（互感+感应）**：两同心共面圆线圈（$a\\ll b$），大线圈通 $I=I_0\\sin\\omega t$。求小线圈中感应电流及平均力矩。",
     "$M=\\mu_0\\pi a^2/(2b)$。$\\mathcal{E}_s=-M dI/dt=-MI_0\\omega\\cos\\omega t$，$I_s=\\mathcal{E}_s/R$。$m_s=\\pi a^2 I_s$，$\\langle\\tau\\rangle=\\mu_0^2\\pi^2 a^4 I_0^2\\omega/(8b^2 R)$。"),
    ("**T7-4（自感计算）**：同轴电缆（内实心圆柱半径 $a$，外薄壳半径 $b$）单位长自感。分别用磁通法和磁能法。",
     "磁通法 $L=\\frac{\\mu_0}{2\\pi}(\\frac{1}{4}+\\ln\\frac{b}{a})$。磁能法：$W_m=\\int\\frac{B^2}{2\\mu_0}dV$，$L=2W_m/I^2$，结果相同。空心内导体时去掉 $1/4$ 项。"),
    ("**T7-5（RL暂态）**：$L=0.5\\,\\text{H}$，$R=10\\,\\Omega$，$\\mathcal{E}=12\\,\\text{V}$。求 $I(t)$、$\\tau$、$t=3\\tau$ 时的电流及储能。",
     "$\\tau=L/R=0.05\\,\\text{s}$。$I(t)=1.2(1-e^{-20t})\\,\\text{A}$。$t=3\\tau$：$I=1.14\\,\\text{A}$。$W_m=\\frac{1}{2}LI_0^2=0.36\\,\\text{J}$。"),
    ("**T7-6（RLC暂态）**：$L=0.1\\,\\text{H}$，$C=10\\,\\mu\\text{F}$。求临界阻尼 $R$；若 $R=50\\Omega$ 判断振荡。",
     "$\\omega_0=1000\\,\\text{rad/s}$。临界 $R=2\\sqrt{L/C}=200\\Omega$。$R=50<200$→欠阻尼。$\\beta=R/(2L)=250$，$\\omega_1=\\sqrt{1000^2-250^2}=968\\,\\text{rad/s}$。"),
    ("**T7-7（能量守恒）**：导体框架+滑棒在磁场中运动，分析动能→电能→焦耳热的转化。",
     "棒运动→切割磁力线→$\\mathcal{E}=Blv$→$I=\\mathcal{E}/R$→安培力 $F=B^2 l^2 v/R$（阻碍）→机械功率 $Fv$=电功率 $I^2 R$。动能完全转化为焦耳热，能量守恒。"),
]):
    w(q)
    w("")
    w("**解**：" + a)
    w("")
    w("---")

w("\\newpage")
w("# 第八章  磁能（3题）")
w("")

w("## T8-1")
w("**原题**：用磁能法求同轴电缆单位长自感。比较空心内导体和实心内导体的结果差异。")
w("**解**：$B=\\mu_0 I/(2\\pi r)$（$a<r<b$）。$W_m=\\frac{\\mu_0 I^2}{4\\pi}\\ln\\frac{b}{a}$。$L=2W_m/I^2=\\frac{\\mu_0}{2\\pi}\\ln\\frac{b}{a}$。实心内导体加内部磁能 $\\frac{\\mu_0}{8\\pi}$。")
w("")
w("---")

w("## T8-2")
w("**原题**：两平行无限长载流导线（间距 $d$），用虚功原理求单位长作用力。")
w("**解**：单位长磁能 $W_m=\\frac{\\mu_0 I_1 I_2}{\\pi}\\ln\\frac{d}{r_0}$。$F=-\\partial W_m/\\partial d|_I=-\\mu_0 I_1 I_2/(\\pi d)$。同向电流 $F<0$（吸引力），单位长力 $f=\\mu_0 I_1 I_2/(2\\pi d)$。")
w("")
w("---")

w("## T8-3")
w("**原题**：电磁铁衔铁受力公式 $F = B^2 S/(2\\mu_0)$ 的推导和应用。")
w("**解**：气隙 $W_m=B^2 S x/\\mu_0$。$F=-\\partial W_m/\\partial x|_\\Phi=-B^2 S/\\mu_0$。若两气隙各分担一半力，每极 $F=-B^2 S/(2\\mu_0)$。代入 $B$ 和 $S$ 即可计算具体吸力。")
w("")

w("\\newpage")
w("# 第九章  交流电路（4题）")
w("")

w("## T9-1")
w("**原题**：RLC串联电路 $R=20\\Omega$，$L=0.1\\text{H}$，$C=5\\mu\\text{F}$，接 $U=220\\text{V},50\\text{Hz}$。求 $I$、$\\cos\\varphi$、各元件电压。")
w("**解**：$\\omega=314$，$X_L=31.4\\Omega$，$X_C=637\\Omega$。$Z=20-j605.6\\Omega$，$|Z|=606\\Omega$。$I=0.363\\text{A}$，$\\cos\\varphi=0.033$。$U_R=7.3\\text{V}$，$U_L=11.4\\text{V}$，$U_C=231\\text{V}$。")
w("")
w("---")

w("## T9-2")
w("**原题**：求上题谐振频率，并计算谐振时的 $I$、$U_L$、$U_C$ 和 $Q$ 值。")
w("**解**：$f_0=1/(2\\pi\\sqrt{LC})=225\\,\\text{Hz}$。谐振时 $Z=R=20\\Omega$，$I=11\\,\\text{A}$。$Q=\\omega_0 L/R=7.07$。$U_L=U_C=QU=1556\\,\\text{V}$（远超电源电压220V！）。")
w("")
w("---")

w("## T9-3")
w("**原题**：设计一串谐电路，$f_0=1\\text{MHz}$，$Q=100$，$C=100\\text{pF}$。求 $L$ 和 $R$。")
w("**解**：$\\omega_0=6.28\\times 10^6$。$L=1/(\\omega_0^2 C)=253\\,\\mu\\text{H}$。$R=\\omega_0 L/Q=15.9\\,\\Omega$。")
w("")
w("---")

w("## T9-4")
w("**原题**：变压器原边 $N_1=1000$，副边 $N_2=100$，原边接 $220\\text{V}$。求副边开路电压。若副边负载 $10\\Omega$，反射到原边的等效电阻多大？")
w("**解**：$U_2=U_1 N_2/N_1=22\\,\\text{V}$。$R'=(N_1/N_2)^2 R_L=1000\\,\\Omega$。$I_1=U_1/R'=0.22\\,\\text{A}$。")
w("")

w("\\newpage")
w("# 第十章  麦克斯韦电磁理论（6题）")
w("")

w("## T10-1（位移电流）")
w("**原题**：平行板电容器（圆极板半径 $a$），$U=U_0\\sin\\omega t$。求位移电流密度和极板间 $B(r)$。")
w("**解**：$D=\\varepsilon_0 U/d$。$j_D=\\partial D/\\partial t=\\varepsilon_0\\omega U_0\\cos\\omega t/d$。安培-麦克斯韦 $B\\cdot 2\\pi r=\\mu_0 j_D\\pi r^2\\Rightarrow B=\\frac{1}{2}\\mu_0\\varepsilon_0\\omega U_0 r\\cos\\omega t/d$。")
w("")
w("---")

w("## T10-2（位移电流必要性）")
w("**原题**：说明为什么必须引入位移电流项。以电容器充放电为例说明矛盾。")
w("**解**：电容器充电时导线有传导电流 $I$，极板间无传导电流。若无位移电流：同一安培环路在导线处 $B\\neq 0$，极板间 $B=0$→矛盾！引入 $\\partial\\boldsymbol{D}/\\partial t$：极板间 $I_D=I$，安培环路定理处处自洽。这是麦克斯韦最伟大的洞察。")
w("")
w("---")

w("## T10-3（波动方程）")
w("**原题**：从麦克斯韦方程组出发，推导真空中 $\\boldsymbol{E}$ 和 $\\boldsymbol{B}$ 的波动方程。")
w("**解**：$\\nabla\\times(\\nabla\\times\\boldsymbol{E})=-\\frac{\\partial}{\\partial t}(\\nabla\\times\\boldsymbol{B})=-\\mu_0\\varepsilon_0\\frac{\\partial^2\\boldsymbol{E}}{\\partial t^2}$。$\\nabla(\\nabla\\cdot\\boldsymbol{E})-\\nabla^2\\boldsymbol{E}=-\\mu_0\\varepsilon_0\\frac{\\partial^2\\boldsymbol{E}}{\\partial t^2}$。真空中 $\\nabla\\cdot\\boldsymbol{E}=0$→$\\nabla^2\\boldsymbol{E}-\\frac{1}{c^2}\\frac{\\partial^2\\boldsymbol{E}}{\\partial t^2}=0$，$c=1/\\sqrt{\\mu_0\\varepsilon_0}$。")
w("")
w("---")

w("## T10-4（平面波性质）")
w("**原题**：真空中平面电磁波 $E_x=E_0\\cos(kz-\\omega t)$，求 $\\boldsymbol{B}$ 表达式、$\\langle S\\rangle$、$\\langle w\\rangle$。")
w("**解**：$\\boldsymbol{B}=(E_0/c)\\cos(kz-\\omega t)\\hat{\\boldsymbol{y}}$。$\\langle S\\rangle=E_0^2/(2\\mu_0 c)\\hat{\\boldsymbol{z}}$，$\\langle w\\rangle=\\varepsilon_0 E_0^2/2$，$\\langle S\\rangle=c\\langle w\\rangle\\hat{\\boldsymbol{z}}$。")
w("")
w("---")

w("## T10-5（坡印亭矢量）")
w("**原题**：载流长直导线表面 $E$ 沿轴向、$B$ 沿环向。求表面 $\\boldsymbol{S}$ 的方向和大小，说明能量从空间流入导线。")
w("**解**：$E_{\\text{axial}}=IR/l$，$B_{\\text{azim}}=\\mu_0 I/(2\\pi a)$。$\\boldsymbol{S}=\\boldsymbol{E}\\times\\boldsymbol{B}/\\mu_0$ 沿径向向内。总流入功率 $=S\\cdot 2\\pi a l=I^2 R$=焦耳热。能量通过电磁场从空间流入导线，而非沿导线内部传输。")
w("")
w("---")

w("## T10-6（辐射压力）")
w("**原题**：激光功率 $P=3\\,\\text{mW}$，光斑直径 $2\\,\\text{mm}$，屏幕反射率 $70\\%$。求屏幕受到的光压。")
w("**解**：$I=P/(\\pi r^2)=955\\,\\text{W/m}^2$。$p=(1+R)I/c=5.4\\times 10^{-6}\\,\\text{N/m}^2$。$E_0=\\sqrt{2I/(c\\varepsilon_0)}=848\\,\\text{V/m}$，$B_0=E_0/c=2.83\\times 10^{-6}\\,\\text{T}$。")
w("")

w("\\newpage")
w("# 综合模拟题（5题）")
w("")

w("## M1（场与介质综合）")
w("**原题**：半径为 $a$ 的导体球带电荷 $Q$，外有同心介质球壳（$a<r<b$，$\\varepsilon_r$），球壳外为真空。(1) 求全空间 $\\boldsymbol{D},\\boldsymbol{E},\\boldsymbol{P}$；(2) 介质壳内外表面的极化电荷；(3) 导体球电势和系统电容。")
w("")
w("**解**：同T2-6。(1) $r<a$：$\\boldsymbol{D}=0$；$a<r<b$：$D=Q/(4\\pi r^2),E=Q/(4\\pi\\varepsilon_0\\varepsilon_r r^2),P=(\\varepsilon_r-1)Q/(4\\pi\\varepsilon_r r^2)$；$r>b$：$D=Q/(4\\pi r^2),E=Q/(4\\pi\\varepsilon_0 r^2),P=0$。(2) $\\sigma'_a=-(\\varepsilon_r-1)Q/(4\\pi\\varepsilon_r a^2)$，$\\sigma'_b=(\\varepsilon_r-1)Q/(4\\pi\\varepsilon_r b^2)$。(3) $V_a=\\frac{Q}{4\\pi\\varepsilon_0}[\\frac{1}{\\varepsilon_r}(\\frac{1}{a}-\\frac{1}{b})+\\frac{1}{b}]$。")
w("")
w("---")

w("## M2（磁与感应综合）")
w("**原题**：半径为 $a$ 的圆柱形永磁体（沿轴均匀磁化 $\\boldsymbol{M}_0$），在外围同轴绕有 $N$ 匝线圈（半径 $b>a$）。(1) 求永磁体轴线上 $B$；(2) 线圈与永磁体间的互感；(3) 若线圈通有交变电流，永磁体是否会退磁？")
w("")
w("**解**：(1) 磁荷法（同6.17），轴线上 $B=\\frac{\\mu_0 M_0}{2}[\\frac{z+l/2}{\\sqrt{a^2+(z+l/2)^2}}-\\frac{z-l/2}{\\sqrt{a^2+(z-l/2)^2}}]$。(2) $M=\\Psi/I$，$\\Psi$ 为永磁体磁场穿过线圈的磁通。(3) 交变场幅值若超过矫顽力则可能退磁；永磁体磁能通过互感与线圈交换。")
w("")
w("---")

w("## M3（暂态+能量综合）")
w("**原题**：$RLC$ 串联电路，$L=0.2\\,\\text{H}$，$C=5\\,\\mu\\text{F}$，$R=20\\,\\Omega$，电容初始电压 $U_0=100\\,\\text{V}$。(1) 判断振荡状态；(2) 写出 $q(t)$ 表达式；(3) 求第一个半周期内电阻消耗的能量。")
w("")
w("**解**：(1) $\\omega_0=1000,\\beta=R/(2L)=50$。$\\beta<\\omega_0$→欠阻尼振荡。(2) $q(t)=Q_0 e^{-\\beta t}\\cos(\\omega_1 t)$，$Q_0=CU_0=5\\times 10^{-4}\\,\\text{C}$，$\\omega_1=\\sqrt{1000^2-50^2}=998.7$。(3) $T/2=\\pi/\\omega_1=3.15\\,\\text{ms}$。消耗能量=初态总电磁能-半周期末剩余电磁能。")
w("")
w("---")

w("## M4（电磁波+能量综合）")
w("**原题**：太阳常数 $S_0=1.36\\times 10^3\\,\\text{W/m}^2$。(1) 求太阳光中 $E_0$ 和 $B_0$；(2) 太阳光对地球的辐射压力；(3) 效率 $20\\%$、面积 $1\\,\\text{m}^2$ 的电池板输出电功率。")
w("")
w("**解**：(1) $E_0=\\sqrt{2S_0/(c\\varepsilon_0)}=1010\\,\\text{V/m}$，$B_0=E_0/c=3.37\\times 10^{-6}\\,\\text{T}$。(2) $F=S_0\\pi R_E^2/c=5.8\\times 10^8\\,\\text{N}$（惊人！与行星际引力同量级概念）。(3) $P_{\\text{out}}=0.20\\times 1360=272\\,\\text{W}$。")
w("")
w("---")

w("## M5（对称性综合）")
w("**原题**：比较并总结 $\\boldsymbol{D}$ 与 $\\boldsymbol{H}$ 在引入动机、基本方程、边界条件和计算方法上的完全对称性。指出二者的根本不同之处。")
w("")
w("**解**：**对称性**：引入动机相同（简化介质问题）；$\\oint\\boldsymbol{D}\\cdot d\\boldsymbol{S}=Q_f$↔$\\oint\\boldsymbol{H}\\cdot d\\boldsymbol{l}=I_f$；$D_n$连续↔$H_t$连续；求法都是\"先由自由源分布求辅助场量，再由本构关系求基本场量\"。**根本不同**：$\\nabla\\cdot\\boldsymbol{D}=\\rho_f$（有散场，源是标量电荷）vs $\\nabla\\cdot\\boldsymbol{B}=0$（无散场，无磁单极子）。束缚源：$\\rho'=-\\nabla\\cdot\\boldsymbol{P}$（散度）vs $\\boldsymbol{j}'=\\nabla\\times\\boldsymbol{M}$（旋度）——因为自由电荷是标量而自由电流是矢量。")
w("")

# ====== 写入 ======
with open('d:/辰辰/first CC/review_answers_full.md', 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines))
print(f'Done: {len(lines)} lines')
