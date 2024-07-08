import streamlit as st
from PIL import Image, ImageEnhance
import base64
from io import BytesIO

# Configuração da página
st.set_page_config(page_title="Desafio", page_icon=":bar_chart:", layout='wide')

# Função para carregar, ajustar transparência e converter a imagem para base64
def get_base64_image(image_path, transparency=0.4):
    image = Image.open(image_path).convert("RGBA")
    alpha = image.split()[3]
    alpha = ImageEnhance.Brightness(alpha).enhance(transparency)
    image.putalpha(alpha)
    buffered = BytesIO()
    image.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode()

# Carregar a imagem de fundo e converter para base64
background_image_path = "/workspaces/TechChallenge4/Imagens/capa4.png"  # Substitua pelo caminho real da sua imagem
background_image_base64 = get_base64_image(background_image_path)

# Definir a imagem de fundo e o estilo das letras
st.markdown(
    f"""
    <style>
    .stApp {{
        background: url(data:image/png;base64,{background_image_base64}) no-repeat center center fixed;
        background-size: cover;
    }}
    h1 {{
        font-family: Arial;
        font-size: 40px;
        color: Black;
    }}
    p, ul {{
        font-family: Arial;
        font-size: 20px;
        color: Black;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Conteúdo da página
st.markdown('<h1>Desafio</h1>', unsafe_allow_html=True)
    
st.markdown("""

<p>Fomos escolhidos por um grande cliente para um projeto desafiador e estratégico: analisar a variação do preço do petróleo e desenvolver um modelo de machine learning capaz de prever o preço do petróleo nos próximos meses.</p>
<p>Utilizaremos uma base de dados robusta proveniente do site IPEA, que disponibiliza os valores do preço por barril do petróleo bruto tipo Brent. Este projeto não só potencializa nossa expertise, mas também entrega valor ao cliente por meio de insights precisos e previsões assertivas.</p>
""", unsafe_allow_html=True)
