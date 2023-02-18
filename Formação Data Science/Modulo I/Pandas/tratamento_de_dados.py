import pandas as pd

#Tratando dados Faltantes
dados = pd.read_csv('../Arquivos/aluguel_residencial.csv', sep = ";")
dados.isnull()
dados[dados.Valor.isnull()]
A = dados.shape[0]
dados.dropna(subset= ['Valor'], inplace= True)
B = dados.shape[0]
A - B
dados[dados.Valor.isnull()]

dados[dados.Condominio.isnull()].shape[0]
selecao = (dados.Tipo == 'Apartamento') & (dados.Condominio.isnull())

A = dados.shape[0]
dados = dados[~selecao]
B = dados.shape[0]
A - B

dados[dados.Condominio.isnull()].shape[0]
dados.fillna(0, inplace = True)
dados[dados.Condominio.isnull()].shape[0]


dados = dados.fillna({'Condominio' : 0, 'IPTU' : 0})

dados.to_csv('../Arquivos/aluguel_residencial.csv', sep = ";", index= False)