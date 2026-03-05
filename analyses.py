import streamlit as st

def show_analyses():
    st.markdown("""
    <div class="main-header">
        <h1>🔬 Analyses disponibles</h1>
        <p>Découvrez nos techniques de caractérisation</p>
    </div>
    """, unsafe_allow_html=True)

    # Trois cartes en colonnes
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="analysis-card" onclick="window.location.href='?page=BET'">
            <img src="https://via.placeholder.com/300x180?text=Surface+specifique" alt="BET">
            <h3>📈 Surface spécifique (BET)</h3>
            <p>Méthode multipoints pour une mesure précise de la surface des matériaux.</p>
            <p><strong>Applications :</strong> Catalyseurs, nanomatériaux, poudres</p>
            <a href="#" class="custom-button">En savoir plus →</a>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Voir détails BET", key="bet_btn"):
            st.session_state["analysis_page"] = "BET"
            st.rerun()

    with col2:
        st.markdown("""
        <div class="analysis-card">
            <img src="https://via.placeholder.com/300x180?text=Porosite" alt="Porosité">
            <h3>🕳️ Porosité</h3>
            <p>Distribution de taille des pores par BJH, DFT et t-plot.</p>
            <p><strong>Applications :</strong> Zéolithes, MOFs, matériaux mésoporeux</p>
            <a href="#" class="custom-button">En savoir plus →</a>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Voir détails Porosité", key="poro_btn"):
            st.session_state["analysis_page"] = "Porosite"
            st.rerun()

    with col3:
        st.markdown("""
        <div class="analysis-card">
            <img src="https://via.placeholder.com/300x180?text=Isothermes" alt="Isothermes">
            <h3>📊 Isothermes</h3>
            <p>Isothermes complètes d'adsorption/désorption N₂ et CO₂.</p>
            <p><strong>Applications :</strong> Caractérisation complète de la texture</p>
            <a href="#" class="custom-button">En savoir plus →</a>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Voir détails Isothermes", key="iso_btn"):
            st.session_state["analysis_page"] = "Isothermes"
            st.rerun()

    # Si une carte a été cliquée, on affiche la page détaillée sans sidebar
    if "analysis_page" in st.session_state:
        st.markdown("---")
        if st.button("← Retour aux analyses"):
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
