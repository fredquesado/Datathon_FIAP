import streamlit as st
from PIL import Image
import base64
from io import BytesIO

# Configuração da página
st.set_page_config(page_title="Tech Challenge 4", page_icon=":house:", layout='wide')
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
    .stApp {{
        background: url(data:image/png;base64,{img_str}) no-repeat center center fixed;
        background-size: cover;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Cabeçalho
with st.container():
    st.title('Bem-vindo(a)')
    st.markdown('<h1 style="font-family:Arial; font-size:60px; color:Black;">Tech Challenge 4</h1>', unsafe_allow_html=True)
    st.markdown('<h1 style="font-family:Arial; font-size:20px; color:Black;">Estudo Abrangente sobre a Dinâmica dos Preços do Petróleo</h1>', unsafe_allow_html=True)
