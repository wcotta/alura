import pandas as pd
notas = pd.read_csv("../Arquivos/ratings.csv")
notas.columns = ["usuarioID", "filmeID", "nota", "momento"]
notas['nota'].unique()
notas['nota'].value_counts()
notas["nota"].mean()
notas["nota"].median()
notas['nota'].value_counts()
notas.nota.plot(kind='hist')
notas.nota.describe()

import seaborn as sns
sns.boxplot(notas.nota)

notas.nota.plot(kind = 'box', vert = False)
