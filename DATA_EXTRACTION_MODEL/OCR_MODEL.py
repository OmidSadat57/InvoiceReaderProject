import pytesseract
import cv2
import glob
import numpy as np
import tqdm

# Tutorial: https://www.youtube.com/watch?v=9FCw1xo_s0I&list=PL2VXyKi-KpYuTAZz__9KVl1jQz74bDG7i&index=7

# If you don't have tesseract executable in your PATH, include the following:
pytesseract.pytesseract.tesseract_cmd = r'C:/Users/jmanc/AppData/Local/Programs/Tesseract-OCR/tesseract.exe'


image_source = 'C:/Users/jmanc/Documents/Jerome Dokus/HTW Studium/Semester 5_HTW/Unternehmenssoftware/Invoice_DATA/Invoices_Kaspersky/images/*.png'

box_output_location = f'C:/Users/jmanc/PycharmProjects/InvoiceReaderProject/DATA_EXTRACTION_MODEL/Kaspersky_Test/Boxes/'

image_output_location = f'C:/Users/jmanc/PycharmProjects/InvoiceReaderProject/DATA_EXTRACTION_MODEL/Kaspersky_Test/Output/'

images = glob.glob(image_source)


for rechnum, img in enumerate(tqdm.tqdm(images)):

    # image processing
    imgx = cv2.imread(img)
    gray = cv2.imread(img, cv2.IMREAD_GRAYSCALE)
    blur = cv2.GaussianBlur(gray, (7, 7), 0)
    thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    kernal = cv2.getStructuringElement(cv2.MORPH_RECT, (12, 12))
    # changing iterations helps with identifying stuctures (compare 1 and 10)
    dilate = cv2.dilate(thresh, kernal, iterations=9)
    cnts = cv2.findContours(dilate, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]
    cnts = sorted(cnts, key=lambda x: cv2.boundingRect(x)[0])

    # box processing
    for boxnum, c in enumerate(cnts):
        x, y, w, h, = cv2.boundingRect(c)
        roi = imgx[y:y + h, x:x + w]
        # Folders 0, 1, 2,...10 required in output location
        cv2.imwrite(box_output_location + f'{rechnum}/box{boxnum}.png', roi)
        # if h > 200 and w > 200:
        cv2.rectangle(imgx, (x, y), (x + w, y + h), (36, 255, 12), 2)

    cv2.imwrite(image_output_location + f'testBoxOutput{rechnum}.png', imgx)

    if rechnum >= 10:
        break
