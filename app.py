import streamlit as st
from pages import Home, grupo, desafio, relatorio_analitico_preditivo, insights_conclusao

# Definir a configuração da página como a primeira ação
st.set_page_config(page_title="DataThon", page_icon=":house:", layout='wide')

# Mapeamento das páginas com os nomes apropriados
PAGES = {
    "Home": Home,
    "Grupo": grupo,
    "Desafio": desafio,
    "Relatório": relatorio_analitico_preditivo,
    "Insights": insights_conclusao,
}

def main():
    st.sidebar.title('Menu de Navegação')
    selection = st.sidebar.radio("Ir para", list(PAGES.keys()))  # Exibe os títulos corretos no menu
    page = PAGES[selection]
    page.app()  # Chama a função app() de cada página

if __name__ == "__main__":
    main()  # Certifique-se de que esta linha existe para chamar a função main
