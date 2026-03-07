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
if "selected_tab" not in st.session_state:
    st.session_state.selected_tab = 0  # 0 = Accueil

def toggle_theme():
    st.session_state.theme = "dark" if st.session_state.theme == "light" else "light"

# CSS global avec support du thème
st.markdown(f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
    
    * {{
        font-family: 'Inter', sans-serif;
        box-sizing: border-box;
    }}
    
    :root {{
        --bg-primary: {'#ffffff' if st.session_state.theme == 'light' else '#1a1a2e'};
        --bg-secondary: {'#f8f9fa' if st.session_state.theme == 'light' else '#16213e'};
        --text-primary: {'#1e2b4f' if st.session_state.theme == 'light' else '#e0e0e0'};
        --text-secondary: {'#5a6b7e' if st.session_state.theme == 'light' else '#b0b0b0'};
        --accent: #667eea;
        --accent-light: #764ba2;
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
    
    @keyframes fadeIn {{
        from {{ opacity: 0; transform: translateY(10px); }}
        to {{ opacity: 1; transform: translateY(0); }}
    }}
    
    .main-header {{
        background: linear-gradient(135deg, var(--accent) 0%, var(--accent-light) 100%);
        padding: 2rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
        animation: fadeIn 0.8s ease;
    }}
    
    .info-card {{
        background: var(--card-bg);
        backdrop-filter: blur(var(--blur-amount));
        border: 1px solid var(--card-border);
        border-radius: 10px;
        padding: 1.5rem;
        margin: 1rem 0;
        box-shadow: var(--shadow);
        transition: all 0.3s ease;
        animation: fadeIn 0.8s ease;
    }}
    
    .info-card:hover {{
        transform: translateY(-5px);
        box-shadow: 0 12px 20px rgba(0, 0, 0, 0.15);
    }}
    
    .analysis-card {{
        background: var(--card-bg);
        backdrop-filter: blur(var(--blur-amount));
        border: 1px solid var(--card-border);
        border-radius: 15px;
        padding: 1.5rem;
        box-shadow: var(--shadow);
        transition: transform 0.3s ease;
        cursor: pointer;
        height: 100%;
        animation: fadeIn 0.8s ease;
    }}
    
    .analysis-card:hover {{
        transform: scale(1.02);
        box-shadow: 0 8px 25px rgba(102, 126, 234, 0.2);
    }}
    
    .analysis-card img {{
        width: 100%;
        height: 180px;
        object-fit: cover;
        border-radius: 10px;
        margin-bottom: 1rem;
    }}
    
    .custom-button {{
        background-color: #667eea;
        color: white;
        padding: 0.5rem 2rem;
        border-radius: 25px;
        text-decoration: none;
        font-weight: 600;
        transition: all 0.3s ease;
        display: inline-block;
        border: none;
    }}
    
    .custom-button:hover {{
        background-color: #764ba2;
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4);
    }}
    
    @media (max-width: 768px) {{
        .main-header h1 {{ font-size: 1.8rem; }}
        .main-header h2 {{ font-size: 1.2rem; }}
        .analysis-card img {{ height: 140px; }}
        .stColumn {{ margin-bottom: 1rem; }}
    }}
    
    .footer {{
        background: var(--card-bg);
        backdrop-filter: blur(var(--blur-amount));
        color: var(--text-primary);
        padding: 2rem;
        border-radius: 10px;
        margin-top: 3rem;
        text-align: center;
        animation: fadeIn 0.8s ease;
        border: 1px solid var(--card-border);
    }}
    
    /* Style des onglets */
    .stTabs [data-baseweb="tab-list"] {{
        gap: 2rem;
        justify-content: center;
        background: var(--card-bg);
        backdrop-filter: blur(var(--blur-amount));
        padding: 0.5rem;
        border-radius: 10px;
        margin-bottom: 2rem;
        border: 1px solid var(--card-border);
    }}
    
    .stTabs [data-baseweb="tab"] {{
        font-size: 1.1rem;
        font-weight: 500;
        color: var(--text-primary);
    }}
    
    .stTabs [aria-selected="true"] {{
        background: linear-gradient(135deg, var(--accent) 0%, var(--accent-light) 100%);
        color: white !important;
        border-radius: 5px;
    }}
    
    h1, h2, h3 {{
        color: var(--text-primary);
        font-weight: 600;
    }}
    
    /* Contrôles en haut à droite */
    .controls {{
        display: flex;
        justify-content: flex-end;
        gap: 0.5rem;
        margin-bottom: 1rem;
    }}
    .controls .stButton > button,
    .controls .stSelectbox {{
        min-width: 40px;
        padding: 0.2rem 0.8rem;
        font-size: 0.9rem;
        background: var(--card-bg);
        border: 1px solid var(--card-border);
        color: var(--text-primary);
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

# Onglets de navigation
tab_labels = [
    get_text("nav_home", st.session_state.lang),
    get_text("nav_analyses", st.session_state.lang),
    get_text("nav_request", st.session_state.lang),
    get_text("nav_resources", st.session_state.lang),
    get_text("nav_contact", st.session_state.lang),
    get_text("nav_admin", st.session_state.lang)
]

# Créer les onglets en utilisant l'index stocké
tabs = st.tabs(tab_labels)

# Afficher le contenu de l'onglet sélectionné
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
