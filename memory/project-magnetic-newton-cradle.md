---
name: project-magnetic-newton-cradle
description: 磁耦合牛顿摆非线性动力学研究——核心学术项目
metadata: 
  node_type: memory
  type: project
  originSessionId: 3ee9f191-2dc6-4cd9-ba37-ee1141d260b4
---

# 磁耦合牛顿摆 — 非线性动力学与模态耦合效应研究

## 项目概述

四球磁耦合牛顿摆的非线性动力学研究，结合实验数据分析和COMSOL仿真，撰写完整学术论文。

## 论文信息

- **标题**: 磁耦合多摆系统的实验标定、数值建模与百球尺度涌现行为（v2，升级自32页原稿）
- **页数**: 34页 (LuaLaTeX编译)
- **终稿**: `C:\Users\chenchen\Desktop\qclaw-backup\magnetic_newton_cradle_paper_v2.pdf`
- **LaTeX源码**: `magnetic_newton_cradle_paper_v2.tex`（工作区已迁至 Desktop\qclaw-backup，原 .qclaw\workspace 仅剩 tmp_thermal）
- **编译器**: LuaLaTeX (XeLaTeX有xdvipdfmx stream损坏bug)
- **状态**: ✅ 已完成（0错误，0未定义引用）
- **2026-07-11 电磁学自洽修订**: 磁体几何改3mm×30mm N42、质量16g、表面场130mT、相邻场0.33mT、μ≈2.2 A·m²；κ由0.002改为物理自洽折中值0.02（已重跑四球标定：基频RMS仍13.7mHz、衰减RMS 8.2→5.3s）；新增磁静力学正向推导+有限尺寸Gilbert模型章节(2图)、磁极相斥一致性验证、涡流阻尼估算(证明可忽略)、6条电磁学文献。图生成脚本 `gen_em_figures.py`。
- **2026-07-11 方向2静态磁力实验补入**: 微信传来实测数据图，OCR得幂律 F(g)=1538·d(cm)^(-3.04±0.06)，R²=0.999，测量范围3-10cm。指数3.04浅于理想偶极4→揭示显著有限尺寸/近场效应(修正了先前"点偶极精确"的过强断言)。实测力律外推给κ_⊥(19cm)≈0.020≈二球实测0.031(独立验证)；(11cm)≈0.18残差归磁通分流。已加静态标定小节+实测原图`static_force_calibration.png`(35页)。仅剩四球在线含分流的有效耦合直接测量待做。

### 论文结构

| 章节 | 核心内容 |
|------|---------|
| 一、引言 | 5个核心科学问题 + 5项本文贡献 |
| 二、实验系统与方法 | TikZ装置图、6种IF方法对比 |
| 三、理论框架 | 磁偶极力→Taylor展开→耦合Duffing→本征频率→KBM频移 |
| 四、实验结果与分析 | 4球非线性参数、A球符号反转、Lyapunov谱、九面板对比 |
| 五、COMSOL仿真 | V2→V5迭代、Duffing vs 模态劈裂竞争诊断 |
| 六、讨论 | 单体-集体符号反转矛盾、κ振幅依赖性、λ可靠性 |
| 七、结论与展望 | 5条结论 + 5个未来方向 |
| 附录 | COMSOL Java API要点、图片清单 |

### 论文三大物理贡献

1. **"涌现非线性"概念**: 耦合项自身可产生超越单体性质的集体非线性行为
2. **单体-集体符号反转矛盾的形式化证明**: A球单体 ε_A 变号 vs 耦合对 c_pair 不变号的坐标变换推导
3. **完整理论推导链**: 磁偶极力 → 耦合Duffing方程 → 本征值分解 → KBM振幅依赖频移公式

## 实验数据

### 两组实验
- **Group 27** (小摆角 θ₀≈0.08 rad): 采样率60Hz，A球启动
- **Group 46** (大摆角 θ₀≈0.11 rad): 采样率60Hz，A球启动
- 数据位置: `C:\Users\chenchen\Desktop\4摆球，距离不变，改变摆角(从左到右ABCD，A为启动球）`

### 核心发现

| 球 | G27 χ | G46 χ | G27 λ | G46 λ | 关键结论 |
|----|-------|-------|-------|-------|---------|
| A | +0.35 硬 | 1.20 软 | 1.02 | 0.80 | **符号反转**：摆幅增大后硬→软弹簧 |
| B | 0.87 软 | 0.87 软 | 0.86 | 0.75 | χ不变，B对振幅不敏感 |
| C | 0.87 软 | 1.12 软 | 1.05 | 1.08 | **不对称暴露**+始终最混沌 |
| D | 0.19 近线 | 0.27 近线 | 0.98 | 1.00 | 始终近线性，**被动混沌** |

### 核心矛盾
- **耦合对层面**: G27和G46均为硬弹簧Duffing（正斜率），不随摆角反转
- **单球层面**: A球在G27为硬弹簧、在G46反转为软弹簧
- **结论**: 多体耦合系统集体行为 ≠ 单体性质简单叠加

## 耦合强度估计

| 方法 | G27 κ | G46 κ |
|------|-------|-------|
| ① 等效二振子 | 0.40% | 0.69% |
| ② 静态弹簧串联 | 1.20% | 2.07% |
| **③ 正态模态反解(推荐)** | **0.57%** | **0.98%** |

完整48步推导见: `coupling-strength-full_2026-05-29.md`

## 关键文件清单

- `magnetic_newton_cradle_paper.pdf` — 32页终稿
- `magnetic_newton_cradle_paper.tex` — LaTeX源码
- `MagneticNewtonCradleV5.java` — V5 COMSOL仿真源码（最终版）
- `MagneticNewtonCradleV4b.java` — V4b COMSOL仿真源码
- `MagneticNewtonCradleV2.java` — V2 COMSOL仿真源码（早期可用版）
- `cradle_data_v5.csv` — V5仿真数据
- `newton_cradle_nonlinear_dynamics.py` — Python非线性动力学分析
- `beat_analysis.py` — 拍现象分析
- `beat_analysis_plots/` — 9张拍分析图 + JSON结果
- `fft_v5_plots/` — V5 FFT分析图（9张）
- `fft_v4b_plots/` — V4b FFT分析图（5张）

## 下一步可能方向

1. **P0**: 20球扩展 — Python scipy.solve_ivp实现（COMSOL不支持20×ODE高效求解）
2. **P1**: 耦合项振幅依赖非线性建模
3. **P2**: 更长实验数据采集（≥120s）用于拍检测
