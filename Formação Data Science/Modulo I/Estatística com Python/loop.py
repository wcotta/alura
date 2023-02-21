import pandas as pd

df=pd.read_csv('../Arquivos/dados.csv', sep=',')

results = []
for idade in df['Idade']:
    if idade >= 18:
        results.append('Maior de Idade')
    else:
        results.append('Menor de Idade')
df['Maior idade'] = results

df.query('Idade < 18')