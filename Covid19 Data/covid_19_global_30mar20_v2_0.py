# -*- coding: utf-8 -*-
"""COVID-19_GLOBAL_28MAR20_v2.0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17EZXs24IRg34Mp38sL6f63uvMwzc-tq2

## **OBTENDO OS DADOS**
"""

import pandas as pd
import numpy as np
casos = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv')
casos.tail()

"""## **CASOS COVID-19 NO MUNDO**"""

casos = np.sum(casos.iloc[ : , 4 : casos.shape[1]])
casos.index = pd.DatetimeIndex(casos.index)
casos.tail()

casos.plot()

"""## **MORTES POR COVID-19 NO MUNDO**"""

mortes = pd.read_csv("https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv")
mortes.shape

mortes = np.sum(mortes.iloc[ : , 4 : mortes.shape[1]])
mortes.index = pd.DatetimeIndex(mortes.index)
mortes.tail()

mortes.plot()

"""## **MORTALIDADE**"""

mortalidade = (mortes/casos)*100
mortalidade.tail()

mortalidade.plot()

"""## **CARREGANDO DADOS DE PACIENTES RECUPERADOS**"""

recuperados = pd.read_csv("https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv")
recuperados.shape

recuperados = np.sum(recuperados.iloc[ : , 4 : recuperados.shape[1]])
recuperados.index = pd.DatetimeIndex(recuperados.index)
recuperados.tail()

recuperados.plot()

ativos = casos - (recuperados+mortes)
ativos.tail()

ativos.plot()

df = pd.concat([casos, ativos, recuperados, mortes], axis=1)
df.tail()

df.columns = (["casos", "ativos", "recuperados", "mortes"])
df.tail()

df.plot()

df = pd.concat([casos, recuperados], axis=1)
df.tail()

df.columns = (["casos", "recuperados"])
df.tail()

df.plot()

"""## **CALCULANDO A TAXA DE RECUPERAÇÃO**"""

recuperacao = (recuperados/casos)*100
recuperacao.tail(30)

recuperacao.plot()