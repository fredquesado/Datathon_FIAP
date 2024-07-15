import streamlit as st

st.title('Insights e Conclusão')

st.markdown("""
### O projeto proporcionou diversos insights valiosos:

**• Influência Geopolítica nos Preços do Petróleo:** O preço do barril de petróleo é fortemente influenciado pela geopolítica global. Isso é evidente nos anos de 1990-1991, durante a Guerra do Golfo, e novamente em 2008, com a crise financeira global. Esses eventos causaram flutuações significativas nos preços devido à incerteza e às mudanças na oferta e demanda.

**• Relação com a Força do Dólar:** Existe uma relação inversa entre o preço do petróleo e a força do dólar. Na análise inicial, observamos que quando o dólar se fortalece, os preços do petróleo tendem a cair.

**• Validade e Limitações dos Modelos Preditivos:** Modelos de previsão de preços do petróleo, como o Random Forest Regressor utilizado neste projeto, são valiosos para embasar decisões estratégicas de curto e médio prazo. No entanto, a análise mostrou que a precisão do modelo diminui para previsões mais longas.

**• Impacto das Políticas de Energia Renovável:** As políticas globais de transição para energias renováveis também têm um impacto significativo nos preços do petróleo.
""", unsafe_allow_html=True)

st.markdown("""
### Conclusões:

Em conclusão, o projeto demonstrou a viabilidade e a importância de utilizar técnicas de machine learning para prever preços de commodities como o petróleo Brent. A aplicação de um modelo Random Forest, juntamente com visualizações interativas, forneceu uma abordagem compreensiva para a análise e previsão de preços, destacando-se como uma ferramenta crucial para investidores e indústrias dependentes do petróleo.
Os insights obtidos com este projeto destacam a complexidade do mercado de petróleo e a importância de considerar múltiplos fatores ao prever os preços. A geopolítica, a força do dólar, a validade dos modelos preditivos e as políticas de energia renovável são todos elementos críticos que influenciam os preços do petróleo. Entender essas dinâmicas permite uma análise mais precisa e informada, essencial para a tomada de decisões estratégicas no setor energético.
""", unsafe_allow_html=True)
