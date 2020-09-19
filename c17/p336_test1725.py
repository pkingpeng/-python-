from PIL import Image

from c17.c17_image_constant import *

cat = Image.open(image_path + 'zophie.png')

cat.rotate(90).save(image_output_path + 'rotate90.png')
cat.rotate(180).save(image_output_path + 'rotate180.png')
cat.rotate(270).save(image_output_path + 'rotate270.png')

cat.rotate(6).save(image_output_path + 'rotete6.png')
cat.rotate(6, expand=True).save(image_output_path + 'rotete6_expanded.png')

cat.transpose(Image.FLIP_LEFT_RIGHT).save(image_output_path + 'horizontal_flip.png')
cat.transpose(Image.FLIP_TOP_BOTTOM).save(image_output_path + 'vertical_flip.png')

print('All done.')

"""
All done.
"""
