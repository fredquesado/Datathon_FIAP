import streamlit as st
from pages import grupo_1, desafio_2, relatorio_analitico_preditivo_3, insights_conclusao_4

# Mapeamento das páginas
PAGES = {
    "Home": Home,
    "Grupo": grupo_1,
    "Desafio": desafio_2,
    "Base Histórica": relatorio_analitico_preditivo_3,
    "Insights e Conclusão": insights_conclusao_4,
}

def main():
    st.sidebar.title('Menu de Navegação')
    selection = st.sidebar.radio("Ir para", list(PAGES.keys()))
    
    page = PAGES[selection]
    page.app()

if __name__ == "__main__":
    main()
