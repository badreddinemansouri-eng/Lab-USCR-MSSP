import streamlit as st

def show_porosite():
    st.markdown("""
    <h1 style="color:var(--text-primary); font-weight:700; margin-bottom:1.5rem;">🕳️ Analyse de la porosité</h1>
    """, unsafe_allow_html=True)
    
    st.image("https://via.placeholder.com/1200x400?text=Micromeritics+ASAP+2020+-+Porosité", use_column_width=True)
    
    with st.container():
        st.subheader("🔬 Méthodes disponibles")
        st.write("L'ASAP 2020 propose plusieurs modèles pour caractériser la distribution de taille des pores, du domaine microporeux au mésoporeux.")
        data_methodes = {
            "Méthode": ["BJH", "t-plot", "DFT/NLDFT", "Horvath-Kawazoe"],
            "Principe": [
                "Modèle de Kelvin pour la condensation capillaire",
                "Épaisseur statistique de la couche adsorbée",
                "Théorie de la fonctionnelle de la densité",
                "Potentiel dans les micropores"
            ],
            "Domaine": [
                "Mésopores (2-50 nm)",
                "Volume microporeux, surface externe",
                "Micro et mésopores (distribution complète)",
                "Micropores étroits (< 1 nm)"
            ]
        }
        st.table(data_methodes)
    
    with st.container():
        st.subheader("⚙️ Spécifications techniques")
        st.markdown("""
        - **Domaine de pression :** 1,3 × 10⁻⁹ à 1,0 P/P₀
        - **Option micropore :** transducteur 0,1 mmHg pour pores de 0,35 à 3 nm
        - **Six ports d'entrée de gaz** avec dédiés pour vapeur et hélium
        - **Logiciel MicroActive** avec calculs intégrés des modèles avancés
        """)
    
    with st.container():
        st.subheader("🧪 Applications")
        st.markdown("""
        - **MOFs et zéolithes :** caractérisation des matériaux de structure pour stockage de gaz
        - **Charbons actifs :** optimisation de la distribution poreuse pour l'adsorption
        - **Stockage d'énergie :** électrodes de supercondensateurs
        - **Géosciences :** porosité des roches pour l'exploration pétrolière
        """)
    
    with st.container():
        st.subheader("📊 Exemple de distribution de pores")
        st.image("https://via.placeholder.com/800x400?text=Distribution+de+pores+BJH+DFT", use_column_width=True)
        st.caption("Courbe de distribution obtenue par la méthode BJH (mésopores) et DFT (micropores).")
