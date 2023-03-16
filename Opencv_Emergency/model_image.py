import cv2 as cv2
import time
from torch import *
import torch
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image


def predict_emergency_vehicle(image_path):
    # loading the model
    model = tf.keras.models.load_model('Models/densenet.h5')

    device = "/gpu:0" if tf.config.list_physical_devices('GPU') else "/cpu:0"

    print(device)

    # Load a test image
    img_path = image_path
    print(img_path)
    img = image.load_img(img_path, target_size=(224, 224))

    # Convert the image to a numpy array
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = x / 255.0  # normalize the image

    # #li.append(float(proba)) if idx == 1 else li.append(1 - float(proba))
    # li.append(float(proba)) if idx == 1 else li.append(0)

    # Make a prediction
    with tf.device(device):
        pred = model.predict(x)
    return pred

def emergency_image(east_path,south_path,west_path,north_path):
    imsize = (224, 224)
    frames_to_skip = 10
    li = []
    im_output="./Opencv_Emergency/Test/"

    video_reader_east = cv2.VideoCapture(east_path)
    video_reader_west = cv2.VideoCapture(west_path)
    video_reader_north = cv2.VideoCapture(north_path)
    video_reader_south = cv2.VideoCapture(south_path)
    tick = time.time()
    try:
        while True:
            ret, image = video_reader_east.read()
            image = cv2.resize(image, imsize)
            cv2.imwrite(im_output+'east.png', image)

            ret, image = video_reader_west.read()
            image = cv2.resize(image, imsize)
            cv2.imwrite(im_output+'west.png', image)

            ret, image = video_reader_north.read()
            image = cv2.resize(image, imsize)
            cv2.imwrite(im_output+'north.png', image)

            ret, image = video_reader_south.read()
            image = cv2.resize(image, imsize)
            cv2.imwrite(im_output+'south.png', image)

        for k in range(frames_to_skip):
            video_reader_east.grab()
            video_reader_west.grab()
            video_reader_north.grab()
            video_reader_south.grab()
    except:
        pass
    emp = ["east.png","south.png","west.png","north.png"]
    for path in emp:
        li.append(predict_emergency_vehicle(im_output+path))


    #print('\n\n', 'Time taken: ', time.time() - tick)
    video_reader_east.release()
    video_reader_west.release()
    video_reader_north.release()
    video_reader_south.release()


    return li

