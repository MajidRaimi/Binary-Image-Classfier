import tensorflow as tf
from tensorflow.keras.models import load_model
import numpy as np
import cv2

happy_sad_model = load_model('models/happy_sad_model.h5')

labels = ['Happy' , 'Sad']


def predictHappyOrSad(imagePath):
    image = cv2.imread(imagePath)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    resizedImage = tf.image.resize(image, (256, 256))
    yhat = happy_sad_model.predict(np.expand_dims(resizedImage/255, 0))

    return labels[round(yhat[0][0])]


