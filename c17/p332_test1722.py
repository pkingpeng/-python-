from PIL import Image

from c17.c17_image_constant import *

cat = Image.open(image_path + 'zophie.png')
croppedIm = cat.crop((335, 345, 565, 560))
croppedIm.save(image_output_path + 'cropped.png')
print('All done')

"""
All done
"""
