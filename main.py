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

# Mode debug
if not st.secrets.get("debug", False):
    st.set_option('client.showErrorDetails', False)

# Initialisation des états de session
if "theme" not in st.session_state:
    st.session_state.theme = "light"
if "lang" not in st.session_state:
    st.session_state.lang = "fr"

# Fonction pour basculer le thème
def toggle_theme():
    st.session_state.theme = "dark" if st.session_state.theme == "light" else "light"

# CSS global
st.markdown(f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;900&family=Inter:wght@300;400;500;600;700&display=swap');

    :root {{
        --bg-primary: {'#ffffff' if st.session_state.theme == 'light' else '#1a1a2e'};
        --bg-secondary: {'#f8f9fa' if st.session_state.theme == 'light' else '#16213e'};
        --text-primary: {'#1e2b4f' if st.session_state.theme == 'light' else '#e0e0e0'};
        --text-secondary: {'#5a6b7e' if st.session_state.theme == 'light' else '#b0b0b0'};
        --accent: #1e2b4f;
        --accent-light: #2a3f6e;
        --card-bg: {'rgba(255,255,255,0.7)' if st.session_state.theme == 'light' else 'rgba(30,30,50,0.7)'};
        --card-border: {'rgba(0,0,0,0.05)' if st.session_state.theme == 'light' else 'rgba(255,255,255,0.05)'};
        --shadow: {'0 10px 30px rgba(0,0,0,0.05)' if st.session_state.theme == 'light' else '0 10px 30px rgba(0,0,0,0.3)'};
        --blur-amount: 10px;
    }}

    /* Appliquer les couleurs */
    body {{
        background-color: var(--bg-primary);
        color: var(--text-primary);
        transition: background-color 0.3s, color 0.3s;
    }}

    .stApp {{
        background: var(--bg-primary);
    }}

    .main .block-container {{
        background: var(--bg-primary);
        box-shadow: var(--shadow);
        padding-top: 1rem;
    }}

    /* Header avec contrôles */
    .header-controls {{
        display: flex;
        justify-content: flex-end;
        gap: 1rem;
        margin-bottom: 1rem;
        align-items: center;
    }}

    .theme-toggle, .lang-select {{
        background: var(--card-bg);
        backdrop-filter: blur(var(--blur-amount));
        border: 1px solid var(--card-border);
        border-radius: 40px;
        padding: 0.5rem 1.2rem;
        color: var(--text-primary);
        cursor: pointer;
        transition: all 0.3s;
        font-size: 1rem;
    }}

    .theme-toggle:hover, .lang-select:hover {{
        transform: scale(1.05);
        background: var(--accent-light);
        color: white;
    }}

    /* Onglets */
    .stTabs [data-baseweb="tab-list"] {{
        gap: 0.5rem;
        background: var(--card-bg);
        backdrop-filter: blur(var(--blur-amount));
        border-radius: 60px;
        padding: 0.5rem;
        border: 1px solid var(--card-border);
        margin-bottom: 2rem;
        flex-wrap: wrap;
    }}

    .stTabs [data-baseweb="tab"] {{
        color: var(--text-primary);
        border-radius: 40px;
        padding: 0.5rem 1.5rem;
        font-weight: 500;
        transition: all 0.2s;
    }}

    .stTabs [aria-selected="true"] {{
        background: var(--accent) !important;
        color: white !important;
    }}

    /* Hero section */
    .hero {{
        position: relative;
        overflow: hidden;
        padding: 4rem 2rem;
        background: linear-gradient(135deg, var(--accent) 0%, var(--accent-light) 100%);
        color: white;
        border-radius: 40px;
        margin-bottom: 2rem;
    }}

    .hero::before {{
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1440 320"><path fill="rgba(255,255,255,0.1)" d="M0,96L48,112C96,128,192,160,288,186.7C384,213,480,235,576,213.3C672,192,768,128,864,117.3C960,107,1056,149,1152,165.3C1248,181,1344,171,1392,165.3L1440,160L1440,320L1392,320C1344,320,1248,320,1152,320C1056,320,960,320,864,320C768,320,672,320,576,320C480,320,384,320,288,320C192,320,96,320,48,320L0,320Z"/></svg>') repeat-x bottom;
        animation: wave 15s linear infinite;
        opacity: 0.3;
    }}

    @keyframes wave {{
        0% {{ background-position: 0 0; }}
        100% {{ background-position: 1440px 0; }}
    }}

    /* Cartes */
    .info-card, .analysis-card {{
        background: var(--card-bg);
        backdrop-filter: blur(var(--blur-amount));
        border: 1px solid var(--card-border);
        border-radius: 24px;
        padding: 2rem;
        box-shadow: var(--shadow);
        transition: transform 0.3s, box-shadow 0.3s;
    }}

    .info-card:hover, .analysis-card:hover {{
        transform: translateY(-8px) scale(1.02);
        box-shadow: 0 30px 60px rgba(0,0,0,0.15);
    }}

    /* Boutons */
    .stButton > button {{
        background: linear-gradient(135deg, var(--accent) 0%, var(--accent-light) 100%);
        color: white;
        border: none;
        border-radius: 50px;
        padding: 0.8rem 2rem;
        font-weight: 600;
        transition: all 0.3s;
        box-shadow: 0 8px 20px rgba(26,54,93,0.2);
        width: 100%;
    }}

    .stButton > button:hover {{
        transform: translateY(-3px);
        box-shadow: 0 15px 30px rgba(26,54,93,0.3);
        filter: brightness(1.1);
    }}

    /* Responsive */
    @media (max-width: 768px) {{
        .hero {{ padding: 2rem 1rem; }}
        .stTabs [data-baseweb="tab"] {{ font-size: 0.9rem; padding: 0.4rem 1rem; }}
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
    lang = st.selectbox("Langue", ["fr", "en"], index=0 if st.session_state.lang == "fr" else 1, label_visibility="collapsed", key="lang_selector")
    if lang != st.session_state.lang:
        st.session_state.lang = lang
        st.rerun()

# Navigation par onglets
tabs = st.tabs([
    get_text("nav_home", st.session_state.lang),
    get_text("nav_analyses", st.session_state.lang),
    get_text("nav_request", st.session_state.lang),
    get_text("nav_resources", st.session_state.lang),
    get_text("nav_contact", st.session_state.lang),
    get_text("nav_admin", st.session_state.lang)
])

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
