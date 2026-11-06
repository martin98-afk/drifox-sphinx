Git Worktree 并行开发
#####################

DriFox 内置 git worktree 管理，让你能在 不污染主仓库代码的情况下，自由切换分支进行开发。

.. image:: /_images/git-worktree.png
   :alt: Git Worktree 管理界面
   :align: center
   :width: 90%

功能概览
========

- 🌲 分支树展示 — 自动检测 git 仓库，以树状列表展示所有 worktree 分支
- 🔵 当前分支标识 — 蓝点标识当前活跃分支；标签页状态环颜色同步（v0.6.12）
- 🔄 一键切换 — 点击「切换」立即将工作目录指向对应 worktree；会话工作目录异步切换（v0.6.12）
- ➕ 新建分支 — 直接从 UI 创建新分支 + worktree；合并回主仓库带冲突预判与双向 dirty 预检
- 🗑 安全删除 — 有未提交改动默认拒绝，强删需二次确认；僵尸 worktree 自动检测（v0.5.8）
- 🏠 根目录固定 — 原始仓库文件夹始终显示为「根目录」；工作目录失效后自动回落主仓库根（v0.5.12）
- 🧠 AI 感知 worktree — 提示词自动注入当前 worktree 上下文；``manage_worktree`` 工具供 AI 编程式管理（v0.5.11）

使用场景
========

- 同时修复多个 bug，每个 bug 一个独立 worktree
- 并行开发多个 feature，互不干扰
- 在主分支稳住的情况下，安全试错新思路

示例流程
========

1. 添加项目文件夹到关键文档，设为工作目录
2. 展开 worktree 树 → 点击「＋ 新建 worktree」
3. 输入分支名 → 自动创建并切换
4. AI 在 worktree 上编辑代码，不影响主仓库
5. 完成工作后「切换」回主分支，或「✕」删除 worktree

AI 工具面
=========

``manage_worktree`` 支持 list / create / remove / merge / switch 五个动作：merge 自动预判冲突并在冲突时保留现场，switch 把会话工作目录切到指定 worktree。死 workdir 自动恢复到主仓库根（v0.6.15）。
