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
       CONFIGURAÇÃO GERAL
       ======================================================== */

    html, body {
        color-scheme: light !important;
    }

    header[data-testid="stHeader"] {
        display: none !important;
    }

    .stApp, [data-testid="stAppViewContainer"], [data-testid="stMain"] {
        background-color: #FBE9A0 !important;
    }

    .block-container {
        max-width: 762px !important;
        width: 100% !important;
        padding: 10px 16px 0 16px !important;
        margin: 0 auto !important;
        box-sizing: border-box !important;
    }

    [data-testid="stVerticalBlock"] {
        gap: 0.15rem;
    }

    [data-testid="column"] {
        padding: 0 !important;
    }

    h1 {
        color: #17130F !important;
        font-family: "Courier New", monospace !important;
        font-size: 28px !important;
        font-weight: 900 !important;
        text-align: center !important;
        margin: 30px 0 10px 0 !important;
    }

    .subtitle {
        color: #17130F;
        font-family: "Courier New", monospace;
        font-size: 14px;
        font-weight: bold;
        text-align: center;
        line-height: 1.25;
        margin-bottom: 18px;
    }

    .stTextInput label {
        color: #17130F !important;
        font-family: "Courier New", monospace !important;
        font-size: 15px !important;
        font-weight: bold !important;
        margin-bottom: 4px !important;
    }

    /* ========================================================
       SOLUÇÃO DEFINITIVA DO INPUT (PC E MOBILE)
       ======================================================== */

    /* Esconde as instruções nativas "Press Enter to apply" */
    div[data-testid="stTextInput"] [data-testid="stInputInstructions"] {
        display: none !important;
    }

    /* Caixa principal do Input */
    div[data-testid="stTextInput"] {
        width: 100% !important;
        max-width: 440px !important;
        margin: 0 auto !important;
    }

    /* Moldura + Fundo Branco em todos os estados da caixa */
    div[data-testid="stTextInput"] > div,
    div[data-testid="stTextInput"] div[data-baseweb="input"],
    div[data-testid="stTextInput"] div[data-baseweb="base-input"] {
        width: 100% !important;
        height: 47px !important;
        background-color: #FFFFFF !important;
        border: 4px solid #17130F !important;
        border-radius: 15px !important;
        padding: 0 !important;
        box-shadow: none !important;
    }

    /* Força o texto PRETO enquanto digita (Foco, Ativo e Hover) */
    div[data-testid="stTextInput"] input,
    div[data-testid="stTextInput"] input:focus,
    div[data-testid="stTextInput"] input:active,
    div[data-testid="stTextInput"] input:hover,
    div[data-testid="stTextInput"] input:-webkit-autofill {
        color: #17130F !important;
        -webkit-text-fill-color: #17130F !important;
        background-color: #FFFFFF !important;
        background: #FFFFFF !important;
        caret-color: #17130F !important;
        font-family: "Courier New", monospace !important;
        font-size: 16px !important;
        font-weight: 900 !important;
        opacity: 1 !important;
        border: none !important;
        outline: none !important;
        box-shadow: none !important;
        padding: 0 12px !important;
        height: 39px !important;
    }

    .field-space {
        height: 28px;
    }

    /* ========================================================
       BOTÃO E ALERTAS
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
    }

    .stButton button,
    .stButton button:hover,
    .stButton button:focus,
    .stButton button:active {
        width: 126px !important;
        min-width: 126px !important;
        height: 80px !important;
        min-height: 80px !important;
        padding: 0 !important;
        background-color: #B84D2D !important;
        color: #D8C8B0 !important;
        border: 4px solid #17130F !important;
        border-radius: 18px !important;
        font-family: "Courier New", monospace !important;
        font-size: 15px !important;
        font-weight: bold !important;
        box-shadow: none !important;
        outline: none !important;
    }

    .custom-alert {
        width: 100%;
        max-width: 440px;
        margin: 10px auto;
        padding: 16px 20px;
        border-radius: 15px;
        border: 4px solid #17130F;
        background-color: #FFFFFF;
        font-family: "Courier New", monospace;
        font-weight: 900;
        font-size: 15px;
        line-height: 1.35;
        box-sizing: border-box;
        text-align: left;
    }

    .custom-alert.success { color: #198754; }
    .custom-alert.warning { color: #D90429; }

    .footer-space { height: 8px; }

    @media (max-width: 480px) {
        h1 { font-size: 20px !important; }
        .subtitle { font-size: 13px; }
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

    idade_texto = st.text_input(
        "Digite sua idade:"
    )


    # ========================================================
    # BOTÃO
    # ========================================================

    st.markdown(
        '<div class="button-area">',
        unsafe_allow_html=True
    )


    if st.button("Verificar"):

        try:

            idade = int(idade_texto)

            # ------------------------------------------------
            # IDADE INVÁLIDA
            # ------------------------------------------------

            if idade < 0 or idade > 100:

                st.markdown(
                    """
                    <div class="custom-alert warning">
                        Digite uma idade entre 0 e 100.
                    </div>
                    """,
                    unsafe_allow_html=True
                )


            # ------------------------------------------------
            # MENOR DE IDADE
            # ------------------------------------------------

            elif idade < 18:

                st.markdown(
                    f"""
                    <div class="custom-alert warning">
                        Infelizmente, {nome}, você não pode
                        acessar por ser menor de idade.
                    </div>
                    """,
                    unsafe_allow_html=True
                )


            # ------------------------------------------------
            # MAIOR DE IDADE
            # ------------------------------------------------

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


        # ----------------------------------------------------
        # TEXTO NÃO NUMÉRICO
        # ----------------------------------------------------

        except ValueError:

            st.markdown(
                """
                <div class="custom-alert warning">
                    Digite uma idade válida.
                </div>
                """,
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
