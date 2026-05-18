from PIL import Image, ImageDraw
W, H = 400, 250
background = Image.new("RGB", (W, H), (30, 65, 120))
foreground = Image.new("RGBA", (W, H), (0, 0, 0, 0))
draw = ImageDraw.Draw(foreground)
draw.rectangle((80, 50, 320, 200), fill=(255, 80, 40, 128)) # alpha=128/255
combined = Image.alpha_composite(background.convert("RGBA"), foreground)
combined.save("alpha_composite.png")