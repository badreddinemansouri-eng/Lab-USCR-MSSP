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

nav_labels = [
    get_text("nav_home", st.session_state.lang),
    get_text("nav_analyses", st.session_state.lang),
    get_text("nav_request", st.session_state.lang),
    get_text("nav_resources", st.session_state.lang),
    get_text("nav_contact", st.session_state.lang),
    get_text("nav_admin", st.session_state.lang)
]

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
        padding: 2rem;
        border-radius: 10px;
        max-width: 1200px;
        margin: 0 auto;
    }}
    .hero {{
        position: relative;
        overflow: hidden;
        padding: 4rem 2rem;
        background: linear-gradient(135deg, var(--accent) 0%, var(--accent-light) 100%);
        color: white;
        border-radius: 40px;
        margin-bottom: 2rem;
        animation: fadeInUp 0.8s ease;
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
    .info-card, .analysis-card {{
        background: var(--card-bg);
        backdrop-filter: blur(var(--blur-amount));
        border: 1px solid var(--card-border);
        border-radius: 24px;
        padding: 2rem;
        box-shadow: var(--shadow);
        transition: transform 0.3s, box-shadow 0.3s;
        animation: fadeInUp 0.8s ease;
    }}
    .info-card:hover, .analysis-card:hover {{
        transform: translateY(-8px) scale(1.02);
        box-shadow: 0 30px 60px rgba(0,0,0,0.15);
    }}
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
    /* Indicateur de page active : barre orange */
    .active-indicator {{
        height: 4px;
        width: 80%;
        margin: 4px auto 0;
        background: #ffaa00;
        border-radius: 2px;
    }}
    /* Sélecteur de langue plus petit */
    .lang-col .stSelectbox {{
        transform: scale(0.7);
        transform-origin: left center;
        margin-left: -10px; /* pour compenser l'espace */
    }}
    @media (max-width: 768px) {{
        .hero {{ padding: 2rem 1rem; }}
    }}
</style>
""", unsafe_allow_html=True)

cols = st.columns(len(nav_labels) + 1)
for i, label in enumerate(nav_labels):
    with cols[i]:
        if st.button(label, key=f"nav_{i}", use_container_width=True):
            st.session_state.page = label
            st.rerun()
        if st.session_state.page == label:
            st.markdown('<div class="active-indicator"></div>', unsafe_allow_html=True)

with cols[-1]:
    st.markdown('<div class="lang-col">', unsafe_allow_html=True)
    lang = st.selectbox("Langue", ["fr", "en"], index=0 if st.session_state.lang == "fr" else 1,
                        label_visibility="collapsed", key="lang_selector")
    st.markdown('</div>', unsafe_allow_html=True)
    if lang != st.session_state.lang:
        st.session_state.lang = lang
        st.rerun()

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
