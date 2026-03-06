import streamlit as st

def show_isothermes():
    st.markdown("""
    <h1 style="color:var(--text-primary); font-weight:700; margin-bottom:1.5rem;">📊 Isothermes d'adsorption/désorption</h1>
    """, unsafe_allow_html=True)
    
    st.image("https://via.placeholder.com/1200x400?text=Micromeritics+ASAP+2020+-+Isothermes", use_column_width=True)
    
    with st.container():
        st.subheader("🔬 Classification IUPAC")
        st.write("La forme de l'isotherme renseigne sur la nature poreuse du matériau. L'ASAP 2020 permet d'obtenir des isothermes complètes avec une haute résolution.")
        data_types = {
            "Type": ["Type I", "Type II", "Type IV", "Type IVa"],
            "Description": [
                "Microporeux, plateau prononcé",
                "Non-poreux ou macroporeux",
                "Mésoporeux avec hystérésis",
                "Hystérésis de type H1/H2"
            ],
            "Matériaux typiques": [
                "Zéolithes, charbons actifs",
                "Poudres, pigments",
                "Catalyseurs, silices mésoporeuses",
                "Pores cylindriques / 'bouteille d'encre'"
            ]
        }
        st.table(data_types)
    
    with st.container():
        st.subheader("⚙️ Fonctionnalités avancées du logiciel MicroActive")
        st.markdown("""
        - **Superposition de données :** comparer jusqu'à 25 fichiers d'isothermes
        - **Smart Dosing™ :** apprentissage automatique du comportement d'adsorption pour optimiser les doses de gaz
        - **Exportation directe** vers tableurs pour analyses complémentaires
        - **Sélection interactive** des plages de données en temps réel
        """)
    
    with st.container():
        st.subheader("🧪 Applications")
        st.markdown("""
        - Étude de la texture complète des matériaux (surface, volume poreux, taille des pores)
        - Détermination de l'énergie d'adsorption (isothermes à différentes températures)
        - Analyse de la microporosité fine avec CO₂ à 273 K
        - Caractérisation des adsorbants pour le stockage de gaz (H₂, CH₄, CO₂)
        """)
    
    with st.container():
        st.subheader("📈 Exemple d'isotherme")
        st.image("https://via.placeholder.com/800x400?text=Isotherme+type+IV+avec+hysteresis", use_column_width=True)
        st.caption("Isotherme de type IV caractéristique des matériaux mésoporeux, avec boucle d'hystérésis.")
