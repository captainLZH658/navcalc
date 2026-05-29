"""Generate anchor icons for all required sizes."""
import os
from PIL import Image, ImageDraw

ICONS_DIR = r'D:\Users\Admin\Desktop\航海计算APP\icons'
SIZES = [72, 96, 128, 144, 152, 192, 384, 512]
BG_COLOR = (31, 78, 121)  # #1F4E79
WHITE = (255, 255, 255)

def draw_anchor(draw, size, margin=0.15):
    """Draw a classic anchor shape centered in the given size."""
    cx, cy = size // 2, size // 2
    r = size // 2 - int(size * margin)
    
    # Ring at top
    ring_r = int(r * 0.18)
    draw.ellipse([cx - ring_r, int(cy - r * 0.75) - ring_r,
                  cx + ring_r, int(cy - r * 0.75) + ring_r],
                 outline=WHITE, width=max(2, size // 40))
    
    # Stock (horizontal bar)
    stock_w = int(r * 0.6)
    stock_y = int(cy - r * 0.4)
    draw.line([cx - stock_w, stock_y, cx + stock_w, stock_y],
              fill=WHITE, width=max(2, size // 30))
    
    # Shank (vertical bar)
    draw.line([cx, int(cy - r * 0.65), cx, int(cy + r * 0.35)],
              fill=WHITE, width=max(2, size // 25))
    
    # Left arm (curved)
    arm_rx = int(r * 0.45)
    arm_ry = int(r * 0.35)
    draw.arc([cx - arm_rx, cy - arm_ry, cx + arm_rx, cy + arm_ry],
             start=200, end=340, fill=WHITE, width=max(2, size // 30))
    
    # Left fluke (arrow-like tip on left)
    fluke_y = int(cy + r * 0.3)
    fluke_x = cx - int(r * 0.38)
    draw.polygon([
        (fluke_x, fluke_y),
        (fluke_x - int(r * 0.15), fluke_y + int(r * 0.15)),
        (fluke_x, fluke_y - int(r * 0.08))
    ], fill=WHITE, outline=WHITE)
    
    # Right fluke
    fluke_x2 = cx + int(r * 0.38)
    draw.polygon([
        (fluke_x2, fluke_y),
        (fluke_x2 + int(r * 0.15), fluke_y + int(r * 0.15)),
        (fluke_x2, fluke_y - int(r * 0.08))
    ], fill=WHITE, outline=WHITE)

def generate_icons():
    for s in SIZES:
        img = Image.new('RGBA', (s, s), BG_COLOR)
        draw = ImageDraw.Draw(img)
        
        # Draw circular background (masked)
        mask = Image.new('L', (s, s), 0)
        mask_draw = ImageDraw.Draw(mask)
        mask_draw.ellipse([0, 0, s-1, s-1], fill=255)
        
        # Apply circular mask
        circle = Image.new('RGBA', (s, s), BG_COLOR)
        circle.putalpha(mask)
        
        # Draw anchor on white background then composite
        anchor_img = Image.new('RGBA', (s, s), (0,0,0,0))
        anchor_draw = ImageDraw.Draw(anchor_img)
        draw_anchor(anchor_draw, s)
        
        # Composite
        final = Image.alpha_composite(circle, anchor_img)
        
        path = os.path.join(ICONS_DIR, f'icon-{s}x{s}.png')
        final.save(path, 'PNG')
        print(f'Created {path} ({s}x{s})')

generate_icons()
