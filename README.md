# 🏰 Universal Travel Planner (全场景旅行度假规划专家)

[![Antigravity Skill](https://img.shields.io/badge/Antigravity-Skill-6366F1.svg)](https://github.com/Rouen007/family-travel-planner)
[![Universal Multi-Persona](https://img.shields.io/badge/Personas-Couples%20%7C%20Family%20%7C%20Solo-10b981.svg)](examples/)
[![Claude Code Compatible](https://img.shields.io/badge/Claude%20Code-Compatible-D97706.svg)](https://claude.ai/)
[![Cursor Rules](https://img.shields.io/badge/Cursor-Rules-0ea5e9.svg)](https://cursor.com/)
[![OpenAI Codex / AGENTS.md](https://img.shields.io/badge/OpenAI-Codex%20%2F%20Agents-10b981.svg)](https://openai.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

**`family-travel-planner`** 是一款功能完备、支持全场景与全人群的通用 AI 旅游规划 Skill。

本工具不仅支持 **多代同堂亲子游**，更全面支持 **年轻恋人/蜜月轻奢度假**、**好友结伴** 与 **个人自由行**。内置 **4 大出行人群模型**、**4 大目的地流派** 与 **多模态交通引擎**，原生适配 **Google Antigravity、Claude Code、Cursor、OpenAI Codex、Windsurf** 等全主流 Agent Harness 架构，一键自动输出 **出版级 Word 原生文档**、**手机 2K 视网膜超清长图海报** 与 **交互式单页网站**。

---

## 👥 四大出行人群模型 (Universal Personas)

| 出行人群画像 | 适用场景 | 核心规划偏好与算法定制 | 官方示例 |
| :--- | :--- | :--- | :--- |
| 💑 **恋人蜜月 / 浪漫二人世界** | 结婚纪念日、情侣蜜月、轻奢度假 | 纯双人高颜值卡片、避开特种兵赶路、雪山/海景落地窗设计酒店、烛光私房晚宴、微醺酒庄、特色伴手礼淘宝。 | [`examples/georgia_couples_romantic.md`](examples/georgia_couples_romantic.md) |
| 👶 **多代亲子 / 三代同堂** | 幼童 (0-2岁) + 长辈 (50+) + 父母 | 推车无障碍通道、14:00-16:00 黄金午睡保护、老少清淡软烂餐饮、乐园身高阈值精准筛选。 | [`examples/shanghai_sample.md`](examples/shanghai_sample.md) |
| 👧 **中童活力探索 (3-6岁)** | 学龄前儿童 + 年轻三口之家 | 非遗沉浸动手体验（木偶戏/小公主簪花/沙滩挖沙抓蟹）、自选小料美食、弹性午休。 | [`examples/quanzhou_minnan_heritage.md`](examples/quanzhou_minnan_heritage.md) |
| 🌲 **自驾山水 / 户外吸氧** | 全家老小或朋友结伴自驾 | 纯电/油车沿途风景线补能规划、竹林步道、独栋民宿泳池、农家土菜老少适口。 | [`examples/moganshan_nature_roadtrip.md`](examples/moganshan_nature_roadtrip.md) |

---

## 🌍 四大目的地场景库 (Destination Archetypes)

- 🏰 **免签浪漫 / 异域轻奢型**：格鲁吉亚高加索雪山、欧洲古堡、东南亚海岛（含外汇换汇防坑、境外刷卡策略、自驾 vs 私人包车决策）。
- 🎡 **主题乐园度假型**：迪士尼、环球影城、长隆海洋王国（含门票抢票倒计时、清凉大剧场吹冷气、单人通道单刷）。
- 🏖️ **海岛沙滩度假型**：三亚亚龙湾、万宁、普吉岛（含一线海景亲子房、避烈日空调午休、海滩挖沙、海鲜防坑）。
- 🏛️ **历史文化古都型**：泉州世遗、北京故宫、西安陕历博、南京（含国潮汉服马面裙穿搭、非遗手作、老字号老饕分级点餐）。

---

## 🌟 核心功能特色 (Core Highlights)

- 智能人群识别：根据出行描述自动匹配穿搭卡片（恋人仅出双人卡片，亲子自动适配儿童年龄阶段）。
- 动态版块隐藏：无自驾需求时**自动隐去停车位模块**，有购物行程时**自动生成特色纪念品与伴手礼淘货攻略**。
- 完整行前清单：包含出境免签护照原件、新版美钞、双币卡、转换插头与打车软件。
- 出版级 Word 原生文档：带 Callout 卡片框、斑马纹表格与多列色块网格，无损导入 Google Docs。
- 手机 2K 超清长图：利用 Headless Chrome 动态计算高度，智能自动裁剪白边，一键 AirDrop 存入手机。
- 零依赖轻量微模板引擎：内置纯标准库 AST Tokenizer，即使未安装 `jinja2` 也能 100% 像素级对齐渲染。

---

## 🚀 跨平台一键安装 (Installation)

### 1. Google Antigravity 安装
```bash
git clone https://github.com/Rouen007/family-travel-planner.git ~/.gemini/antigravity/skills/family-travel-planner
```

### 2. Claude Code / Cursor / Windsurf / Codex
直接在项目根目录打开本仓库，自动读取 `CLAUDE.md`、`.cursorrules` 或 `AGENTS.md` 即可生效。

---

## ⚙️ 核心构建脚本使用指南 (CLI Scripts)

```bash
# 1. 编译格鲁吉亚恋人浪漫度假成果（Word + 网页 + 手机长图）
python3 scripts/cli.py all --input examples/georgia_couples_romantic.md --output-dir dist/ --view

# 2. 编译三亚海岛亲子度假成果
python3 scripts/cli.py all --input examples/sanya_beach_resort.md --output-dir dist/

# 3. 运行全套自动化测试
python3 tests/test_pipeline.py
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
├── examples/                         # 🌍 全场景示例库
│   ├── georgia_couples_romantic.md   # 💑 格鲁吉亚恋人浪漫轻奢示例
│   ├── quanzhou_minnan_heritage.md   # 👧 泉州世遗与5岁小公主簪花示例
│   ├── sanya_beach_resort.md         # 🏖️ 三亚海岛亲子度假示例
│   ├── beijing_culture_universal.md  # 🏛️ 北京故宫+环球影城示例
│   ├── moganshan_nature_roadtrip.md  # 🌲 莫干山山水自驾示例
│   └── shanghai_sample.md            # 🎡 上海迪士尼自驾示例
├── scripts/                          # ⚙️ 自动化多端渲染 Python 脚本库
│   ├── cli.py                        # 🚀 统一命令行工具
│   ├── parser.py                     # 🔍 通用 Markdown 解析器
│   ├── renderer.py                   # ⚡ 零依赖 AST 微模板渲染器
│   ├── build_styled_docx.py          # 📄 出版级 Word 原生文档编译器
│   ├── generate_web.py               # 🌐 响应式单页 Web 网页生成器
│   └── render_poster.py              # 🖼️ 2K 手机超清长图海报渲染器
├── templates/                        # 📑 标准化规划模板库
│   ├── questionnaire.md              # 📋 行前 4 大核心维度问卷模板
│   ├── itinerary_template.md         # 📅 逐日时间轴 Markdown 模板
│   ├── deals_matrix_template.md      # 💰 省钱买券对比表模板
│   ├── outfit_guide_template.md      # 👗 出行穿搭黄金法则模板
│   ├── poster_template.html          # 🎨 移动端长图海报前端 HTML 模板
│   └── web_template.html             # 🌐 响应式 Web SPA 前端模板
└── tests/                            # 🧪 自动化测试套件
    └── test_pipeline.py              # 自动化单元测试 (100% 通过)
```

---

## 📄 开源许可证 (License)

本项目采用 [MIT License](LICENSE) 开源许可证。
