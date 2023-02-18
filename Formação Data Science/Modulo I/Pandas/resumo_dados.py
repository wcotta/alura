import pandas as pd

#Relatório de Análise IV
#Seleção e Frequências

dados = pd.read_csv('../Arquivos/aluguel_residencial.csv', sep = ";")

#Selecionar somente os imóveis classificados com tipo "Apartamento"
selecao_apartamento = dados.Tipo =='Apartamento'
n1 = dados[selecao_apartamento]
n1 = dados[selecao_apartamento].shape[0]

#Selecione os imóveis classificados com tipos "Casa", "Casa de Condomínio" e "Casa de Vila"
selecao_casas = (dados.Tipo == 'Casa') | (dados.Tipo == 'Casa de Condomínio') | (dados.Tipo == 'Casa de Vila')
n2 = dados[selecao_casas]
n2 = dados[selecao_casas].shape[0]

#Selecione imóveis com áreas entre 60 e 1oo metros quadrados, incluindo os limites
selecao_area = (dados.Area >= 60) & (dados.Area <= 100)
n3 = dados[selecao_area]
n3 = dados[selecao_area].shape[0]

#Selecione os imóveis que tenham pelo menos 4 quartos e aluguel menor que R@ 2.000,00
selecao_especial = (dados.Quartos >= 4) & (dados.Valor < 2000)
n4 = dados[selecao_especial]
n4 = dados[selecao_especial].shape[0]

print("Nº de imóveis classificados com tipo 'Apartamento' <- {}".format(n1))
print("Nº de imóveis classificados com tipos 'Casa', 'Casa de Condomínio' e 'Casa de Vila' <- {}".format(n2))
print("Nº de imóveis com área entre 60 e 100 metros quadrados, incluindo os limites <- {}".format(n3))
print("Nº de imóveis que tenham pelo menos 4 quartos e aluguel menor que R$ 2.000,00 <- {}".format(n4))
