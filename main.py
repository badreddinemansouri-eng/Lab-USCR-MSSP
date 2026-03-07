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
from components import nav_link

st.set_page_config(
    page_title="USR Mesure de Surface Spécifique et Porosité",
    page_icon="🧪",
    layout="wide",
    initial_sidebar_state="collapsed"
)

if not st.secrets.get("debug", False):
    st.set_option('client.showErrorDetails', False)

# Initialisation des états
if "theme" not in st.session_state:
    st.session_state.theme = "light"
if "lang" not in st.session_state:
    st.session_state.lang = "fr"
if "page" not in st.session_state:
    st.session_state.page = get_text("nav_home", st.session_state.lang)

def toggle_theme():
    st.session_state.theme = "dark" if st.session_state.theme == "light" else "light"

# CSS global ultra-moderne
st.markdown(f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
    @import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css');

    :root {{
        --bg-primary: {'#ffffff' if st.session_state.theme == 'light' else '#0a0a0a'};
        --bg-secondary: {'#f8fafc' if st.session_state.theme == 'light' else '#111111'};
        --text-primary: {'#1a1a1a' if st.session_state.theme == 'light' else '#ffffff'};
        --text-secondary: {'#64748b' if st.session_state.theme == 'light' else '#a0a0a0'};
        --accent: #3b82f6;
        --accent-light: #60a5fa;
        --accent-dark: #2563eb;
        --card-bg: {'rgba(255,255,255,0.8)' if st.session_state.theme == 'light' else 'rgba(20,20,20,0.8)'};
        --card-border: {'rgba(0,0,0,0.05)' if st.session_state.theme == 'light' else 'rgba(255,255,255,0.05)'};
        --shadow: {'0 25px 50px -12px rgba(0,0,0,0.25)' if st.session_state.theme == 'light' else '0 25px 50px -12px rgba(0,0,0,0.5)'};
        --blur-amount: 12px;
        --transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }}

    * {{
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }}

    body {{
        font-family: 'Inter', sans-serif;
        background-color: var(--bg-primary);
        color: var(--text-primary);
        transition: background-color 0.3s, color 0.3s;
        line-height: 1.6;
    }}

    .stApp {{
        background: var(--bg-primary);
    }}

    .main .block-container {{
        max-width: 1400px;
        padding: 2rem;
        margin: 0 auto;
        background: var(--bg-primary);
        border-radius: 32px;
        box-shadow: var(--shadow);
    }}

    /* Barre de navigation ultra-moderne */
    .nav-bar {{
        display: flex;
        justify-content: space-between;
        align-items: center;
        background: var(--card-bg);
        backdrop-filter: blur(var(--blur-amount));
        border: 1px solid var(--card-border);
        border-radius: 100px;
        padding: 0.5rem 0.5rem;
        margin-bottom: 3rem;
        box-shadow: var(--shadow);
    }}

    .nav-links {{
        display: flex;
        gap: 0.25rem;
        flex-wrap: wrap;
    }}

    .nav-item {{
        display: flex;
        align-items: center;
        gap: 0.5rem;
        padding: 0.75rem 1.5rem;
        border-radius: 100px;
        color: var(--text-secondary);
        transition: var(--transition);
        cursor: pointer;
        font-weight: 500;
    }}

    .nav-item:hover {{
        background: rgba(59, 130, 246, 0.1);
        color: var(--accent);
    }}

    .nav-item.active {{
        background: linear-gradient(135deg, var(--accent) 0%, var(--accent-light) 100%);
        color: white;
        box-shadow: 0 10px 20px -5px rgba(59, 130, 246, 0.5);
    }}

    .nav-icon {{
        font-size: 1.2rem;
    }}

    .nav-controls {{
        display: flex;
        gap: 0.5rem;
        align-items: center;
    }}

    .theme-toggle, .lang-select {{
        background: var(--card-bg);
        border: 1px solid var(--card-border);
        border-radius: 100px;
        padding: 0.5rem 1rem;
        color: var(--text-primary);
        cursor: pointer;
        transition: var(--transition);
        font-size: 0.9rem;
    }}

    .theme-toggle:hover, .lang-select:hover {{
        background: var(--accent);
        color: white;
        border-color: var(--accent);
    }}

    /* Hero section */
    .hero {{
        text-align: center;
        padding: 4rem 2rem;
        background: linear-gradient(135deg, var(--accent) 0%, var(--accent-light) 100%);
        border-radius: 48px;
        color: white;
        margin-bottom: 3rem;
        animation: fadeInUp 0.8s ease;
    }}

    .hero h1 {{
        font-size: 3rem;
        font-weight: 800;
        margin-bottom: 1rem;
        letter-spacing: -0.02em;
    }}

    .hero-subtitle {{
        font-size: 1.5rem;
        opacity: 0.9;
        margin-bottom: 1rem;
    }}

    .hero-description {{
        font-size: 1.1rem;
        opacity: 0.8;
        max-width: 600px;
        margin: 0 auto;
    }}

    /* Cartes */
    .info-card, .analysis-card {{
        background: var(--card-bg);
        backdrop-filter: blur(var(--blur-amount));
        border: 1px solid var(--card-border);
        border-radius: 32px;
        padding: 2rem;
        box-shadow: var(--shadow);
        transition: var(--transition);
        animation: fadeInUp 0.8s ease;
    }}

    .info-card:hover, .analysis-card:hover {{
        transform: translateY(-8px);
        box-shadow: 0 30px 60px -15px rgba(0,0,0,0.3);
    }}

    .analysis-card {{
        cursor: pointer;
    }}

    .analysis-card img {{
        width: 100%;
        height: 200px;
        object-fit: cover;
        border-radius: 24px;
        margin-bottom: 1.5rem;
        transition: var(--transition);
    }}

    .analysis-card:hover img {{
        transform: scale(1.05);
    }}

    .badge {{
        display: inline-block;
        background: var(--accent);
        color: white;
        padding: 0.3rem 1rem;
        border-radius: 100px;
        font-size: 0.8rem;
        font-weight: 600;
        margin-top: 1rem;
    }}

    /* Animations */
    @keyframes fadeInUp {{
        from {{
            opacity: 0;
            transform: translateY(20px);
        }}
        to {{
            opacity: 1;
            transform: translateY(0);
        }}
    }}

    @keyframes pulse {{
        0%, 100% {{
            transform: scale(1);
        }}
        50% {{
            transform: scale(1.05);
        }}
    }}

    /* Boutons */
    .stButton > button {{
        background: linear-gradient(135deg, var(--accent) 0%, var(--accent-light) 100%);
        color: white;
        border: none;
        border-radius: 100px;
        padding: 0.8rem 2rem;
        font-weight: 600;
        transition: var(--transition);
        box-shadow: 0 10px 20px -5px rgba(59, 130, 246, 0.5);
        width: 100%;
        border: 1px solid rgba(255,255,255,0.1);
    }}

    .stButton > button:hover {{
        transform: translateY(-3px);
        box-shadow: 0 20px 30px -5px rgba(59, 130, 246, 0.7);
        filter: brightness(1.1);
    }}

    /* Responsive */
    @media (max-width: 768px) {{
        .nav-bar {{
            flex-direction: column;
            border-radius: 40px;
            padding: 1rem;
        }}
        .nav-links {{
            justify-content: center;
            width: 100%;
        }}
        .nav-controls {{
            width: 100%;
            justify-content: center;
            margin-top: 0.5rem;
        }}
        .hero h1 {{
            font-size: 2rem;
        }}
        .hero-subtitle {{
            font-size: 1.2rem;
        }}
    }}
</style>
""", unsafe_allow_html=True)

# Barre de navigation
nav_items = [
    (get_text("nav_home", st.session_state.lang), "nav_home", "🏠"),
    (get_text("nav_analyses", st.session_state.lang), "nav_analyses", "🔬"),
    (get_text("nav_request", st.session_state.lang), "nav_request", "📝"),
    (get_text("nav_resources", st.session_state.lang), "nav_resources", "📚"),
    (get_text("nav_contact", st.session_state.lang), "nav_contact", "📞"),
    (get_text("nav_admin", st.session_state.lang), "nav_admin", "🔐")
]

with st.container():
    st.markdown('<div class="nav-bar">', unsafe_allow_html=True)
    st.markdown('<div class="nav-links">', unsafe_allow_html=True)
    for label, key, icon in nav_items:
        nav_link(label, key, icon)
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
if st.session_state.page == "nav_home":
    show_home()
elif st.session_state.page == "nav_analyses":
    show_analyses()
elif st.session_state.page == "nav_request":
    show_request()
elif st.session_state.page == "nav_resources":
    show_resources()
elif st.session_state.page == "nav_contact":
    show_contact()
elif st.session_state.page == "nav_admin":
    show_admin()
