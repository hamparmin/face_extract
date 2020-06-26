#load dependencies
import cv2
from pathlib import Path
from rm_background import replace_background
from face_crop import cropper
import numpy as np

#specify paths
original_path="images\\test1.jpg"
background_removed_path="images\\clean.jpg"
cropped_path="images\\cropped.jpg"

#run background removal
replace_background(original_path, background_removed_path)

#run face crop
cropper(background_removed_path, cropped_path)

#display images
img1=cv2.imread(original_path)
img2=cv2.imread(background_removed_path)
img3=cv2.imread(cropped_path)

numpy_horizontal = np.hstack((img1,img2,img3))

cv2.imshow(numpy_horizontal)

cv2.waitKey(0)