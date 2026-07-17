
FAQ 常见问题
############

安装与运行
==========

DriFox 支持哪些 Python 版本？
--------------------------------

Python 3.14+，推荐使用 Python 3.14 或更高版本。

安装时提示依赖冲突怎么办？
---------------------------

推荐使用 ``uv sync`` 安装，uv 会自动解决依赖冲突。如果遇到问题：

.. code-block:: bash

    # 清理缓存后重试
    uv sync --reinstall

    # 或指定组安装排查
    uv sync --group dev --no-group gateway

支持 macOS 吗？Linux 呢？
-------------------------

DriFox 目前主要支持 Windows（PyQt5），macOS 和 Linux 支持正在开发中。
macOS 用户可使用 ``uv sync --group mac-build`` 尝试构建 DMG 包。

功能与使用
==========

DriFox 和 Cursor / Copilot 有什么区别？
----------------------------------------

.. list-table::
   :header-rows: 1
   :widths: 20 50

   * - 工具
     - 定位
   * - DriFox
     - AI 桌面对话助手，悬浮对话框 + 多平台消息网关
   * - Cursor
     - AI 原生 IDE，编辑器内嵌
   * - GitHub Copilot
     - IDE 插件，代码补全 + 聊天
   * - Claude Code
     - 终端原生 Agentic Coding System

DriFox 的核心差异在于"不绑定 IDE"——它是一个悬浮在桌面上的独立 AI 助手，可以在任何编辑器/IDE 上方工作。

为什么不做成 IDE 插件？
-----------------------

设计哲学不同。DriFox 的目标是**工具链无关**——不管你用 VS Code、PyCharm、Neovim 还是记事本，DriFox 都在那里。它不侵入你的编辑器，而是作为一个独立的 AI 层悬浮在桌面上。

如何切换 AI 模型？
------------------

在设置面板的「模型配置」中切换。支持 OpenAI / Claude / DeepSeek / MiniMax / 通义千问等多种模型。不同模型可在不同会话中独立配置。

会话数据存在哪里？安全吗？
---------------------------

所有数据存储在本地 ``.drifox/sessions.db`` SQLite 数据库中，不上传任何云端。
长期记忆数据也全部本地存储，不经过第三方服务器。

技术问题
========

启动时闪退怎么办？
------------------

.. code-block:: bash

    # 尝试以调试模式启动
    python main.py --debug

    # 查看日志文件
    cat .drifox/logs/latest.log

    # 清空缓存后重试
    rm -rf .drifox/cache

如何卸载 DriFox？
-----------------

.. code-block:: bash

    # 删除项目目录即可
    rm -rf DriFox/

    # 如需删除所有数据（会话、记忆、配置）
    rm -rf ~/.drifox/

自定义与扩展
====================

如何开发一个插件？
---------------------------

参考 :doc:`插件系统` 和 :doc:`UI_插件系统` 文档。三步即可创建插件：

1. 在 ``.drifox/plugins/`` 创建插件目录
2. 添加 ``.drifox-plugin/plugin.json`` 清单文件
3. 添加命令/Agent/Skill/主题/Hook/MCP 等组件

如何编写自定义 Skill？
-------------------------------

参考 :doc:`Skills_系统`。在 ``.drifox/skills/<name>/`` 下创建 ``SKILL.md`` 即可。

如何连接 MCP Server？
-----------------------------

参考 :doc:`MCP_系统`。在插件或全局配置中添加 ``.mcp.json`` 配置即可。
