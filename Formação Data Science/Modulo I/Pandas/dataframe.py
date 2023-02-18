import pandas as pd

data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
df1 = pd.DataFrame(data)
index = ['Linha' + str(i) for i in range(3)]
df1 = pd.DataFrame(data= data, index = index)
colunas = ['Coluna' + str(i) for i in range(3)]
df1 = pd.DataFrame(data= data, index = index, columns=colunas)

df1[df1>2] = 'A'
type(df1.iloc[1, 1])

#criando dataframes

df2 = pd.DataFrame(data= data, index = index, columns=colunas)
df3 = pd.DataFrame(data= data, index = index, columns=colunas)

df1[df1>0] = 'A'

df2[df2>0] = 'B'

df3[df3>0] = 'C'

df4 = pd.concat([df1, df2, df3])
df5 = pd.concat([df1, df2, df3], axis=1)

df6 = pd.DataFrame({'A': {'X': 1}, 'B': {'X': 2}})
df7 = pd.DataFrame({'C': {'X': 3}, 'D': {'X': 4}})
pd.concat([df6, df7], axis=1)
