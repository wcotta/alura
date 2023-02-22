import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

dados = pd.read_csv('../Arquivos/dados.csv')

dados.Renda.quantile([0.25, 0.5, 0.75])

[i/10 for i in range(1,10)]

dados.Renda.quantile([i/10 for i in range(1,10)])
dados.Renda.quantile([i/100 for i in range(1,100)])

#Plotando o boxplot usando o Seaborn
ax = sns.boxplot( x = 'Altura', data = dados, orient = 'h')
ax.figure.set_size_inches(12, 4)
ax.set_title('Altura', fontsize=18)
ax.set_xlabel('Metros', fontsize=14)
ax

#Clusterizando os dados com a Variável 'Sexo'
ax = sns.boxplot( x = 'Altura', y= 'Sexo', data = dados, orient = 'h')
ax.figure.set_size_inches(12, 4)
ax.set_title('Altura', fontsize=18)
ax.set_xlabel('Metros', fontsize=14)
ax

#Verificando a distribuição da variável 'Renda'
ax = sns.boxplot( x = 'Renda', data = dados.query('Renda < 10000'), orient = 'h')
ax.figure.set_size_inches(12, 4)
ax.set_title('Renda', fontsize=18)
ax.set_xlabel('Salário', fontsize=14)
ax

#Clusterizando a distribuição da variável 'Renda' com a Variável 'Sexo'
ax = sns.boxplot( x = 'Renda', y = 'Sexo', data = dados.query('Renda < 10000'), orient = 'h')
ax.figure.set_size_inches(12, 4)
ax.set_title('Renda', fontsize=18)
ax.set_xlabel('Salário', fontsize=14)
ax

#Verificando a distribuição da variável 'Anos de Estudo'
ax = sns.boxplot( x = 'Anos de Estudo', data = dados, orient = 'h')
ax.figure.set_size_inches(12, 4)
ax.set_title('Anos de Estudo', fontsize=18)
ax.set_xlabel('Anos', fontsize=14)
ax

#Clusterizando a distribuição da variável 'Anos de Estudo' com a Variável 'Sexo'
ax = sns.boxplot( x = 'Anos de Estudo', y = 'Sexo', data = dados, orient = 'h')
ax.figure.set_size_inches(12, 4)
ax.set_title('Anos de Estudo', fontsize=18)
ax.set_xlabel('Anos', fontsize=14)
ax

