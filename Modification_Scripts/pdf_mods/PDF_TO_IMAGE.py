try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import pdf2image
import tqdm
import glob

# If you don't have tesseract executable in your PATH, include the following:
pytesseract.pytesseract.tesseract_cmd = r'C:/Users/jmanc/AppData/Local/Programs/Tesseract-OCR/tesseract.exe'

# C:\Users\jmanc\Documents\Jerome Dokus\HTW Studium\Semester 5_HTW\Unternehmenssoftware\Invoice_DATA\Invoices_Amazon
pdfs = glob.glob('C:/Users/jmanc/Documents/Jerome Dokus/HTW Studium/Semester 5_HTW/Unternehmenssoftware/Invoice_DATA/Invoices_Kaspersky/*.pdf')

# save images in list
for x, pdf in enumerate(tqdm.tqdm(pdfs)):
    pdf_to_image = pdf2image.convert_from_path(pdf, 400)
    pdf_to_image[0].save(f'C:/Users/jmanc/Documents/Jerome Dokus/HTW Studium/Semester 5_HTW/Unternehmenssoftware/Invoice_DATA/Invoices_Kaspersky/images/kaspersky{x}.png')

