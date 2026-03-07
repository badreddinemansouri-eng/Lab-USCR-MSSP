import streamlit as st
from utils_i18n import get_text
from utils import get_all_news

def show_home():
    st.markdown("""
    <div class="hero">
        <h1>🧪 Unité de Service commune de Recherche</h1>
        <p style="font-size:1.5rem;">Mesure de Surface Spécifique et de Porosité</p>
        <p style="font-size:1.2rem; margin-top:1rem;">Analyse texturale de précision avec le Micromeritics ASAP 2020</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        with st.container():
            st.markdown("## 🎯 " + get_text("welcome", st.session_state.lang))
            st.markdown("""
            Notre unité est dédiée à la caractérisation texturale des matériaux poreux et divisés. 
            Nous mettons à disposition des chercheurs et industriels un équipement de pointe pour 
            l'analyse de surface spécifique et de porosité.
            
            **Notre mission :** Fournir des mesures précises et reproductibles pour accompagner 
            vos projets de recherche et développement.
            """)
            
        col_stats1, col_stats2, col_stats3 = st.columns(3)
        with col_stats1:
            st.metric("Analyses réalisées", "1500+", "+12%")
        with col_stats2:
            st.metric("Chercheurs accompagnés", "85", "+8")
        with col_stats3:
            st.metric("Publications supportées", "45", "+5")
    
    with col2:
        st.markdown("""
        <div class="info-card">
            <h3>👥 """ + get_text("our_team", st.session_state.lang) + """</h3>
            <p><strong>Badreddine Mansouri</strong><br>
            <span style="color:var(--text-secondary);">Responsable des analyses</span></p>
            <p><strong>Pr. Lassaad BEN HAMMOUDA</strong><br>
            <span style="color:var(--text-secondary);">Directeur de l'unité</span></p>
        """, unsafe_allow_html=True)
        
        # Style spécifique pour le bouton "Faire une demande"
        st.markdown("""
        <style>
            #home_request_btn {
                animation: pulse 2s infinite !important;
                background: linear-gradient(135deg, #ff6b6b, #ee5a24) !important;
                border: none !important;
                color: white !important;
                font-weight: bold !important;
                font-size: 1.2rem !important;
                padding: 0.8rem 2rem !important;
                border-radius: 50px !important;
                width: 100% !important;
                margin-top: 1rem !important;
                cursor: pointer !important;
                transition: all 0.3s !important;
            }
            #home_request_btn:hover {
                transform: scale(1.05) !important;
                box-shadow: 0 10px 30px rgba(255, 107, 107, 0.5) !important;
            }
            @keyframes pulse {
                0% { transform: scale(1); box-shadow: 0 0 0 0 rgba(255, 107, 107, 0.7); }
                70% { transform: scale(1.05); box-shadow: 0 0 20px 10px rgba(255, 107, 107, 0.3); }
                100% { transform: scale(1); box-shadow: 0 0 0 0 rgba(255, 107, 107, 0); }
            }
        </style>
        """, unsafe_allow_html=True)
        
        # Utilisation de st.button standard pour la navigation
        if st.button(get_text("make_request", st.session_state.lang) + " →", key="home_request_btn"):
            st.session_state.selected_tab = 2  # index de l'onglet "Demande"
            st.rerun()
        
        st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.markdown("## 🔬 Notre équipement principal")
    
    col_eq1, col_eq2 = st.columns(2)
    
    with col_eq1:
        st.markdown("""
        <div class="info-card">
            <h3>Micromeritics ASAP 2020</h3>
            <p>L'ASAP 2020 est un analyseur de surface et de porosité de haute performance, conçu pour la caractérisation précise des matériaux.</p>
            <h4>Caractéristiques techniques :</h4>
            <ul>
                <li>✅ Surface spécifique de 0.01 à > 2000 m²/g</li>
                <li>✅ Volume poreux de 0.0001 à > 2.0 cm³/g</li>
                <li>✅ Diamètre de pores de 3.5 à 5000 Å</li>
                <li>✅ Analyse multi-gaz : N₂, Ar, CO₂, etc.</li>
                <li>✅ Ports de dégazage : 2 préparateurs</li>
                <li>✅ Analyse simultanée de 2 échantillons</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col_eq2:
        st.image("https://micromeritrics.com.cn/wp-content/uploads/2024/01/ASAP-2020-plus-micromeritics.png", 
                caption="Micromeritics ASAP 2020 - Analyseur de surface et porosité",
                use_column_width=True)
    
    st.markdown("## 📊 Analyses disponibles")
    
    col_ana1, col_ana2, col_ana3 = st.columns(3)
    
    with col_ana1:
        st.markdown("""
        <div class="analysis-card" style="cursor:default;">
            <h4>📈 Surface spécifique</h4>
            <p>Méthode BET multipoints pour une mesure précise de la surface spécifique des matériaux.</p>
            <p><span class="badge">Catalyseurs, adsorbants, nanomatériaux</span></p>
        </div>
        """, unsafe_allow_html=True)
    
    with col_ana2:
        st.markdown("""
        <div class="analysis-card" style="cursor:default;">
            <h4>🕳️ Porosité</h4>
            <p>Distribution de taille des pores par méthodes BJH, DFT et t-plot.</p>
            <p><span class="badge">Zéolithes, MOFs, matériaux mésoporeux</span></p>
        </div>
        """, unsafe_allow_html=True)
    
    with col_ana3:
        st.markdown("""
        <div class="analysis-card" style="cursor:default;">
            <h4>📊 Isothermes</h4>
            <p>Isothermes complètes d'adsorption/désorption à 77K (N₂) et 273K (CO₂).</p>
            <p><span class="badge">Caractérisation complète de la texture</span></p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("## 🔜 Prochainement disponibles")
    
    col_fut1, col_fut2 = st.columns(2)
    
    with col_fut1:
        st.markdown("""
        <div class="info-card">
            <h4>🔥 Chimisorption TPR</h4>
            <p>Réduction en température programmée pour l'étude des catalyseurs</p>
            <p><em>Disponible à partir de Septembre 2026</em></p>
        </div>
        """, unsafe_allow_html=True)
    
    with col_fut2:
        st.markdown("""
        <div class="info-card">
            <h4>☀️ UV-Vis Solide</h4>
            <p>Spectroscopie UV-Visible en phase solide (réflectance diffuse)</p>
            <p><em>Disponible à partir de Janvier 2027</em></p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("## 📰 Actualités")
    
    # Récupérer les actualités depuis Supabase
    news_list = get_all_news()
    if news_list:
        for i in range(0, len(news_list), 2):
            cols = st.columns(2)
            for j in range(2):
                if i + j < len(news_list):
                    news = news_list[i + j]
                    with cols[j]:
                        if news.get('image_url'):
                            st.image(news['image_url'], use_column_width=True)
                        st.markdown(f"""
                        <div class="info-card">
                            <h4>{news['title']}</h4>
                            <p><small>{news['created_at'][:10]}</small></p>
                            <p>{news['content']}</p>
                        </div>
                        """, unsafe_allow_html=True)
    else:
        st.info("Aucune actualité pour le moment.")
    
    st.markdown("---")
    
    with st.expander("🎥 Voir la vidéo de présentation"):
        st.video("https://www.youtube.com/watch?v=placeholder")
        st.caption("Présentation du laboratoire et de l'ASAP 2020")
