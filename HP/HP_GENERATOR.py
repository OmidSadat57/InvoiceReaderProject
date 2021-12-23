from __future__ import print_function
from mailmerge import MailMerge
from docx2pdf import convert
import pandas as pd

data = pd.read_csv('C:/Studium/6. Semester/Unternehmenssoftware/Projektarbeit/Invoice_HP_data(csv).csv')

for index, row in data.iterrows():

    if index == 3:  # use index == 200 --> if you want to generate 200 invoices
        break

    template = "C:/Studium/6. Semester/Unternehmenssoftware/Projektarbeit/Invoice_HP_data(csv)invoice_hp.docx"
    document = MailMerge(template)
    document.merge(
        Name=row['Name'].upper(),  # format = upper()
        Lastname=row['Lastname'].upper(),  # format = upper()
        Street=row['Street'],
        HouseNumber=str(row['HouseNumber']),
        PostalCode=str(row['PostalCode']),
        City=row['City'],
        Country=row['Country'],
        HPOrderNumber=row['HPOrderNumber'],
        CustomerOrderNumber=row['CustomerOrderNumber'],
        CustomerOrderDate=row['CustomerOrderDate'],
        CustomerNumber=str(row['CustomerNumber']),
        HPUSTID=row['HPUSTID'],
        n=str(row['n']),
        PNr=row['PNr'],
        Product=row['Produkt'],
        LSNr=row['LSNr'],
        DeliveryDate=row['DeliveryDate'],  # format = DD Month YYYY
        PackID=row['PackID'],
        SerialNr=['SerialNr'],
        x=str(row['x']),
        s00=str(row['s00']),
        a=str(row['a']),
        s0=str(row['s0']),
        s1=str(row['s1']),
        total=str(row['total']),
        InvoiceNumber=str(row['InvoiceNumber'])
    )

    document.write('hp-invoice-output.docx')
    convert(f'hp-invoice-output.docx', f'C:/Studium/6. Semester/Unternehmenssoftware/Projektarbeit/invoices_hp/hp-invoice-output{index}.pdf')