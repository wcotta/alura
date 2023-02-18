import pandas as pd

dados = pd.read_csv("../Arquivos/aluguel.csv", sep = ";")
tipos_de_imoveis = dados.Tipo
tipos_de_imoveis.drop_duplicates(keep= 'first', inplace=True)

#Organizando a Visualização
tipos_de_imoveis = pd.DataFrame(tipos_de_imoveis)

tipos_de_imoveis.shape[0]
range(tipos_de_imoveis.shape[0])
for i in range(tipos_de_imoveis.shape[0]):
    print(i)

tipos_de_imoveis.index = range(tipos_de_imoveis.shape[0])
tipos_de_imoveis.columns.name = 'Id'