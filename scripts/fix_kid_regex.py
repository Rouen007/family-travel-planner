path = "/Users/rouen/.gemini/antigravity/skills/family-travel-planner/scripts/parser.py"
with open(path, "r", encoding="utf-8") as f:
    code = f.read()

# Replace has_kids logic
old_logic = 'has_kids = any(k in content for k in ["娃", "宝", "儿童", "孩子", "小公主", "幼童", "学步", "带娃", "小帅哥"])'
new_logic = 'has_kids = any(k in content for k in ["宝宝", "女宝", "男宝", "带宝", "娃娃", "女娃", "男娃", "儿童", "小孩", "小孩子", "带娃", "小公主", "幼童", "学步儿"])'

code = code.replace(old_logic, new_logic)

# Replace age regex
old_age = r'm_age = re.search(r"(\d{1,2})\s*岁\s*(?:[女男]?娃|[女男]?宝|孩子|女儿|儿子|小公主|幼童|儿童)", content)'
new_age = r'm_age = re.search(r"(\d{1,2})\s*岁\s*(?:[女男]?[娃宝]|孩子|女儿|儿子|小公主|幼童|儿童)", content)'

with open(path, "w", encoding="utf-8") as f:
    f.write(code)

print("Fixed child detection regex!")
