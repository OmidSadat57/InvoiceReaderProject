from __future__ import print_function
from mailmerge import MailMerge
import pandas
# from datetime import date
from docx2pdf import convert

template = "invoice_apple.docx"
df = pandas.read_csv('Apple/Adressen_Apple.csv', ';', dtype={'KundenNr': str})
p_df = pandas.read_csv('Product_Data/product_computers.csv', ';')

# print(document.get_merge_fields())

for index, row in df.iterrows():

    if index >= 192:
        break

    try:

        document = MailMerge(template)

        document.merge(
            Nme=row['Vorname'],  # format = Jerome
            LstNme=row['Name'],  # format = Cook
            Street=row['Straße'][:9],
            HsNr=str(row['Hausnummer']),
            City=row['Ort'],
            PCode=str(row['PLZ']),
            Country='Germany',  # format = upper()
            DeliveryDate=row['Bestelldatum'],  # format = dd.mm.yyyy
            DueDate=row['Lieferdatum'],  # format = dd.mm.yyyy
            InvNum='DE12ABII34',  # len = 10, char = numbers + letters, , format = LLxxxxxxxx
            ApOrNr='0123456789',  # len = 10, char = numbers
            OrdDate=row['Bestelldatum'],  # format = dd.mm.yyyy
            CNr=str(row['KundenNr']),  # len = 6, char = numbers
            OrdNum='ABCD123456',  # len = 10, char = numbers + letter , format = Lxxxxxxxxx
            DelivNum='0123456789',  # len = 10, char = numbers
            ProdNum='123456',  # len = 6, char = numbers
            MatNum='LLLXXLL/L',  # len = 9, char = numbers + letters, format = LLLxxLL/L
            Product=p_df.iloc[index, 0][:33],  # items from Apple product list, strings sliced at len 33
            Prc=str(row['Betrag']).replace(' €', ''),  # max len = xxx,xx
            n=str(row['n']),  # max len = xx
            x=str(row['Stückpreis ohne Ust']),  # max len = xx,xx
            p=str(row['Ust. % Satz']),  # max len = xx
            y=str(row['Stückpreis mit Ust']),  # max len = xx,xx
            z=str(row['ZS Produkt']),  # max len = xx,xx
            s0=str(row['Zs ohne Ust']),  # max len = xxx,xx
            s1=str(row['Gesamt Ust. Betrag']))  # max len = x,xx

        document.write(f'testing/docx/amazon-output{index + 1}.docx')

        convert(f'testing/docx/amazon-output{index + 1}.docx', f'C:/Users/jmanc/PycharmProjects/InvoiceReaderProject/testing/amazon{index + 1}.pdf')

    except:
        pass
