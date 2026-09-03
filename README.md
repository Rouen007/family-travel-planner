# 🏰 Family Travel Planner (家庭多代亲子自驾游规划专家)

[![Antigravity Skill](https://img.shields.io/badge/Antigravity-Skill-6366F1.svg)](https://github.com/Rouen007/family-travel-planner)
[![Claude Code Compatible](https://img.shields.io/badge/Claude%20Code-Compatible-D97706.svg)](https://claude.ai/)
[![Cursor Rules](https://img.shields.io/badge/Cursor-Rules-0ea5e9.svg)](https://cursor.com/)
[![OpenAI Codex / AGENTS.md](https://img.shields.io/badge/OpenAI-Codex%20%2F%20Agents-10b981.svg)](https://openai.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

**`family-travel-planner`** 是一款专为 **多代同行家庭（0-6岁幼童 ＋ 50+长辈 ＋ 年轻父母）** 设计的通用 AI 旅游规划 Skill。

支持 **Google Antigravity、Claude Code、Cursor、OpenAI Codex、Windsurf** 等全主流 Agent Harness 架构，彻底告别特种兵赶路，一键自动输出 **出版级 Word 原生文档**、**手机 2K 视网膜超清长图海报** 与 **交互式单页网站**。

---

## 🌟 全主流 Harness 兼容支持 (Multi-Harness Support)

本 Skill 开箱原生支持以下所有主流 AI 编码与智能体环境：

| Harness / 平台 | 配置文件 / 载入方式 | 说明 |
| :--- | :--- | :--- |
| 🪐 **Google Antigravity** | `SKILL.md` | 克隆至 `~/.gemini/antigravity/skills/` 自动发现并加载 |
| 🤖 **Claude Code / Anthropic** | `CLAUDE.md` | 项目根目录原生识别，遵循全套规划规则与脚本 |
| 💻 **Cursor IDE** | `.cursorrules` | Cursor 对话自动载入家庭规划与省钱买券逻辑 |
| ⚡ **OpenAI Codex / ChatGPT** | `AGENTS.md` | 通用 Agent 规范与 Prompt 接口标准 |
| 🌊 **Windsurf / Cascade** | `.windsurfrules` | Windsurf 原生上下文与工作流支持 |

---

## 🚀 一键安装与配置 (Installation)

### 1. Google Antigravity 安装
```bash
git clone https://github.com/Rouen007/family-travel-planner.git ~/.gemini/antigravity/skills/family-travel-planner
```

### 2. Claude Code (Anthropic) 使用
直接在任意工程目录中引入本仓库或将 `CLAUDE.md` 放入工作区即可生效。

### 3. Cursor / Windsurf 使用
在 Cursor / Windsurf 项目中打开本仓库，自动读取 `.cursorrules` / `.windsurfrules`。

---

## 💬 交互式使用流程 (How It Works)

在任意兼容 Harness 的对话中发送旅行需求，例如：
> *“使用 `family-travel-planner` 帮我们全家（2岁宝宝92cm + 50+外婆 + 年轻父母）规划一次从杭州到上海迪士尼 3 天 2 晚的自驾游。”*

Skill 将自动进入 **标准四步规划流水线**：

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                        🏰 标准四步家庭规划流水线                                        │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ Step 1. 【前置问卷交互】 ➔ 收集出行人数、宝宝年龄/身高、长辈体能、车型续航与大本营     │
│ Step 2. 【智能路径与时间轴】 ➔ 错峰自驾、极充补能、14-16点午睡刚性保护、老幼适口餐饮   │
│ Step 3. 【省钱与穿搭矩阵】 ➔ 闲鱼/点评买券优惠表、行前抢票倒计时、全家穿搭示意图       │
│ Step 4. 【多端交付物编译】 ➔ 自动调用 Python 脚本生成 Word .docx 与手机超清长图 .png │
└────────────────────────────────────────────────────────────────────────────────────────┘
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
├── README.md                         # 📖 全平台通用开源说明书
├── scripts/                          # ⚙️ 自动化渲染 Python 脚本库
│   ├── build_styled_docx.py          # 📄 出版级 Word 原生文档编译器 (支持 Google Docs)
│   └── render_poster.py              # 🖼️ 2K 手机超清长图海报渲染器 (Headless Chrome)
└── templates/                        # 📑 5 大标准化规划模板库
    ├── questionnaire.md              # 📋 行前 4 大核心维度问卷模板
    ├── itinerary_template.md         # 📅 3天逐日保姆级时间轴 Markdown 模板
    ├── deals_matrix_template.md      # 💰 点评与闲鱼省钱买券对比表模板
    ├── outfit_guide_template.md      # 👗 红黑白全家穿搭黄金法则模板
    └── poster_template.html          # 🎨 移动端长图海报前端 HTML 模板
```

---

## ⚙️ 核心构建脚本使用指南 (CLI Scripts)

### 1. 编译出版级 Word 原生文档 (`.docx`)
```bash
python3 scripts/build_styled_docx.py
```
> *生成的 `.docx` 拖入 Google Drive 可直接以原生精美排版在 Google Docs 中无损打开！*

### 2. 渲染 2K 手机超清长图海报 (`.png`)
```bash
python3 scripts/render_poster.py
```

---

## 📄 开源许可证 (License)

本项目采用 [MIT License](LICENSE) 开源许可证。
