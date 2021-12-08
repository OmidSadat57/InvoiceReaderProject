
from __future__ import print_function
from mailmerge import MailMerge
from docx2pdf import convert
import pandas as pd
from decimal import Decimal

data = pd.read_csv('C:/Users/Admin/Desktop/Unternehmenssoftware/Project_InvoiceReader/Xing_Data_Invoice_Generator/Xing_data.csv')

for index, row in data.iterrows():
    if index == 3:  # use index == 200 --> if you want to generate 200 invoices
        break

    template = "C:/Users/Admin/Desktop/Unternehmenssoftware/Project_InvoiceReader/Xing_Data_Invoice_Generator/XING_PRM_Template.docx"
    document = MailMerge(template)
    document.merge(
        Name=row['Vorname'],
        LastName=row['Name'],
        Street=row['Straße'],
        HouseNumber=str(row['Hausnummer']),  # format = xx ; max possible = xxx
        City=row['Ort'],
        ZIPCode=str(row['PLZ']),  # postal code format = xxxxx
        Country=row['Land'],
        InvoiceDate=row['Rechnungs_Datum'],  # as string, format = DD.MM.YYYY
        InvoiceNum=str(row['Rechnungs_Nummer']),  # len = 15, char = PRM + number , format = PRMxxxxxxxxxxxxx
        CustomerNumber=str(row['Kunden_Nummer']),  # len = 10, char = number , format = xxxxxxxxxx
        Product=row['Produkt'],  # product as string --> value = 'Premium-Mitgliedschaft'
        LBegin=row['Leistungs_Beginn'],  # the same as InvoiceDate, as string format = DD.MM.YYYY
        LEnd=row['Leistungs_Ende'],  # the date of service end, format = DD.MM.YYYY
        NB=str(round(Decimal(row['Preis_ohne_Ust']), 2)).replace(".", ","),  # format max = xx,xx
        p=str(round(Decimal(row['Ust. % Satz'] * 100))),  # format = xx
        UstB=str(round(Decimal(row['Ust']), 2)).replace(".", ","),  # format = x,xx
        BB=str(round(Decimal(row['Preis_mit_Ust']), 2)).replace(".", ","),  # # format = xx,xx
        BB1=str(round(Decimal(row['Preis_mit_Ust']), 2)),  # format = xx,xx
        AbrNum=row['Abrechnungs_Nummer']  ## max len = 19, format = B-xAVxxxxxGGxxxxxxx
    )

    document.write('Xing-Invoice-output.docx')
    convert(f'Xing-Invoice-output.docx', f'C:/Users/Admin/Desktop/Invoices_Xing/Xing_invoice-output{index}.pdf')
