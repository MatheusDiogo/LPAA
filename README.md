<h1>Análise de Vendas</h1>

Este repositório contém um script em Python para análise de vendas. O código utiliza a biblioteca pandas, matplotlib e seaborn para processar os dados de vendas e gerar visualizações gráficas.

## Dependências
Certifique-se de que as seguintes bibliotecas Python estão instaladas:

- pandas
- matplotlib
- seaborn
- numpy

## Uso
1. Execute o script em um ambiente Python.
2. O código irá ler os dados de vendas de um arquivo Excel fornecido via link público do Google Sheets.
3. Serão realizadas etapas de limpeza e organização dos dados.
4. Serão geradas visualizações gráficas para análise das vendas.

## Funcionalidades do Código
O script oferece as seguintes funcionalidades:

- Tratamento de dados nulos: caso haja dados nulos em campos como "Cidade", "Data", "Vendas", "LojaID" e "Qtde", o código realiza tratamentos adequados.
- Adição da coluna "Mês": é adicionada uma coluna ao DataFrame com o valor do mês correspondente à data.
- Visualização de vendas por loja: são gerados gráficos de barras para mostrar o total arrecadado, total de vendas realizadas e total de produtos vendidos por cada loja.
- Análise temporal de vendas: são criados gráficos de linha temporal para visualizar a evolução das vendas ao longo dos meses e das lojas.
- Boxplot: é exibido um boxplot para verificar os parâmetros estatísticos das vendas por loja.
- Análise detalhada por mês e loja: é gerado um gráfico de barras para analisar as vendas por mês e loja.

Certifique-se de ter permissões de leitura para acessar o arquivo de dados fornecido via link público do Google Sheets.

<b>Observação:</b> O código está configurado para analisar dados específicos. Caso queira utilizar outros dados, é necessário ajustar o link do Google Sheets e as colunas a serem consideradas.

### Arquivos
- [Análise de Vendas.py](Análise%20de%20Vendas.py): Código para análise de vendas.
</br>
