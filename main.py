import streamlit as st
from home import show_home
from analyses import show_analyses
from request import show_request
from resources import show_resources
from contact import show_contact
from admin import show_admin

# Imports pour les pages détaillées (utilisées par analyses.py)
from bet import show_bet
from porosite import show_porosite
from isothermes import show_isothermes

st.set_page_config(
    page_title="USR Mesure de Surface Spécifique et Porosité",
    page_icon="🧪",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Mode debug (cacher les erreurs aux utilisateurs)
if not st.secrets.get("debug", False):
    st.set_option('client.showErrorDetails', False)

# CSS global avec design moderne et animations
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');
    
    * {
        font-family: 'Inter', sans-serif;
        box-sizing: border-box;
        margin: 0;
        padding: 0;
    }
    
    /* Animations */
    @keyframes fadeInUp {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    @keyframes float {
        0% { transform: translateY(0px); }
        50% { transform: translateY(-5px); }
        100% { transform: translateY(0px); }
    }
    
    /* Header principal */
    .main-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2.5rem;
        border-radius: 20px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 10px 30px rgba(102, 126, 234, 0.3);
        animation: fadeInUp 1s ease;
    }
    
    .main-header h1 {
        font-size: 2.5rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
    }
    
    .main-header p {
        font-size: 1.2rem;
        opacity: 0.9;
    }
    
    /* Cartes d'information */
    .info-card {
        background: white;
        border-radius: 15px;
        padding: 1.8rem;
        margin: 1rem 0;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.05);
        transition: all 0.3s ease;
        border: 1px solid rgba(0, 0, 0, 0.03);
        animation: fadeInUp 0.8s ease;
    }
    
    .info-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 20px 40px rgba(102, 126, 234, 0.15);
        border-color: #667eea;
    }
    
    .info-card h3 {
        color: #2c3e50;
        font-weight: 600;
        margin-bottom: 1rem;
    }
    
    .info-card h4 {
        color: #667eea;
        font-weight: 600;
        margin-bottom: 0.5rem;
    }
    
    /* Cartes d'analyse (page analyses) */
    .analysis-card {
        background: white;
        border-radius: 20px;
        padding: 1.8rem;
        box-shadow: 0 15px 35px rgba(0, 0, 0, 0.1);
        transition: all 0.3s ease;
        cursor: pointer;
        border: 1px solid rgba(0, 0, 0, 0.05);
        height: 100%;
        animation: fadeInUp 0.8s ease;
        text-align: center;
    }
    
    .analysis-card:hover {
        transform: scale(1.02);
        box-shadow: 0 25px 50px rgba(102, 126, 234, 0.2);
        border-color: #667eea;
    }
    
    .analysis-card img {
        width: 100%;
        height: 200px;
        object-fit: cover;
        border-radius: 15px;
        margin-bottom: 1.5rem;
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
        transition: transform 0.3s ease;
    }
    
    .analysis-card:hover img {
        transform: scale(1.05);
    }
    
    .analysis-card h3 {
        color: #2c3e50;
        font-weight: 700;
        margin-bottom: 0.8rem;
    }
    
    .analysis-card p {
        color: #6c757d;
        line-height: 1.6;
        margin-bottom: 1.2rem;
    }
    
    /* Boutons personnalisés */
    .custom-button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 0.7rem 2rem;
        border-radius: 50px;
        text-decoration: none;
        font-weight: 600;
        transition: all 0.3s ease;
        display: inline-block;
        border: none;
        box-shadow: 0 5px 15px rgba(102, 126, 234, 0.3);
        cursor: pointer;
        font-size: 1rem;
    }
    
    .custom-button:hover {
        transform: translateY(-3px);
        box-shadow: 0 10px 25px rgba(102, 126, 234, 0.5);
    }
    
    .custom-button:active {
        transform: translateY(0);
    }
    
    /* Onglets */
    .stTabs [data-baseweb="tab-list"] {
        gap: 2rem;
        justify-content: center;
        background: white;
        padding: 0.8rem;
        border-radius: 60px;
        box-shadow: 0 5px 20px rgba(0, 0, 0, 0.03);
        margin-bottom: 2rem;
        border: 1px solid rgba(0, 0, 0, 0.05);
    }
    
    .stTabs [data-baseweb="tab"] {
        font-size: 1.1rem;
        font-weight: 500;
        color: #6c757d;
        padding: 0.5rem 1.2rem;
        border-radius: 40px;
        transition: all 0.2s ease;
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white !important;
        box-shadow: 0 5px 15px rgba(102, 126, 234, 0.3);
    }
    
    /* Tableaux */
    table {
        width: 100%;
        border-collapse: collapse;
        margin: 1rem 0;
        border-radius: 10px;
        overflow: hidden;
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.05);
    }
    
    th {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        font-weight: 600;
        padding: 12px;
        text-align: left;
    }
    
    td {
        padding: 10px;
        border-bottom: 1px solid #f1f1f1;
    }
    
    tr:hover {
        background-color: #f8f9fa;
    }
    
    /* Pied de page */
    .footer {
        background: #2c3e50;
        color: white;
        padding: 2rem;
        border-radius: 20px;
        margin-top: 3rem;
        text-align: center;
        animation: fadeInUp 0.8s ease;
    }
    
    /* Responsive */
    @media (max-width: 768px) {
        .main-header h1 { font-size: 2rem; }
        .main-header p { font-size: 1rem; }
        .analysis-card img { height: 150px; }
        .stTabs [data-baseweb="tab"] { font-size: 0.9rem; padding: 0.3rem 0.8rem; }
    }
    
    @media (max-width: 480px) {
        .main-header h1 { font-size: 1.6rem; }
        .analysis-card { padding: 1rem; }
        .custom-button { padding: 0.5rem 1.5rem; }
    }
    
    /* Arrière-plan général */
    .stApp {
        background-color: #f8f9fa;
    }
    
    .main .block-container {
        background: white;
        border-radius: 30px;
        padding: 2rem;
        box-shadow: 0 20px 40px rgba(0, 0, 0, 0.03);
        max-width: 1300px;
        margin: 0 auto;
    }
    
    /* Images responsives */
    img {
        max-width: 100%;
        height: auto;
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
