from future import print_function
from datetime import date
from mailmerge import MailMerge
# from datetime import date
from docx2pdf import convert
import pandas as pd

data4 = pd.read_csv('C:/Users/Admin/Desktop/Unternehmenssoftware/DataSetBereinigung_Projekt/alte_Unterlagen/Adresses_adapted.csv')

for index, row in data4.iterrows():
    template = "C:/Users/Admin/Desktop/Unternehmenssoftware/DataSetBereinigung_Projekt/alte_Unterlagen/invoice.docx"
    document = MailMerge(template)
    document.merge(
        Name=row['Vorname'],
        LastName=row['Name'],
        Street=row['Straße'],
        HouseNumber=str(row['Hausnummer']),
        City=row['Ort'],
        PostalCode=str(row['PLZ']),
        Country=row['Land'],
        DeliveryDate='21 September 2021',
        InvoiceNumber='DE2MQ619AEUI',
        Prc='999,00'
    )

    document.write('invoice-output.docx')
    convert(f'invoice-output.docx', f'C:/Users/Admin/Desktop/Invoices/output{index}.pdf')