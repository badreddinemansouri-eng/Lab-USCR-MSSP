import streamlit as st
from home import show_home
from analyses import show_analyses
from request import show_request
from resources import show_resources
from contact import show_contact
from admin import show_admin

# Ces imports sont utilisés par analyses.py via st.session_state
from bet import show_bet
from porosite import show_porosite
from isothermes import show_isothermes

st.set_page_config(
    page_title="USR Mesure de Surface Spécifique et Porosité",
    page_icon="🧪",
    layout="wide",
    initial_sidebar_state="collapsed"  # ← sidebar désactivée
)

# Mode debug (cacher les erreurs aux utilisateurs)
if not st.secrets.get("debug", False):
    st.set_option('client.showErrorDetails', False)

# CSS global (identique, avec styles pour les onglets)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
    
    * {
        font-family: 'Inter', sans-serif;
        box-sizing: border-box;
    }
    
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    .main-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
        animation: fadeIn 0.8s ease;
    }
    
    .info-card {
        background-color: #f8f9fa;
        border-radius: 10px;
        padding: 1.5rem;
        margin: 1rem 0;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        transition: all 0.3s ease;
        animation: fadeIn 0.8s ease;
    }
    
    .info-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 20px rgba(0, 0, 0, 0.15);
    }
    
    .analysis-card {
        background: white;
        border-radius: 15px;
        padding: 1.5rem;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        transition: transform 0.3s ease;
        cursor: pointer;
        border: 1px solid #e9ecef;
        height: 100%;
        animation: fadeIn 0.8s ease;
    }
    
    .analysis-card:hover {
        transform: scale(1.02);
        box-shadow: 0 8px 25px rgba(102, 126, 234, 0.2);
    }
    
    .analysis-card img {
        width: 100%;
        height: 180px;
        object-fit: cover;
        border-radius: 10px;
        margin-bottom: 1rem;
    }
    
    .custom-button {
        background-color: #667eea;
        color: white;
        padding: 0.5rem 2rem;
        border-radius: 25px;
        text-decoration: none;
        font-weight: 600;
        transition: all 0.3s ease;
        display: inline-block;
        border: none;
    }
    
    .custom-button:hover {
        background-color: #764ba2;
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4);
    }
    
    @media (max-width: 768px) {
        .main-header h1 { font-size: 1.8rem; }
        .main-header h2 { font-size: 1.2rem; }
        .analysis-card img { height: 140px; }
        .stColumn { margin-bottom: 1rem; }
    }
    
    .footer {
        background-color: #2c3e50;
        color: white;
        padding: 2rem;
        border-radius: 10px;
        margin-top: 3rem;
        text-align: center;
        animation: fadeIn 0.8s ease;
    }
    
    /* Style des onglets */
    .stTabs [data-baseweb="tab-list"] {
        gap: 2rem;
        justify-content: center;
        background-color: #f8f9fa;
        padding: 0.5rem;
        border-radius: 10px;
        margin-bottom: 2rem;
    }
    
    .stTabs [data-baseweb="tab"] {
        font-size: 1.1rem;
        font-weight: 500;
        color: #2c3e50;
    }
    
    .stTabs [aria-selected="true"] {
        background-color: #667eea;
        color: white !important;
        border-radius: 5px;
    }
    
    h1, h2, h3 {
        color: #2c3e50;
        font-weight: 600;
    }
    
    .stApp { background-color: #f5f5f5; }
    .main .block-container {
        background-color: white;
        border-radius: 10px;
        padding: 2rem;
        box-shadow: 0 2px 10px rgba(0,0,0,0.05);
        max-width: 1200px;
        margin: 0 auto;
    }
</style>
""", unsafe_allow_html=True)

# Navigation par onglets
tabs = st.tabs(["🏠 Accueil", "🔬 Analyses", "📝 Demande", "📚 Ressources", "📞 Contact", "🔐 Admin"])

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
