import pandas as pd
s = pd.Series(list('asdadeadesdasesda'))
s
s.unique()
s.value_counts()

dados = pd.read_csv('../Arquivos/aluguel.csv', sep=	";")
dados.Tipo.unique()
dados.Tipo.value_counts()
