# Claude Code DeepSeek 启动脚本
# 设置 PATH（如已配置系统环境变量则可省略）
$env:PATH = "D:\node.js;C:\Users\chenchen\AppData\Roaming\npm;" + $env:PATH

# API Key 已配置在 C:\Users\chenchen\.claude\settings.json 的 env 中，此处不再硬编码
# 启动 Claude Code
claude --model deepseek-v4-pro