import streamlit as st
from pages import Grupo, Desafio, Relatório_Analitico_Preditivo, Previsão, Insights_e_Conclusoes

# Mapeamento das páginas
PAGES = {
    "Home": Home 0,
    "Grupo": Grupo_1,
    "Desafio": Desafio,
    "Relatório Analitico Preditivo": Relatório_Analitico_Preditivo,
    "Previsão": Previsão,
    "Insights e Conclusão": Insights_e_Conclusoes,
}

def main():
    st.sidebar.title('Menu de Navegação')
    selection = st.sidebar.radio("Ir para", list(PAGES.keys()))
    
    page = PAGES[selection]
    
if __name__ == "__main__":
    main()
