from PIL import Image
import os

INPUT_DIR = "img"
THUMBS_DIR = "img/thumbs"
FULL_DIR = "img/full"

os.makedirs(THUMBS_DIR, exist_ok=True)
os.makedirs(FULL_DIR, exist_ok=True)

for file in os.listdir(INPUT_DIR):
    if file.lower().endswith((".jpg", ".jpeg", ".png")):

        path = os.path.join(INPUT_DIR, file)
        img = Image.open(path)

        # FULL optimize
        full = img.copy()
        full.thumbnail((3000, 3000))
        full.save(os.path.join(FULL_DIR, file), quality=85, optimize=True)

        # THUMB
        thumb = img.copy()
        thumb.thumbnail((800, 800))
        thumb.save(os.path.join(THUMBS_DIR, file), quality=80, optimize=True)

        print("Processed:", file)

print("Bitti 🚀")