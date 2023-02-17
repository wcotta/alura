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


#############################################################################################################################
# Desafio. Criar Novo dataframe agrupados com ID com contagem de usuario, media de voto e tantar calcular a media ponderada #
#############################################################################################################################
import numpy as np

# numpy - media pondera
media = np.average(medias_por_filme)
ponderada = np.average(medias_por_filme, weights=avaliacoes_por_filme)

# pandas juntando series
geral = pd.merge(avaliacoes_por_filme,medias_por_filme, how='inner', on='filmeID')

# Criar coluna calculada para validar filmes com média acima da ponderada
validacao = medias_por_filme / ponderada

# Juntou a coluna calculada ao dataframe geral
classificacao = pd.merge(geral,validacao, how='inner', on='filmeID')

# filtrou filmes com média acima da ponderada
class_filtro = classificacao.query('nota_y > 1')

# Criou uma coluna calculada para criterio de ordenação em ralação ao peso (validação e Qtd de votos)
criterio = class_filtro.nota_x * class_filtro["usuarioID"]

# Juntou a coluna de criterio ao dataframe filtrado
final = pd.merge(class_filtro,criterio.to_frame(), how='inner', on='filmeID')

# Renomeou as colnas
final.columns = ["QTD_Votos", "Média_Notas", "Validação","Criterio"]

# ordenou o dataframe em relação ao criterio
class_ord = final.sort_values(by=["Criterio"], ascending=False)

#descobrindo filme com maior votos, top 10
Tier10 = pd.merge(class_ord,filmes, how='left',on='filmeID').head(10)