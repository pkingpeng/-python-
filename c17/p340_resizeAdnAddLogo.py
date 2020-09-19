#! python3
# Resizes all images in current working directory to
# fit in a  300*300 square, and adds catlogo.png to the lower-right corner.

import os

from PIL import Image

os.chdir('/Users/moqi/Downloads/output')
logo_dir = 'withLogo'
os.makedirs(logo_dir, exist_ok=True)

square_fit_size = 300
logo_filename = 'catlogo.png'

logoIm = Image.open(logo_filename)
logoWidth, logoHeight = logoIm.size

for filename in os.listdir('.'):
    if not (filename.endswith('.png') or filename.endswith('.jpg')) \
            or filename == logo_filename:
        continue

    im = Image.open(filename)
    width, height = im.size

    if width > square_fit_size and height > square_fit_size:
        if width > height:
            height = int((square_fit_size / width) * height)
            width = square_fit_size
        else:
            width = int((square_fit_size / height) * width)
            height = square_fit_size

        print('Resizing %s...' % filename)
        im = im.resize((width, height))

    print('Adding logo to %s...' % filename)
    im.paste(logoIm, (width - logoWidth, height - logoHeight), logoIm)
    im.save(os.path.join(logo_dir, filename))

"""
试了作者的原程序，跑出来也是每个图片左上角多了一个 logo 猫的尾巴，
可能的原因有：图片大小和位置，以及 API 升级，后面再调试。
"""
