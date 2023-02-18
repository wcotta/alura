#Relatório de Análises I
import pandas as pd

#Importando o dataframe e separando pelo delimitador
dados = pd.read_csv("../Arquivos/aluguel.csv", sep=";")

#Informações Gerais sobre a base de dados
dados.dtypes

tipos_de_dados = pd.DataFrame(dados.dtypes, columns=["tipos_de_dados"])
tipos_de_dados.columns.name = 'variaveis'

#Verificando formato dos dados
dados.shape
dados.shape[0]
dados.shape[1]

print("A base de dados apresenta {} registros (imóveis) e {} variáveis".format(dados.shape[0], dados.shape[1]))