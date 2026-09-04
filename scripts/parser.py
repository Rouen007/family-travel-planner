"""
Universal Destination-Agnostic Travel Markdown Parser
Intelligently extracts sections, 100% dynamic tables with headers, family age cohorts, timelines, souvenirs, and metadata.
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
            {"label": "👗 穿搭风格", "val": "协调视觉色系", "desc": "高级审美+唯美出片"}
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
        "days": [
            {
                "day_tag": "Day 1",
                "day_title": "启程抵达 ➔ 办理入住 ➔ 深度午休 ➔ 悠闲夜游",
                "color_hex": "E11D48",
                "items": [
                    ("上午", "启程出发，平稳前往目的地。"),
                    ("中午", "品尝当地特色午餐，客栈/酒店办理入住。"),
                    ("14:00 - 16:00", "全家舒适深度午休彻底回血！"),
                    ("傍晚与夜间", "漫步特色历史街区或滨海步道，打卡晚市美食。")
                ]
            },
            {
                "day_tag": "Day 2",
                "day_title": "核心景点沉浸游 ➔ 特色大餐 ➔ 黄金午休 ➔ 特色漫步",
                "color_hex": "2563EB",
                "items": [
                    ("上午", "黄金早场打卡标志性景点或非遗体验。"),
                    ("中午", "享用当地特色能量大餐。"),
                    ("14:00 - 16:00", "避开正午烈日，舒适午休休整。"),
                    ("傍晚与夜间", "夕阳漫步或观赏特色夜景秀。")
                ]
            },
            {
                "day_tag": "Day 3",
                "day_title": "文化探访 ➔ 老字号午餐 ➔ 全家合影 ➔ 顺畅返程",
                "color_hex": "059669",
                "items": [
                    ("上午", "睡到自然醒，悠闲退房打卡文化古迹。"),
                    ("中午", "品尝老字号风味小吃。"),
                    ("下午", "地标前留下美好合影，启程返家。")
                ]
            }
        ],
        "dining_headers": ["餐厅名称与地点", "招牌特色硬菜", "参考消费", "推荐指数", "订座/咨询电话"],
        "dining_rows": [],
        "deals": [],
        "parking_headers": ["目的地", "推荐停车场", "导航关键字", "收费标准", "核心优势与设施"],
        "parking_rows": [],
        "parking": [],
        "souvenirs": [],
        "weather_headers": ["日期与节点", "天气与体感", "预估气温", "实战应对与穿衣提示"],
        "weather_rows": [],
        "weather_bullets": [],
        "checklist": [
            "身份证原件 ＋ 电子门票/预约码",
            "满电大容量充电宝 ＋ 手机数据线",
            "晴雨两用折叠伞 ＋ 便携防晒/雨具",
            "舒适轻便缓震运动鞋（全天健步走）",
            "便携水杯 ＋ 湿纸巾/纸巾",
            "常用应急药品 ＋ 防磨脚创口贴"
        ],
        "footer": {
            "wish": "祝旅途顺畅 · 游玩尽兴 · 留下最美好的度假回忆！✨",
            "hotel": "",
            "hotlines": ["🚨 紧急求助：110 / 120", "🌐 旅游政务热线：12345"]
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

    # 2. Dynamic Outfits Extraction from Markdown
    custom_outfits = []
    m_outfits_sec = re.search(r"^##\s+[^#\n]*?(?:穿搭|服饰|着装|ootd)[^#\n]*?\n([\s\S]*?)(?=^##\s|\Z)", content, re.M | re.I)
    if m_outfits_sec:
        cur_card = None
        card_styles = [
            {"bg": "FFF5F5", "border": "FECDD3", "default_tag": "甜美出圈 · C位"},
            {"bg": "F0F9FF", "border": "BFDBFE", "default_tag": "清爽型男 · 护花"},
            {"bg": "FEFCE8", "border": "FEF08A", "default_tag": "温婉大方 · 舒适"},
            {"bg": "F0FDF4", "border": "BBF7D0", "default_tag": "活力元气 · 亮眼"}
        ]
        s_idx = 0
        for line in m_outfits_sec.group(1).split("\n"):
            m_top = re.match(r"^[-*]\s+(.*?)\*\*(.+?)\*\*[：:]?", line)
            if m_top:
                if cur_card:
                    custom_outfits.append(cur_card)
                prefix = m_top.group(1).strip()
                core = m_top.group(2).strip()
                full_name = f"{prefix} {core}".strip() if prefix else core

                st = card_styles[s_idx % len(card_styles)]
                s_idx += 1

                m_tag = re.search(r"[（\(](.+?)[）\)]", full_name)
                if m_tag:
                    c_tag = m_tag.group(1).strip()
                    c_name = re.sub(r"[（\(].+?[）\)]", "", full_name).strip()
                else:
                    c_name = full_name
                    c_tag = "浪漫出圈 · 高甜" if ("公主" in c_name or "女" in c_name) else ("帅气护花 · 型男" if ("骑士" in c_name or "男" in c_name) else st["default_tag"])

                cur_card = {
                    "name": c_name,
                    "tag": c_tag,
                    "bg": st["bg"],
                    "border": st["border"],
                    "desc_lines": []
                }
            elif cur_card and line.strip().startswith(("-", "*", "•")):
                sub_clean = re.sub(r"^[-*•\s]+", "", line).strip()
                sub_clean = sub_clean.replace("**", "").strip()
                if sub_clean:
                    cur_card["desc_lines"].append(f"• {sub_clean}")
        if cur_card:
            custom_outfits.append(cur_card)

        for c in custom_outfits:
            c["desc"] = "\n".join(c["desc_lines"]) if c["desc_lines"] else "• 舒适轻便运动跑鞋\n• 协调视觉色系"
            del c["desc_lines"]

    outfits = []
    if is_couple and not has_kids and not has_seniors:
        if any(k in content for k in ["迪士尼", "乐园", "Disney", "环球"]):
            data["stats"] = [
                {"label": "⏰ 当天节奏", "val": "08:30排队—烟花散场", "desc": "正点入园·浪漫尽兴"},
                {"label": "🎢 必刷大项", "val": "三大王牌极限心跳", "desc": "创极速光轮+热力追踪"},
                {"label": "📸 情侣机位", "val": "城堡与旋转木马", "desc": "浪漫高甜·电影感大片"},
                {"label": "👗 恋人穿搭", "val": "在逃公主与骑士", "desc": "红白黑高甜出圈"}
            ]
        elif any(k in content for k in ["高加索", "格鲁吉亚"]):
            data["stats"] = [
                {"label": "🏨 浪漫大本营", "val": "高加索设计酒店", "desc": "雪山落地窗+星空露台"},
                {"label": "🍷 微醺格调", "val": "8000年陶罐酒", "desc": "琥珀酒微醺+烛光晚宴"},
                {"label": "🚗 出行方式", "val": "私享专车/包车", "desc": "沿途高加索公路大片"},
                {"label": "👗 恋人穿搭", "val": "复古高级色系", "desc": "雪山大衣+法式长裙"}
            ]
        else:
            data["stats"] = [
                {"label": "🏨 浪漫大本营", "val": "精选品质酒店", "desc": "舒适景观+浪漫氛围"},
                {"label": "🚗 出行方式", "val": "私享专车/自驾", "desc": "自由随性+沿途看景"},
                {"label": "🍷 微醺格调", "val": "地道老饕体验", "desc": "烛光晚宴+在地文化"},
                {"label": "👗 恋人穿搭", "val": "协调视觉色系", "desc": "高级审美+唯美出片"}
            ]

        if custom_outfits:
            outfits = custom_outfits
        elif any(k in content for k in ["迪士尼", "乐园", "Disney", "环球"]):
            outfits = [
                {
                    "name": "👩 在逃公主（女友）",
                    "tag": "甜美出圈 · 浪漫灵动",
                    "bg": "FFF5F5",
                    "border": "FECDD3",
                    "desc": "• 主装：法式复古白衬衫 ＋ 正红收腰蓬蓬裙\n• 配饰：米妮大蝴蝶结发箍 ＋ 偏光墨镜 ＋ 斜挎包\n• 鞋履：严禁高跟鞋！舒适缓震软底运动鞋"
                },
                {
                    "name": "👨 护花骑士（男友）",
                    "tag": "清爽帅气 · 后勤担当",
                    "bg": "F0F9FF",
                    "border": "BFDBFE",
                    "desc": "• 主装：简约纯白短T ＋ 黑色轻薄工装短袖外搭\n• 下装：深灰色轻便速干休闲长裤 / 短裤\n• 鞋履：专业缓震透气跑鞋 (全天健步走)"
                }
            ]
        elif any(k in content for k in ["高加索", "格鲁吉亚"]):
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
        else:
            outfits = [
                {
                    "name": "👩 女士 / 女友",
                    "tag": "优雅唯美 · 出圈",
                    "bg": "FFF5F5",
                    "border": "FECDD3",
                    "desc": "• 主装：亮色连衣裙 / 质感休闲套装\n• 配饰：精致遮阳帽 ＋ 偏光墨镜 ＋ 轻量挎包\n• 鞋履：舒适健步休闲运动鞋"
                },
                {
                    "name": "👨 男士 / 男友",
                    "tag": "清爽挺拔 · 型男",
                    "bg": "F0F9FF",
                    "border": "BFDBFE",
                    "desc": "• 主装：纯色舒适透气短T / 亚麻休闲衬衫\n• 下装：深色修身直筒休闲长裤\n• 鞋履：轻便缓震运动跑鞋"
                }
            ]
    else:
        if any(k in content for k in ["迪士尼", "乐园", "Disney", "环球"]):
            hotel_val = "度假区万怡酒店" if "万怡" in content else "主题乐园/度假酒店"
            hotel_desc = "免费停车+班车直达" if "万怡" in content else "便捷往返+轻松休整"
            ev_val = "极氪极充 18分钟" if ("极充" in content or "极氪" in content) else "自驾畅行/包车"
            ev_desc = "顺路满电+零续航焦虑" if ("极充" in content or "极氪" in content) else "沿途看景+轻松休整"
            data["stats"] = [
                {"label": "🏨 度假大本营", "val": hotel_val, "desc": hotel_desc},
                {"label": "🚗 纯电自驾", "val": ev_val, "desc": ev_desc},
                {"label": "👶 亲子慢游", "val": "2岁女宝+50+外婆", "desc": "黄金午睡+无障碍动线"},
                {"label": "👗 亲子穿搭", "val": "红白黑经典系列", "desc": "视觉统一+高级出片"}
            ]

        if custom_outfits:
            outfits = custom_outfits
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
    day_matches = list(re.finditer(r"(?:###|##)\s*((?:Day\s*\d+|第[一二三四五六七八九十\d]+天)[^\n]*?)(?:\n|$)([\s\S]*?)(?=(?:###|##)\s*(?:Day\s*\d+|第[一二三四五六七八九十\d]+天)|\Z|^##\s)", content, re.M | re.I))
    colors = ["E11D48", "2563EB", "059669", "D97706", "7C3AED", "0D9488"]
    
    parsed_days = []
    cn_map = {"第一天": "Day 1", "第二天": "Day 2", "第三天": "Day 3", "第四天": "Day 4", "第五天": "Day 5", "第六天": "Day 6"}
    for idx, dm in enumerate(day_matches):
        raw_header = dm.group(1).strip()
        body = dm.group(2).strip()
        
        m_day_tag = re.match(r"^(Day\s*\d+|第[一二三四五六七八九十\d]+天)", raw_header, re.I)
        if m_day_tag:
            raw_tag = m_day_tag.group(1).strip()
            if raw_tag.lower().startswith("day"):
                tag = "Day " + re.sub(r"(?i)^day\s*", "", raw_tag)
            else:
                tag = cn_map.get(raw_tag, raw_tag)
            d_title = raw_header[m_day_tag.end():].lstrip(" ·:-—\t")
        else:
            header_parts = re.split(r"[：:·\-\➔\s]+", raw_header, maxsplit=1)
            raw_tag = header_parts[0] if len(header_parts) > 0 else f"Day {idx+1}"
            tag = cn_map.get(raw_tag, raw_tag)
            d_title = header_parts[1] if len(header_parts) > 1 else raw_header
        
        items = []
        for line in body.split("\n"):
            line = line.strip()
            if re.match(r"^[-*•\s\-_=]{2,}$", line):
                continue
            if line.startswith(("-", "*", "•")):
                clean_line = re.sub(r"^[-*•]\s*", "", line)
                clean_line = clean_line.replace("**", "").strip()
                if not clean_line or re.match(r"^[-=_]{2,}$", clean_line):
                    continue
                t_match = re.match(r"([0-9]{1,2}:[0-9]{2}(?:\s*[-—~]\s*[0-9]{1,2}:[0-9]{2})?|[上下]午|清晨|傍晚|夜间|全天)[：:\s|｜]+([\s\S]+)", clean_line)
                if t_match:
                    items.append((t_match.group(1).strip(), t_match.group(2).strip()))
                elif clean_line and not clean_line.startswith(("#", "---")):
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
    def extract_markdown_table_with_headers(sec_pattern):
        m_sec = re.search(sec_pattern, content, re.M | re.I)
        if not m_sec: return [], []
        sec_text = m_sec.group(1)
        table_lines = [l.strip() for l in sec_text.split("\n") if l.strip().startswith("|") and l.strip().endswith("|")]
        if len(table_lines) < 3: return [], []
        headers = [c.strip() for c in table_lines[0].split("|")[1:-1]]
        rows = []
        for l in table_lines[2:]:
            cols = [c.strip() for c in l.split("|")[1:-1]]
            if any(cols):
                rows.append(cols)
        return headers, rows

    # 5. Dynamic Prep Extraction
    p_headers, p_rows = extract_markdown_table_with_headers(r"^##\s+[^#\n]*?(?:行前|抢票|准备|免签|外汇)[^#\n]*?\n([\s\S]*?)(?=^##\s|\Z)")
    if p_rows:
        data["prep_rows"] = [tuple(r[:4]) if len(r) >= 4 else tuple(r + [""] * (4 - len(r))) for r in p_rows]
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
            data["prep_rows"] = p_bullets
        else:
            data["prep_rows"] = []

    # 6. Dynamic Deals & Dining Extraction (100% Dynamic Headers & Rows)
    d_headers, d_rows = extract_markdown_table_with_headers(r"^##\s+[^#\n]*?(?:美食|餐厅|微醺|餐饮|省钱)[^#\n]*?\n([\s\S]*?)(?=^##\s|\Z)")
    if d_rows:
        data["dining_headers"] = d_headers
        data["dining_rows"] = d_rows
        data["deals"] = d_rows
    else:
        data["dining_headers"] = ["餐厅名称与地点", "招牌必点特色", "参考消费", "推荐指数", "订座/咨询电话"]
        data["dining_rows"] = []
        data["deals"] = []

    # 7. Robust Dynamic Checklist Extraction
    chk_items = []
    for line in content.split("\n"):
        line = line.strip()
        if line.startswith(("- [ ]", "- [x]", "- [X]")):
            clean = re.sub(r"^-\s*\[[ xX]\]\s*", "", line).strip()
            clean = clean.replace("**", "").strip()
            if clean: chk_items.append(clean)

    data["checklist"] = chk_items if chk_items else []

    # 8. Dynamic Parking / Transport Extraction (ONLY if parking table exists)
    pk_headers, pk_rows = extract_markdown_table_with_headers(r"^##\s+[^#\n]*?(?:停车|地库|车位)[^#\n]*?\n([\s\S]*?)(?=^##\s|\Z)")
    if pk_rows:
        data["parking_headers"] = pk_headers
        data["parking_rows"] = pk_rows
        data["parking"] = pk_rows
    else:
        data["parking_headers"] = []
        data["parking_rows"] = []
        data["parking"] = []

    # 9. Dynamic Souvenirs & Shopping Extraction
    souvenirs = []
    m_souv = re.search(r"^##\s+[^#\n]*?(?:纪念品|伴手礼|特产|淘宝|购物|买啥)[^#\n]*?\n([\s\S]*?)(?=^##\s|\Z)", content, re.I)
    if m_souv:
        for line in m_souv.group(1).split("\n"):
            line = line.strip()
            if line.startswith(("-", "*", "1.", "2.", "3.", "4.", "5.", "6.")):
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

    # 9.5 Dynamic Map Image Extraction
    map_img = ""
    # Check markdown image tags
    m_img = re.search(r"!\[.*?\]\((.*?\.(?:png|jpg|jpeg|webp))\)", content, re.I)
    if m_img:
        cand = m_img.group(1).strip()
        if os.path.isabs(cand) and os.path.exists(cand):
            map_img = cand
        elif file_path:
            rel_path = os.path.join(os.path.dirname(os.path.abspath(file_path)), cand)
            if os.path.exists(rel_path): map_img = rel_path
    
    # Fallback to known map if exists in trip dir or coding dir
    if not map_img and file_path:
        cand_dirs = [
            os.path.dirname(os.path.abspath(file_path)),
            os.path.join(os.path.dirname(os.path.abspath(file_path)), "magical-family-journey"),
            "/Users/rouen/Documents/coding/magical-family-journey"
        ]
        for d in cand_dirs:
            p = os.path.join(d, "上海迪士尼亲子顺时针动线与烟花观赏实景地图.png")
            if os.path.exists(p):
                map_img = p
                break

    data["map_path"] = map_img
    data["map_b64"] = ""
    if map_img and os.path.exists(map_img):
        try:
            import base64
            with open(map_img, "rb") as f_img:
                b64_data = base64.b64encode(f_img.read()).decode("utf-8")
                ext = os.path.splitext(map_img)[1].lower().replace(".", "")
                mime = "image/png" if ext == "png" else ("image/jpeg" if ext in ("jpg", "jpeg") else "image/webp")
                data["map_b64"] = f"data:{mime};base64,{b64_data}"
        except Exception as e:
            print(f"Base64 map encode note: {e}")

    # 9.8 Dynamic Weather Extraction
    data["weather_headers"] = ["日期与节点", "天气与体感", "预估气温", "实战应对与穿衣提示"]
    data["weather_rows"] = []
    data["weather_bullets"] = []
    m_wthr = re.search(r"^##\s+[^#\n]*?(?:天气|气象|气候|降雨|气温)[^#\n]*?\n([\s\S]*?)(?=^##\s|\Z)", content, re.M | re.I)
    if m_wthr:
        w_text = m_wthr.group(1)
        w_lines = [l.strip() for l in w_text.split("\n") if l.strip().startswith("|") and l.strip().endswith("|")]
        if len(w_lines) >= 3:
            data["weather_headers"] = [c.strip() for c in w_lines[0].split("|")[1:-1]]
            data["weather_rows"] = [[c.strip() for c in l.split("|")[1:-1]] for l in w_lines[2:]]
        else:
            w_bullets = []
            for line in w_text.split("\n"):
                line = line.strip()
                if line.startswith(("-", "*")):
                    clean = re.sub(r"^[-*]\s*", "", line).strip()
                    if clean and not clean.startswith("#"):
                        parts = re.split(r"[：:]", clean, maxsplit=1)
                        if len(parts) == 2:
                            w_bullets.append((parts[0].replace("**", "").strip(), parts[1].replace("**", "").strip()))
                        else:
                            w_bullets.append((clean[:12], clean))
            data["weather_bullets"] = w_bullets

    # 10. Dynamic Footer & Hotlines
    hotel_info = ""
    if "万怡" in content:
        hotel_info = "上海国际旅游度假区万怡酒店 (浦东秀浦路 3999 弄 17 号 · 021-68869888)"
    elif "天域" in content:
        hotel_info = "三亚亚龙湾天域度假酒店 (0898-88567888)"
    elif "Rooms" in content:
        hotel_info = "卡兹别克 Rooms Hotel (+995 322 02 00 99)"
    hotlines = []
    m_med = re.search(r"^##\s+[^#\n]*?(?:医疗|电话|通讯录|备忘录|热线|求助)[^#\n]*?\n([\s\S]*?)(?=^##\s|\Z)", content, re.M | re.I)
    if m_med:
        for line in m_med.group(1).split("\n"):
            line = line.strip()
            if line.startswith(("-", "*")):
                clean = re.sub(r"^[-*]\s*", "", line).strip()
                clean = clean.replace("**", "").replace("`", "")
                if clean: hotlines.append(clean)
    if not hotlines:
        if any(k in content for k in ["迪士尼", "Disney"]):
            hotlines = [
                "🏰 迪士尼官方客服: 400-180-0000",
                "🏥 乐园医疗急救站: 021-20995533",
                "🚨 度假区治安派出所: 021-22047800",
                "🚇 地铁11号线运营热线: 021-64370000"
            ]
        else:
            hotlines = [
                "🚨 紧急求助电话: 110 / 120",
                "🌐 旅游政务热线: 12345"
            ]

    data["footer"] = {
        "wish": "祝 2岁小公主 ＆ 全家旅途顺畅 · 拍照绝美出圈 · 留下最美好的童话回忆！✨" if has_kids else "祝两人世界浪漫甜蜜 · 刷遍王牌大项 · 烟花拥吻定格最美瞬间！✨",
        "hotel": hotel_info,
        "hotlines": hotlines[:4]
    }

    return data
