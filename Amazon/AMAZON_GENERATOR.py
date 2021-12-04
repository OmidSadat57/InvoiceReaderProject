
from __future__ import print_function
from mailmerge import MailMerge
from docx2pdf import convert
import pandas as pd
from decimal import Decimal

data = pd.read_csv('C:/Users/Admin/Desktop/Unternehmenssoftware/DataSetBereinigung_Projekt/Test1/Adresses_edited.csv')

for index, row in data.iterrows():

    template = "C:/Users/Admin/Desktop/Unternehmenssoftware/DataSetBereinigung_Projekt/Test1/invoice_amazon.docx"
    document = MailMerge(template)
    # replace dots with commas
    stueckpreis_ohne_ust = str(round(Decimal(row['Stückpreis ohne Ust']), 2))
    stueckpreis_ohne_ust = stueckpreis_ohne_ust.replace(".", ",")
    stueckpreis_mit_ust = str(round(Decimal(row['Stückpreis mit Ust']), 2))
    stueckpreis_mit_ust = stueckpreis_mit_ust.replace(".", ",")
    zs_produkt = str(round(Decimal(row['ZS Produkt']), 2))
    zs_produkt =zs_produkt.replace(".", ",")
    vk_ohne_ust = str(round(Decimal(row['VK ohne Ust']), 2))
    vk_ohne_ust = vk_ohne_ust.replace(".", ",")
    vk_mit_ust = str(round(Decimal(row['VK mit Ust']), 2))
    vk_mit_ust = vk_mit_ust.replace(".", ",")
    vk_gesamt = str(round(Decimal(row['VK Gesamt']), 2))
    vk_gesamt = vk_gesamt.replace(".", ",")
    price = str(round(Decimal(row['ZS Produkt']), 2))
    price = price.replace(".", ",")
    zs_ohne_ust = str(round(Decimal(row['Zs ohne Ust']), 2))
    zs_ohne_ust = zs_ohne_ust.replace(".", ",")
    gesamt_ust_betrag = str(round(Decimal(row['Gesamt Ust. Betrag']), 2))
    gesamt_ust_betrag = gesamt_ust_betrag.replace(".", ",")

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
        x=stueckpreis_ohne_ust,  # max len = xx,xx
        p=str(round(Decimal(row['Ust. % Satz'] * 100))),  # max len = xx
        y=stueckpreis_mit_ust,  # max len = xx,xx
        z=zs_produkt,  # max len = xx,xx
        a=vk_ohne_ust,  # max len = xx,xx
        b=vk_mit_ust,  # max len = xx,xx
        c=vk_gesamt,  # max len = xx,xx
        Prc=price,  # max len = xxx,xx
        s0=zs_ohne_ust,  # max len = xxx,xx
        s1=gesamt_ust_betrag  # max len = x,xx
    )

    document.write('invoice-output_new.docx')
    convert(f'invoice-output_new.docx', f'C:/Users/Admin/Desktop/Invoices_test1/output_new{index}.pdf')
