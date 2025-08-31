import cv2
import sys
image = cv2.imread("Untitled design.jpeg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
faceCascade = cv2.CascadeClassifier("data\\haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier("data\\haarcascade_eye_tree_eyeglasses.xml")
faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.075,
    minNeighbors=5,
    minSize=(15, 15)
)
for (x,y,w,h) in faces:
    cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = image[y:y+h, x:x+w]
    eyes = eye_cascade.detectMultiScale(roi_gray)
    for (ex,ey,ew,eh) in eyes:
        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
print("[INFO] Found {0} Faces!".format(len(faces)))
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0,0,255), 2)
status = cv2.imwrite('Untitled design.jpg', image)
print("[INFO] Image Untitled design.jpg written to filesystem: ", status)