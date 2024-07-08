import streamlit as st
import ipeadatapy as ipea
import pandas as pd
import matplotlib.pyplot as plt

st.title('Análise base histórica')

# Criação das abas
tab1, tab2, tab3 = st.tabs(["Valor x Ano", "Refazer 1", "Refazer 2"])


# Conteúdo da aba "Valor x Ano"
with tab1:
    
    st.markdown("""
    # Valor x Ano - Base Histórica
    Este gráfico de dispersão revela uma fascinante relação entre os anos e os valores em dólares americanos (US$), oferecendo uma visão intrigante sobre tendências e flutuações econômicas ao longo do tempo. Aqui estão os pontos mais interessantes:
    """)
    col1, col2 = st.columns([1, 2])  # Dividir a aba em duas colunas, com a segunda coluna maior

    with col1:
        with st.expander("Linha do Tempo Econômica"):
            st.markdown("""
            O eixo horizontal do gráfico representa uma linha do tempo, mostrando como os valores variaram ao longo dos anos. É como se estivéssemos olhando para uma história financeira se desdobrando diante de nossos olhos.
            """)
        with st.expander("Valores em Alta e Baixa"):
            st.markdown("""
            O eixo vertical exibe valores que variam de aproximadamente 20(US$) a 140(US$). Essa ampla faixa sugere um mercado dinâmico, repleto de altos e baixos emocionantes.
            """)
        with st.expander("Padrões de Distribuição"):
            st.markdown("""
            A dispersão dos pontos azuis destaca períodos de estabilidade e volatilidade. Em alguns anos, os valores são muito próximos uns dos outros, indicando estabilidade. Em outros, há uma dispersão maior, sugerindo incerteza e variação.
            """)
        with st.expander("Tendências Notáveis"):
            st.markdown("""
            Observa-se um aumento gradual e consistente nos valores ao longo do tempo, pontuado por picos impressionantes em certos anos. Esses picos podem estar ligados a eventos econômicos importantes, mudanças no mercado ou outras influências significativas.
            """)
        with st.expander("Concentração de Valores"):
            st.markdown("""
            A sobreposição de pontos em certas áreas sugere que muitos registros compartilham valores semelhantes em determinados períodos. Isso pode indicar fases de estabilidade ou momentos em que o mercado encontrou um equilíbrio.
            """)

    with col2:
        # Listagem das séries disponíveis no IPEA
        df = ipea.list_series()
        babacu = ipea.timeseries('EIA366_PBRENT366')

        # Adiciona slider para selecionar o período do gráfico
        anos = babacu['YEAR'].unique()
        ano_inicio, ano_fim = st.slider(
            'Selecione o período',
            min_value=int(anos.min()),
            max_value=int(anos.max()),
            value=(int(anos.min()), int(anos.max()))
        )

        # Filtrar os dados com base no período selecionado
        dados_filtrados = babacu[(babacu['YEAR'] >= ano_inicio) & (babacu['YEAR'] <= ano_fim)]
        
        # Plotar gráfico de dispersão usando matplotlib
        fig, ax = plt.subplots()
        scatter = ax.scatter(dados_filtrados['YEAR'], dados_filtrados['VALUE (US$)'], c='blue', alpha=0.6, edgecolors='w', s=100)

        ax.set_xlabel('Ano')
        ax.set_ylabel('Valor (US$)')
        ax.set_title('Gráfico de Dispersão: ANO vs VALOR')
        ax.grid(True, linestyle='--', alpha=0.6)

        # Ajustar layout para evitar sobreposição
        fig.tight_layout()
        
        # Exibir o gráfico no Streamlit
        st.pyplot(fig)

    st.markdown("""
    Em resumo, este gráfico não apenas mostra números, mas conta uma história rica e dinâmica sobre a evolução dos valores ao longo do tempo. Ele nos oferece uma janela para entender as forças que moldam os mercados e a economia, destacando momentos de crescimento, estabilidade e transformação.
    """)

# Conteúdo das abas "Refazer 1" e "Refazer 2" pode ser adicionado conforme necessário
with tab2:
    st.write("Conteúdo para Refazer 1")

with tab3:
    st.write("Conteúdo para Refazer 2")
