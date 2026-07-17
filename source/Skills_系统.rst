Skills 系统
###########

Skills 是扩展 AI 能力的可安装模块，每个 Skill 包含 ``SKILL.md`` 定义工作流程。
Skill 可作为插件组件，由插件系统的 ``skills/`` 目录提供；也支持通过 ``.drifox/skills/<name>/`` 直接安装。

内置 Skills（20+）
==================

.. list-table::
   :header-rows: 1
   :widths: 20 40 30

   * - Skill
     - 功能
     - 触发条件
   * - brainstorming
     - 头脑风暴与创意发散
     - 用户表达创意需求
   * - caveman
     - 极简压缩沟通（-75% token）
     - 用户说 "caveman mode"
   * - diagnose
     - 硬 bug 与性能回归诊断
     - 用户报告 bug
   * - tdd
     - 测试驱动开发（红-绿-重构）
     - 用户要求 TDD
   * - git-commit
     - 智能 git 提交
     - 用户要求提交代码
   * - writing-plans
     - 计划文档编写
     - 用户有需求要规划
   * - grill-me
     - 挑战性提问评审
     - 用户需要挑战性反馈
   * - find-skills
     - 发现和安装新技能
     - 用户询问如何做某事
   * - triage
     - 任务分类与优先级排序
     - 用户需要任务分诊
   * - zoom-out
     - 宏观视角分析
     - 用户需要全局视野
   * - to-prd
     - 需求文档生成
     - 用户需要 PRD
   * - improve-codebase-architecture
     - 代码架构改进
     - 用户要重构代码

Skill 标准结构
==============

::

    skill-name/
    ├── SKILL.md              # 主文件 (必需)
    ├── references/           # 参考文档 (可选)
    ├── scripts/              # 工具脚本 (可选)
    └── assets/              # 资源文件 (可选)

端到端示例：TDD 技能执行流程
==============================

.. list-table::
   :header-rows: 1
   :widths: 8 25 30

   * - 步骤
     - AI 行为
     - 说明
   * - 1
     - Skill 匹配：用户要求 TDD → 加载 tdd 技能
     - ``skill("tdd")`` 激活
   * - 2
     - 读取 SKILL.md 获取工作流程
     - 「红-绿-重构」三阶段
   * - 3
     - 阶段一（红）：先写测试
     - ``Write("test_foo.py")``
   * - 4
     - 运行测试确认失败
     - ``Bash("pytest test_foo.py")`` → 失败
   * - 5
     - 阶段二（绿）：写实现代码
     - ``Write("foo.py", impl)``
   * - 6
     - 运行测试确认通过
     - ``Bash("pytest test_foo.py")`` → 通过
   * - 7
     - 阶段三（重构）：优化代码
     - ``Edit(old, new)`` 改善设计
   * - 8
     - 再次运行测试确认通过
     - TDD 循环完成

设计哲学
========

Skills 系统的本质是 **Prompt 即能力**——每个 Skill 就是一个 Markdown 文档，描述了一个完整的工作流程。这不是代码，而是 AI 的「操作手册」。

1. **声明式而非编程式** — 用户不需要写代码来定义行为，用 Markdown 描述流程即可
2. **即插即用** — 放入 skills/ 目录即可生效，无需注册或编译
3. **组合优于继承** — 不同 Skill 可以组合使用，workflow scripts 可以调用多个 Skill
4. **社区共享** — Skill 是纯文本，可以轻松分享和复用

自定义 Skill
============

在 ``.drifox/skills/<name>/`` 或安装在插件 ``skills/`` 目录下添加 Skill，使用 ``/技能名`` 触发。
