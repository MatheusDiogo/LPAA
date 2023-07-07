import pandas as pd
import matplotlib.pyplot as plt

#Link de dados publicado no google sheets
URL = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vSvFVrhq0t3kaAlYFppS1lYgX1MTvYaehc2kvRQqhsPky_b1xH1WDK00vSK-ygqftD9G5x9Z2FQgfdG/pub?output=xlsx'

#Entrada de dados
dados = pd.DataFrame(pd.read_excel(URL))

dados['Cidade'].fillna("Recife", inplace=True) #Caso haja dado nulo em cidade colocar padrão como Recife
dados['Data'].dropna(inplace=True ) #Caso haja dado nulo data e não há como verificar data correta o dado deve ser apagado
dados['Vendas'].fillna("0", inplace=True) #Caso haja dado nulo em Vendas colocar padrão como 0
dados['LojaID'].dropna(inplace=True) #Caso haja dado nulo no ID da Loja e não há como verificar ID correto o dado deve ser apagado
dados['Qtde'].fillna("0", inplace=True) #Caso haja dado nulo em Qtde colocar padrão como 0

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
df
