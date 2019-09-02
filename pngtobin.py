from pil import Image

image = Image.open('tiger.png')
pixels = image.load()

out_file = open('image.bin', 'wb')

for y in range(128):
    for x in range(128):
        out_file.write(chr(pixels[x,y]))
