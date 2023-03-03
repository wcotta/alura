import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

dados = pd.read_csv("../Arquivos/Consumo_cerveja.csv", sep=";")
dados.shape

#Estatísticas descritivas
dados.describe().round(2)

#Matriz de Correlação
dados.corr().round(4)

#Plotando a variável dependente
fig, ax = plt.subplots(figsize=(20,6))
ax.set_title('Consumo de Cerveja', fontsize=20)
ax.set_ylabel('Litros', fontsize=16)
ax = dados.consumo.plot()

#Plotando o boxplot
ax = sns.boxplot(data = dados.consumo, orient = 'v', width = 0.2)
ax.figure.set_size_inches(6,4)
ax.set_title('Consumo de Cerveja', fontsize=20)
ax.set_ylabel('Litros', fontsize=16)

#Boxplot com duas variáveis
ax = sns.boxplot(data = dados, y = 'consumo', x = 'fds', orient = 'v', width = 0.5, palette = 'Blues_r')
ax.figure.set_size_inches(8,4)
ax.set_title('Consumo de Cerveja', fontsize=20)
ax.set_ylabel('Litros', fontsize=16)
ax.set_xlabel('Final de Semana', fontsize=16)

#Distribuição de frequência da variável dependente 'y'
ax = sns.distplot(dados.consumo)
sns.set_palette('Blues_r')
sns.set_style('darkgrid')
ax.set_title('Distribuição de Frequência', fontsize=20)

#Análise variável dependente x variável explicativa
ax = sns.pairplot(dados, y_vars = 'consumo',
                  x_vars = ['temp_min', 'temp_media', 'temp_max', 'chuva', 'fds'],
                  kind = 'reg')
ax.fig.suptitle('Dispersão entre as variáveis', fontsize = 16, y=1.1)

#Extra
ax = sns.jointplot(x="temp_max", y = "consumo", data = dados, kind = 'reg')
ax.fig.suptitle('Dispersao - Consumo X Temperatura', fontsize=18, y=1.05)
ax.set_axis_labels("Temperatura Máxima", "Consumo de Cerveja", fontsize=14)

ax= sns.lmplot(x="temp_max", y="consumo", data=dados, hue = 'fds', markers = ['o', '*'], legend = False)
ax.fig.suptitle('Reta de Regressao - Consumo X Temperatura', fontsize=16, y=1.02)
ax.set_xlabels("Temperatura Máxima (°C)", fontsize=14)
ax.set_ylabels("Consumo de Cerveja (litros)", fontsize=14)
ax.add_legend(title="Fim de Semana")

ax= sns.lmplot(x="temp_max", y="consumo", data=dados, col = 'fds')
ax.fig.suptitle('Reta de Regressao - Consumo X Temperatura', fontsize=16, y=1.02)
ax.set_xlabels("Temperatura Máxima (°C)", fontsize=14)
ax.set_ylabels("Consumo de Cerveja (litros)", fontsize=14)
