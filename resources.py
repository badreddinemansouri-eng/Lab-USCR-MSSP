import streamlit as st

def show_resources():
    st.markdown("""
    <div class="main-header">
        <h1>📚 Ressources</h1>
        <p>Documentation, protocoles et informations utiles</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("## 📄 Documents téléchargeables")
        
        with st.expander("📋 Formulaire de demande vierge"):
            st.markdown("""
            Téléchargez le formulaire de demande au format PDF à remplir manuellement.
            """)
            st.download_button(
                label="📥 Télécharger le formulaire PDF",
                data=open("formulaire_demande.pdf", "rb").read() if False else b"Placeholder",
                file_name="formulaire_demande.pdf",
                mime="application/pdf",
                disabled=True  # À activer quand le fichier existe
            )
        
        with st.expander("📊 Guide de préparation des échantillons"):
            st.markdown("""
            **Recommandations générales :**
            - Quantité minimale : 100 mg
            - Séchage préalable recommandé à 105°C
            - Éviter les contaminants organiques
            - Broyer si nécessaire (granulométrie < 500 μm)
            
            [Téléchargement disponible prochainement]
            """)
        
        with st.expander("📑 Modèle de publication"):
            st.markdown("""
                Comment citer notre unité dans vos publications :""")
    
    with col2:
    st.markdown("## 🎓 Formations")
    
    st.markdown("""
    <div class="info-card">
    <h4>Formation à l'ASAP 2020</h4>
    <p><strong>Durée :</strong> 2 jours</p>
    <p><strong>Programme :</strong></p>
    <ul>
        <li>Théorie de l'adsorption</li>
        <li>Préparation des échantillons</li>
        <li>Paramétrage des analyses</li>
        <li>Traitement des données</li>
    </ul>
    <p><strong>Prochaine session :</strong> 15-16 Avril 2026</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("## 🔗 Liens utiles")
    st.markdown("""
    - [Micromeritics - ASAP 2020](https://www.micromeritics.com)
    - [Université de Tunis El Manar](http://www.utm.rnu.tn)
    - [Ministère de l'Enseignement Supérieur](http://www.mes.tn)
    """)
              
