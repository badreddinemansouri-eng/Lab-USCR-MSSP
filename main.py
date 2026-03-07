import streamlit as st
from home import show_home
from analyses import show_analyses
from request import show_request
from resources import show_resources
from contact import show_contact
from admin import show_admin
from bet import show_bet
from porosite import show_porosite
from isothermes import show_isothermes
from utils_i18n import get_text

st.set_page_config(
    page_title="USR Mesure de Surface Spécifique et Porosité",
    page_icon="🧪",
    layout="wide",
    initial_sidebar_state="collapsed"
)

if not st.secrets.get("debug", False):
    st.set_option('client.showErrorDetails', False)

if "theme" not in st.session_state:
    st.session_state.theme = "light"
if "lang" not in st.session_state:
    st.session_state.lang = "fr"
if "page" not in st.session_state:
    st.session_state.page = get_text("nav_home", st.session_state.lang)

def toggle_theme():
    st.session_state.theme = "dark" if st.session_state.theme == "light" else "light"

# CSS minimal pour la barre de navigation (juste pour que les colonnes se comportent bien)
st.markdown("""
<style>
    /* Réinitialiser les marges/paddings des colonnes pour la barre de navigation */
    .nav-row {
        display: flex;
        align-items: center;
        gap: 0.5rem;
        margin-bottom: 2rem;
        flex-wrap: wrap;
    }
    .nav-item {
        flex: 0 0 auto;
    }
    .nav-item .stButton > button {
        background: transparent;
        border: none;
        padding: 0.5rem 1rem;
        border-radius: 40px;
        font-weight: 500;
        width: auto;
    }
    .nav-item .stButton > button:hover {
        background: rgba(0,0,0,0.05);
    }
    .control-group {
        display: flex;
        gap: 0.5rem;
        margin-left: auto;
        align-items: center;
    }
    .control-group .stButton > button,
    .control-group .stSelectbox {
        min-width: 40px;
        padding: 0.3rem 0.8rem;
        font-size: 0.9rem;
    }
    @media (max-width: 768px) {
        .nav-row {
            justify-content: center;
        }
        .control-group {
            margin-left: 0;
            width: 100%;
            justify-content: center;
        }
    }
</style>
""", unsafe_allow_html=True)

# Libellés de navigation
nav_labels = [
    get_text("nav_home", st.session_state.lang),
    get_text("nav_analyses", st.session_state.lang),
    get_text("nav_request", st.session_state.lang),
    get_text("nav_resources", st.session_state.lang),
    get_text("nav_contact", st.session_state.lang),
    get_text("nav_admin", st.session_state.lang)
]

# Construction de la barre de navigation avec une ligne flex
st.markdown('<div class="nav-row">', unsafe_allow_html=True)

# Boutons de navigation
for label in nav_labels:
    st.markdown('<div class="nav-item">', unsafe_allow_html=True)
    if st.button(label, key=f"nav_{label}"):
        st.session_state.page = label
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# Contrôles (thème et langue) dans un groupe à droite
st.markdown('<div class="control-group">', unsafe_allow_html=True)
col_theme, col_lang = st.columns(2)
with col_theme:
    if st.button("☀️" if st.session_state.theme == "light" else "🌙", key="theme_btn"):
        toggle_theme()
        st.rerun()
with col_lang:
    lang = st.selectbox("Langue", ["fr", "en"], index=0 if st.session_state.lang == "fr" else 1,
                        label_visibility="collapsed", key="lang_selector")
    if lang != st.session_state.lang:
        st.session_state.lang = lang
        st.rerun()
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# Routage
if st.session_state.page == get_text("nav_home", st.session_state.lang):
    show_home()
elif st.session_state.page == get_text("nav_analyses", st.session_state.lang):
    show_analyses()
elif st.session_state.page == get_text("nav_request", st.session_state.lang):
    show_request()
elif st.session_state.page == get_text("nav_resources", st.session_state.lang):
    show_resources()
elif st.session_state.page == get_text("nav_contact", st.session_state.lang):
    show_contact()
elif st.session_state.page == get_text("nav_admin", st.session_state.lang):
    show_admin()
