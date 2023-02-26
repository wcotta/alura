import pandas as pd
import seaborn as sns
import matplotlib.pylab as plt
import numpy as np
from scipy.stats import norm

dados = pd.read_csv('dados.csv', sep = ',')

###Criando a Tabela Padronizada
tabela_normal_padronizada = pd.DataFrame(
    [], 
        index=["{0:0.2f}".format(i / 100) for i in range(0, 400, 10)],
        columns = ["{0:0.2f}".format(i / 100) for i in range(0, 10)])

for index in tabela_normal_padronizada.index:
    for column in tabela_normal_padronizada.columns:
        Z = np.round(float(index) + float(column), 2)
        tabela_normal_padronizada.loc[index, column] = "{0:0.4f}".format(norm.cdf(Z))

tabela_normal_padronizada.rename_axis('Z', axis = 'columns', inplace = True)

tabela_normal_padronizada

###Tabela Padronizada
media = 1.7
media

desvio_padrao = 0.1
desvio_padrao

Z = (1.8 - media) / desvio_padrao
Z

probabilidade = 0.8413
probabilidade

#Ultilizando o Scypy
norm.cdf(Z)

###Exercício
media = 70
media

desvio_padrao = 5
desvio_padrao

Z = (85 - media) / desvio_padrao
Z

norm.cdf(Z)


#Probabilidade com intervalos

media = 1.7

desvio_padrao = 0.1

Z1 = (1.8 - media) / desvio_padrao
Z2 = (1.6 - media) / desvio_padrao

norm.cdf(Z1) - norm.cdf(Z2)

##Exercício
media = 300

desvio_padrao = 50

Zs = (350- media) / desvio_padrao
Zi = (250- media) / desvio_padrao

a = norm.cdf(Zs) - norm.cdf(Zi)

Zs = (500- media) / desvio_padrao
Zi = (400- media) / desvio_padrao

b = norm.cdf(Zs) - norm.cdf(Zi)
a
b

#Caso III
media = 1.7

desvio_padrao = 0.1

Z = (1.9 - media) / desvio_padrao

norm.cdf(-Z)

##Exercício
media = 720

desvio_padrao = 30

Zs = (750 - media) / desvio_padrao
Zi = (650 - media) / desvio_padrao

a = (norm.cdf(Zs) - norm.cdf(Zi)).round(4)*100

Z = (800 - media) / desvio_padrao
b = (norm.cdf(-Z)).round(4)*100

Z = (700 - media) / desvio_padrao
c = (norm.cdf(Z)).round(4)*100

print(a, b, c)

norm.cdf(1.96)
norm.cdf(-2.15)
