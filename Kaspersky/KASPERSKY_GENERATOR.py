from __future__ import print_function
from mailmerge import MailMerge
from docx2pdf import convert
import pandas as pd
from decimal import Decimal
from datetime import datetime

excel_data = pd.read_excel('C:/Studium/6. Semester/Unternehmenssoftware/repo/InvoiceReaderProject/Kaspersky/Invoice_Kaspersky_data.xlsx')

excel_data.to_csv('C:/Studium/6. Semester/Unternehmenssoftware/repo/InvoiceReaderProject/Kaspersky/Invoice_Kaspersky_data_csv.csv', index=False)


for index, row in excel_data.iterrows():

    if index == 3:  # use index == 200 --> if you want to generate 200 invoices
        break

    template = "C:/Studium/6. Semester/Unternehmenssoftware/repo/InvoiceReaderProject/Kaspersky/invoice_kaspersky.docx"
    document = MailMerge(template)
    
    d = datetime.date(row['InvoiceDate'])
    
    document.merge(
        Name=row['Name'].upper(),  # format = upper()
        Lastname=row['Lastname'].upper(),  # format = upper()
        Street=row['Street'],
        HouseNumber=str(row['HouseNumber']),
        PostalCode=str(row['PostalCode']),
        City=row['City'],
        Country=row['Country'],
        email=row['email'],
        InvoiceID=row['InvoiceID'],
        InvoiceDate=str(d),
        OrderNr=row['OrderNr'],
        Ref=row['Ref'],
        Product=row['Product'],
        n=str(row['n']),
        s00=str(round(Decimal(row['s00']), 2)).replace('.',','),
        x=str(round(Decimal(row['x']), 2)).replace('.',','),
        s1=str(round(Decimal(row['s1']), 2)).replace('.',','),
        total=str(round(Decimal(row['total']), 2)).replace('.',','),
    )

    document.write('kaspersky-invoice-output.docx')
    convert(f'kaspersky-invoice-output.docx', f'C:/Studium/6. Semester/Unternehmenssoftware/Projektarbeit/invoices_kas/kaspersky-invoice-output{index}.pdf')