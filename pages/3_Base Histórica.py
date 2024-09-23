import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

# Título do aplicativo
st.title('Análise Base Histórica PEDE - Passos Mágicos')

# Caminho do arquivo
file_path = "/workspaces/Fiap_Datathon/Arquivos/PEDE_PASSOS_DATASET_FIAP.csv"

# Carregar os dados diretamente do caminho
try:
    df = pd.read_csv(file_path, sep=';')

    # Renomeando as colunas com base no dicionário de dados
    df = df.rename(columns={
        'ANOS_NA_PM_2020': 'Anos no PM 2020',  
        'INDE_2020': 'Desempenho_2020', 
        'INDE_2021': 'Desempenho_2021', 
        'INDE_2022': 'Desempenho_2022',
        'IEG_2020': 'Engajamento_2020',  # Índice de Engajamento Geral (IEG)
        'IEG_2021': 'Engajamento_2021',
        'IEG_2022': 'Engajamento_2022',
        'IDA_2020': 'Aprendizagem_2020',  # Índice de Desenvolvimento de Aprendizagem (IDA)
        'IDA_2021': 'Aprendizagem_2021',
        'IDA_2022': 'Aprendizagem_2022',
        'IAA_2020': 'Autoavaliacao_2020',  # Índice de Autoavaliação (IAA)
        'IAA_2021': 'Autoavaliacao_2021',
        'IAA_2022': 'Autoavaliacao_2022'
    })

    # Garantir que as colunas sejam numéricas
    indicadores = ['Desempenho_2020', 'Desempenho_2021', 'Desempenho_2022',
                   'Engajamento_2020', 'Engajamento_2021', 'Engajamento_2022',
                   'Aprendizagem_2020', 'Aprendizagem_2021', 'Aprendizagem_2022',
                   'Autoavaliacao_2020', 'Autoavaliacao_2021', 'Autoavaliacao_2022']
    
    for indicador in indicadores:
        df[indicador] = pd.to_numeric(df[indicador], errors='coerce')

    # Criação das abas
    introducao, tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "Introdução", "Evolução Desempenho", 
        "Evolução Engajamento", "Autoavaliação x Aprendizagem", 
        "Correlação Indicadores", "Picos de Aumento e Diminuição", 
        "Distribuição por Faixa Etária"
    ])

    ### Introdução
    with introducao:
        st.header("Introdução")
        st.markdown("""
        Bem-vindo à Análise Base Histórica PEDE - Passos Mágicos. 
        Neste painel, você encontrará análises detalhadas sobre o desempenho dos alunos ao longo dos anos, 
        com foco em indicadores como Engajamento, Autoavaliação, Aprendizagem e outros aspectos educacionais.
        Selecione as abas acima para explorar as análises.
        """)

    ### Aba 1: Evolução do Desempenho Médio
    with tab1:
        st.subheader("Evolução do Desempenho Médio")
        st.markdown("""
        O gráfico abaixo mostra a evolução do **Desempenho Médio (INDE)** dos alunos ao longo dos anos selecionados. 
        
        **Análise:**
        - Se o desempenho médio aumentou ao longo do tempo, pode-se inferir melhorias na qualidade do ensino.
        - Caso tenha havido uma queda, fatores como a pandemia, alterações no corpo docente ou outros aspectos podem ter impactado negativamente o desempenho.
        """)
        desempenho_medio = []
        anos = ['2020', '2021', '2022']
        if '2020' in anos:
            desempenho_medio.append(df['Desempenho_2020'].mean())
        if '2021' in anos:
            desempenho_medio.append(df['Desempenho_2021'].mean())
        if '2022' in anos:
            desempenho_medio.append(df['Desempenho_2022'].mean())
        fig_desempenho = px.line(x=anos, y=desempenho_medio, labels={'x': 'Ano', 'y': 'Desempenho Médio'}, title="Evolução do Desempenho Médio")
        st.plotly_chart(fig_desempenho)

    ### Aba 2: Evolução do Engajamento
    with tab2:
        st.subheader("Evolução do Engajamento ao Longo dos Anos")
        st.markdown("""
        Este gráfico mostra a evolução do **Índice de Engajamento Geral (IEG)** dos alunos ao longo dos anos selecionados.

        **Análise:**
        - Um aumento no engajamento indica que os alunos estão mais envolvidos com suas atividades escolares, o que pode refletir em melhores resultados acadêmicos.
        - Uma queda no engajamento pode indicar problemas de motivação ou falta de interesse, o que pode exigir ajustes pedagógicos.
        """)
        engajamento_medio = []
        if '2020' in anos:
            engajamento_medio.append(df['Engajamento_2020'].mean())
        if '2021' in anos:
            engajamento_medio.append(df['Engajamento_2021'].mean())
        if '2022' in anos:
            engajamento_medio.append(df['Engajamento_2022'].mean())
        fig_engajamento = px.line(x=anos, y=engajamento_medio, labels={'x': 'Ano', 'y': 'Engajamento Médio'}, title="Evolução do Engajamento Médio")
        st.plotly_chart(fig_engajamento)

    ### Aba 3: Comparação de Autoavaliação e Aprendizagem
    with tab3:
        st.subheader("Comparação de Autoavaliação e Aprendizagem")
        st.markdown("""
        Este gráfico compara a **Autoavaliação** (IAA) e o **Índice de Aprendizagem** (IDA) ao longo dos anos.

        **Análise:**
        - Se ambos (IAA e IDA) estão alinhados, isso mostra que os alunos estão conscientes do seu próprio aprendizado.
        - Se o IAA for alto, mas o IDA for baixo, isso pode indicar autoconfiança excessiva.
        """)
        anos_para_comparacao = [f'Autoavaliacao_{ano}' for ano in anos] + [f'Aprendizagem_{ano}' for ano in anos]
        fig_comparacao_iaa_ida = px.box(df, y=anos_para_comparacao, title="Comparação de Autoavaliação e Aprendizagem")
        st.plotly_chart(fig_comparacao_iaa_ida)

    ### Aba 4: Correlação entre Indicadores Educacionais
    with tab4:
        st.subheader("Correlação entre Indicadores Educacionais")
        st.markdown("""
        O gráfico abaixo exibe a **correlação** entre os principais indicadores educacionais: Engajamento, Autoavaliação e Aprendizagem.

        **Análise:**
        - Correlações positivas indicam que os alunos mais engajados também tendem a ter melhor desempenho e se autoavaliar melhor.
        - Correlações negativas ou fracas podem indicar desconexões entre engajamento e desempenho, apontando possíveis áreas de intervenção.
        """)
        corr_df = df[['Engajamento_2020', 'Engajamento_2021', 'Engajamento_2022', 
                      'Autoavaliacao_2020', 'Autoavaliacao_2021', 'Autoavaliacao_2022',
                      'Aprendizagem_2020', 'Aprendizagem_2021', 'Aprendizagem_2022']].corr()
        fig_corr = px.imshow(corr_df, title="Correlação entre Indicadores")
        st.plotly_chart(fig_corr)

    ### Aba 5: Picos de Aumento e Diminuição no Desempenho
    with tab5:
        st.subheader("Picos de Aumento e Diminuição de Desempenho")
        st.markdown("""
        Aqui você pode observar as mudanças no desempenho dos alunos entre os anos selecionados.

        **Análise:**
        - Aumento no desempenho pode estar relacionado a melhorias na pedagogia ou intervenções específicas.
        - Quedas podem indicar eventos externos (como a pandemia), mudanças no ambiente escolar ou dificuldades individuais.
        """)
        df['Dif_Desempenho_2020_2021'] = df['Desempenho_2021'] - df['Desempenho_2020']
        df['Dif_Desempenho_2021_2022'] = df['Desempenho_2022'] - df['Desempenho_2021']

        dif_desempenho = []
        if '2021' in anos and '2020' in anos:
            dif_desempenho.append(df['Dif_Desempenho_2020_2021'].mean())
        if '2022' in anos and '2021' in anos:
            dif_desempenho.append(df['Dif_Desempenho_2021_2022'].mean())

        fig_dif = px.line(x=['2020-2021', '2021-2022'], y=dif_desempenho, 
                          labels={'x': 'Período', 'y': 'Diferença Média no Desempenho'}, 
                          title="Diferença Média no Desempenho (INDE)")
        st.plotly_chart(fig_dif)

    ### Aba 6: Distribuição dos Indicadores por Faixa Etária
    with tab6:
        if 'IDADE' in df.columns:  # Verifica se há uma coluna de idade no dataset
            st.subheader("Distribuição dos Indicadores por Faixa Etária")
            st.markdown("""
            Este gráfico mostra como o Engajamento, Autoavaliação e Aprendizagem variam de acordo com a faixa etária dos alunos.

            **Análise:**
            - Faixas etárias mais jovens podem apresentar maior engajamento inicial, enquanto faixas mais velhas podem ter maior autoavaliação devido à maturidade.
            - Se o engajamento diminuir com a idade, isso pode indicar perda de motivação ao longo do tempo, exigindo adaptações pedagógicas.
            """)
            fig_faixa_etaria = px.histogram(
                df, 
                x='IDADE', 
                y=['Engajamento_2020', 'Autoavaliacao_2020', 'Aprendizagem_2020'], 
                title="Distribuição de Indicadores por Faixa Etária",
                labels={'x': 'Idade', 'y': 'Indicadores'}
            )
            st.plotly_chart(fig_faixa_etaria)
        else:
            st.error("A coluna 'IDADE' não foi encontrada no dataset.")

except FileNotFoundError:
    st.error(f"Arquivo não encontrado: {file_path}")

