from PIL import Image
import math

img = Image.open("exp1.bmp")

width = 65

colordict = {
    (0,0,0): "@",
    (255,49,24) : "#",
    (255,148,90) : ">",
    (198,99,0) : "%",
    (255,255,255) : ".",
    (0, 132, 198) : "+"
}
    

# img = img.convert('L')
pixels = img.getdata()

#print(pixels[0])

#for pixel in pixels:
#    print(sum(list(pixel)))

new_pixels = [colordict[pixel] for pixel in pixels]
new_pixels = ''.join(new_pixels)

new_pixels_count = len(new_pixels)

final_image = [new_pixels[index : index+width] for index in range(0, new_pixels_count, width)]
final_image = "\",\n\"".join(final_image)

with open("ascii.txt", "w") as f:
    f.write(final_image)


