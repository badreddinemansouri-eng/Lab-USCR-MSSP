import streamlit as st

def show_analyses():
    st.markdown("""
    <div class="main-header">
        <h1>🔬 Analyses disponibles</h1>
        <p>Techniques de pointe pour la caractérisation de vos matériaux</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="analysis-card">
            <img src="https://via.placeholder.com/400x250?text=Analyse+BET" alt="BET">
            <h3>📈 Surface spécifique (BET)</h3>
            <p>Méthode multipoints pour une mesure précise de la surface des matériaux. Idéal pour catalyseurs, nanomatériaux et poudres.</p>
            <p><strong>Applications :</strong> Catalyse, Pharmacie, Nanomatériaux</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("🔍 Voir détails BET", key="bet_btn", use_container_width=True):
            st.session_state["analysis_page"] = "BET"
            st.rerun()

    with col2:
        st.markdown("""
        <div class="analysis-card">
            <img src="https://via.placeholder.com/400x250?text=Porosité" alt="Porosité">
            <h3>🕳️ Porosité</h3>
            <p>Distribution de taille des pores par BJH, DFT et t-plot. Essentiel pour zéolithes, MOFs et matériaux mésoporeux.</p>
            <p><strong>Applications :</strong> MOFs, Charbons actifs, Géosciences</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("🔍 Voir détails Porosité", key="poro_btn", use_container_width=True):
            st.session_state["analysis_page"] = "Porosite"
            st.rerun()

    with col3:
        st.markdown("""
        <div class="analysis-card">
            <img src="https://via.placeholder.com/400x250?text=Isothermes" alt="Isothermes">
            <h3>📊 Isothermes</h3>
            <p>Isothermes complètes d'adsorption/désorption N₂ et CO₂ pour une caractérisation texturale complète.</p>
            <p><strong>Applications :</strong> Adsorbants, Stockage de gaz, Énergie</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("🔍 Voir détails Isothermes", key="iso_btn", use_container_width=True):
            st.session_state["analysis_page"] = "Isothermes"
            st.rerun()

    if "analysis_page" in st.session_state:
        st.markdown("---")
        col_back = st.columns([1, 10, 1])[1]
        with col_back:
            if st.button("← Retour aux analyses", use_container_width=True):
                del st.session_state["analysis_page"]
                st.rerun()
        
        if st.session_state["analysis_page"] == "BET":
            from bet import show_bet
            show_bet()
        elif st.session_state["analysis_page"] == "Porosite":
            from porosite import show_porosite
            show_porosite()
        elif st.session_state["analysis_page"] == "Isothermes":
            from isothermes import show_isothermes
            show_isothermes()
