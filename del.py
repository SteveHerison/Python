
# Dados fornecidos
dados_x = ['2018', '2019', '2020', '2021']
dados_y = [10, 20, 5, 35]

# Criar o gráfico de barras
fig = px.bar(x=dados_x, y=dados_y, width=700, height=300)

# Exibir o gráfico
fig.show()