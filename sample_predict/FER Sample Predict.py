# creates user_test folder
user_test_path = os.path.join(BASE_DIR, 'user_test')
if not(os.path.exists(os.path.join(BASE_DIR, 'user_test'))):
    os.mkdir(user_test_path)
    print('Directory created.')

print('Please upload your picture')
if os.path.isfile(os.path.join(user_test_path, 'pic.jpg')):
    print('You have succesfully uploaded a picture!')

# load json and create model
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.models import model_from_json
import numpy
import os
import numpy as np
import cv2

# loading the model
json_file = open(model_file_json, 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
# load weights into new model
loaded_model.load_weights(model_file_h5)
print("Loaded model from disk")

# setting image resizing parameters
WIDTH = 48
HEIGHT = 48
x=None
y=None
labels = ['Angry', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral']

img_file_name = 'angry_face11.jpg'
# loading image
full_size_image = cv2.imread(os.path.join(BASE_DIR, 'user_test', img_file_name))
print("Image Loaded")
gray=cv2.cvtColor(full_size_image,cv2.COLOR_RGB2GRAY)
face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
faces = face.detectMultiScale(gray, 1.3, 5)