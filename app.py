import streamlit as st
import importlib

# Importar módulos usando importlib para lidar com nomes com acentos
Grupo = importlib.import_module('pages.1_Grupo')
Desafio = importlib.import_module('pages.2_Desafio')
Relatorio_Analitico_Preditivo = importlib.import_module('pages.3_Relatório_Analitico_Preditivo')
Insights_e_Conclusoes = importlib.import_module('pages.5_Insights_e_Conclusoes')

# Se o arquivo Home for necessário, importe também (caso o nome do arquivo tenha acento, use importlib)
Home = importlib.import_module('pages.0_Home')

# Mapeamento das páginas
PAGES = {
    "Home": Home,
    "Grupo": Grupo,
    "Desafio": Desafio,
    "Relatório Analitico Preditivo": Relatorio_Analitico_Preditivo,
    "Insights e Conclusão": Insights_e_Conclusoes,
}

if __name__ == "__main__":
    main()
