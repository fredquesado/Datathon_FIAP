import streamlit as st
from pages import Home, Grupo, Desafio, Relatorio_Analitico_Preditivo, Insights_e_Conclusao

# Coloque esta configuração no início de app.py
st.set_page_config(page_title="DataThon", page_icon=":house:", layout='wide')

# Mapeamento das páginas
PAGES = {
    "Home": Home,
    "Grupo": Grupo,
    "Desafio": Desafio,
    "Relatório": Relatorio_Analitico_Preditivo,
    "Insights": Insights_e_Conclusao,
}

if __name__ == "__main__":
    main()
