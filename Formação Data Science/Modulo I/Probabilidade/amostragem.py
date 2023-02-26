import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import seaborn as sns

#Amostragem Aleatória Simples
dados = pd.read_csv('dados.csv', sep = ',')
dados.shape[0]
dados.Renda.mean()

##Amostragem aleatória simples .sample()
amostra  = dados.sample(n = 1000, random_state=101)
amostra.shape[0]
amostra.Renda.mean()
dados.Sexo.value_counts(normalize=True)
amostra.Sexo.value_counts(normalize=True)

##Teoria do limite Central
n = 2000
total_de_amostras = 1500

amostras = pd.DataFrame()
amostras
for i in range(total_de_amostras):
    _ = dados.Idade.sample(n)
    _.index = range(0, len(_))
    amostras['Amostra' + str(i)] = _
amostras
amostras.mean().hist()
sns.histplot(amostras.mean())
dados.Idade.mean()
amostras.mean().mean()
amostras.mean().std()
dados.Idade.std() / np.sqrt(n)

# amostras.mean().hist()

# Comparando médias
dados.Idade.mean()
#amostras.mean().mean()

# Comparando Desvio Padrão
#amostras.mean().std()
dados.Idade.std() / np.sqrt(n) # type: ignore


################ DESAFIO

qtd_amostra = int(input('Quantas amostras deseja realizar?'))
tam_amostra = int(input('Qual tamanho das amostras?'))
amostra1 = pd.DataFrame()

for i in range(qtd_amostra):
    amostra1['Amostra{}'.format(i+1)] = dados.Renda.sample(tam_amostra).describe()


populacao = dados.Renda.describe()
amostras = amostra1.mean(axis=1)

comparacao = pd.DataFrame({'População': populacao, 'Amostra': amostras})

comparacao['Erro'] = ((( populacao - amostras)  / populacao) * 100).abs().round(2)

print('Quantidade de Amostras: {}, Tamanho da Amostra: {}'.format(qtd_amostra,tam_amostra))
print(comparacao)


###Intervalos de confiança
media_amostral = 5050
significancia = 0.05
confianca = 1 - significancia
z = norm.ppf(0.975)
desv_pad = 150
n = 20
raiz = np.sqrt(n)

sigma = desv_pad/raiz

erro = z * sigma
intervalo = (
    media_amostral - erro,
    media_amostral + erro)

norm.interval(alpha = 0.95, loc = media_amostral, scale = sigma)

##Exercício 1
z = norm.ppf(0.975)
desv_pad = 6
n = 50
raiz = np.sqrt(n)
sigma = desv_pad/raiz
erro = z * sigma

#Exercício 2
media_amostral = 28
desv_pad = 11
n = 1976
z = norm.ppf(0.95)
raiz = np.sqrt(n)
sigma = desv_pad/raiz
norm.interval(alpha = 0.90, loc = media_amostral, scale = sigma)
erro = z * sigma

##Tamanho da Amostra [População Infinita]
sigma = 3323.30
z = norm.ppf(0.975)
e = 100

n = (z * (sigma/e))**2
int(n.round())

##Exercício
sigma = 15
z = norm.ppf(0.95)
e = 0.1 * 45.5 #Erro percentual em relação a média

n = (z * (sigma/e))**2
int(n.round())

##Tamanho da Amostra [População Finita]
N = 10000
z = norm.ppf(0.975)
s = 12
e = 5

n = ((s**2) * (z**2) * (N)) / (((s**2) * (z**2)) + (e**2 * (N-1)))
int(n.round())

##Exercício [População Finita]
N = 2000
z = norm.ppf(0.975)
s = 0.48
e = 0.3

n = ((s**2) * (z**2) * (N)) / (((s**2) * (z**2)) + (e**2 * (N-1)))
int(n.round())