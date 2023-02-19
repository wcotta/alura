import pandas as pd
import numpy as np
import seaborn as sns
import scipy as sp

print('Versão do pandas -> %s' % pd.__version__)
print('Versão do numpy -> %s' % np.__version__)
print('Versão do seaborn -> %s' % sns.__version__)
print('Versão do scipy -> %s' % sp.__version__)

dados = pd.read_csv('../Arquivos/dados.csv')

#Veriáveis qualitativas Ordinais
sorted(dados['Anos de Estudo'].unique())

#Variáveis qualitativas Nominais
sorted(dados['Sexo'].unique())
sorted(dados['Cor'].unique())

#Variáveis quantitativas discretas
sorted(dados['Idade'].unique())
print('De %s até %s anos' % (dados.Idade.min(), dados.Idade.max()))

#Variáveis quantitativas contínuas
print('De %s até %s metros' % (dados.Altura.min().round(2), dados.Altura.max().round(2)))

#Distribuição de Frequencia para Variaveis Qualitativas
frequencia = dados['Sexo'].value_counts()
###Exibindo o resumo da frequencia em percentual
percentual_frequencia = (dados['Sexo'].value_counts(normalize=True)*100).round(2)
###Distribuição de Frequencia qualitativas
dist_freq_qual = pd.DataFrame({'Frequência': frequencia, 'Porcentagem (%)': percentual_frequencia})
dist_freq_qual.rename(index = {0:'Masculino', 1: 'Feminino'}, inplace = True)
dist_freq_qual.rename_axis('Sexo', axis='columns', inplace=True)

#Criando uma biblioteca
sexo = {0: 'Masculino',
        1: 'Feminino'}

cor = {0: 'Indígena',
        2: 'Branca',
        4: 'Preta',
        6: 'Amarela',
        8: 'Parda',
        9: 'Sem declaração'}

#Criando uma tabela com duas variáveis
freq = pd.crosstab(dados.Sexo, dados.Cor)
#Usando a biblioteca para renomear as linhas e colunas
freq.rename(index=sexo, columns=cor ,inplace=True)

percent = (pd.crosstab(dados.Sexo, 
                       dados.Cor, 
                       normalize=True)*100
                       ).round(2)
percent.rename(index=sexo, columns=cor ,inplace=True)

#Agregando pela renda
renda = (pd.crosstab(dados.Sexo, 
                       dados.Cor, 
                       aggfunc = 'mean',
                       values = dados.Renda
                       )).round(2)
renda.rename(index=sexo, columns=cor ,inplace=True)

#Criando uma biblioteca de classe social
dados.Renda.min()
dados.Renda.max()
classes = [0, 1576, 3152, 7880, 15760, 200000]
labels = ['E', 'D', 'C', 'B', 'A']
#Criando uma série classificando os dados segundo um critério
classif = pd.cut(x = dados.Renda,
                bins = classes,
                labels = labels,
                include_lowest=True
                )
classificacao = classif.value_counts()

percent_classif = (classif.value_counts(normalize = True)*100).round(2)
dist_freq_quant = pd.DataFrame({'Frequência': classificacao, 'Porcentagem (%)': percent_classif})
dist_freq_quant.sort_index(ascending=False, inplace = True)

#Exercício
classes1 = [dados.Altura.min(), 1.65, 1.75, dados.Altura.max()]
labels1 = ['1 - Baixa', '2 - Média', '3 - Alta']

frequencia1 = pd.value_counts(
    pd.cut(
        x = dados.Altura,
        bins = classes1,
        labels = labels1,
        include_lowest = True
    )
)

percentual1 = pd.value_counts(
    pd.cut(
        x = dados.Altura,
        bins = classes1,
        labels = labels1,
        include_lowest = True
    ), normalize = True
) * 100

dist_freq_altura = pd.DataFrame(
    {'Frequência': frequencia1, 'Porcentagem (%)': percentual1}
)

dist_freq_altura.rename_axis('Estaturas', axis= 'columns', inplace = True)

dist_freq_altura.sort_index(ascending = True, inplace = True)

dist_freq_altura

#Usando Numpy para definir as classes

n = dados.shape[0]
k= 1 + (10/3) * np.log10(n)
k = int(k.round(0))

freq_class = pd.value_counts(
    pd.cut(
    x =dados.Renda,
    bins = 17,
    include_lowest=True
    ), sort=False
)

perc_class = pd.value_counts(
    pd.cut(
    x =dados.Renda,
    bins = 17,
    include_lowest=True
    ), sort=False, normalize=True
)*100
dist_freq_numpy = pd.DataFrame(
    {'Frequência': freq_class, 'Porcentagem (%)': perc_class}
)

#Plotando o Histograma com o Seaborn
ax = sns.displot(dados.Altura, kde = False)
ax.figure.set_size_inches(12, 6)
ax.set_title('Distribuição de Frequências - Altura', fontsize=18)
ax.set_xlabel('Metros', fontsize=14)
ax

#Plotando o Histograma com o Pandas
dados.Altura.hist(bins = 50, figsize=(12,6))

dist_freq_quant['Frequência'].plot.bar(width = 1, color= 'blue', alpha = 0.2, figsize=(12,6))

#######DESAFIO##########

Q1 = dados.Renda.quantile(.25)
Q3 = dados.Renda.quantile(.75)
IIQ = Q3 - Q1
limite_inferior = Q1 - 1.5 * IIQ
limite_superior = Q3 + 1.5 * IIQ
selecao = (dados.Renda>=limite_inferior) & (dados.Renda<=limite_superior)
dados_new = dados[selecao]

n1 = dados_new.shape[0]
k1= (1 + (10/3) * np.log10(n)).round(0)
k1 = int(k)

freq_class1 = pd.value_counts(
    pd.cut(
    x =dados_new.Renda,
    bins = k1,
    include_lowest=True
    ), sort=False
).round(0)

perc_class1 = pd.value_counts(
    pd.cut(
    x =dados_new.Renda,
    bins = k1,
    include_lowest=True
    ), sort=False, normalize=True
)*100
dist_freq_numpy1 = pd.DataFrame(
    {'Frequência': freq_class1, 'Porcentagem (%)': perc_class1}
)

dist_freq_numpy1['Frequência'].plot.bar(width = 1, color= 'grey', alpha = 1, figsize=(12,6))

dados_new.Renda.hist(bins = k)

sns.histplot(dados_new.Renda, 
             stat='density', 
             bins=k)
sns.kdeplot(dados_new.Renda, 
            fill=True, 
            bw_adjust=5, 
            cut = 3)

#bins quantidade de classes
#bw_adjust suavisa 