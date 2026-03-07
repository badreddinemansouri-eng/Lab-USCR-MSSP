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
    st.session_state.selected_tab = 0  # 0 = Accueil
if "mobile_menu_open" not in st.session_state:
    st.session_state.mobile_menu_open = False

def toggle_theme():
    st.session_state.theme = "dark" if st.session_state.theme == "light" else "light"

def open_menu():
    st.session_state.mobile_menu_open = True

def close_menu():
    st.session_state.mobile_menu_open = False

# Libellés des onglets
tab_labels = [
    get_text("nav_home", st.session_state.lang),
    get_text("nav_analyses", st.session_state.lang),
    get_text("nav_request", st.session_state.lang),
    get_text("nav_resources", st.session_state.lang),
    get_text("nav_contact", st.session_state.lang),
    get_text("nav_admin", st.session_state.lang)
]

# CSS pour le responsive (desktop vs mobile)
st.markdown(f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
    * {{ font-family: 'Inter', sans-serif; }}

    /* Thème clair/sombre */
    :root {{
        --bg-primary: {'#ffffff' if st.session_state.theme == 'light' else '#1a1a2e'};
        --text-primary: {'#1e2b4f' if st.session_state.theme == 'light' else '#e0e0e0'};
        --accent: #667eea;
        --accent-dark: #764ba2;
    }}
    body {{ background-color: var(--bg-primary); color: var(--text-primary); }}
    .stApp {{ background: var(--bg-primary); }}

    /* Onglets desktop */
    .desktop-only {{
        display: block;
    }}
    .mobile-only {{
        display: none;
    }}

    /* Style des onglets (identique à la version souhaitée) */
    .stTabs [data-baseweb="tab-list"] {{
        gap: 2rem;
        justify-content: center;
        background-color: #f8f9fa;
        padding: 0.5rem;
        border-radius: 10px;
        margin-bottom: 2rem;
    }}
    .stTabs [data-baseweb="tab"] {{
        font-size: 1.1rem;
        font-weight: 500;
        color: #2c3e50;
    }}
    .stTabs [aria-selected="true"] {{
        background-color: #667eea;
        color: white !important;
        border-radius: 5px;
    }}

    /* Header mobile */
    .mobile-header {{
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 1rem;
    }}
    .hamburger {{
        font-size: 2rem;
        background: none;
        border: none;
        color: var(--text-primary);
        cursor: pointer;
    }}
    .theme-lang-mobile {{
        display: flex;
        gap: 0.5rem;
    }}

    /* Menu mobile overlay */
    .mobile-menu {{
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: var(--bg-primary);
        z-index: 1000;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        gap: 2rem;
    }}
    .close-btn {{
        position: absolute;
        top: 20px;
        right: 30px;
        font-size: 2.5rem;
        background: none;
        border: none;
        color: var(--text-primary);
        cursor: pointer;
    }}
    .mobile-menu .stButton > button {{
        font-size: 1.8rem;
        background: transparent;
        border: none;
        color: var(--text-primary);
        padding: 0.5rem 2rem;
        border-radius: 40px;
        width: auto;
        box-shadow: none;
    }}
    .mobile-menu .stButton > button:hover {{
        background: rgba(102, 126, 234, 0.1);
    }}

    @media (max-width: 768px) {{
        .desktop-only {{
            display: none;
        }}
        .mobile-only {{
            display: block;
        }}
    }}
</style>
""", unsafe_allow_html=True)

# --- Version mobile : header avec hamburger et contrôles ---
st.markdown('<div class="mobile-only">', unsafe_allow_html=True)
col_hamburger, col_theme_lang = st.columns([1, 2])
with col_hamburger:
    if st.button("☰", key="hamburger"):
        open_menu()
        st.rerun()
with col_theme_lang:
    col_theme_mob, col_lang_mob = st.columns(2)
    with col_theme_mob:
        if st.button("☀️" if st.session_state.theme == "light" else "🌙", key="theme_mobile"):
            toggle_theme()
            st.rerun()
    with col_lang_mob:
        lang = st.selectbox("Langue", ["fr", "en"], index=0 if st.session_state.lang == "fr" else 1,
                            label_visibility="collapsed", key="lang_mobile")
        if lang != st.session_state.lang:
            st.session_state.lang = lang
            st.rerun()
st.markdown('</div>', unsafe_allow_html=True)

# --- Menu mobile (affiché si ouvert) ---
if st.session_state.mobile_menu_open:
    with st.container():
        st.markdown('<div class="mobile-menu">', unsafe_allow_html=True)
        if st.button("✕", key="close_menu"):
            close_menu()
            st.rerun()
        for i, label in enumerate(tab_labels):
            if st.button(label, key=f"mobile_nav_{i}"):
                st.session_state.selected_tab = i
                close_menu()
                st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

# --- Version desktop : onglets ---
with st.container():
    st.markdown('<div class="desktop-only">', unsafe_allow_html=True)
    # Barre de contrôle (thème et langue) en haut à droite
    col1, col2, col3 = st.columns([6, 1, 1])
    with col2:
        if st.button("☀️" if st.session_state.theme == "light" else "🌙", key="theme_desktop"):
            toggle_theme()
            st.rerun()
    with col3:
        lang = st.selectbox("Langue", ["fr", "en"], index=0 if st.session_state.lang == "fr" else 1,
                            label_visibility="collapsed", key="lang_desktop")
        if lang != st.session_state.lang:
            st.session_state.lang = lang
            st.rerun()

    # Onglets
    tabs = st.tabs(tab_labels)
    with tabs[st.session_state.selected_tab]:
        if st.session_state.selected_tab == 0:
            show_home()
        elif st.session_state.selected_tab == 1:
            show_analyses()
        elif st.session_state.selected_tab == 2:
            show_request()
        elif st.session_state.selected_tab == 3:
            show_resources()
        elif st.session_state.selected_tab == 4:
            show_contact()
        elif st.session_state.selected_tab == 5:
            show_admin()
    st.markdown('</div>', unsafe_allow_html=True)
