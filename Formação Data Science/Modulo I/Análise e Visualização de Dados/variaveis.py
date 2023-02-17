import pandas as pd

#Importando um dataframe e verificando os dados únicos da coluna original_language

tmdb = pd.read_csv("../Arquivos/tmdb_5000_movies.csv")
tmdb.original_language.unique()

#Criando uma série com a contagem da coluna original_language
idiomas = tmdb.original_language.value_counts()

#Convertendo uma série em dataframe
idiomas = tmdb.original_language.value_counts().to_frame()

#Tornando o index uma coluna do dataframe
idiomas = tmdb.original_language.value_counts().to_frame().reset_index()

#Renomeando Colunas
idiomas.columns = ["original_language", "total"]

import seaborn as sns

#Plotando um gráfico de barras
sns.barplot(x=idiomas.original_language, y=idiomas.total)
sns.barplot(data=idiomas, x="original_language", y="total")

#Plotando o mesmo gráfico de forma mais direta
sns.catplot(x="original_language", kind="count", data=tmdb)

import matplotlib.pyplot as plt

#Gerando gráfico de pizza com pyplot
plt.pie(idiomas.total, labels = idiomas.original_language)

#Manipulando a visualização de dados
total_por_idioma = tmdb.original_language.value_counts()
total_geral = total_por_idioma.sum()
total_ingles = total_por_idioma.loc["en"]
total_outros = total_geral - total_ingles
dados = {
    "lingua" : ["Ingles", "outros"],
    "total" : [total_ingles, total_outros]
}

#Criando um dataframe
pd.DataFrame(dados)
 
#Plotando o gráfico
sns.barplot(x="lingua", y="total", data = dados)

#Filtrando os dados, excluindo uma categoria selecionada
total_filmes_exceto_ingles = tmdb.query("original_language != 'en'").original_language.value_counts()
filmes_exceto_ingles = tmdb.query("original_language != 'en'")

#Plotando o gráfico
sns.catplot(x = "original_language", kind = "count", data = filmes_exceto_ingles)

#Modificando o Gráfico
sns.catplot(x = "original_language", kind = "count", 
            data = filmes_exceto_ingles, 
            aspect = 2, 
            palette = "Blues_r", 
            order = total_filmes_exceto_ingles.index)

