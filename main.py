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
if "page" not in st.session_state:
    st.session_state.page = get_text("nav_home", st.session_state.lang)
if "mobile_menu_open" not in st.session_state:
    st.session_state.mobile_menu_open = False

def toggle_theme():
    st.session_state.theme = "dark" if st.session_state.theme == "light" else "light"

def open_menu():
    st.session_state.mobile_menu_open = True

def close_menu():
    st.session_state.mobile_menu_open = False

# Libellés de navigation
nav_labels = [
    get_text("nav_home", st.session_state.lang),
    get_text("nav_analyses", st.session_state.lang),
    get_text("nav_request", st.session_state.lang),
    get_text("nav_resources", st.session_state.lang),
    get_text("nav_contact", st.session_state.lang),
    get_text("nav_admin", st.session_state.lang)
]

# CSS minimal et clair
st.markdown(f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap');
    * {{ font-family: 'Inter', sans-serif; margin: 0; padding: 0; box-sizing: border-box; }}
    body {{ background: {'#fff' if st.session_state.theme == 'light' else '#1a1a2e'}; }}
    .stApp {{ background: inherit; }}

    /* Barre de navigation desktop */
    .desktop-nav {{
        display: flex;
        justify-content: space-between;
        align-items: center;
        background: transparent;
        padding: 0.5rem 0;
        margin-bottom: 2rem;
        border-bottom: 1px solid rgba(0,0,0,0.1);
    }}
    .nav-links {{
        display: flex;
        gap: 2rem;
        flex-wrap: wrap;
    }}
    .nav-link {{
        background: none;
        border: none;
        color: {'#1e2b4f' if st.session_state.theme == 'light' else '#fff'};
        font-size: 1rem;
        font-weight: 500;
        cursor: pointer;
        padding: 0.25rem 0;
        border-bottom: 2px solid transparent;
        transition: border-color 0.2s;
    }}
    .nav-link:hover {{
        border-bottom-color: #1e2b4f;
    }}
    .nav-link.active {{
        border-bottom-color: #1e2b4f;
        font-weight: 600;
    }}
    .nav-controls {{
        display: flex;
        gap: 1rem;
        align-items: center;
    }}
    .theme-btn, .lang-select {{
        background: transparent;
        border: 1px solid rgba(0,0,0,0.1);
        border-radius: 20px;
        padding: 0.3rem 1rem;
        font-size: 0.9rem;
        cursor: pointer;
        color: inherit;
    }}
    .theme-btn:hover, .lang-select:hover {{
        background: rgba(0,0,0,0.05);
    }}

    /* Header mobile */
    .mobile-header {{
        display: none;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 1rem;
    }}
    .hamburger {{
        font-size: 2rem;
        background: none;
        border: none;
        color: inherit;
        cursor: pointer;
    }}

    /* Menu mobile overlay */
    .mobile-menu {{
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: {'#fff' if st.session_state.theme == 'light' else '#1a1a2e'};
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
        color: inherit;
        cursor: pointer;
    }}
    .mobile-menu .nav-link {{
        font-size: 1.8rem;
        border-bottom: none;
    }}

    @media (max-width: 768px) {{
        .desktop-nav {{
            display: none;
        }}
        .mobile-header {{
            display: flex;
        }}
    }}
</style>
""", unsafe_allow_html=True)

# --- En-tête mobile (visible sur petits écrans) ---
st.markdown('<div class="mobile-header">', unsafe_allow_html=True)
if st.button("☰", key="hamburger"):
    open_menu()
    st.rerun()
st.markdown('<div style="flex-grow:1;"></div>', unsafe_allow_html=True)
col_theme_mobile, col_lang_mobile = st.columns(2)
with col_theme_mobile:
    if st.button("☀️" if st.session_state.theme == "light" else "🌙", key="theme_mobile"):
        toggle_theme()
        st.rerun()
with col_lang_mobile:
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
        for i, label in enumerate(nav_labels):
            active_class = "active" if st.session_state.page == label else ""
            # Utiliser un bouton pour chaque lien (car Streamlit n'a pas de lien natif)
            if st.button(label, key=f"mobile_nav_{i}"):
                st.session_state.page = label
                close_menu()
                st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

# --- Barre de navigation desktop ---
with st.container():
    st.markdown('<div class="desktop-nav">', unsafe_allow_html=True)
    st.markdown('<div class="nav-links">', unsafe_allow_html=True)
    for i, label in enumerate(nav_labels):
        active_class = "active" if st.session_state.page == label else ""
        # Utiliser un bouton pour chaque lien
        if st.button(label, key=f"desktop_nav_{i}"):
            st.session_state.page = label
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('<div class="nav-controls">', unsafe_allow_html=True)
    col_theme, col_lang = st.columns(2)
    with col_theme:
        if st.button("☀️" if st.session_state.theme == "light" else "🌙", key="theme_desktop"):
            toggle_theme()
            st.rerun()
    with col_lang:
        lang = st.selectbox("Langue", ["fr", "en"], index=0 if st.session_state.lang == "fr" else 1,
                            label_visibility="collapsed", key="lang_desktop")
        if lang != st.session_state.lang:
            st.session_state.lang = lang
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# --- Routage ---
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
