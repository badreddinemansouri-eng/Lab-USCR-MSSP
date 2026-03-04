import streamlit as st
from home import show_home
from analyses import show_analyses
from request import show_request
from resources import show_resources
from contact import show_contact

st.set_page_config(
    page_title="USR Mesure de Surface Spécifique et Porosité",
    page_icon="🧪",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }
    
    .main-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
    }
    
    .info-card {
        background-color: #f8f9fa;
        border-radius: 10px;
        padding: 1.5rem;
        margin: 1rem 0;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        transition: transform 0.3s ease;
    }
    
    .info-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
    }
    
    .custom-button {
        background-color: #667eea;
        color: white;
        padding: 0.5rem 2rem;
        border-radius: 5px;
        text-decoration: none;
        font-weight: 600;
        transition: background-color 0.3s ease;
    }
    
    .custom-button:hover {
        background-color: #764ba2;
    }
    
    .footer {
        background-color: #2c3e50;
        color: white;
        padding: 2rem;
        border-radius: 10px;
        margin-top: 3rem;
        text-align: center;
    }
    
    .css-1d391kg {
        background-color: #f8f9fa;
    }
    
    h1, h2, h3 {
        color: #2c3e50;
        font-weight: 600;
    }
    
    .equipment-image {
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.image("https://via.placeholder.com/200x100?text=USR+Logo", use_column_width=True)
    st.markdown("## **Unité de Service**")
    st.markdown("### Mesure de Surface Spécifique")
    st.markdown("---")
    
    st.markdown("### 📋 Navigation")
    page = st.radio(
        "Aller à",
        ["🏠 Accueil", "🔬 Analyses", "📝 Formulaire de Demande", "📚 Ressources", "📞 Contact", "🔐 Admin"],
        label_visibility="collapsed"
    )
    
    st.markdown("---")
    st.markdown("### 🕒 Horaires")
    st.markdown("Lundi - Vendredi: 8h30 - 17h00")
    st.markdown("Samedi: 9h00 - 12h00")
    
    st.markdown("### 📍 Adresse")
    st.markdown("Université de Tunis El Manar")
    st.markdown("Campus Universitaire Farhat Hached")
    st.markdown("1068 Tunis, Tunisie")
    
    st.markdown("---")
    st.markdown("**Version 2.1** | © 2026")

if page == "🏠 Accueil":
    show_home()
elif page == "🔬 Analyses":
    show_analyses()
elif page == "📝 Formulaire de Demande":
    show_request()
elif page == "📚 Ressources":
    show_resources()
elif page == "📞 Contact":
    show_contact()
elif page == "🔐 Admin":
    from admin import show_admin
    show_admin()
