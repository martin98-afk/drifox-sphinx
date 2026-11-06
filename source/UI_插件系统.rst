UI 插件系统
###########

UI 插件是 DriFox v0.3.0 的核心里程碑——插件不仅能扩展 AI 能力，还能直接在 DriFox 界面中 渲染自定义 UI 组件。

.. image:: /_images/ui插件样例.png
   :alt: UI 插件运行界面
   :align: center
   :width: 90%

三种 UI 组件类型
================

.. list-table::
   :header-rows: 1
   :widths: 20 40 30

   * - 类型
     - 说明
     - 特点
   * - 🃏 浮动卡片 (Floating Card)
     - 悬浮在聊天区域上/下方的独立 QWidget 面板
     - 注册即命令，toggle 显示/隐藏，多窗口隔离
   * - 🧩 内容渲染器 (Content Renderer)
     - 自定义消息 ``custom`` 类型内容块渲染
     - 匹配 custom_type 自动调用渲染函数
   * - 🏭 消息工厂 (Message Factory)
     - 根据消息条件返回自定义 QWidget
     - 替代默认消息卡片渲染
   * - 📥 内嵌面板 (Inline Panel)
     - 消息卡内嵌面板槽位，插件向单条消息注入面板
     - 历史消息重载时自动恢复（v0.6.14）
   * - 🪟 独立弹窗 (register_window)
     - 插件独立弹窗：左侧栏入口 + 右键弹出，支持 group 分组覆盖（v0.6.2）
     - 完整 context provider 与主题级联

浮动卡片特性
============

- 注册即命令 — 调用 ``registry.register_floating_card()`` 后自动注册 ``/卡片ID`` 命令
- 双容器位置 — ``top`` （上部，与配置卡片同级）或 ``bottom`` （下部，覆盖聊天区域）
- 上下文注入 — 通过 ``set_context_provider()`` 拉取项目根目录、会话 ID、主题色等
- 多窗口隔离 — 每个窗口独立缓存卡片实例，项目/会话切换时自动重建
- 热插拔支持 — 插件启用/禁用时即时创建/销毁，无需重启；热重载保真清理 host 资源与 UI 注册（v0.6.14）
- 能力面扩展 — ``ui.notify`` （kind + duration，v0.6.14）、``ui.artifacts.show`` （消息卡成果栏，工具产出可视闭环，v0.6.11）、``card_container_surface_color`` （SDK 主题色，v0.6.13）
- 快捷键绑定 — UI 插件可绑定快捷键并持久化（v0.5.12）
- 独立设置页 — 插件注册表支持独立设置 tab，设置卡可脱离大设置页单独注册（v0.6.14）

生命周期
========

::

    插件启用 → PluginManager 检测 ui/__init__.py
        → 标记 components["ui"] = True
        → backend._load_plugin_ui() 调用 UIPluginRegistry.load_plugin()
            → 导入 ui/__init__.py → 执行 register_ui(registry)
                → 注册浮动卡片、内容渲染器、消息工厂
                    → 浮动卡片自动注册 /命令
                    → 首次执行命令时创建 widget 实例

内置 UI 插件
============

.. list-table::
   :header-rows: 1
   :widths: 20 20 40 15

   * - 插件
     - 类型
     - 说明
     - 命令
   * - 上下文用量统计
     - 浮动卡片
     - 14天Token趋势、每日消息量、会话活跃度、项目分布
     - /context-usage-stats
   * - 项目文件树
     - 浮动卡片
     - 树形浏览文件，智能过滤忽略目录，搜索过滤，实时监听
     - /file-tree
   * - Git 仪表盘
     - 浮动卡片
     - 分支切换、变更文件清单、提交历史速览
     - /git-dashboard
   * - agent_trace
     - 浮动卡片
     - 智能体执行轨迹：TurnList、时间线面板、统计页（v0.5.6）
     - —
   * - 历史管理
     - 浮动卡片
     - 历史会话迁浮动卡 + 置顶/移动项目（v0.5.11）
     - —
   * - ui-slots-demo
     - 示例插件
     - 独立弹窗 + 消息卡片按钮/信息注入四类扩展点演示（v0.6.2）
     - —
   * - _vendor/ 依赖演示
     - 浮动卡片
     - 演示插件 _vendor/ 打包第三方包机制
     - /vendor-demo

开发一个 UI 插件
=======================

三步即可创建一个 UI 浮动卡片插件：

1. 在插件目录创建 ``ui/__init__.py``，提供 ``register_ui(registry)`` 函数
2. 在 ``ui/cards.py`` 中实现 QWidget 子类（浮动卡片内容）
3. 在 ``register_ui`` 中调用 ``registry.register_floating_card()`` 注册

设计约束
========

所有 UI 插件遵守 闭包设计约束：不导入 ``app.core`` 或 ``app.widgets`` 内部模块，
所有文件操作只通过 stdlib 完成，确保与主程序解耦、热重载安全。
