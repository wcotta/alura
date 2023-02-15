import pandas as pd
notas = pd.read_csv("../Arquivos/ratings.csv")
notas.columns = ["usuarioID", "filmeID", "nota", "momento"]
notas['nota'].unique()
notas['nota'].value_counts()
notas["nota"].mean()
notas["nota"].median()
notas['nota'].value_counts()
notas.nota.plot(kind='hist')
notas.nota.describe()

import seaborn as sns
sns.boxplot(notas.nota)

notas.nota.plot(kind = 'box', vert = False)

#Importando o dataset de filmes
filmes = pd.read_csv("../Arquivos/movies.csv")

#Modificando o cabeçalho
filmes.columns = ["filmeID", "titulo", "generos"]

#Gerando uma Query no python
#Analisando a média das notas de um filme específico
notas.query("filmeID==1").nota.mean()
notas.query("filmeID==2").nota.mean()

#Agrupando médias por uma coluna específica
notas.groupby("filmeID").mean()

#Médias por filme - Série de dados
medias_por_filme = notas.groupby("filmeID").mean()["nota"]

#Visualizando a distribuição das médias
medias_por_filme.plot(kind="hist")
sns.boxplot(x=medias_por_filme)
sns.distplot(medias_por_filme, bins = 10)

#importando o matplotlib
import matplotlib.pyplot as plt

#Plotando o Histograma com o Pyplot
plt.hist(medias_por_filme)
plt.title("Histograma das Médias dos Filmes")

#Usando o Pyplot para configurar o Seaborn
import matplotlib.pyplot as plt
plt.figure(figsize= (3,8))
sns.boxplot(y=medias_por_filme)

avaliacoes_por_filme = notas.groupby("filmeID").count()["usuarioID"]

#Média ponderada