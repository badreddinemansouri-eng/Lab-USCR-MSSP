import streamlit as st

def show_porosite():
    st.markdown("""
    <div style="animation: fadeIn 0.8s ease;">
        <h1 style="color:#2c3e50;">🕳️ Analyse de la porosité</h1>
        <img src="https://via.placeholder.com/800x400?text=Distribution+de+taille+des+pores" style="width:100%; border-radius:10px; margin:20px 0;" alt="Porosité">
        
        <div class="info-card">
            <h3>🔬 Méthodes disponibles</h3>
            <p>L'ASAP 2020 propose plusieurs modèles pour caractériser la distribution de taille des pores, du domaine microporeux au mésoporeux.</p>
            <table style="width:100%; border-collapse: collapse;">
                <tr style="background-color:#667eea; color:white;">
                    <th style="padding:8px;">Méthode</th>
                    <th style="padding:8px;">Principe</th>
                    <th style="padding:8px;">Domaine</th>
                </tr>
                <tr><td style="border:1px solid #ddd; padding:8px;">BJH</td><td style="border:1px solid #ddd; padding:8px;">Modèle de Kelvin pour la condensation capillaire</td><td style="border:1px solid #ddd; padding:8px;">Mésopores (2-50 nm)</td></tr>
                <tr><td style="border:1px solid #ddd; padding:8px;">t-plot</td><td style="border:1px solid #ddd; padding:8px;">Épaisseur statistique de la couche adsorbée</td><td style="border:1px solid #ddd; padding:8px;">Volume microporeux, surface externe</td></tr>
                <tr><td style="border:1px solid #ddd; padding:8px;">DFT/NLDFT</td><td style="border:1px solid #ddd; padding:8px;">Théorie de la fonctionnelle de la densité</td><td style="border:1px solid #ddd; padding:8px;">Micro et mésopores (distribution complète)</td></tr>
                <tr><td style="border:1px solid #ddd; padding:8px;">Horvath-Kawazoe</td><td style="border:1px solid #ddd; padding:8px;">Potentiel dans les micropores</td><td style="border:1px solid #ddd; padding:8px;">Micropores étroits (< 1 nm)</td></tr>
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
            <img src="https://via.placeholder.com/600x300?text=Distribution+BJH+DFT" style="width:100%; border-radius:10px;" alt="Distribution de pores">
            <p style="font-style:italic; margin-top:10px;">Courbe de distribution obtenue par la méthode BJH (mésopores) et DFT (micropores).</p>
        </div>
        
        <p style="margin-top:30px;">🔙 <a href="#" onclick="window.location.href='?page=Analyses'" style="color:#667eea;">Retour aux analyses</a></p>
    </div>
    """, unsafe_allow_html=True)
