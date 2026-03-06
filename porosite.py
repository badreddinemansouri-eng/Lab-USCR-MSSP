import streamlit as st

def show_porosite():
    st.markdown("""
    <div style="animation: fadeInUp 0.8s ease;">
        <h1 style="color:#2c3e50; font-weight:700;">🕳️ Analyse de la porosité</h1>
        <img src="https://via.placeholder.com/1200x400?text=Micromeritics+ASAP+2020+-+Porosité" style="width:100%; border-radius:20px; margin:20px 0; box-shadow:0 10px 30px rgba(0,0,0,0.1);" alt="Analyse porosité">
        
        <div class="info-card">
            <h3>🔬 Méthodes disponibles</h3>
            <p>L'ASAP 2020 propose plusieurs modèles pour caractériser la distribution de taille des pores, du domaine microporeux au mésoporeux.</p>
            <table>
                <tr><th>Méthode</th><th>Principe</th><th>Domaine</th></tr>
                <tr><td><strong>BJH</strong></td><td>Modèle de Kelvin pour la condensation capillaire</td><td>Mésopores (2-50 nm)</td></tr>
                <tr><td><strong>t-plot</strong></td><td>Épaisseur statistique de la couche adsorbée</td><td>Volume microporeux, surface externe</td></tr>
                <tr><td><strong>DFT/NLDFT</strong></td><td>Théorie de la fonctionnelle de la densité</td><td>Micro et mésopores (distribution complète)</td></tr>
                <tr><td><strong>Horvath-Kawazoe</strong></td><td>Potentiel dans les micropores</td><td>Micropores étroits (< 1 nm)</td></tr>
            </table>
        </div>
        
        <div class="info-card">
            <h3>⚙️ Spécifications techniques</h3>
            <ul>
                <li><strong>Domaine de pression :</strong> 1,3 × 10⁻⁹ à 1,0 P/P₀</li>
                <li><strong>Option micropore :</strong> transducteur 0,1 mmHg pour pores de 0,35 à 3 nm</li>
                <li><strong>Six ports d'entrée de gaz</strong> avec dédiés pour vapeur et hélium</li>
                <li><strong>Logiciel MicroActive</strong> avec calculs intégrés des modèles avancés</li>
            </ul>
        </div>
        
        <div class="info-card">
            <h3>🧪 Applications</h3>
            <ul>
                <li><strong>MOFs et zéolithes :</strong> caractérisation des matériaux de structure pour stockage de gaz</li>
                <li><strong>Charbons actifs :</strong> optimisation de la distribution poreuse pour l'adsorption</li>
                <li><strong>Stockage d'énergie :</strong> électrodes de supercondensateurs</li>
                <li><strong>Géosciences :</strong> porosité des roches pour l'exploration pétrolière</li>
            </ul>
        </div>
        
        <div class="info-card">
            <h3>📊 Exemple de distribution de pores</h3>
            <img src="https://via.placeholder.com/800x400?text=Distribution+de+pores+BJH+DFT" style="width:100%; border-radius:15px; margin:10px 0;" alt="Distribution de pores">
            <p style="font-style:italic; color:#6c757d; text-align:center;">Courbe de distribution obtenue par la méthode BJH (mésopores) et DFT (micropores).</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
