import pytesseract
import cv2
import glob
import numpy as np
import tqdm

# Tutorial: https://www.youtube.com/watch?v=9FCw1xo_s0I&list=PL2VXyKi-KpYuTAZz__9KVl1jQz74bDG7i&index=7

# If you don't have tesseract executable in your PATH, include the following:
pytesseract.pytesseract.tesseract_cmd = r'C:/Users/jmanc/AppData/Local/Programs/Tesseract-OCR/tesseract.exe'

image_list = []

# img_size = 250

images = glob.glob(
    'C:/Users/jmanc/Documents/Jerome Dokus/HTW Studium/Semester 5_HTW/Unternehmenssoftware/Invoice_DATA/Invoices_Amazon/amazon0.png')

# save images in list
for img in tqdm.tqdm(images):

    imgx = cv2.imread(img)
    gray = cv2.imread(img, cv2.IMREAD_GRAYSCALE)
    blur = cv2.GaussianBlur(gray, (7, 7), 0)
    thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    kernal = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 13))
    # changing iterations helps with identifying stuctures (compare 1 and 10)
    dilate = cv2.dilate(thresh, kernal, iterations=10)
    cnts = cv2.findContours(dilate, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]
    cnts = sorted(cnts, key=lambda x: cv2.boundingRect(x)[0])

    for c in cnts:
        x, y, w, h, = cv2.boundingRect(c)
        # if h > 200 and w > 200:
        cv2.rectangle(imgx, (x, y), (x + w, y + h), (36, 255, 12), 2)

    cv2.imwrite('testBoxOutput2.png', imgx)

    # imgx = pytesseract.image_to_data(imgx[0])
    # print(imgx)

    # image_list.append(imgx)