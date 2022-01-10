try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import pdf2image


# If you don't have tesseract executable in your PATH, include the following:
pytesseract.pytesseract.tesseract_cmd = r'C:/Users/jmanc/AppData/Local/Programs/Tesseract-OCR/tesseract.exe'

pdf = pdf2image.convert_from_path('output.pdf', 500)

# img = 'test.PNG'

# Simple image to string

print(pytesseract.image_to_string(pdf[0]))

# print(pytesseract.image_to_string(img))


