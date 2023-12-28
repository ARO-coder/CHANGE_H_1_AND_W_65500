from PIL import Image

img = Image.open('d.png')

    # Resize the image (w,h)
resized_img = img.resize((200,325))



    # Save the resized image
resized_img.save('out.png')
