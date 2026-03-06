import streamlit as st

def show_bet():
    st.markdown("""
    <h1 style="color:var(--text-primary); font-weight:700; margin-bottom:1.5rem;">📈 Analyse BET – Surface spécifique</h1>
    """, unsafe_allow_html=True)
    
    st.image("https://via.placeholder.com/1200x400?text=Micromeritics+ASAP+2020+-+Analyse+BET", use_column_width=True)
    
    with st.container():
        st.subheader("🔬 Principe de la méthode")
        st.write("""
        La méthode BET (Brunauer-Emmett-Teller) est la technique de référence pour déterminer 
        la surface spécifique des matériaux. Elle repose sur l'adsorption physique d'un gaz inerte 
        (généralement de l'azote) à la température de l'azote liquide (77 K). L'équation BET permet 
        de relier la quantité de gaz adsorbé à la pression relative et d'en déduire la surface spécifique en m²/g.
        """)
    
    with st.container():
        st.subheader("⚙️ Spécifications techniques (ASAP 2020)")
        st.markdown("""
        - **Domaine de mesure :** de 0,01 à > 2000 m²/g (jusqu'à 0,0005 m²/g avec option Krypton)
        - **Gaz utilisés :** N₂, Ar, CO₂, Kr
        - **Précision des transducteurs :** 0,12 % de la lecture
        - **Ports de dégazage :** 2 préparateurs indépendants
        - **Analyse simultanée :** jusqu'à 2 échantillons
        """)
    
    with st.container():
        st.subheader("🧪 Applications")
        data = {
            "Domaine": ["Catalyse", "Pharmaceutique", "Nanomatériaux", "Céramiques"],
            "Application": [
                "Caractérisation des supports (alumine, silice, zéolithes)",
                "Contrôle qualité des principes actifs et excipients",
                "Nanotubes, nanoparticules, graphène",
                "Optimisation du frittage et des propriétés mécaniques"
            ]
        }
        st.table(data)
    
    with st.container():
        st.subheader("📈 Exemple de courbe BET")
        st.image("https://via.placeholder.com/800x400?text=Courbe+BET+multipoints", use_column_width=True)
        st.caption("La partie linéaire (généralement entre P/P₀ = 0,05 et 0,30) permet de déterminer la capacité de la monocouche et la surface spécifique.")
