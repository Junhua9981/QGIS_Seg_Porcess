from PIL import Image
import os
def merge_pics(file_paths, output_path):

    all_transparent = True

    imgs = []

    for file_path in file_paths:
        imgs.append(Image.open(file_path).convert('RGBA'))

    width, height = imgs[0].size

    new_img = Image.new('RGBA', (width, height), (0, 0, 0, 255))

    for x in range(width):
        for y in range(height):

            for idx, img in enumerate(imgs):

                r, g, b, a = img.getpixel((x, y))

                if a == 0:
                    pass
                # 如果該像素點的alpha值不為0，即為非透明的，將該點設為黑色
                else:
                    all_transparent = False
                    color_num = idx + 1
                    new_img.putpixel((x, y), (color_num, color_num, color_num, 255))

    if all_transparent:
        return False
    

    new_img.save(output_path)
    return True


LABEL_NAMES = [
    "Veg",
    "Orchard",
    "Swamp",
    "Sandbar",
    "Waterbody",
    "Builtup",
]

f = open("filelist.txt", "a")
sf = open("shortfilelist.txt", "a")
fail_txt = open("fail.txt", "a")
index = 0

FILE_DIR = "./14"
LABEL_DIR = "./2017_Label"
for root, dirs, files in os.walk( FILE_DIR ):
    for file in files:
        if file.endswith(".png"):
            success = merge_pics(
                [ os.path.join(root.replace("Veg", name), file) for name in LABEL_NAMES ],
                  os.path.join( LABEL_DIR , root[ -5 :]+"_"+file) 
                )
            if success:
                f.write( os.path.join( LABEL_DIR , root[ -5 :]+"_"+file) + "\n" )
                sf.write( os.path.join( r"2017_Label" , root[ -5 :]+"_"+file) + "\n" )
                print("Success", os.path.join(root, file) )
            else:
                print("All Transparent", os.path.join(root, file))
                fail_txt.write( os.path.join( r"2017_Label" , root[ -5 :]+"_"+file) + "\n" )
        index += 1
        if index == 200:
            f.flush()
            sf.flush()
            fail_txt.flush()
            index = 0

f.close()
sf.close()
fail_txt.close()