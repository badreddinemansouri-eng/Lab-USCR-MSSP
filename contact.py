import streamlit as st

def show_contact():
    st.markdown("""
    <div class="main-header">
        <h1>📞 Contactez-nous</h1>
        <p>Notre équipe est à votre disposition</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("""
        <div class="info-card">
            <h3>📍 Adresse</h3>
            <p><strong>Uni té de Service commune de Recherche</strong><br>
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
        # Utilisez votre propre image ou une capture d'écran Google Maps
        st.image("https://i.imgur.com/dCemmMW.png", use_column_width=True)  # À remplacer par votre image
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
