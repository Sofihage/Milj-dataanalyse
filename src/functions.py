# import av alle bibliotekene vi trenger
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import missingno as msno
import sys

sys.path.append('C:/Users/sofie/OneDrive - NTNU/4. semester/TDT4114 Anvendt programmering/Milj-dataanalyse/venv/Lib/site-packages')   
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import train_test_split
from sklearn import datasets, linear_model


# Gjøre referansetid om til datatypen DateTime
def make_datetime(dataset):
    dataset['referansetid'] = pd.to_datetime(dataset['referansetid'])
    print('referansetid er gjort om til DateTime')
    return (dataset['referansetid'])


# Gir valgt kolonne en label 
def label(dataset, column="tidsforskyvning"):
    le = LabelEncoder()
    dataset[column] = le.fit_transform(dataset[column])
    print(f'{column} har fått labels')
    print(dataset)


# Finner medianen
def median(dataset):
    median = np.median(dataset['verdi'])
    print("Medianen er", median)
    return median

# Lager et enkelt stolpediagram over en serie med data + gjennomsnitt
def average_month_bargraph(series, name, unit):
    index = series.index
    values = series.values
    series_mean = [np.mean(series.values)]*len(series.index)

    # Initiere subplots
    fig, ax = plt.subplots()
    # Plotte dataserie
    data_bars = ax.bar(index, values)
    # Plotte gjennomsnittet
    mean_line = ax.plot(index, series_mean,
                        label='Gjennomsnitt',
                        linestyle='--',
                        color='orange'
                        )
    # Formatering
    legend = ax.legend(loc='upper center')
    plt.title(name)
    plt.xlabel('Måned')
    plt.ylabel(unit)
    ax.set_axisbelow(True)
    plt.grid(axis='y')
    plt.xticks(rotation=0, ticks=index, labels=index)

    plt.show()

# Finner det årlige gjennomsnittet for verdien til datasettet
def average_year(dataset):
    value = np.mean(dataset['verdi'])
    print(f"Gjennomsnittlig verdi for datasettet er {value:.2f}")
    return value


# Regner ut gjennomsnitt gruppert etter de ulike verdiene i valgt kolonne
def average_other(dataset, column="måned"):

    # Lager en ny kolonne i temperatur som forteller hvilken måned det er 
    if column == 'måned':
        dataset['måned'] = dataset['referansetid'].dt.month

    # Regner ut gjennomsnittet for hver kolonne
    other_average = round(dataset.groupby(column)['verdi'].mean(), 2)
    return(other_average)


# Finner standardavik 
def std(dataset):
    std = np.std(dataset['verdi'])
    print('Standardavviket er', round(std, 2))
    return float(std)


# Finner øvre og nedre grense med hjelp av standardavvik
def lower_upper_limit(dataset):
    mean = average_year(dataset)
    s = std(dataset)
    threshold = 3
    lower_limit = mean - threshold * s
    upper_limit = mean + threshold * s

    return(lower_limit, upper_limit)

    print("Nedre grense:", lower_limit)
    print("Øvre grense:", upper_limit)


# Viser og teller eventuelle manglende verdier
def missing_numbers(dataset, column='verdi'):

    # Teller om noen av verdiene er None eller NaN
    count_nan = dataset.isnull().sum()
    print(count_nan)

    # Visualiserer hvor mange verdier hver kolonne har
    msno.bar(dataset)

    
    data_missing = dataset[dataset[column].isna()]
    print(data_missing)


# Deler datasettet inn i train og test
def train_test_set(dataset, size_test):    
    # Gir labels til referansetid
    label(dataset, 'referansetid')

    # Deler datasettet inn i train og test  
    X_train, X_test, y_train, y_test = train_test_split(dataset['referansetid'], dataset['verdi'], test_size=size_test, random_state=42)

    X_train, y_train = zip(*sorted(zip(X_train, y_train), key=lambda x: x[0]))
    X_test, y_test = zip(*sorted(zip(X_test, y_test), key=lambda x: x[0]))

    X_train = np.array(X_train).reshape(-1, 1)
    X_test = np.array(X_test).reshape(-1, 1)
    y_train = np.array(y_train)
    y_test = np.array(y_test)

    print('Datasettet er delt inn i train og test')
    print(f'Størrelsen på test er {size_test}')

    return(X_train, X_test, y_train, y_test)


# Lager lineær regresjon og lagrer koeffisienter og konstantledd
def linear(X, y):
    regr = linear_model.LinearRegression()

    regr.fit(X, y)

    lin_y_pred = regr.predict(X)

    a = regr.coef_
    a = a[0]
    print("koeffisienter:", a)

    b = regr.intercept_
    print("konstantledd:", b)
    
    return lin_y_pred


def poly(X, y):
    poly = PolynomialFeatures(degree=2, include_bias=False)

    poly_features = poly.fit_transform(X)

    poly_reg = linear_model.LinearRegression()

    poly_reg.fit(poly_features, y)

    poly_y_pred = poly_reg.predict(poly_features)

    b, a = poly_reg.coef_
    print("koeffisienter:", b, a)

    c = poly_reg.intercept_
    print("konstantledd:", c)

    return poly_y_pred