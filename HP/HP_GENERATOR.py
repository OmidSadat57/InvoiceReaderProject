from __future__ import print_function
from mailmerge import MailMerge
from docx2pdf import convert
import pandas as pd
from datetime import datetime
from decimal import Decimal


excel_data = pd.read_excel('C:/Studium/6. Semester/Unternehmenssoftware/repo/InvoiceReaderProject/HP/Invoice_HP_data.xlsx')

excel_data.to_csv('C:/Studium/6. Semester/Unternehmenssoftware/repo/InvoiceReaderProject/HP/Invoice_HP_data_csv.csv', index=False)

for index, row in excel_data.iterrows():

    if index == 200:  # use index == 200 --> if you want to generate 200 invoices
        break

    template = "C:/Studium/6. Semester/Unternehmenssoftware/repo/InvoiceReaderProject/HP/invoice_hp.docx"
    document = MailMerge(template)
    
    orderdate = datetime.date(row['CustomerOrderDate'])
    deliverydate = datetime.date(row['DeliveryDate'])

    document.merge(
        Name=row['Name'],  # format = upper()
        Lastname=row['Lastname'],  # format = upper()
        Street=row['Street'],
        HouseNumber=str(row['HouseNumber']),
        PostalCode=str(row['PostalCode']),
        City=row['City'],
        Country=row['Country'],
        HPOrderNumber=row['HPOrderNumber'],
        CustomerOrderNumber=row['CustomerOrderNumber'],
        CustomerOrderDate=str(orderdate),
        CustomerNumber=str(row['CustomerNumber']),
        HPUSTID=row['HPUSTID'],
        n=str(row['n']),
        PNr=row['PNr'],
        Product=row['Produkt'],
        LSNr=str(row['LSNr']),
        DeliveryDate=str(deliverydate),  
        PackID=row['PackID'],
        SerialNr=['SerialNr'],
        x=str(round(Decimal(row['x']), 2)).replace('.',','),
        s00=str(round(Decimal(row['s00']), 2)).replace('.',','),
        a=str(round(Decimal(row['a']), 2)).replace('.',','),
        s0=str(round(Decimal(row['s0']), 2)).replace('.',','),
        s1=str(round(Decimal(row['s1']), 2)).replace('.',','),
        total=str(round(Decimal(row['total']), 2)).replace('.',','),
        InvoiceNumber=str(row['InvoiceNumber'])
    )

    document.write('hp-invoice-output.docx')
    convert(f'hp-invoice-output.docx', f'C:/Studium/6. Semester/Unternehmenssoftware/Projektarbeit/invoices_hp/hp-invoice-output{index}.pdf')