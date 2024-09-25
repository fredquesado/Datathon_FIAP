import streamlit as st
from PIL import Image
import base64
from io import BytesIO

# Configuração da página
st.set_page_config(page_title="Grupo Responsável", page_icon=":house:", layout='wide')

# Função para carregar e converter a imagem para base64
def get_base64_image(image_path):
    image = Image.open(image_path).convert("RGBA")
    buffered = BytesIO()
    image.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode()

# Carregar a imagem de fundo e converter para base64
background_image_path = "Imagens/capa4.png"
background_image_base64 = get_base64_image(background_image_path)

# Definir a imagem de fundo com transparência e adicionar o gradiente
st.markdown(
    f"""
    <style>
    .stApp {{
        background: linear-gradient(to bottom, rgba(128, 0, 32, 0.5), rgba(255, 255, 255, 0.5)), 
                    url(data:image/png;base64,{background_image_base64}) no-repeat center center fixed;
        background-size: cover;
    }}

    /* Centraliza o conteúdo principal */
    .block-container {{
        padding: 5% 15%;
    }}

    /* Estilo da badge de aluno */
    .badge {{
        background-color: rgba(255, 255, 255, 0.9);  /* Leve transparência no fundo */
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);  /* Sombra suave */
        margin-bottom: 10px;
    }}

    /* Estilo do título da página */
    h1 {{
        font-family: 'Poppins', sans-serif;
        font-weight: 700;
        color: #2e4053;  /* Azul-acinzentado */
        text-align: center;
        font-size: 2.5em;
    }}

    /* Estilo dos parágrafos com informações */
    p {{
        font-family: 'Poppins', sans-serif;
        color: #800020;  /* Bordô */
        font-size: 1.2em;
        margin: 0;
    }}

    </style>
    """,
    unsafe_allow_html=True
)

# Nome dos componentes do grupo
student_data = [
    {"nome": "Antônio Leão", "matricula": "RM349640"},
    {"nome": "Frederico Quesado", "matricula": "RM352633"},
    {"nome": "Lucas Tabelini", "matricula": "RM352725"},
    {"nome": "Renan Carneiro", "matricula": "RM352715"},
    {"nome": "Vanessa Andrade", "matricula": "RM352921"},
    
]

# Título da página
st.markdown('<h1>Grupo Responsável</h1>', unsafe_allow_html=True)

# Dividir em duas colunas
left_column, right_column = st.columns(2)

# Exibir informações dos alunos usando badges estilizadas
for i, student in enumerate(student_data):
    column = left_column if i % 2 == 0 else right_column
    with column:
        st.markdown(
            f"""
            <div class="badge">
                <p><strong>Nome:</strong> {student['nome']}</p>
                <p><strong>Número de Matrícula:</strong> {student['matricula']}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
