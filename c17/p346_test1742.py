import os

from PIL import Image, ImageDraw, ImageFont

from c17.c17_image_constant import *

im = Image.new('RGBA', (200, 200), 'white')
draw = ImageDraw.Draw(im)

draw.text((20, 150), 'Hello World', fill='purple')
fontsFolder = '/System/Library/Fonts/Supplemental/'
arialFont = ImageFont.truetype(os.path.join(fontsFolder, 'arial.ttf'), 32)
draw.text((100, 150), 'moqimoqide', fill='gray', font=arialFont)

im.save(image_output_path + 'text.png')
print('All done.')
