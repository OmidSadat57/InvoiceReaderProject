# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 15:50:21 2021

@author: Admin
"""

import pandas as pd

old_data = pd.read_csv('C:/Users/Admin/Desktop/Unternehmenssoftware/DataSetBereinigung_Projekt/Adresses_edited.csv')

# according to statista Xing had around 19 million customers in 2020 in DACH region
# remove multiple rows by index or set in Xing_Generator.py the index to 
# --> if index == 200: break, in order to generate only 200+1 invoices
old_data.to_csv('C:/Users/Admin/Desktop/Unternehmenssoftware/DataSetBereinigung_Projekt/Test2_Xing/Xing_data.csv', index=False)
data_xing = pd.read_csv('C:/Users/Admin/Desktop/Unternehmenssoftware/DataSetBereinigung_Projekt/Test2_Xing/Xing_data.csv')


# add new columns and change column 'Land' value from Germany to Deutschland
data_xing['Land'] = ['Deutschland' for x in range(len(data_xing['Land']))]
data_xing['Rechnungs_Liefer_Datum'] = ['07.11.2020' for x in range(len(data_xing['Land']))]
data_xing['Bestell_Datum'] = ['07.11.2020' for x in range(len(data_xing['Rechnungs_Liefer_Datum']))]

# a change to column name from 'Rechnungs_Liefer_Datum' to Rechnungs_Datum'
data_xing.columns = ['Vorname', 'Name', 'Straße', 'Hausnummer', 'PLZ', 'Ort', 'Land', 'Rechnungs_Datum', 
                      'Leistungs_Beginn', 'n', 'VK ohne Ust', 'VK mit Ust', 'VK Gesamt', 'Stückpreis mit Ust', 
                      'Stückpreis ohne Ust', 'Ust. % Satz', 'ZS Produkt', 'Zs ohne Ust', 'Gesamt Ust. Betrag']

# add new columns
data_xing['Leistungs_Ende'] = ['06.11.2021' for x in range(len(data_xing['Leistungs_Beginn']))]
data_xing['Produkt'] = ['Premium-Mitgliedschaft' for x in range(len(data_xing['Rechnungs_Datum']))]
data_xing['Preis_ohne_Ust'] = [9.95 for x in range(len(data_xing['Produkt']))]
data_xing['Ust'] = [x * 0.19 for x in data_xing['Preis_ohne_Ust']]
data_xing['Preis_mit_Ust'] = list(data_xing['Preis_ohne_Ust'] + data_xing['Ust'])

# add the column customer number as string and other
data_xing['Kunden_Nummer'] = ['PRM' + str(x) for x in range(120110038741, 120110039740)]
data_xing['Rechnungs_Nummer'] = [x for x in range(1095658611, 1095659610)]
data_xing['Abrechnungs_Nummer'] = ['B-9AV15436GG' + str(x) for x in range(4988600, 4989599)]

data_xing = data_xing[['Kunden_Nummer', 'Vorname', 'Name', 'Straße', 'Hausnummer', 'PLZ', 'Ort', 'Land', 
                       'Rechnungs_Nummer', 'Rechnungs_Datum', 
                       'Leistungs_Beginn', 'Leistungs_Ende', 'Produkt', 'Preis_ohne_Ust', 'Preis_mit_Ust', 
                       'Ust. % Satz', 'Ust', 'Abrechnungs_Nummer']]
data_xing.to_csv('C:/Users/Admin/Desktop/Unternehmenssoftware/DataSetBereinigung_Projekt/Test2_Xing/Xing_data.csv', index=False)
# data_xing.columns
# print(type(data_xing['Rechnungs_Datum'][0]))
