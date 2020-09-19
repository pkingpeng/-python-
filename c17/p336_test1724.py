from PIL import Image

from c17.c17_image_constant import *

cat = Image.open(image_path + 'zophie.png')

catWidth, catHeight = cat.size
quarterSizeIm = cat.resize((int(catWidth / 2), int(catHeight / 2)))
quarterSizeIm.save(image_output_path + 'quartersized.png')

svelteIm = cat.resize((catWidth, catHeight + 300))
svelteIm.save(image_output_path + 'svelte.png')
print('All done')

"""
All done
"""
