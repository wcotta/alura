import  pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#Média aritmética

df = pd.DataFrame(data = {'Fulano': [8, 10, 4, 8, 6, 10, 8],
                          'Beltrano': [10, 2, 0.5, 1, 3, 9.5, 10],
                          'Sicrano': [7.5, 8, 7, 8, 8, 8.5, 7]},
                 index = ['Matemática',
                          'Português',
                          'Inglês',
                          'Geografia',
                          'História',
                          'Física',
                          'Química'])
df.rename_axis('Matérias', axis = 'columns', inplace = True)
df

df.Fulano.mean()

dados = pd.read_csv('../Arquivos/dados.csv')
dados.Renda.mean()

dados.head()

#Calculando média agrupada por 'Sexo'
dados.groupby(['Sexo'])['Renda'].mean()

##Exercício
dataset = pd.DataFrame({
    'Sexo': ['H', 'M', 'M', 'M', 'M', 'H', 'H', 'H', 'M', 'M'],
    'Idade': [53, 72, 54, 27, 30, 40, 58, 32, 44, 51]
})

dataset.Idade.mean()
dataset.groupby(['Sexo'])['Idade'].mean()

notas_fulano = df.Fulano
notas_fulano
notas_fulano = notas_fulano.sort_values()
notas_fulano = notas_fulano.reset_index()

notas_fulano.median()

dados.Renda.median()

df.mode()

dados.Renda.mode()
dados.Altura.mode()

#Plotando o gráfico de distribuição
grafico = sns.distplot(dados.Renda)
#Filtrando os dados a serem plotados
ax = sns.distplot(dados.query('Renda <200000').Renda)

dados.Renda.mode()
dados.Renda.mean()
dados.Renda.median()

altura = sns.distplot(dados.Altura)

dados.Altura.mode()
dados.Altura.mean()
dados.Altura.median()

sns.histplot(dados['Anos de Estudo'], stat='density', bins = 17)
sns.kdeplot(dados['Anos de Estudo'], 
            fill=True, 
            bw_adjust=8, 
            cut = 3)
