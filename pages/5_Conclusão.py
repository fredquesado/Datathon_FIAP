import streamlit as st

st.title('Conclusão')

st.markdown("# Insights e Considerações Finais", unsafe_allow_html=True)

st.markdown("""
<style>
.big-font {
    font-size: 20px !important;
    margin-bottom: 15px;
    text-indent: 40px;
    max-width: 1000px; /* Define a largura máxima do texto */
    margin-left: 20px; /* Correção: Adiciona 'px' para alinhar corretamente o texto à esquerda */
}
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="big-font">O projeto proporcionou diversos insights valiosos:</p>', unsafe_allow_html=True)

st.markdown('<p class="big-font">• Influência Geopolítica nos Preços do Petróleo: O preço do barril de petróleo é fortemente influenciado pela geopolítica global. Isso é evidente nos anos de 1990-1991, durante a Guerra do Golfo, e novamente em 2008, com a crise financeira global. Esses eventos causaram flutuações significativas nos preços devido à incerteza e às mudanças na oferta e demanda.</p>', unsafe_allow_html=True)

st.markdown('<p class="big-font">• Relação com a Força do Dólar: Existe uma relação inversa entre o preço do petróleo e a força do dólar. Na análise inicial, observamos que quando o dólar se fortalece, os preços do petróleo tendem a cair.</p>', unsafe_allow_html=True)

st.markdown('<p class="big-font">• Validade e Limitações dos Modelos Preditivos: Modelos de previsão de preços do petróleo, como o Random Forest Regressor utilizado neste projeto, são valiosos para embasar decisões estratégicas de curto e médio prazo. No entanto, a análise mostrou que a precisão do modelo diminui para previsões mais longas.</p>', unsafe_allow_html=True)

st.markdown('<p class="big-font">• Impacto das Políticas de Energia Renovável: As políticas globais de transição para energias renováveis também têm um impacto significativo nos preços do petróleo.</p>', unsafe_allow_html=True)

st.markdown('<p class="big-font">Em conclusão, o projeto demonstrou a viabilidade e a importância de utilizar técnicas de machine learning para prever preços de commodities como o petróleo Brent. Os insights obtidos com este projeto destacam a complexidade do mercado de petróleo e a importância de considerar múltiplos fatores ao prever os preços.</p>', unsafe_allow_html=True)
