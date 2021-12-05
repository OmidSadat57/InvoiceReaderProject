
from __future__ import print_function
from mailmerge import MailMerge
from docx2pdf import convert
import pandas as pd
from decimal import Decimal

data = pd.read_csv('C:/Users/Admin/Desktop/Unternehmenssoftware/DataSetBereinigung_Projekt/Test1/Test_data.csv')

for index, row in data.iterrows():

    template = "C:/Users/Admin/Desktop/Unternehmenssoftware/DataSetBereinigung_Projekt/Test1/invoice_amazon.docx"
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
        OrderNumber='123-1234567-1234567',  # len = 19, char = numbers + '-' , format = xxx-xxxxxxx-xxxxxxx
        InvoiceNumber='DE2MQ619AEUI',  # len = 12, char = numbers + letters, , format = upper(letters)
        Product='Super Laser - COLOR : Green, full power, destroy planets',
        asinID='if392jf893',  # len = 10, char = numbers + letters, format = upper(letters)
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

    document.write('invoice-output_new.docx')
    convert(f'invoice-output_new.docx', f'C:/Users/Admin/Desktop/Invoices_test1/output_new{index}.pdf')
