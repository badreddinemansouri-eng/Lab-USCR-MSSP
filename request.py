import streamlit as st
from datetime import date
from utils import save_request, generate_pdf, send_email

def show_request():
    st.markdown("""
    <div class="main-header">
        <h1>📝 Formulaire de demande d'analyse</h1>
        <p>Remplissez ce formulaire pour soumettre votre demande</p>
    </div>
    """, unsafe_allow_html=True)

    with st.form("request_form"):
        st.subheader("Informations du chercheur")
        col1, col2 = st.columns(2)
        with col1:
            researcher_name = st.text_input("Nom et prénom du demandeur *", key="name")
            researcher_email = st.text_input("Email *", key="email")
            researcher_phone = st.text_input("Tél", key="phone")
            qualification = st.text_input("Qualité", key="qualification")
        with col2:
            organisation = st.text_input("Organisme *", key="organisation")
            diploma = st.selectbox("Diplôme en cours", ["", "Habilitation", "Doctorat", "Maîtrise", "Autres"], key="diploma")
            supervisor_name = st.text_input("Nom et prénom de l’encadrant *", key="supervisor")
            director_name = st.text_input("Nom et prénom du Directeur de laboratoire *", key="director")
            lab_unit = st.text_input("Laboratoire/Unité de Recherche/Service (Nom & Code) *", key="lab_unit")

        st.subheader("Échantillons (max 4)")
        st.markdown("Chaque échantillon doit avoir un nom (max 8 caractères), une nature et une température de prétraitement éventuelle.")
        samples = []
        for i in range(4):
            with st.expander(f"Échantillon {i+1}"):
                cola, colb, colc = st.columns(3)
                with cola:
                    name = st.text_input(f"Nom (max 8)", key=f"sample_name_{i}", max_chars=8)
                with colb:
                    nature = st.text_input(f"Nature", key=f"sample_nature_{i}")
                with colc:
                    temp = st.text_input(f"Traitement (°C) *", key=f"sample_temp_{i}")
                if name or nature or temp:
                    samples.append({"name": name, "nature": nature, "temp": temp})

        st.subheader("Traitement global de l’échantillon")
        colt1, colt2 = st.columns(2)
        with colt1:
            treatment_ambiance = st.checkbox("Ambiance")
        with colt2:
            treatment_temperature = st.text_input("Si Autre, T = °C", key="global_temp")

        st.subheader("Analyses demandées")
        analysis_types = st.multiselect(
            "Sélectionnez les analyses",
            ["S BET", "Porosité", "t-plot", "BJH-des", "Isothermes"],
            key="analysis"
        )

        st.subheader("Date de la demande")
        date_demande = st.date_input("Date", value=date.today(), key="date")

        special_instructions = st.text_area("Instructions spéciales / Remarques", key="special")

        st.markdown("---")
        st.markdown("**En soumettant ce formulaire, vous recevrez un PDF par email. Vous devrez le faire signer et cacheter par votre directeur avant de le déposer au laboratoire.**")
        submitted = st.form_submit_button("Soumettre la demande")

    if submitted:
        required = [researcher_name, researcher_email, organisation, director_name, lab_unit]
        if not all(required):
            st.error("Veuillez remplir tous les champs obligatoires (*).")
            return
        if not samples:
            st.error("Veuillez renseigner au moins un échantillon.")
            return
        if not analysis_types:
            st.error("Sélectionnez au moins un type d'analyse.")
            return

        data = {
            "researcher_name": researcher_name,
            "researcher_email": researcher_email,
            "researcher_phone": researcher_phone,
            "qualification": qualification,
            "organisation": organisation,
            "diploma": diploma,
            "supervisor_name": supervisor_name,
            "director_name": director_name,
            "lab_unit": lab_unit,
            "samples": samples,
            "treatment_ambiance": treatment_ambiance,
            "treatment_temperature": treatment_temperature,
            "analysis_types": analysis_types,
            "date_demande": date_demande.isoformat() if date_demande else None,
            "special_instructions": special_instructions,
        }

        with st.spinner("Traitement de votre demande..."):
            try:
                request_id = save_request(data)
                data["request_id"] = request_id
                pdf_bytes = generate_pdf(data)
                send_email(researcher_email, request_id, pdf_bytes)
                st.success(f"Demande enregistrée ! Un email a été envoyé à {researcher_email} avec le formulaire PDF (référence {request_id}).")
            except Exception as e:
                st.error(f"Erreur : {e}")
