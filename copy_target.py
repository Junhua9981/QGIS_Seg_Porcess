import os
import shutil



target_dir = "./14"
dest_dir = "./2017_Target"
for root, dirs, files in os.walk("2017_Label"):
    for file in files:
        if file.endswith(".png"):
            src = os.path.join( target_dir, file.split("_")[0], file.split("_")[1].replace(".png", ".jpg") )
            dst = os.path.join( dest_dir, file.replace(".png", ".jpg") )
            shutil.copyfile(src, dst)

print("Done")
    