# Relatório de Análise III

import pandas as pd
dados = pd.read_csv('../Arquivos/aluguel.csv', sep=";")

#Criando uma lista
list(dados.Tipo.drop_duplicates())

residencial = ['Quitinete',
 'Casa',
 'Apartamento',
 'Casa de Condomínio',
 'Casa de Vila']

#Validando dados de uma coluna
selecao = dados.Tipo.isin(residencial)
dados_residencial = dados[selecao]

list(dados_residencial.Tipo.drop_duplicates())
dados_residencial.shape[0]
dados_residencial.index = range(dados_residencial.shape[0])

#Exportando a base de dados
dados_residencial.to_csv('../Arquivos/aluguel_residencial.csv', sep = ";", index=False, )

dados_residencial_2 = pd.read_csv('../Arquivos/aluguel_residencial.csv', sep = ";")