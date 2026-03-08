#The purpose of this script is to generate consistent backgrounds to use in the grub themes. 
# This fixes an issue that as of March 2026 exists with QEMU and Grub2 backgrounds not rendering correctly. 
# This may not be needed in the future, but having a script to generate the backgrounds is overall considerably more time efficient.
from PIL import Image
import os


# Semi-transparent purple at 50% transparency: RGBA (75, 0, 130, 128)
COLOR = (75, 0, 130, 128)
OUTPUT_DIR = "/boot/grub/themes/gentoo-glass"
slices = ["w", "c", "e"]
os.makedirs(OUTPUT_DIR, exist_ok=True)

for s in slices:
    img = Image.new("RGBA", (10, 10), COLOR)
    img.save(f"{OUTPUT_DIR}/select_{s}.png")

print("Done. Images written to", OUTPUT_DIR)