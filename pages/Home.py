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

# Adicionar a imagem de fundo
st.markdown(
    f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap');
    
    .stApp {{
        background: url(data:image/png;base64,{img_str}) no-repeat center center fixed;
        background-size: cover;
    }}
    
    h1 {{
        font-family: 'Poppins', sans-serif;
        font-weight: 600;
        color: #212529;
        text-shadow: 1px 1px 2px #000;
    }}
    
    h2 {{
        font-family: 'Poppins', sans-serif;
        font-weight: 400;
        color: #212529;
    }}
    
    </style>
    """,
    unsafe_allow_html=True
)

# Cabeçalho
with st.container():
    st.markdown('<h1 style="font-size:60px;">Bem-vindo(a)</h1>', unsafe_allow_html=True)
    st.markdown('<h1 style="font-size:50px;">Datathon - Fiap</h1>', unsafe_allow_html=True)
    st.markdown('<h2 style="font-size:20px;">Transformando dados em impacto: previsão e análise para uma educação mais inclusiva e eficaz</h2>', unsafe_allow_html=True)
