"""
2K Retina Mobile Long Poster Generator
Renders an HTML template into a high-DPI full-page PNG poster with automatic whitespace cropping.
Zero-dependency template rendering with cross-platform Chrome detection.
"""
import os
import sys
import shutil
import argparse
import subprocess
import tempfile

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, current_dir)
from parser import parse_travel_markdown
from renderer import render_template

def find_chrome_binary():
    if os.environ.get("CHROME_PATH") and os.path.exists(os.environ.get("CHROME_PATH")):
        return os.environ.get("CHROME_PATH")
    mac_paths = [
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        "/Applications/Chromium.app/Contents/MacOS/Chromium",
        "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge",
        os.path.expanduser("~/Applications/Google Chrome.app/Contents/MacOS/Google Chrome")
    ]
    for p in mac_paths:
        if os.path.exists(p): return p
    for bin_name in ["google-chrome", "google-chrome-stable", "chromium", "chromium-browser", "edge"]:
        path = shutil.which(bin_name)
        if path: return path
    return None

def render_poster(input_path, output_path, view=False):
    chrome_bin = find_chrome_binary()
    if not chrome_bin:
        print("⚠️ Warning: Google Chrome/Chromium binary not found in standard paths.")
        print("Please set CHROME_PATH environment variable to enable headless image rendering.")
        return False
        
    data = parse_travel_markdown(input_path) if input_path and os.path.exists(input_path) else parse_travel_markdown("")
    template_path = os.path.join(os.path.dirname(current_dir), "templates", "poster_template.html")
    
    if not os.path.exists(template_path):
        raise FileNotFoundError(f"Poster template not found at {template_path}")

    with open(template_path, "r", encoding="utf-8") as f:
        tmpl_str = f.read()

    html_content = render_template(tmpl_str, {"data": data})
    
    with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False, encoding="utf-8") as temp_html:
        temp_html.write(html_content)
        temp_html_path = temp_html.name

    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)

    cmd = [
        chrome_bin,
        "--headless",
        "--disable-gpu",
        "--hide-scrollbars",
        f"--screenshot={output_path}",
        "--window-size=1080,8800",
        f"file://{temp_html_path}"
    ]
    
    try:
        subprocess.run(cmd, check=True, capture_output=True)
    except Exception as e:
        print(f"Error executing Headless Chrome: {e}")
        if os.path.exists(temp_html_path): os.remove(temp_html_path)
        return False

    if os.path.exists(temp_html_path):
        os.remove(temp_html_path)

    try:
        from PIL import Image, ImageChops
        im = Image.open(output_path)
        bg = Image.new("RGB", im.size, (241, 245, 249))
        diff = ImageChops.difference(im.convert("RGB"), bg)
        bbox = diff.getbbox()
        if bbox:
            bottom = min(im.size[1], bbox[3] + 40)
            cropped_im = im.crop((0, 0, im.size[0], bottom))
            cropped_im.save(output_path)
            print(f"Successfully rendered and cropped 2K long poster at: {output_path} ({cropped_im.size[0]}x{cropped_im.size[1]}px)")
    except Exception as e:
        print(f"Pillow auto-crop note: {e}")

    if view and sys.platform == "darwin":
        subprocess.run(["open", output_path])

    return True

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Render 2K Mobile Long Poster from travel plan")
    parser.add_argument("--input", "-i", default="", help="Path to travel markdown file")
    parser.add_argument("--output", "-o", default="dist/travel_poster.png", help="Path to output PNG file")
    parser.add_argument("--view", "-v", action="store_true", help="Automatically open image after rendering")
    args = parser.parse_args()
    render_poster(args.input, args.output, args.view)
