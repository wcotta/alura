import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split

dados = pd.read_csv("../Arquivos/Consumo_cerveja.csv", sep=";")

#Criando uma série da variável dependente
y = dados.consumo
X = dados[{'temp_max', 'chuva', 'fds'}]

#Criando dataset de treino
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=2811)

#Criando modelo de regressão linear
from sklearn.linear_model import LinearRegression #Criar modelo de regressão linear
from sklearn import metrics #Gera as métricas de eficácia da estimação

modelo = LinearRegression()
modelo.fit(X_train, y_train)

#Obtendo o coeficinente de determinação
print('R² = {}'.format(modelo.score(X_train, y_train).round(2)))

#Gerando previsões
y_previsto = modelo.predict(X_test)

#Obtendo o coeficinente de determinação
print('R² = %s'%metrics.r2_score(y_test, y_previsto).round(2))

#Fazendo previsões pontuais
entrada = X_test[0:1]
modelo.predict(entrada)[0]

#Criando um simulador simples
temp_max=40
chuva=0
fds=1
entrada=[[temp_max, chuva, fds]]

print('{0:.2f} litros'.format(modelo.predict(entrada)[0]))

#Interpretação dos coeficientes estimados
modelo.intercept_ #quando o valor de todas variáveis explicativas forem igual a zero
modelo.coef_ #coeficiente angular de cada variável
X.columns 
index = ['Intercept0', 'Temperatura máxima', 'Chuva (mm)', 'Final de Semana']
pd.DataFrame(np.append(modelo.intercept_, modelo.coef_), index = index, columns = ['Parâmetros'])

#Plotando a correlação entre a previsão e o valor real dos dados de treino
y_previsto_train = modelo.predict(X_train)
ax = sns.scatterplot(x=y_previsto_train, y=y_train)
ax.figure.set_size_inches(12, 6)
ax.set_title('Previsão X Real', fontsize=18)
ax.set_xlabel('Consumo de Cerveja (litros) - Previsão', fontsize=14)
ax.set_ylabel('Consumo de Cerveja (litros) - Real', fontsize=14)

#Obtendo os resíduos
residuo = y_train - y_previsto_train
#Plotando os resíduos x previsão
ax = sns.scatterplot(x=y_previsto_train, y=residuo, s=150)
ax.figure.set_size_inches(20, 8)
ax.set_title('Resíduos X Previsão', fontsize=18)
ax.set_xlabel('Consumo de Cerveja (litros) - Previsão', fontsize=14)
ax.set_ylabel('Resíduos', fontsize=14)

#Comparando modelos
X2 = dados[['temp_media', 'chuva', 'fds']]
X2_train, X2_test, y2_train, y2_test = train_test_split(X2, y, test_size=0.3, random_state=2811)
modelo2 = LinearRegression()
modelo2.fit(X2_train, y2_train)

print('Modelo com temperatura Média')
print('R² = {}'.format(modelo2.score(X2_train, y2_train).round(2)))

print('Modelo com temperatura Máxima')
print('R² = {}'.format(modelo.score(X_train, y_train).round(2)))

y_previsto2 = modelo2.predict(X2_test)

print('Modelo com temperatura Média')
print('R² = {}'.format(metrics.r2_score(y2_test, y_previsto2).round(2)))

print('Modelo com temperatura Máxima')
print('R² = {}'.format(metrics.r2_score(y_test, y_previsto).round(2)))

#Raiz do erro quadrático médio
#Temperatura média
eqm2 = metrics.mean_squared_error(y2_test, y_previsto2).round(2)
reqm2 = np.sqrt(eqm2).round(2)
R2_2 = metrics.r2_score(y2_test, y_previsto2).round(2)
pd.DataFrame([eqm2, reqm2, R2_2], ['EQM', 'REQM', 'R²'], columns=['Métricas'])

#Temperatura máxima
eqm = metrics.mean_squared_error(y_test, y_previsto).round(2)
reqm = np.sqrt(eqm).round(2)
R2 = metrics.r2_score(y2_test, y_previsto).round(2)
pd.DataFrame([eqm, reqm, R2], ['EQM', 'REQM', 'R²'], columns=['Métricas'])

#Salvando e carregando o modelo estimado
import pickle
output = open('modelo_consumo_cerveja', 'wb')
pickle.dump(modelo, output)
output.close()