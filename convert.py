from PIL import Image
import math

# 読み込み
with open("a.spaces", "r", encoding="utf-8") as f:
    text = f.read()

# 1次元化
pixels_1d = []
for char in text:
    if char == ' ':
        pixels_1d.append(0)  # 黒
    elif char == '　':
        pixels_1d.append(1)  # 白
    # 改行やその他は無視

N = len(pixels_1d)

# 最小の平方サイズ
size = math.ceil(math.sqrt(N))

# 画像作成（白背景）
img = Image.new("RGB", (size, size), (255, 255, 255))
pix = img.load()

# 配置（行優先）
for i, val in enumerate(pixels_1d):
    x = i % size
    y = i // size

    if val == 0:
        pix[x, y] = (0, 0, 0)
    else:
        pix[x, y] = (255, 255, 255)

# 拡大（任意：見やすさ向上）
scale = 8
img = img.resize((size * scale, size * scale), Image.NEAREST)

img.save("a.png")