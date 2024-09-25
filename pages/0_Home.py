import streamlit as st
def main():
   # Definir a configuração da página
   st.set_page_config(page_title="Capa do Trabalho", layout="centered")
   # Estilo customizado
   st.markdown(
       """
<style>
       .title {
           font-size: 40px;
           font-weight: bold;
           color: #2e4053;  /* Azul-acinzentado */
           text-align: center;
           margin-top: 50px;
       }
       .subtitle {
           font-size: 24px;
           color: #1c2833;  /* Cinza escuro */
           text-align: center;
           margin-top: 20px;
       }
       .group {
           font-size: 20px;
           color: #1c2833;  /* Cinza escuro */
           text-align: center;
           margin-top: 40px;
           line-height: 1.6;  /* Espaçamento entre linhas */
       }
</style>
       """,
       unsafe_allow_html=True
   )
   # Exibir o título do trabalho
   st.markdown('<div class="title">Datathon - Fiap</div>', unsafe_allow_html=True)
   st.markdown('<div class="subtitle">Transformando dados em impacto: previsão e análise para uma educação mais inclusiva e eficaz</div>', unsafe_allow_html=True)
   # Exibir os nomes do grupo em ordem alfabética
   st.markdown(
       """
<div class="group">
           Nome: Frederico Quesado<br>
           Número de Matrícula: RM352633<br><br>
           Nome: Lucas Tabelini<br>
           Número de Matrícula: RM352725<br><br>
           Nome: Renan Carneiro<br>
           Número de Matrícula: RM352715<br><br>
           Nome: Vanessa Andrade<br>
           Número de Matrícula: RM352921
</div>
       """,
       unsafe_allow_html=True
   )
# Chamar a função main
if __name__ == "__main__":
   main()
