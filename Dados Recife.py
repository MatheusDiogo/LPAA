import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

#Link de dados publicado no google sheets
URL = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vSvFVrhq0t3kaAlYFppS1lYgX1MTvYaehc2kvRQqhsPky_b1xH1WDK00vSK-ygqftD9G5x9Z2FQgfdG/pub?output=xlsx'

#Entrada de dados
dados = pd.DataFrame(pd.read_excel(URL))

dados['Cidade'].fillna("Recife", inplace=True) #Caso haja dado nulo em cidade colocar padrão como Recife
dados['Data'].dropna(inplace=True ) #Caso haja dado nulo data e não há como verificar data correta o dado deve ser apagado
dados['Vendas'].fillna("0", inplace=True) #Caso haja dado nulo em Vendas colocar padrão como 0
dados['LojaID'].dropna(inplace=True) #Caso haja dado nulo no ID da Loja e não há como verificar ID correto o dado deve ser apagado
dados['Qtde'].fillna("0", inplace=True) #Caso haja dado nulo em Qtde colocar padrão como 0
dados['Mês'] = pd.DatetimeIndex(dados['Data']).month #Adicionando coluna com valor de meses para analises futuras

#Ordenando dados para visualização de grafico de linha temporal
dados.sort_values(by=['Data','LojaID'])
dados.reset_index(drop = True, inplace = True)

#Organizando dados para gerar possíveis insights
df = pd.DataFrame(dados.groupby(['LojaID'])['Cidade', 'Data'].nunique())
df['Cidade'] = 'Recife'
df.rename(columns={"Data":"Dias Loja Aberta"}, inplace=True)
df['Total Arrecadado'] = dados.groupby(['LojaID'])['Vendas'].sum()
df['Total Vendas Realizadas'] = dados['LojaID'].value_counts()
df['Total Produtos Vendidos'] = dados.groupby(['LojaID'])['Qtde'].sum()
df.reset_index(level = ['LojaID'], inplace = True)
df.plot(x="LojaID", y=["Total Arrecadado"], kind="bar")

df.plot(x="LojaID", y=["Total Vendas Realizadas", "Total Produtos Vendidos"], kind="bar")

#Boxplot dos dados para verificar parâmetros estatisticos
boxplot = sns.boxplot(x = 'Vendas', y = 'LojaID', data = dados, orient = 'h')
boxplot.figure.set_size_inches(12,4)
boxplot.set_title('Vendas Realizadas', fontsize=18)
boxplot.set_xlabel('Valor vendido', fontsize=14)
boxplot.set_ylabel('Número da Loja', fontsize=14)
boxplot

analiseVendas = pd.DataFrame(dados.groupby(['LojaID', 'Mês'])['Vendas'].sum())
analiseVendas.unstack(0).plot(kind='bar')
plt.show()

analiseVendas.unstack().plot(kind='bar')
plt.show()

analiseEvolucao = pd.DataFrame(dados.groupby(['Mês', 'LojaID'])['Vendas'].sum())
analiseEvolucao.unstack().plot()
plt.xticks([1,2,3])
