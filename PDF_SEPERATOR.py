try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import pdf2image

# If you don't have tesseract executable in your PATH, include the following:
pytesseract.pytesseract.tesseract_cmd = r'C:/Users/jmanc/AppData/Local/Programs/Tesseract-OCR/tesseract.exe'

print('Start conversion')
pdf = pdf2image.convert_from_path('1. Vorlesung_RN_15.10.2019.pdf', 350)
print('conversion finished')

# img = 'test.PNG'

# Simple image to string

#print(pytesseract.image_to_string(pdf[0]))

for number, page in enumerate(pdf, start=1):
    page.save(f'image/page{number}.png')

# print(pytesseract.image_to_string(img))
