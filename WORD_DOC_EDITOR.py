from __future__ import print_function

from datetime import date

from mailmerge import MailMerge
# from datetime import date
from docx2pdf import convert

template = "invoice.docx"

document = MailMerge(template)
print(document.get_merge_fields())

document.merge(
    Name='DARTH',
    LastName='VADER',
    Street='Throne-Room',
    HouseNumber='1',
    City='Deathstar',
    PostalCode='000066',
    Country='Galactic Empire',
    DeliveryDate='21 September 2021',  # format = DD Month YYYY
    InvoiceNumber='DE2MQ619AEUI',  # len = 12, char = numbers + letters
    Product='Super Laser - COLOR : Green, full power, destroy planets',
    asinID='if392jf893',  # len = 10, char = numbers + letters
    Prc='999,00',  # max len = xxx,xx
    n='10',  # max len = xx
    a='2,00',  # max len = xx,xx
    b='3,00',  # max len = xx,xx
    c='3,00',  # max len = xx,xx
    x='4,99',  # max len = xx,xx
    p='19',  # max len = xx
    y='5,99',  # max len = xx,xx
    z='99,00',  # max len = xx,xx
    s0='599,99',  # max len = xxx,xx
    s1='9,99')  # max len = x,xx

document.write('invoice-output.docx')

convert('invoice-output.docx', f'C:/Users/jmanc/PycharmProjects/InvoiceReaderProject/output.pdf')
