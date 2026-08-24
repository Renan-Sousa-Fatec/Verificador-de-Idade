import streamlit as st
from pathlib import Path


# ============================================================
# CONFIGURAÇÃO DA PÁGINA
# ============================================================

st.set_page_config(
    page_title="Bark Labs | Verificador de Idade",
    page_icon="🐶",
    layout="wide"
)


# ============================================================
# CAMINHOS
# ============================================================

BASE_DIR = Path(__file__).parent

LOGO_PATH = BASE_DIR / "assets" / "bark-labs.png"
FOOTER_PATH = BASE_DIR / "assets" / "rodape.png"


# ============================================================
# CSS
# ============================================================

st.markdown("""
<style>

    /* ========================================================
       FUNDO
       ======================================================== */

    .stApp {
        background-color: #FBE9A0 !important;
    }

    [data-testid="stAppViewContainer"] {
        background-color: #FBE9A0 !important;
    }

    [data-testid="stMain"] {
        background-color: #FBE9A0 !important;
    }


    /* ========================================================
       ESCONDE HEADER DO STREAMLIT
       ======================================================== */

    header[data-testid="stHeader"] {
        display: none !important;
    }


    /* ========================================================
       CONTAINER PRINCIPAL
       ======================================================== */

    .block-container {

        max-width: 762px !important;

        width: 100% !important;

        padding-top: 10px !important;

        padding-left: 16px !important;

        padding-right: 16px !important;

        padding-bottom: 10px !important;

        margin-left: auto !important;

        margin-right: auto !important;

        box-sizing: border-box !important;
    }


    /* ========================================================
       COLUNAS
       ======================================================== */

    [data-testid="column"] {
        padding: 0 !important;
    }


    /* ========================================================
       TÍTULO
       ======================================================== */

    h1 {

        color: #17130F !important;

        font-family: "Courier New", monospace !important;

        font-size: 28px !important;

        font-weight: 900 !important;

        text-align: center !important;

        margin-top: 30px !important;

        margin-bottom: 10px !important;
    }


    /* ========================================================
       SUBTÍTULO
       ======================================================== */

    .subtitle {

        color: #17130F;

        font-family: "Courier New", monospace;

        font-size: 14px;

        font-weight: bold;

        text-align: center;

        line-height: 1.25;

        margin-bottom: 18px;
    }


    /* ========================================================
       LABELS
       ======================================================== */

    .stTextInput label,
    .stNumberInput label {

        color: #17130F !important;

        font-family: "Courier New", monospace !important;

        font-size: 15px !important;

        font-weight: bold !important;

        margin-bottom: 4px !important;
    }


    /* ========================================================
       INPUTS
       
       IMPORTANTE:
       Não estamos colocando um monte de regras aqui.
       O teste mínimo mostrou que estas são suficientes.
       ======================================================== */

    div[data-testid="stTextInput"] input,
    div[data-testid="stNumberInput"] input {

        background-color: #FFFFFF !important;

        color: #17130F !important;

        -webkit-text-fill-color: #17130F !important;

        caret-color: #17130F !important;

        opacity: 1 !important;

        font-family: "Courier New", monospace !important;

        font-size: 16px !important;

        font-weight: 900 !important;
    }


    /* ========================================================
       INPUT FOCADO
       ======================================================== */

    div[data-testid="stTextInput"] input:focus,
    div[data-testid="stNumberInput"] input:focus {

        background-color: #FFFFFF !important;

        color: #17130F !important;

        -webkit-text-fill-color: #17130F !important;

        caret-color: #17130F !important;

        opacity: 1 !important;
    }


    /* ========================================================
       CAIXA DO NOME
       ======================================================== */

    div[data-testid="stTextInput"] > div {

        background-color: #FFFFFF !important;

        border: 4px solid #17130F !important;

        border-radius: 15px !important;

        box-shadow: none !important;
    }


    /* ========================================================
       CAIXA DA IDADE
       ======================================================== */

    div[data-testid="stNumberInput"] > div {

        background-color: #FFFFFF !important;

        border: 4px solid #17130F !important;

        border-radius: 15px !important;

        box-shadow: none !important;
    }


    /* ========================================================
       CAMADAS INTERNAS
       ======================================================== */

    div[data-testid="stTextInput"] div[data-baseweb="base-input"],
    div[data-testid="stNumberInput"] div[data-baseweb="input"] {

        background-color: #FFFFFF !important;

        border: none !important;

        box-shadow: none !important;
    }


    /* ========================================================
       REMOVE OS BOTÕES + E - DA IDADE
       ======================================================== */

    div[data-testid="stNumberInput"] button {

        display: none !important;

        visibility: hidden !important;
    }


    /* Chrome / Edge / Safari */

    div[data-testid="stNumberInput"] input::-webkit-inner-spin-button,
    div[data-testid="stNumberInput"] input::-webkit-outer-spin-button {

        -webkit-appearance: none !important;

        appearance: none !important;

        margin: 0 !important;
    }


    /* Firefox */

    div[data-testid="stNumberInput"] input[type="number"] {

        -moz-appearance: textfield !important;

        appearance: textfield !important;
    }


    /* ========================================================
       ESPAÇO ENTRE NOME E IDADE
       ======================================================== */

    .field-space {
        height: 25px;
    }


    /* ========================================================
       BOTÃO
       ======================================================== */

    .button-area {

        width: 100%;

        max-width: 440px;

        display: flex;

        justify-content: center;

        align-items: center;

        margin: 20px auto 10px auto;
    }


    .stButton {

        width: 100% !important;

        display: flex !important;

        justify-content: center !important;

        align-items: center !important;
    }


    .stButton button {

        width: 126px !important;

        min-width: 126px !important;

        height: 80px !important;

        min-height: 80px !important;

        padding: 0 !important;

        background-color: #B84D2D !important;

        color: #D8C8B0 !important;

        border: 4px solid #17130F !important;

        border-radius: 18px !important;

        box-sizing: border-box !important;

        font-family: "Courier New", monospace !important;

        font-size: 15px !important;

        font-weight: bold !important;

        box-shadow: none !important;

        outline: none !important;
    }


    /* ========================================================
       BOTÃO - NÃO MUDA AO CLICAR
       ======================================================== */

    .stButton button:hover,
    .stButton button:focus,
    .stButton button:active {

        background-color: #B84D2D !important;

        color: #D8C8B0 !important;

        border: 4px solid #17130F !important;

        box-shadow: none !important;

        outline: none !important;
    }


    /* ========================================================
       MENSAGEM DE RESULTADO
       ======================================================== */

    .custom-alert {

        width: 100%;

        max-width: 440px;

        margin: 12px auto 0 auto;

        padding: 16px 20px;

        background-color: #FFFFFF;

        border: 4px solid #17130F;

        border-radius: 15px;

        box-sizing: border-box;

        font-family: "Courier New", monospace;

        font-size: 15px;

        font-weight: 900;

        line-height: 1.35;

        text-align: left;
    }


    /* ========================================================
       SUCESSO
       ======================================================== */

    .custom-alert.success {
        color: #198754;
    }


    /* ========================================================
       MENOR DE IDADE / ERRO
       ======================================================== */

    .custom-alert.warning {
        color: #B84D2D;
    }


    /* ========================================================
       ESPAÇO EXTRA ENTRE RESPOSTA E RODAPÉ
       
       Aqui coloquei uma linha a mais.
       ======================================================== */

    .footer-space {

        height: 35px;
    }


    /* ========================================================
       RODAPÉ
       ======================================================== */

    .footer-image {

        width: 90%;

        margin-left: auto;

        margin-right: auto;
    }


    /* ========================================================
       CELULAR
       ======================================================== */

    @media (max-width: 480px) {

        h1 {
            font-size: 21px !important;
        }

        .subtitle {
            font-size: 13px;
        }

        .stButton button {

            width: 110px !important;

            min-width: 110px !important;

            height: 70px !important;

            min-height: 70px !important;

            font-size: 13px !important;
        }

    }

</style>
""", unsafe_allow_html=True)


# ============================================================
# CABEÇALHO
# ============================================================

logo_col, title_col, right_col = st.columns(
    [1.15, 3.85, 1],
    gap="small"
)


# ============================================================
# LOGO
# ============================================================

with logo_col:

    st.image(
        str(LOGO_PATH),
        width=115
    )


# ============================================================
# TÍTULO
# ============================================================

with title_col:

    st.title("VERIFICADOR DE IDADE")

    st.markdown(
        """
        <div class="subtitle">
            Descubra se você pode acessar<br>
            nosso sistema!
        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# FORMULÁRIO
# ============================================================

left, center, right = st.columns(
    [1, 3, 1],
    gap="small"
)


with center:

    # ========================================================
    # NOME
    # ========================================================

    nome = st.text_input(
        "Digite seu nome:"
    )


    # ========================================================
    # ESPAÇO
    # ========================================================

    st.markdown(
        '<div class="field-space"></div>',
        unsafe_allow_html=True
    )


    # ========================================================
    # IDADE
    # ========================================================

    idade = st.number_input(
        "Digite sua idade:",
        min_value=0,
        max_value=100,
        value=0,
        step=1
    )


    # ========================================================
    # BOTÃO
    # ========================================================

    st.markdown(
        '<div class="button-area">',
        unsafe_allow_html=True
    )

    verificar = st.button("Verificar")

    st.markdown(
        '</div>',
        unsafe_allow_html=True
    )


    # ========================================================
    # RESULTADO
    # ========================================================

    if verificar:

        if idade < 18:

            st.markdown(
                f"""
                <div class="custom-alert warning">
                    Infelizmente, {nome}, você não pode
                    acessar por ser menor de idade.
                </div>
                """,
                unsafe_allow_html=True
            )

        else:

            st.markdown(
                f"""
                <div class="custom-alert success">
                    Bem-vindo, {nome}! Você pode acessar
                    por ser maior de idade.
                </div>
                """,
                unsafe_allow_html=True
            )


# ============================================================
# ESPAÇO EXTRA ANTES DO RODAPÉ
# ============================================================

st.markdown(
    '<div class="footer-space"></div>',
    unsafe_allow_html=True
)


# ============================================================
# RODAPÉ
# ============================================================

footer_left, footer_center, footer_right = st.columns(
    [0.05, 0.90, 0.05],
    gap="small"
)


with footer_center:

    st.image(
        str(FOOTER_PATH),
        use_container_width=True
    )
