import streamlit as st

def show_isothermes():
    st.markdown("""
    <div style="animation: fadeInUp 0.8s ease;">
        <h1 style="color:#2c3e50; font-weight:700;">📊 Isothermes d'adsorption/désorption</h1>
        <img src="https://via.placeholder.com/1200x400?text=Micromeritics+ASAP+2020+-+Isothermes" style="width:100%; border-radius:20px; margin:20px 0; box-shadow:0 10px 30px rgba(0,0,0,0.1);" alt="Isothermes">
        
        <div class="info-card">
            <h3>🔬 Classification IUPAC</h3>
            <p>La forme de l'isotherme renseigne sur la nature poreuse du matériau. L'ASAP 2020 permet d'obtenir des isothermes complètes avec une haute résolution.</p>
            <table>
                <tr><th>Type</th><th>Description</th><th>Matériaux typiques</th></tr>
                <tr><td><strong>Type I</strong></td><td>Microporeux, plateau prononcé</td><td>Zéolithes, charbons actifs</td></tr>
                <tr><td><strong>Type II</strong></td><td>Non-poreux ou macroporeux</td><td>Poudres, pigments</td></tr>
                <tr><td><strong>Type IV</strong></td><td>Mésoporeux avec hystérésis</td><td>Catalyseurs, silices mésoporeuses</td></tr>
                <tr><td><strong>Type IVa</strong></td><td>Hystérésis de type H1/H2</td><td>Pores cylindriques / "bouteille d'encre"</td></tr>
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
            <img src="https://via.placeholder.com/800x400?text=Isotherme+type+IV+avec+hysteresis" style="width:100%; border-radius:15px; margin:10px 0;" alt="Isotherme type IV">
            <p style="font-style:italic; color:#6c757d; text-align:center;">Isotherme de type IV caractéristique des matériaux mésoporeux, avec boucle d'hystérésis.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
