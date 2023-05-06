import cv2
import pytest
import cvzone
from cvzone.ClassificationModule import Classifier
from cvzone.HandTrackingModule import HandDetector

@pytest.fixture(scope="module")
def classifier():
    model_path = "Model/keras_model.h5"
    classifier = cvzone.ClassificationModule.Classifier(model_path)
    return classifier


def test_classifier_a(classifier):
    image = cv2.imread("test_images/A.jpg")
    image = cv2.resize(image, (300, 300))
    prediction, index = classifier.getPrediction(image)
    classes = ["A", "B", "C", "D", "E"]
    assert classes[index] == "A"

def test_classifier_b(classifier):
    image = cv2.imread("test_images/B.jpg")
    image = cv2.resize(image, (300, 300))
    prediction, index = classifier.getPrediction(image)
    classes = ["A", "B", "C", "D", "E"]
    assert classes[index] == "B"

def test_classifier_c(classifier):
    image = cv2.imread("test_images/C.jpg")
    image = cv2.resize(image, (300, 300))
    prediction, index = classifier.getPrediction(image)
    classes = ["A", "B", "C", "D", "E"]
    assert classes[index] == "C"

@pytest.fixture(scope="module")
def hand_detector():
    return HandDetector(maxHands=1)


def test_hand_detector(hand_detector):
    image = cv2.imread("test_images/hand.jpg")
    image = cv2.resize(image, (640, 480))
    hands = hand_detector.findHands(image)
    assert len(hands) > 1