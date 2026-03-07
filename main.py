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

# États de session
if "theme" not in st.session_state:
    st.session_state.theme = "light"
if "lang" not in st.session_state:
    st.session_state.lang = "fr"
if "selected_tab" not in st.session_state:
    st.session_state.selected_tab = 0

def toggle_theme():
    st.session_state.theme = "dark" if st.session_state.theme == "light" else "light"

# Libellés des onglets
tab_labels = [
    get_text("nav_home", st.session_state.lang),
    get_text("nav_analyses", st.session_state.lang),
    get_text("nav_request", st.session_state.lang),
    get_text("nav_resources", st.session_state.lang),
    get_text("nav_contact", st.session_state.lang),
    get_text("nav_admin", st.session_state.lang)
]

# CSS minimal (uniquement pour le thème et le style des onglets)
st.markdown(f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
    * {{ font-family: 'Inter', sans-serif; }}
    body {{ background: {'#ffffff' if st.session_state.theme == 'light' else '#1a1a2e'}; }}
    .stApp {{ background: inherit; }}
    .main .block-container {{ background: inherit; }}
    .stTabs [data-baseweb="tab-list"] {{
        gap: 2rem;
        justify-content: center;
        background-color: {'#f8f9fa' if st.session_state.theme == 'light' else '#16213e'};
        padding: 0.5rem;
        border-radius: 10px;
        margin-bottom: 2rem;
    }}
    .stTabs [data-baseweb="tab"] {{
        font-size: 1.1rem;
        font-weight: 500;
        color: {'#2c3e50' if st.session_state.theme == 'light' else '#e0e0e0'};
    }}
    .stTabs [aria-selected="true"] {{
        background-color: #667eea;
        color: white !important;
        border-radius: 5px;
    }}
</style>
""", unsafe_allow_html=True)

# Barre de contrôle (thème et langue) en haut à droite
col1, col2, col3 = st.columns([6, 1, 1])
with col2:
    if st.button("☀️" if st.session_state.theme == "light" else "🌙", key="theme_btn"):
        toggle_theme()
        st.rerun()
with col3:
    lang = st.selectbox("Langue", ["fr", "en"], index=0 if st.session_state.lang == "fr" else 1,
                        label_visibility="collapsed", key="lang_selector")
    if lang != st.session_state.lang:
        st.session_state.lang = lang
        st.rerun()

# Onglets
tabs = st.tabs(tab_labels)

# Afficher le contenu de l'onglet sélectionné
with tabs[0]:
    show_home()
with tabs[1]:
    show_analyses()
with tabs[2]:
    show_request()
with tabs[3]:
    show_resources()
with tabs[4]:
    show_contact()
with tabs[5]:
    show_admin()
