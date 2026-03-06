import streamlit as st
from utils import get_all_requests, mark_sample_completed, get_all_news, add_news, update_news, delete_news
from datetime import datetime

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
    <div class="main-header hero" style="background:linear-gradient(135deg, #1e2b4f 0%, #2a3f6e 100%);">
        <h1>🔐 Panneau d'administration</h1>
        <p>Gestion des demandes et des actualités</p>
    </div>
    """, unsafe_allow_html=True)

    if not check_password():
        return

    st.success("Connexion réussie")

    # Onglets dans l'admin
    tab1, tab2 = st.tabs(["📋 Demandes", "📰 Actualités"])

    with tab1:
        st.subheader("Gestion des demandes d'analyse")
        requests = get_all_requests()
        if not requests:
            st.info("Aucune demande pour le moment.")
        else:
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

    with tab2:
        st.subheader("Gestion des actualités")
        
        # Formulaire d'ajout
        with st.expander("➕ Ajouter une actualité", expanded=False):
            with st.form("add_news_form"):
                title = st.text_input("Titre *")
                content = st.text_area("Contenu *")
                image_url = st.text_input("URL de l'image (optionnel)")
                submitted = st.form_submit_button("Publier")
                if submitted and title and content:
                    add_news(title, content, image_url)
                    st.success("Actualité ajoutée !")
                    st.rerun()
        
        # Liste des actualités existantes
        news_list = get_all_news()
        if news_list:
            for news in news_list:
                with st.expander(f"📰 {news['title']} ({news['created_at'][:10]})"):
                    st.write(f"**Contenu:** {news['content']}")
                    st.write(f"**Image:** {news.get('image_url', 'aucune')}")
                    
                    col_edit, col_delete = st.columns(2)
                    with col_edit:
                        if st.button("✏️ Modifier", key=f"edit_{news['id']}"):
                            st.session_state[f"edit_news_{news['id']}"] = True
                    with col_delete:
                        if st.button("🗑️ Supprimer", key=f"delete_{news['id']}"):
                            delete_news(news['id'])
                            st.success("Actualité supprimée")
                            st.rerun()
                    
                    # Formulaire d'édition (si bouton cliqué)
                    if st.session_state.get(f"edit_news_{news['id']}", False):
                        with st.form(f"edit_form_{news['id']}"):
                            new_title = st.text_input("Titre", value=news['title'])
                            new_content = st.text_area("Contenu", value=news['content'])
                            new_image = st.text_input("URL image", value=news.get('image_url', ''))
                            save = st.form_submit_button("Enregistrer")
                            if save:
                                update_news(news['id'], new_title, new_content, new_image)
                                st.success("Actualité mise à jour")
                                del st.session_state[f"edit_news_{news['id']}"]
                                st.rerun()
        else:
            st.info("Aucune actualité pour le moment.")
