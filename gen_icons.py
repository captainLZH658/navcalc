"""Generate PWA icons with Pillow - white ship wheel on navy blue background"""
import os
from PIL import Image, ImageDraw

OUTPUT_DIR = r'D:\Users\Admin\Desktop\航海计算APP\icons'
os.makedirs(OUTPUT_DIR, exist_ok=True)

NAVY = (31, 78, 121)      # #1F4E79
WHITE = (255, 255, 255)
LIGHT = (200, 220, 240)

def draw_wheel(draw, cx, cy, r, fill):
    """Draw a simple ship wheel symbol"""
    # Outer circle (rim)
    draw.ellipse([cx-r, cy-r, cx+r, cy+r], outline=fill, width=max(1, r//12))
    # Inner circle (hub)
    hub_r = r // 4
    draw.ellipse([cx-hub_r, cy-hub_r, cx+hub_r, cy+hub_r], fill=fill)
    # 8 spokes
    for angle in range(0, 360, 45):
        import math
        rad = math.radians(angle)
        # Spoke line from inner to outer
        x1 = cx + hub_r * math.cos(rad)
        y1 = cy + hub_r * math.sin(rad)
        x2 = cx + (r - r//8) * math.cos(rad)
        y2 = cy + (r - r//8) * math.sin(rad)
        draw.line([(x1, y1), (x2, y2)], fill=fill, width=max(1, r//16))

sizes = [72, 96, 128, 144, 152, 192, 384, 512]
for s in sizes:
    img = Image.new('RGB', (s, s), NAVY)
    draw = ImageDraw.Draw(img)
    cx = cy = s // 2
    r = int(s * 0.4)
    draw_wheel(draw, cx, cy, r, WHITE)
    fn = os.path.join(OUTPUT_DIR, f'icon-{s}x{s}.png')
    img.save(fn, 'PNG')
    print(f'Created {fn} ({s}x{s})')

print('Done')
