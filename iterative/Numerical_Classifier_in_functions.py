import cv2
from cvzone.HandTrackingModule import HandDetector
from cvzone.ClassificationModule import Classifier
import numpy as np
import math


def main():
    classifyNumerical()


def classifyNumerical():
    videoCapture = cv2.VideoCapture(0)
    detect = HandDetector(maxHands=1)
    offsetValue = 25
    imageSize = 300
    classifier = Classifier("NumbersModel/keras_model.h5", "NumbersModel/labels.txt")
    labels = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    while True:
        # To check if ESC key is pressed
        key = cv2.waitKey(1) & 0xFF
        if key == 27:  # If ESC key is pressed
            break  # Exit the loop

        success, image = videoCapture.read()
        imageOutput = image.copy()
        hands = detect.findHands(image, draw=False)

        if hands:
            hand = hands[0]
            x, y, w, h = hand["bbox"]

            imageWithBackground = np.ones((imageSize, imageSize, 3), np.uint8) * 255
            imageCropped = image[
                           y - offsetValue: y + h + offsetValue,
                           x - offsetValue: x + w + offsetValue,
                           ]
            heightOverWidth = h / w  # aspect ratio

            # if statement to keep proportion of images, depending on aspect ratio
            if heightOverWidth > 1:  # if image height is larger than width
                constant = imageSize / h
                calculatedWidth = math.ceil(constant * w)
                resizedImage = cv2.resize(
                    imageCropped, (calculatedWidth, imageSize)
                )  # resize the image
                resizedImageShape = resizedImage.shape
                widthDiff = math.ceil((300 - calculatedWidth) * 0.5)
                imageWithBackground[
                : resizedImageShape[0], widthDiff: calculatedWidth + widthDiff
                ] = resizedImage
                prediction, index = classifier.getPrediction(
                    imageWithBackground
                )  # get prediction and index value

            else:  # if image width is larger than height
                constant = imageSize / w
                calculatedHeight = math.ceil(constant * h)
                resizedImage = cv2.resize(
                    imageCropped, (imageSize, calculatedHeight)
                )  # resize the image
                heightDiff = math.ceil((imageSize - calculatedHeight) * 0.5)
                imageWithBackground[
                heightDiff: calculatedHeight + heightDiff, :
                ] = resizedImage
                prediction, index = classifier.getPrediction(
                    imageWithBackground, draw=False
                )

            # styling output
            cv2.rectangle(
                imageOutput,
                (x - offsetValue, y - offsetValue - 50),
                (x - offsetValue + 90, y - offsetValue),
                ((0, 255, 0)),
                cv2.FILLED,
            )
            cv2.putText(
                imageOutput,
                labels[index],
                (x, y - 30),
                cv2.FONT_HERSHEY_DUPLEX,
                1.5,
                (0, 0, 0),
                2,
            )
            cv2.rectangle(
                imageOutput,
                (x - offsetValue, y - offsetValue),
                (x + w + offsetValue, y + h + offsetValue),
                ((0, 255, 0)),
                3,
            )

        cv2.imshow("Image", imageOutput)
        cv2.waitKey(1)


if __name__ == "__main__":
    main()