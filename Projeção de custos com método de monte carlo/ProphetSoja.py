# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 18:37:26 2019

@author: mathe
"""
import pandas as pd
from fbprophet import Prophet

#leitura dos dados
data = pd.read_excel('Soja.xlsx')

#atribui um objeto m à classe Prophet
m=Prophet()

#ajusta os pontos de tendência, quanto mais a taxa maior a flexibilidade
m = Prophet(changepoint_prior_scale=0.005)

#ajuste do modelo com o método fit da classe
m.fit(data)

#método para gerar uma tabela de resultados futuros com periodicidade mensal
future = m.make_future_dataframe(12,freq='M')

#predição sobre a variável criada
forecast = m.predict(future)

#tabela com os resultados de tendências (yhat), limites superiores (yhat_upper)
#limites inferiores (yhat_lower)
forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']]

#plotagem dos resultados de predição na sequencia da série histórica
fig1=m.plot(forecast)

#rotina para escrever os resultados em uma planilha excel
ResumoEstatístico=forecast.describe()
mzfinal=forecast.append(ResumoEstatístico)
mzfinal.to_excel('ResultadosProphet0005.xlsx')