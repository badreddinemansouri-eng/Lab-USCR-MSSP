import streamlit as st
from utils_i18n import get_text

def show_analyses():
    st.markdown("""
    <div class="main-header hero" style="background:linear-gradient(135deg, #1e2b4f 0%, #2a3f6e 100%);">
        <h1>🔬 """ + get_text("nav_analyses", st.session_state.lang) + """</h1>
        <p>Découvrez nos techniques de caractérisation</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="analysis-card">
            <img src="https://via.placeholder.com/400x250?text=Analyse+BET" alt="BET">
            <h3>📈 Surface spécifique (BET)</h3>
            <p>Méthode multipoints pour une mesure précise de la surface des matériaux.</p>
            <div class="badge">Catalyse • Pharmacie • Nanomatériaux</div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("🔍 Découvrir BET", key="bet_btn", use_container_width=True):
            st.session_state["analysis_page"] = "BET"
            st.rerun()

    with col2:
        st.markdown("""
        <div class="analysis-card">
            <img src="https://via.placeholder.com/400x250?text=Porosité" alt="Porosité">
            <h3>🕳️ Porosité</h3>
            <p>Distribution de taille des pores par BJH, DFT et t-plot.</p>
            <div class="badge">MOFs • Zéolithes • Géosciences</div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("🔍 Découvrir Porosité", key="poro_btn", use_container_width=True):
            st.session_state["analysis_page"] = "Porosite"
            st.rerun()

    with col3:
        st.markdown("""
        <div class="analysis-card">
            <img src="https://via.placeholder.com/400x250?text=Isothermes" alt="Isothermes">
            <h3>📊 Isothermes</h3>
            <p>Isothermes complètes d'adsorption/désorption N₂ et CO₂.</p>
            <div class="badge">Adsorbants • Stockage de gaz • Énergie</div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("🔍 Découvrir Isothermes", key="iso_btn", use_container_width=True):
            st.session_state["analysis_page"] = "Isothermes"
            st.rerun()

    if "analysis_page" in st.session_state:
        st.markdown("---")
        col_back = st.columns([1, 2, 1])[1]
        with col_back:
            if st.button(get_text("back_to_analyses", st.session_state.lang), use_container_width=True):
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
