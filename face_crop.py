import cv2
def cropper(path, output_path):
    image=cv2.imread(path)
    gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.3,
            minNeighbors=3,
            minSize=(30, 30)
    )    
    print("[INFO] Found {0} Faces!".format(len(faces)))

    for (x, y, w, h) in faces: #only extract the face found first
        #cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        c1=int(w/3)
        c2=int(h/3)
        print(w,h)

        roi_color = image[(y-c2):(y + h + c2), (x-c1):(x + w + c1)] 

        print("[INFO] Object found. Saving locally.") 
        cv2.imwrite(output_path, roi_color)