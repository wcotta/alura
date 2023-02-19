import pandas as pd
dados = pd.read_csv('../Arquivos/aluguel_residencial.csv', sep=	";")
dados.Valor.mean()

bairros = ['Barra da Tijuca', 'Copacabana', 'Ipanema', 'Leblon', 'Botafogo', 'Flamengo', 'Tijuca']
selecao = dados['Bairro'].isin(bairros)
dados = dados[selecao]
dados['Bairro'].drop_duplicates()
grupo_bairro = dados.groupby('Bairro')
for bairro, dados in grupo_bairro: 
    print(bairro)

for bairro, dados in grupo_bairro: 
    print('{} -> {}'.format(bairro, dados.Valor.mean()))

grupo_bairro["Valor", "Condominio"].mean().round(2)

grupo_bairro['Valor'].describe().round(2)
grupo_bairro['Valor'].aggregate(['min', 'max', 'sum'])