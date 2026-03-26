#!/usr/bin/env python3
from collections import deque
import os

import numpy as np
from PIL import Image, ImageDraw, ImageFont

MEDIA = '/home/kangah/Desktop/MasterThesisLsu/media'
FONT_BOLD = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
TITLE_SIZE = 38


def find_top_legend_circle(img):
    arr = np.array(img.convert('RGBA'))
    h, w = arr.shape[:2]
    x_start = int(w * 0.64)
    red = arr[:, x_start:, 0]
    green = arr[:, x_start:, 1]
    blue = arr[:, x_start:, 2]
    alpha = arr[:, x_start:, 3]

    mask = (
        (red > 180) &
        (green > 60) & (green < 140) &
        (blue > 40) & (blue < 130) &
        (alpha == 255)
    )

    seen = np.zeros_like(mask, dtype=bool)
    candidates = []
    region_h, region_w = mask.shape

    for y in range(region_h):
        for x in range(region_w):
            if not mask[y, x] or seen[y, x]:
                continue

            q = deque([(x, y)])
            seen[y, x] = True
            area = 0
            min_x = max_x = x
            min_y = max_y = y

            while q:
                cx, cy = q.popleft()
                area += 1
                min_x = min(min_x, cx)
                max_x = max(max_x, cx)
                min_y = min(min_y, cy)
                max_y = max(max_y, cy)

                for nx, ny in ((cx + 1, cy), (cx - 1, cy), (cx, cy + 1), (cx, cy - 1)):
                    if 0 <= nx < region_w and 0 <= ny < region_h and mask[ny, nx] and not seen[ny, nx]:
                        seen[ny, nx] = True
                        q.append((nx, ny))

            width = max_x - min_x + 1
            height = max_y - min_y + 1
            abs_min_x = min_x + x_start
            abs_max_x = max_x + x_start

            if (
                1400 <= area <= 2200 and
                40 <= width <= 55 and
                40 <= height <= 55 and
                abs_min_x > int(w * 0.66) and
                min_y > int(h * 0.35)
            ):
                candidates.append((min_y, abs_min_x, abs_max_x, max_y))

    if not candidates:
        raise RuntimeError('Could not find a legend circle')

    candidates.sort()
    top_y, left_x, right_x, bottom_y = candidates[0]
    return left_x, top_y, right_x, bottom_y


def add_legend_title(filename, title, kind):
    src = os.path.join(MEDIA, filename)
    img = Image.open(src).copy()
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(FONT_BOLD, TITLE_SIZE)

    circle_left, circle_top, _, _ = find_top_legend_circle(img)
    if kind == 'vel':
        title_x = circle_left - 12
    else:
        title_x = circle_left - 50
    title_y = circle_top - TITLE_SIZE - 15

    bbox = draw.textbbox((title_x, title_y), title, font=font)
    draw.rectangle(
        [bbox[0], bbox[1] - 5, bbox[2] + 5, bbox[3] + 5],
        fill='white',
    )
    draw.text((title_x, title_y), title, fill='black', font=font)
    img.save(src, 'PNG')
    print(f'  Added "{title}" to {filename} at ({title_x}, {title_y})')


for f in ['rf_vel.png', 'et_vel.png', 'sbas_vel.png']:
    add_legend_title(f, 'Velocity (mm/yr)', 'vel')

for f in ['rf_susc.png', 'et_susc.png', 'sbas_susc.png']:
    add_legend_title(f, 'Susceptibility', 'susc')

print('Done.')
