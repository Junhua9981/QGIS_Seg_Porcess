from PIL import Image
import os
def count_pics(file_path):
    img = Image.open(file_path).convert('RGBA')
    width, height = img.size

    clazz=[0,0,0,0,0,0,0,]
    for w in range(width):
        for h in range(height):
            r, g, b, a = img.getpixel((w, h))
            clazz[r] += 1
        
    return clazz
            
    
num_of_pixels = [0,0,0,0,0,0,0,]

for root, dirs, files in os.walk("2017_Label"):
    for file in files:
        if file.endswith(".png"):
            clazz = count_pics(os.path.join(root, file))
            
            for i in range(7):
                num_of_pixels[i] += clazz[i]
            # print(f"{file} {clazz}")
print(num_of_pixels)
print(f"total: {sum(num_of_pixels)}")

LABEL_NAMES = [
    "background",
    "Veg",
    "Orchard",
    "Swamp",
    "Sandbar",
    "Waterbody",
    "Builtup",
]
for name, num in zip(LABEL_NAMES, num_of_pixels):
    print(f"{name}: {num} ({num/sum(num_of_pixels):.2%})")
    