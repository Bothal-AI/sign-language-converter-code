import cv2
import pytest
import cvzone
from cvzone.ClassificationModule import Classifier
from cvzone.HandTrackingModule import HandDetector


# Test alphabets
@pytest.fixture(scope="module")
def classifier():
    model_path = "Model/keras_model.h5"
    classifier = cvzone.ClassificationModule.Classifier(model_path)
    return classifier

def test_classifier_a(classifier):
    image = cv2.imread("test_images/A.jpg")
    image = cv2.resize(image, (300, 300))
    prediction, index = classifier.getPrediction(image)
    classes = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
              "V", "W", "X", "Y"]
    assert isinstance(classes[index],(str)) == True

def test_classifier_b(classifier):
    image = cv2.imread("test_images/B.jpg")
    image = cv2.resize(image, (300, 300))
    prediction, index = classifier.getPrediction(image)
    classes = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
              "V", "W", "X", "Y"]
    assert isinstance(classes[index],(str)) == True

def test_classifier_c(classifier):
    image = cv2.imread("test_images/C.jpg")
    image = cv2.resize(image, (300, 300))
    prediction, index = classifier.getPrediction(image)
    classes = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
              "V", "W", "X", "Y"]
    assert isinstance(classes[index],(str)) == True


# Test numbers
@pytest.fixture(scope="module")
def classifierNums():
    model_path = "NumbersModel/keras_model.h5"
    classifierNums = cvzone.ClassificationModule.Classifier(model_path)
    return classifierNums

def test_classifier_3(classifierNums):
    image = cv2.imread("test_images/3.jpg")
    image = cv2.resize(image, (300, 300))
    prediction, index = classifierNums.getPrediction(image)
    classes = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert isinstance(classes[index],(int)) == True

def test_classifier_4(classifierNums):
    image = cv2.imread("test_images/4.jpg")
    image = cv2.resize(image, (300, 300))
    prediction, index = classifierNums.getPrediction(image)
    classes = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert isinstance(classes[index],(int)) == True

def test_classifier_5(classifierNums):
    image = cv2.imread("test_images/5.jpg")
    image = cv2.resize(image, (300, 300))
    prediction, index = classifierNums.getPrediction(image)
    classes = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert isinstance(classes[index],(int)) == True


@pytest.fixture(scope="module")
def hand_detector():
    return HandDetector(maxHands=1)


def test_hand_detector(hand_detector):
    image = cv2.imread("test_images/hand.jpg")
    image = cv2.resize(image, (640, 480))
    hands = hand_detector.findHands(image)
    assert len(hands) > 1