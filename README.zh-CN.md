<div align="center">

# AI4Math · 论文写作

面向数学论文起草、证明义务审查与 LaTeX 投稿就绪检查的来源证据驱动工作流。

[English](README.md) · [贡献者](CONTRIBUTORS.md) · [技能包](#技能包) · [安装](#安装) · [快速开始](#快速开始) · [安全边界](#安全边界)

![version](https://img.shields.io/badge/version-0.1.0-blue)
![skills](https://img.shields.io/badge/skills-1-2ea44f)
![license](https://img.shields.io/badge/license-MIT-green)

</div>

<p align="center">
  如果这个项目对你有帮助，欢迎为仓库点 Star ⭐
  <a href="https://github.com/VeryMath/AI4Math-Paper-Writing"><img alt="GitHub Stars" src="https://img.shields.io/github/stars/VeryMath/AI4Math-Paper-Writing?style=social"></a>
</p>

## 这个仓库是什么

这个仓库是 AI4Math 论文写作方向的技能入口。它不替代来源证据、证明检查或实验验证；它提供的是一个让 coding agent 基于已给材料起草、修改和审查数学论文文本的结构化 workflow。

根 README 负责说明地图；真正执行任务时，请进入 `skills/paper-writing/` 并阅读包内 README 和 `SKILL.md`。

## 技能包

| 包 | 适用任务 | 入口 |
| --- | --- | --- |
| [`paper-writing`](skills/paper-writing/) | 基于已提供来源起草、修改、组织和审查数学论文，包括 claim-evidence 审查、证明义务检查、符号一致性、公式可读性和 LaTeX 投稿预检。 | [`README`](skills/paper-writing/README.md) · [`SKILL`](skills/paper-writing/SKILL.md) |

## 安装

推荐方式是 AI 自动安装：让你的 coding agent 自己 clone 或更新仓库、读取 Skill 说明、安装入口并验证 discovery。

```text
请帮我安装这个 AI4Math Skill。

仓库：https://github.com/VeryMath/AI4Math-Paper-Writing.git
分支：main
Skill 路径：
- skills/paper-writing

请执行：
1. 本地 clone 或更新仓库。
2. 读取 README.md、SKILL.md 以及目标 Skill 入口。
3. 如果当前环境支持本地 Skill discovery，把包含 SKILL.md 的目录链接到本地 skills 目录。
4. 如果 Skill 依赖相邻支持目录，请保留这些 sibling 目录。
5. 验证安装后的 Skill 是否可被发现。
6. 告诉我安装路径、是否需要重启 agent，并给我一个测试 prompt。
```

Codex 风格本地 discovery 的手工 fallback：

```bash
git clone https://github.com/VeryMath/AI4Math-Paper-Writing.git
cd AI4Math-Paper-Writing
mkdir -p ~/.codex/skills
ln -s "$PWD/skills/paper-writing" ~/.codex/skills/paper-writing
```

如果你的 agent 使用别的本地 Skill 目录，把 `~/.codex/skills` 替换成对应配置路径。

## 快速开始

克隆仓库并打开技能包：

```bash
git clone https://github.com/VeryMath/AI4Math-Paper-Writing.git
cd AI4Math-Paper-Writing
```

从这里开始：

```text
skills/paper-writing/SKILL.md
```

## 仓库结构

```text
AI4Math-Paper-Writing/
├── README.md
├── README.zh-CN.md
├── SKILL.md
└── skills/
    └── paper-writing/
        ├── SKILL.md
        ├── skills/
        └── templates/
```

## 验证

这个仓库没有根级构建步骤。修改技能包后，请检查 `SKILL.md`、README 链接、模板和包内说明。

## 安全边界

不要提交私有草稿、未公开审稿材料、保密实验日志、API key、`.env` 文件或生成缓存。公开示例和模板应保持来源中性，并确认可以再分发。
