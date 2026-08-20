# Mayer 公式 $C_{p,m} - C_{V,m} = R$ 解读

> 杨思辰 · 未来技术学院 · 物理学专业 | 2026-06-27

---

## 一、公式中各符号的含义

| 符号 | 全称 | 含义 |
|------|------|------|
| $C_{p,m}$ | 摩尔定压热容 | 1 mol 气体在**压强不变**的条件下，温度升高 1 K 所吸收的热量 |
| $C_{V,m}$ | 摩尔定容热容 | 1 mol 气体在**体积不变**的条件下，温度升高 1 K 所吸收的热量 |
| $R$ | 普适气体常量 | $8.314\ \text{J/(mol·K)}$ |

$$\boxed{C_{p,m} - C_{V,m} = R}$$

---

## 二、物理意义：为什么 $C_{p,m}$ 比 $C_{V,m}$ 大 $R$？

### 核心思想

在两种过程中，气体吸收的热量去向不同：

| 过程 | 吸热 $Q$ 的去向 |
|------|-----------------|
| **等容升温** | 全部用于**增加内能** $\Delta U$（气体不做功） |
| **等压升温** | 一部分用于**增加内能** $\Delta U$，另一部分用于**对外做膨胀功** $p\Delta V$ |

### 用公式说明

由热力学第一定律：$\delta Q = \mathrm{d}U + p\mathrm{d}V$

**等容过程**（$\mathrm{d}V = 0$）：

$$C_{V,m} = \left(\frac{\delta Q}{\mathrm{d}T}\right)_V = \left(\frac{\partial U_m}{\partial T}\right)_V$$

全部热量转为内能，不做功。

**等压过程**（$\mathrm{d}p = 0$）：

$$C_{p,m} = \left(\frac{\delta Q}{\mathrm{d}T}\right)_p = \left(\frac{\partial U_m}{\partial T}\right)_p + p\left(\frac{\partial V_m}{\partial T}\right)_p$$

热量 = 内能增加 + 膨胀功。

### 两者的差值

对于理想气体：
- $\left(\frac{\partial U_m}{\partial T}\right)_V = \left(\frac{\partial U_m}{\partial T}\right)_p$（理想气体内能 $U$ 仅依赖于 $T$，与 $V$、$p$ 无关——**焦耳定律**）
- $p\left(\frac{\partial V_m}{\partial T}\right)_p = p \cdot \frac{R}{p} = R$（由 $pV_m = RT$，等压下 $\mathrm{d}V_m/\mathrm{d}T = R/p$）

因此：

$$C_{p,m} - C_{V,m} = \frac{\mathrm{d}U_m}{\mathrm{d}T} + R - \frac{\mathrm{d}U_m}{\mathrm{d}T} = R$$

> **一句话总结：$C_{p,m}$ 比 $C_{V,m}$ 多出的 $R$，正是等压过程中 1 mol 气体升温 1 K 时对外做的膨胀功。**

---

## 三、图解对比

```
等容升温（V = const）：
┌──────────┐
│  气体    │ ← 加热 Q_V
│  V 不变  │   全部转为内能 ΔU
└──────────┘   不做功 W = 0

等压升温（p = const）：
┌──────────┐
│  气体 ⟶  │ ← 加热 Q_p
│  活塞外移 │   ① 增加内能 ΔU
└──────────┘   ② 推动活塞做功 pΔV

Q_p = Q_V + pΔV = Q_V + R（每 mol 每 K）
```

---

## 四、由 Mayer 公式推出的结论

### 4.1 定容热容只取决于分子自由度

对于理想气体，$U_m = \frac{i}{2}RT$（$i$ 为有效自由度数），因此：

$$\boxed{C_{V,m} = \frac{i}{2}R}$$

| 分子类型 | 自由度 $i$ | $C_{V,m}$ | $C_{p,m} = C_{V,m} + R$ |
|----------|:---------:|:---------:|:------------------------:|
| 单原子 | 3 | $\frac{3}{2}R$ | $\frac{5}{2}R$ |
| 刚性双原子 | 5 | $\frac{5}{2}R$ | $\frac{7}{2}R$ |
| 刚性多原子 | 6 | $3R$ | $4R$ |
| 非刚性双原子 | 7 | $\frac{7}{2}R$ | $\frac{9}{2}R$ |

### 4.2 绝热指数 $\gamma$

$$\boxed{\gamma = \frac{C_{p,m}}{C_{V,m}} = 1 + \frac{R}{C_{V,m}} = 1 + \frac{2}{i}}$$

| 分子类型 | $\gamma$ |
|----------|:--------:|
| 单原子 | $5/3 \approx 1.67$ |
| 刚性双原子 | $7/5 = 1.40$ |
| 刚性多原子 | $4/3 \approx 1.33$ |

### 4.3 Mayer 公式的适用条件

$$\boxed{C_{p,m} - C_{V,m} = R \quad \text{（仅对理想气体严格成立）}}$$

- ✅ **理想气体**：严格成立（由焦耳定律保证）
- ⚠️ **实际气体**：不严格成立，差值大于 $R$（因内能有体积依赖性）
- ⚠️ **液体/固体**：$C_p \approx C_V$（因热膨胀系数很小，$p\Delta V$ 可忽略）

---

## 五、推导关联公式

从 Mayer 公式出发，结合其他热力学关系，可以导出：

**内能与状态方程的关系**：

$$\boxed{\left(\frac{\partial U}{\partial V}\right)_T = T\left(\frac{\partial p}{\partial T}\right)_V - p}$$

- 对理想气体 $p = nRT/V$，代入得 $\left(\frac{\partial U}{\partial V}\right)_T = 0$（焦耳定律）
- 对范氏气体，代入得 $\left(\frac{\partial U}{\partial V}\right)_T = a/V_m^2$（非零！）

**任意系统的 $C_p - C_V$ 通式**：

$$\boxed{C_p - C_V = T\left(\frac{\partial p}{\partial T}\right)_V\left(\frac{\partial V}{\partial T}\right)_p}$$

对理想气体代入 $pV = nRT$ 即退化为 $nR$。

---

## 六、真题中的典型考法

### 考法一：直接计算

> 已知某理想气体的 $C_{V,m} = \frac{5}{2}R$，求 $C_{p,m}$ 和 $\gamma$。

**解**：$C_{p,m} = C_{V,m} + R = \frac{7}{2}R$，$\gamma = \frac{C_{p,m}}{C_{V,m}} = \frac{7}{5} = 1.4$

### 考法二：概念辨析

> "任何气体的 $C_p - C_V = R$" 这句话对吗？

**答**：**不对。** Mayer 公式仅对理想气体严格成立。实际气体的 $C_p - C_V > R$（因为内能还依赖于体积）。

### 考法三：自由度推断

> 实验测得某气体的 $\gamma = 1.67$，判断其分子类型。

**解**：$\gamma = 1 + \frac{2}{i} = 1.67 \Rightarrow i = 3$，为**单原子分子**。

---

## 七、记忆要点

| 关键点 | 内容 |
|--------|------|
| 公式 | $C_{p,m} - C_{V,m} = R$ |
| 差值 $R$ 的物理含义 | 1 mol 气体等压升温 1 K 对外做的**膨胀功** |
| 成立前提 | **理想气体**（焦耳定律保证 $U$ 只依赖于 $T$） |
| 参数关系 | $\gamma = 1 + R/C_{V,m} = 1 + 2/i$ |

---

<div style="text-align: center; font-size: 14pt; font-weight: bold; color: #1A3C6E; margin-top: 1.5cm;">

—— 全文完 ——

</div>
