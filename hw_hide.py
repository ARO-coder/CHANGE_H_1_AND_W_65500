from PIL import Image

i = Image.open('out.png')

w,h = i.size

pix = [i.getpixel((x, y)) for y in range(h) for x in range(w)]

new =  Image.new('RGB', (w * h,1))

new.putdata(pix)

new.save('tt.jpg')
