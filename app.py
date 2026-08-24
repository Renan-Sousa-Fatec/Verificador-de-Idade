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
# CAMINHOS DOS ARQUIVOS
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
       FORÇA ESQUEMA DE CORES CLARO
       ======================================================== */

    html,
    body,
    [data-testid="stAppViewContainer"] {
        color-scheme: light !important;
    }


    /* ========================================================
       ESCONDE O CABEÇALHO PADRÃO
       ======================================================== */

    header[data-testid="stHeader"] {
        display: none !important;
    }


    /* ========================================================
       FUNDO DA APLICAÇÃO
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
       CONTAINER PRINCIPAL
       ======================================================== */

    .block-container {
        max-width: 762px !important;

        width: 100% !important;

        padding-top: 10px !important;

        padding-left: 16px !important;

        padding-right: 16px !important;

        padding-bottom: 0 !important;

        margin-left: auto !important;

        margin-right: auto !important;

        box-sizing: border-box !important;
    }


    /* ========================================================
       REDUZ ESPAÇAMENTOS PADRÃO
       ======================================================== */

    [data-testid="stVerticalBlock"] {
        gap: 0.15rem;
    }


    [data-testid="column"] {
        padding: 0 !important;
    }


    /* ========================================================
       CABEÇALHO
       ======================================================== */

    div[data-testid="stHorizontalBlock"]:first-of-type {
        align-items: center !important;
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

        white-space: normal !important;
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
       FORMULÁRIO
       ======================================================== */

    .form-column {
        width: 100%;

        max-width: 440px;

        margin-left: auto;

        margin-right: auto;
    }


    /* ========================================================
       LABELS
       ======================================================== */

    .stTextInput label {

        color: #17130F !important;

        font-family: "Courier New", monospace !important;

        font-size: 15px !important;

        font-weight: bold !important;

        margin-bottom: 4px !important;
    }


    /* ========================================================
       CAMPOS DE TEXTO
       ======================================================== */

    div[data-testid="stTextInput"] {

        width: 100% !important;

        max-width: 440px !important;

        margin-left: auto !important;

        margin-right: auto !important;

        box-sizing: border-box !important;
    }


    /* ========================================================
       MOLDURA EXTERNA
       ======================================================== */

    div[data-testid="stTextInput"] > div {

        width: 100% !important;

        height: 47px !important;

        background-color: #FFFFFF !important;

        border: 4px solid #17130F !important;

        border-radius: 15px !important;

        box-sizing: border-box !important;

        padding: 0 !important;

        box-shadow: none !important;
    }


    /* ========================================================
       CAMADA BASEWEB
       ======================================================== */

    div[data-testid="stTextInput"] div[data-baseweb="base-input"],
    div[data-testid="stTextInput"] div[data-baseweb="input"] {

        width: 100% !important;

        height: 39px !important;

        background-color: #FFFFFF !important;

        border: none !important;

        border-radius: 10px !important;

        box-shadow: none !important;

        padding: 0 !important;

        box-sizing: border-box !important;
    }


    /* ========================================================
       INPUT REAL
       ======================================================== */

    div[data-testid="stTextInput"] input,
    div[data-testid="stTextInput"] input:focus,
    div[data-testid="stTextInput"] input:active,
    div[data-testid="stTextInput"] input:hover {

        width: 100% !important;

        height: 39px !important;

        background: #FFFFFF !important;

        background-color: #FFFFFF !important;

        color: #17130F !important;

        -webkit-text-fill-color: #17130F !important;

        caret-color: #17130F !important;

        border: none !important;

        border-radius: 10px !important;

        outline: none !important;

        box-shadow: none !important;

        padding: 0 12px !important;

        box-sizing: border-box !important;

        font-family: "Courier New", monospace !important;

        font-size: 16px !important;

        font-weight: 900 !important;

        opacity: 1 !important;

        color-scheme: light !important;

        -webkit-appearance: none !important;

        appearance: none !important;
    }


    /* ========================================================
       FOCO DA CAIXA
       ======================================================== */

    div[data-testid="stTextInput"] > div:focus-within {

        background-color: #FFFFFF !important;

        border: 4px solid #17130F !important;

        box-shadow: none !important;
    }


    div[data-testid="stTextInput"] div[data-baseweb="base-input"]:focus-within,
    div[data-testid="stTextInput"] div[data-baseweb="input"]:focus-within {

        background-color: #FFFFFF !important;

        border: none !important;

        box-shadow: none !important;
    }


    /* ========================================================
       PLACEHOLDER
       ======================================================== */

    div[data-testid="stTextInput"] input::placeholder {

        color: #17130F !important;

        -webkit-text-fill-color: #17130F !important;

        opacity: 1 !important;
    }


    /* ========================================================
       ESPAÇAMENTO ENTRE CAMPOS
       ======================================================== */

    .field-space {
        height: 28px;
    }


    /* ========================================================
       ÁREA DO BOTÃO
       ======================================================== */

    .button-area {

        width: 100%;

        max-width: 440px;

        display: flex;

        justify-content: center;

        align-items: center;

        margin-left: auto;

        margin-right: auto;

        margin-top: 20px;

        margin-bottom: 10px;

        box-sizing: border-box;
    }


    /* ========================================================
       BOTÃO
       ======================================================== */

    .stButton {

        width: 100% !important;

        display: flex !important;

        justify-content: center !important;

        align-items: center !important;

        margin: 0 !important;
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

        transition: none !important;
    }


    /* ========================================================
       BOTÃO - HOVER / FOCUS / ACTIVE
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
       MENSAGENS DE RESULTADO
       ======================================================== */

    .custom-alert {

        width: 100%;

        max-width: 440px;

        margin: 10px auto;

        padding: 16px 20px;

        border-radius: 15px;

        border: 4px solid #17130F;

        font-family: "Courier New", monospace;

        font-weight: 900;

        font-size: 15px;

        line-height: 1.35;

        box-sizing: border-box;

        text-align: left;
    }


    /* ========================================================
       MAIOR DE IDADE
       ======================================================== */

    .custom-alert.success {

        background-color: #FFFFFF;

        color: #198754;
    }


    /* ========================================================
       MENOR DE IDADE / ERRO
       ======================================================== */

    .custom-alert.warning {

        background-color: #FFFFFF;

        color: #D90429;
    }


    /* ========================================================
       ESPAÇO ANTES DO RODAPÉ
       ======================================================== */

    .footer-space {
        height: 8px;
    }


    /* ========================================================
       RODAPÉ
       ======================================================== */

    .footer-column {

        width: 90%;

        margin-left: auto;

        margin-right: auto;
    }


    /* ========================================================
       TELAS PEQUENAS
       ======================================================== */

    @media (max-width: 480px) {

        h1 {
            font-size: 20px !important;
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
# TÍTULO E SUBTÍTULO
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

    # --------------------------------------------------------
    # NOME
    # --------------------------------------------------------

    nome = st.text_input(
        "Digite seu nome:"
    )


    # --------------------------------------------------------
    # ESPAÇO ENTRE OS CAMPOS
    # --------------------------------------------------------

    st.markdown(
        '<div class="field-space"></div>',
        unsafe_allow_html=True
    )


    # --------------------------------------------------------
    # IDADE
    # --------------------------------------------------------

    idade_texto = st.text_input(
        "Digite sua idade:",
        max_chars=3
    )


    # --------------------------------------------------------
    # BOTÃO
    # --------------------------------------------------------

    st.markdown(
        '<div class="button-area">',
        unsafe_allow_html=True
    )


    if st.button("Verificar"):

        try:

            idade = int(idade_texto)

            if idade < 0 or idade > 100:

                st.markdown(
                    '<div class="custom-alert warning">'
                    'Digite uma idade entre 0 e 100.'
                    '</div>',
                    unsafe_allow_html=True
                )

            elif idade < 18:

                st.markdown(
                    f'<div class="custom-alert warning">'
                    f'Infelizmente, {nome}, você não pode '
                    'acessar por ser menor de idade.'
                    '</div>',
                    unsafe_allow_html=True
                )

            else:

                st.markdown(
                    f'<div class="custom-alert success">'
                    f'Bem-vindo, {nome}! Você pode acessar '
                    'por ser maior de idade.'
                    '</div>',
                    unsafe_allow_html=True
                )

        except ValueError:

            st.markdown(
                '<div class="custom-alert warning">'
                'Digite uma idade válida.'
                '</div>',
                unsafe_allow_html=True
            )


    st.markdown(
        '</div>',
        unsafe_allow_html=True
    )


# ============================================================
# ESPAÇO ANTES DO RODAPÉ
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
