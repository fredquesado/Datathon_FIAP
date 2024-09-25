import streamlit as st
from PIL import Image
import base64
from io import BytesIO

def main():
    # Configura as preferências da página, como título, ícone e layout.
    st.set_page_config(page_title="DataThon", page_icon=":house:", layout='wide')
    
    # Exibe uma mensagem de sucesso no menu lateral.
    st.sidebar.success("Selecione uma página acima.")

    # Carrega a imagem de fundo.
    image = Image.open("Imagens/capa4.png").convert("RGBA")

    # Redimensiona a imagem para se ajustar melhor à tela.
    new_width = 1600  # Define a nova largura da imagem.
    new_height = 800  # Define a nova altura da imagem.
    resized_image = image.resize((new_width, new_height))

    # Converte a imagem redimensionada para o formato base64 para ser usada no HTML.
    buffered = BytesIO()
    resized_image.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode()

    # Aplica a imagem de fundo e ajusta a transparência da interface.
    st.markdown(
        f"""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap');
        
        /* Define o estilo de fundo da aplicação com a imagem carregada */
        .stApp {{
            background: url(data:image/png;base64,{img_str}) no-repeat center center fixed;
            background-size: cover;
            color: #ffffff;  /* Define a cor padrão do texto */
        }}

        /* Centraliza o conteúdo principal da página */
        .block-container {{
            padding: 5% 15%;
        }}
        
        /* Estiliza a caixa de conteúdo central com leve transparência */
        .badge {{
            background-color: rgba(255, 255, 255, 0.85);  /* Transparência da caixa de conteúdo */
            padding: 30px;
            border-radius: 15px;
            box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.2);  /* Adiciona uma sombra suave */
            text-align: center;
            width: 80%;
            margin: auto;
        }}

        /* Define o estilo do título principal */
        h1 {{
            font-family: 'Poppins', sans-serif;
            font-weight: 700;
            color: #2e4053;  /* Cor do título */
            text-align: center;
            font-size: 3em;  /* Tamanho do título */
            margin-bottom: 20px;
        }}
        
        /* Define o estilo do subtítulo */
        h2 {{
            font-family: 'Poppins', sans-serif;
            font-weight: 400;
            color: #1c2833;  /* Cor do texto do subtítulo */
            text-align: center;
            font-size: 1.2em;
            margin-bottom: 50px;
            line-height: 1.5;
        }}

        /* Estiliza os botões de navegação */
        .stButton>button {{
            background-color: #800020;
            color: #ffffff;
            font-size: 1.2em;
            padding: 10px 20px;
            border-radius: 5px;
            border: none;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);  /* Adiciona uma leve sombra */
            transition: background-color 0.3s ease;  /* Transição suave ao passar o mouse */
        }}

        /* Muda a cor do botão ao passar o mouse */
        .stButton>button:hover {{
            background-color: #990033;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

    # Adiciona o cabeçalho e a descrição principal em uma caixa centralizada e estilizada (badge).
    st.markdown(
        """
        <div class="badge">
            <h1>Datathon - Fiap</h1>
            <h2>Transformando dados em impacto: previsão e análise para uma educação mais inclusiva e eficaz</h2>
        </div>
        """,
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
