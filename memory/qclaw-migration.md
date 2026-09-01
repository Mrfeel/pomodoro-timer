---
name: qclaw-migration
description: QClaw工作区迁移到Claude Code的记录
metadata: 
  node_type: memory
  type: project
  originSessionId: 3ee9f191-2dc6-4cd9-ba37-ee1141d260b4
---

# QClaw → Claude Code 迁移记录

**迁移日期**: 2026-06-11
**原因**: 用户即将卸载QClaw

## QClaw Agent 概览

- **名称**: QClaw（官方默认Agent）
- **平台**: OpenClaw
- **运行时间**: 2026-04-05（创建）至 2026-06-09（最后活跃）
- **模型**: qclaw/pool-deepseek-v4-pro
- **工作区**: `C:\Users\chenchen\.qclaw\workspace\`

## 已迁移内容

所有关键信息已迁移至 Claude Code memory 系统，包括：
- 用户身份 → [[user-profile]]
- 磁耦合牛顿摆项目 → [[project-magnetic-newton-cradle]]
- COMSOL仿真 → [[project-comsol-simulation]]
- 杨氏模量实验 → [[project-youngs-modulus]]
- 热学分析 → [[project-thermal-physics]]
- 复习提纲 → [[project-review-outlines]]
- COMSOL API参考 → [[comsol-api-reference]]
- QClaw工作区文件地图 → [[qclaw-workspace-map]]

## QClaw工作区保留建议

原工作区 `C:\Users\chenchen\.qclaw\workspace\` 包含大量不可替代的学术产出，**强烈建议保留完整目录**，至少在卸载前备份以下目录和文件：

### 必须备份
1. **memory/ 目录** — 全部日常记录（13天，2026-04-13 至 2026-06-09）
2. **skills/ 目录** — 26个已安装技能定义
3. **MagneticNewtonCradle*.java** — COMSOL仿真源码（V2, V4b, V5）
4. **magnetic_newton_cradle_paper.pdf** — 32页学术论文终稿
5. **magnetic_newton_cradle_paper.tex** — 论文LaTeX源码
6. **tmp_thermal/ 目录** — 热学数量级汇编（最新工作）
7. **beat_analysis_plots/ 目录** — 拍现象分析图
8. **fft_v5_plots/ 和 fft_v4b_plots/ 目录** — FFT分析图
9. **cradle_data_v5.csv** — V5仿真数据
10. **杨氏模量实验报告_综合版.tex** — 实验报告LaTeX源码
11. **所有 task-summary_*.md 和 *_2026-*.md** — 任务归档（约30个）

### 可以忽略
- `node_modules/` — 可通过 npm install 恢复
- `__pycache__/` — Python缓存
- `*.aux, *.out, *.log` — LaTeX编译中间文件
- 重复的daily notes（5月23日有大量重复）

## 经验教训（从QClaw记忆中学到的）

1. **写文件后必须验证内容完整性**（检查行数、步骤数）
2. **Webchat不支持LaTeX渲染**，用Unicode纯文本
3. **COMSOL .mph文件被GUI打开时锁定**，model.save()会失败
4. **PowerShell调用comsolbatch需用cmd /c包装**
5. **COMSOL Java API属性名区分大小写**，用小写驼峰
6. **永远先用最小测试脚本验证API**，再修改主代码
