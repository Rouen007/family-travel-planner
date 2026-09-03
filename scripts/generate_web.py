"""
Single-Page Web App Generator
Compiles travel plan data into an interactive responsive HTML webpage.
Zero-dependency with Jinja2 auto-detection.
"""
import os
import sys
import argparse

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, current_dir)
from parser import parse_travel_markdown
from renderer import render_template

def generate_web(input_path, output_path):
    data = parse_travel_markdown(input_path) if input_path and os.path.exists(input_path) else parse_travel_markdown("")
    template_path = os.path.join(os.path.dirname(current_dir), "templates", "web_template.html")
    
    if not os.path.exists(template_path):
        raise FileNotFoundError(f"Web template not found at {template_path}")

    with open(template_path, "r", encoding="utf-8") as f:
        tmpl_str = f.read()

    html_out = render_template(tmpl_str, {"data": data})
    
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
