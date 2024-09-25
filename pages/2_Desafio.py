import streamlit as st
from PIL import Image
import base64
from io import BytesIO

# Configuração da página
st.set_page_config(page_title="Desafio", page_icon=":bar_chart:", layout='wide')
st.sidebar.success("Selecione uma página acima.")

# Função para carregar e redimensionar a imagem
def load_and_resize_image(image_path, new_width=1600, new_height=800):
    image = Image.open(image_path).convert("RGBA")
    resized_image = image.resize((new_width, new_height))
    buffered = BytesIO()
    resized_image.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode()

# Carregar a imagem de fundo e converter para base64
background_image_path = "Imagens/capa4.png"  # Substitua pelo caminho real da sua imagem
background_image_base64 = load_and_resize_image(background_image_path)

# Adicionar a imagem de fundo sem transparência
st.markdown(
    f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap');
    
    .stApp {{
        background: url(data:image/png;base64,{background_image_base64}) no-repeat center center fixed;
        background-size: cover;
        color: #ffffff;  /* Cor do texto principal */
    }}

    /* Centralizando o conteúdo */
    .block-container {{
        padding: 5% 15%;
    }}
    
    h1 {{
        font-family: 'Poppins', sans-serif;
        font-weight: 700;
        color: #800020;  /* Título bordô */
        text-align: center;
        font-size: 3em;  /* Diminuído para 3em */
        text-shadow: 2px 2px 4px #000000;
        margin-bottom: 20px;
    }}
    
    h2 {{
        font-family: 'Poppins', sans-serif;
        font-weight: 400;
        color: black;  /* Texto preto */
        text-align: left;  /* Alinhamento à esquerda */
        font-size: 1.2em;  /* Diminuído para 1.2em */
        margin-bottom: 50px;
        line-height: 1.5;
    }}

    /* Estilo para botões de navegação */
    .stButton>button {{
        background-color: #800020;
        color: #ffffff;
        font-size: 1.2em;
        padding: 10px 20px;
        border-radius: 5px;
        border: none;
        box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
        transition: background-color 0.3s ease;
    }}

    .stButton>button:hover {{
        background-color: #990033;
    }}

    /* Badge estilizada esbranquiçada com texto preto */
    .badge {{
        display: inline-block;
        padding: 10px 20px;
        font-size: 1.2em;  /* Diminuído para 1.2em */
        font-weight: 600;
        color: black;  /* Texto em preto */
        background-color: rgba(255, 255, 255, 0.7);  /* Badge esbranquiçada */
        border-radius: 50px;
        text-align: center;
        margin: 0 auto;
        box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.2);
    }}

    .badge-container {{
        display: flex;
        justify-content: center;
        margin-top: 50px;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Cabeçalho e descrição principal dentro da badge
st.markdown(
    """
    <div class="badge-container">
        <div class="badge">
            <h1>Desafio</h1>
            <h2>
                <p>O presente relatório visa apresentar uma análise detalhada dos dados educacionais de estudantes atendidos pelo programa Passos Mágicos nos anos de 2020, 2021 e 2022.</p>
                <p>O objetivo principal é avaliar o impacto do programa no desenvolvimento dos estudantes, com foco nos indicadores de desempenho e evolução ao longo do período analisado.</p>
                <p>A proposta analítica visa não apenas identificar as principais métricas e indicadores de desempenho, mas também fornecer insights sobre a evolução dos alunos e destacar as áreas onde o impacto da ONG é mais evidente.</p>
            </h2>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)
