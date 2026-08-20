@echo off
REM 设置环境变量
set PATH=D:\node.js;C:\Users\chenchen\AppData\Roaming\npm;%PATH%
set OPENAI_API_KEY=sk-947e17cb35174c20bf5529b7f72f608a
set OPENAI_BASE_URL=https://api.deepseek.com/v1

REM 启动 Codex
node "C:\Users\chenchen\AppData\Roaming\npm\node_modules\@openai\codex\bin\codex.js" --model deepseek-chat
