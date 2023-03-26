import cv2
from cvzone.HandTrackingModule import HandDetector
from cvzone.ClassificationModule import Classifier
import numpy as np
import math

videoCapture = cv2.VideoCapture(0)
detect = HandDetector(maxHands=1)
offsetValue = 25
imageSize = 300
counter = 0
classifier = Classifier("Model/keras_model.h5", "Model/labels.txt")
labels = ["A", "B", "C", "D", "E"]

while True:
    success, image = videoCapture.read()
    imageOutput = image.copy()
    hands = detect.findHands(image, draw=False)

    if hands:
        hand = hands[0]
        x, y, w, h = hand['bbox']

        imageWithBackground = np.ones((imageSize, imageSize, 3), np.uint8) * 255
        imageCropped = image[y - offsetValue:y + h + offsetValue, x - offsetValue:x + w + offsetValue]
        imageCroppedShape = imageCropped.shape
        heightOverWidth = (h / w)


        #if statement to keep proportion of images
        if heightOverWidth > 1:
            constant = imageSize / h
            calculatedWidth = math.ceil(constant * w)
            resizedImage = cv2.resize(imageCropped, (calculatedWidth, imageSize))
            resizedImageShape = resizedImage.shape
            widthDiff = math.ceil((300 - calculatedWidth) * 0.5)
            imageWithBackground[:resizedImageShape[0], widthDiff:calculatedWidth+widthDiff] = resizedImage

            #print prediction and index value
            prediction, index = classifier.getPrediction(imageWithBackground)
            print(prediction, index)

        else:
            constant = imageSize / w
            calculatedHeight = math.ceil(constant * h)
            resizedImage = cv2.resize(imageCropped, (imageSize, calculatedHeight))
            resizedImageShape = resizedImage.shape
            heightDiff = math.ceil((imageSize - calculatedHeight) * 0.5)
            imageWithBackground[heightDiff:calculatedHeight + heightDiff, :] = resizedImage
            prediction, index = classifier.getPrediction(imageWithBackground, draw=False)

        #styling output
        cv2.rectangle(imageOutput, (x - offsetValue, y - offsetValue - 50), (x - offsetValue + 90, y - offsetValue), ((0,255,0)), cv2.FILLED)
        cv2.putText(imageOutput, labels[index], (x,y-30), cv2.FONT_HERSHEY_DUPLEX,1.5, (0,0,0), 2)
        cv2.rectangle(imageOutput, (x-offsetValue,y-offsetValue), (x+ w+offsetValue, y + h+offsetValue), ((0,255,0)) , 3)

        cv2.imshow("ImageCrop", imageCropped)
        cv2.imshow("ImageWithBackground", imageWithBackground)


    cv2.imshow("Image", imageOutput)
    cv2.waitKey(1)
