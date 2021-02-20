from PIL import Image

# Converts images/bitmaps directly to ascii-art.
# Colors need to be predefined and the output does need some further
# formatting before it can replace the frames in the .json file.

# manually change your frame here.
img = Image.open("exp1.bmp")

# images need to have a resolution of w: 65, h: 63
width = 65

# all colors in your frames need to be predefined here. (R,G,B)
colordict = {
    (0,0,0): "@",
    (255,49,24) : "#",
    (255,148,90) : ">",
    (198,99,0) : "%",
    (255,255,255) : ".",
    (0, 132, 198) : "+"
}

pixels = img.getdata()

new_pixels = [colordict[pixel] for pixel in pixels]
new_pixels = ''.join(new_pixels)

new_pixels_count = len(new_pixels)

final_image = [new_pixels[index : index+width] for index in range(0, new_pixels_count, width)]
final_image = "\",\n\"".join(final_image)

with open("ascii.txt", "w") as f:
    f.write(final_image)

