import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy as sc
from scipy.stats import binom
import seaborn as sns

media = 20
k = 15
probabilidade = ((np.e ** (-media)) * (media ** k)) / (np.math.factorial(k))
print('%0.8f' % probabilidade)

#Simplificando o cálculo usando a biblioteca scipy
from scipy.stats import poisson
probabilidade = poisson.pmf(k, media)
print('%0.8f' % probabilidade)

###Exercício
media = 25
k = 25
probabilidade = poisson.pmf([20, 22, 23], media)*100
probabilidade

############# DESAFIO
media_des = 20
k_des = []
for i in range(40):
    k_des.append(i+1)
prob_des = (poisson.pmf(k_des,media_des)*100).round(1)

dados = pd.DataFrame({'QTD': k_des,'Chance':prob_des})

plt.figure(figsize=(14,6))
plot = sns.barplot(data = dados, x = 'QTD', y = 'Chance', color = 'gray', width = 0.9)
for i in plot.containers:
    plot.bar_label(i,)
