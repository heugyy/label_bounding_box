# label_bounding_box

## main.py
The `main.py` records the location (left corner point(x1,y1) and right corner (x2,y2)) and save in file `results.txt`. In each row of the file, the document arranges as `file_path, class_label, x1_1,y1_1,x2_1,y2_1,  x1_2,,y1_2,x2_2,y2_2,...`.

Usage:
1. arragne your data into the folders of each according classes, the folder names indicate the class labels.
2. Change the 'data_pth' to your image folder, and then run the main.py and show the image.
3. In the image, firstly click the left corner and then the right corner of ROI for recording x1_1,y1_1,x2_1,y2_1. You can click multiple ROIs.
4. Close the current image once finished, and then the second image shows repeat step 3.

## rearrange.py
The `rearrange.py` converts the location format to `center_x, center_y, width, height`.

