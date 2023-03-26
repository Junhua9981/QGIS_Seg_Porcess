# QGIS_Seg_Process_Util  

## When to Use This Tool  
In image segmentation tasks, we may need a dataset in which each image is a PNG file, and all pixels only contain RGB values from [1 - n-1].  
However, QGIS does not have this function built-in, so this tool was developed for this purpose.  

## How to Use  
Categorize each class separately and export the annotated images as transparent PNG files with the following file structure:  
```
|- 2017_Label_Veg  
|- 2017_Label_[class_name]  
|- ...  
```
Run ` python conv_dataset.py.`  
## What is the Output  
A PNG file is generated with (0,0,0,255) overlaid on (n-1, n-1, n-1, 255) according to the class order.  

## Other Tools  
`copy_target.py` copies the target image files with the same filename to the specified folder.  
`count_pixel.py` calculates how many of each pixel exists and their percentage  
