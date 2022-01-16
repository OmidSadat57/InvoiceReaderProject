import cv2
import glob
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import tqdm

try:
    from PIL import Image
except ImportError:
    import Image

# image = mpimg.imread('C:/Users/jmanc/PycharmProjects/InvoiceReaderProject/Apple/Data/img/apple1.png')

image_list = []

img_size = 250

images = glob.glob('/InvoiceType/Apple/Data/img/*.png')

# save images in list
for img in tqdm.tqdm(images):
    # read image and convert to grayscale
    imgx = cv2.imread(img, cv2.IMREAD_GRAYSCALE)
    # resize image
    imgx = cv2.resize(imgx, (img_size, img_size))
    # imgx / 255
    imgx = imgx / 255

    image_list.append(imgx)

# convert list to numpy array
apple_data = np.array(image_list)

# print(np.array(image_list[1]).shape)

