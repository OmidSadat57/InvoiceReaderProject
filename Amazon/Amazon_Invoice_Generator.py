
from __future__ import print_function
from mailmerge import MailMerge
from docx2pdf import convert
import pandas as pd
from decimal import Decimal

data = pd.read_csv('C:/Users/Admin/Desktop/Unternehmenssoftware/Project_InvoiceReader/Amazon_Data_Invoice_Generator/Amazon_Data.csv')

for index, row in data.iterrows():

    if index == 3:  # use index == 200 --> if you want to generate 200 invoices
        break

    template = "C:/Users/Admin/Desktop/Unternehmenssoftware/Project_InvoiceReader/Amazon_Data_Invoice_Generator/invoice_amazon.docx"
    document = MailMerge(template)
    document.merge(
        Name=row['Vorname'].upper(),  # format = upper()
        LastName=row['Name'].upper(),  # format = upper()
        Street=row['Straße'],
        HouseNumber=str(row['Hausnummer']),
        City=row['Ort'],
        PostalCode=str(row['PLZ']),
        Country=row['Land'],
        DeliveryDate=row['Rechnungs_Liefer_Datum'],  # format = DD Month YYYY
        OrderDate=row['Bestell_Datum'],  # format = DD Month YYYY
        OrderNumber=row['Bestell_Nummer'],  # len = 19, char = numbers + '-' , format = xxx-xxxxxxx-xxxxxxx
        InvoiceNumber=row['Rechnungs_Nummer'],  # len = 12, char = numbers + letters, , format = upper(letters)
        Product=row['Produkt'],
        asinID=row['ASIN_ID'],  # len = 10, char = numbers + letters, format = upper(letters)
        n=str(row['n']),  # max len = x
        x=str(round(Decimal(row['Stückpreis ohne Ust']), 2)).replace(".", ","),  # max len = xx,xx
        p=str(round(Decimal(row['Ust. % Satz'] * 100))),  # max len = xx
        y=str(round(Decimal(row['Stückpreis mit Ust']), 2)).replace(".", ","),  # max len = xx,xx
        z=str(round(Decimal(row['ZS Produkt']), 2)).replace(".", ","),  # max len = xx,xx
        a=str(round(Decimal(row['VK ohne Ust']), 2)).replace(".", ","),  # max len = xx,xx
        b=str(round(Decimal(row['VK mit Ust']), 2)).replace(".", ","),  # max len = xx,xx
        c=str(round(Decimal(row['VK Gesamt']), 2)).replace(".", ","),  # max len = xx,xx
        Prc=str(round(Decimal(row['ZS Produkt']), 2)).replace(".", ","),  # max len = xxx,xx
        s0=str(round(Decimal(row['Zs ohne Ust']), 2)).replace(".", ","),  # max len = xxx,xx
        s1=str(round(Decimal(row['Gesamt Ust. Betrag']), 2)).replace(".", ",")  # max len = x,xx
    )

    document.write('Amazon-invoice-output.docx')
    convert(f'Amazon-invoice-output.docx', f'C:/Users/Admin/Desktop/Invoices_Amazon/Amazon-invoice-output{index}.pdf')
