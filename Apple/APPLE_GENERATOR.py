from __future__ import print_function

from datetime import date

from mailmerge import MailMerge
# from datetime import date
from docx2pdf import convert

template = "invoice_apple.docx"

document = MailMerge(template)
print(document.get_merge_fields())

document.merge(
    Nme='DARTH',  # format = Jerome
    LstNme='VADER',  # format = Cook
    Street='Throne',
    HsNr='1',
    City='Deathstar',
    PCode='000066',
    Country='Galactic Empire',  # format = upper()
    DeliveryDate='04.05.2021',  # format = dd.mm.yyyy
    DueDate='04.05.2021',  # format = dd.mm.yyyy
    InvNum='DDDDDDDDDI',  # len = 10, char = numbers + letters, , format = LLxxxxxxxx
    ApOrNr='1234567890',  # len = 10, char = numbers
    OrdDate='03.05.2021',  # format = dd.mm.yyyy
    CNr='123456',  # len = 6, char = numbers
    OrdNum='A123456789',  # len = 10, char = numbers + letter , format = Lxxxxxxxxx
    DelivNum='1234567890',  # len = 10, char = numbers
    ProdNum='123456',  # len = 6, char = numbers
    MatNum='ABC12DE/F',  # len = 9, char = numbers + letters, format = LLLxxLL/L
    Product='Super Laser - COLOR : Green, full power',  # items from Apple product list
    Prc='999,00',  # max len = xxx,xx
    n='10',  # max len = xx
    x='4,99',  # max len = xx,xx
    p='19',  # max len = xx
    y='5,99',  # max len = xx,xx
    z='99,00',  # max len = xx,xx
    s0='599,99',  # max len = xxx,xx
    s1='9,99')  # max len = x,xx

document.write('invoice-output.docx')

convert('../invoice-output.docx', f'C:/Users/jmanc/PycharmProjects/InvoiceReaderProject/output.pdf')
