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
if "menu_open" not in st.session_state:
    st.session_state.menu_open = False

def toggle_theme():
    st.session_state.theme = "dark" if st.session_state.theme == "light" else "light"

def open_menu():
    st.session_state.menu_open = True

def close_menu():
    st.session_state.menu_open = False

nav_labels = [
    get_text("nav_home", st.session_state.lang),
    get_text("nav_analyses", st.session_state.lang),
    get_text("nav_request", st.session_state.lang),
    get_text("nav_resources", st.session_state.lang),
    get_text("nav_contact", st.session_state.lang),
    get_text("nav_admin", st.session_state.lang)
]

# CSS modernisé (inclut le style pour le menu mobile)
st.markdown(f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
    * {{ font-family: 'Inter', sans-serif; }}
    body {{ background: {'#fff' if st.session_state.theme == 'light' else '#1a1a2e'}; }}
    .stApp {{ background: inherit; }}

    /* Barre desktop */
    .desktop-nav {{
        display: flex;
        justify-content: space-between;
        align-items: center;
        background: rgba(255,255,255,0.1);
        backdrop-filter: blur(10px);
        border-radius: 40px;
        padding: 0.5rem 1rem;
        margin-bottom: 2rem;
        border: 1px solid rgba(0,0,0,0.05);
    }}
    .desktop-nav .nav-links {{
        display: flex;
        gap: 0.5rem;
        flex-wrap: wrap;
    }}
    .desktop-nav .nav-links .stButton > button {{
        background: transparent;
        border: none;
        color: {'#1e2b4f' if st.session_state.theme == 'light' else '#fff'};
        padding: 0.5rem 1.2rem;
        border-radius: 40px;
        font-weight: 500;
        box-shadow: none;
        width: auto;
    }}
    .desktop-nav .nav-links .stButton > button:hover {{
        background: rgba(26,54,93,0.1);
    }}
    .desktop-nav .nav-controls {{
        display: flex;
        gap: 0.5rem;
        align-items: center;
    }}
    .desktop-nav .nav-controls .stButton > button,
    .desktop-nav .nav-controls .stSelectbox {{
        min-width: 40px;
        padding: 0.3rem 0.8rem;
        font-size: 0.9rem;
        background: transparent;
        color: {'#1e2b4f' if st.session_state.theme == 'light' else '#fff'};
        border: 1px solid rgba(0,0,0,0.1);
        border-radius: 40px;
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
        cursor: pointer;
        background: none;
        border: none;
        color: {'#1e2b4f' if st.session_state.theme == 'light' else '#fff'};
        padding: 0 1rem;
    }}

    /* Menu mobile slide-in */
    .mobile-menu {{
        position: fixed;
        top: 0;
        left: 0;
        width: 80%;
        height: 100%;
        background: {'#fff' if st.session_state.theme == 'light' else '#1a1a2e'};
        z-index: 1000;
        transform: translateX(-100%);
        transition: transform 0.3s ease-in-out;
        box-shadow: 2px 0 10px rgba(0,0,0,0.3);
        padding: 2rem;
        display: flex;
        flex-direction: column;
        gap: 1rem;
    }}
    .mobile-menu.open {{
        transform: translateX(0);
    }}
    .mobile-menu .stButton > button {{
        font-size: 1.5rem;
        background: transparent;
        border: none;
        color: {'#1e2b4f' if st.session_state.theme == 'light' else '#fff'};
        padding: 0.8rem 2rem;
        border-radius: 40px;
        font-weight: 500;
        width: 100%;
        text-align: left;
        box-shadow: none;
    }}
    .mobile-menu .stButton > button:hover {{
        background: rgba(26,54,93,0.1);
    }}
    .close-btn {{
        font-size: 2rem;
        align-self: flex-end;
        cursor: pointer;
        color: {'#1e2b4f' if st.session_state.theme == 'light' else '#fff'};
        margin-bottom: 1rem;
    }}
    .menu-overlay {{
        display: none;
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: rgba(0,0,0,0.5);
        z-index: 999;
    }}
    .menu-overlay.open {{
        display: block;
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

# En-tête mobile
st.markdown('<div class="mobile-header">', unsafe_allow_html=True)
if st.button("☰", key="hamburger_btn"):
    open_menu()
st.markdown('<div style="flex-grow:1;"></div>', unsafe_allow_html=True)
col_theme_mobile, col_lang_mobile = st.columns(2)
with col_theme_mobile:
    if st.button("☀️" if st.session_state.theme == "light" else "🌙", key="theme_btn_mobile"):
        toggle_theme()
        st.rerun()
with col_lang_mobile:
    lang = st.selectbox("Langue", ["fr", "en"], index=0 if st.session_state.lang == "fr" else 1,
                        label_visibility="collapsed", key="lang_selector_mobile")
    if lang != st.session_state.lang:
        st.session_state.lang = lang
        st.rerun()
st.markdown('</div>', unsafe_allow_html=True)

# Menu mobile (affiché conditionnellement)
if st.session_state.menu_open:
    with st.container():
        st.markdown('<div class="mobile-menu open">', unsafe_allow_html=True)
        # Bouton de fermeture (croix)
        if st.button("✕", key="close_menu_btn"):
            close_menu()
            st.rerun()
        # Liens de navigation
        for i, label in enumerate(nav_labels):
            if st.button(label, key=f"mobile_nav_{i}"):
                st.session_state.page = label
                close_menu()
                st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
        # Overlay
        st.markdown('<div class="menu-overlay open" onclick="document.getElementById(\'close_menu_btn\').click();"></div>', unsafe_allow_html=True)

# Barre de navigation desktop
with st.container():
    st.markdown('<div class="desktop-nav">', unsafe_allow_html=True)
    st.markdown('<div class="nav-links">', unsafe_allow_html=True)
    for i, label in enumerate(nav_labels):
        if st.button(label, key=f"desktop_nav_{i}"):
            st.session_state.page = label
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('<div class="nav-controls">', unsafe_allow_html=True)
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
