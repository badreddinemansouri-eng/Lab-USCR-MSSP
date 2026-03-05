import streamlit as st

def show_isothermes():
    st.markdown("""
    <div style="animation: fadeIn 0.8s ease;">
        <h1 style="color:#2c3e50;">📊 Isothermes d'adsorption/désorption</h1>
        <img src="https://via.placeholder.com/800x400?text=Isothermes+N2+CO2" style="width:100%; border-radius:10px; margin:20px 0;" alt="Isothermes">
        
        <div class="info-card">
            <h3>🔬 Classification IUPAC</h3>
            <p>La forme de l'isotherme renseigne sur la nature poreuse du matériau. L'ASAP 2020 permet d'obtenir des isothermes complètes avec une haute résolution.</p>
            <table style="width:100%; border-collapse: collapse;">
                <tr style="background-color:#667eea; color:white;">
                    <th style="padding:8px;">Type</th>
                    <th style="padding:8px;">Description</th>
                    <th style="padding:8px;">Matériaux typiques</th>
                </tr>
                <tr><td style="border:1px solid #ddd; padding:8px;"><strong>Type I</strong></td><td style="border:1px solid #ddd; padding:8px;">Micropor eux, plateau prononcé</td><td style="border:1px solid #ddd; padding:8px;">Zéolithes, charbons actifs</td></tr>
                <tr><td style="border:1px solid #ddd; padding:8px;"><strong>Type II</strong></td><td style="border:1px solid #ddd; padding:8px;">Non-poreux ou macroporeux</td><td style="border:1px solid #ddd; padding:8px;">Poudres, pigments</td></tr>
                <tr><td style="border:1px solid #ddd; padding:8px;"><strong>Type IV</strong></td><td style="border:1px solid #ddd; padding:8px;">Mésoporeux avec hystérésis</td><td style="border:1px solid #ddd; padding:8px;">Catalyseurs, silices mésoporeuses</td></tr>
                <tr><td style="border:1px solid #ddd; padding:8px;"><strong>Type IVa</strong></td><td style="border:1px solid #ddd; padding:8px;">Hystérésis de type H1/H2</td><td style="border:1px solid #ddd; padding:8px;">Pores cylindriques / "bouteille d'encre"</td></tr>
            </table>
        </div>
        
        <div class="info-card">
            <h3>⚙️ Fonctionnalités avancées du logiciel MicroActive</h3>
            <ul>
                <li><strong>Superposition de données :</strong> comparer jusqu'à 25 fichiers d'isothermes</li>
                <li><strong>Smart Dosing™ :</strong> apprentissage automatique du comportement d'adsorption pour optimiser les doses de gaz</li>
                <li><strong>Exportation directe</strong> vers tableurs pour analyses complémentaires</li>
                <li><strong>Sélection interactive</strong> des plages de données en temps réel</li>
            </ul>
        </div>
        
        <div class="info-card">
            <h3>🧪 Applications</h3>
            <ul>
                <li>Étude de la texture complète des matériaux (surface, volume poreux, taille des pores)</li>
                <li>Détermination de l'énergie d'adsorption (isothermes à différentes températures)</li>
                <li>Analyse de la microporosité fine avec CO₂ à 273 K</li>
                <li>Caractérisation des adsorbants pour le stockage de gaz (H₂, CH₄, CO₂)</li>
            </ul>
        </div>
        
        <div class="info-card">
            <h3>📈 Exemple d'isotherme</h3>
            <img src="https://via.placeholder.com/600x300?text=Isotherme+type+IV+avec+hysteresis" style="width:100%; border-radius:10px;" alt="Isotherme type IV">
            <p style="font-style:italic; margin-top:10px;">Isotherme de type IV caractéristique des matériaux mésoporeux, avec boucle d'hystérésis.</p>
        </div>
        
        <p style="margin-top:30px;">🔙 <a href="#" onclick="window.location.href='?page=Analyses'" style="color:#667eea;">Retour aux analyses</a></p>
    </div>
    """, unsafe_allow_html=True)
