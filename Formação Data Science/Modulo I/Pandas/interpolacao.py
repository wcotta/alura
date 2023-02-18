import pandas as pd

data = [0.5, None, None, 0.52, 0.54, None, None, 0.59, 0.6, None, 0.7]
s = pd.Series(data)
#Preencher dados faltantes por zero
s.fillna(0)

#Preencher os dados faltantes com os valores das linhas acima
s.fillna(method = 'ffill')

#Preencher os valores faltantes com os valroes das linhas abaixo
s.fillna(method = 'bfill')

#Preencher os valroes faltantes com a média dos valores dos dados
s.fillna(s.mean())

s1 = s.fillna(method = 'ffill', limit = 1)
s1.fillna(method = 'bfill', limit = 1)