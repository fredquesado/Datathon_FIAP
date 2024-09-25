import streamlit as st
import importlib

# Importar módulos usando importlib para lidar com nomes com acentos
Grupo = importlib.import_module('pages.1_Grupo')
Desafio = importlib.import_module('pages.2_Desafio')
Relatorio_Analitico_Preditivo = importlib.import_module('pages.3_Relatorio_Analitico_Preditivo')
Insights_e_Conclusoes = importlib.import_module('pages.5_Insights_e_Conclusoes')
Home = importlib.import_module('pages.0_Home')

# Mapeamento das páginas
PAGES = {
    "Home": Home,
    "Grupo": Grupo,
    "Desafio": Desafio,
    "Relatório Analitico Preditivo": Relatorio_Analitico_Preditivo,
    "Insights e Conclusão": Insights_e_Conclusoes,
}

# Definir a função main
def main():
    st.title("Menu de Navegação")

    # Exibir o menu de navegação na parte principal da página
    selection = st.selectbox("Escolha a página", list(PAGES.keys()), index=0)

    # Carregar a página selecionada
    page = PAGES[selection]

    # Exibir o conteúdo da página selecionada
    page.main()  # Supondo que cada módulo tenha uma função `main()` que renderiza a página

# Chamar a função main dentro do bloco correto
if __name__ == "__main__":
    main()
