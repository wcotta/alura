import pandas as pd
import matplotlib.pyplot as plt
plt.rc('figure', figsize = (14,6))
 
#Importando Dados
dados = pd.read_csv("../Arquivos/aluguel_residencial.csv", sep = ";")
dados.boxplot(['Valor'])
valor = dados['Valor']

#Calculando Quartis
Q1 = valor.quantile(.25)
Q3 = valor.quantile(.75)
IIQ = Q3 - Q1
limite_inferior = Q1 - 1.5 * IIQ
limite_superior = Q3 + 1.5 * IIQ
selecao = (valor>=limite_inferior) & (valor<=limite_superior)
dados_new = dados[selecao]
dados_new.boxplot(['Valor'])

dados.hist(['Valor'])
dados_new.hist(['Valor'])

#Exercício
df = pd.read_csv("../Arquivos/aluguel_amostra.csv", sep = ";")
m2 = df['Valor m2']
Q1 = m2.quantile(.25)
Q3 = m2.quantile(.75)
IIQ = Q3 - Q1
limite_inferior = Q1 - 1.5 * IIQ
limite_superior = Q3 + 1.5 * IIQ
print(Q1, Q3, IIQ, limite_inferior, limite_superior)

#Outiliers por grupo
dados_new.boxplot(['Valor'], by= ['Tipo'] )

grupo_tipo = dados.groupby('Tipo')['Valor']
Q1 = grupo_tipo.quantile(.25)
Q3 = grupo_tipo.quantile(.75)
IIQ = Q3 - Q1
limite_inferior = Q1 - 1.5 * IIQ
limite_superior = Q3 + 1.5 * IIQ
print(Q1, Q3, IIQ, limite_inferior, limite_superior)

limite_superior['Apartamento']

dados_new = pd.DataFrame()
for tipo in grupo_tipo.groups.keys():
    eh_tipo = dados['Tipo'] == tipo
    eh_dentro_limite = (dados['Valor'] >= limite_inferior[tipo]) & (dados['Valor'] <= limite_superior[tipo])
    selecao = eh_tipo & eh_dentro_limite 
    dados_selecao = dados[selecao]
    dados_new = pd.concat([dados_new, dados_selecao])

dados_new.boxplot(['Valor'], by= ['Tipo'] )
dados_new.to_csv('../Arquivos/aluguel_residencial_sem_outiliers.csv', sep=';', index=False)