from __future__ import print_function

from datetime import date

from mailmerge import MailMerge
from docx2pdf import convert

template = "invoice_hp.docx"

document = MailMerge(template)
print(document.get_merge_fields())

document.merge(
    Name='DARTH',  # format = Jerome
    Lastname='VADER',  # format = Cook
    Street='Throne',
    HouseNumber='1',
    City='Deathstar',
    PostalCode='000066',
    Country='Galactic Empire',  # format = upper()
    HPOrderNumber='56G123456789' # format 00a000000000
    CustomerOrderNumber='ABCD1234567' # format aaa0000000
    DeliveryDate='04.05.2021',  # format = dd.mm.yyyy
    CustomerOrderDate='04.05.2021',  # format = dd.mm.yyyy
    CustomerNumber='123456789' #format 000000000   
    InvoiceNumber='1234567',  # len = 7, format = 0000000
    InvoiceDate='20.05.2021',  # date
    HPUSTID='DE1123456789',  # format = DE000000000
    Pnr='123A4BC',  # format = 000a0aa, Produktnummer
    Product='HP Envy',  # Produktname
    LSNr='111222333',  # len = p, char = numbers, Lieferscheinnummer
    PackID='ABC1DE2F34',  
    SerialNr='ABC12345D6',  # char = numbers + letters, format = aaa00000a0
    Prc='999,00',  # max len = xxx,xx
    n='1',  # max len = xx
    x='499,99',  # max len = xxx,xx
    s00='499,99',  # max len = xxx, Zwischensumme ohne Steuer ohne Versandkosten
    a='0',  # max len = xx,xx
    s0='499,99',  # max len = xxx,xx
    s1='94,99')  # max len = xxx,xx
    total='594,98'

document.write('invoice-output.docx')

convert('../invoice-output.docx', f'C:/Studium/6. Semester/Unternehmenssoftware/repo/InvoiceReaderProject/HP/output.pdf')
