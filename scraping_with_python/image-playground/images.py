from PIL import Image, ImageFilter

img = Image.open('./Pokedex/pikachu.jpg')
filtered_img = img.convert('L')  # greyscale image.
box = (100,100,400,400)
region = filtered_img.crop(box)
region.save("grey.png", 'png')