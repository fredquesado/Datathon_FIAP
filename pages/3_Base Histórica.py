import streamlit as st
import ipeadatapy as ipea
import pandas as pd
import numpy as np
import ipeadatapy as ip
import matplotlib.pyplot as plt
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import yfinance as yf
import datetime
import plotly.graph_objects as go

st.title('Análise base histórica')

# Criação das abas
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(['Gráfico Inicial',"Valor x Ano", "Picos de Aumento e Diminuição", "Métricas Estatísticas dos Preços do Petróleo", "Histograma de Preço Médio Anual","Relação com Dólar"])
with tab1:
    st.markdown("""
    Gráfico do preço do petróleo Brent ao longo dos anos
    """)
    

    # Listagem das séries disponíveis no IPEA
    df = ipea.list_series()
    data = ipea.timeseries('EIA366_PBRENT366')

    # Adiciona slider para selecionar o período do gráfico
    anos = data['YEAR'].unique()
    ano_inicio1, ano_fim1 = st.slider(
        'Selecione o período',
        min_value=int(anos.min()),
        max_value=int(anos.max()),
        value=(int(anos.min()), int(anos.max())),
        key='slider1'
    )

    # Filtrar os dados com base no período selecionado
    dados_filtrados = data[(data['YEAR'] >= ano_inicio1) & (data['YEAR'] <= ano_fim1)]
    
    # Plotar gráfico de dispersão usando matplotlib
    fig0, ax = plt.subplots()
    graf1 =ax.plot(dados_filtrados.index, dados_filtrados['VALUE (US$)'], color='blue', alpha=0.6, linewidth=2)

    ax.set_xlabel('Ano')
    ax.set_ylabel('Valor (US$)')
    ax.set_title('Gráfico de Dispersão: ANO vs VALOR')
    ax.grid(True, linestyle='--', alpha=0.6)

    # Ajustar layout para evitar sobreposição
    fig0.tight_layout()
    
    # Exibir o gráfico no Streamlit
    st.pyplot(fig0)

    st.markdown("""
    Explore a montanha-russa do mercado através deste gráfico dinâmico! Ele mostra a trajetória de um valor em dólares de 1988 a 2024, destacando momentos de ascensão meteórica e quedas abruptas. Veja como o valor dispara para alturas vertiginosas em 2008 e 2012, testemunhando a volatilidade do mercado que cativa e desafia investidores. Acompanhe essa jornada empolgante de altos e baixos que oferece insights cruciais sobre as complexidades do mundo financeiro. Ideal para quem busca entender as forças que moldam nossas economias e oportunidades de investimento!
    """)
    
# Conteúdo da aba "Valor x Ano"
with tab2:
    st.markdown("""
    Este gráfico de dispersão revela uma fascinante relação entre os anos e os valores em dólares americanos (US\$), oferecendo uma visão intrigante sobre tendências e flutuações econômicas ao longo do tempo. Aqui estão os pontos mais interessantes:
    """)
    
    col1, col2 = st.columns([1, 2])  # Dividir a aba em duas colunas, com a segunda coluna maior

    with col1:
        with st.expander("Linha do Tempo Econômica"):
            st.markdown("""
            O eixo horizontal do gráfico representa uma linha do tempo, mostrando como os valores variaram ao longo dos anos. É como se estivéssemos olhando para uma história financeira se desdobrando diante de nossos olhos.
            """)
        with st.expander("Valores em Alta e Baixa"):
            st.markdown("""
            O eixo vertical exibe valores que variam de aproximadamente 20(US\$) a 140(US\$). Essa ampla faixa sugere um mercado dinâmico, repleto de altos e baixos emocionantes.
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
        data = ipea.timeseries('EIA366_PBRENT366')

        # Adiciona slider para selecionar o período do gráfico
        anos = data['YEAR'].unique()
        ano_inicio, ano_fim = st.slider(
            'Selecione o período',
            min_value=int(anos.min()),
            max_value=int(anos.max()),
            value=(int(anos.min()), int(anos.max()))
        )

        # Filtrar os dados com base no período selecionado
        dados_filtrados = data[(data['YEAR'] >= ano_inicio) & (data['YEAR'] <= ano_fim)]
        
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

# Conteúdo da aba "Picos de Aumento e Diminuição"
with tab3:
    st.markdown("""
    O gráfico ilustra a fascinante evolução dos preços ao longo de várias décadas, destacando momentos marcantes de aumentos e quedas abruptas. 
    Este gráfico oferece uma janela para o passado, ajudando-nos a entender como eventos globais moldam os preços e, consequentemente, a economia. Ele também nos dá uma perspectiva valiosa para prever futuras tendências, preparando-nos para navegar pelas inevitáveis flutuações do mercado.
    """)
    col1, col2 = st.columns([1, 2])  # Dividir a aba em duas colunas, com a segunda coluna maior
    with col1:
        with st.expander("Evolução dos Preços"):
             st.markdown("""Desde 1988, os preços mostraram uma trajetória cheia de altos e baixos. Notamos uma ascensão constante até 2008, seguida por uma queda drástica. Esse padrão se repete em outras ocasiões, refletindo a volatilidade inerente ao mercado.
                         """)
        st.markdown('<h1 style="font-family:Arial; font-size:20px; color:Back;">Picos Memoráveis:</h1>', unsafe_allow_html=True)
        with st.expander("2008 - O Grande Salto"):
             st.markdown("""Ponto Verde: Em 2008, os preços atingiram um ápice impressionante de aproximadamente 140 US\$. Esse pico coincide com a crise financeira global, marcada pela bolha imobiliária e a subsequente recessão. Foi um período de grande incerteza econômica que inflacionou os preços de maneira significativa.
                         """)    
        with st.expander("1998 - A Grande Queda"):
             st.markdown("""Ponto Vermelho: O gráfico destaca uma queda acentuada em 1998, onde os preços despencaram para cerca de 10 US\$. Este período pode estar associado a crises econômicas regionais ou outros eventos adversos que afetaram drasticamente o mercado.
                         """)     
        with st.expander("2020 - Impacto da Pandemia"):
             st.markdown("""Outro Ponto Vermelho: Em 2020, os preços caíram novamente, refletindo o impacto severo da pandemia de COVID-19. A pandemia trouxe uma desaceleração econômica global, afetando todos os setores de maneira significativa.
                         """)  
    with col2: 
        with st.expander("Cores - Gráfico"):
             st.markdown(""" - Azul: Representa a linha do preço ao longo do tempo.""")
             st.markdown(""" - Verde: Indica os maiores picos de aumento.""")
             st.markdown(""" - Vermelho: Sinaliza os maiores picos de diminuição.""")

        # Obter os dados
        data = ipea.timeseries('EIA366_PBRENT366')

        # Resetar o índice para usar a coluna de datas
        data = data.reset_index()

        # Certificar que a coluna 'DATE' está no formato de datetime
        data['DATE'] = pd.to_datetime(data['DATE'])

        # Ordenar os dados por data
        data = data.sort_values(by='DATE')

        # Extrair valores e datas
        values = data['VALUE (US$)'].values
        dates = data['DATE'].values

        # Identificar picos de alta e baixa
        picos_aumento_indices = np.argwhere((values > np.roll(values, 1)) & (values > np.roll(values, -1))).flatten()
        picos_diminuicao_indices = np.argwhere((values < np.roll(values, 1)) & (values < np.roll(values, -1))).flatten()

        # Selecionar os 3 maiores picos de aumento
        top_3_increase_indices = picos_aumento_indices[np.argsort(values[picos_aumento_indices])[-3:]]

        # Selecionar os 3 maiores picos de diminuição
        top_3_decrease_indices = picos_diminuicao_indices[np.argsort(values[picos_diminuicao_indices])[:3]]

        # Extrair os anos correspondentes aos picos de aumento e diminuição
        years = data['DATE'].dt.year.values

        # Selecionar os anos dos 3 maiores picos de aumento
        top_3_increase_years = years[top_3_increase_indices]

        # Selecionar os anos dos 3 maiores picos de diminuição
        top_3_decrease_years = years[top_3_decrease_indices]

        # Plotar gráfico de linha
        fig2, ax2 = plt.subplots(figsize=(14, 7))
        ax2.plot(data['DATE'], data['VALUE (US$)'], label='Preço (US$)', color='blue')

        # Destaque para os 3 maiores picos de aumento
        ax2.scatter(dates[top_3_increase_indices], values[top_3_increase_indices], color='green', s=100, label='Maiores Picos de Aumento', zorder=5)
        for i, txt in enumerate(top_3_increase_years):
            ax2.annotate(txt, (dates[top_3_increase_indices[i]], values[top_3_increase_indices[i]]), xytext=(-20, 10), textcoords='offset points', fontsize=10, color='green')

        # Destaque para os 3 maiores picos de diminuição
        ax2.scatter(dates[top_3_decrease_indices], values[top_3_decrease_indices], color='red', s=100, label='Maiores Picos de Diminuição', zorder=5)
        for i, txt in enumerate(top_3_decrease_years):
            ax2.annotate(txt, (dates[top_3_decrease_indices[i]], values[top_3_decrease_indices[i]]), xytext=(-20, -20), textcoords='offset points', fontsize=10, color='red')

        # Adicionar rótulos e título
        ax2.set_xlabel('Data')
        ax2.set_ylabel('Valor (US$)')
        ax2.set_title('Evolução do Preço ao Longo do Tempo com Destaque nos Maiores Picos')
        ax2.legend()
        ax2.grid(True)

        # Exibir o gráfico no Streamlit
        st.pyplot(fig2)

    st.markdown('<h1 style="font-family:Arial; font-size:20px; color:Back;">Tendências e Recuperação</h1>', unsafe_allow_html=True)
    st.markdown('<h1 style="font-family:Arial; font-size:15px; color:Back;">Volatilidade:</h1>', unsafe_allow_html=True)        
    st.markdown("""
    O gráfico é um testemunho da natureza volátil dos preços ao longo das décadas. As flutuações são comuns, com períodos de aumentos rápidos seguidos por quedas abruptas.
    """)
    st.markdown('<h1 style="font-family:Arial; font-size:15px; color:Back;">Resiliência:</h1>', unsafe_allow_html=True)        
    st.markdown("""
    Após cada grande queda, os preços demonstram uma notável capacidade de recuperação, embora o caminho de volta seja irregular. Essa resiliência pode ser atribuída a políticas econômicas eficazes, recuperação do mercado e adaptações estratégicas.
    """)

# Conteúdo da aba "Métricas Estatísticas dos Preços do Petróleo"
with tab4:
    st.markdown('<h1 style="font-family:Arial; font-size:20px; color:Black;">Análises de tendências </h1>', unsafe_allow_html=True)
    st.markdown("""
            A análise dessas métricas revela um mercado de petróleo em constante movimento, com momentos de calmaria e tempestades financeiras. A média de 53.1105 dólares serve como um farol, guiando-nos através de um oceano de incertezas. O alto desvio padrão nos lembra das ondas gigantes de volatilidade que desafiam até os navegadores mais experientes.
            Os extremos de 9.1 e 143.95 dólares pintam um quadro de picos vertiginosos e vales profundos, cada um contando uma história de crises e booms. Os percentis e a mediana nos fornecem uma janela para a distribuição dos preços, revelando que, frequentemente, o mercado se move entre marés altas e baixas.
            A moda de 18.48 dólares surge como uma ilha comum, um preço onde o mercado frequentemente ancorou. Já o coeficiente de variação de 62.54% encapsula a essência de um mercado turbulento e imprevisível, onde a estabilidade é raramente alcançada.
            Em resumo, esta tabela não é apenas uma coleção de números frios, mas uma narrativa viva e palpitante das forças econômicas e geopolíticas que moldam o mercado global de petróleo. Ela conta histórias de glória e desespero, de desafios e resiliência, revelando a verdadeira natureza deste mercado fascinante.
    """) 
    
    col1, col2 = st.columns([1, 1])  # Dividir a aba em duas colunas iguais
    
    with col1:
        st.markdown('<h1 style="font-family:Arial; font-size:15px; color:Black;">Maiores Médias Anuais dos Preços do Petróleo</h1>', unsafe_allow_html=True)

    with col1:
        with st.expander("1º Lugar (2012)"):
             st.markdown("""O ano de 2012 registrou a maior média anual dos preços do petróleo, com um valor de 111.706880 dólares. Esse período provavelmente foi marcado por fatores como alta demanda global, tensões geopolíticas, ou restrições na oferta que impulsionaram os preços para cima.
        """)
    with col1:
        with st.expander("2º Lugar (2011)"):
             st.markdown("""Com uma média de 111.285552 dólares, o ano de 2011 também viu preços elevados do petróleo. Este valor próximo ao de 2012 sugere que esses dois anos foram bastante similares em termos de condições de mercado.
        """)  
    with col1:
        with st.expander("3º Lugar (2013)"):
             st.markdown("""Em 2013, a média anual foi de 108.573697 dólares. Embora ligeiramente inferior aos anos anteriores, esse valor ainda indica um período de preços altos, possivelmente devido à continuidade de fatores de oferta e demanda similares aos de 2011 e 2012.
        """)            
    with col2:
        st.markdown('<h1 style="font-family:Arial; font-size:15px; color:Black;">Menores Médias Anuais dos Preços do Petróleo</h1>', unsafe_allow_html=True)

    with col2:
        with st.expander("Último Lugar (1998)"):
             st.markdown("""O ano de 1998 registrou a menor média anual dos preços do petróleo, com um valor de 12.758103 dólares. Este preço extremamente baixo pode ser atribuído a uma combinação de crises econômicas, aumento da produção, ou redução na demanda.
        """)  
    with col2:
        with st.expander("Penúltimo Lugar (1988)"):
             st.markdown("""Em 1988, a média anual dos preços do petróleo foi de 14.905412 dólares. Este ano também foi caracterizado por preços baixos, indicando um período de estabilidade ou excesso de oferta.
        """)   
    with col2:
        with st.expander("Antepenúltimo Lugar (1994)"):
             st.markdown("""O ano de 1994 teve uma média anual de 15.856389 dólares. Como nos anos anteriores, este valor sugere um mercado onde a oferta superou a demanda, mantendo os preços relativamente baixos.
        """)    
    st.markdown('<h1 style="font-family:Arial; font-size:20px; color:Black;">Análise métricas</h1>', unsafe_allow_html=True)
    st.markdown("""
            A tabela revela um contraste marcante entre os anos de maiores e menores médias dos preços do petróleo. Entre 2011 e 2013, os preços foram excepcionalmente altos, refletindo um período de tensões geopolíticas e forte demanda global. Esses anos são destacados por médias que ultrapassam os 100 dólares por barril, indicando uma era de preços robustos no mercado de petróleo.
            Por outro lado, os anos de 1998, 1988, e 1994 mostram um cenário de preços muito mais baixos, com médias anuais que variam entre aproximadamente 12.75 e 15.85 dólares. Esses valores baixos podem ser atribuídos a uma combinação de fatores como crises econômicas, aumento da produção de petróleo, e menor demanda global.
            Em suma, a tabela não apenas nos apresenta uma coleção de números, mas uma narrativa dinâmica das forças que moldaram o mercado global de petróleo ao longo das décadas. Ela destaca períodos de prosperidade e dificuldade, oferecendo uma visão clara sobre a volatilidade e a complexidade do mercado de petróleo.
    """) 

# Conteúdo da aba "Histograma de Preço Médio Anual"
with tab5:
    st.markdown('<h1 style="font-family:Arial; font-size:15px; color:Black;">Histograma de Preço Médio Anual de Petróleo Brent</h1>', unsafe_allow_html=True)

    col1, col2 = st.columns([1, 1])  # Dividir a aba em duas colunas iguais
    
    with col1:
        with st.expander("Concentração de Preços Baixos"):
             st.markdown("""A maior frequência de preços médios anuais está no intervalo de aproximadamente 10 a 30 dólares (US\$). Isso indica que, ao longo do tempo, houve muitos anos em que o preço médio do petróleo Brent foi relativamente baixo.
                        Especificamente, vemos que cerca de 12 anos registraram preços médios anuais nessa faixa, destacando uma tendência histórica de preços mais baixos em diversas ocasiões.
        """)
    with col1:
        with st.expander("Distribuição Bimodal"):
             st.markdown("""O histograma apresenta uma distribuição bimodal, com duas concentrações significativas de dados: uma nos preços baixos e outra em faixas mais altas. Isso sugere que o mercado de petróleo Brent experimenta frequentes transições entre períodos de preços baixos e altos, possivelmente devido a fatores geopolíticos e econômicos.
                        Além da concentração inicial, há picos adicionais nos intervalos de 50 a 70 dólares (US\$) e de 90 a 110 dólares (US\$).
        """)
    with col2:
        with st.expander("Intervalos com Menor Frequência"):
             st.markdown("""Existe uma lacuna notável nos preços médios entre 30 e 50 dólares (US\$), onde poucos anos registraram preços médios dentro desse intervalo. Isso pode indicar que as flutuações do mercado tendem a evitar essa faixa de preços ou que eventos econômicos significativos frequentemente empurram os preços para fora dessa faixa.
        """)
    with col2:
        with st.expander("Picos em Faixas Específicas"):
             st.markdown("""Os picos notáveis nos intervalos de 50 a 70 dólares (US\$) e de 90 a 110 dólares (US\$), cada um com aproximadamente 3 a 4 anos de ocorrência, sugerem períodos específicos onde fatores econômicos e geopolíticos causaram elevações significativas nos preços do petróleo Brent.
        """)
    
    # Supondo que 'data' já esteja carregado e seja um DataFrame
    # Calcular a média de cada ano
    media_por_ano = data.groupby(data['YEAR'])['VALUE (US$)'].mean()

    # Criar o gráfico de histograma
    fig3, ax3 = plt.subplots(figsize=(10, 6))
    ax3.hist(media_por_ano, bins=10, color='lightblue', edgecolor='black')
    ax3.set_xlabel('Preço Médio (US$)')
    ax3.set_ylabel('Frequência')
    ax3.set_title('Histograma de Preço Médio Anual de Petróleo Brent')
    ax3.grid(True, linestyle='--', alpha=0.5)
    fig3.tight_layout()
    
    # Exibir o gráfico no Streamlit
    st.pyplot(fig3)
   
   # Conteúdo da aba "Histograma de Preço Médio Anual"
    
    st.markdown('<h1 style="font-family:Arial; font-size:15px; color:Black;">Gráfico de Barras da Média Anual de Preço do Petróleo Brent</h1>', unsafe_allow_html=True)

    col1, col2 = st.columns([1, 1])  # Dividir a aba em duas colunas iguais
    
    with col1:
        with st.expander("Tendência de Alta ao Longo dos Anos"):
             st.markdown("""O gráfico de barras revela uma clara tendência de alta nos preços médios anuais do petróleo Brent ao longo dos anos. Desde os valores baixos no final da década de 1980 e início da década de 1990, há um aumento gradual até o início dos anos 2000.
            Esse crescimento reflete a crescente demanda global por petróleo, bem como a influência de eventos geopolíticos e econômicos que afetaram a oferta.
        """) 
    with col1:
        with st.expander("Picos Máximos em 2008 e 2011-2013"):
             st.markdown("""Observa-se um pico significativo em 2008, onde os preços médios anuais ultrapassaram 100 dólares (US\$), coincidindo com a crise financeira global. Após uma breve queda, os preços voltaram a subir e atingiram novos picos entre 2011 e 2013, marcando um período de alta volatilidade e preços elevados no mercado de petróleo.
            Esses picos podem ser associados a tensões geopolíticas, alta demanda e restrições na oferta.
        """) 
    with col2:
        with st.expander("Queda e Recuperação Pós-2014"):
             st.markdown("""Após 2014, há uma queda acentuada nos preços, refletindo uma mudança no mercado global de petróleo, possivelmente devido ao aumento da produção de petróleo de xisto nos EUA e uma diminuição da demanda global.
            No entanto, observa-se uma recuperação gradual nos anos subsequentes, embora com flutuações significativas, destacando a resiliência e a volatilidade do mercado de petróleo.
        """) 
    with col2:
        with st.expander("Impacto da Pandemia de COVID-19 em 2020"):
             st.markdown("""Em 2020, os preços caíram novamente, refletindo o impacto severo da pandemia de COVID-19. A desaceleração econômica global afetou todos os setores de maneira significativa, levando a uma queda nos preços do petróleo.
        """) 
    # Calcular a média de cada ano e criar o gráfico de barras
    fig4, ax4 = plt.subplots(figsize=(12, 6))
    media_por_ano.plot(kind='bar', color='lightblue', edgecolor='black', ax=ax4)
    ax4.set_xlabel('Ano')
    ax4.set_ylabel('Preço Médio (US$)')
    ax4.set_title('Média Anual de Preço do Petróleo Brent')
    ax4.grid(True, linestyle='--', alpha=0.5)
    plt.xticks(rotation=45)
    fig4.tight_layout()
    
    # Exibir o gráfico de barras no Streamlit
    st.pyplot(fig4)
    
    st.markdown('<h1 style="font-family:Arial; font-size:15px; color:Black;">Analise Geral</h1>', unsafe_allow_html=True)
    st.markdown("""Após 2014, há uma queda acentuada nos preços, refletindo uma mudança no mercado global de petróleo, possivelmente devido ao aumento da produção de petróleo de xisto nos EUA e uma diminuição da demanda global.
            Os gráficos fornecem uma visão abrangente da dinâmica dos preços do petróleo Brent ao longo das últimas décadas. O histograma destaca a predominância de preços mais baixos, enquanto o gráfico de barras ilustra a tendência geral de aumento com picos e quedas significativas. Esses gráficos juntos revelam a natureza volátil e influenciada por múltiplos fatores do mercado de petróleo, refletindo as complexas interações entre oferta, demanda, eventos geopolíticos e crises econômicas globais.
    """)
with tab6:
    st.markdown('Foi investigado aqui uma relação entre o preço do petróleo Brent e o preço do dólar, uma vez que o petróleo é cotado em dólares no mercado internacional. Quando o dólar se valoriza, o preço do petróleo tende a cair, pois se torna mais caro em outras moedas, reduzindo a demanda global. Por outro lado, quando o dólar se desvaloriza, o preço do petróleo geralmente sobe, tornando-o mais acessível internacionalmente e aumentando a demanda. Essa dinâmica reflete a sensibilidade do mercado de petróleo às flutuações cambiais e à interdependência entre commodities e moedas. ')

    st.markdown('Para investigar essa relação, utilizou-se o USDX. O USDX, ou Índice do Dólar dos Estados Unidos, é uma medida do valor do dólar norte-americano em relação a uma cesta de seis principais moedas estrangeiras: euro, iene japonês, libra esterlina, dólar canadense, coroa sueca e franco suíço. Ele oferece uma visão abrangente da força do dólar no mercado global. Utilizar o USDX para investigar a relação entre o preço do petróleo Brent e o preço do dólar é eficaz porque captura as variações do dólar em um contexto amplo.')

    st.markdown('Utilizando-se a biblioteca do Yahoo Finance, obteve-se os dados do USDX para as mesmas datas contidas na database do Ipea, onde se construiu um gráfico e calculou-se a correlação:')
    series = ip.list_series()
    data = ip.timeseries('EIA366_PBRENT366')
    data = data[["VALUE (US$)"]]
    data.rename(columns={"VALUE (US$)": "Price"}, inplace=True)
    data.index.name = "date"
    data = data.dropna()
    data.index = pd.to_datetime(data.index)
    
    # Define the date range based on your existing DataFrame
    start_date = data.index.min()
    end_date = data.index.max()

    # Fetch USDX data from Yahoo Finance
    usdx = yf.download('DX-Y.NYB', start=start_date, end=end_date)

    # Select and rename relevant columns
    usdx = usdx[['Close']]
    usdx.rename(columns={'Close': 'USDX'}, inplace=True)

    # Join the data
    combined_data = data.join(usdx, how='inner')

    # Handle any missing data (if necessary)
    combined_data.dropna(inplace=True)

    # Create traces for Brent Price and USDX
    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=combined_data.index,
            y=combined_data['Price'],
            name='Brent Price',
            line=dict(color='red'),
            yaxis='y1'
        )
    )

    fig.add_trace(
        go.Scatter(
            x=combined_data.index,
            y=combined_data['USDX'],
            name='USDX',
            line=dict(color='blue'),
            yaxis='y2'
        )
    )

    # Create a layout with two y-axes
    fig.update_layout(
        title='Preço do Petroleo Brent vs. USDX',
        xaxis=dict(title='Date'),
        yaxis=dict(
            title='Brent Price',
            titlefont=dict(color='red'),
            tickfont=dict(color='red')
        ),
        yaxis2=dict(
            title='USDX',
            titlefont=dict(color='blue'),
            tickfont=dict(color='blue'),
            anchor='x',
            overlaying='y',
            side='right'
        ),
        legend=dict(
            x=0.1,
            y=0.9
        )
    )

    # Show the plot in Streamlit
    st.plotly_chart(fig)
    correlation = combined_data['USDX'].corr(combined_data['Price'])
    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        st.metric(label="Correlação Observada", value=round(correlation, 2))

    st.markdown('Observa-se uma correlação negativa, que é relevante mas não extremamente alta, pois existem outros fatores globais que influenciam nesse preço, como demanda, fatores geopoliticos, etc.')
