@echo off
REM 设置 PATH（如已配置系统环境变量则可省略）
set PATH=D:\node.js;C:\Users\chenchen\AppData\Roaming\npm;%PATH%

REM API Key 已配置在 C:\Users\chenchen\.claude\settings.json 的 env 中，此处不再硬编码
REM 启动 Claude Code
claude --model deepseek-v4-pro