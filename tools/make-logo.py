"""Draw the $DOSSIER logo (1024x1024, flat vector poster style).

One bold subject: a kraft dossier folder, stamped TOP SECRET, with a gold
coin peeking out of the top. Big readable text only: DOSSIER, TOP SECRET,
coin.dossier.json, make.fun. Dark teal background, high contrast.
No gradients, no photo, no copied art — drawn with PIL primitives.
"""
from PIL import Image, ImageDraw, ImageFont

W = 1024
BG = (14, 59, 51)          # deep teal
FOLDER = (232, 200, 126)   # kraft manila
FOLDER_DARK = (203, 168, 94)
TAB = (232, 200, 126)
RED = (192, 57, 43)        # stamp red
INK = (26, 26, 26)
GOLD = (245, 197, 66)
GOLD_DARK = (212, 160, 32)
CREAM = (250, 243, 224)

FONT_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def font(size, bold=True):
    return ImageFont.truetype(FONT_BOLD if bold else FONT, size)


img = Image.new("RGB", (W, W), BG)
d = ImageDraw.Draw(img)

# subtle dotted frame corners (faint, keeps thumbnail clean)
for x in range(48, W - 48, 64):
    d.ellipse([x, 40, x + 8, 48], fill=(30, 90, 78))
    d.ellipse([x, W - 48, x + 8, W - 40], fill=(30, 90, 78))

# gold coin peeking out of the folder top (circle + $)
cx, cy, r = 512, 300, 118
d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=GOLD, outline=GOLD_DARK, width=10)
d.ellipse([cx - r + 26, cy - r + 26, cx + r - 26, cy + r - 26], outline=GOLD_DARK, width=6)
f_dollar = font(150)
tw = d.textlength("$", font=f_dollar)
d.text((cx - tw / 2, cy - 108), "$", font=f_dollar, fill=(120, 84, 10))

# folder tab (top-left)
d.rounded_rectangle([172, 330, 470, 420], radius=18, fill=FOLDER)
# folder body
d.rounded_rectangle([172, 380, 852, 880], radius=22, fill=FOLDER)
# folder inner shadow line (open-folder edge)
d.rounded_rectangle([172, 380, 852, 430], radius=22, fill=FOLDER_DARK)
d.rectangle([172, 405, 852, 430], fill=FOLDER_DARK)
# folder flap line
d.line([172, 715, 852, 715], fill=FOLDER_DARK, width=6)

# big title on the folder
f_title = font(132)
label = "DOSSIER"
tw = d.textlength(label, font=f_title)
d.text(((W - tw) / 2, 470), label, font=f_title, fill=INK)

# file label under the title (above the stamp, never overlapped)
f_file = font(52)
label2 = "coin.dossier.json"
tw = d.textlength(label2, font=f_file)
d.text(((W - tw) / 2, 625), label2, font=f_file, fill=(90, 60, 20))

# red TOP SECRET stamp, rotated -12 degrees, on its own layer (below the label)
stamp = Image.new("RGBA", (640, 170), (0, 0, 0, 0))
sd = ImageDraw.Draw(stamp)
f_stamp = font(76)
sd.rectangle([8, 8, 632, 162], outline=RED, width=9)
sd.rectangle([22, 22, 618, 148], outline=RED, width=3)
txt = "TOP SECRET"
tw = sd.textlength(txt, font=f_stamp)
sd.text(((640 - tw) / 2, 38), txt, font=f_stamp, fill=RED)
stamp = stamp.rotate(-12, resample=Image.BICUBIC, expand=False)
img.paste(stamp, (192, 735), stamp)

# bottom line: make.fun
f_site = font(46)
site = "make.fun"
tw = d.textlength(site, font=f_site)
d.text(((W - tw) / 2, 930), site, font=f_site, fill=CREAM)

img.save("/home/hatch/workspace/makefun/build/makefun-coin-promo-01-r5/logo.png")
print("logo saved, size:", img.size)
