import streamlit as st
from PIL import Image
import base64
from io import BytesIO

# Configuração da página
st.set_page_config(page_title="DataThon", page_icon=":house:", layout='wide')
st.sidebar.success("Selecione uma página acima.")

# Carregar a imagem e aplicar transparência
image = Image.open("Imagens/capa4.png").convert("RGBA")
data = image.getdata()

# Definir o nível de transparência
transparency_level = 100  # Pode variar de 0 (completamente transparente) a 255 (opaco)

new_data = []
for item in data:
    # Alterar apenas os pixels que não são totalmente transparentes
    if item[3] > 0:
        new_data.append((item[0], item[1], item[2], transparency_level))
    else:
        new_data.append(item)

image.putdata(new_data)

# Redimensionar a imagem
new_width = 1600  # Define a nova largura desejada
new_height = 800  # Define a nova altura desejada
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
        padding-top: 5%;
        padding-bottom: 5%;
        padding-left: 15%;
        padding-right: 15%;
    }}
    
    h1 {{
        font-family: 'Poppins', sans-serif;
        font-weight: 700;
        color: #800020;  /* Título bordô */
        text-align: center;
        font-size: 4em;
        text-shadow: 2px 2px 4px #000000;
        margin-bottom: 20px;
    }}
    
    h2 {{
        font-family: 'Poppins', sans-serif;
        font-weight: 400;
        color: #ffffff;
        text-align: center;
        font-size: 1.5em;
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

    </style>
    """,
    unsafe_allow_html=True
)

# Cabeçalho e descrição principal
with st.container():
    st.markdown('<h1>Bem-vindo(a)</h1>', unsafe_allow_html=True)
    st.markdown('<h1>Datathon - Fiap</h1>', unsafe_allow_html=True)
    st.markdown(
        '<h2>Transformando dados em impacto: previsão e análise para uma educação mais inclusiva e eficaz</h2>',
        unsafe_allow_html=True
    )

# Espaçamento
st.write("")

# Adicionar botões de navegação estilizados
col1, col2, col3 = st.columns([1, 1, 1])
with col1:
    st.button('Página Inicial')
with col2:
    st.button('Relatórios')
with col3:
    st.button('Contato')
