from PIL import Image

from c17.c17_image_constant import *

cat = Image.open(image_path + 'zophie.png')
print(cat.size)
print(cat.filename)
print(cat.format)
print(cat.format_description)
cat.close()

print()

im = Image.new('RGBA', (100, 200), 'purple')
im.save(image_output_path + 'purpleImage.png')
im2 = Image.new('RGBA', (20, 20))
im2.save(image_output_path + 'transparentImage.png')
print('Output Success')

"""
(816, 1088)
../resource/image/zophie.png
PNG
Portable network graphics

Output Success
"""
