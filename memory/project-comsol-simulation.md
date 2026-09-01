---
name: project-comsol-simulation
description: COMSOL Multiphysics 6.3 仿真工作——磁力牛顿摆的Java API建模
metadata: 
  node_type: memory
  type: project
  originSessionId: 3ee9f191-2dc6-4cd9-ba37-ee1141d260b4
---

# COMSOL Multiphysics 6.3 仿真工作

## 环境配置

- **安装路径**: `D:\COMSOL\comsol\COMSOL63\Multiphysics`
- **可执行文件**: `bin\win64\` 目录
  - `comsol.exe` — 主GUI
  - `comsolbatch.exe` — 批处理
  - `comsolcompile.exe` — Java编译
  - `comsolmphserver.exe` — Model Server

## 技术方案

使用 **GlobalEquations** (0D) 物理接口直接求解4个耦合Duffing振子ODE：
```
θ̈ᵢ + ω₀²θᵢ + εᵢθᵢ³ + γθ̇ᵢ + ωc²(2θᵢ − θᵢ₋₁ − θᵢ₊₁) = 0
```

## 仿真版本迭代

| 版本 | κ | 时长 | 状态 | 关键结果 |
|------|-----|------|------|---------|
| V2 | 0.008 | 30s | ✅ | 成立，30步内完成 |
| V3 | 0.008 | 250s | ✅ | 非线性主导，无清晰模态劈裂 |
| V4 | 0.030 | ~194s | ❌ | 步长坍缩至1e-13 |
| **V4b** | **0.020** | **250s** | ✅ | 9817步，8s求解。Δf≈9.7 mHz |
| **V5** | **0.040** | **500s** | ✅ | 9356步，14s求解。含非线性项 |

### V5 最终参数（[[project-magnetic-newton-cradle]]论文使用）
- f₀ = 1.0 Hz, κ = 0.04, γ = 0.07 + 平方阻尼
- Ball A: sigmoid过渡Duffing (硬→软, θ_c≈0.095 rad)
- 各球独立 ω₀ (0.997-1.001 Hz，B/C不对称)
- α⁵磁耦合Taylor展开（V5.3中移除以避免blowup）

### V5 FFT结果（非线性）
- A: 1.026, 1.078 Hz
- B: 1.030, 1.006 Hz
- C: 1.026, 1.052, 1.084 Hz
- D: 1.050, 1.028 Hz

## 编译运行命令

```powershell
$bin = "D:\COMSOL\comsol\COMSOL63\Multiphysics\bin\win64"
# 编译
cmd /c "$bin\comsolcompile.exe" C:\Users\chenchen\.qclaw\workspace\MagneticNewtonCradleV5.java
# 运行
cmd /c "$bin\comsolbatch.exe" -inputfile C:\Users\chenchen\.qclaw\workspace\MagneticNewtonCradleV5.class -outputfile result.mph -batchlog log.txt
```

注意: PowerShell调用必须用 `cmd /c` 包装。

## COMSOL 6.3 Java API 速查表（关键！见[[comsol-api-reference]]）

详细API参考已记录在 [[comsol-api-reference]] 中。

## 关键文件

- `MagneticNewtonCradleV5.java` — V5最终版源码
- `MagneticNewtonCradleV4b.java` — V4b源码
- `MagneticNewtonCradleV2.java` — V2源码
- `MagneticNewtonCradle.java` — V1原始版本
- `TestSolverSetup.java` — API调试测试
- `comsol_v2_run_2026-05-29T2339.md` — V2完整运行记录
- `comsol-v5-optimization_2026-06-02T1723.md` — V5优化记录

## 重要陷阱

1. **时间导数命名必须是后缀式**: `u1tt`, `u1t` (不是 `utt1`, `ut1`)
2. **因变量需显式设置**: `ode.set("name", "u1")` 
3. **物理接口名称**: `"GlobalEquations"` (不是 `"GlobalODEsAndDAEs"`)
4. **方程属性名**: `"equation"` (不是 `"f"`)
5. **Study类型**: `"Transient"` (不是 `"TimeDependent"`)
6. **求解调用**: `model.study("std1").run()` (不是 `model.sol().runAll()`)
7. **.mph文件被GUI打开时锁定**: model.save()会抛IOException
8. **evalGlobal()不存在于COMSOL 6.3**: CSV需GUI手动导出
