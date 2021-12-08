# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 15:50:21 2021

@author: Admin
"""

import pandas as pd

old_data = pd.read_csv('C:/Users/Admin/Desktop/Unternehmenssoftware/Project_InvoiceReader/Adresses_edited.csv')

# according to statista Xing had around 19 million customers in 2020 in DACH region
# remove multiple rows by index or set in Xing_Invoice_Generator.py the index to 
# --> if index == 200: break, in order to generate only 200+1 invoices
old_data.to_csv('C:/Users/Admin/Desktop/Unternehmenssoftware/Project_InvoiceReader/Xing_Data_Invoice_Generator/Xing_data.csv', index=False)
xing_data = pd.read_csv('C:/Users/Admin/Desktop/Unternehmenssoftware/Project_InvoiceReader/Xing_Data_Invoice_Generator/Xing_data.csv')


# add new columns and change column 'Land' value from Germany to Deutschland
xing_data['Land'] = ['Deutschland' for x in range(len(xing_data['Land']))]
xing_data['Rechnungs_Liefer_Datum'] = ['07.11.2020' for x in range(len(xing_data['Land']))]
xing_data['Bestell_Datum'] = ['07.11.2020' for x in range(len(xing_data['Rechnungs_Liefer_Datum']))]

# a change to column name from 'Rechnungs_Liefer_Datum' to Rechnungs_Datum'
xing_data.columns = ['Vorname', 'Name', 'Straße', 'Hausnummer', 'PLZ', 'Ort', 'Land', 'Rechnungs_Datum', 'Leistungs_Beginn', 'n', 'VK ohne Ust', 'VK mit Ust', 'VK Gesamt', 'Stückpreis mit Ust', 'Stückpreis ohne Ust', 'Ust. % Satz', 'ZS Produkt', 'Zs ohne Ust', 'Gesamt Ust. Betrag']

# add new columns
xing_data['Leistungs_Ende'] = ['06.11.2021' for x in range(len(xing_data['Leistungs_Beginn']))]
xing_data['Produkt'] = ['Premium-Mitgliedschaft' for x in range(len(xing_data['Rechnungs_Datum']))]
xing_data['Preis_ohne_Ust'] = [9.95 for x in range(len(xing_data['Produkt']))]
xing_data['Ust'] = [x * 0.19 for x in xing_data['Preis_ohne_Ust']]
xing_data['Preis_mit_Ust'] = list(xing_data['Preis_ohne_Ust'] + xing_data['Ust'])

# add the column customer number as string and other
xing_data['Kunden_Nummer'] = ['PRM' + str(x) for x in range(120110038741, 120110039740)]
xing_data['Rechnungs_Nummer'] = [x for x in range(1095658611, 1095659610)]
xing_data['Abrechnungs_Nummer'] = ['B-9AV15436GG' + str(x) for x in range(4988600, 4989599)]

# set new column order
xing_data = xing_data[['Kunden_Nummer', 'Vorname', 'Name', 'Straße', 'Hausnummer', 'PLZ', 'Ort', 'Land', 'Rechnungs_Nummer', 'Rechnungs_Datum', 'Leistungs_Beginn', 'Leistungs_Ende', 'Produkt', 'Preis_ohne_Ust', 'Preis_mit_Ust', 'Ust. % Satz', 'Ust', 'Abrechnungs_Nummer']]
xing_data.to_csv('C:/Users/Admin/Desktop/Unternehmenssoftware/Project_InvoiceReader/Xing_Data_Invoice_Generator/Xing_data.csv', index=False)
# xing_data.columns
# print(type(xing_data['Rechnungs_Datum'][0]))
