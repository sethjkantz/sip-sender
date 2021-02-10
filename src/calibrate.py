#will have to change around a little if we switch to vid
#1250 / 1300 ??
KNOWN_DIST = 36.0
KNOWN_WIDTH = 5.0


import cv2
import sys

# 3 ft from camera
# image detects ~ 5 inch square

# Get user supplied values
imagePath = sys.argv[1]
cascPath = "haarcascade_frontalface_default.xml"

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
    minSize=(30, 30)
   # flags = cv2.cv.CV_HAAR_SCALE_IMAGE
    #flags = cv2.CV_HAAR_SCALE_IMAGE

)

print("Found {0} faces!".format(len(faces)))

# Draw a rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
    focalLength = w * KNOWN_DIST / KNOWN_WIDTH
    print("focal length")
    print(focalLength)
    print(" \n");
cv2.imshow("Faces found", image)
cv2.waitKey(0)


def dist2Cam(knownWidth,focalLength,pixWidth):
    return (knownWidth * focalLength) / pixWidth


cv2.putText(image, "%.2fft" % (inches / 12),(image.shape[1] - 200, image.shape[0] - 20), cv2.FONT_HERSHEY_SIMPLEX,2.0, (0, 255, 0), 3)
