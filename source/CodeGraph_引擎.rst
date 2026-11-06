CodeGraph 代码智能引擎
######################

DriFox v0.3.4 集成 CodeGraph 代码智能引擎，提供语义级别的代码探索能力。

五种探索模式
============

.. list-table::
   :header-rows: 1
   :widths: 15 50

   * - 模式
     - 说明
   * - search
     - 搜索符号（函数/类/方法/变量），支持按 kind 过滤和精确/模糊匹配
   * - explore
     - 综合搜索 + 调用上下文，一次输出符号定义和引用信息
   * - callers
     - 查找谁调用了指定符号，可配置遍历深度
   * - callees
     - 查找指定符号调用了谁，可配置遍历深度
   * - impact
     - 变更影响分析，评估改动波及范围

功能特性
========

- **语义化索引** — 自动解析代码符号、引用关系、调用链
- **文件同步** — 工作目录变更时自动重初始化索引（v0.4.4 能力升级与同步稳定性增强）
- **文件监听** — 实时同步文件系统变更到索引
- **多种过滤** — 按类型（function/class/method/variable/field/enum）过滤搜索结果
- **深度控制** — callers/callees/impact 可配置 1-3 级遍历深度
- **路径筛选** — files 模式按目录筛选索引文件

使用示例
========

::

    # 探索一个符号
    codegraph_explore("ChatBackend")

    # 查找谁调用了 send_message
    codegraph_explore("send_message", mode="callers")

    # 变更影响分析
    codegraph_explore("on_click", mode="impact")

    # 查看索引状态
    codegraph_explore(mode="status")
