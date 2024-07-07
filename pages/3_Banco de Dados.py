import streamlit as st
from PIL import Image

st.title('Banco de Dados')

tab1, tab2, tab3 = st.tabs(["PNAD Covid-19","Perguntas Escolhidas","Big Query"])
with tab1:
    st.markdown("""
    # PNAD COVID
    A Pesquisa Nacional por Amostra de Domicílios – COVID-19 ou simplesmente [PNAD Covid](https://covid19.ibge.gov.br/), não é apenas uma pesquisa, mas uma iniciativa do IBGE (Instituto Brasileiro de Geografia e Estatística) que buscou entender efeitos da pandemia em nosso país.
    Através do PNAD, buscou-se mensurar o impacto da pandemia nas mais diferentes esferas, e, por essa razão, foi necessário um vasto questionário com perguntas envolvendo questões clínicas, socioeconômicas e características da população.

    Sem uma pesquisa dessa magnitude, seria extremamente difícil entender os problemas causados, bem como identificar os mais afetados pela maior crise sanitária do século.

    Através da análise dos dados colhidos, é possível traçar estratégias políticas que poderão não só minimizar o impacto como também evitar futuros cenários como o que vimos durante a pandemia.
    """)

with tab2:
    st.markdown("""
    # Selecionando as perguntas
    Ao selecionar as perguntas para análise dos dados, consideramos a importância de questões que identificam sintomas, impacto na saúde, acesso a serviços médicos e medidas preventivas durante a pandemia. Além disso, incluímos dados sociodemográficos para uma análise mais detalhada. 
    Iniciamos com a abordagem dos sintomas, destacando a importância de questões que identificam sintomas característicos, como febre, perda de cheiro ou sabor, tosse, entre outros, os quais são cruciais para a identificação de possíveis padrões de manifestações clínicas.

    Além disso, priorizamos perguntas relacionadas ao impacto na saúde e procura por atendimento, que nos permitem avaliar a gravidade da condição de saúde dos indivíduos, a necessidade de recursos médicos e o acesso aos serviços de saúde, evidenciado também pela questão sobre plano de saúde médico.
    É crucial destacar a complexidade da entubação, procedimento delicado que demanda treinamento específico. A escassez de profissionais qualificados para realizar entubações seguras ressalta a necessidade de investimento na formação e preparo de equipes de saúde.
    Considerando o contexto da pandemia do Coronavírus, incorporamos questionamentos sobre as medidas preventivas adotadas, como restrições de contato social e a presença de itens básicos de limpeza e proteção nos domicílios, essenciais para compreender as práticas preventivas e seu impacto na propagação da doença.

    Por fim, a inclusão de dados sociodemográficos, como idade, sexo, etnia, escolaridade, unidade da federação, entre outros, busca fornecer subsídios para uma análise mais detalhada e estratificada dos resultados, considerando as especificidades de diferentes grupos populacionais.
    Dessa forma, a escolha das perguntas para análise reflete a preocupação em obter dados abrangentes e significativos, capazes de contribuir para uma melhor compreensão dos fenômenos em estudo e para o desenvolvimento de estratégias eficazes no âmbito da saúde pública.

    Veja abaixo os itens selecionados:
    ### Perguntas Clínicas
    | Pergunta | Código | Descrição |
    | -------- | ------ | --------- |
    | 1 | B0011 | Na semana passada teve febre? |
    | 2 | B00110 | Na semana passada teve dor nos olhos? |
    | 3 | B00111 | Na semana passada teve perda de cheiro ou sabor? |
    | 4 | B00112 | Na semana passada teve dor muscular? |
    | 5 | B00113 | Na semana passada teve diarreia? |
    | 6 | B0012 | Na semana passada teve tosse? |
    | 7 | B0013 | Na semana passada teve dor de garganta? |
    | 8 | B0014 | Na semana passada teve dificuldade para respirar? |
    | 9 | B0015 | Na semana passada teve dor de cabeça? |
    | 10 | B0016 | Na semana passada teve dor no peito? |
    | 11 | B0017 | Na semana passada teve náusea? |
    | 12 | B0018 | Na semana passada teve nariz entupido ou escorrendo? |
    | 13 | B0019 | Na semana passada teve fadiga? |
    | 14 | B002 | Por causa disso, foi a algum estabelecimento de saúde? |
    | 15 | B006 | Durante a internação, foi sedado, entubado e colocado em respiração artificial com ventilador |
    | 16 | B007 | Tem algum plano de saúde médico, seja particular, de empresa ou de órgão público |
    | 17* | B009B | Qual o resultado? (SWAB) |
    | 17* | B009D | Qual o resultado? (Dedo) |
    | 17* | B009F | Qual o resultado? (Veia) |
    | 18 | B011 | Na semana passada, devido à pandemia do Coronavírus, em que medida o(a) Sr(a) restringiu o contato com as pessoas? |
    | 19 | F002A2 | Na semana passada, o(a) Sr(a) estava em trabalho remoto (home office ou teletrabalho)? |
    | 20 | F002A3 | No seu domicílio há os seguintes itens básicos de limpeza e proteção: máscaras |

    * Foi considerado apenas uma pergunta para essas 3, visto que juntas elas dão a resposta do teste para COVID de forma geral.

    ### Informações Pessoais
    | Código | Descrição |
    | ------ | --------- |
    | A002 | Idade do morador |
    | A003 | Sexo |
    | A004 | Cor ou raça |
    | A005 | Escolaridade |
    | UF | Unidade da Federação |
    | mês | Mês da pesquisa |
    | V1022 | Situação do domicílio |


    """)
with tab3:
    st.markdown("""
    # BigQuery
    No trabalho mencionado, uma fonte essencial de dados para nossa análise foi o Google BigQuery. O Google BigQuery é um serviço de data warehouse e análise de dados na nuvem oferecido pela Google Cloud Platform. Ele foi projetado para processar e analisar grandes conjuntos de dados de forma eficiente, permitindo consultas rápidas e escalabilidade conforme necessário.

    Os dados da Pesquisa Nacional por Amostra de Domicílios (PNAD) foram armazenados no Google BigQuery e podem ser acessados através desse [link](https://basedosdados.org/dataset/c747a59f-b695-4d19-82e4-fef703e74c17?table=5894e1ac-dc08-465d-91a3-703683da85ba).
    Por meio dessa plataforma, pudemos acessar, explorar e analisar os dados da PNAD de maneira ágil e eficaz, executando consultas complexas e extraindo insights relevantes para nosso estudo.

    ## Passos tomados
    
    1. Foi realizada uma Query em SQL para extrair todos os dados relevantes dos meses de setembro a novembro de 2020. A Query está representada na imagem a seguir, e pode ser encontrada tambem no [github](https://github.com/Renan-Carneiro/TechChallenge3PnadCovid).
    """)
    image = Image.open("./imagens/Base de Dados/2QueryBigQuery.png")
    st.image(image)
    st.markdown("""
    2. Foi armazenado o resultado dessa pesquisa no Google Cloud, no caminho **"techchallengepnad.Pnad91011.TabelaPrincipal09a11"**
    """   )
    image = Image.open("./imagens/Base de Dados/3BaseAposQuery.png")
    st.image(image)
    image = Image.open("./imagens/Base de Dados/4detalhesBasePosQuery.png")
    st.image(image)
    st.markdown("""
    3. Foi utilizado então o google collab para fazer o acesso a essa base que criamos com novas consultas SQL. O notebook gerado está incluso no [github](https://github.com/Renan-Carneiro/TechChallenge3PnadCovid).
    
    Exemplo de acesso pelo collab:
    """   )
    image = Image.open("./imagens/Base de Dados/notebook.png")
    st.image(image)
