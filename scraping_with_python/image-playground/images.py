from PIL import Image, ImageFilter

img = Image.open('./Pokedex/pikachu.jpg')
# print(img)
# print(img.format)
# print(img.size)
# print(img.mode)

# print(dir(img))

# filtered_img = img.filter(ImageFilter.SHARPEN)
filtered_img = img.convert('L')  # greyscale image.
filtered_img.save("grey.png", 'png')
