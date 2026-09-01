---
name: lessons-from-qclaw
description: 从QClaw工作中学到的经验教训——避免重复犯同样的错误
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 3ee9f191-2dc6-4cd9-ba37-ee1141d260b4
---

# 从QClaw工作中学到的经验教训

**Why:** QClaw在数月的密集工作中积累了大量经验，这些经验对Claude Code继续提供帮助至关重要。

**How to apply:** 在进行类似任务时主动参考这些教训。

## 通用工作习惯

1. **写文件后必须验证**: 检查行数、步骤数、关键计算是否保留。"包含N个步骤" = 文件中真的要有N个步骤。
2. **永远确认文件路径再写入**: QClaw曾因路径相似而覆盖了.tex文件，需从备份恢复。
3. **用户关注的是文件内容而非对话**: 对话中展示的完整推导必须实际写入文件。
4. **COMSOL .mph文件被GUI打开时锁定**: 编译前先关闭COMSOL GUI中打开的.mph。

## 技术细节

5. **webchat不支持LaTeX数学渲染**: 所有公式用Unicode纯文本（θ, ω, κ, √, ², ³等）。
6. **PowerShell调用外部exe**: 带`-`参数的命令要用`cmd /c`包装。
7. **Windows换行符**: `\r\n` vs `\n`，Python脚本处理文本文件时要注意。
8. **PDF文件被阅读器锁定**是常见问题，编译时输出到新文件名可绕过。

## COMSOL相关（详见[[comsol-api-reference]]）

9. **COMSOL Java API属性名区分大小写**，用小写驼峰命名。
10. **先创建最小测试脚本验证API**，再修改主代码。
11. **Study类型名在GUI中显示"Time Dependent"但API中叫"Transient"**——不以GUI为准。

## 数学/物理

12. **多体耦合系统集体行为 ≠ 单体性质简单叠加**——这是磁牛顿摆论文的核心发现。
13. **A类不确定度重复计算**是常见错误：检查合成公式中是否有分量被包含两次。
14. **Duffing非线性频移(~10-15 mHz)与线性模态劈裂(~4-8 mHz)可能混叠**——仿真设计时需确保两者量级可分离。
