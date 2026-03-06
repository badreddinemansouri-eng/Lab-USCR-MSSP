import streamlit as st
import folium
from streamlit_folium import folium_static
from utils_i18n import get_text

def show_contact():
    st.markdown("""
    <div class="main-header hero" style="background:linear-gradient(135deg, #1e2b4f 0%, #2a3f6e 100%);">
        <h1>📞 """ + get_text("contact_us", st.session_state.lang) + """</h1>
        <p>Notre équipe est à votre disposition</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="info-card">
            <h3>📍 Adresse</h3>
            <p><strong>Unité de Service commune de Recherche</strong><br>
            Mesure de Surface Spécifique et de Porosité<br><br>
            <strong>Université de Tunis El Manar</strong><br>
            Campus Universitaire Farhat Hached<br>
            Bâtiment des Sciences Exactes – Département de Chimie<br>
            1068 Tunis, Tunisie</p>
            
            <h3>📞 Téléphone</h3>
            <p>+216 71 872 600 (standard FST)</p>
            
            <h3>📧 Email</h3>
            <p>badreddine.mansouri@etudiant-fst.utm.tn<br>
            lassaad.benhammouda@utm.tn</p>
            
            <h3>🕒 Horaires</h3>
            <p>Lundi - Vendredi : 8h30 - 17h00<br>
            Samedi : 9h00 - 12h00</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="info-card">
            <h3>🗺️ Plan d'accès</h3>
        """, unsafe_allow_html=True)
        
        # Carte interactive avec Folium
        m = folium.Map(location=[36.8275, 10.1658], zoom_start=15, tiles="OpenStreetMap")
        folium.Marker(
            [36.8275, 10.1658],
            popup="Faculté des Sciences de Tunis",
            tooltip="Notre laboratoire",
            icon=folium.Icon(color="blue", icon="flask", prefix="fa")
        ).add_to(m)
        folium_static(m, width=600, height=400)
        
        st.markdown("</div>", unsafe_allow_html=True)
        
        st.markdown("""
        <div class="info-card">
            <h3>👥 Personnel</h3>
            <p><strong>Badreddine Mansouri</strong><br>
            Technicien responsable des analyses<br>
            📧 badreddine.mansouri@etudiant-fst.utm.tn<br>
            📞 +216 53 821 882<br>
            🕒 Permanence : Lundi, Mercredi, Vendredi</p>
            
            <p><strong>Pr. Lassaad BEN HAMMOUDA</strong><br>
            Directeur de l'unité<br>
            📧 lassaad.benhammouda@utm.tn<br>
            📞 +216 XX XXX XXX<br>
            🕒 Sur rendez-vous uniquement</p>
        </div>
        """, unsafe_allow_html=True)
