
from __future__ import print_function
from mailmerge import MailMerge
from docx2pdf import convert
import pandas as pd
from decimal import Decimal

data = pd.read_csv('C:/Users/Admin/Desktop/Unternehmenssoftware/Project_InvoiceReader/PRO-Clipper_Data_Invoice_Generator/Pro-clipper_Data.csv')

for index, row in data.iterrows():
    if index == 3:  # use index == 200 --> if you want to generate 200 invoices
        break

    template = 'C:/Users/Admin/Desktop/Unternehmenssoftware/Project_InvoiceReader/PRO-Clipper_Data_Invoice_Generator/PRO-Clipper_Template.docx'
    document = MailMerge(template)
    document.merge(
        Name=row['Vorname'],
        LastName=row['Name'],
        Street=row['Straße'],
        HouseNumber=str(row['Hausnummer']),  # format = xx ; max possible = xxx
        ZIPCode=str(row['PLZ']),  # postal code format = xxxxx
        City=row['Ort'],
        Country=row['Land'],
        InvDate=row['Rechnungs_Liefer_Datum'],  # as string, format = DD.MM.YYYY
        OrderDate=row['Auftrags_Datum'],  # format = as string, format = DD.MM.YYYY
        InvNum=row.Rechnungs_Nummer,  # as string format = GERXXXXXX --> char + number; max 6 numbers
        OrderNum=row.Auftrags_Nummer,  # as string format = XXXXXXXXP --> number + char; max 8 numbers
        PayMtd=row.Zahlungsart,  # as string like ['Bar', 'Rechnung', 'Vorkasse', 'PayPal']
        ShipngMtd=row.Versandart,  # as string like ['Lieferung', 'Selbstabholer'], lieferung = standard delivery at 3.99 €
        ArticleNumber=row['Artikel-Nr'],  # as string or string combined with differing dashes and numbers
        ProductName=row['Produkt-Name'],
        ProductDescription=row['Produkt-Beschreibung'],
        n=str(row.Menge),  # as integer format = x; only for testing as always
        NB=str(round(Decimal(row['Einzelpreis ohne Ust']), 2)).replace(".", ","),  # as float formt = max --> xxxx,xx
        NW=str(round(Decimal(row['Warenwert netto']), 2)).replace(".", ","),  # # format = xxx,xx
        VK=str(round(Decimal(row['Versandkosten netto']), 2)).replace(".", ","),  # max len = x,xx
        Ust=str(round(Decimal(row['Gesamt Ust']), 2)).replace(".", ","),  # # format = xxx,xx
        BB=str(round(Decimal(row['Gesamtbetrag']), 2)).replace(".", ","),  # # format = xxx,xx
    )

    document.write('Pro-clipper-Invoice-output.docx')
    convert(f'Pro-clipper-Invoice-output.docx', f'C:/Users/Admin/Desktop/Invoices_Pro-clipper/Pro-clipper-{row.Rechnungs_Nummer}.pdf')
