# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 16:36:59 2021

@author: Omid
"""

import pandas as pd
import random as rand
from datetime import timedelta, date

# import data sets
pro_clipper_product_data = pd.read_excel('C:/Users/Admin/Desktop/Unternehmenssoftware/Project_InvoiceReader/PRO-Clipper_Data_Invoice_Generator/pro-clipper_Produkt_Data.xlsx', index_col=0)
pro_clipper_product_data.to_csv('C:/Users/Admin/Desktop/Unternehmenssoftware/Project_InvoiceReader/PRO-Clipper_Data_Invoice_Generator/pro-clipper_Data_Entwurf_Test.csv', index=True)
product_data_new = pd.read_csv('C:/Users/Admin/Desktop/Unternehmenssoftware/Project_InvoiceReader/PRO-Clipper_Data_Invoice_Generator/pro-clipper_Data_Entwurf_Test.csv')

# xing data is available on Github
xing_data = pd.read_csv('C:/Users/Admin/Desktop/Unternehmenssoftware/Project_InvoiceReader/Xing_Data_Invoice_Generator/Xing_data.csv')
pro_clipper_data = xing_data.copy(deep=True)

# ========================================================================== #
# generate date range
def daterange(date1, date2):
    for n in range(int ((date2 - date1).days)+1):
        yield date1 + timedelta(n)

# generate dates by generated date range
def generate_date(start_date, end_date):
    date_list1 = []
    for dt in daterange(start_date, end_date):
        date_list1.append(dt.strftime("%d.%m.%Y"))  # format is like --> 19.12.2019
        #date_list1.append(dt.strftime("%d %B %Y"))  # format is like --> 19 December 2019
        #print(dt.strftime("%Y-%m-%d"))
    return date_list1

# order date (start-end)
start_dt1 = date(2018, 12, 17)
end_dt1 = date(2021, 9, 10)
auftrags_datum = generate_date(start_dt1, end_dt1)

# invoice and delivery date (start-end)
start_dt = date(2018, 12, 20)
end_dt = date(2021, 9, 13)
rechnungs_liefer_datum = generate_date(start_dt, end_dt)

# ========================================================================== #

pro_clipper_data['Rechnungs_Nummer'] = [f'GER{num - 1095000000}' for num in pro_clipper_data['Rechnungs_Nummer']]

pro_clipper_data['Auftrags_Nummer'] = [f'{num - 1083303805}P' for num in xing_data['Rechnungs_Nummer']]
pro_clipper_data['Auftrags_Datum'] = auftrags_datum
pro_clipper_data['Rechnungs_Liefer_Datum'] = rechnungs_liefer_datum
# set new order to columns
pro_clipper_data.columns
pro_clipper_data = pro_clipper_data[['Vorname', 'Name', 'Straße', 'Hausnummer', 'PLZ', 'Ort', 'Land', 
                                     'Auftrags_Nummer', 'Auftrags_Datum', 'Rechnungs_Nummer', 
                                     'Rechnungs_Liefer_Datum']]

# ========================================================================== #

# add article numbers to a new list to combine them with other relted data
article_numbers = list()
a1 = [product_data_new['Artikel-Nr'][0] for x in range(100)]
a2 = [product_data_new['Artikel-Nr'][1] for x in range(100)]
a3 = [product_data_new['Artikel-Nr'][2] for x in range(100)]
a4 = [product_data_new['Artikel-Nr'][3] for x in range(100)]
a5 = [product_data_new['Artikel-Nr'][4] for x in range(100)]
a6 = [product_data_new['Artikel-Nr'][5] for x in range(100)]
a7 = [product_data_new['Artikel-Nr'][6] for x in range(100)]
a8 = [product_data_new['Artikel-Nr'][7] for x in range(100)]
a9 = [product_data_new['Artikel-Nr'][8] for x in range(100)]
a10 = [product_data_new['Artikel-Nr'][9] for x in range(99)]
article_numbers = a1 + a2 + a3 + a4 + a5 + a6 + a7 + a8 + a9 + a10
pro_clipper_data['Artikel-Nr'] = article_numbers

# ========================================================================== #

# add product names
product_names = list()
b1 = [product_data_new['Produkt-Name'][0] for x in range(100)]
b2 = [product_data_new['Produkt-Name'][1] for x in range(100)]
b3 = [product_data_new['Produkt-Name'][2] for x in range(100)]
b4 = [product_data_new['Produkt-Name'][3] for x in range(100)]
b5 = [product_data_new['Produkt-Name'][4] for x in range(100)]
b6 = [product_data_new['Produkt-Name'][5] for x in range(100)]
b7 = [product_data_new['Produkt-Name'][6] for x in range(100)]
b8 = [product_data_new['Produkt-Name'][7] for x in range(100)]
b9 = [product_data_new['Produkt-Name'][8] for x in range(100)]
b10 = [product_data_new['Produkt-Name'][9] for x in range(99)]
product_names = b1 + b2 + b3 + b4 + b5 + b6 + b7 + b8 + b9 + b10
pro_clipper_data['Produkt-Name'] = product_names

# ========================================================================== #

# add product descriptions
product_description_list = list()
c1 = [product_data_new['Produkt-Beschreibung'][0] for x in range(100)]
c2 = [product_data_new['Produkt-Beschreibung'][1] for x in range(100)]
c3 = [product_data_new['Produkt-Beschreibung'][2] for x in range(100)]
c4 = [product_data_new['Produkt-Beschreibung'][3] for x in range(100)]
c5 = [product_data_new['Produkt-Beschreibung'][4] for x in range(100)]
c6 = [product_data_new['Produkt-Beschreibung'][5] for x in range(100)]
c7 = [product_data_new['Produkt-Beschreibung'][6] for x in range(100)]
c8 = [product_data_new['Produkt-Beschreibung'][7] for x in range(100)]
c9 = [product_data_new['Produkt-Beschreibung'][8] for x in range(100)]
c10 = [product_data_new['Produkt-Beschreibung'][9] for x in range(99)]
product_description_list = c1 + c2 + c3 + c4 + c5 + c6 + c7 + c8 + c9 + c10
pro_clipper_data['Produkt-Beschreibung'] = product_description_list


# ========================================================================== #

# add prices
price_list = list()
c1 = [product_data_new['Einzelpreis'][0] for x in range(100)]
c2 = [product_data_new['Einzelpreis'][1] for x in range(100)]
c3 = [product_data_new['Einzelpreis'][2] for x in range(100)]
c4 = [product_data_new['Einzelpreis'][3] for x in range(100)]
c5 = [product_data_new['Einzelpreis'][4] for x in range(100)]
c6 = [product_data_new['Einzelpreis'][5] for x in range(100)]
c7 = [product_data_new['Einzelpreis'][6] for x in range(100)]
c8 = [product_data_new['Einzelpreis'][7] for x in range(100)]
c9 = [product_data_new['Einzelpreis'][8] for x in range(100)]
c10 = [product_data_new['Einzelpreis'][9] for x in range(99)]
price_list = c1 + c2 + c3 + c4 + c5 + c6 + c7 + c8 + c9 + c10
pro_clipper_data['Einzelpreis mit Ust'] = price_list

# ========================================================================== #

# add a list of how often an invoice position is ordered or bought, randomly between 1-3 for testing
pro_clipper_data['Menge'] = [rand.randint(1, 3) for x in range(len(pro_clipper_data['Produkt-Name']))]

# list of shipping methods
# versandart = ['Selbstabholer', 'Lieferung']
# add shipping methods
versand_art = list()

for i in range(len(pro_clipper_data['Einzelpreis mit Ust'])):
    if i % 2 == 0:
        versand_art.append('Selbstabholer')
    else:
        versand_art.append('Lieferung')

pro_clipper_data['Versandart'] = versand_art

# add delivery charges
versand_kosten = list()

for index, row in pro_clipper_data.iterrows():
    if (row['Einzelpreis mit Ust'] * row['Menge']) < 49.00 and row['Versandart'] == 'Selbstabholer':
        versand_kosten.append(0.00)
    elif (row['Einzelpreis mit Ust'] * row['Menge']) >= 49.00:
        versand_kosten.append(0.00)
    else:
        versand_kosten.append(3.99)
        
pro_clipper_data['Versandkosten'] = versand_kosten

# ========================================================================== #

# list of payment methods
zahlungsart = ['PayPal', 'Vorkasse', 'Rechnung', 'Bar']
    
pro_clipper_data['Zahlungsart'] = [rand.choice(zahlungsart) for x in range(len(pro_clipper_data['Versandart']))]
pro_clipper_data['Ust. % Satz'] = [0.19 for x in range(len(pro_clipper_data['Einzelpreis mit Ust']))]
# ========================================================================== #

ust_list = list()

for index, row in pro_clipper_data.iterrows():
    ust = (row['Einzelpreis mit Ust'] / 119) * 100 * row['Ust. % Satz']
    ust_list.append(ust)
        
pro_clipper_data['Ust'] = ust_list

pro_clipper_data['Einzelpreis ohne Ust'] = pro_clipper_data['Einzelpreis mit Ust'] - pro_clipper_data['Ust']
pro_clipper_data['Warenwert netto'] = pro_clipper_data['Einzelpreis ohne Ust'] * pro_clipper_data['Menge']
pro_clipper_data['Versandkosten netto'] = pro_clipper_data['Versandkosten'] - (pro_clipper_data['Versandkosten'] * pro_clipper_data['Ust. % Satz'])
pro_clipper_data['Gesamt Ust'] = (pro_clipper_data['Versandkosten'] * pro_clipper_data['Ust. % Satz']) + (pro_clipper_data['Ust'] * pro_clipper_data['Menge'])
pro_clipper_data['Gesamtbetrag'] = (pro_clipper_data['Einzelpreis ohne Ust'] * pro_clipper_data['Menge']) + (pro_clipper_data['Versandkosten netto'] * pro_clipper_data['Menge']) + pro_clipper_data['Gesamt Ust']

# write the created data table to csv file
pro_clipper_data.to_csv('C:/Users/Admin/Desktop/Unternehmenssoftware/Project_InvoiceReader/PRO-Clipper_Data_Invoice_Generator/Pro-clipper_Data.csv', index=False)
# ========================================================================== #
