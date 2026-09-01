# CODEX.md — 项目规范与用户偏好

> 创建日期: 2026-08-20
> 来源: 迁移自 Claude Code 记忆系统（C:\Users\chenchen\.claude\projects\D-----first-CC\memory\）

本文件是 Codex 在本工作区工作的最高优先级行为规范，每次都必须遵守。

## 1. 语言与交流

- 始终使用**简体中文**与用户交流（最终回复、进度更新、解释均用中文）。
- 代码中的函数名、变量名可保持英文，但**注释和解释必须使用中文**。
- 用户偏好**极度详尽的推导**：所有中间步骤都要保留并讲解，不跳步。
- 用户对**乱码非常敏感**：注意 UTF-8 编码，避免 GBK/UTF-8 混淆。
- 终端/对话环境不支持 LaTeX 渲染时，数学符号用 Unicode 纯文本（θ、ω、√、²、³、κ 等）。

## 2. 用户信息

- 姓名: 杨思辰
- 学号: PB25992094
- 学院: 未来技术学院（中国科学技术大学）
- 专业: 物理学（本科）
- 指导教师: 仝朔源
- 时区: Asia/Shanghai · 系统: Windows 11（用户 chenchen）

## 3. 文档输出规范（重要）

- 涉及**数学公式**的内容，最终交付 **Word 文档 (.docx)**，不用纯文本 LaTeX。
- 生成方式: 写 Markdown 源文件（LaTeX 公式 $...$ / $$...$$）→ 用 pandoc 转换: `pandoc input.md -o output.docx --from markdown --to docx`（编译为 Word 原生 OMML 公式）。
- 验证: 用 python 检查 docx 内 `m:oMath` 标签数量，确认公式真的被编译。
- 数学类 Word 文档的格式模板以 `线性代数第七章_详尽讲解.md/.docx` 为准。要点：
  - 头部标注课程/章节、来源、用户信息、考试重点
  - 强调块: `> 💡` 直观理解 / `> ⭐` 核心结论 / `> 🔥` 考试重点 / `> ⚠️` 注意事项
  - 例题格式: `### 📝 Example N` + 分步解答（**第1步：** ...）
  - 结尾附 `# 📋 小测重点速查卡片`
  - 语气亲切但严谨，适当使用 emoji（📝📋💡⭐🔥⚠️）

## 4. 环境与工具链

- Windows 11 中文系统，控制台 GBK 936 — 注意中文乱码坑
- Python 3.12: `C:\Users\chenchen\AppData\Local\Programs\Python\Python312\python.exe`；常用 numpy/scipy/matplotlib/PIL/openpyxl/python-docx
- C/C++: MSYS2 MinGW-w64 gcc 16.1.0，路径 `C:\msys64\ucrt64\bin`；make 是 `mingw32-make`；pacman 包管理（USTC 镜像）；练习目录 `D:\辰辰\c-practice`
- LaTeX: 优先 LuaLaTeX（XeLaTeX 有 xdvipdfmx stream 损坏 bug）；中文用 ctex
- 仿真: COMSOL Multiphysics 6.3，位于 `D:\COMSOL\comsol\COMSOL63\Multiphysics`；命令行需用 `cmd /c` 包装
- 文档转换: pandoc；Node.js 可用于本地服务器/二维码生成

## 5. 关键文件路径

- QClaw 工作区（历史学术产出）: `C:\Users\chenchen\.qclaw\workspace\` — **卸载 QClaw 前务必保留**
- 桌面备份: `C:\Users\chenchen\Desktop\qclaw-backup\`（含磁牛顿摆论文终稿）
- 实验数据: `C:\Users\chenchen\Desktop\4摆球，距离不变，改变摆角(从左到右ABCD，A为启动球）`
- 教材/习题: `C:\Users\chenchen\Downloads\`

## 6. 项目背景与当前状态

### 历史学术项目（已完成）
- **磁耦合牛顿摆论文**（核心学术项目）: 34 页 LuaLaTeX 论文，非线性动力学 + COMSOL 仿真。终稿 `Desktop\qclaw-backup\magnetic_newton_cradle_paper_v2.pdf`。核心发现: "涌现非线性"、单体-集体符号反转矛盾、完整理论推导链。
- **杨氏模量实验报告**: v7 最终版，E = (1.97 ± 0.09) × 10¹¹ Pa。
- **热学数量级汇编**（张玉民《热学》第二版）: `tmp_thermal/` 下完整 9 章数量级表格 + Word 版。
- **复习提纲**: 线性代数 B1、热学 v4（781 个 OMML 公式）、数学分析 B2。
- **数据结构小学期**（2026-07-10 ~ 07-29）: 6 个实验全部完成，C 语言，教材在 Downloads。

### 近期活动（音乐/游戏/网页）
- **《谪仙人·李白历史摇滚音乐剧》策划**: `build_musical_doc_v3.py` 生成策划方案 docx。
- **音乐剧服装连线小游戏**: `musical-costume-game.html` + `game-qrcode.png`（2026-08-19 创建），本地服务器 `http://192.168.1.51:8080/musical-costume-game.html`。
- **公网部署（2026-08-20 完成，永久版）**: 游戏已部署到 GitHub Pages，无需本机运行，任意网络可访问。
  - 永久地址: `https://mrfeel.github.io/musical-costume-game/` 
  - 仓库: `https://github.com/Mrfeel/musical-costume-game`（public；游戏本体为 index.html）
  - 二维码: `game-qrcode.png`（已指向永久地址，红褐 #c0392b + 奶油 #fffaf0，500×500）
  - 更新方法: 修改 `musical-costume-game.html` 后，以 index.html 名义 push 到仓库 main 分支，GitHub Actions 自动重新部署
  - 历史: 曾用 cloudflared 隧道方案（`.tools\cloudflared.exe` 保留备用，已停用）
  - 2026-08-20 v2 优化: 与灯光游戏相同方案——鼠标+触屏统一拖拽（Pointer Events）、即时判定（错误抖动并自动还原）、匹配进度条、撤销、连胜里程碑、通关彩带、个人最佳记录（localStorage）。
  - 2026-08-20 v2.1: 新增 16 个音乐剧角色 Q版小人（手绘 SVG，`CHIBI_SVGS` 内嵌卡片）。备注: 路线 B（AI 生成）不可用——环境 `OPENAI_API_KEY` 实为 DeepSeek 密钥（`OPENAI_BASE_URL=https://api.deepseek.com/v1`），无图像生成接口（全部 404）。
- **舞台灯光配对游戏（带图）**: `stage-lighting-game.html`（2026-08-20 创建），12 种灯具 ↔ 12 种光效用途，卡片内嵌手绘 SVG 灯具图，深色舞台主题，初始即乱序。
  - 永久地址: `https://mrfeel.github.io/stage-lighting-game/`
  - 仓库: `https://github.com/Mrfeel/stage-lighting-game`（public；游戏本体为 index.html）
  - 更新方法: 与服装游戏相同，修改 `stage-lighting-game.html` 后以 index.html 名义 push 到该仓库 main 分支。
  - 2026-08-20 v2 优化: 鼠标+触屏统一拖拽（Pointer Events）、即时判定（错误抖动并自动还原）、匹配进度条、撤销、连对里程碑、通关彩带、个人最佳记录（localStorage）。

### 课程
- 在修: 电子技术基础（康华光《电子技术基础（模拟部分）》+ 李瀚荪《电路分析基础》）、线性代数 B1、热学、数据结构等。

## 7. 经验教训（避免重复犯错）

1. 写文件后必须验证（行数、步骤数、关键计算是否真的保留）。
2. 永远确认文件路径再写入，避免覆盖。
3. 用户关注的是文件内容而非对话——对话里展示的推导必须实际写入文件。
4. COMSOL .mph 被 GUI 打开时会锁定，编译前先关闭。
5. PowerShell 调用带 `-` 参数的外部 exe 用 `cmd /c` 包装。
6. 注意 Windows 换行符 `\r\n`。
7. PDF 被阅读器锁定时，编译输出到新文件名可绕过。
8. A 类不确定度重复计算是常见错误，检查合成公式。
9. C 源码 printf 中文在 GBK 控制台乱码: `SetConsoleOutputCP(CP_UTF8)` 或 `chcp 65001`。

## 8. 记忆系统位置

完整记忆已随 2026-09-01 迁移存档至本仓库（Claude Code 已卸载，不再依赖 `~/.claude`）：
- 记忆索引: `memory\MEMORY.md`（16 个记忆文件，含 COMSOL API 速查、工具链配置、QClaw 技能清单等，需要时直接读取本目录）
- Claude Code 历史会话归档: `archive\claude-code\`（完整会话记录、history.jsonl、旧版 .claude 配置；已加入 .gitignore，不提交 git，仅供查阅）
## 9. 工作习惯

- 动手前先简要说明计划，边做边同步进度。
- 完成后用简洁的结构化摘要汇报，引用文件路径方便用户点击。
- 涉及重要交付物时，先告知用户再开始大块工作。