# 🏰 Family Travel Planner (家庭多代亲子自驾游规划专家)

[![Antigravity Skill](https://img.shields.io/badge/Antigravity-Skill-6366F1.svg)](https://github.com/Rouen007/family-travel-planner)
[![Universal Multi-Destination](https://img.shields.io/badge/Travel-Universal%20Archetypes-10b981.svg)](examples/)
[![Claude Code Compatible](https://img.shields.io/badge/Claude%20Code-Compatible-D97706.svg)](https://claude.ai/)
[![Cursor Rules](https://img.shields.io/badge/Cursor-Rules-0ea5e9.svg)](https://cursor.com/)
[![OpenAI Codex / AGENTS.md](https://img.shields.io/badge/OpenAI-Codex%20%2F%20Agents-10b981.svg)](https://openai.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

**`family-travel-planner`** 是一款专为 **多代同行家庭（0-6岁幼童 ＋ 50+长辈 ＋ 年轻父母）** 设计的通用 AI 旅游规划 Skill。

本工具**完全不局限于单一目的地**，内置 **4 大通用旅行场景方法论**（主题乐园、海岛沙滩、古都研学、山水自然自驾），支持 **Google Antigravity、Claude Code、Cursor、OpenAI Codex、Windsurf** 等全主流 Agent Harness 架构，一键自动输出 **出版级 Word 原生文档**、**手机 2K 视网膜超清长图海报** 与 **交互式单页网站**。

---

## 🌍 四大多代家庭通用旅行场景库 (Universal Archetypes)

| 旅行场景流派 | 适用典型目的地 | 核心适幼与适老规划重点 | 官方示例 |
| :--- | :--- | :--- | :--- |
| 🎡 **主题乐园度假型** | 迪士尼、环球影城、长隆海洋王国、乐高乐园 | 宝宝精确身高项目匹配、早场温和项目、室内冷气大剧场、爸妈单人通道单刷。 | [`examples/shanghai_sample.md`](examples/shanghai_sample.md) |
| 🏖️ **海岛沙滩度假型** | 三亚、万宁、厦门、青岛、普吉岛 | 一线海景亲子酒店、海滩挖沙推车无障碍步道、防晒与婴幼儿涉水装备、海鲜防坑避雷。 | [`examples/sanya_beach_resort.md`](examples/sanya_beach_resort.md) |
| 🏛️ **历史文化古都型** | 北京故宫、西安陕历博、南京、苏州园林 | 故宫/展馆门票定时秒杀、长辈平缓坡道无障碍动线、地方特色清淡老字号、古风亲子穿搭。 | [`examples/beijing_culture_universal.md`](examples/beijing_culture_universal.md) |
| 🌲 **山水自然自驾型** | 莫干山、千岛湖、安吉、川西、桂林阳朔 | 纯电/油车沿途风景线补能规划、竹林氧吧推车步道、农家土菜老幼适口、独栋民宿泳池。 | [`examples/moganshan_nature_roadtrip.md`](examples/moganshan_nature_roadtrip.md) |

---

## 🌟 核心价值主张 (Core Highlights)

- 👶 **幼童适龄与身高精准匹配**：根据宝宝精确身高（如 92cm），智能筛选无身高限制与门槛项目，规避惊险排队雷区。
- 👵 **50+ 长辈体贴慢游**：避开陡坡台阶与高强度暴走，精选地道清淡热汤餐饮，舒适度优先。
- ⚡ **纯电 / 燃油自驾差异化算法**：
  - **纯电车 (EV)**：拒绝服务区暴晒，规划“途径大型商场地库极充 + 吃饭换尿布 + 积分抵扣停车费”；
  - **燃油车**：极简加油提示（出发前加满一箱油，600-800km 续航无忧），专注停车与早晚高峰限行规避。
- 💤 **14:00—16:00 黄金午睡雷打不动**：大床深度午睡 / 推车室内冷气大剧场双模式，爸妈单刷。
- 💰 **全网省钱买券矩阵**：大众点评本地团购 ＋ 官方/闲鱼餐饮电子券，全家直省 30% 以上。
- 🎨 **全家红黑白高颜值协调穿搭**：视觉 C 位亲子呼应，出片高级整齐。

---

## 🚀 跨平台一键安装与使用 (Installation)

### 1. Google Antigravity 安装
```bash
git clone https://github.com/Rouen007/family-travel-planner.git ~/.gemini/antigravity/skills/family-travel-planner
```

### 2. Claude Code / Cursor / Windsurf / Codex
在项目根目录打开本仓库，自动读取 `CLAUDE.md`、`.cursorrules` 或 `AGENTS.md` 即可生效。

---

## ⚙️ 核心构建脚本使用指南 (CLI Scripts)

通过内置 CLI 脚本一键输出 3 种标准交付物：

```bash
# 一键编译指定规划文件的 Word + 网页 + 手机超清长图
python3 scripts/cli.py all --input examples/sanya_beach_resort.md --output-dir dist/ --view

# 仅生成出版级 Word 文档
python3 scripts/cli.py docx --input examples/beijing_culture_universal.md --output-dir dist/

# 仅渲染手机 2K 视网膜超清长图
python3 scripts/cli.py poster --input examples/moganshan_nature_roadtrip.md --output-dir dist/ --view
```

---

## 📁 目录架构说明 (Architecture)

```
family-travel-planner/
├── SKILL.md                          # 🪐 Antigravity 核心大脑规则
├── CLAUDE.md                         # 🤖 Claude Code 核心执行规范
├── .cursorrules                      # 💻 Cursor IDE 规则配置
├── .windsurfrules                    # 🌊 Windsurf 规则配置
├── AGENTS.md                         # ⚡ OpenAI Codex / 通用 Agent 标准
├── README.md                         # 📖 通用开源说明书
├── requirements.txt                  # 📦 依赖规范
├── pyproject.toml                    # 📦 项目构建元数据
├── LICENSE                           # 📄 MIT 开源许可证
├── examples/                         # 🌍 四大多代家庭目的地示例库
│   ├── sanya_beach_resort.md         # 🏖️ 三亚海岛亲子度假示例
│   ├── beijing_culture_universal.md  # 🏛️ 北京故宫+环球影城示例
│   ├── moganshan_nature_roadtrip.md  # 🌲 莫干山山水自驾示例
│   └── shanghai_sample.md            # 🎡 上海迪士尼自驾示例
├── scripts/                          # ⚙️ 自动化多端渲染 Python 脚本库
│   ├── cli.py                        # 🚀 统一命令行工具
│   ├── parser.py                     # 🔍 通用 Markdown 解析器
│   ├── build_styled_docx.py          # 📄 出版级 Word 原生文档编译器
│   ├── generate_web.py               # 🌐 响应式单页 Web 网页生成器
│   └── render_poster.py              # 🖼️ 2K 手机超清长图海报渲染器
├── templates/                        # 📑 标准化规划模板库
│   ├── questionnaire.md              # 📋 行前 4 大核心维度问卷模板
│   ├── itinerary_template.md         # 📅 逐日时间轴 Markdown 模板
│   ├── deals_matrix_template.md      # 💰 省钱买券对比表模板
│   ├── outfit_guide_template.md      # 👗 红黑白穿搭黄金法则模板
│   ├── poster_template.html          # 🎨 移动端长图海报前端 HTML 模板
│   └── web_template.html             # 🌐 响应式 Web SPA 前端模板
└── tests/                            # 🧪 自动化测试套件
    └── test_pipeline.py              # 自动化单元测试 (100% 通过)
```

---

## 📄 开源许可证 (License)

本项目采用 [MIT License](LICENSE) 开源许可证。
