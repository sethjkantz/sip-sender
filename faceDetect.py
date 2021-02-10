# Seth Kantz
# https://realpython.com/face-detection-in-python-using-a-webcam/
# will want to switch to use camera and grab() at some point
# https://docs.opencv.org/3.4/d8/dfe/classcv_1_1VideoCapture.html#ab5b7391cd5ec50e7237e575a758f6f05
   #     https://www.pyimagesearch.com/2015/01/19/find-distance-camera-objectmarker-using-python-opencv/


import cv2
import sys
FOCAL = 1250

# takes known width and pixel width to calculate dist in string format
# image detects ~ 5 inch square

def dist2CamStr(knownWidth,pixWidth):
    
    inches = (knownWidth * FOCAL) / pixWidth
    if(inches < 12):
        dist = "%0.2f in" %inches
    else:
        feet = (inches - (inches % 12.0)) / 12.0
        inches = inches % 12.0
        dist = "%0.0f ft %0.2f in" % (feet, inches)
    return dist


# Get user supplied values
imagePath = sys.argv[1]
cascPath = "src/haarcascade_frontalface_default.xml"

# Create the haar cascade
faceCascade = cv2.CascadeClassifier(cascPath)

# Read the image
image = cv2.imread(imagePath)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.2,
    minNeighbors=5,
    minSize=(30, 30),
    flags = cv2.CASCADE_SCALE_IMAGE
)

print("Found {0} faces!".format(len(faces)))

# Draw a rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
    dist = dist2CamStr(5.0,w)
    cv2.putText(image,str(dist) ,(x, y+w+60), cv2.FONT_HERSHEY_SIMPLEX,1.5, (0, 255, 0), 3)

cv2.imshow("Faces found", image)
cv2.waitKey(0)

