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

<p>O presente relatório visa apresentar uma análise detalhada dos dados educacionais de estudantes atendidos pelo programa Passos Mágicos nos anos de 2020, 2021 e 2022. O objetivo principal é avaliar o impacto do programa no desenvolvimento dos estudantes, com foco nos indicadores de desempenho e evolução ao longo do período analisado.</p>
<p>A proposta analítica visa não apenas identificar as principais métricas e indicadores de desempenho, mas também fornecer insights sobre a evolução dos alunos e destacar as áreas onde o impacto da ONG é mais evidente.</p>
""", unsafe_allow_html=True)
