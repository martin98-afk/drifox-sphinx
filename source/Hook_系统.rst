Hook 系统
#########

.. image:: /_images/hooks配置.png
   :alt: Hook 配置界面
   :align: center
   :width: 90%


DriFox 支持通过可视化界面配置和管理 Hook 事件钩子。

支持的事件类型
==============

.. list-table::
   :header-rows: 1
   :widths: 20 50

   * - 事件
     - 触发时机
   * - SessionStart
     - 新会话启动时
   * - PreUserMessage
     - 用户消息发送前
   * - PostUserMessage
     - 用户消息发送后
   * - PreAssistantMessage
     - AI 助手回复前
   * - PreToolUse
     - 工具执行前（可 BLOCK）
   * - PostToolUse
     - 工具执行后

Hook 类型
=========

- **command** — 执行系统命令/脚本
- **http** — 发起 HTTP 请求
- **python function** — 调用 Python 函数

决策控制
========

Hook 可通过以下方式控制流程：

- Exit code 2 → BLOCK（跳过工具执行）
- JSON 输出 ``{"decision": "block"}`` → BLOCK
- JSON 输出 ``{"decision": "continue"}`` → 继续
