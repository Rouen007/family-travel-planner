"""
Single-Page Web App Generator
Compiles travel plan data into an interactive responsive HTML webpage.
Supports both Jinja2 and pure Python fallback.
"""
import os
import sys
import argparse

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, current_dir)
from parser import parse_travel_markdown

def render_fallback_html(data):
    stats_html = "".join([f'<div class="bg-white/10 rounded-xl p-3 border border-white/10"><div class="text-xs text-slate-400">{s["label"]}</div><div class="text-sm font-bold mt-1 text-white">{s["val"]}</div><div class="text-xs text-rose-300 mt-1">{s["desc"]}</div></div>' for s in data["stats"]])
    outfits_html = "".join([f'<div class="p-4 rounded-2xl border" style="background-color: #{c["bg"]}; border-color: #{c["border"]};"><div class="font-bold text-slate-900 text-base mb-1">{c["name"]} <span class="text-xs px-2 py-0.5 rounded-full bg-white font-medium text-slate-600 border">{c["tag"]}</span></div><div class="text-xs text-slate-600 whitespace-pre-line leading-relaxed mt-2">{c["desc"]}</div></div>' for c in data["outfits"]])
    days_html = "".join([f'<div class="bg-slate-50 p-4 rounded-2xl border border-slate-200"><div class="font-bold text-slate-900 text-sm mb-3 flex items-center gap-2"><span class="text-white text-xs px-2 py-0.5 rounded-md font-black" style="background-color: #{d["color_hex"]};">{d["day_tag"].split("·")[0]}</span><span>{d["day_tag"]} · {d["day_title"]}</span></div><div class="space-y-2">' + "".join([f'<div class="flex gap-2 text-xs"><span class="bg-white border text-slate-700 font-bold px-1.5 py-0.5 rounded h-fit whitespace-nowrap">{t[0]}</span><span class="text-slate-600 leading-relaxed">{t[1]}</span></div>' for t in d["items"]]) + '</div></div>' for d in data["days"]])
    deals_html = "".join([f'<tr><td class="p-2.5 font-bold">{d[0]}</td><td class="p-2.5 text-slate-600">{d[1]}</td><td class="p-2.5 text-slate-400 line-through">{d[2]}</td><td class="p-2.5 text-rose-600 font-bold">{d[3]}</td><td class="p-2.5"><span class="bg-rose-50 text-rose-600 px-1.5 py-0.5 rounded font-bold">{d[4]}</span></td><td class="p-2.5 text-slate-600">{d[5]}</td></tr>' for d in data["deals"]])
    check_html = "".join([f'<div class="flex items-center gap-2 p-2.5 rounded-xl bg-slate-50 border border-slate-100"><span class="w-4 h-4 rounded bg-rose-600 text-white flex items-center justify-center font-bold text-[10px]">✓</span><span class="text-slate-700 font-medium">{item}</span></div>' for item in data["checklist"]])
    hotlines_html = "".join([f'<span>{hl}</span>' for hl in data["footer"]["hotlines"]])

    return f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
<title>{data["title"]}</title>
<script src="https://cdn.tailwindcss.com"></script>
<style> body {{ font-family: -apple-system, BlinkMacSystemFont, "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", sans-serif; }} </style>
</head>
<body class="bg-slate-100 text-slate-800 pb-12">
  <div class="max-w-3xl mx-auto px-4 pt-6 space-y-6">
    <div class="bg-gradient-to-r from-slate-900 via-rose-950 to-slate-900 text-white rounded-3xl p-6 shadow-xl">
      <span class="inline-block bg-white/20 backdrop-blur px-3 py-1 rounded-full text-xs font-semibold text-rose-200 mb-3">🏰 {data["dates"]} · 家庭自驾</span>
      <h1 class="text-2xl sm:text-3xl font-black mb-2">{data["title"]}</h1>
      <p class="text-sm text-slate-300 mb-6">{data["subtitle"]}</p>
      <div class="grid grid-cols-2 sm:grid-cols-4 gap-3">{stats_html}</div>
    </div>
    <div class="bg-white rounded-3xl p-6 shadow-sm border border-slate-200">
      <h2 class="text-lg font-bold text-slate-900 mb-4 flex items-center gap-2"><span>👗</span> 全家协调穿搭卡片</h2>
      <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">{outfits_html}</div>
    </div>
    <div class="bg-white rounded-3xl p-6 shadow-sm border border-slate-200">
      <h2 class="text-lg font-bold text-slate-900 mb-4 flex items-center gap-2"><span>📅</span> 逐日保姆级时间表</h2>
      <div class="space-y-4">{days_html}</div>
    </div>
    <div class="bg-white rounded-3xl p-6 shadow-sm border border-slate-200 overflow-x-auto">
      <h2 class="text-lg font-bold text-slate-900 mb-4 flex items-center gap-2"><span>💰</span> 餐饮买券省钱总表</h2>
      <table class="w-full text-xs text-left">
        <thead><tr class="bg-slate-100 text-slate-700"><th class="p-2.5 rounded-l-lg">餐厅场景</th><th class="p-2.5">特色菜品</th><th class="p-2.5">原价</th><th class="p-2.5">券后价</th><th class="p-2.5">立省</th><th class="p-2.5 rounded-r-lg">买券平台</th></tr></thead>
        <tbody class="divide-y divide-slate-100">{deals_html}</tbody>
      </table>
    </div>
    <div class="bg-white rounded-3xl p-6 shadow-sm border border-slate-200">
      <h2 class="text-lg font-bold text-slate-900 mb-4 flex items-center gap-2"><span>🛒</span> 行前打勾清单</h2>
      <div class="grid grid-cols-1 sm:grid-cols-2 gap-2 text-xs">{check_html}</div>
    </div>
    <div class="bg-slate-900 text-slate-400 rounded-3xl p-6 text-center text-xs space-y-2">
      <div class="text-white font-bold text-sm">{data["footer"]["wish"]}</div>
      <div>{data["footer"]["hotel"]}</div>
      <div class="flex justify-center flex-wrap gap-3 pt-2 text-slate-300">{hotlines_html}</div>
    </div>
  </div>
</body>
</html>"""

def generate_web(input_path, output_path):
    data = parse_travel_markdown(input_path) if input_path and os.path.exists(input_path) else parse_travel_markdown(__file__)
    
    try:
        from jinja2 import Template
        template_path = os.path.join(os.path.dirname(current_dir), "templates", "web_template.html")
        with open(template_path, "r", encoding="utf-8") as f:
            tmpl = Template(f.read())
        html_out = tmpl.render(data=data)
    except ImportError:
        html_out = render_fallback_html(data)
        
    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html_out)
    print(f"Successfully generated single-page web app at: {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate Single Page Web App from travel markdown")
    parser.add_argument("--input", "-i", default="", help="Path to travel markdown file")
    parser.add_argument("--output", "-o", default="dist/index.html", help="Path to output html file")
    args = parser.parse_args()
    generate_web(args.input, args.output)
