# import av alle bibliotekene vi trenger
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder


# Gjøre referansetid om til datatypen DateTime
def make_datetime(dataset):
    dataset['referansetid'] = pd.to_datetime(dataset['referansetid'])
    print('referansetid er gjort om til DateTime')
    return (dataset['referansetid'])


# Gir tidsforskyvning en label 
def label_tidsforskyvning(dataset):
    le = LabelEncoder()
    dataset['tidsforskyvning'] = le.fit_transform(dataset['tidsforskyvning'])
    print('tidsforskyvning har fått labels')
    print(dataset)


# Finner det årlige gjennomsnittet for verdien til datasettet
def average_year(dataset):
    value = np.mean(dataset['verdi'])
    unit = input("Hva er enheten til verdien i datasettet?")
    print(f"Gjennomsnittlig verdi for datasettet er {value:.2f} {unit}")
    return value


# Regner ut gjennomsnittet for hver måned
def average_month(dataset):

    # Lager en ny kolonne i temperatur som forteller hvilken måned det er 
    dataset['måned'] = dataset['referansetid'].dt.month

    # Regner ut gjennomsnittet for hver måned
    monthly_average = round(dataset.groupby('måned')['verdi'].mean(), 2)
    print('gjennomsnittlig månedlig verdi er:')
    print(monthly_average)
    return(monthly_average)


# Finner medianen
def median(dataset):
    median = np.median(dataset['verdi'])
    print("Medianen er", median)

