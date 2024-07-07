import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import ipeadatapy as ipea
import numpy as np

# Função para carregar os dados
@st.cache
def load_data():
    babacu = ipea.timeseries('EIA366_PBRENT366')
    babacu = babacu.reset_index()
    babacu['DATE'] = pd.to_datetime(babacu['DATE'])
    babacu = babacu.sort_values(by='DATE')
    return babacu

# Carregar os dados
babacu = load_data()

# Título da aplicação
st.title('Análise do Preço do Petróleo Brent')

# Gráfico de Dispersão
st.subheader('Gráfico de Dispersão: ANO vs VALOR')
plt.figure(figsize=(10, 6))
plt.scatter(babacu['DATE'].dt.year, babacu['VALUE (US$)'])
plt.xlabel('ANO')
plt.ylabel('VALOR (US$)')
plt.title('Gráfico de Dispersão: ANO vs VALOR')
st.pyplot(plt)

# Gráfico de Linha com Picos de Aumento e Diminuição
st.subheader('Gráfico de Linha com Picos de Aumento e Diminuição')
values = babacu['VALUE (US$)'].values
dates = babacu['DATE'].values

# Identificar picos de alta e baixa
picos_aumento_indices = np.argwhere((values > np.roll(values, 1)) & (values > np.roll(values, -1))).flatten()
picos_diminuicao_indices = np.argwhere((values < np.roll(values, 1)) & (values < np.roll(values, -1))).flatten()

# Selecionar os 3 maiores picos de aumento
top_3_increase_indices = picos_aumento_indices[np.argsort(values[picos_aumento_indices])[-3:]]

# Selecionar os 3 maiores picos de diminuição
top_3_decrease_indices = picos_diminuicao_indices[np.argsort(values[picos_diminuicao_indices])[:3]]

# Plotar gráfico de linha
plt.figure(figsize=(14, 7))
plt.plot(babacu['DATE'], babacu['VALUE (US$)'], label='Preço (US$)', color='blue')

# Destaque para os 3 maiores picos de aumento
plt.scatter(dates[top_3_increase_indices], values[top_3_increase_indices], color='green', marker='o', label='Picos de Aumento')

# Destaque para os 3 maiores picos de diminuição
plt.scatter(dates[top_3_decrease_indices], values[top_3_decrease_indices], color='red', marker='o', label='Picos de Diminuição')

plt.xlabel('Data')
plt.ylabel('Valor (US$)')
plt.title('Gráfico de Linha com Picos de Aumento e Diminuição')
plt.legend()
st.pyplot(plt)

# Histograma do Preço Médio Anual
st.subheader('Histograma do Preço Médio Anual')
media_por_ano = babacu.groupby(babacu['DATE'].dt.year)['VALUE (US$)'].mean()

plt.figure(figsize=(10, 6))
plt.hist(media_por_ano, bins=10, color='lightblue', edgecolor='black')
plt.xlabel('Preço Médio (US$)')
plt.ylabel('Frequência')
plt.title('Histograma de Preço Médio Anual de Petróleo Brent')
plt.grid(True, linestyle='--', alpha=0.5)
st.pyplot(plt)

# Gráfico de Barras da Média Anual de Preço
st.subheader('Média Anual de Preço do Petróleo Brent')
plt.figure(figsize=(12, 6))
media_por_ano.plot(kind='bar', color='lightblue', edgecolor='black')
plt.xlabel('Ano')
plt.ylabel('Preço Médio (US$)')
plt.title('Média Anual de Preço do Petróleo Brent')
plt.grid(True, linestyle='--', alpha=0.5)
plt.xticks(rotation=45)
st.pyplot(plt)
