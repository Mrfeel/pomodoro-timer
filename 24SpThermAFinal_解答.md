# 2024春 热学(A) 期末考试参考答案与详细解答

> **试卷来源**: 回忆版，中国科学技术大学物理学院
> **考试时间**: 2024年6月16日（周日）14:30-16:30

---

## 一、选择题（15分，每题3分）

### 第1题

**题目**：在封闭系统经过一个不可逆的循环后，下列说法一定正确的是：
- A. 系统的熵增大
- B. 系统从外界吸收的热量大于系统对外界做的功
- C. 环境的熵增大
- D. 环境的内能减小

**答案：C**

**解析**：
- 熵是态函数，经过一个循环后系统回到初态，故 $\Delta S_{\text{系统}} = 0$，A错误。
- 对于不可逆循环，总熵增加原理要求 $\Delta S_{\text{总}} = \Delta S_{\text{系统}} + \Delta S_{\text{环境}} > 0$。
- 由于 $\Delta S_{\text{系统}} = 0$，必有 $\Delta S_{\text{环境}} > 0$。故C正确。
- 热力学第一定律：$\Delta U = Q - W = 0$（循环），故 $Q = W$。B说 $Q > W$（不严谨），无法确定与"不可逆"有必然联系。
- 环境的内能变化不确定（取决于具体过程），D错误。

---

### 第2题

**题目**：根据热力学第二定律，下列说法正确的是：
- A. 热量只能从高温物体传给低温物体，不能从低温物体传给高温物体。
- B. 功可以全部转化成热，热不能全部转化成功。
- C. 气体只能自由膨胀，不能自动收缩。
- D. 有规则运动的能量能转化成无规则运动的能量，无规则运动的能量不能转化成有规则运动的能量。

**答案：D**

**解析**：
- A错误：热量可以借助外界做功（如制冷机）从低温传向高温，只不过不能**自发地**传递。
- B错误：热可以全部转化成功（如理想气体等温膨胀），但不能在**循环过程**中不产生其他影响地把热全部变成功（开尔文表述）。
- C错误：气体可以被压缩（外界做功），不能**自发地**收缩。
- D正确：这是热力学第二定律的微观统计解释——有序运动可以变为无序运动，无序运动不能**自发**变为有序运动（熵增原理）。

---

### 第3题

**题目**：在温度 $T$ 下，分子质量为 $m$ 的理想气体，在 $x$ 方向上的速度分量的平方平均值 $\overline{v_x^2}$ 为：
- A. $\overline{v_x^2} = \sqrt{\frac{3kT}{m}}$
- B. $\overline{v_x^2} = \frac{1}{3}\sqrt{\frac{3kT}{m}}$
- C. $\overline{v_x^2} = \frac{3kT}{m}$
- D. $\overline{v_x^2} = \frac{kT}{m}$

**答案：D**

**解析**：
由能量均分定理，每个平动自由度的平均动能为 $\frac{1}{2}kT$：

$$\frac{1}{2}m\overline{v_x^2} = \frac{1}{2}kT$$

$$\overline{v_x^2} = \frac{kT}{m}$$

注意区别：$\overline{v^2} = \overline{v_x^2} + \overline{v_y^2} + \overline{v_z^2} = \frac{3kT}{m}$（C选项是总方均值，不是 $x$ 分量）。

---

### 第4题

**题目**：在温度 $T$ 下，一容器中装满了分子摩尔质量为 $\mu$ 的理想气体。在容器壁上开一面积为 $S$ 的小孔，测得一秒内流出气体的质量为 $M$，则容器的压强为：
- A. $\frac{M}{S}\sqrt{\frac{2\pi RT}{\mu}}$
- B. $\frac{M}{S}\sqrt{\frac{k_B T}{\mu}}$
- C. $\frac{M}{S}\sqrt{\frac{2\pi k_B T}{\mu}}$
- D. $\frac{2M}{S}\sqrt{\frac{k_B T}{\mu}}$

**答案：A**

**解析**：
泻流质量流率公式的推导：

单位时间通过单位面积小孔流出的分子数为 $\frac{1}{4}n\langle v \rangle$。

- 分子数密度：$n = p/(kT)$
- 平均速率：$\langle v \rangle = \sqrt{\frac{8kT}{\pi m}} = \sqrt{\frac{8RT}{\pi\mu}}$（其中 $m = \mu/N_A$）
- 每个分子质量：$m = \mu/N_A$

一秒内通过面积 $S$ 流出的质量：

$$M = S \cdot \frac{1}{4}n\langle v \rangle \cdot \frac{\mu}{N_A} = \frac{S}{4} \cdot \frac{p}{kT} \cdot \sqrt{\frac{8RT}{\pi\mu}} \cdot \frac{\mu}{N_A}$$

利用 $R = kN_A$：

$$M = \frac{Sp}{4kT} \cdot \sqrt{\frac{8RT}{\pi\mu}} \cdot \frac{\mu}{N_A} = \frac{Sp}{4} \cdot \sqrt{\frac{8\mu}{\pi RT N_A^2}} \cdot \frac{1}{\cdots}$$

更简洁地推导：

$$M = \frac{S}{4} \cdot \frac{p}{kT} \cdot \sqrt{\frac{8kT}{\pi m}} \cdot m = \frac{Sp}{4kT} \cdot \sqrt{\frac{8kTm}{\pi}}$$

$$M = \frac{Sp}{4} \cdot \sqrt{\frac{8m}{\pi kT}} = \frac{Sp}{4} \cdot \sqrt{\frac{8\mu}{\pi RT}}$$

解得：

$$p = \frac{4M}{S} \cdot \sqrt{\frac{\pi RT}{8\mu}} = \frac{M}{S} \cdot \sqrt{\frac{2\pi RT}{\mu}}$$

故选 **A**。

---

### 第5题

**题目**：晶体熔解的过程中，吸收的热量用于：
- A. 破坏空间结构，增大分子势能
- B. 破坏空间结构，增大分子动能
- C. 破坏空间结构，既增大分子动能也增大分子势能
- D. 破坏空间结构，既不增大分子动能也不增大分子势能

**答案：A**

**解析**：
- 晶体熔解过程是**等温等压**的相变过程。
- 温度不变 → 分子平均动能不变。
- 熔解热（潜热）全部用于**破坏晶格的空间点阵结构**，增加分子间的势能（克服分子间引力做功）。
- 故选A。

---

## 二、简答题（10分，每题5分）

### 第1题

**题目**：1mol的理想气体，分别经过等容、等压、绝热过程，使其温度升高10%，哪个过程气体最终状态的熵值最大，为什么？

**解答**：

**等压过程最终熵最大。**

**原因**：

对理想气体，熵变公式为：
- 等容过程：$dS = \frac{C_V}{T}dT$，$\Delta S_V = C_V \ln\frac{T_2}{T_1} = C_V \ln(1.1)$
- 等压过程：$dS = \frac{C_p}{T}dT$，$\Delta S_p = C_p \ln\frac{T_2}{T_1} = C_p \ln(1.1)$
- 可逆绝热过程：$dQ = 0$，$\Delta S_{\text{ad}} = 0$

由于三个过程的初态相同（初熵相同），且 $C_p > C_V > 0$：

$$\Delta S_p > \Delta S_V > \Delta S_{\text{ad}} = 0$$

故等压过程的终态熵值最大。

**物理图像**：等压过程升温时气体还需对外膨胀做功，需要吸收更多热量 → 熵变更大。而绝热过程是等熵的。

---

### 第2题

**题目**：液体的粘滞系数随温度的升高而减小，与气体呈现相反的变化趋势，为什么？

**解答**：

两种物态中粘滞性的微观机制不同：

**气体**：
- 粘滞性来源于**分子热运动导致的动量输运**（不同流速层之间的分子交换）。
- 温度升高 → 分子热运动速率增大 → 碰撞频率和动量交换增强 → 粘滞系数**增大**。
- 气体粘滞系数 $\eta \propto \sqrt{T}$（麦克斯韦理论）。

**液体**：
- 粘滞性主要来源于**分子间相互作用力**，分子相对运动需克服周围分子的"笼效应"。
- 温度升高 → 分子动能增大 → 更容易克服分子间势垒 → 分子更易流动 → 粘滞系数**减小**。
- 液体粘滞系数 $\eta \propto e^{E_a/(kT)}$（Arrhenius型），随温度升高指数衰减。

**总结**：气体的粘滞机制是动量传递，温度促进传递；液体的粘滞机制是分子束缚，温度帮助克服束缚。机制不同，趋势相反。

---

## 三、解答题（75分）

**常用常数**：$R = 8.314 \text{ J/mol·K}$，$k = 1.38 \times 10^{-23} \text{ J/K}$，$N_A = 6.022 \times 10^{23} \text{ mol}^{-1}$

**常用积分**：$I(n) = \int_0^\infty e^{-\alpha x^2} x^n dx$

$$I(0) = \frac{1}{2}\sqrt{\frac{\pi}{\alpha}}, \quad I(1) = \frac{1}{2\alpha}, \quad I(2) = \frac{1}{4}\sqrt{\frac{\pi}{\alpha^3}}, \quad I(3) = \frac{1}{2\alpha^2}, \quad I(4) = \frac{3}{8}\sqrt{\frac{\pi}{\alpha^5}}$$

---

### 第1题（约15分）

**题目**：已知各向同性的简单固体等压体膨胀系数 $\alpha$，等温压缩系数 $\beta$，利用简单固体的状态方程、热力学第一定律和 $(\partial U/\partial V)_T$ 的结果，对于简单固体，证明：

$$C_p - C_V = \frac{TV_0\alpha^2}{\beta}$$

**证明**：

#### 方法一：利用热力学恒等式

热力学基本恒等式：

$$C_p - C_V = -T\frac{(\partial V/\partial T)_p^2}{(\partial V/\partial p)_T}$$

定义体膨胀系数 $\alpha$ 和等温压缩系数 $\beta$：

$$\alpha = \frac{1}{V}\left(\frac{\partial V}{\partial T}\right)_p, \qquad \beta = -\frac{1}{V}\left(\frac{\partial V}{\partial p}\right)_T$$

则：
$$\left(\frac{\partial V}{\partial T}\right)_p = V\alpha, \qquad \left(\frac{\partial V}{\partial p}\right)_T = -V\beta$$

代入恒等式：

$$C_p - C_V = -T\frac{(V\alpha)^2}{-V\beta} = \frac{TV\alpha^2}{\beta}$$

对于固体，体积变化很小，$V \approx V_0$（参考态体积），故：

$$\boxed{C_p - C_V = \frac{TV_0\alpha^2}{\beta}}$$

#### 方法二：利用 $(\partial U/\partial V)_T$ 结果

另一热力学恒等式：

$$C_p - C_V = \left[p + \left(\frac{\partial U}{\partial V}\right)_T\right]\left(\frac{\partial V}{\partial T}\right)_p$$

对于简单固体，其状态方程为 $V = V_0(1 + \alpha T - \beta p)$（线性近似），由热力学关系：

$$\left(\frac{\partial U}{\partial V}\right)_T = T\left(\frac{\partial p}{\partial T}\right)_V - p$$

利用循环关系：
$$\left(\frac{\partial p}{\partial T}\right)_V = -\frac{(\partial V/\partial T)_p}{(\partial V/\partial p)_T} = \frac{V\alpha}{V\beta} = \frac{\alpha}{\beta}$$

故 $(\partial U/\partial V)_T = \frac{T\alpha}{\beta} - p$。

代入得：

$$C_p - C_V = \left[p + \frac{T\alpha}{\beta} - p\right] \cdot V\alpha = \frac{TV\alpha^2}{\beta} \approx \frac{TV_0\alpha^2}{\beta}$$

证毕。$\square$

---

### 第2题

**题目**：1mol 振动自由度被冻结的双原子分子，经历如下图所示的 ABCA 准静态循环过程。求：
1. A点气体的压强；
2. B点气体的方均根速率和C点方均根速率的比值；
3. 从B到C的过程中，气体的熵变；
4. 该循环的效率。

> **⚠️ 说明**：试卷中的 PV 图无法从PDF中完整提取。以下解答基于标准热学考题中常见的 ABCA 循环图进行推演。**考生应根据实际图示数值进行替换计算。**

#### 对图示的推断

根据对图像的OCR识别，图中标注了以下参数：
- 纵轴（压强 $P$）：$P_0$ 和 $2P_0$
- 横轴（体积 $V$）：$V_0$ 和 $3V_0$
- 等温线 $T_0$ 经过A点

由此推演循环的典型配置：

| 状态点 | 压强 | 体积 | 温度 |
|--------|------|------|------|
| A | $P_0$ | $V_0$ | $T_A = P_0V_0/R = T_0$ |
| B | $P_0$ | $3V_0$ | $T_B = 3P_0V_0/R = 3T_0$ |
| C | $2P_0$ | $V_0$ | $T_C = 2P_0V_0/R = 2T_0$ |

- **A→B**：等压膨胀（$P = P_0$）
- **C→A**：等容升压（$V = V_0$）
- **B→C**：直线过程

对于振动自由度冻结的双原子分子：
$$C_V = \frac{5}{2}R, \quad C_p = \frac{7}{2}R, \quad \gamma = \frac{7}{5}$$

#### (1) A点气体的压强

若图示中A点对应最低压强 $P_0$ 和最低体积 $V_0$，且等温线 $T_0$ 经过A点，由理想气体状态方程：

$$P_A = \frac{RT_0}{V_0}$$

**若 $T_0$ 和 $V_0$ 在图中已给出数值，则可直接代入计算。** 若仅给出 $T_0$（等温线标注），则 $P_A = RT_0/V_0$。

> 若题目意图是 $P_0, V_0$ 为已知符号量，则 **$P_A = P_0$**（直接从图中读取）。

#### (2) B点和C点方均根速率的比值

方均根速率：$v_{\text{rms}} = \sqrt{\frac{3RT}{M}}$（或 $v_{\text{rms}} = \sqrt{\frac{3kT}{m}}$）

对于同种气体，$M$ 相同，故 $v_{\text{rms}} \propto \sqrt{T}$：

$$\frac{v_{\text{rms},B}}{v_{\text{rms},C}} = \sqrt{\frac{T_B}{T_C}} = \sqrt{\frac{3T_0}{2T_0}} = \sqrt{\frac{3}{2}} \approx 1.225$$

> 具体比值取决于图中 $T_B$ 和 $T_C$ 的实际数值。此处基于推定值 $T_B = 3T_0$, $T_C = 2T_0$。

#### (3) 从B到C的过程中气体的熵变

B→C的熵变。对于理想气体，由初态 $(P_B, V_B, T_B)$ 到末态 $(P_C, V_C, T_C)$：

$$\Delta S_{B \to C} = C_V \ln\frac{T_C}{T_B} + R\ln\frac{V_C}{V_B}$$

代入推定值（$T_B=3T_0$, $T_C=2T_0$, $V_B=3V_0$, $V_C=V_0$）：

$$\Delta S_{B \to C} = \frac{5}{2}R \ln\frac{2T_0}{3T_0} + R\ln\frac{V_0}{3V_0}$$

$$= \frac{5}{2}R \ln\frac{2}{3} + R\ln\frac{1}{3}$$

$$= R\left(\frac{5}{2}\ln\frac{2}{3} + \ln\frac{1}{3}\right)$$

$$= R\left(\frac{5}{2}\ln 2 - \frac{5}{2}\ln 3 - \ln 3\right)$$

$$= R\left(\frac{5}{2}\ln 2 - \frac{7}{2}\ln 3\right) < 0$$

> 数值结果取决于图中B、C点的实际 $(P, V)$ 值。熵变可正可负，取决于具体路径。

**直接使用态函数计算**（对于直线路径需积分）：
若B→C为直线 $P = kV + b$，则需积分 $dS = \frac{C_V}{T}dT + \frac{P}{T}dV$ 或 $dS = \frac{C_p}{T}dT - \frac{V}{T}dP$。对于理想气体，只需知道初末态即可（熵是态函数）。

#### (4) 该循环的效率

$$\eta = \frac{W_{\text{净}}}{Q_{\text{吸}}}$$

**净功** $W_{\text{净}}$ = PV图上循环包围的面积：

若ABCA构成三角形，面积为：
$$W_{\text{净}} = \frac{1}{2}(V_B - V_A)(P_C - P_A) = \frac{1}{2}(2V_0)(P_0) = P_0V_0 = RT_0$$

（此处以推定值为例，实际依图计算）

**吸热过程分析**：
- A→B（等压膨胀，$\Delta T > 0$）：$Q_{AB} = C_p\Delta T = \frac{7}{2}R \cdot 2T_0 = 7RT_0$（吸热）
- B→C：需分析是否吸热（部分可能放热）
- C→A（等容升压，$\Delta T > 0$）：$Q_{CA} = C_V\Delta T = \frac{5}{2}R \cdot (-T_0)$（放热，因温度降低）

> **请根据实际图示数值进行具体计算。** 一般做法为：
> 1. 计算各过程的功和热量
> 2. 判断哪些过程吸热、哪些放热
> 3. $\eta = W_{\text{净}} / \sum Q_{\text{吸}}$

---

### 第3题（约15分）

**题目**：已知一根长为 $L$ 的橡皮筋，其张力 $X$ 与温度的关系满足 $X = A(L)T$，其中 $A(L)$ 恒为正，橡皮筋满足热力学第一定律 $dU = TdS + XdL$，证明：
1. 橡皮筋的内能只与温度有关，与橡皮筋的长度无关；
2. 缓慢地等温拉长橡皮筋，橡皮筋的熵增加；
3. 缓慢地绝热拉长橡皮筋，橡皮筋的温度升高。

**证明**：

#### (1) 内能只与温度有关

引入**亥姆霍兹自由能**：$F = U - TS$

$$dF = dU - TdS - SdT = (TdS + XdL) - TdS - SdT = XdL - SdT$$

$F$ 的自然变量是 $(T, L)$。由全微分条件：

$$X = \left(\frac{\partial F}{\partial L}\right)_T, \quad S = -\left(\frac{\partial F}{\partial T}\right)_L$$

**麦克斯韦关系**（由 $\partial^2 F/\partial L\partial T = \partial^2 F/\partial T\partial L$）：

$$\left(\frac{\partial X}{\partial T}\right)_L = -\left(\frac{\partial S}{\partial L}\right)_T$$

由 $X = A(L)T$，得 $(\partial X/\partial T)_L = A(L)$，故：

$$\left(\frac{\partial S}{\partial L}\right)_T = -A(L)$$

现在计算 $(\partial U/\partial L)_T$：

$$dU = TdS + XdL$$

$$\left(\frac{\partial U}{\partial L}\right)_T = T\left(\frac{\partial S}{\partial L}\right)_T + X = -TA(L) + A(L)T = 0$$

$(\partial U/\partial L)_T = 0$ 说明在等温条件下 $U$ 不随 $L$ 变化。又 $(\partial U/\partial T)_L = C_L$（长度不变时的热容），故 $U$ 仅是 $T$ 的函数。

**结论**：$\boxed{U = U(T)}$，与 $L$ 无关。$\square$

#### (2) 等温拉长时熵的变化

由上述推导，$(\partial S/\partial L)_T = -A(L)$。

等温拉伸 $(dL > 0)$：
$$dS = \left(\frac{\partial S}{\partial L}\right)_T dL = -A(L)\, dL$$

由于 $A(L) > 0$，$dL > 0$，故 $dS = -A(L)dL < 0$。

> **数学结果**：等温拉伸时橡皮筋的熵**减小**（$dS < 0$）。
>
> **物理解释**：拉伸使高分子链段沿拉伸方向取向，系统更有序 → 熵减小。这与橡胶的**Gough-Joule效应**（受热收缩）一致：等温拉伸释放热量。
>
> ⚠️ **注意**：此结论与题干所述"熵增加"相反。经严格推导，在 $dU = TdS + XdL$ 的约定下（外界对系统做功为正），等温拉伸导致熵减小。若题中采用 $dU = TdS - XdL$ 约定，则结论相反。本解答采用题目给定约定。

#### (3) 绝热拉长时温度的变化

对于绝热可逆过程（$dS = 0$）：

$$dS = \left(\frac{\partial S}{\partial T}\right)_L dT + \left(\frac{\partial S}{\partial L}\right)_T dL = 0$$

$$\frac{C_L}{T}dT + [-A(L)]dL = 0$$

$$\frac{dT}{dL} = \frac{T A(L)}{C_L}$$

由于 $A(L) > 0$，$C_L > 0$，$T > 0$：

$$\frac{dT}{dL} = \frac{TA(L)}{C_L} > 0$$

**结论**：$\boxed{\text{绝热拉伸时温度升高}}$。$\square$

**物理图像**：绝热拉伸时外界对橡皮筋做功，熵不能减少（绝热可逆），这部分功转化为内能使温度升高。

---

### 第4题

**题目**：两种气体混合后在一密闭容器中达到平衡，温度为 $T$。气体1分子的质量为 $m$，气体2分子的质量为 $2m$，气体2的密度为气体1的一半，求：
1. 混合气体分子的速率分布；
2. 在容器壁上开一小孔使气体分子流出，极短时间后封闭小孔。泄流出的气体分子流入新的容器中并达到平衡，求新的气体的速率分布。

**解答**：

#### 已知条件整理

设气体1的分子数密度为 $n_1$，气体2的为 $n_2$。

密度关系：$\rho_2 = \frac{1}{2}\rho_1$

$$\rho_1 = n_1 m, \quad \rho_2 = n_2 \cdot (2m) = 2n_2 m$$

$$2n_2 m = \frac{1}{2} n_1 m \quad \Rightarrow \quad n_2 = \frac{n_1}{4}$$

总分子数密度：$n = n_1 + n_2 = \frac{5}{4}n_1$

#### (1) 混合气体的速率分布

平衡态下每种气体各自满足麦克斯韦速率分布。混合气体的速率分布为两分布的加权叠加。

麦克斯韦速率分布函数：$f(v)dv = 4\pi n \left(\frac{m}{2\pi kT}\right)^{3/2} v^2 e^{-mv^2/(2kT)} dv$

**气体1**（质量 $m$，密度 $n_1$）：

$$f_1(v)dv = 4\pi n_1 \left(\frac{m}{2\pi kT}\right)^{3/2} v^2 e^{-mv^2/(2kT)} dv$$

**气体2**（质量 $2m$，密度 $n_2 = n_1/4$）：

$$f_2(v)dv = 4\pi \cdot \frac{n_1}{4} \left(\frac{2m}{2\pi kT}\right)^{3/2} v^2 e^{-2mv^2/(2kT)} dv$$

$$= \pi n_1 \left(\frac{2m}{2\pi kT}\right)^{3/2} v^2 e^{-mv^2/(kT)} dv$$

$$= \pi n_1 \cdot \frac{2\sqrt{2}}{(2\pi kT)^{3/2}} \cdot m^{3/2} \cdot v^2 e^{-mv^2/(kT)} dv$$

总分布：

$$\boxed{f(v)dv = 4\pi v^2 \left[n_1\left(\frac{m}{2\pi kT}\right)^{3/2} e^{-mv^2/(2kT)} + \frac{n_1}{4}\left(\frac{2m}{2\pi kT}\right)^{3/2} e^{-mv^2/kT}\right]dv}$$

以总数密度 $n = \frac{5}{4}n_1$ 归一化表示：$n_1 = \frac{4}{5}n$

$$f(v)dv = 4\pi n v^2 \left[\frac{4}{5}\left(\frac{m}{2\pi kT}\right)^{3/2} e^{-mv^2/(2kT)} + \frac{1}{5}\left(\frac{2m}{2\pi kT}\right)^{3/2} e^{-mv^2/kT}\right]dv$$

#### (2) 泄流后新容器中的速率分布

泻流分子数流率与平均速率成正比。对于物种 $i$：

$$\Phi_i = \frac{1}{4}n_i \langle v_i \rangle$$

两种气体平均速率之比：
$$\langle v_1 \rangle = \sqrt{\frac{8kT}{\pi m}}, \quad \langle v_2 \rangle = \sqrt{\frac{8kT}{\pi \cdot 2m}} = \frac{\langle v_1 \rangle}{\sqrt{2}}$$

极短时间内泻流出的分子数之比：

$$\frac{N_1'}{N_2'} = \frac{\Phi_1}{\Phi_2} = \frac{n_1 \langle v_1 \rangle}{n_2 \langle v_2 \rangle} = \frac{n_1 \cdot \langle v_1 \rangle}{(n_1/4) \cdot (\langle v_1 \rangle/\sqrt{2})} = 4\sqrt{2}$$

泻流气体在新容器中重新达到平衡（温度仍为 $T$），新的分子数密度比：

$$n_1' : n_2' = 4\sqrt{2} : 1$$

新混合气体中气体1的占比：
$$x_1 = \frac{4\sqrt{2}}{4\sqrt{2} + 1} = \frac{4\sqrt{2}}{1 + 4\sqrt{2}}$$

新气体中气体2的占比：
$$x_2 = \frac{1}{1 + 4\sqrt{2}}$$

**新容器中的速率分布**（同样温度 $T$ 下的麦克斯韦分布加权叠加）：

$$\boxed{f_{\text{new}}(v)dv = 4\pi n' v^2 \left[x_1\left(\frac{m}{2\pi kT}\right)^{3/2} e^{-mv^2/(2kT)} + x_2\left(\frac{2m}{2\pi kT}\right)^{3/2} e^{-mv^2/kT}\right]dv}$$

其中 $n'$ 为新容器中的总分子数密度，$x_1 = \frac{4\sqrt{2}}{1+4\sqrt{2}}$，$x_2 = \frac{1}{1+4\sqrt{2}}$。

> **物理本质**：由于气体1分子较轻（平均速率大），在泻流中优先流出，导致新容器中轻分子的比例 $x_1 > 4/5$（原容器中比例），即**泻流具有同位素分离效应**。

---

### 第5题

**题目**：1mol 气体满足 Clausius 状态方程：

$$p = \frac{RT}{v - b} - \frac{a}{T(v + c)^2}$$

求：
1. 气体的临界摩尔体积 $v_c$、临界温度 $T_c$、临界压强 $p_c$ 和临界系数 $\frac{RT_c}{p_c v_c}$；
2. 不同种类的 Clausius 气体在临界状态时的性质是否相同，为什么？

**解答**：

#### (1) 临界参数的求解

临界点由以下方程组确定：

$$\left(\frac{\partial p}{\partial v}\right)_T = 0, \qquad \left(\frac{\partial^2 p}{\partial v^2}\right)_T = 0$$

**一阶导数**：

$$\frac{\partial p}{\partial v} = -\frac{RT}{(v-b)^2} + \frac{2a}{T(v+c)^3}$$

令其为零（在临界点处）：

$$\frac{RT_c}{(v_c - b)^2} = \frac{2a}{T_c(v_c + c)^3} \tag{1}$$

**二阶导数**：

$$\frac{\partial^2 p}{\partial v^2} = \frac{2RT}{(v-b)^3} - \frac{6a}{T(v+c)^4}$$

令其为零：

$$\frac{2RT_c}{(v_c - b)^3} = \frac{6a}{T_c(v_c + c)^4}$$

化简得：
$$\frac{RT_c}{(v_c - b)^3} = \frac{3a}{T_c(v_c + c)^4} \tag{2}$$

**(2) ÷ (1)**：

$$\frac{RT_c/(v_c-b)^3}{RT_c/(v_c-b)^2} = \frac{3a/[T_c(v_c+c)^4]}{2a/[T_c(v_c+c)^3]}$$

$$\frac{1}{v_c - b} = \frac{3}{2(v_c + c)}$$

$$2(v_c + c) = 3(v_c - b)$$

$$2v_c + 2c = 3v_c - 3b$$

$$\boxed{v_c = 3b + 2c}$$

**求 $T_c$**：由(1)式得 $RT_c^2 = \frac{2a(v_c - b)^2}{(v_c + c)^3}$

代入 $v_c - b = 2(b + c)$，$v_c + c = 3(b + c)$：

$$RT_c^2 = \frac{2a \cdot 4(b+c)^2}{27(b+c)^3} = \frac{8a}{27(b+c)}$$

$$\boxed{T_c = \sqrt{\frac{8a}{27R(b+c)}}}$$

**求 $p_c$**：将 $v_c$ 和 $T_c$ 代入状态方程：

$$p_c = \frac{RT_c}{v_c - b} - \frac{a}{T_c(v_c + c)^2}$$

分别计算：

$$\frac{RT_c}{v_c - b} = \frac{\sqrt{\frac{8aR}{27(b+c)}}}{2(b+c)} = \sqrt{\frac{2aR}{27(b+c)^3}}$$

$$\frac{a}{T_c(v_c + c)^2} = \frac{a}{\sqrt{\frac{8a}{27R(b+c)}} \cdot 9(b+c)^2} = \sqrt{\frac{aR}{24(b+c)^3}}$$

$$p_c = \sqrt{\frac{aR}{(b+c)^3}} \left(\sqrt{\frac{2}{27}} - \sqrt{\frac{1}{24}}\right)$$

$$\sqrt{\frac{2}{27}} - \sqrt{\frac{1}{24}} = \frac{\sqrt{48} - \sqrt{27}}{\sqrt{648}} = \frac{4\sqrt{3} - 3\sqrt{3}}{18\sqrt{2}} = \frac{\sqrt{3}}{18\sqrt{2}}$$

更简洁地：

$$\boxed{p_c = \sqrt{\frac{aR}{216(b+c)^3}}}$$

**求临界系数**：

$$\frac{RT_c}{p_c v_c} = \frac{\sqrt{\frac{8aR}{27(b+c)}}}{\sqrt{\frac{aR}{216(b+c)^3}} \cdot (3b + 2c)}$$

$$= \frac{\sqrt{\frac{8aR}{27(b+c)}} \cdot \sqrt{\frac{216(b+c)^3}{aR}}}{3b + 2c}$$

$$= \frac{\sqrt{\frac{8 \times 216}{27} (b+c)^2}}{3b + 2c} = \frac{\sqrt{64(b+c)^2}}{3b + 2c}$$

$$\boxed{\frac{RT_c}{p_c v_c} = \frac{8(b+c)}{3b + 2c}}$$

#### (2) 不同 Clausius 气体临界性质是否相同？

**不相同。**

**原因**：

Clausius 方程的临界系数为：

$$K_c = \frac{RT_c}{p_c v_c} = \frac{8(b+c)}{3b + 2c} = \frac{8(1 + c/b)}{3 + 2c/b}$$

该系数依赖于参数比 $c/b$，而非普适常数。

- 当 $c = 0$ 时，$K_c = 8/3 \approx 2.667$（退化为类似范德瓦尔斯的结果）
- 当 $c \neq 0$ 时，$K_c \neq 8/3$

这不同于**范德瓦尔斯方程**（$K_c^{\text{vdW}} = 8/3 \approx 2.667$，对所有气体相同），也不同于**理想气体**（$K_c^{\text{ideal}} = 1$）。

**物理本质**：不同的 Clausius 气体有不同的 $a, b, c$ 参数，反映了不同的分子间相互作用（$a$ 为吸引项系数，$b$ 为排斥体积，$c$ 为修正参数）。$K_c$ 依赖于 $c/b$，不同气体的 $c/b$ 不同，导致临界系数不同。这更接近真实气体的情况（真实气体的临界系数在 3.0~4.5 之间变化）。

---

### 第6题

**题目**：在地幔某深度下存在熔岩和岩石的交界面，此处岩石熔点为 $1300^\circ\text{C}$，熔岩和岩石的密度比 $\rho_l/\rho_s$ 约为 0.9，该界面处的重力加速度为 $9.8 \text{ m/s}^2$，岩石熔解的潜热为 $4.18 \times 10^5 \text{ J/kg}$，求：高度降低 1km 后岩石的熔点变化多少。

**解答**：

#### 物理模型

使用**克拉珀龙方程**（Clausius-Clapeyron equation）描述固-液相变的 $P$-$T$ 关系：

$$\frac{dP}{dT} = \frac{L}{T \Delta v}$$

其中：
- $L$：单位质量的熔解潜热
- $\Delta v = v_l - v_s = \frac{1}{\rho_l} - \frac{1}{\rho_s}$：单位质量熔解时的体积变化

#### 计算步骤

**第一步**：计算 $\Delta v$

$$\rho_l = 0.9\rho_s$$

$$v_l = \frac{1}{\rho_l} = \frac{1}{0.9\rho_s} = \frac{10}{9\rho_s}$$

$$v_s = \frac{1}{\rho_s}$$

$$\Delta v = v_l - v_s = \frac{10}{9\rho_s} - \frac{1}{\rho_s} = \frac{1}{9\rho_s}$$

由于 $\rho_l < \rho_s$（熔岩密度小于岩石），$\Delta v > 0$。这与大多数物质一致（液相密度通常小于固相，水除外）。

**第二步**：由克拉珀龙方程求 $\frac{dT}{dP}$

$$\frac{dT}{dP} = \frac{T \Delta v}{L} = \frac{T}{L} \cdot \frac{1}{9\rho_s}$$

$$T_m = 1300^\circ\text{C} = 1300 + 273 = 1573 \text{ K}$$

$$\frac{dT}{dP} = \frac{1573}{4.18 \times 10^5} \cdot \frac{1}{9\rho_s} = \frac{1573}{9 \times 4.18 \times 10^5 \rho_s}$$

**第三步**：高度降低 1km 对应的压强变化

深度增加 → 压强增大。使用流体静力学公式：
$$\Delta P = \rho_s g \Delta h$$

其中 $\Delta h = 1 \text{ km} = 1000 \text{ m}$（高度降低，$\Delta h$ 取正值表示深度增加）。

$$\Delta P = \rho_s \times 9.8 \times 1000 = 9800 \rho_s \text{ Pa}$$

**第四步**：熔点变化

$$\Delta T = \frac{dT}{dP} \cdot \Delta P = \frac{1573}{9 \times 4.18 \times 10^5 \rho_s} \cdot 9800 \rho_s$$

注意 $\rho_s$ 恰好约掉！

$$\Delta T = \frac{1573 \times 9800}{9 \times 4.18 \times 10^5}$$

$$= \frac{1.54154 \times 10^7}{3.762 \times 10^6}$$

$$= 4.10 \text{ K} \approx 4.1^\circ\text{C}$$

#### 结论

$$\boxed{\Delta T_m \approx 4.1^\circ\text{C}}$$

**高度降低 1km（即深度增加 1km）后，岩石的熔点升高约 4.1°C。**

#### 物理讨论

- $\Delta v > 0$（熔化时体积膨胀）→ $\frac{dT}{dP} > 0$ → 压强增大时熔点**升高**。
- 地幔越深处压强越大，岩石熔点越高，这与地球内部的地温曲线和熔融曲线共同决定了熔岩与岩石交界面的深度。
- 结果中 $\rho_s$ 恰好约掉，说明熔点变化与岩石的具体密度无关，只与密度比、潜热和重力加速度有关。这是量纲分析的优美结果。

---

## 附录：常用公式汇总

| 公式 | 表达式 | 说明 |
|------|--------|------|
| 热力学恒等式 | $C_p - C_V = T\left(\frac{\partial p}{\partial T}\right)_V\left(\frac{\partial V}{\partial T}\right)_p$ | 普适 |
| 麦克斯韦速率分布 | $f(v) = 4\pi n\left(\frac{m}{2\pi kT}\right)^{3/2}v^2e^{-mv^2/(2kT)}$ | 3D |
| 泻流通量 | $\Phi = \frac{1}{4}n\langle v \rangle$ | 单位面积 |
| 平均速率 | $\langle v \rangle = \sqrt{\frac{8kT}{\pi m}}$ | MB分布 |
| 克拉珀龙方程 | $\frac{dP}{dT} = \frac{L}{T\Delta v}$ | 一级相变 |
| 临界点条件 | $\left(\frac{\partial p}{\partial v}\right)_T = \left(\frac{\partial^2 p}{\partial v^2}\right)_T = 0$ | — |

---

> **说明**：
> 1. 第2题因试卷中PV图无法清晰提取，解答基于对图像中数值的OCR识别（$P_0, 2P_0, V_0, 3V_0, T_0$）进行了合理推定。**请以实际试卷中的图示数值为准进行替换计算。**
> 2. 第3题第(2)问：在 $dU = TdS + XdL$ 约定下，数学推导得出等温拉伸时熵**减小**而非增加。这可能是因为"回忆版"试题表述与原始试卷有出入，或是采用不同符号约定。解答按照题目给定的基本方程严格推导，并在文中说明了此差异。
> 3. 如发现任何错误或有疑问，请通过 yuhongfei@mail.ustc.edu.cn 联系试卷整理者。

---

*解答完成日期：2026年6月28日*
