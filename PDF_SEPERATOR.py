try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import pdf2image

# If you don't have tesseract executable in your PATH, include the following:
pytesseract.pytesseract.tesseract_cmd = r'C:/Users/jmanc/AppData/Local/Programs/Tesseract-OCR/tesseract.exe'

print('Start conversion')
pdf = pdf2image.convert_from_path('pdfs/2020-12-22-muster-der-vordrucke-im-umsatzsteuer-voranmeldungs-und-vorauszahlungsverfahren-fuer-das-kalenderjahr-2021.pdf', 350)
print('conversion finished')

# img = 'test.PNG'

# Simple image to string

# print(pytesseract.image_to_string(pdf[0]))

size = len(pdf)

for number, page in enumerate(pdf, start=1015):
    page.save(f'image/page{number}.png')
    print(f'Complete: {number} / {size + 1014}')  # 1025 ins Gesamt 22-11-2021

# print(pytesseract.image_to_string(img))
