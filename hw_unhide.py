from PIL import Image

img = Image.open('tt.jpg').convert('RGB')
new_img = Image.new('RGB', (200,326))

w = h = 0

for i in range(0, img.size[0]):
    r,g,b = img.getpixel((i, 0))
    w = (i % 200)
    if i % 200 == 0:
        h = h + 1
        print(h)
    new_img.putpixel((w,h), (r,g,b))

new_img.save('k.jpg')
