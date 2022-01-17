import pytesseract
import cv2
import glob
import numpy as np
import tqdm
import pandas

# Tutorial: https://www.youtube.com/watch?v=9FCw1xo_s0I&list=PL2VXyKi-KpYuTAZz__9KVl1jQz74bDG7i&index=7

# If you don't have tesseract executable in your PATH, include the following:
pytesseract.pytesseract.tesseract_cmd = r'C:/Users/jmanc/AppData/Local/Programs/Tesseract-OCR/tesseract.exe'


image_source = 'C:/Users/jmanc/Documents/Jerome Dokus/HTW Studium/Semester 5_HTW/Unternehmenssoftware/Invoice_DATA/Invoices_Xing/images/*.png'

csv_output_location = 'C:/Users/jmanc/PycharmProjects/InvoiceReaderProject/DATA_EXTRACTION_MODEL/XING_Test/'

csv_output_filename = 'XingDataOutput.csv'


# images = glob.glob('C:/Users/jmanc/Documents/Jerome Dokus/HTW Studium/Semester 5_HTW/Unternehmenssoftware/Invoice_DATA/Invoices_Amazon/images/*.png')
# images = glob.glob('C:/Users/jmanc/Documents/Jerome Dokus/HTW Studium/Semester 5_HTW/Unternehmenssoftware/Invoice_DATA/Invoices_Pro-clipper/images/*.png')
# images = glob.glob('C:/Users/jmanc/Documents/Jerome Dokus/HTW Studium/Semester 5_HTW/Unternehmenssoftware/Invoice_DATA/Invoices_Apple/images/*.png')

images = glob.glob(image_source)

df = pandas.DataFrame(columns=['Person', 'Street', 'PostalCode_City', 'Country'])

error_list = list()

# save images in list
for rechnum, img in enumerate(tqdm.tqdm(images)):

    imgx = cv2.imread(img)
    gray = cv2.imread(img, cv2.IMREAD_GRAYSCALE)
    blur = cv2.GaussianBlur(gray, (7, 7), 0)
    thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    kernal = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 13))
    # changing iterations helps with identifying stuctures (compare 1 and 10)
    dilate = cv2.dilate(thresh, kernal, iterations=5)
    cnts = cv2.findContours(dilate, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]
    cnts = sorted(cnts, key=lambda x: cv2.boundingRect(x)[0])

    box = cnts[7]
    x, y, w, h, = cv2.boundingRect(box)
    roi = imgx[y:y + h, x:x + w]

    ocr_string = pytesseract.image_to_string(roi)
    ocr_string = ocr_string.strip('\x0c')
    ocr_string_list = ocr_string.split('\n')

    # filter out blanks
    for item in ocr_string_list:
        if item == '':
            ocr_string_list.remove(item)

    print(ocr_string_list)

    try:

        data = {
            'Person': ocr_string_list[0],
            'Street': ocr_string_list[1],
            'PostalCode_City': ocr_string_list[2],
            'Country': ocr_string_list[3]
        }

        df = df.append(data, ignore_index=True)

    except IndexError:
        error_list.append(img)

    # if rechnum == 10:
    #     break

    # !!! Box count start = 0 !!!
    # Amazon: Person Info = Box 7, Logo/Organization = Box 1 {iterations = 10}
    # Apple: Person Info = Box 7, Logo = Box 1 {iterations = 9}
    # Pro-clipper: Person Info = Box 2, Logo = Box b {iterations = 13}
    # Xing: Person Info = Box 5, Logo = Box 8 {iterations = 13}

df.to_csv(csv_output_location + csv_output_filename, sep=';', encoding='utf-8')

print(len(error_list))
