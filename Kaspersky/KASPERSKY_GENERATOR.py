from __future__ import print_function
from mailmerge import MailMerge
from docx2pdf import convert
import pandas as pd

data = pd.read_csv('C:/Studium/6. Semester/Unternehmenssoftware/Projektarbeit/Invoice_Kaspersky_data(csv).csv')

for index, row in data.iterrows():

    if index == 3:  # use index == 200 --> if you want to generate 200 invoices
        break

    template = "C:/Studium/6. Semester/Unternehmenssoftware/Projektarbeit/invoice_kaspersky.docx"
    document = MailMerge(template)
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
        InvoiceDate=row['InvoiceDate'],
        OrderNr=row['OrderNr'],
        Ref=row['Ref'],
        Product=row['Product'],
        n=str(row['n']),
        s00=str(row['s00']),
        x=str(row['x']),
        s1=str(row['s1']),
        total=str(row['total']),
    )

    document.write('kaspersky-invoice-output.docx')
    convert(f'kaspersky-invoice-output.docx', f'C:/Studium/6. Semester/Unternehmenssoftware/Projektarbeit/invoices_kaspersky/kaspersky-invoice-output{index}.pdf')