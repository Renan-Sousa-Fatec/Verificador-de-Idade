import streamlit as st

st.set_page_config(
    page_title="Teste",
    layout="centered"
)

st.markdown("""
<style>

.stApp {
    background-color: #FBE9A0 !important;
}

input {
    background-color: white !important;
    color: black !important;
    -webkit-text-fill-color: black !important;
    caret-color: black !important;
    opacity: 1 !important;
}

</style>
""", unsafe_allow_html=True)

st.title("TESTE")

nome = st.text_input("Digite alguma coisa:")

st.write("Valor recebido:", nome)
