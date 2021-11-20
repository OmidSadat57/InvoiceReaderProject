from __future__ import print_function

from datetime import date

from mailmerge import MailMerge
# from datetime import date
from docx2pdf import convert

template = "invoice.docx"

document = MailMerge(template)
print(document.get_merge_fields())

document.merge(
    NameBig='DARTH',
    LastNameBig='VADER',
    Name2='DARTH',
    LastName2='VADER',
    Street='Throne-Room',
    HouseNumber='1',
    City='Deathstar',
    PostalCode='000066',
    Country='Galactic Empire',
    DeliveryDate='21 September 2021',
    InvoiceNumber='DE2MQ619AEUI',
    Prc='999,00')

document.write('invoice-output.docx')

convert('invoice-output.docx', f'C:/Users/jmanc/PycharmProjects/PythonTestZone/output.pdf')