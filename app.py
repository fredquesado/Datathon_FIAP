import streamlit as st
from pages import Home, Grupo, Desafio, Relatorio_Analitico_Preditivo, Insights_e_Conclusão

# Mapeamento das páginas
PAGES = {
    "Home": Home,
    "Grupo": Grupo,
    "Desafio": Desafio,
    "Relatório analitico preditivo": Relatorio_Analitico_Preditivo,
    "Insights e Conclusão": Insights_e_Conclusão,
}

def main():
    st.sidebar.title('Menu de Navegação')
    selection = st.sidebar.radio("Ir para", list(PAGES.keys()))
    
    page = PAGES[selection]
    page.app()

if __name__ == "__main__":
    main()
