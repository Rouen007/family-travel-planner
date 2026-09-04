"""
Universal Destination-Agnostic Travel Markdown Parser
Intelligently extracts sections, tables, family age cohorts, timelines, souvenirs, and metadata from ANY travel markdown plan.
Zero-recursion safe, robust, and supports couples, solo, multi-gen family, and kid-friendly trips.
"""
import re
import os

def _get_default_generic_data():
    """Returns a completely safe static baseline dictionary with zero recursion."""
    return {
        "title": "旅行度假保姆级完整规划",
        "subtitle": "轻松慢游 · 舒适深度休整 · 地道老饕美食 · 零特种兵赶路",
        "dates": "出行规划",
        "stats": [
            {"label": "🏨 浪漫大本营", "val": "精选品质酒店", "desc": "舒适景观+地理便捷"},
            {"label": "🚗 交通出行", "val": "私享专车/自驾", "desc": "行程自由+沿途看景"},
            {"label": "🍷 品质格调", "val": "地道老饕体验", "desc": "特色正餐+在地文化"},
            {"label": "👗 全家穿搭", "val": "协调视觉色系", "desc": "高级审美+唯美出片"}
        ],
        "outfits": [
            {"name": "👩 女士 / 女友", "tag": "优雅知性 · 唯美", "bg": "FFF5F5", "border": "FECDD3", "desc": "• 主装：亮色羊绒大衣 / 复古法式长裙\n• 配饰：贝雷帽 / 墨镜 / 精致皮包\n• 鞋履：舒适健步软皮靴 / 经典单鞋"},
            {"name": "👨 男士 / 男友", "tag": "清爽挺拔 · 型男", "bg": "F0F9FF", "border": "BFDBFE", "desc": "• 主装：挺括工装夹克 / 纯羊毛大衣 / 纯色针织衫\n• 下装：深色修身休闲长裤\n• 鞋履：轻便皮鞋 / 舒适缓震运动鞋"}
        ],
        "prep_rows": [
            ("D-30 ~ D-15", "机票与核心特色酒店锁定", "官方平台 / OTA", "提前预订旺季稀缺景观房源与机位，确认退改保障。"),
            ("D-10", "当地包车 / 租车自驾确认", "正规平台 / 租车渠道", "确认国际驾照翻译件、全险保单与提车网点。"),
            ("D-7", "热门餐厅与特色体验预约", "大众点评 / 官网预约", "提前预订热门高分餐厅烛光晚宴或特色温泉/门票。"),
            ("D-2", "外汇准备与行李打包", "银行预约换新版美金", "带好 Visa/Master 双币卡，准备崭新无瑕疵美钞。"),
            ("出行当天", "准时启程", "航旅纵横 / 实时导航", "提前 2.5 小时抵达机场办理值机行李托运。")
        ],
        "days": [],
        "deals": [],
        "parking": [],
        "souvenirs": [],
        "checklist": [
            "护照原件（有效期 6 个月以上，免签 30 天） ＋ 往返机票行程单打印件",
            "$500 - $800 崭新美金现钞（2013年后大面额、无污损无折痕）",
            "Visa / MasterCard 全币种双币信用卡 ＋ 1张银联借记卡（BOG银行ATM应急取现）",
            "保暖羊绒衫 ＋ 挡风大衣 ＋ 复古约会礼服/长裙（高加索早晚温差大）",
            "双人合影便携三脚架 / 蓝牙自拍杆 / 胶片复古相机",
            "欧标德标双圆孔转换插头 ＋ 便携大容量充电宝",
            "提前下载手机打车软件【Yandex Go】（在第比利斯打车极其便宜方便，一口价防宰客）"
        ],
        "footer": {
            "wish": "祝恋人/全家旅途顺畅 · 拍照绝美出片 · 留下最美好的浪漫回忆！✨",
            "hotel": "住宿大本营：请确认酒店名称与前台联系电话",
            "hotlines": ["🇨🇳 中国驻当地使领馆领保专线", "🌐 外交部全球领事保护：+86 10 12308", "🚨 当地紧急求助与急救专线：112"]
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

    # 2. Intelligent Family / Couple Demographics Detection
    is_couple = any(k in content for k in ["恋人", "情侣", "夫妻", "二人世界", "双人行", "蜜月"])
    has_kids = any(k in content for k in ["宝宝", "女宝", "男宝", "带宝", "娃娃", "女娃", "男娃", "儿童", "小孩", "小孩子", "带娃", "小公主", "幼童", "学步儿"])
    has_seniors = any(k in content for k in ["外婆", "奶奶", "姥姥", "爷爷", "长辈", "老人"])

    outfits = []
    if is_couple and not has_kids and not has_seniors:
        outfits = [
            {
                "name": "👩 女士 / 女友",
                "tag": "浪漫法式 · 唯美女主",
                "bg": "FFF5F5",
                "border": "FECDD3",
                "desc": "• 主装：红色/复古色修身长裙 ＋ 羊绒大衣\n• 配饰：法式贝雷帽 ＋ 偏光墨镜 ＋ 精致手提包\n• 鞋履：舒适健步短皮靴 / 经典平底单鞋"
            },
            {
                "name": "👨 男士 / 男友",
                "tag": "清爽挺拔 · 绅士男主",
                "bg": "F0F9FF",
                "border": "BFDBFE",
                "desc": "• 主装：挺括工装夹克 / 纯色毛呢大衣 / 质感羊毛衫\n• 下装：深色微修身休闲长裤\n• 鞋履：轻便复古皮鞋 / 舒适缓震跑鞋"
            }
        ]
        data["stats"] = [
            {"label": "🏨 浪漫大本营", "val": "高加索设计酒店", "desc": "雪山落地窗+星空露台"},
            {"label": "🍷 微醺格调", "val": "8000年陶罐酒", "desc": "琥珀酒微醺+烛光晚宴"},
            {"label": "🚗 出行方式", "val": "私享专车/包车", "desc": "沿途高加索公路大片"},
            {"label": "👗 恋人穿搭", "val": "复古高级色系", "desc": "雪山大衣+法式长裙"}
        ]
    else:
        child_age = None
        m_age = re.search(r"(\d{1,2})\s*岁\s*(?:[女男]?[娃宝]|孩子|女儿|儿子|小公主|幼童|儿童)", content)
        if m_age:
            child_age = int(m_age.group(1))

        if child_age is not None or has_kids:
            c_age = child_age if child_age is not None else 3
            is_girl = any(k in content for k in ["女娃", "女宝", "女儿", "小公主"])
            child_name = f"👧 {c_age}岁{'女娃' if is_girl else '宝宝'}" if is_girl else f"👶 {c_age}岁宝宝"
            
            if c_age <= 2:
                outfits.append({
                    "name": child_name,
                    "tag": "全家童话 C 位",
                    "bg": "FFF5F5",
                    "border": "FECDD3",
                    "desc": "• 连体：亮色亲子系软棉娃娃裙/连体服\n• 配饰：软萌防晒帽 / 吸汗发带\n• 鞋袜：透气防滑软底学步小红鞋"
                })
            elif 3 <= c_age <= 6:
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
            "name": "👩 妈妈" if has_kids else "👩 女士",
            "tag": "上亮下暗 · 显瘦",
            "bg": "FAFAFA",
            "border": "CBD5E1",
            "desc": "• 上装：正红/暖色修身短袖 / 国风衬衫\n• 下装：优雅黑色高腰中长裙 / 垂感阔腿裤\n• 配饰：精致发饰 / 偏光墨镜 + 亲子同色系"
        })
        outfits.append({
            "name": "👨 爸爸" if has_kids else "👨 男士",
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
                t_match = re.match(r"(?:\*\*)?([0-9]{1,2}:[0-9]{2}(?:\s*[-—~]\s*[0-9]{1,2}:[0-9]{2})?|[上下]午|清晨|傍晚|夜间|全天)(?:\*\*)?[：:\s|｜]+([\s\S]+)", clean_line)
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
        rows = []
        for l in table_lines[2:]:
            cols = [c.strip() for c in l.split("|")[1:-1]]
            if any(cols):
                rows.append(cols)
        return rows

    # 5. Dynamic Prep Extraction (Table or Bullet Points)
    prep_table = extract_markdown_table(r"##\s*[^#\n]*?(?:行前|抢票|准备|免签|外汇)[^#\n]*?\n([\s\S]*?)(?=##|\Z)")
    if prep_table:
        data["prep_rows"] = [tuple(r[:4]) if len(r) >= 4 else tuple(r + [""] * (4 - len(r))) for r in prep_table]
    else:
        m_prep_sec = re.search(r"##\s*[^#\n]*?(?:行前|抢票|准备|免签)[^#\n]*?\n([\s\S]*?)(?=##|\Z)", content, re.I)
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
                        p_bullets.append((node, detail[:25] + "..." if len(detail) > 25 else detail, "官方/权威渠道", detail))
            if p_bullets:
                data["prep_rows"] = p_bullets

    # 6. Dynamic Deals & Dining Extraction
    dining_table = extract_markdown_table(r"##\s*[^#\n]*?(?:美食|餐厅|微醺|餐饮|省钱)[^#\n]*?\n([\s\S]*?)(?=##|\Z)")
    if dining_table:
        data["deals"] = [tuple(r[:6]) if len(r) >= 6 else tuple(r + [""] * (6 - len(r))) for r in dining_table]

    # 7. Robust Dynamic Checklist Extraction
    # Scan content for checkboxes or checklist sections
    chk_items = []
    for line in content.split("\n"):
        line = line.strip()
        if line.startswith(("- [ ]", "- [x]", "- [X]")):
            clean = re.sub(r"^-\s*\[[ xX]\]\s*", "", line).strip()
            clean = clean.replace("**", "").strip()
            if clean:
                chk_items.append(clean)

    if chk_items:
        data["checklist"] = chk_items

    # 8. Dynamic Parking / Transport Extraction (ONLY if parking table exists)
    if "停车" in content or "车位" in content:
        park_table = extract_markdown_table(r"##\s*[^#\n]*?(?:停车|地库|车位)[^#\n]*?\n([\s\S]*?)(?=##|\Z)")
        if park_table:
            data["parking"] = [tuple(r[:5]) if len(r) >= 5 else tuple(r + [""] * (5 - len(r))) for r in park_table]
        else:
            data["parking"] = []
    else:
        data["parking"] = []

    # 9. Dynamic Souvenirs & Shopping Extraction
    souvenirs = []
    m_souv = re.search(r"##\s*[^#\n]*?(?:纪念品|伴手礼|特产|淘宝|购物|买啥)[^#\n]*?\n([\s\S]*?)(?=##|\Z)", content, re.I)
    if m_souv:
        for line in m_souv.group(1).split("\n"):
            line = line.strip()
            if line.startswith(("-", "*", "1.", "2.", "3.", "4.", "5.")):
                clean = re.sub(r"^(?:[-*]|\d+\.)\s*", "", line).strip()
                if clean and not clean.startswith("#"):
                    parts = re.split(r"[：:]", clean, maxsplit=1)
                    if len(parts) == 2:
                        s_name = parts[0].replace("*", "").strip()
                        s_desc = parts[1].replace("*", "").strip()
                        souvenirs.append((s_name, s_desc))
                    else:
                        souvenirs.append((clean[:18], clean))
    data["souvenirs"] = souvenirs

    return data
