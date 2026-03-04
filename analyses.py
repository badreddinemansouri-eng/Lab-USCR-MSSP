import streamlit as st

def show_analyses():
    st.markdown("""
    <div class="main-header">
        <h1>🔬 Analyses disponibles</h1>
        <p>Caractérisation complète de vos matériaux</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    ### Analyse texturale par ASAP 2020
    Notre équipement permet une large gamme d'analyses pour la caractérisation des matériaux poreux et divisés.
    
    | Analyse | Principe | Applications |
    |---------|----------|--------------|
    | **Surface spécifique (BET)** | Adsorption de N₂ à 77K, méthode multipoints | Catalyseurs, nanomatériaux, poudres |
    | **Distribution de taille des pores** | BJH, DFT, t-plot | Zéolithes, MOFs, matériaux mésoporeux |
    | **Volume microporeux** | t-plot, DR | Charbons actifs, tamis moléculaires |
    | **Isothermes complètes** | Adsorption/désorption N₂, CO₂ | Étude de la texture complète |
    
    ### Prochainement
    - **Chimisorption TPR** (Temperature Programmed Reduction) – pour l'étude de la réductibilité des catalyseurs
    - **UV-Vis en phase solide** – spectroscopie de réflectance diffuse pour l'analyse des solides
    
    N’hésitez pas à nous contacter pour toute demande spécifique ou pour discuter de votre projet.
    """)
