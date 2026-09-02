import subprocess
from PIL import Image, ImageChops

html_path = "/Users/rouen/Documents/coding/poster_cartoon.html"
out_png = "/Users/rouen/Documents/coding/上海亲子自驾游完整攻略_超清长图.png"
chrome_bin = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

cmd = [
    chrome_bin,
    "--headless",
    "--disable-gpu",
    f"--screenshot={out_png}",
    "--window-size=1080,8800",
    f"file://{html_path}"
]

res = subprocess.run(cmd, capture_output=True, text=True)
print("Rendered headless screenshot.")

im = Image.open(out_png)
bg = Image.new("RGB", im.size, (241, 245, 249))
diff = ImageChops.difference(im.convert("RGB"), bg)
bbox = diff.getbbox()

if bbox:
    bottom = min(im.size[1], bbox[3] + 40)
    cropped_im = im.crop((0, 0, im.size[0], bottom))
    cropped_im.save(out_png)
    print(f"Cropped to exact dimensions: {cropped_im.size}")

subprocess.run(["open", out_png])
