import streamlit as st

def show_bet():
    st.markdown("""
    <div style="animation: fadeInUp 0.8s ease;">
        <h1 style="color:#2c3e50; font-weight:700;">📈 Analyse BET – Surface spécifique</h1>
        <img src="https://via.placeholder.com/1200x400?text=Micromeritics+ASAP+2020+-+Analyse+BET" style="width:100%; border-radius:20px; margin:20px 0; box-shadow:0 10px 30px rgba(0,0,0,0.1);" alt="Analyse BET">
        
        <div class="info-card">
            <h3>🔬 Principe de la méthode</h3>
            <p>La méthode BET (Brunauer-Emmett-Teller) est la technique de référence pour déterminer la surface spécifique des matériaux. Elle repose sur l'adsorption physique d'un gaz inerte (généralement de l'azote) à la température de l'azote liquide (77 K). L'équation BET permet de relier la quantité de gaz adsorbé à la pression relative et d'en déduire la surface spécifique en m²/g.</p>
        </div>
        
        <div class="info-card">
            <h3>⚙️ Spécifications techniques (ASAP 2020)</h3>
            <ul>
                <li><strong>Domaine de mesure :</strong> de 0,01 à > 2000 m²/g (jusqu'à 0,0005 m²/g avec option Krypton)</li>
                <li><strong>Gaz utilisés :</strong> N₂, Ar, CO₂, Kr</li>
                <li><strong>Précision des transducteurs :</strong> 0,12 % de la lecture</li>
                <li><strong>Ports de dégazage :</strong> 2 préparateurs indépendants</li>
                <li><strong>Analyse simultanée :</strong> jusqu'à 2 échantillons</li>
            </ul>
        </div>
        
        <div class="info-card">
            <h3>🧪 Applications</h3>
            <table>
                <tr><th>Domaine</th><th>Application</th></tr>
                <tr><td>Catalyse</td><td>Caractérisation des supports (alumine, silice, zéolithes)</td></tr>
                <tr><td>Pharmaceutique</td><td>Contrôle qualité des principes actifs et excipients</td></tr>
                <tr><td>Nanomatériaux</td><td>Nanotubes, nanoparticules, graphène</td></tr>
                <tr><td>Céramiques</td><td>Optimisation du frittage et des propriétés mécaniques</td></tr>
            </table>
        </div>
        
        <div class="info-card">
            <h3>📈 Exemple de courbe BET</h3>
            <img src="https://via.placeholder.com/800x400?text=Courbe+BET+multipoints" style="width:100%; border-radius:15px; margin:10px 0;" alt="Courbe BET">
            <p style="font-style:italic; color:#6c757d; text-align:center;">La partie linéaire (généralement entre P/P₀ = 0,05 et 0,30) permet de déterminer la capacité de la monocouche et la surface spécifique.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
