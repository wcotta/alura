import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy as sc

dados = pd.read_csv('dados.csv', sep=",")

###Distribuição Binomial
from scipy.special import comb

combinacoes = comb(60, 6)
combinacoes

probabilidade = 1/combinacoes
print('%0.15f' %probabilidade)

###Exercício
sorteio = comb(25, 20)
probabi = 1/ sorteio

#Nº de experimentos
n = 10

n_alt_por_questao = 3
p = 1/n_alt_por_questao
p
q = 1-p
q

#Primeiro critério de aprovação
k = 5

probabilidade = (comb(n, k)) * (p ** k) * (q ** (n - k))
print('%0.8f' % probabilidade)

#Usando o Scipy
from scipy.stats import binom

probabilidade = binom.pmf(k, n, p)
print('%0.8f' % probabilidade)

#Calculando a probabilidade de acerto de 5 questões ou mais
prob = binom.pmf([5, 6, 7, 8, 9, 10], n, p).sum()
prob

#Simplificando 
prob = binom.sf(4, n, p)
prob

prob = binom.cdf(4, n, p)
prob

moeda = binom.pmf(2, 4, 0.5)
moeda

n = 10
p = 1/6
dado = binom.sf(2, n, p)
dado

n = 3
p = 0.22
k = 2
filhos = binom.pmf(k, n, p)
filhos
familias = 50*filhos
familias
