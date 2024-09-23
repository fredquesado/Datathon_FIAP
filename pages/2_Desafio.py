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
background_image_path = "Imagens/capa4.png"  # Substitua pelo caminho real da sua imagem
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

<p>Fomos escolhidos para um projeto desafiador e estratégico: analisar o impacto educacional que a ONG Passos Mágicos tem gerado na comunidade que atende e desenvolver um modelo preditivo capaz de prever o desempenho futuro dos alunos.</p>
<p>Utilizaremos uma base de dados extensa com informações educacionais dos anos de 2020, 2021 e 2023. Este projeto não só amplia nossa expertise em análise de dados, como também entrega insights valiosos para a ONG, ajudando a tomar decisões mais assertivas e transformar a vida de crianças e jovens em situação de vulnerabilidade social.</p>
""", unsafe_allow_html=True)
