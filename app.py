import streamlit as st
from pages import '1_Grupo', '2_Desafio', '3_relatorio_analitico_preditivo', '4_Insights_e_Conclusão'

# Mapeamento das páginas
PAGES = {
    "Home": Home,
    "Grupo": 1_Grupo,
    "Desafio": 2_Desafio,
    "Relatório analitico preditivo": 3_relatorio_analitico_preditivo,
    "Insights e Conclusão": 4_Insights_e_Conclusão,
}

def main():
    st.sidebar.title('Menu de Navegação')
    selection = st.sidebar.radio("Ir para", list(PAGES.keys()))
    
    page = PAGES[selection]
    page.app()

if __name__ == "__main__":
    main()
