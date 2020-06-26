#load dependencies
import cv2
import os
from rm_background import replace_background
from face_crop import cropper
import numpy as np

#after placing images in images folder
image_names=os.listdir("images\\")

def extract(image_name):
    original_path="images\\"+image_name
    bg_rm_path="images\\"+"bg_rm_"+image_name
    cropped_path="images\\"+"cropped_"+image_name
    #run background removal
    replace_background(original_path, bg_rm_path)

    #run face crop
    cropper(bg_rm_path, cropped_path)

#main loop
for i in image_names:
    extract(i)

#display images
#   img3=cv2.imread(cropped_path)

# numpy_horizontal = np.hstack((img1,img2,img3))

# cv2.imshow(numpy_horizontal)

# cv2.waitKey(0)