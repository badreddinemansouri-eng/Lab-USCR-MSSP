import streamlit as st

def show_home():
    st.markdown("""
    <div class="main-header">
        <h1>🧪 Unité de Service commune de Recherche</h1>
        <h2>Mesure de Surface Spécifique et de Porosité</h2>
        <p style="font-size: 1.2rem;">Analyse texturale de précision avec le Micromeritics ASAP 2020</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("## 🎯 Bienvenue")
        st.markdown("""
        Notre unité est dédiée à la caractérisation texturale des matériaux poreux et divisés. 
        Nous mettons à disposition des chercheurs et industriels un équipement de pointe pour 
        l'analyse de surface spécifique et de porosité.
        
        **Notre mission** : Fournir des mesures précises et reproductibles pour accompagner 
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
        st.markdown("### 👥 Équipe")
        st.markdown("""
        **Technicien**  
        Badreddine Mansouri  
        *Responsable des analyses*
        
        **Directeur**  
        Pr. Lassaad BEN HAMMOUDA  
        *Responsable scientifique*
        """)
        
        st.markdown("""
        <a href="#" class="custom-button" onclick="alert('Redirection vers le formulaire')">
            Faire une demande →
        </a>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.markdown("## 🔬 Notre équipement principal")
    
    col_eq1, col_eq2 = st.columns(2)
    
    with col_eq1:
        st.markdown("""
        <div class="info-card">
            <h3>Micromeritics ASAP 2020</h3>
            <p>L'ASAP 2020 est un analyseur de surface et de porosité de haute performance, 
            conçu pour la caractérisation précise des matériaux.</p>
            
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
        # Replace with your actual photo
        st.image("https://via.placeholder.com/600x400?text=Micromeritics+ASAP+2020", 
                caption="Micromeritics ASAP 2020 - Analyseur de surface et porosité",
                use_column_width=True)
    
    st.markdown("## 📊 Analyses disponibles")
    
    col_ana1, col_ana2, col_ana3 = st.columns(3)
    
    with col_ana1:
        st.markdown("""
        <div class="info-card">
            <h4>📈 Surface spécifique</h4>
            <p>Méthode BET multipoints pour une mesure précise de la surface spécifique des matériaux.</p>
            <p><strong>Applications :</strong> Catalyseurs, adsorbants, nanomatériaux</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col_ana2:
        st.markdown("""
        <div class="info-card">
            <h4>🕳️ Porosité</h4>
            <p>Distribution de taille des pores par méthodes BJH, DFT et t-plot.</p>
            <p><strong>Applications :</strong> Zéolithes, MOFs, matériaux mésoporeux</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col_ana3:
        st.markdown("""
        <div class="info-card">
            <h4>📊 Isothermes</h4>
            <p>Isothermes complètes d'adsorption/désorption à 77K (N₂) et 273K (CO₂).</p>
            <p><strong>Applications :</strong> Caractérisation complète de la texture</p>
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
    
    col_news1, col_news2 = st.columns(2)
    
    with col_news1:
        st.markdown("""
        <div class="info-card">
            <h4>📢 Nouvelle formation</h4>
            <p><small>15 Mars 2026</small></p>
            <p>Formation à l'utilisation de l'ASAP 2020 ouverte aux chercheurs et doctorants. 
            Inscriptions jusqu'au 30 Mars.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col_news2:
        st.markdown("""
        <div class="info-card">
            <h4>🏆 Publication collaborative</h4>
            <p><small>10 Février 2026</small></p>
            <p>Notre unité a contribué à une étude sur les nouveaux MOFs pour le stockage de gaz, 
            publiée dans Chemistry of Materials.</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    with st.expander("🎥 Voir la vidéo de présentation"):
        st.video("https://www.youtube.com/watch?v=placeholder")  # Replace with your video
        st.caption("Présentation du laboratoire et de l'ASAP 2020")
