import pandas as pd
import matplotlib.pyplot as plt

url_csv = 'https://raw.githubusercontent.com/xavecoding/pandas-essencial/main/datasets/GasPricesinBrazil_2004-2019.csv'
data = pd.read_csv(url_csv, sep=';')
colunas = data[['REGIÃO', 'PREÇO MÉDIO REVENDA', 'DESVIO PADRÃO REVENDA']]
dados = colunas.groupby('REGIÃO').sum()
# Configurar o gráfico
fig, ax = plt.subplots(figsize=(14, 8))  # Tamanho maior para melhor visualização

# Plotar os dados com cores diferentes
colors = ['skyblue', 'salmon']  # Cores diferentes para cada barra
dados[['PREÇO MÉDIO REVENDA', 'DESVIO PADRÃO REVENDA']].plot(kind='bar', ax=ax, color=colors, edgecolor='black')

# Adicionar títulos e rótulos
ax.set_title('Preço Médio e Desvio Padrão de Revenda de Gasolina por Região no Brasil', fontsize=16, fontweight='bold')
ax.set_xlabel('Região', fontsize=14, fontweight='bold')
ax.set_ylabel('')  # Remover o rótulo do eixo y
ax.legend(['Preço Médio Revenda', 'Desvio Padrão Revenda'], fontsize=12, loc='upper left')

# Ajustar rótulos do eixo x para ficar retos
plt.xticks(rotation=0, ha='center', fontsize=12)  # Rótulos alinhados e sem rotação

# Adicionar os valores em cima das barras
for container in ax.containers:
    ax.bar_label(container, fmt='%.2f', label_type='edge', fontsize=10, color='black', padding=3)

# Adicionar gridlines
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Adicionar uma tabela de valores abaixo do gráfico (opcional)
# Cria uma tabela de dados abaixo do gráfico
table_data = dados.reset_index()
table_data = table_data.rename(columns={
    'PREÇO MÉDIO REVENDA': 'Preço Médio Revenda',
    'DESVIO PADRÃO REVENDA': 'Desvio Padrão Revenda'
})
table_ax = fig.add_axes([0.15, 0.1, 0.7, 0.2])  # [x, y, largura, altura]
table_ax.axis('tight')
table_ax.axis('off')
table_ax.table(cellText=table_data.values, colLabels=table_data.columns, loc='center', cellLoc='center', colColours=['lightgrey']*len(table_data.columns))

# Ajustar o layout para não cortar nada
plt.tight_layout()

# Exibir o gráfico
plt.show()