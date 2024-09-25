import streamlit as st
from PIL import Image
import base64
from io import BytesIO

# Configuração da página
st.set_page_config(page_title="Datathon - Fiap", page_icon=":star:", layout='wide')

# Função para carregar e converter a imagem para base64
def get_base64_image(image_path):
    image = Image.open(image_path).convert("RGBA")
    buffered = BytesIO()
    image.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode()

# Carregar a imagem de fundo e converter para base64
background_image_path = "Imagens/capa4.png" 
background_image_base64 = get_base64_image(background_image_path)

# Definir a imagem de fundo com transparência e aplicar estilos modernos
st.markdown(
    f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600&display=swap');

    .stApp {{
        font-family: 'Montserrat', sans-serif;
        background: linear-gradient(to bottom, rgba(255, 255, 255, 0.8), rgba(255, 255, 255, 0.8)),
                    url(data:image/png;base64,{background_image_base64}) no-repeat center center fixed;
        background-size: cover;
        color: #333333;
    }}

    h1 {{
        font-size: 48px;
        color: #800080;
        text-align: center;
        margin-bottom: 50px;
        font-weight: 600;
    }}

    .student-card {{
        background-color: rgba(255, 255, 255, 0.9);
        border-radius: 15px;
        padding: 20px;
        margin: 10px 0;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
        transition: transform 0.2s ease-in-out;
    }}

    .student-card:hover {{
        transform: translateY(-5px);
        box-shadow: 0 6px 15px rgba(0, 0, 0, 0.15);
    }}

    p {{
        font-size: 18px;
        color: #333;
    }}

    .stButton>button {{
        background-color: #800080;
        color: white;
        border-radius: 10px;
        padding: 10px 20px;
        font-size: 16px;
        font-weight: 600;
        border: none;
        cursor: pointer;
        transition: background-color 0.3s ease-in-out;
    }}

    .stButton>button:hover {{
        background-color: #5c005c;
    }}

    </style>
    """,
    unsafe_allow_html=True
)

# Título da página estilizado
st.markdown('<h1>Datathon - Fiap</h1>', unsafe_allow_html=True)

# Nome dos componentes do grupo
student_data = [
    {"nome": "Antônio Leão", "matricula": "RM349640"},
    {"nome": "Frederico Quesado", "matricula": "RM352633"},
    {"nome": "Lucas Tabelini", "matricula": "RM352725"},
    {"nome": "Renan Carneiro", "matricula": "RM352715"},
    {"nome": "Vanessa Andrade", "matricula": "RM352921"},
]

# Dividir em duas colunas com layout centralizado
left_column, right_column = st.columns(2)

# Exibir informações dos alunos com um visual moderno
for i, student in enumerate(student_data):
    column = left_column if i % 2 == 0 else right_column
    with column:
        st.markdown(
            f"""
            <div class="student-card">
                <p><strong>Nome:</strong> {student['nome']}</p>
                <p><strong>Número de Matrícula:</strong> {student['matricula']}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

# Adicionar um botão estilizado para mais informações (opcional)
st.button("Saiba Mais")
