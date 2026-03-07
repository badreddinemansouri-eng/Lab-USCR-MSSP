import streamlit as st

def nav_link(label, page_key, icon=None):
    """Affiche un lien de navigation stylisé."""
    is_active = (st.session_state.page == page_key)
    icon_html = f'<span class="nav-icon">{icon}</span>' if icon else ""
    active_class = "active" if is_active else ""
    html = f"""
    <div class="nav-item {active_class}" onclick="document.getElementById('nav-{page_key}').click()">
        {icon_html}
        <span class="nav-label">{label}</span>
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)
    # Bouton caché pour capturer le clic
    if st.button(label, key=f"nav_{page_key}", help=label):
        st.session_state.page = page_key
        st.rerun()

def info_card(title, content, icon=None):
    """Affiche une carte d'information."""
    icon_html = f'<div class="card-icon">{icon}</div>' if icon else ""
    st.markdown(f"""
    <div class="info-card">
        {icon_html}
        <h3>{title}</h3>
        <p>{content}</p>
    </div>
    """, unsafe_allow_html=True)

def analysis_card(title, description, badge, image_url, page_key):
    """Affiche une carte d'analyse."""
    html = f"""
    <div class="analysis-card" onclick="document.getElementById('goto-{page_key}').click()">
        <img src="{image_url}" alt="{title}">
        <h3>{title}</h3>
        <p>{description}</p>
        <div class="badge">{badge}</div>
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)
    if st.button("Voir détails", key=f"goto_{page_key}"):
        st.session_state["analysis_page"] = page_key
        st.rerun()

def hero(title, subtitle, description):
    """Affiche une section hero."""
    st.markdown(f"""
    <div class="hero">
        <h1>{title}</h1>
        <p class="hero-subtitle">{subtitle}</p>
        <p class="hero-description">{description}</p>
    </div>
    """, unsafe_allow_html=True)
