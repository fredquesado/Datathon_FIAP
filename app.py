import streamlit as st
from pages import Home, grupo, desafio, relatorio_analitico_preditivo, insights_conclusao

# Coloque esta configuração no início de app.py
st.set_page_config(page_title="DataThon", page_icon=":house:", layout='wide')

# Mapeamento das páginas
PAGES = {
    "Home": Home,
    "Grupo": grupo,
    "Desafio": desafio,
    "Relatório": relatorio_analitico_preditivo,
    "Insights": insights_conclusao,
}

if __name__ == "__main__":
    main()
