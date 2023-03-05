# plot photo with detected faces using opencv cascade classifier
from cv2 import imread,imwrite
from cv2 import imshow
from cv2 import waitKey
from cv2 import destroyAllWindows
from cv2 import CascadeClassifier
from cv2 import rectangle
from flask import jsonify

def preprocessor(img):
    # load the photograph
    # firstly we are checking if there is a person in the image
    pixels = imread(img)
    # load the pre-trained model
    classifier = CascadeClassifier('C:/Users/DELL/Desktop/COC/flask_api/haarcascade_frontalface_default.xml')
    # perform face detection
    bboxes = classifier.detectMultiScale(pixels)
    # print bounding box for each detected face
    # print(1)
    if len(bboxes)>1:
        return {'err':'Too many people'}
    if len(bboxes)==0:
        return {'err':'No person found in the image'}
    for box in bboxes:
        # extract
        x, y, width, height = box
        x2, y2 = x + width, y + height
        # draw a rectangle over the pixels
        rectangle(pixels, (x, y), (x2, y2), (0,0,255), 1)
        
    # show the image
    # imwrite("object-detection.jpg", image)
    # imshow('face detection', pixels)
    # # keep the window open until we press a key
    # waitKey(0)
    # # close the window
    # destroyAllWindows()
    return {'msg':'success'}

# out = preprocessor()
# print(out)