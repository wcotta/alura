import pandas as pd

#Series 
data = [1, 2, 3, 4, 5]
s = pd.Series(data)

#Criando um Index
index = ['Linha' + str(i) for i in range(5)]
s = pd.Series(data=data, index=index)