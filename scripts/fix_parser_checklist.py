path = "/Users/rouen/.gemini/antigravity/skills/family-travel-planner/scripts/parser.py"
with open(path, "r", encoding="utf-8") as f:
    code = f.read()

# Fix checklist regex: specifically match sections with 清单 or containing checkboxes
old_check_logic = """    # 7. Dynamic Checklist Extraction
    m_check = re.search(r"##\s*[^#\n]*?(?:清单|准备物品|打勾|避雷|行前必备)[^#\n]*?\n([\s\S]*?)(?=##|\Z)", content, re.I)
    if m_check:
        chk_items = []
        for line in m_check.group(1).split("\\n"):
            line = line.strip()
            if line.startswith(("- [ ]", "- [x]", "- [X]")):
                clean = re.sub(r"^-\s*\[[ xX]\]\s*", "", line).strip()
                if clean: chk_items.append(clean)
            elif line.startswith(("-", "*")):
                clean = re.sub(r"^[-*]\s*", "", line).strip()
                if clean and not clean.startswith("#"): chk_items.append(clean)
        if chk_items:
            data["checklist"] = chk_items"""

new_check_logic = """    # 7. Dynamic Checklist Extraction
    # First priority: Find section that specifically mentions 清单 or 打勾
    all_check_matches = list(re.finditer(r"##\s*[^#\n]*?(?:清单|打勾|装备|行李|必备物品)[^#\n]*?\n([\s\S]*?)(?=##|\Z)", content, re.I))
    found_items = []
    for m in all_check_matches:
        sec_text = m.group(1)
        for line in sec_text.split("\\n"):
            line = line.strip()
            if line.startswith(("- [ ]", "- [x]", "- [X]")):
                clean = re.sub(r"^-\s*\[[ xX]\]\s*", "", line).strip()
                if clean: found_items.append(clean)
            elif line.startswith(("-", "*")):
                clean = re.sub(r"^[-*]\s*", "", line).strip()
                if clean and not clean.startswith("#") and not line.startswith(("- [ ]", "- [x]", "- [X]")):
                    found_items.append(clean)
        if found_items:
            break

    # Second priority: Find any checkboxes in the document
    if not found_items:
        for line in content.split("\\n"):
            line = line.strip()
            if line.startswith(("- [ ]", "- [x]", "- [X]")):
                clean = re.sub(r"^-\s*\[[ xX]\]\s*", "", line).strip()
                if clean: found_items.append(clean)

    if found_items:
        data["checklist"] = found_items"""

code = code.replace(old_check_logic, new_check_logic)

# Add Souvenirs extraction to parser
old_parking_logic = """    # 8. Dynamic Parking / Transport Extraction
    park_table = extract_markdown_table(r"##\s*[^#\n]*?(?:停车|交通|补能|自驾|包车)[^#\n]*?\n([\s\S]*?)(?=##|\Z)")
    if park_table:
        data["parking"] = [tuple(r[:5]) if len(r) >= 5 else tuple(r + [""] * (5 - len(r))) for r in park_table]

    return data"""

new_parking_and_souvenir_logic = """    # 8. Dynamic Parking / Transport Extraction (ONLY if explicitly relevant)
    if "停车" in content or "自驾" in content:
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
        for line in m_souv.group(1).split("\\n"):
            line = line.strip()
            if line.startswith(("-", "*", "1.", "2.", "3.", "4.", "5.")):
                clean = re.sub(r"^(?:[-*]|\d+\.)\s*", "", line).strip()
                if clean:
                    parts = re.split(r"[：:]", clean, maxsplit=1)
                    if len(parts) == 2:
                        s_name = parts[0].replace("*", "").strip()
                        s_desc = parts[1].replace("*", "").strip()
                        souvenirs.append((s_name, s_desc))
                    else:
                        souvenirs.append((clean[:15], clean))
    data["souvenirs"] = souvenirs

    return data"""

code = code.replace(old_parking_logic, new_parking_and_souvenir_logic)

with open(path, "w", encoding="utf-8") as f:
    f.write(code)

print("Updated parser with robust checklist, parking suppression, and souvenirs extraction!")
