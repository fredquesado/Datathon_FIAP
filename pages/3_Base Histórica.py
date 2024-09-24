import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

# Título do aplicativo
st.title("Análise de Performance - ONG Passos Mágicos")

# Caminho do arquivo
file_path = "/workspaces/Fiap_Datathon/Arquivos/PEDE_PASSOS_DATASET_FIAP.csv"

# Usando bloco try para evitar erro de arquivo
try:
    df = pd.read_csv(file_path, sep=';')

    # Renomeando as colunas com base nos indicadores de performance
    df = df.rename(columns={
        'ANOS_PM_2020': 'AnosNaONG_2020',  
        'INDE_2020': 'Desempenho_2020', 
        'INDE_2021': 'Desempenho_2021', 
        'INDE_2022': 'Desempenho_2022',
        'IEG_2020': 'Engajamento_2020', 
        'IEG_2021': 'Engajamento_2021',
        'IEG_2022': 'Engajamento_2022',
        'IDA_2020': 'Aprendizagem_2020',  
        'IDA_2021': 'Aprendizagem_2021',
        'IDA_2022': 'Aprendizagem_2022',
        'IAA_2020': 'Autoavaliacao_2020',  
        'IAA_2021': 'Autoavaliacao_2021',
        'IAA_2022': 'Autoavaliacao_2022',
        'IPS_2020': 'Psicossocial_2020',
        'IPS_2021': 'Psicossocial_2021',
        'IPS_2022': 'Psicossocial_2022',
        'IPP_2020': 'Psicopedagogico_2020',
        'IPP_2021': 'Psicopedagogico_2021',
        'IPP_2022': 'Psicopedagogico_2022',
        'IPV_2020': 'PontoDeVirada_2020',
        'IPV_2021': 'PontoDeVirada_2021',
        'IPV_2022': 'PontoDeVirada_2022',
        'IAN_2020': 'AdequaçãoDeNivel_2020',
        'IAN_2021': 'AdequaçãoDeNivel_2021',
        'IAN_2022': 'AdequaçãoDeNivel_2022',
        'IDADE_ALUNO_2020': 'Idade'
    })

    # Definindo os anos disponíveis
    anos = [2020, 2021, 2022]

    # Garantir que as colunas sejam numéricas e remover valores ausentes
    indicadores = [
        'Desempenho_2020', 'Desempenho_2021', 'Desempenho_2022', 
        'Engajamento_2020', 'Engajamento_2021', 'Engajamento_2022',
        'Aprendizagem_2020', 'Aprendizagem_2021', 'Aprendizagem_2022',
        'Autoavaliacao_2020', 'Autoavaliacao_2021', 'Autoavaliacao_2022',
        'Psicossocial_2020', 'Psicossocial_2021', 'Psicossocial_2022',
        'Psicopedagogico_2020', 'Psicopedagogico_2021', 'Psicopedagogico_2022',
        'PontoDeVirada_2020', 'PontoDeVirada_2021', 'PontoDeVirada_2022',
        'AdequaçãoDeNivel_2020', 'AdequaçãoDeNivel_2021', 'AdequaçãoDeNivel_2022'
    ]

    for indicador in indicadores:
        df[indicador] = pd.to_numeric(df[indicador], errors='coerce')

    # Função para plotar a matriz de correlação triangular
    def plotar_matriz_triangular(correlacao, titulo):
        mask = np.triu(np.ones_like(correlacao, dtype=bool))  # Criar máscara para a parte superior
        plt.figure(figsize=(10, 8))
        sns.heatmap(correlacao, mask=mask, annot=True, fmt=".2f", cmap='coolwarm', square=True, cbar_kws={"shrink": .8})
        plt.title(titulo)
        st.pyplot(plt)

    # Aba para introdução e storytelling
    introducao, tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "Introdução e Storytelling", "Evolução de Desempenho", 
        "Comparação entre Indicadores", "Correlação entre Indicadores", "Matriz de Correlação por Grupos", "Predição"
    ])

        ### Introdução e Storytelling ###
    with introducao:
        st.header("Storytelling - Impacto da ONG Passos Mágicos")
        st.markdown("""
        A ONG Passos Mágicos tem como missão melhorar o desempenho educacional de crianças e adolescentes por meio de atividades de engajamento e autoavaliação. 
        Este painel apresenta uma análise detalhada dos dados para entender como as ações da ONG têm impactado o desempenho ao longo dos anos.
        
        **História Contada pelos Dados:**
        - **Desempenho**: Observamos um crescimento contínuo no Índice de Desenvolvimento Educacional (INDE) nos últimos três anos.
        - **Engajamento**: Alunos mais jovens tendem a apresentar maior engajamento nas atividades, especialmente nas faixas etárias abaixo de 15 anos.
        - **Autoavaliação e Aprendizagem**: A autoavaliação dos alunos está alinhada com seus resultados de aprendizado, indicando uma boa consciência sobre seu desempenho.
        
        Selecione as abas para explorar mais insights.
        """)

        ### Aba 1: Evolução de Desempenho ###
    with tab1:
        st.subheader("Evolução do Desempenho ao Longo dos Anos")
        st.markdown("""
        A análise da visão do gráfico sugere que o desempenho médio dos alunos, representado pelo Índice de Desenvolvimento Educacional (INDE), apresentou uma tendência de queda entre os anos de 2020 e 2021, mas houve uma recuperação em 2022.
        """)

        # Gráfico de linha interativo para evolução do desempenho com hover detalhado
        data_grafico = df[['Desempenho_2020', 'Desempenho_2021', 'Desempenho_2022']].mean().reset_index()
        data_grafico.columns = ['Ano', 'Desempenho Médio']
        fig_desempenho = px.line(data_grafico, x='Ano', y='Desempenho Médio', 
                                 title="Evolução do Desempenho Médio (INDE)",
                                 labels={'Ano': 'Ano', 'Desempenho Médio': 'Desempenho Médio'},
                                 hover_data=['Desempenho Médio'])
        st.plotly_chart(fig_desempenho)
        
        st.markdown("""
        **Aqui estão alguns pontos importantes observados no gráfico:**
        - **Declínio entre 2020 e 2021:** O desempenho médio dos alunos caiu significativamente entre 2020 e 2021, conforme indicado pela linha descendente. Isso pode ser reflexo de desafios que os alunos enfrentaram nesse período, como a adaptação a novas metodologias de ensino ou outros fatores que afetaram a performance.
        - **Recuperação em 2022:** Em 2022, há uma recuperação no desempenho médio. A linha ascendente sugere que, após o período de queda, medidas foram tomadas que impactaram positivamente o desempenho dos alunos, como melhorias em estratégias pedagógicas ou maior engajamento nas atividades da ONG.
        - **Tendência Geral:** Embora haja essa recuperação em 2022, o desempenho médio ainda não alcançou os níveis de 2020. Isso pode indicar que o impacto negativo observado em 2021 não foi completamente revertido, e que é necessário continuar focando em estratégias que possam trazer o desempenho de volta ao nível mais alto de 2020.
        """)
    ### Aba 2: Comparação entre Desempenho, Engajamento, Aprendizagem e Autoavaliação ###
    with tab2:
        st.subheader("Comparação entre Desempenho, Engajamento, Aprendizagem e Autoavaliação")
        st.markdown("""
        A análise dos dados da ONG Passos Mágicos revela uma história interessante sobre a jornada dos alunos ao longo dos últimos três anos, trazendo à tona o impacto das atividades de engajamento, aprendizado e autoavaliação. Vamos explorar mais detalhadamente os principais aspectos observados no gráfico e o que isso pode nos dizer sobre a evolução dos alunos.
        """)

        st.markdown("""
        **Selecione os indicadores e anos para comparar seu desempenho.**
        """)

        # Filtros de múltipla seleção para os indicadores e anos
        indicadores_selecionados = st.multiselect(
            '**Selecione os Indicadores**',
            ['Autoavaliacao', 'Engajamento', 'Aprendizagem', 'Psicossocial', 'Psicopedagogico', 'PontoDeVirada', 'AdequaçãoDeNivel'],
            default=['Autoavaliacao', 'Engajamento', 'Aprendizagem']
        )

        anos_selecionados = st.multiselect(
            '**Selecione os Anos**',
            [2020, 2021, 2022],
            default=[2020, 2021, 2022]
        )

        # Filtrar os dados de acordo com os indicadores e anos selecionados
        dados_para_comparacao = pd.DataFrame()

        for indicador in indicadores_selecionados:
            for ano in anos_selecionados:
                coluna_nome = f"{indicador}_{ano}"
                if coluna_nome in df.columns:
                    df_temp = df[[coluna_nome]].copy()
                    df_temp['Indicador'] = indicador
                    df_temp['Ano'] = ano
                    df_temp.rename(columns={coluna_nome: 'Valor'}, inplace=True)
                    dados_para_comparacao = pd.concat([dados_para_comparacao, df_temp])

        # Verificar se há dados suficientes para plotar
        if not dados_para_comparacao.empty:
            # Gráfico de comparação entre os indicadores e anos
            fig_comparacao = px.box(
                dados_para_comparacao,
                x='Ano',
                y='Valor',
                color='Indicador',
                title="Comparação entre Indicadores e Anos",
                labels={'Valor': 'Valor do Indicador'}
            )
            st.plotly_chart(fig_comparacao)
        else:
            st.write("Nenhum dado disponível para os filtros selecionados.")
    
        col1, col2 = st.columns([1, 1])  

        with col1:
            with st.expander("Autoavaliação"):
                st.markdown("""
            A autoavaliação dos alunos é um indicativo de como eles percebem seu próprio progresso. Em 2020, vemos uma grande variação nos resultados, com alguns alunos avaliando seu desempenho muito abaixo da média. Isso pode refletir incertezas ou dificuldades que os alunos enfrentaram nesse primeiro ano. Conforme os anos avançam, especialmente em 2021, essa variação diminui, sugerindo que os alunos começaram a se ajustar às suas rotinas e se tornaram mais conscientes de seus pontos fortes e fracos. Já em 202
            Já em 2022, observamos uma nova expansão na variação, mas com resultados médios mais elevados, sugerindo que, mesmo com uma dispersão maior, a percepção de autossuficiência e evolução se fortaleceu para a maioria.
                """)

        with col1:
            with st.expander("Engajamento"):
                st.markdown("""
            O engajamento é a alma de qualquer atividade educacional. Em 2020, os alunos demonstraram um bom nível de comprometimento, com pouca variação entre eles. Isso talvez reflita o entusiasmo inicial de se envolver com as atividades da ONG. No entanto, em 2022, percebemos uma ampliação na dispersão dos resultados. Isso pode indicar que alguns alunos estão mais conectados do que nunca, enquanto outros podem estar se distanciando, talvez devido a desafios externos ou uma necessidade de maior personalização no suporte oferecido.
                """)

        with col1:
            with st.expander("Aprendizagem"):
                st.markdown("""
            O desempenho relacionado à aprendizagem segue um padrão intrigante. Vemos uma grande variação, especialmente em 2022, onde aparecem mais outliers nos extremos inferiores. Isso pode refletir as dificuldades enfrentadas por alguns alunos, possivelmente exacerbadas por questões como a adaptação ao ensino remoto ou híbrido, se relevante. No entanto, a presença de outliers não significa que a aprendizagem foi prejudicada para todos. Pelo contrário, a mediana dos resultados indica que muitos alunos ainda conseguiram manter um desempenho sólido.
                """)

        with col2:
            with st.expander("Indicadores Psicossocial e Psicopedagógico"):
                st.markdown("""
            Esses dois indicadores revelam informações valiosas sobre o estado emocional e a capacidade de aprendizagem dos alunos. Em 2020, o bem-estar psicossocial parece ter sido mais variável, possivelmente devido à incerteza que o ano trouxe. No entanto, à medida que avançamos para 2022, vemos uma melhora considerável, com a maioria dos alunos demonstrando maior estabilidade emocional. O mesmo pode ser dito para o indicador psicopedagógico, que reflete o suporte educacional recebido. Em 2022, tanto o desempenho emocional quanto o apoio pedagógico parecem estar mais consolidados, refletindo no bem-estar geral dos alunos.
                """)

        with col2:
            with st.expander("Ponto de Virada"):
                st.markdown("""
            Este é um dos indicadores mais reveladores e inspiradores. Em 2022, muitos alunos parecem ter experimentado grandes momentos de mudança em suas trajetórias. Isso pode significar que mais alunos atingiram marcos importantes, como superação de desafios acadêmicos ou emocionais, e estão mais preparados para seguir em frente. A maior dispersão nesse ano pode ser vista como algo positivo, indicando que muitos tiveram suas "viradas" pessoais que os ajudaram a crescer.
                """)

        with col2:
            with st.expander("Adequação ao Nível"):
                st.markdown("""
            Em 2021, esse indicador mostrou uma grande variabilidade, sugerindo que muitos alunos ainda estavam lutando para encontrar seu ritmo ideal. No entanto, em 2022, vemos uma melhora significativa, com menos variação e uma mediana mais alta. Isso pode refletir um esforço coordenado da ONG em ajustar o conteúdo e o suporte oferecido aos alunos, garantindo que mais deles estivessem no caminho certo em relação ao seu nível educacional.
                """)

        st.markdown("""
        A história contada por esses dados é uma de resiliência e progresso. Embora 2020 tenha sido um ano com mais desafios e incertezas, os alunos da ONG Passos Mágicos parecem ter encontrado seu caminho, especialmente em 2022, onde observamos melhorias em quase todos os indicadores. Ainda que alguns alunos enfrentem dificuldades, especialmente em termos de engajamento e aprendizagem, os resultados mostram que a maioria está evoluindo de maneira positiva, apoiada pelas atividades e pelo suporte da ONG.
        """)

    ### Aba 3: Correlação entre Indicadores ###
    with tab3:
        st.markdown(" ### Análise da Correlação entre Indicadores")
        st.markdown("""
        A matriz de correlação mostrada no gráfico de calor nos dá uma visão profunda sobre como os diferentes indicadores de performance da ONG Passos Mágicos estão relacionados entre si. Vamos interpretar esses resultados com foco nas implicações práticas que essas correlações podem ter:
        """)

        col1, col2 = st.columns([1, 1])  

        with col1:
            with st.expander("Correlação Positiva entre Engajamento e Autoavaliação (2021-2022)"):
                st.markdown("""
            Observamos uma correlação significativa entre Engajamento e Autoavaliação. Isso sugere que os alunos que se engajam mais nas atividades da ONG tendem a se avaliar de forma mais consciente e positiva.
                """)

        with col1:
            with st.expander("Correlação entre Aprendizagem e Outros Indicadores"):
                st.markdown("""
            Há uma forte correlação entre o indicador de Aprendizagem e outros fatores como Autoavaliação e Engajamento. Isso faz sentido, já que alunos mais engajados tendem a ter melhores resultados de aprendizagem.
                """)

        with col1:
            with st.expander("Psicopedagógico e Ponto de Virada"):
                st.markdown("""
            A correlação entre os indicadores Psicopedagógico e Ponto de Virada sugere que momentos de mudança significativa estão intimamente ligados ao suporte recebido.
                """)

        with col2:
            with st.expander("Variação entre os Anos"):
                st.markdown("""
            O gráfico de calor também mostra como as correlações mudam de ano para ano. Isso pode indicar a necessidade de uma abordagem flexível.
                """)

        with col2:
            with st.expander("Adequação ao Nível e Outros Indicadores"):
                st.markdown("""
            O indicador de Adequação ao Nível também tem correlação com outros fatores, especialmente Engajamento e Autoavaliação.
                """)
        st.subheader("Correlação entre Indicadores de Performance")
        corr_df = df[indicadores].corr()
        fig_corr = px.imshow(corr_df, title="Matriz de Correlação entre Indicadores")
        st.plotly_chart(fig_corr)



    ### Aba 4: Matriz de Correlação por Grupos ###
    with tab4:
               
        st.markdown("### Análise dos Outliers")
        st.markdown("""
        **A análise de outliers separou os alunos em dois grupos: os melhores desempenhos (acima de 95%) e os alunos em desenvolvimento (abaixo de 5%).** 
        A matriz de correlação revela padrões distintos de relacionamento entre os indicadores para cada grupo. 
        Alunos com melhores desempenhos tendem a ter uma correlação mais forte entre **Ponto de Virada** e **Psicopedagógico**, sugerindo que o suporte psicológico tem um papel crucial em momentos decisivos de suas trajetórias educacionais. 
        Por outro lado, alunos em desenvolvimento mostram correlações mais fracas entre os indicadores, o que pode indicar uma necessidade de intervenções mais personalizadas para impulsionar seu progresso.
        """)

        st.markdown(" ### Análise das Matrizes de Correlação")

        col1, col2 = st.columns([1, 1])  

        with col1:
            with st.expander("Correlação entre IPP (Indicador Psicopedagógico) e IPV (Indicador de Ponto de Virada)"):
                st.markdown("""
            - **Melhores Alunos:** Há uma correlação muito forte entre o IPP (Indicador Psicopedagógico) e o IPV (Indicador de Ponto de Virada), com um valor de 0.89. Isso indica que, para os melhores alunos, uma avaliação psicopedagógica positiva está intimamente ligada a momentos de transformação significativa em seu desenvolvimento. Alunos que recebem avaliações mais altas no IPP tendem a atingir pontos de virada com mais frequência.
            - **Alunos em Desenvolvimento:** A correlação entre o IPP e o IPV é moderada nos alunos em desenvolvimento (0.37), o que sugere que, embora a avaliação psicopedagógica ainda tenha influência sobre os momentos de transformação, outros fatores podem desempenhar um papel mais importante para esse grupo.
        """)
        with col1:
            with st.expander("Correlação entre INDE (Indicador de Desenvolvimento Educacional) e IPV (Indicador de Ponto de Virada)"):
                st.markdown("""
            - **Melhores Alunos:** A correlação entre o INDE (Indicador de Desenvolvimento Educacional) e o IPV é inexistente nos melhores alunos (-0.03), indicando que, para esses alunos, o desenvolvimento educacional não está diretamente relacionado a momentos de transformação significativa. Para esse grupo, o progresso educacional já pode estar mais consolidado, e o IPV pode estar ligado a outras áreas de desenvolvimento.
            - **Alunos em Desenvolvimento:** Nos alunos em desenvolvimento, a correlação entre INDE e IPV é mais forte (0.41), sugerindo que o progresso educacional é um fator crucial para desencadear pontos de virada significativos. À medida que esses alunos progridem educacionalmente, eles tendem a experimentar momentos de transformação em seu desenvolvimento.
        """)
        with col1:
            with st.expander("Correlação entre IAA (Indicador de Autoavaliação) e IPV (Indicador de Ponto de Virada)"):
                st.markdown("""
            - **Melhores Alunos:** A correlação entre o IAA (Indicador de Autoavaliação) e o IPV é baixa (0.12), o que indica que, para os melhores alunos, a autoavaliação não tem um papel tão determinante nos momentos de transformação. Esses alunos podem já ter uma autoavaliação bem estabelecida, e o progresso em outras áreas pode estar impulsionando os pontos de virada.
            - **Alunos em Desenvolvimento:** Nos alunos em desenvolvimento, a correlação entre IAA e IPV é ligeiramente negativa (-0.11), o que pode sugerir que os alunos que se avaliam de maneira mais crítica não atingem pontos de virada tão facilmente. Para esses alunos, a autoavaliação pode ser um desafio e pode estar desacelerando o progresso percebido.
        """)
        with col2:
            with st.expander("Correlação entre IEG (Indicador de Engajamento) e INDE (Indicador de Desenvolvimento Educacional)"):
                st.markdown("""
            - **Melhores Alunos:** A correlação entre o IEG (Indicador de Engajamento) e o INDE (Indicador de Desenvolvimento Educacional) nos melhores alunos é moderada (0.38), sugerindo que o engajamento dos alunos ainda contribui para seu progresso educacional, embora outros fatores possam também estar influenciando esse desenvolvimento.
            - **Alunos em Desenvolvimento:** Nos alunos em desenvolvimento, a correlação entre IEG e INDE é mais forte (0.60), o que indica que o engajamento é um fator crucial para o progresso educacional desses alunos. Isso sugere que o envolvimento ativo nas atividades da ONG e no ambiente escolar é essencial para que esses alunos avancem em seu desenvolvimento acadêmico.
        """)
        with col2:
            with st.expander("Correlação entre IDA (Indicador de Desempenho Acadêmico) e IPS (Indicador Psicossocial)"):
                st.markdown("""
            - **Melhores Alunos:** A correlação entre IDA (Indicador de Desempenho Acadêmico) e IPS (Indicador Psicossocial) nos melhores alunos é muito fraca (0.02), indicando que, para esses alunos, o desempenho acadêmico não está diretamente relacionado à sua avaliação psicossocial. Eles podem estar em uma fase em que ambos os indicadores são importantes, mas não necessariamente se influenciam mutuamente.
            - **Alunos em Desenvolvimento:** Já nos alunos em desenvolvimento, essa correlação é mais forte (0.36), o que sugere que, para esses alunos, o desempenho acadêmico e o desenvolvimento psicossocial estão mais interligados. À medida que o desempenho acadêmico melhora, esses alunos também tendem a melhorar suas habilidades psicossociais, refletindo um progresso mais amplo.
        """)
        st.markdown("""A análise das correlações revela que o impacto do programa da ONG Passos Mágicos é mais significativo para os alunos em desenvolvimento, especialmente no que se refere ao INDE (Indicador de Desenvolvimento Educacional) e ao IPP (Indicador Psicopedagógico), que estão mais fortemente correlacionados ao IPV (Indicador de Ponto de Virada). Para esses alunos, o progresso educacional, o engajamento e a participação psicopedagógica são fatores essenciais que ajudam a desencadear pontos de transformação importantes em seu desenvolvimento.
        Nos melhores alunos, a relação entre esses indicadores é mais estabilizada, sugerindo que eles já atingiram um nível de desenvolvimento educacional e psicossocial que requer menos interdependência entre as variáveis para atingir pontos de virada. O impacto do programa, portanto, é mais direto e profundo nos alunos em desenvolvimento, que ainda estão construindo suas habilidades e precisam de mais suporte para alcançar transformações significativas.
        Essa análise confirma que o programa deve continuar a focar nas necessidades dos alunos em desenvolvimento, pois eles respondem melhor ao progresso educacional e ao engajamento pedagógico, enquanto os melhores alunos já atingem pontos de virada por outras vias.
        """)

        # Separar os anos de 2020, 2021 e 2022 em DataFrames distintos
        df_2020 = df[['Desempenho_2020', 'Autoavaliacao_2020', 'Engajamento_2020', 'Psicossocial_2020', 'Aprendizagem_2020', 'Psicopedagogico_2020', 'PontoDeVirada_2020', 'AdequaçãoDeNivel_2020']]
        df_2021 = df[['Desempenho_2021', 'Autoavaliacao_2021', 'Engajamento_2021', 'Psicossocial_2021', 'Aprendizagem_2021', 'Psicopedagogico_2021', 'PontoDeVirada_2021', 'AdequaçãoDeNivel_2021']]
        df_2022 = df[['Desempenho_2022', 'Autoavaliacao_2022', 'Engajamento_2022', 'Psicossocial_2022', 'Aprendizagem_2022', 'Psicopedagogico_2022', 'PontoDeVirada_2022', 'AdequaçãoDeNivel_2022']]

        # Função para separar os outliers
        def separar_outliers(df, coluna):
            limite_inferior = df[coluna].quantile(0.05)
            limite_superior = df[coluna].quantile(0.95)
            
            melhores = df[df[coluna] > limite_superior].sort_values(by=coluna, ascending=False).reset_index(drop=True)
            desenvolvimento = df[df[coluna] < limite_inferior].sort_values(by=coluna).reset_index(drop=True)

            return melhores, desenvolvimento

        # Aplicar a função para separar outliers para cada ano
        melhores_2020, desenvolvimento_2020 = separar_outliers(df_2020, 'Desempenho_2020')
        melhores_2021, desenvolvimento_2021 = separar_outliers(df_2021, 'Desempenho_2021')
        melhores_2022, desenvolvimento_2022 = separar_outliers(df_2022, 'Desempenho_2022')

        # Função para juntar DataFrames de melhores ou desenvolvimento
        def juntar_melhores_desenvolvimento(*dfs):
            dfs_sem_sufixo = [df.rename(columns=lambda x: x.replace('_2020', '').replace('_2021', '').replace('_2022', '')) for df in dfs]
            df_final = pd.concat(dfs_sem_sufixo, ignore_index=True)
            return df_final

        # Juntar os DataFrames de melhores e desenvolvimento
        df_melhores = juntar_melhores_desenvolvimento(melhores_2020, melhores_2021, melhores_2022)
        df_desenvolvimento = juntar_melhores_desenvolvimento(desenvolvimento_2020, desenvolvimento_2021, desenvolvimento_2022)

        # Calcular as matrizes de correlação para os melhores e desenvolvimento
        correlacao_melhores = df_melhores[['Desempenho', 'Autoavaliacao', 'Engajamento', 'Psicossocial', 'Aprendizagem', 'Psicopedagogico', 'PontoDeVirada', 'AdequaçãoDeNivel']].corr()
        correlacao_desenvolvimento = df_desenvolvimento[['Desempenho', 'Autoavaliacao', 'Engajamento', 'Psicossocial', 'Aprendizagem', 'Psicopedagogico', 'PontoDeVirada', 'AdequaçãoDeNivel']].corr()

        # Função para plotar a matriz de correlação triangular
        def plotar_matriz_triangular(correlacao, titulo):
            mask = np.triu(np.ones_like(correlacao, dtype=bool))
            plt.figure(figsize=(10, 8))
            sns.heatmap(correlacao, mask=mask, annot=True, fmt=".2f", cmap='coolwarm', square=True, cbar_kws={"shrink": .8})
            plt.title(titulo)
            st.pyplot(plt)

        # Plotar as matrizes de correlação
        plotar_matriz_triangular(correlacao_melhores, 'Matriz de Correlação - Melhores Alunos')
        plotar_matriz_triangular(correlacao_desenvolvimento, 'Matriz de Correlação - Alunos em Desenvolvimento')
    
    
    ### Aba 5: Predição ###
    with tab5:
        st.subheader("Predição do Desempenho Futuro")

    # Disponibilizar os nomes das variáveis e os anos para escolha
        variaveis_nomes = [
            'Engajamento', 'Autoavaliacao', 'Psicossocial', 
            'Aprendizagem', 'Psicopedagogico', 'PontoDeVirada', 'AdequaçãoDeNivel'
        ]
        anos_disponiveis = [2020, 2021, 2022]

    # Caixa de seleção para o usuário escolher os nomes das variáveis
        variaveis_selecionadas_nomes = st.multiselect(
        "Selecione as variáveis para o modelo preditivo (por nome)", 
        variaveis_nomes,
        default=variaveis_nomes  # Definir todas como padrão
    )

    # Caixa de seleção para o usuário escolher os anos
        anos_selecionados = st.multiselect(
        "Selecione os anos para o modelo preditivo", 
        anos_disponiveis,
        default=anos_disponiveis  # Definir todos como padrão
    )

    # Construir as variáveis com base na combinação dos nomes e anos selecionados
        variaveis_selecionadas = []
        for nome in variaveis_selecionadas_nomes:
            for ano in anos_selecionados:
                variaveis_selecionadas.append(f"{nome}_{ano}")

    # Exibir as variáveis selecionadas
        st.write(f"Variáveis selecionadas para o modelo: {', '.join(variaveis_selecionadas)}")

    # Função para preparar os dados com as variáveis selecionadas
        def preparar_dados(df, variaveis_selecionadas):
            target = 'Desempenho_2022'

        # Remover valores ausentes
            df = df.dropna(subset=variaveis_selecionadas + [target])

        # Dividir em treino e teste
            X_train, X_test, y_train, y_test = train_test_split(df[variaveis_selecionadas], df[target], test_size=0.2, random_state=42)
            return X_train, X_test, y_train, y_test

    # Função para treinar o modelo
        def treinar_modelo(X_train, y_train):
            modelo = RandomForestRegressor(random_state=42)
            modelo.fit(X_train, y_train)
            return modelo

    # Função para fazer previsões e exibir resultados plotados
        def previsoes_plotadas(modelo, X_test, y_test):
            y_pred = modelo.predict(X_test)
            mse = mean_squared_error(y_test, y_pred)

        # Exibir o Mean Squared Error
            st.write(f"Mean Squared Error: {mse}")

        # Criar DataFrame para plotar previsões vs reais
            df_resultados = pd.DataFrame({
            'Real': y_test,
            'Previsão': y_pred
            }).reset_index(drop=True)

        # Plotar os resultados
            fig = px.line(df_resultados, title="Previsão de Desempenho vs Real",
                      labels={'index': 'Observações', 'value': 'Desempenho'},
                      markers=True)
            fig.add_scatter(x=df_resultados.index, y=df_resultados['Real'], mode='lines+markers', name='Real')
            fig.add_scatter(x=df_resultados.index, y=df_resultados['Previsão'], mode='lines+markers', name='Previsão')
            st.plotly_chart(fig)

        # Exibir importância das variáveis
            importancia = modelo.feature_importances_
            df_importancia = pd.DataFrame({
            'Variável': X_test.columns,
            'Importância': importancia
            }).sort_values(by='Importância', ascending=False)

        # Exibir gráfico de barras da importância das variáveis
            fig_importancia = px.bar(df_importancia, x='Variável', y='Importância', title="Importância das Variáveis no Modelo")
            st.plotly_chart(fig_importancia)

    # Preparar dados
        if variaveis_selecionadas:
            X_train, X_test, y_train, y_test = preparar_dados(df, variaveis_selecionadas)

        # Treinar o modelo
            modelo = treinar_modelo(X_train, y_train)

        # Exibir previsões plotadas e importância das variáveis
            previsoes_plotadas(modelo, X_test, y_test)
        else:
            st.write("Selecione ao menos uma variável para treinar o modelo.")

except FileNotFoundError:
    st.error(f"Arquivo não encontrado: {file_path}")
