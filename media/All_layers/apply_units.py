#!/usr/bin/env python3
from PIL import Image, ImageDraw, ImageFont
import numpy as np
import os
import shutil

BASE = '/home/kangah/Desktop/MasterThesisLsu/media/All_layers'
OUT = os.path.join(BASE, 'with_units')
os.makedirs(OUT, exist_ok=True)

FONT_BOLD = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
FONT_REG = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'


def annotate_inline_unit(filename, text, x, y, fontsize, bold=True, pad=4):
    src = os.path.join(BASE, filename)
    out = os.path.join(OUT, filename)
    img = Image.open(src).copy()
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(FONT_BOLD if bold else FONT_REG, fontsize)
    bbox = draw.textbbox((x, y), text, font=font)
    draw.rectangle(
        [bbox[0], bbox[1] - pad, bbox[2] + pad, bbox[3] + pad],
        fill='white',
    )
    draw.text((x, y), text, fill='black', font=font)
    img.save(out, 'PNG')


def copy_original(filename):
    shutil.copy2(os.path.join(BASE, filename), os.path.join(OUT, filename))


# Copy all image layers first so the output folder is complete.
for entry in os.listdir(BASE):
    src = os.path.join(BASE, entry)
    if os.path.isfile(src) and entry.lower().endswith(('.png', '.jpg', '.jpeg', '.tif', '.tiff')):
        copy_original(entry)


# Large map legends: unit placed inline with "Value".
VALUE_OFFSET = 172
large_map_units = [
    ('dem.png', ' (m)', 1713, 964, 48),
    ('aspect.png', ' (°)', 1709, 966, 48),
    ('slope.png', ' (°)', 1738, 970, 48),
    ('dtf.png', ' (°)', 1708, 969, 48),
    ('distancefrod.png', ' (m)', 1719, 970, 48),
    ('distancebridge.png', ' (m)', 1706, 966, 48),
    ('distancerail.png', ' (m)', 1705, 968, 48),
    ('distanceriver.png', ' (m)', 1720, 965, 48),
    ('preci.png', ' (mm)', 1715, 974, 48),
]

for filename, unit, value_x, value_y, fontsize in large_map_units:
    annotate_inline_unit(filename, unit, value_x + VALUE_OFFSET, value_y, fontsize)


# TPI has a smaller legend, but the same "Value (unit)" pattern.
annotate_inline_unit('TPI.png', ' (m)', 608, 290, 18, pad=2)


# Curvature has a smaller legend; unit provided by user as per meter.
annotate_inline_unit('Curvature.png', ' (1/m)', 623, 300, 14, pad=2)


# Replace gray (193,193,193) background with white on slope.
slope_path = os.path.join(OUT, 'slope.png')
slope_img = Image.open(slope_path)
data = np.array(slope_img)
mask = (data[:, :, 0] == 193) & (data[:, :, 1] == 193) & (data[:, :, 2] == 193)
data[mask] = [255, 255, 255, 255]
Image.fromarray(data).save(slope_path, 'PNG')

# Leave these unchanged because they are categorical or unitless in this set.
# lulcnew.png, geology.png, well.png, twi.png

print(f'Annotated layers saved to: {OUT}')
