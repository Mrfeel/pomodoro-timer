---
name: c-cpp-toolchain-setup
description: MSYS2/MinGW-w64 gcc 工具链安装位置与 VS Code 配置
metadata: 
  node_type: memory
  type: reference
  originSessionId: 7f1544cb-b8ff-44ca-bd58-2b901f965cb8
---

2026-07-10 为杨思辰配置了 C/C++ 开发环境（MinGW-w64 via MSYS2）。

- **工具链版本**: gcc 16.1.0 / g++ 16.1.0 / gdb 17.2 / make 4.4.1
- **编译器路径**: `C:\msys64\ucrt64\bin`（已加入用户 PATH），gcc/g++/gdb 均在此
- **make 命令**: `mingw32-make`（不是 `make`）
- **包管理**: `C:\msys64\usr\bin\pacman.exe`，装库用 `pacman -S mingw-w64-ucrt-x86_64-<包名>`
- **镜像源**: 已把 USTC 中科大镜像置顶于 `C:\msys64\etc\pacman.d\mirrorlist.mingw` 和 `mirrorlist.msys`（默认境外镜像太慢）
- **VS Code**: 已装 ms-vscode.cpptools 扩展
- **练习文件夹**: `D:\辰辰\c-practice`，含 hello.c 及 `.vscode/`（tasks.json 编译、launch.json 调试、c_cpp_properties.json 智能提示）已配好，打开即可 Ctrl+Shift+B 编译、F5 调试

注意：改 PATH 后需重开终端/VS Code 才生效。物理计算若需科学库（GSL/FFTW）可用 pacman 装。

**中文乱码坑（已踩）**: UTF-8 源文件在中文 Windows(GBK 936 控制台)下 printf 中文会乱码。解决：源码开头 `#include <windows.h>` 并调用 `SetConsoleOutputCP(CP_UTF8);`，或临时 `chcp 65001`。已在 D:\c-practice\main.c 中示范。

**用户是 C 语言初学者**，讲解需从最基础讲起（如"重新编译就是再敲一遍 gcc"、`.\exe` 运行、改代码必须重新编译）。曾把 hello.c 误建成文件夹导致 No such file。
