import streamlit as st

import streamlit as st

# Sample data (replace with your actual data)
student_data = [
    {"nome": "Antônio Leão", "matricula": "RM349640"},
    {"nome": "Frederico Quesado", "matricula": "RM352633"},
    {"nome": "Lucas Tabelini", "matricula": "RM352725"},
    {"nome": "Renan Carneiro", "matricula": "RM352715"},
    {"nome": "Vanessa Andrade", "matricula": "RM352921"},
    # Add more students as needed
]

# Page title
st.title("Grupo Responsável")

# Display student information using badges
for student in student_data:
    st.markdown(
        f"""
        <div style="border: 1px solid #ddd; padding: 10px; border-radius: 5px; margin-bottom: 10px;">
            <p><strong>Nome:</strong> {student['nome']}</p>
            <p><strong>Número de Matrícula:</strong> {student['matricula']}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )