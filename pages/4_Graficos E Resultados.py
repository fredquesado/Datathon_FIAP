import streamlit as st
from PIL import Image

st.title('Gráficos e Resultados')

tab1, tab2 = st.tabs(["Análise Demográfica","Análise de Sintomas"])
with tab1:
    st.markdown("""
    # Análise Demográfica
    A seguir realizaremos algumas análises sobre características da população que participou dessa pesquisa.
    Essas análises serão sobre características **Sociais, Clínicas e Econômicas**.
    
    ## Gênero e Incidência
    """)
    image = Image.open("./imagens/Graficos/barras_teste_positivo_por_sexo.png")
    st.image(image)
    st.markdown("""
    Nesse gráfico podemos ver que há uma porcentagem maior de mulheres que responderam a pesquisa e houve levemente mais testes positivos de COVID entre elas.
    """)
    st.markdown("""
    ## Faixa Etária e Porcentagem de Teste Positivo
    """)
    image = Image.open("./imagens/Graficos/teste_positivo_por_faixa_etaria.png")
    st.image(image)
    st.markdown("""
    Podemos perceber que as faixas mais novas de idade (0 a 20) apresentaram poucos testes positivos, com maior incidencia de diagnóstico na população econômicamente ativa, e nos idosos.
    """)
    st.markdown("""
    ## Composição Geral por etnia, e de pessoas que testaram positivo
    """)
    image = Image.open("./imagens/Graficos/barras_teste_positivo_por_etnia.png")
    st.image(image)
    st.markdown("""
    Houve uma maior incidência na população indígena, o que pode ser um ponto de atenção, por se tratar de uma parcela vulnerável da população, que exige maior monitoramento por parte da saúde pública.
    """)
    st.markdown("""
    ## Top 10 Estados por Porcentagem de Respondentes e Porcentagem de Teste Positivo
    """)
    image = Image.open("./imagens/Graficos/estadosEpositivos.png")
    st.image(image)
    st.markdown("""
    Observamos uma porcentagem maior de positivados no maranhão, e menor em Minas Gerais (que apresentou um maior numero de respondentes). Dito isso, é preciso ter cautela quanto a interpretação desse dado de maneira isolada, pois
    existem diferenças na taxa de teste entre os estados, o que pode mascarar incidências maiores em estados que testam menos.
    """)
    st.markdown("""
    ## Composição Geral por escolaridade, e de pessoas que testaram positivo
    """)
    image = Image.open("./imagens/Graficos/escolaridadeEpositivos.png")
    st.image(image)
    st.markdown("""
    Existe a interessante observação de que nas camadas com maior escolaridade, há uma porcentagem maior de positivação nos testes. Uma possível explicação é a de que as populações com maior escolaridade são economicamente ativas, e portanto tiveram uma
    maior exposição no seu dia a dia.
    """)
    st.markdown("""
    ## Distribuição de Plano de Saúde na População
    """)
    image = Image.open("./imagens/Graficos/pizzaPlanoSaude.png")
    st.image(image)
    st.markdown("""
    Dentre os respondentes, existe uma proporção muito maior de pessoas que não possuem plano de saúde complementar, dependendendo então apenas do SUS. Isso demonstra a importância
    do Sistema Público de Saúde para atendimento da população, principalmente em casos extremos como o de uma pandemia.
    """)
    st.markdown("""
    ## Uso de máscaras pela população
    """)
    image = Image.open("./imagens/Graficos/treeUsoMascara.png")
    st.image(image)
    st.markdown("""
    A quase totalidade dos respondentes reportou o uso de máscaras ao responder a pergunta nesse intervalo, o que demonstra que as políticas públicas de incentivo ao uso dessa proteção
    obtiveram êxito.
    """)
    st.markdown("""
    ## Isolamento Social
    """)
    image = Image.open("./imagens/Graficos/RestricaovsPositivos.png")
    st.image(image)
    st.markdown("""
    Pode-se verificar por esse gráfico o aumento da chance de teste positivo para pessoas que evitaram menos a exposição ao risco do contato social.
    """)    
    

with tab2:
    st.markdown("""
    ## Sintomas mais comuns x Sintomas com mais testes positivos
    """)
    image = Image.open("./imagens/Graficos/SintomasVsPositivos.png")
    st.image(image)
    st.markdown("""
    Temos no lado esquerdo os sintomas mais reportados pela população, onde queixas de dor de cabeça, nariz entupido e tosse são comuns, por exemplo.
    
    No lado direito temos a incidência de testes positivos de COVID para cada um desses sintomas.
    
    É interessante perceber que dor de cabeça é o sintoma com maior chance de teste positivo, tambem ligado a tosse, dor muscular, febre, fadiga, e dificuldade com cheiro e sabor.
    Esses ultimos sintomas são mais incomuns, e portanto merecem uma melhor investigação pelos profissionais da saúde.
    """)
    st.markdown("""
    ## Percentual de Pessoas Entubadas por Sintoma
    """)
    image = Image.open("./imagens/Graficos/EntubadosTiveramSintomas.png")
    st.image(image)
    st.markdown("""
    Dentre os entrevistados que foram entubados, a grande maioria apresentou os sintomas de Dificuldade para respirar, tosse, febre, fadiga, e dor muscular, dentre outras.
    
    No entanto, analisamos tambem esse panorama enxergado através dos sintomas da população em geral, e sua chance de necessitar de uma entubação:
    """)
    image = Image.open("./imagens/Graficos/SintomasVsEntubados.png")
    st.image(image)
    st.markdown("""
    Aqui percebemos que as pessoas que apresentaram dor no peito, dificuldade com cheiro e sabor, febre, nausea e fadiga na semana anterior, principalmente, apresentaram uma chance maior de ser necessitar de respiração articial (entubação).
    """)