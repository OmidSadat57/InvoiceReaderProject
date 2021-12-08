# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 14:18:22 2021

@author: Admin
"""

from datetime import timedelta, date
import pandas as pd

# generate date range
def daterange(date1, date2):
    for n in range(int ((date2 - date1).days)+1):
        yield date1 + timedelta(n)

# generate dates by generated date range
def generate_date(start_date, end_date):
    date_list1 = []
    for dt in daterange(start_date, end_date):
        date_list1.append(dt.strftime("%d %B %Y"))  # format is like --> 19 December 2019
        #print(dt.strftime("%Y-%m-%d"))
    return date_list1

# order date (start-end)
start_dt1 = date(2018, 12, 17)
end_dt1 = date(2021, 9, 10)
bestell_datum = generate_date(start_dt1, end_dt1)

# invoice and delivery date (start-end)
start_dt = date(2018, 12, 20)
end_dt = date(2021, 9, 13)
rechnungs_liefer_datum = generate_date(start_dt, end_dt)

# import given or available data
excel_data_old = pd.read_excel('C:/Users/Admin/Desktop/Unternehmenssoftware/Project_InvoiceReader/Adressen.xlsx', index_col=0)
# write data to .csv file
excel_data_old.to_csv('C:/Users/Admin/Desktop/Unternehmenssoftware/Project_InvoiceReader/Adressen.csv', index=True)

amazon_data = pd.read_csv('C:/Users/Admin/Desktop/Unternehmenssoftware/Project_InvoiceReader/Adressen.csv')
amazon_data.columns

# select and add only necessary columns as to new amazon data frame 
amazon_data['Land'] = ['Germany' for x in range(len(amazon_data['Ort']))]
amazon_data['Bestell_Datum'] = bestell_datum
amazon_data['Rechnungs_Liefer_Datum'] = rechnungs_liefer_datum

# ============================================================================#
# order number pattern = '123-123xxxx-123xxxx'
# generate a list of order numbers and combine it with dashes as specified in the pattern
order_numbers = list()
num_list1 = [i for i in range(3567, 4566)]
for i in num_list1:
    st = f'123-123{i}-123{i}'
    order_numbers.append(st)

amazon_data['Bestell_Nummer'] = order_numbers

# ============================================================================#
# ASIN --> asinID_pattern = 'ifxxxjfxxx'
# generate a list of asinIDs and combine it with letter as specified in the pattern
asin_numbers1 = list()
asin_list1 = [i for i in range(100, 1000)]
for x in asin_list1:
    st1 = f'if492jf{x}'
    asin_numbers1.append(st1)

#print(len(asin_numbers1))

asin_numbers2 = list()
asin_list2 = [i for i in range(400, 499)]
for t in asin_list2:
    st2 = f'if592jf{x}'
    asin_numbers2.append(st2)

#print(len(asin_numbers2))

amazon_data['ASIN_ID'] = asin_numbers1 + asin_numbers2

# ============================================================================#
# example --> InvoiceNumber = DE2MQ619AEUI
# invoice number pattern = 'DExMQxxxAEUI'
# generate a list of invoice numbers and combine it with letters as specified in the pattern
invoice_numbers1 = list()
num_list3 = [i for i in range(100, 1000)]
for e in num_list3:
    st3 = f'DE3MQ{e}AEUI'
    invoice_numbers1.append(st3)

invoice_numbers2 = list()
num_list4 = [i for i in range(400, 499)]
for p in num_list4:
    st4 = f'DE4MQ{p}AEUI'
    invoice_numbers2.append(st4)

amazon_data['Rechnungs_Nummer'] = invoice_numbers1 + invoice_numbers2
# ============================================================================#

# sort values for adding products to prices, each product should be assigned to prices 
# and correspond to their real and possible prices on the market
amazon_data = amazon_data.sort_values('Stückpreis ohne Ust', ascending=True)
amazon_data.columns

# have a look to different price categories in the data table Amazon_Data.csv
price_categories = set(amazon_data['Stückpreis ohne Ust'])

stueckpreis_ohne_ust = list(amazon_data['Stückpreis ohne Ust'])

v1 = ['Flachdichtung - WC' for x in range(stueckpreis_ohne_ust.count(stueckpreis_ohne_ust[20]))]
v2 = ['Dichtung - Plastik' for x in range(stueckpreis_ohne_ust.count(stueckpreis_ohne_ust[104]))]
v3 = ['Gummi-Dichtung' for x in range(stueckpreis_ohne_ust.count(stueckpreis_ohne_ust[168]))]
v4 = ['Rost Kerze Edelrost' for x in range(stueckpreis_ohne_ust.count(stueckpreis_ohne_ust[189]))]
v5 = ['Hirsch Rentier Elch Figur' for x in range(stueckpreis_ohne_ust.count(stueckpreis_ohne_ust[274]))]
v6 = ['Tragbares Wiederaufladbare Buchlampe' for x in range(stueckpreis_ohne_ust.count(stueckpreis_ohne_ust[295]))]
v7 = ['Retro LED Lampe Schreibtischlampe' for x in range(stueckpreis_ohne_ust.count(stueckpreis_ohne_ust[316]))]
v8 = ['Lavalampe Magma Lava Lampe Magmaleuchte' for x in range(stueckpreis_ohne_ust.count(stueckpreis_ohne_ust[337]))]
v9 = ['Himalaya- Salzlampe' for x in range(stueckpreis_ohne_ust.count(stueckpreis_ohne_ust[358]))]
v10 = ['LED Stern Deko Boden Lampe Weihnachte' for x in range(stueckpreis_ohne_ust.count(stueckpreis_ohne_ust[377]))]
v11 = ['LED Pyramide 60 cm warmweiß - 20 LED' for x in range(stueckpreis_ohne_ust.count(stueckpreis_ohne_ust[398]))]
v12 = ['Playstation, Icons Light, Nachtlicht' for x in range(stueckpreis_ohne_ust.count(stueckpreis_ohne_ust[419]))]
v13 = ['LED Deckenleuchte Wandleuchte Fernbedienung' for x in range(stueckpreis_ohne_ust.count(stueckpreis_ohne_ust[440]))]
v14 = ['Stehlampe Holz Tripod Stativ Dreibein' for x in range(stueckpreis_ohne_ust.count(stueckpreis_ohne_ust[504]))]
v15 = ['LED Unterbauleuchte Mit Bewegungsmelder' for x in range(stueckpreis_ohne_ust.count(stueckpreis_ohne_ust[546]))]
v16 = ['Tischlampe Nachttischlampe 2er Set' for x in range(stueckpreis_ohne_ust.count(stueckpreis_ohne_ust[588]))]
v17 = ['Dimmbar LED Klemmleuchte Schreibtischlampe' for x in range(stueckpreis_ohne_ust.count(stueckpreis_ohne_ust[609]))]
v18 = ['LED Unterbauleuchte Lichtleiste Küche' for x in range(stueckpreis_ohne_ust.count(stueckpreis_ohne_ust[695]))]
v19 = ['PUMA Nucleus Trainingsschuhe' for x in range(stueckpreis_ohne_ust.count(stueckpreis_ohne_ust[716]))]
v20 = ['Kappa Base 2 Sportschuhe Turnschuhe Sneakers' for x in range(stueckpreis_ohne_ust.count(stueckpreis_ohne_ust[737]))]
v21 = ['Adidas Schuhe ClimaCool 2 Sneakers' for x in range(stueckpreis_ohne_ust.count(stueckpreis_ohne_ust[764]))]
v22 = ['Philipp Plein Sport Runner Sneaker ' for x in range(stueckpreis_ohne_ust.count(stueckpreis_ohne_ust[808]))]
v23 = ['Nike Court Borough Mid Winter Sneaker' for x in range(stueckpreis_ohne_ust.count(stueckpreis_ohne_ust[830]))]
v24 = ['NIKE AIR FORCE 1 Mit Stiefel TOoP Sneaker' for x in range(stueckpreis_ohne_ust.count(stueckpreis_ohne_ust[876]))]
v25 = ['Herren Schuhe Turnschuhe Sneaker Airmax' for x in range(stueckpreis_ohne_ust.count(stueckpreis_ohne_ust[897]))]
v26 = ['Panasonic ToughBook CF-52 i5 15,4' for x in range(stueckpreis_ohne_ust.count(stueckpreis_ohne_ust[919]))]
v27 = ['Lenovo IdeaPad 1 81VU00A4GE - 14' for x in range(stueckpreis_ohne_ust.count(stueckpreis_ohne_ust[922]))]
v28 = ['LENOVO ThinkPad X260 Intel Core i7 6. Gen 2' for x in range(stueckpreis_ohne_ust.count(stueckpreis_ohne_ust[943]))]
v29 = ['Rennrad Herren Gebraucht' for x in range(stueckpreis_ohne_ust.count(stueckpreis_ohne_ust[962]))]
v30 = ['Rakete Roadster Berlin - Urban Bike' for x in range(stueckpreis_ohne_ust.count(stueckpreis_ohne_ust[984]))]
v31 = ['26 ZOLL MOUNTAINBIKE SHIMANO 21GANG 26' for x in range(stueckpreis_ohne_ust.count(stueckpreis_ohne_ust[998]))]

product = v1+v2+v3+v4+v5+v6+v7+v8+v9+v10+v11+v12+v13+v14+v15+v16+v17+v18+v19+v20+v21+v22+v23+v24+v25+v26+v27+v28+v29+v30+v31

amazon_data['Produkt'] = product
amazon_data.index
amazon_data = amazon_data.sort_index()

# ============================================================================#
# set specific order for columns and write into new .csv file
amazon_data = amazon_data[['Vorname', 'Name', 'Straße', 'Hausnummer', 'PLZ', 'Ort', 'Land', 'Produkt', 'Bestell_Nummer', 'ASIN_ID', 'Bestell_Datum', 'Rechnungs_Nummer', 'Rechnungs_Liefer_Datum', 'n', 'VK ohne Ust', 'VK mit Ust', 'VK Gesamt', 'Stückpreis mit Ust', 'Stückpreis ohne Ust', 'Ust. % Satz', 'ZS Produkt', 'Zs ohne Ust', 'Gesamt Ust. Betrag']]
amazon_data.to_csv('C:/Users/Admin/Desktop/Unternehmenssoftware/Project_InvoiceReader/Amazon_Data_Invoice_Generator/Amazon_Data.csv', index=False)
# import data only for testing, if necessary
# test_df = pd.read_csv('C:/Users/Admin/Desktop/Unternehmenssoftware/Project_InvoiceReader/Amazon_Data_Invoice_Generator/Amazon_Data.csv')
