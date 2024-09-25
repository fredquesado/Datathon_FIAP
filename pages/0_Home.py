import streamlit as st
from PIL import Image
import base64
from io import BytesIO

# Configuração da página
st.set_page_config(page_title="DataThon", page_icon=":house:", layout='wide')
st.sidebar.success("Selecione uma página acima.")

# Carregar a imagem e aplicar transparência
image = Image.open("Imagens/capa4.png").convert("RGBA")

# Aplicar transparência diretamente na imagem
transparency_level = 100  # Defina o nível de transparência (0-255)
image.putalpha(transparency_level)

# Redimensionar a imagem
new_width = 1600  # Defina a nova largura desejada
new_height = 800  # Defina a nova altura desejada
resized_image = image.resize((new_width, new_height))

# Converter a imagem redimensionada para base64
buffered = BytesIO()
resized_image.save(buffered, format="PNG")
img_str = base64.b64encode(buffered.getvalue()).decode()

# Adicionar a imagem de fundo (sem gradiente, apenas a imagem original)
st.markdown(
    f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap');
    
    .stApp {{
        background: url(data:image/png;base64,{img_str}) no-repeat center center fixed;
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
        color: #ffffff;
        text-align: center;
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
            <h1>Bem-vindo(a)</h1>
            <h1>Datathon - Fiap</h1>
            <h2>Transformando dados em impacto: previsão e análise para uma educação mais inclusiva e eficaz</h2>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)
