---
name: math-output-format
description: 数学公式输出需使用Word文档，公式需经过编译
metadata: 
  node_type: memory
  type: feedback
  originSessionId: ea12a238-a098-4ddd-9f0a-447ed426a196
---

用户明确要求：涉及数学公式的内容，输出一律使用Word文档（.docx），并且公式需要通过pandoc编译为Word原生OMML格式。

实现方式：
1. 编写Markdown文件，使用LaTeX语法写公式（`$...$` 行内，`$$...$$` 行间）
2. 使用 pandoc 转换为 docx：`pandoc input.md -o output.docx --from markdown --to docx`
3. 验证公式数量：`python -c "import zipfile; ..."` 检查 `m:oMath` 标签数量

**Why:** 用户习惯在Word中查看和编辑数学公式，纯文本LaTeX不便阅读。
**How to apply:** 每次涉及数学公式的输出任务，最终交付docx文件而非直接显示LaTeX代码。
