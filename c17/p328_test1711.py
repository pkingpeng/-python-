from PIL import ImageColor

print(ImageColor.getcolor('red', 'RGBA'))
print(ImageColor.getcolor('RED', 'RGBA'))
print(ImageColor.getcolor('Black', 'RGBA'))
print(ImageColor.getcolor('chocolate', 'RGBA'))
print(ImageColor.getcolor('CornflowerBlue', 'RGBA'))

"""
(255, 0, 0, 255)
(255, 0, 0, 255)
(0, 0, 0, 255)
(210, 105, 30, 255)
(100, 149, 237, 255)
"""
