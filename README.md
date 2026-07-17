# Toy MCP Guide

让AI通过MCP协议控制蓝牙玩具——双方案完整搭建教程。

## 方案

| 方案 | 路径 | 适用设备 |
|------|------|----------|
| ToyMCP | VPS → state.json → 手机HTML（Web Bluetooth）→ BLE | 标准Svakom协议玩具（分欣/Erica） |
| ToyADB | 笔记本 → ADB无线 → 手机APP | 私有BLE协议玩具（B220等） |

## 快速开始

见完整教程：`Toy_MCP_完整搭建教程.html`

## 致谢

方案一 Web Bluetooth 控制思路参考了 [svakom-ble-ai](https://github.com/vickyldr/svakom-ble-ai) 项目的 BLE 协议分析。本项目在此基础上增加了 FastMCP 服务端、双方案架构（ToyADB）、强度映射修复、多设备支持及 HyperOS 适配。

## 作者

[AZHi-xinxin](https://github.com/AZHi-xinxin)
