# Math Beamer

English guide: [README.md](README.md)

`math-beamer` 是面向数学 Beamer 幻灯片的 AI4Math Skill。它帮助
coding agent 把论文、笔记、证明草稿、课程讲义、实验日志和已有
LaTeX 幻灯片整理成可编译、可审查、可追溯来源的 Beamer 源码、PDF、
审查报告和 slide-to-source ledger。

## 何时使用

适合这些场景：

- 数学 seminar、课程、组会精读、答辩、workshop、poster 或实验结果汇报；
- 幻灯片需要保留定理假设、证明状态、符号、引用、公式、算法、图表和数值结果；
- 希望从模板目录中选择一个可维护的 Beamer 模板，并用可复现命令检查编译。

模板目录覆盖通用 seminar、定理/证明报告、论文精读、优化、数值分析、算法、
概率统计、几何拓扑、代数数论、组合与图论、逻辑/基础/范畴、核心分析、PDE、
动力系统、控制系统、信息/编码/密码、课程、答辩、workshop、backup-heavy
报告、实验数据汇报和 poster。

不适合用来制作泛营销 PPT、编造没有来源支持的数学内容，或在未检查授权和学校
logo 使用边界时公开发布第三方机构模板。

## 产物

agent 应产出 Beamer source tree、可选 PDF、build/layout report、
`slide-source-ledger.md` 和修订说明。报告中要写清模板选择、编译引擎、
未解决的数学风险，以及授权或机构品牌限制。

## Skill 入口

| 文件 | 用途 |
| --- | --- |
| `SKILL.md` | 主工作流和审查规则 |
| `templates/catalog.yaml` | 模板目录 |
| `templates/preview-gallery.md` | 可视化模板选择页 |
| `templates/previews/*.png` | 真实编译的封面与内容预览 |
| `templates/packs/*/` | starter Beamer 模板 |
| `templates/slide-source-ledger.md` | 幻灯片来源 ledger |
| `templates/review-report.md` | 编译和审查报告 |
| `references/` | 来源索引、数学领域模式和模板政策 |
| `agents/openai.yaml` | OpenAI/Codex 元数据 |

## 安装

复制给你的 coding agent：

```text
请帮我安装 `math-beamer` skill。

仓库：https://github.com/VeryMath/AI4Math-Writing.git
分支：main
Skill 路径：math-beamer

请读取包内 README 和 SKILL.md，安装包含 SKILL.md 的目录，验证 `$math-beamer`
是否可发现，并告诉我是否需要重启 agent。
```

如果从 AI4Math Skill Library 镜像使用，就安装当前这个包含 `SKILL.md` 的目录。

## 快速开始

```text
Use this repository's math-beamer workflow.

Read:
- SKILL.md
- templates/preview-gallery.md
- templates/catalog.yaml
- references/template-policy.md

Goal:
根据给定论文笔记制作 25 分钟数学报告。

Target:
<论文源码、笔记目录或已有 Beamer 项目>

Constraints:
- 先 inspect；
- 起草前先查看预览图库，再选择模板和 slide budget；
- 编译或使用机构品牌前先询问；
- 保留 slide-source ledger。
```

## 如何交互

常用 checkpoint：

| 决策词 | 含义 |
| --- | --- |
| `approve` | 执行下一步 |
| `revise` | 先修改计划 |
| `reject` | 停止当前路线 |
| `skip` | 跳过当前阶段 |
| `stop` | 结束并总结状态 |

建议第一次这样开始：

```text
First inspect the source packet and template catalog only. Then tell me:
1. which Beamer workflow applies;
2. which template you recommend;
3. which files or commands you would use;
4. what checkpoint needs my approve / revise / reject / skip decision.
```

## Workflow And Outputs

```text
source packet
  -> 数学类型和听众分析
  -> 模板选择
  -> talk thesis 和 section map
  -> 代表性样张
  -> 完整 deck
  -> latexmk 编译
  -> PDF/log/source audit
  -> 修订报告
```

耐久产物通常放在：

```text
outputs/<run_id>/
```

## 安全和审查规则

- 保留定理假设、量词、定义域和证明状态。
- 明确标注 conjecture、heuristic、example、experiment 和 future work。
- 不编造引用、定理依赖或实验数字。
- 公开模板不能含本机绝对路径或私有文件。
- 下载来的模板只有在 license、机构品牌和个人信息都检查后才能 vendoring。
- 获得允许后用 `latexmk` 编译，并报告确切命令。

## 仓库结构

```text
SKILL.md
README.md
README.zh-CN.md
LICENSE
requirements-preview.txt
agents/openai.yaml
references/
templates/
  catalog.yaml
  packs/
```

## 依赖

仅使用 Skill 指令和已有预览图不需要 Python 运行时依赖。重新生成预览图需要：

- Python 3.9 或更高版本，以及 `requirements-preview.txt` 中声明的包；
- `latexmk`、`pdflatex` 和 `xelatex`；
- Poppler 提供的 `pdftoppm`；
- starter packs 使用的 TeX 宏包：Beamer、CTeX/`ctexbeamer`、AMSMath、
  AMS symbols/theorem support、Booktabs、PGF/TikZ、PGFPlots 和
  `beamerposter`。

安装 Python 依赖：

```bash
python3 -m pip install -r requirements-preview.txt
```

包内模板不需要网络访问、shell escape 或本机绝对路径。

## 维护检查

在 `AI4Math-Writing` 仓库根目录运行：

```bash
python3 -m unittest discover -s tests -v
```

修改模板时，还要用对应 `template.yaml` 中声明的引擎编译相关 starter deck。

## 许可证

本包按 `LICENSE` 中的 MIT License 发布。该声明仅适用于 VeryMath
有权再分发的包内内容。第三方模板在其许可证、机构品牌和个人数据边界确认前，
仅作为来源索引，不作为包内可再分发模板。

## 贡献者

课程贡献者：**Conan Xu**。课程版来源和整理记录见
[`PROVENANCE.yaml`](PROVENANCE.yaml) 与
[`NORMALIZATION.md`](NORMALIZATION.md)。
