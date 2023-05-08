import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np
import math
import time


videoCapture = cv2.VideoCapture(0)
detect = HandDetector(maxHands=1)
offsetValue = 25
imageSize = 300
counter = 0

#Change path for different letters!
folder = "Data/A"

while True:
    #find and capture hand
    successful, image = videoCapture.read()
    hands, image = detect.findHands(image)

    #crop image to uniform shape
    if hands:
        capturedHand = hands[0]
        x, y, w, h = capturedHand['bbox']

        imageWithBackground = np.ones((imageSize, imageSize, 3), np.uint8) * 255
        imageCropped = image[y - offsetValue:y + h+offsetValue, x-offsetValue:x + w+offsetValue]
        imageCroppedShape = imageCropped.shape
        heightOverWidth = (h/w)

        #if statement to keep proportion of images
        if heightOverWidth > 1:
            constant = imageSize / h
            calculatedWidth = math.ceil(constant * w)
            resizedImage = cv2.resize(imageCropped, (calculatedWidth, imageSize))
            resizedImageShape = resizedImage.shape
            widthDiff = math.ceil((300 - calculatedWidth) * 0.5)
            imageWithBackground[:resizedImageShape[0], widthDiff:calculatedWidth+widthDiff] = resizedImage
        else:
            constant = imageSize / w
            calculatedHeight = math.ceil(constant * h)
            resizedImage = cv2.resize(imageCropped, (imageSize, calculatedHeight))
            resizedImageShape = resizedImage.shape
            heightDiff = math.ceil((imageSize - calculatedHeight) * 0.5)
            imageWithBackground[heightDiff:calculatedHeight + heightDiff, :] = resizedImage

        cv2.imshow("ImageCrop", imageCropped)
        cv2.imshow("ImageWithBackground", imageWithBackground)


    #output
    cv2.imshow("Image", image)
    key = cv2.waitKey(1)

    #saving images
    if key == ord("s"):
        counter = counter + 1
        cv2.imwrite(f'{folder}/Image_{time.time()}.jpg', imageWithBackground)
        print(counter)