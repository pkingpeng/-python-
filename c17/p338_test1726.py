from PIL import Image, ImageColor

from c17.c17_image_constant import *

im = Image.new('RGBA', (100, 100))
print(im.getpixel((0, 0)))

for x in range(100):
    for y in range(50):
        im.putpixel((x, y), (210, 210, 210))

for x in range(100):
    for y in range(50, 100):
        im.putpixel((x, y), ImageColor.getcolor('darkgray', 'RGBA'))

print(im.getpixel((0, 0)))
print(im.getpixel((0, 50)))

im.save(image_output_path + 'putPixel.png')
print('All done.')

"""
(0, 0, 0, 0)
(210, 210, 210, 255)
(169, 169, 169, 255)
All done.
"""
