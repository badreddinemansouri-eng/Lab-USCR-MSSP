import streamlit as st
from utils_i18n import get_text
from components import analysis_card

def show_analyses():
    st.markdown("""
    <div class="hero" style="background:linear-gradient(135deg, #3b82f6, #60a5fa);">
        <h1>🔬 Analyses disponibles</h1>
        <p>Découvrez nos techniques de caractérisation</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        analysis_card(
            "📈 Surface spécifique (BET)",
            "Méthode multipoints pour une mesure précise de la surface des matériaux.",
            "Catalyse • Pharmacie • Nanomatériaux",
            "https://via.placeholder.com/400x250?text=Analyse+BET",
            "BET"
        )

    with col2:
        analysis_card(
            "🕳️ Porosité",
            "Distribution de taille des pores par BJH, DFT et t-plot.",
            "MOFs • Zéolithes • Géosciences",
            "https://via.placeholder.com/400x250?text=Porosité",
            "Porosite"
        )

    with col3:
        analysis_card(
            "📊 Isothermes",
            "Isothermes complètes d'adsorption/désorption N₂ et CO₂.",
            "Adsorbants • Stockage de gaz • Énergie",
            "https://via.placeholder.com/400x250?text=Isothermes",
            "Isothermes"
        )

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
