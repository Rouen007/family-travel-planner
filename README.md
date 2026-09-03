# 🏰 Family Travel Planner (家庭多代亲子自驾游规划专家)

[![Antigravity Skill](https://img.shields.io/badge/Antigravity-Skill-6366F1.svg)](https://github.com/Rouen007/family-travel-planner)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

**`family-travel-planner`** 是一款专为 **多代同行家庭（0-6岁幼童 ＋ 50+长辈 ＋ 年轻父母）** 设计的 Antigravity 智能旅游规划 Skill。

它彻底告别走马观花式的“特种兵旅游”，通过科学的人员画像建模、油电差异化自驾算法、每日午睡刚性保护机制、老幼适口餐饮挖掘与全网买券省钱模型，一键自动输出 **出版级 Word 原生文档**、**手机 2K 视网膜超清长图海报** 与 **交互式单页网站**。

---

## 🌟 核心价值主张 (Core Highlights)

- 👶 **幼童适龄与身高精准匹配**：根据宝宝精确身高（如 92cm），智能筛选乐园无身高限制与门槛项目，规避惊险排队雷区。
- 👵 **50+ 长辈体贴慢游**：避开陡坡台阶与高强度暴走，精选地道清淡热汤餐饮，舒适度优先。
- ⚡ **纯电 / 燃油自驾差异化算法**：
  - **纯电车 (EV)**：拒绝服务区暴晒，规划“途径大型商场地库极充 18 分钟 + 吃饭换尿布 + 积分抵扣停车费（实付 0 元）”；
  - **燃油车**：极简加油提示（出发前加满一箱油，600-800km 续航无忧），专注停车与早晚高峰限行规避。
- 💤 **14:00—16:00 黄金午睡雷打不动**：大床深度午睡 / 推车室内冷气大剧场双模式，爸妈单人通道单刷。
- 💰 **全网省钱买券矩阵**：大众点评本地团购 ＋ 闲鱼乐园餐饮电子二维码，全家 3 天直省 300+ 元。
- 🎨 **全家红黑白高颜值协调穿搭**：视觉 C 位亲子呼应，出片高级整齐。

---

## 🚀 快速安装 (Installation)

将本仓库克隆至您的 Antigravity 本地技能目录：

```bash
git clone https://github.com/Rouen007/family-travel-planner.git ~/.gemini/antigravity/skills/family-travel-planner
```

克隆完成后，Antigravity 会自动识别并加载该 Skill。

---

## 💬 交互式使用流程 (How It Works)

在对话中直接发送任意旅游规划需求，例如：
> *“使用 `family-travel-planner` 帮我们全家规划一次从杭州到上海迪士尼 3 天 2 晚的自驾游。”*

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
├── SKILL.md                          # 📘 Skill 核心指南与决策引擎规范
├── README.md                         # 📖 完整使用与开源说明文档
├── scripts/                          # ⚙️ 自动化渲染与构建 Python 脚本库
│   ├── build_styled_docx.py          # 📄 出版级 Word 原生文档编译器 (支持 Google Docs)
│   └── render_poster.py              # 🖼️ 2K 手机超清长图海报渲染器 (Headless Chrome)
└── templates/                        # 📑 规划模板库
    ├── questionnaire.md              # 📋 行前 4 大核心维度问卷模板
    ├── itinerary_template.md         # 📅 3天逐日保姆级时间轴 Markdown 模板
    ├── deals_matrix_template.md      # 💰 点评与闲鱼省钱买券对比表模板
    ├── outfit_guide_template.md      # 👗 红黑白全家穿搭黄金法则模板
    └── poster_template.html          # 🎨 移动端长图海报前端 HTML 模板
```

---

## ⚙️ 核心构建脚本使用指南 (CLI Scripts)

### 1. 编译出版级 Word 原生文档 (`.docx`)
支持将规划内容编译为带 **单单元格 Callout 卡片、4 列穿搭色块网格、斑马纹表格** 的 Word 文件：
```bash
python3 scripts/build_styled_docx.py
```
> *注：生成的 `.docx` 拖入 Google Drive 可直接以原生精美排版在 Google Docs 中无损打开！*

### 2. 渲染 2K 手机超清长图海报 (`.png`)
利用本地 Headless Chrome 动态测量页面真实高度，自动裁剪边距并调出 Mac 预览：
```bash
python3 scripts/render_poster.py
```

---

## 📄 开源许可证 (License)

本项目采用 [MIT License](LICENSE) 开源许可证。
