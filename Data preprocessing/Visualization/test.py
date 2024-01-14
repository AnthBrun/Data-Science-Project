import plotly.express as px
import pandas as pd
import numpy as np

#Path = "C:\\Users\\Anthony\\OneDrive - FHDO - PROD\\Informatik\\3. Semester\\Programmierkurs II\\Data Science Projekt\\Data preprocessing\\tageswerte_KL_collected.csv"
Path = "/home/anthony/OneDrive/Informatik/3. Semester/Programmierkurs II/Data Science Projekt/Data preprocessing/monatswerte_KL_collected.csv"
#Path = "/home/anthony/OneDrive/Informatik/3. Semester/Programmierkurs II/Data Science Projekt/Data preprocessing/monatswerte_KL_collected.csv"


dataframe = pd.read_csv(Path, encoding="latin-1")
dataframe.replace(-999, np.NAN, inplace=True)

icedays = dataframe[dataframe['MO_TN'] <= 0]
icedays['MESS_DATUM_BEGINN'] = pd.to_datetime(icedays['MESS_DATUM_BEGINN'])
icedays = icedays[icedays['MESS_DATUM_BEGINN'].dt.year >= 1824]

monthly_min_temps = icedays.groupby('MESS_DATUM_BEGINN')['MO_TN'].min().reset_index()

print("plot") 

fig = px.bar(monthly_min_temps, x='MESS_DATUM_BEGINN', y='MO_TN',
             labels={'MO_TN': 'Temperatur(°C)', 'MESS_DATUM_BEGINN': 'Datum (Jahr)'},
             title='Minimale Höchsttemperatur unter 0°C pro Monat (ab 1824)')

fig.show()
