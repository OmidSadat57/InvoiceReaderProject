import cv2
import glob
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import tqdm
# from tensorflow import keras

try:
    from PIL import Image
except ImportError:
    import Image

# image = mpimg.imread('C:/Users/jmanc/PycharmProjects/InvoiceReaderProject/Apple/Data/img/apple1.png')

img_size = 250


training_set = []

training_images = glob.glob('C:/Users/jmanc/PycharmProjects/InvoiceReaderProject/Simulation/training_set/*.png')

label = [0, 1]

# save images in list
for img in tqdm.tqdm(training_images):
    # read image and convert to grayscale
    imgx = cv2.imread(img, cv2.IMREAD_GRAYSCALE)
    # resize image
    imgx = cv2.resize(imgx, (img_size, img_size))
    # imgx / 255
    imgx = imgx / 255

    training_set.append([imgx, label])

print(np.array(training_set).shape)

# _______________________________________________________________________________

# test_set = []
#
# test_images = glob.glob('C:/Users/jmanc/PycharmProjects/InvoiceReaderProject/Simulation/test_set/*.png')
#
# # save images in list
# for img in tqdm.tqdm(test_images):
#     # image name
#     img_name = img.split('\\')[1]
#     # read image and convert to grayscale
#     imgx = cv2.imread(img, cv2.IMREAD_GRAYSCALE)
#     # resize image
#     imgx = cv2.resize(imgx, (img_size, img_size))
#     # imgx / 255
#     imgx = imgx / 255
#
#     test_set.append([np.array(imgx), img_name])
#
# print(np.array(test_set).shape)

# _______________________________________________________________________________

# # Define sequential model
# model = keras.Sequential()
#
# # Define the first layer
# model.add(keras.layers.Dense(16, activation='sigmoid', input_shape=(784,)))
#
# # Add activation function to classifier
# model.add(keras.layers.Dense(4, activation='softmax'))
#
# # Set the optimizer, loss function, and metrics
# model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
#
# # Add the number of epochs and the validation split
# model.fit(sign_language_features, sign_language_labels, epochs=10, validation_split=0.1)