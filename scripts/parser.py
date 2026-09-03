"""
Universal Destination-Agnostic Travel Markdown Parser
Intelligently extracts sections, tables, family age cohorts, timelines, and metadata from ANY travel markdown plan.
Zero-recursion safe and robust.
"""
import re
import os

def _get_default_generic_data():
    """Returns a completely safe static baseline dictionary with zero recursion."""
    return {
        "title": "家庭亲子多代自驾游保姆级完整规划",
        "subtitle": "轻松慢游 · 保证14:00-16:00午睡 · 老幼胃口兼顾 · 零特种兵赶路",
        "dates": "出行规划",
        "stats": [
            {"label": "🏨 大本营住宿", "val": "精选品质酒店", "desc": "舒适安静+地理便捷"},
            {"label": "⚡ 补能/出行", "val": "优选极速补能", "desc": "吃饭顺便充+免停车费"},
            {"label": "⏰ 规律作息", "val": "14:00 - 16:00", "desc": "每日锁定黄金深度午休"},
            {"label": "👗 全家穿搭", "val": "协调视觉色系", "desc": "亲子呼应+沉稳显瘦"}
        ],
        "outfits": [
            {"name": "👧 宝贝", "tag": "全家视觉 C 位", "bg": "FFF5F5", "border": "FECDD3", "desc": "• 主装：亮色舒适透气亲子套装/小裙子\n• 配饰：软萌遮阳帽 / 亲子发带\n• 鞋袜：轻便透气防滑运动鞋"},
            {"name": "👩 妈妈", "tag": "上亮下暗 · 显瘦", "bg": "FAFAFA", "border": "CBD5E1", "desc": "• 上装：修身亮色短袖/法式衬衫\n• 下装：高腰垂感长裙/阔腿裤\n• 配饰：时尚太阳镜 + 亲子同色包包"},
            {"name": "👨 爸爸", "tag": "清爽挺拔 · 型男", "bg": "F0F9FF", "border": "BFDBFE", "desc": "• 上装：纯色/微印花透气纯棉T恤\n• 下装：黑色/深灰轻薄透气休闲裤\n• 配饰：偏光墨镜 + 缓震支撑跑鞋"}
        ],
        "prep_rows": [
            ("D-15 ~ D-10", "核心景区门票与酒店确认", "官方平台 / OTA", "提前核实家庭实名信息；确认酒店婴儿床与接驳车班次。"),
            ("D-7 准点", "热门博物馆 / 特殊展馆抢票", "官方公众号 / 小程序", "提前录入全家身份证信息，定好提前5分钟闹钟准时秒杀！"),
            ("D-2", "餐饮优惠券 / 门票电子券", "大众点评 / 官方优惠平台", "提前选购未核销随时退的优惠套餐券，保存二维码至手机相册。"),
            ("D-1 晚上", "车辆与行李终极检查", "就近加满油 / 纯电充满100%", "核查全员身份证原件、医保卡、常备药美林、加长充电线。"),
            ("出行当天", "错峰启程 ＆ 提前在线取号", "导航软件 ＋ 点评在线取号", "提前查看当日路况避开高峰；临近饭点在线取号减少等位。")
        ],
        "days": [
            {
                "day_tag": "Day 1",
                "day_title": "启程抵达 ➔ 办理入住 ➔ 深度午休 ➔ 悠闲夜游",
                "color_hex": "E11D48",
                "items": [
                    ("上午", "自驾/高铁启程出发，平稳前往目的地。"),
                    ("中午", "品尝当地地道特色午餐，大本营客栈/酒店办理入住。"),
                    ("14:00 - 16:00", "拉上遮光窗帘，全家舒适大床深度午睡彻底回血！"),
                    ("傍晚与夜间", "漫步特色历史街区或滨海步道，打卡地道晚市特色美食。")
                ]
            },
            {
                "day_tag": "Day 2",
                "day_title": "核心景点沉浸游 ➔ 特色大餐 ➔ 黄金午休 ➔ 非遗/踏浪",
                "color_hex": "2563EB",
                "items": [
                    ("上午", "黄金早场打卡标志性景点或非遗体验，人少拍照绝美。"),
                    ("中午", "享用当地特色能量大餐，品味招牌风味。"),
                    ("14:00 - 16:00", "避开正午烈日，回酒店房间舒适午睡休整。"),
                    ("傍晚与夜间", "夕阳漫步或观赏特色夜景秀，享受温馨家庭夜晚。")
                ]
            },
            {
                "day_tag": "Day 3",
                "day_title": "文化探访 ➔ 老字号午餐 ➔ 全家合影 ➔ 顺畅返程",
                "color_hex": "059669",
                "items": [
                    ("上午", "睡到自然醒，悠闲退房，打卡清幽文化古迹或公园。"),
                    ("中午", "品尝老字号非遗风味小吃或家常菜。"),
                    ("下午", "地标前留下美好全家福合影，启程平稳返家。")
                ]
            }
        ],
        "deals": [
            ("首日午餐：地道特色餐厅", "招牌必点高蛋白适口菜品", "约 ¥260", "约 ¥198", "省 ¥60", "【大众点评】 提前在线排队 + 买精选套餐"),
            ("首日晚餐：舒适清淡晚餐", "热汤生滚粥、蒸点、清炒时蔬", "约 ¥280", "约 ¥220", "省 ¥60", "【大众点评】 88 折代金券买单"),
            ("次日午餐：景区核心大餐", "招牌大套餐 (分量足老幼共享)", "¥118/份", "¥68-78/份", "省 ¥80", "【官方/正规优惠】 提前准备电子核销券"),
            ("次日晚餐：地道暖胃正餐", "热汤面、慢炖滋补煲、清淡肉类", "¥108/份", "¥68-75/份", "省 ¥70", "【大众点评】 晚市特惠套餐"),
            ("返程午餐：非遗特色小吃", "老字号传统经典点心组合", "约 ¥110", "约 ¥75", "省 ¥35", "【大众点评/美团】 双人超值经典组合券")
        ],
        "parking": [
            ("途径停留点", "商场地库", "商场地下停车场", "6-8元/h (消费抵扣)", "车位充裕，支持超快充，配套五星母婴室。"),
            ("度假大本营", "酒店专属车库", "大本营酒店停车场", "住客免费", "免停车费，直通景区接驳车或步行可达。"),
            ("核心打卡点", "景区配套停车场", "景区地面/地下停车场", "按次/按小时收费", "提前导航精准入口，无障碍电梯直达。"),
            ("返程商业中心", "商场地库", "地标商场地下停车场", "消费积分抵扣", "临近高速路口，吃完饭极速上高速顺畅返程。")
        ],
        "checklist": [
            "所有成人有效身份证原件（景区/酒店必刷）",
            "儿童实体医保卡 ＋ 手机相册存好户口本及出生证明照片",
            "全家协调出行穿搭（红白亲子呼应 + 黑色下装显瘦）",
            "随车清洁垃圾袋 ＋ 湿巾 ＋ 消毒棉片",
            "儿童常用退烧药美林（确认有效期） ＋ 防蚊喷雾",
            "随行加长快充数据线×3-4条",
            "便携式折叠轻便推车 ＋ 遮阳伞 ＋ 挂式小风扇",
            "一次性全包围马桶垫 ＋ 一次性围兜",
            "儿童常温果泥吸吸乐 / 益智绘本贴纸（路途安抚神器）"
        ],
        "footer": {
            "wish": "祝全家旅途顺畅 · 拍照绝美出片 · 留下最美好的家庭回忆！✨",
            "hotel": "住宿大本营：请确认酒店名称与前台联系电话",
            "hotlines": ["🚨 当地妇女儿童医院急诊", "🏥 当地三甲综合医院", "🎡 景区/大本营官方服务热线"]
        }
    }

def parse_travel_markdown(file_path):
    if not file_path or not os.path.exists(file_path):
        return _get_default_generic_data()

    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    data = _get_default_generic_data()

    # 1. Parse Title, Subtitle, Dates
    m_title = re.search(r"^#\s+(.+)$", content, re.M)
    if m_title:
        data["title"] = m_title.group(1).strip()

    m_sub = re.search(r"^>\s*\*\*规划定位\*\*[：:]\s*(.+)$", content, re.M)
    if m_sub:
        data["subtitle"] = m_sub.group(1).strip()

    m_dates = re.search(r"^>\s*\*\*行程日期\*\*[：:]\s*(.+)$", content, re.M)
    if m_dates:
        data["dates"] = m_dates.group(1).strip()

    # 2. Intelligent Family Demographics Detection
    full_text = content.lower()
    has_seniors = any(k in content for k in ["外婆", "奶奶", "姥姥", "爷爷", "长辈", "老人"])
    
    # Detect child age
    child_age = 2
    m_age = re.search(r"(\d{1,2})\s*岁", content)
    if m_age:
        child_age = int(m_age.group(1))

    is_girl = any(k in content for k in ["女娃", "女宝", "女儿", "小公主"])
    child_name = f"👧 {child_age}岁{'女娃' if is_girl else '宝宝'}" if is_girl else f"👶 {child_age}岁宝宝"

    # Adapt outfits based on detected family members
    outfits = []
    if child_age <= 2:
        outfits.append({
            "name": child_name,
            "tag": "全家童话 C 位",
            "bg": "FFF5F5",
            "border": "FECDD3",
            "desc": "• 连体：亮色亲子系软棉娃娃裙/连体服\n• 配饰：软萌防晒帽 / 吸汗发带\n• 鞋袜：透气防滑软底学步小红鞋"
        })
    elif 3 <= child_age <= 6:
        outfits.append({
            "name": child_name,
            "tag": "国风小公主 C 位" if is_girl else "活泼小帅哥",
            "bg": "FFF5F5",
            "border": "FECDD3",
            "desc": "• 主装：精美儿童马面裙 / 国风汉服 / 亮色洋装\n• 配饰：非遗小簪花围 / 萌趣蝴蝶结\n• 鞋袜：轻便舒适防滑跑鞋 (方便奔跑踏浪)"
        })
    else:
        outfits.append({
            "name": child_name,
            "tag": "阳光活力大童",
            "bg": "FFF5F5",
            "border": "FECDD3",
            "desc": "• 主装：排汗速干运动短袖 + 工装短裤\n• 配饰：运动遮阳帽 + 亲子胸包\n• 鞋袜：专业缓震运动鞋"
        })

    outfits.append({
        "name": "👩 妈妈",
        "tag": "上亮下暗 · 显瘦",
        "bg": "FAFAFA",
        "border": "CBD5E1",
        "desc": "• 上装：正红/暖色修身短袖 / 国风衬衫\n• 下装：优雅黑色高腰中长裙 / 垂感阔腿裤\n• 配饰：精致发饰 / 偏光墨镜 + 亲子同色系"
    })
    outfits.append({
        "name": "👨 爸爸",
        "tag": "清爽挺拔 · 型男",
        "bg": "F0F9FF",
        "border": "BFDBFE",
        "desc": "• 上装：米奇/纯色透气纯棉白T恤\n• 下装：黑色/深灰轻薄透气休闲长裤\n• 配饰：偏光太阳镜 + 舒适运动鞋"
    })

    if has_seniors:
        senior_title = "👵 50+外婆" if "外婆" in content else ("👵 奶奶" if "奶奶" in content else "👵 50+长辈")
        outfits.append({
            "name": senior_title,
            "tag": "温婉大方 · 显白",
            "bg": "FEFCE8",
            "border": "FEF08A",
            "desc": "• 上装：象牙白/奶杏色新中式短袖衬衫\n• 下装：黑色垂感宽松阔腿长裤\n• 配饰：舒适轻便防滑健步鞋"
        })

    data["outfits"] = outfits

    # 3. Dynamic Timeline Extraction
    day_matches = list(re.finditer(r"(?:###|##)\s*(Day\s*\d+[^:\n]+?)(?:\n|$)([\s\S]*?)(?=(?:###|##)\s*Day\s*\d+|\Z|##\s*[^D\d])", content, re.IGNORECASE))
    colors = ["E11D48", "2563EB", "059669", "D97706", "7C3AED", "0D9488"]
    
    parsed_days = []
    for idx, dm in enumerate(day_matches):
        raw_header = dm.group(1).strip()
        body = dm.group(2).strip()
        
        header_parts = re.split(r"[：:·\-\➔\s]+", raw_header, maxsplit=1)
        tag = header_parts[0] if len(header_parts) > 0 else f"Day {idx+1}"
        d_title = header_parts[1] if len(header_parts) > 1 else raw_header
        
        items = []
        for line in body.split("\n"):
            line = line.strip()
            if line.startswith(("-", "*", "•")):
                clean_line = re.sub(r"^[-*•]\s*", "", line)
                t_match = re.match(r"(?:\*\*)?([0-9]{1,2}:[0-9]{2}(?:\s*[-—~]\s*[0-9]{1,2}:[0-9]{2})?|[上下]午|清晨|傍晚|夜间)(?:\*\*)?[：:\s|｜]+([\s\S]+)", clean_line)
                if t_match:
                    items.append((t_match.group(1).strip(), t_match.group(2).strip()))
                else:
                    items.append(("行程", clean_line))
                    
        if items:
            parsed_days.append({
                "day_tag": tag,
                "day_title": d_title,
                "color_hex": colors[idx % len(colors)],
                "items": items
            })

    if parsed_days:
        data["days"] = parsed_days

    # 4. Dynamic Markdown Table Parser (Generic Helper)
    def extract_markdown_table(sec_pattern):
        m_sec = re.search(sec_pattern, content, re.I)
        if not m_sec: return []
        sec_text = m_sec.group(1)
        table_lines = [l.strip() for l in sec_text.split("\n") if l.strip().startswith("|") and l.strip().endswith("|")]
        if len(table_lines) < 3: return []
        # skip header and delimiter lines
        rows = []
        for l in table_lines[2:]:
            cols = [c.strip() for c in l.split("|")[1:-1]]
            if any(cols):
                rows.append(cols)
        return rows

    # 5. Dynamic Prep Extraction (Table or Bullet Points)
    prep_table = extract_markdown_table(r"##\s*[^#\n]*?(?:行前|抢票|时间表|准备)[^#\n]*?\n([\s\S]*?)(?=##|\Z)")
    if prep_table:
        data["prep_rows"] = [tuple(r[:4]) if len(r) >= 4 else tuple(r + [""] * (4 - len(r))) for r in prep_table]
    else:
        # Check for bullet points under prep section
        m_prep_sec = re.search(r"##\s*[^#\n]*?(?:行前|抢票|时间表|准备)[^#\n]*?\n([\s\S]*?)(?=##|\Z)", content, re.I)
        if m_prep_sec:
            p_bullets = []
            for line in m_prep_sec.group(1).split("\n"):
                line = line.strip()
                if line.startswith(("-", "*")):
                    clean = re.sub(r"^[-*]\s*", "", line)
                    parts = re.split(r"[：:]", clean, maxsplit=1)
                    if len(parts) == 2:
                        node = parts[0].strip()
                        detail = parts[1].strip()
                        p_bullets.append((node, detail[:25] + "..." if len(detail) > 25 else detail, "官方/权威平台", detail))
            if p_bullets:
                data["prep_rows"] = p_bullets

    # 6. Dynamic Deals & Dining Extraction
    dining_table = extract_markdown_table(r"##\s*[^#\n]*?(?:美食|餐饮|买券|省钱)[^#\n]*?\n([\s\S]*?)(?=##|\Z)")
    if dining_table:
        data["deals"] = [tuple(r[:6]) if len(r) >= 6 else tuple(r + [""] * (6 - len(r))) for r in dining_table]
    else:
        # Check for bullet items under dining section
        m_dine = re.search(r"##\s*[^#\n]*?(?:美食|餐饮|买券|省钱)[^#\n]*?\n([\s\S]*?)(?=##|\Z)", content, re.I)
        if m_dine:
            d_bullets = []
            for line in m_dine.group(1).split("\n"):
                line = line.strip()
                if line.startswith(("-", "*")):
                    clean = re.sub(r"^[-*]\s*", "", line)
                    parts = re.split(r"[：:]", clean, maxsplit=1)
                    if len(parts) == 2:
                        d_target = parts[0].replace("*", "").strip()
                        d_dishes = parts[1].strip()
                        d_bullets.append((d_target, d_dishes, "市价约¥200+", "团购优惠价", "省30%+", "【大众点评/本地名店】 招牌必点"))
            if d_bullets:
                data["deals"] = d_bullets

    # 7. Dynamic Checklist Extraction
    m_check = re.search(r"##\s*[^#\n]*?(?:清单|准备物品|打勾|装备)[^#\n]*?\n([\s\S]*?)(?=##|\Z)", content, re.I)
    if m_check:
        chk_items = []
        for line in m_check.group(1).split("\n"):
            line = line.strip()
            if line.startswith(("- [ ]", "- [x]", "- [X]")):
                clean = re.sub(r"^-\s*\[[ xX]\]\s*", "", line).strip()
                if clean: chk_items.append(clean)
            elif line.startswith(("-", "*")):
                clean = re.sub(r"^[-*]\s*", "", line).strip()
                if clean and not clean.startswith("#"): chk_items.append(clean)
        if chk_items:
            data["checklist"] = chk_items

    # 8. Dynamic Parking Extraction
    park_table = extract_markdown_table(r"##\s*[^#\n]*?(?:停车|交通|补能|自驾)[^#\n]*?\n([\s\S]*?)(?=##|\Z)")
    if park_table:
        data["parking"] = [tuple(r[:5]) if len(r) >= 5 else tuple(r + [""] * (5 - len(r))) for r in park_table]

    return data
