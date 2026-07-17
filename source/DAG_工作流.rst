DAG 工作流
######################

.. image:: /_images/subagent_dag.png
   :alt: DAG 工作流可视化界面
   :align: center
   :width: 90%


SubAgent DAG（有向无环图）工作流允许编排多个子智能体，自动拓扑排序、并行执行无依赖节点，并实时生成可视化工作流图。

功能概览
========

- 🔗 **DAG 编排** — 定义 nodes + edges，支持三种拓扑模式
- 🔄 **自动拓扑排序** — 入度为 0 的节点自动并行启动
- 🧠 **结果自动注入** — 下游节点自动获取上游结果
- ⚡ **并行执行** — 无依赖节点同时运行
- 📊 **实时可视化** — ECharts 力导向图实时展示节点状态

状态颜色编码
============

.. list-table::
   :header-rows: 1
   :widths: 15 15 50

   * - 状态
     - 颜色
     - 说明
   * - ⏳ pending
     - 黄色
     - 等待执行
   * - 🔵 running
     - 蓝色
     - 正在执行中
   * - ✅ completed
     - 绿色
     - 执行成功完成
   * - ❌ failed
     - 红色
     - 执行失败
   * - ⏭️ skipped
     - 灰色
     - 因上游失败自动跳过

支持的 DAG 拓扑模式
===================

.. list-table::
   :header-rows: 1
   :widths: 15 30 30

   * - 模式
     - 说明
     - 适用场景
   * - Pipeline
     - 严格的串行链
     - A → B → C，依赖关系明确
   * - Fan-out
     - 先并行再汇聚
     - 多路探索 → 汇总分析
   * - Hybrid
     - 分支 + 汇合点混合
     - 复杂任务：分析 → 多路实现 → 审查汇总

执行流程
========

1. AI 分析任务 → 标记依赖 → 设计拓扑
2. 调用 subagent_dag(nodes=[...], edges=[...])
3. SubAgentManager 验证 DAG（节点存在性 + 环检测）
4. 入度为 0 的节点并行启动（独立 QThread + LLM + 工具）
5. 节点完成后自动更新 ECharts 节点图状态
6. 级联检查下游 → 入度为 0 时启动
7. 全部完成 → 清理状态 → 汇总结果

示例
====

.. code-block:: python

    subagent_dag(
        nodes=[
            {"id": "plan", "agent": "plan", "description": "分析需求"},
            {"id": "explore_1", "agent": "explore", "description": "研究模块A"},
            {"id": "explore_2", "agent": "explore", "description": "研究模块B"},
            {"id": "build", "agent": "build", "description": "编码实现"},
            {"id": "review", "agent": "code-reviewer", "description": "审查"},
        ],
        edges=[
            {"from": "plan", "to": "explore_1"},
            {"from": "plan", "to": "explore_2"},
            {"from": "explore_1", "to": "build"},
            {"from": "explore_2", "to": "build"},
            {"from": "build", "to": "review"},
        ]
    )
