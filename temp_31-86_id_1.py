#id 1 Aach in BW

import pandas as pd
import numpy as np

path = "C:\\Users\\Anthony\\OneDrive - FHDO - PROD\\Informatik\\3. Semester\\Programmierkurs II\\Data Science Projekt\\produkt_klima_monat_19310101_19860630_00001.csv"

df = pd.read_csv(path)
df = pd.DataFrame(data=df)
# MESS_DATUM_BEGINN  MESS_DATUM_ENDE
mess_datum_beginn = df['MESS_DATUM_BEGINN']
mess_datum_ende = df['MESS_DATUM_ENDE']
mo_rr = df['MO_RR']
mx_rs = df['MX_RS']
save = pd.DataFrame(data=[[mess_datum_beginn],[mess_datum_ende],[mx_rs],[mo_rr]])
print(save)

# with open("produk_klima_monat_short.csv",'w+') as file:
#     file.write(save)