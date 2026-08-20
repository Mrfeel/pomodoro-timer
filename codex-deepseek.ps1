# Codex DeepSeek 启动脚本
# 设置环境变量
$env:PATH = "D:\node.js;C:\Users\chenchen\AppData\Roaming\npm;" + $env:PATH
$env:OPENAI_API_KEY = "sk-947e17cb35174c20bf5529b7f72f608a"
$env:OPENAI_BASE_URL = "https://api.deepseek.com/v1"

# 启动 Codex
node "C:\Users\chenchen\AppData\Roaming\npm\node_modules\@openai\codex\bin\codex.js" --model deepseek-chat
