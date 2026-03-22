from PIL import Image

# 入力ファイル
with open("a.spaces", "r", encoding="utf-8") as f:
    lines = f.read().splitlines()

height = len(lines)
width = max(len(line) for line in lines) if lines else 0

# 画像作成（白背景）
img = Image.new("RGB", (width, height), "white")
pixels = img.load()

for y, line in enumerate(lines):
    for x, char in enumerate(line):
        if char == ' ':
            pixels[x, y] = (0, 0, 0)  # 半角→黒
        elif char == '　':
            pixels[x, y] = (255, 255, 255)  # 全角→白
        # その他は無視（白のまま）

img.save("a.png")
