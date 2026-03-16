#The purpose of this script is to generate consistent backgrounds to use in the grub themes. 
# This fixes an issue that as of March 2026 exists with QEMU and Grub2 backgrounds not rendering correctly. 
# This may not be needed in the future, but having a script to generate the backgrounds is overall considerably more time efficient.
from PIL import Image, ImageDraw
import os



COLOR = (118, 112, 150, 80) # Semi-transparent purple at 50% transparency: RGBA (75, 0, 130, 128)
OUTPUT_DIR = "/mnt/gentoo/boot/grub/themes/gentoo_glass" #Where do we wanna store our image?
SLICE_HEIGHT = 50  # Width and height of each slice in pixels
SLICE_WIDTH = 5 # Width of the slice
CORNER_RADIUS = 5  # Corner radius in pixels (0 = no rounding)
slices = ["w", "c", "e"] #The slices we wanna generate, w is left , c is center, e is right
os.makedirs(OUTPUT_DIR, exist_ok=True) #make sure our output directory exists and if it doesn't, we create it.

for s in slices:
    #This is the center slice so we just add a color and nothing else and continue.
    if s == "c" or CORNER_RADIUS == 0:
        img = Image.new("RGBA", (SLICE_WIDTH, SLICE_HEIGHT), COLOR)
        img.save(f"{OUTPUT_DIR}/select_{s}.png")
        continue;

    wide = Image.new("RGBA", (SLICE_WIDTH * 2, SLICE_HEIGHT), (0, 0, 0, 0))
    draw = ImageDraw.Draw(wide)
    draw.rounded_rectangle([0, 0, SLICE_WIDTH * 2 - 1, SLICE_HEIGHT - 1], radius=CORNER_RADIUS, fill=COLOR)

    # Round our left and right button corners.
    if s == "w":
        img = wide.crop((0, 0, SLICE_WIDTH, SLICE_HEIGHT)) # left portion of button
    elif s == "e":
        img = wide.crop((SLICE_WIDTH, 0, SLICE_WIDTH * 2, SLICE_HEIGHT)) # right portion of button
    img.save(f"{OUTPUT_DIR}/select_{s}.png")

print("Done. Images written to", OUTPUT_DIR)
