import streamlit as st

def show_contact():
    st.markdown("""
    <div class="main-header">
        <h1>📞 Contact</h1>
        <p>Comment nous joindre</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        # À remplacer dans la section "Adresse" (lignes 9-15 environ)
        st.markdown("""
            ## 📍 Adresse
            **Unité de Service commune de Recherche**  
            **Mesure de Surface Spécifique et de Porosité**  
            
            **Université de Tunis El Manar**  
            Campus Universitaire Farhat Hached  
            Bâtiment des Sciences Exactes – Département de Chimie  
            1068 Tunis, Tunisie  
            
            **Faculté des Sciences de Tunis (FST)**  
            📍 Campus Universitaire - El Manar, 2092 Tunis  
            📞 +216 71 872 600  
            📠 +216 71 871 666  
            
            🕒 **Horaires d'ouverture :**  
            Lundi - Vendredi : 8h30 - 17h00  
            Samedi : 9h00 - 12h00  
            """)
        
        # Replace with actual map image or embed Google Maps
        st.markdown("### 🗺️ Plan d'accès")
        st.image("https://i.imgur.com/dCemmMW.png", 
                use_column_width=True)
    
    with col2:
        st.markdown("## 👥 Personnel")
        
        st.markdown("""
        <div class="info-card">
            <h4>Badreddine Mansouri</h4>
            <p><strong>Technicien responsable des analyses</strong></p>
            <p>📧 badreddine.mansouri@etudiant-fst.utm.tn</p>
            <p>📞 +216 53 821 882</p>
            <p>🕒 Permanence : Lundi, Mercredi, Vendredi</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="info-card">
            <h4>Pr. Lassaad BEN HAMMOUDA</h4>
            <p><strong>Directeur de l'unité</strong></p>
            <p>📧 lassaad.benhammouda@utm.tn</p>
            <p>📞 +216 XX XXX XXX</p>
            <p>🕒 Sur rendez-vous uniquement</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("## 📧 Formulaire de contact")
        with st.form("contact_form"):
            name = st.text_input("Votre nom *")
            email = st.text_input("Votre email *")
            subject = st.selectbox("Sujet", ["Demande d'information", "Question technique", "Prise de rendez-vous", "Autre"])
            message = st.text_area("Votre message *")
            
            submitted = st.form_submit_button("Envoyer")
            if submitted:
                st.success("Message envoyé ! Nous vous répondrons dans les plus brefs délais.")
