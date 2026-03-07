import streamlit as st
from home import show_home
from analyses import show_analyses
from request import show_request
from resources import show_resources
from contact import show_contact
from admin import show_admin
from bet import show_bet
from porosite import show_porosite
from isothermes import show_isothermes
from utils_i18n import get_text

st.set_page_config(
    page_title="USR Mesure de Surface Spécifique et Porosité",
    page_icon="🧪",
    layout="wide",
    initial_sidebar_state="collapsed"
)

if not st.secrets.get("debug", False):
    st.set_option('client.showErrorDetails', False)

if "theme" not in st.session_state:
    st.session_state.theme = "light"
if "lang" not in st.session_state:
    st.session_state.lang = "fr"
if "page" not in st.session_state:
    st.session_state.page = get_text("nav_home", st.session_state.lang)

def toggle_theme():
    st.session_state.theme = "dark" if st.session_state.theme == "light" else "light"

# Liste des libellés de navigation
nav_labels = [
    get_text("nav_home", st.session_state.lang),
    get_text("nav_analyses", st.session_state.lang),
    get_text("nav_request", st.session_state.lang),
    get_text("nav_resources", st.session_state.lang),
    get_text("nav_contact", st.session_state.lang),
    get_text("nav_admin", st.session_state.lang)
]

# Créer une ligne de colonnes : 6 boutons + 2 contrôles
cols = st.columns(len(nav_labels) + 2)

# Placer les boutons de navigation dans les premières colonnes
for i, label in enumerate(nav_labels):
    with cols[i]:
        if st.button(label, key=f"nav_{i}"):
            st.session_state.page = label
            st.rerun()

# Contrôle thème (avant-dernière colonne)
with cols[-2]:
    if st.button("☀️" if st.session_state.theme == "light" else "🌙", key="theme_btn"):
        toggle_theme()
        st.rerun()

# Contrôle langue (dernière colonne)
with cols[-1]:
    lang = st.selectbox("Langue", ["fr", "en"], index=0 if st.session_state.lang == "fr" else 1,
                        label_visibility="collapsed", key="lang_selector")
    if lang != st.session_state.lang:
        st.session_state.lang = lang
        st.rerun()

# Routage
if st.session_state.page == get_text("nav_home", st.session_state.lang):
    show_home()
elif st.session_state.page == get_text("nav_analyses", st.session_state.lang):
    show_analyses()
elif st.session_state.page == get_text("nav_request", st.session_state.lang):
    show_request()
elif st.session_state.page == get_text("nav_resources", st.session_state.lang):
    show_resources()
elif st.session_state.page == get_text("nav_contact", st.session_state.lang):
    show_contact()
elif st.session_state.page == get_text("nav_admin", st.session_state.lang):
    show_admin()
