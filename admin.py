import streamlit as st
from utils import get_all_requests, mark_sample_completed

def check_password():
    def password_entered():
        if st.session_state["password"] == st.secrets["ADMIN_PASSWORD"]:
            st.session_state["password_correct"] = True
            del st.session_state["password"]
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        st.text_input(
            "Mot de passe administrateur", type="password", on_change=password_entered, key="password"
        )
        return False
    elif not st.session_state["password_correct"]:
        st.text_input(
            "Mot de passe administrateur", type="password", on_change=password_entered, key="password"
        )
        st.error("😕 Mot de passe incorrect")
        return False
    else:
        return True

def show_admin():
    st.markdown("""
    <div class="main-header">
        <h1>🔐 Panneau d'administration</h1>
        <p>Gestion des demandes et suivi des analyses</p>
    </div>
    """, unsafe_allow_html=True)

    if not check_password():
        return

    st.success("Connexion réussie")

    requests = get_all_requests()
    if not requests:
        st.info("Aucune demande pour le moment.")
        return

    for req in requests:
        with st.expander(f"Demande {req['request_id']} - {req['researcher_name']} ({req.get('date_demande', 'Date inconnue')})"):
            st.write(f"**Email chercheur:** {req['researcher_email']}")
            st.write(f"**Organisme:** {req.get('organisation', '')}")
            st.write("**Échantillons:**")

            samples = req.get('samples', [])
            for idx, sample in enumerate(samples):
                col1, col2, col3 = st.columns([2, 1, 2])
                with col1:
                    st.write(f"**{sample.get('name', 'N/A')}** - {sample.get('nature', '')} (Traitement: {sample.get('temp', 'non spécifié')}°C)")
                with col2:
                    if sample.get('completed', False):
                        st.success("✅ Terminé")
                    else:
                        st.warning("⏳ En cours")
                with col3:
                    if not sample.get('completed', False):
                        if st.button(f"Marquer comme terminé", key=f"complete_{req['request_id']}_{idx}"):
                            success = mark_sample_completed(
                                req['request_id'],
                                idx,
                                sample.get('name', 'échantillon'),
                                req['researcher_email']
                            )
                            if success:
                                st.success(f"Email envoyé à {req['researcher_email']} pour l'échantillon {sample.get('name')}")
                                st.rerun()
                            else:
                                st.error("Erreur lors de la mise à jour")
