---
name: qclaw-workspace-map
description: QClaw工作区文件地图——关键文件的位置和用途
metadata: 
  node_type: memory
  type: reference
  originSessionId: 3ee9f191-2dc6-4cd9-ba37-ee1141d260b4
---

# QClaw 工作区文件地图

**工作区根目录**: `C:\Users\chenchen\.qclaw\workspace\`

## 目录结构

```
workspace/
├── AGENTS.md              — Agent行为指南（QClaw平台）
├── SOUL.md                — Agent灵魂定义
├── IDENTITY.md            — Agent身份（QClaw）
├── USER.md                — 用户档案（模板，未填写）
├── MEMORY.md              — 长期记忆
├── HEARTBEAT.md           — 心跳任务配置
├── TOOLS.md               — 工具配置
├── memory/                — 日常记录 (2026-04-13 ~ 2026-06-09)
├── skills/                — 26个技能定义
│   ├── academic-deep-research/
│   ├── arxiv-scholar-search/
│   ├── course-study/
│   ├── deep-research-pro/
│   ├── image*/ (多个图像工具)
│   ├── language-learning/
│   ├── literature-review/
│   ├── literature-search/
│   ├── multi-search-engine/
│   ├── notebooklm-cli/
│   ├── pdf*/ (多个PDF工具)
│   ├── ppt*/ (多个PPT工具)
│   ├── scholar*/
│   ├── study-buddy/study-plan/study-tutor/
│   ├── summarize/
│   ├── video*/ (多个视频工具)
│   └── word-docx/word-reader/
├── tmp_thermal/           — ⭐ 热学数量级分析（最后的工作）
│   ├── 全书数量级汇总.md
│   ├── 热学_数量级汇编.docx
│   └── pages/ (235张PNG)
├── beat_analysis_plots/   — 拍现象分析图+JSON
├── fft_v5_plots/          — V5 FFT分析图
├── fft_v4b_plots/         — V4b FFT分析图
├── three_ball_group1~3/   — 三球实验数据分析
├── mph_v5_extracted/      — V5 COMSOL模型提取数据
├── node_modules/          — npm依赖（可恢复）
└── __pycache__/           — Python缓存（可忽略）
```

## 核心学术产出文件

### 磁耦合牛顿摆
- `magnetic_newton_cradle_paper.pdf` — 🏆 32页论文终稿
- `magnetic_newton_cradle_paper.tex` — LaTeX源码
- `MagneticNewtonCradleV5.java` — V5仿真源码
- `MagneticNewtonCradleV4b.java` — V4b仿真源码
- `MagneticNewtonCradle.java` — V1源码

### 杨氏模量实验
- `杨氏模量实验报告_综合版.tex` — LaTeX源码（最终版）
- `杨氏模量实验报告_v7.pdf` — 编译输出

### 热学
- `tmp_thermal/全书数量级汇总.md` — ⭐ 最新工作
- `tmp_thermal/热学_数量级汇编.docx`

### 仿真数据
- `cradle_data_v5.csv` — V5仿真CSV
- `cradle_data_v3.csv` — V3仿真CSV
- `cradle_data_v4b` — V4b原始导出

### 分析脚本（可复用）
- `beat_analysis.py` — 拍现象分析
- `analyze_blue.py` — 蓝色通道分析
- `fft_v4b_analysis.py` — V4b FFT分析
- `fft_v5_analysis.py` — V5 FFT分析
- `convert_v5_csv.py` — V5 CSV转换
- `calc_youngs_modulus.py` — 杨氏模量计算
- `gen_report_v2.py` — 仿真报告生成器
- `newton_cradle_nonlinear_dynamics.py` — 非线性动力学

### 任务归档 (~30个文件)
- `task-summary_*.md` — 任务总结
- `*_2026-*.md` — 带时间戳的任务工件

## 大型/可恢复文件（卸载前可放心删除）
- `node_modules/` — npm install恢复
- `__pycache__/` — Python自动生成
- `*.aux, *.out, *.log` — LaTeX中间文件
- `batch_mnc*.log` — 批处理日志
- `all_pdf_text.txt`, `Ch*_extracted.txt` — PDF提取中间文本
