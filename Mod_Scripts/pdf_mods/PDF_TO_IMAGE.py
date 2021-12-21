try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import pdf2image

# If you don't have tesseract executable in your PATH, include the following:
pytesseract.pytesseract.tesseract_cmd = r'C:/Users/jmanc/AppData/Local/Programs/Tesseract-OCR/tesseract.exe'

print('Start')

size = 192

for x in range(1, 193):
    pdf_to_image = pdf2image.convert_from_path(f'Apple/Data/amazon{str(x)}.pdf', 400)
    pdf_to_image[0].save(f'Apple/Data/img/apple{x}.png')
    print(f'Complete: {x} / {size}')

print('done')
