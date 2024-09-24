import streamlit as st
from pages import Home, grupo_1, desafio_2, relatorio_analitico_preditivo_3, insights_conclusao_4

# Mapeamento das páginas com os nomes apropriados
PAGES = {
    "Home": Home,
    "Grupo": grupo_1,
    "Desafio": desafio_2,
    "Relatório": relatorio_analitico_preditivo_3,
    "Insights": insights_conclusao_4,
}

def main():
    st.sidebar.title('Menu de Navegação')
    selection = st.sidebar.radio("Ir para", list(PAGES.keys()))  # Exibe os títulos corretos no menu
    page = PAGES[selection]
    page.app()  # Chama a função app() de cada página

if __name__ == "__main__":
    main()
