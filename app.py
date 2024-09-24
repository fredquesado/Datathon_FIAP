import streamlit as st
from pages import Home, grupo, desafio, relatorio_analitico_preditivo, insights_conclusao

# Mapeamento das páginas com os nomes apropriados
PAGES = {
    "Home": Home,
    "Grupo": grupo,
    "Desafio": desafio,
    "Relatório": relatorio_analitico_preditivo,
    "Insights": insights_conclusao,
}

if __name__ == "__main__":
    main()
