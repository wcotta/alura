import pandas as pd
dados = pd.read_csv('../Arquivos/aluguel_residencial.csv', sep=	";")
dados['Valor_Bruto'] = dados.Valor + dados.Condominio + dados.IPTU
dados["valor_m2"] = dados['Valor'] / dados['Area']
dados['valor_m2'] = dados["valor_m2"].round(2)
dados['Valor_Bruto m2'] = (dados['Valor_Bruto'] / dados['Area']).round(2)

casa = ['Casa', 'Casa de Condomínio', 'Casa de Vila']
#Aplicando umafunção para cada registro do dataframe
dados['Tipo agregado'] = dados['Tipo'].apply(lambda x: 'Casa' if x in casa else 'Apartamento')

#Excluindo Variáveis
dados_aux = pd.DataFrame(dados[['Tipo agregado', 'valor_m2', 'Valor_Bruto', 'Valor_Bruto m2']])
del dados_aux['Valor_Bruto']
dados_aux.pop('Valor_Bruto m2')
dados.drop(['Valor_Bruto', 'Valor_Bruto m2'], axis=1, inplace=True)
dados.to_csv('../Arquivos/aluguel_residencial.csv', sep=	";", index=False)