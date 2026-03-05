import os
import uuid
from datetime import datetime
import streamlit as st
from supabase import create_client, Client
from fpdf import FPDF
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

# ---------- Nettoyage du texte ----------
def clean_text(text):
    """Remplace les caractères Unicode problématiques par leurs équivalents ASCII."""
    if text is None:
        return ""
    replacements = {
        "\u2019": "'",
        "\u2018": "'",
        "\u201c": '"',
        "\u201d": '"',
        "\u2013": "-",
        "\u2014": "--",
        "\u00e9": "e",
        "\u00e8": "e",
        "\u00ea": "e",
        "\u00e2": "a",
        "\u00f4": "o",
        "\u00ee": "i",
        "\u00fb": "u",
        "\u00e0": "a",
        "\u00e7": "c",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text

# ---------- Formatage de la date ----------
def format_date(date_str):
    """Convertit une date ISO (YYYY-MM-DD) en format JJ/MM/AAAA."""
    if not date_str:
        return datetime.now().strftime("%d/%m/%Y")
    try:
        d = datetime.strptime(date_str, "%Y-%m-%d")
        return d.strftime("%d/%m/%Y")
    except:
        return date_str

# ---------- Supabase ----------
def init_supabase() -> Client:
    url = st.secrets["SUPABASE_URL"]
    key = st.secrets["SUPABASE_KEY"]
    return create_client(url, key)

def save_request(data: dict) -> str:
    supabase = init_supabase()
    today = datetime.now().strftime("%Y%m%d")
    random_part = str(uuid.uuid4())[:4].upper()
    request_id = f"MSSP_{today}_{random_part}"
    data["request_id"] = request_id
    data["created_at"] = datetime.now().isoformat()
    for sample in data.get("samples", []):
        sample["completed"] = False
    if "date_demande" in data and data["date_demande"]:
        data["date_demande"] = str(data["date_demande"])
    supabase.table("requests").insert(data).execute()
    return request_id

def get_all_requests():
    supabase = init_supabase()
    response = supabase.table("requests").select("*").order("created_at", desc=True).execute()
    return response.data

def mark_sample_completed(request_id: str, sample_index: int, sample_name: str, researcher_email: str) -> bool:
    supabase = init_supabase()
    response = supabase.table("requests").select("samples").eq("request_id", request_id).execute()
    if not response.data:
        return False
    samples = response.data[0]["samples"]
    if sample_index >= len(samples):
        return False
    samples[sample_index]["completed"] = True
    supabase.table("requests").update({"samples": samples}).eq("request_id", request_id).execute()
    send_completion_email(sample_name, researcher_email, request_id)
    return True

# ---------- PDF Generation (layout amélioré) ----------
def generate_pdf(data: dict) -> bytes:
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=10)

    # ----- Trois logos (placeholders) -----
    pdf.set_fill_color(200, 200, 200)
    pdf.rect(10, 8, 30, 30, 'F')
    pdf.set_xy(10, 15)
    pdf.set_font("Arial", 'B', 8)
    pdf.cell(30, 6, clean_text("Logo"), align='C', border=0)

    pdf.set_fill_color(200, 200, 200)
    pdf.rect(90, 8, 30, 30, 'F')
    pdf.set_xy(90, 15)
    pdf.cell(30, 6, clean_text("Logo"), align='C')

    pdf.set_fill_color(200, 200, 200)
    pdf.rect(170, 8, 30, 30, 'F')
    pdf.set_xy(170, 15)
    pdf.cell(30, 6, clean_text("Logo"), align='C')

    pdf.set_font("Arial", size=10)

    # ----- Titre -----
    pdf.set_y(40)
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(0, 10, txt=clean_text("Demande d'une mesure de la surface specifique et de la porosite"), ln=True, align='C')
    pdf.ln(5)

    # ----- Informations chercheur (avec gestion des longs textes) -----
    pdf.set_font("Arial", size=9)
    line_height = 6

    # Ligne 1 : Nom + Tél
    pdf.cell(55, line_height, clean_text("Nom et prénom du demandeur :"), 0, 0)
    pdf.cell(70, line_height, clean_text(data.get('researcher_name', '__________________')), 0, 0)
    pdf.cell(20, line_height, clean_text("Tél :"), 0, 0)
    pdf.cell(0, line_height, clean_text(data.get('researcher_phone', '__________________')), 0, 1)

    # Ligne 2 : Email / Qualité
    pdf.cell(55, line_height, clean_text("Email :"), 0, 0)
    pdf.cell(70, line_height, clean_text(data.get('researcher_email', '__________________')), 0, 0)
    pdf.cell(20, line_height, clean_text("Qualité :"), 0, 0)
    pdf.cell(0, line_height, clean_text(data.get('qualification', '__________________')), 0, 1)

    # Ligne 3 : Organisme (multi_cell pour les longs textes)
    pdf.cell(55, line_height, clean_text("Organisme :"), 0, 0)
    x_org = pdf.get_x()
    y_org = pdf.get_y()
    pdf.multi_cell(0, line_height, clean_text(data.get('organisation', '__________________')), 0, 'L')
    # multi_cell a déjà sauté à la ligne suivante

    # Ligne 4 : Diplôme
    pdf.set_font("Arial", size=9)
    pdf.cell(55, line_height, clean_text("Diplôme en cours :"), 0, 0)
    pdf.multi_cell(0, line_height, clean_text(data.get('diploma', '__________________')), 0, 'L')

    # Ligne 5 : Encadrant
    pdf.set_font("Arial", size=9)
    pdf.cell(55, line_height, clean_text("Nom et prénom de l'encadrant :"), 0, 0)
    pdf.multi_cell(0, line_height, clean_text(data.get('supervisor_name', '__________________')), 0, 'L')

    # Ligne 6 : Directeur de laboratoire (NOUVEAU)
    pdf.set_font("Arial", size=9)
    pdf.cell(55, line_height, clean_text("Nom et prénom du Directeur de laboratoire :"), 0, 0)
    pdf.multi_cell(0, line_height, clean_text(data.get('director_name', '__________________')), 0, 'L')

    # Ligne 7 : Laboratoire/Unité (libellé long, police plus petite)
    pdf.set_font("Arial", size=8)
    pdf.cell(65, line_height, clean_text("Laboratoire/Unité de Recherche/Service (Nom & Code) :"), 0, 0)
    pdf.set_font("Arial", size=9)
    pdf.multi_cell(0, line_height, clean_text(data.get('lab_unit', '__________________')), 0, 'L')

    pdf.ln(5)

    # ----- Tableau des échantillons (4 lignes) -----
    pdf.set_font("Arial", 'B', 10)
    pdf.cell(0, line_height, clean_text("Nombre d'échantillons (max 4)"), ln=True)
    pdf.set_font("Arial", size=9)

    col_widths = [40, 60, 40]  # Nom, Nature, Traitement
    pdf.cell(col_widths[0], line_height, clean_text("Nom (max 8 car.)"), 1, 0, 'C')
    pdf.cell(col_widths[1], line_height, clean_text("Nature de l'échantillon"), 1, 0, 'C')
    pdf.cell(col_widths[2], line_height, clean_text("Traitement (°C)"), 1, 1, 'C')

    samples = data.get('samples', [])
    for i in range(4):
        sample = samples[i] if i < len(samples) else {}
        pdf.cell(col_widths[0], line_height, clean_text(sample.get('name', '')[:8]), 1)
        pdf.cell(col_widths[1], line_height, clean_text(sample.get('nature', '')), 1)
        pdf.cell(col_widths[2], line_height, clean_text(sample.get('temp', '')), 1, 1)

    pdf.ln(5)

    # ----- Traitement de l'échantillon -----
    pdf.set_font("Arial", 'B', 10)
    pdf.cell(0, line_height, clean_text("Traitement de l'échantillon :"), ln=True)
    pdf.set_font("Arial", size=9)
    ambiance = "[X]" if data.get('treatment_ambiance') else "[ ]"
    pdf.cell(30, line_height, clean_text(f"{ambiance} Ambiance"), 0, 0)
    pdf.cell(30, line_height, clean_text("Autre [ ]"), 0, 0)
    pdf.cell(15, line_height, clean_text("T ="), 0, 0)
    pdf.cell(30, line_height, clean_text(data.get('treatment_temperature', '_____ °C')), 0, 1)

    pdf.cell(0, line_height, clean_text("Votre échantillon est stable jusqu'à la température : T = __________ °C"), ln=True)
    pdf.ln(5)

    # ----- Analyses demandées et signature (deux colonnes) -----
    start_y = pdf.get_y()

    # Colonne gauche : analyses
    pdf.set_font("Arial", 'B', 10)
    pdf.cell(0, line_height, clean_text("Types d'analyses demandées :"), ln=True)
    pdf.set_font("Arial", size=9)

    analysis_list = ["S BET", "Porosité", "t-plot", "BJH-des", "Isothermes"]
    selected = data.get('analysis_types', [])

    for analysis in analysis_list:
        checked = "[X]" if analysis in selected else "[ ]"
        pdf.cell(50, line_height, clean_text(f"{checked} {analysis}"), 0, 1)

    # Colonne droite : signature
    pdf.set_xy(120, start_y)
    pdf.set_font("Arial", 'B', 9)
    pdf.multi_cell(70, line_height, clean_text("Signature & cachet de l'Encadrant / du Directeur du Laboratoire (Obligatoire) :"))
    pdf.set_xy(120, pdf.get_y())
    pdf.cell(70, line_height, clean_text("......................................"), ln=True)

    # Ajustement vertical
    pdf.set_y(max(pdf.get_y(), start_y + len(analysis_list)*line_height + 10))

    # ----- Avis du responsable -----
    pdf.ln(5)
    pdf.set_font("Arial", size=10)
    pdf.cell(0, line_height, clean_text("Avis du responsable des équipements : L. BEN HAMMOUDA"), ln=True)
    pdf.ln(5)

    # ----- Date et référence -----
    date_str = format_date(data.get('date_demande'))
    pdf.cell(35, line_height, clean_text("Date de la demande :"), 0, 0)
    pdf.cell(50, line_height, clean_text(" " + date_str), 0, 0)
    pdf.cell(45, line_height, clean_text("Références de la Demande :"), 0, 0)
    pdf.cell(0, line_height, clean_text(" " + data.get('request_id', 'MSSP_2025')), 0, 1)

    return pdf.output(dest='S')

# ---------- Email Functions (inchangées) ----------
def send_email(recipient: str, request_id: str, pdf_bytes: bytes):
    sender = st.secrets["EMAIL_USER"]
    password = st.secrets["EMAIL_PASSWORD"]

    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = recipient
    msg['Subject'] = f"Votre demande d'analyse {request_id}"

    body = f"""
    Bonjour,

    Vous trouverez en pièce jointe le formulaire de demande d'analyse pré-rempli pour la demande N° {request_id}.

    Veuillez imprimer ce document, le faire signer et cacheter par votre directeur de laboratoire, puis le déposer à notre unité.

    Cordialement,
    Badreddine Mansouri
    Unité de Service commune de Recherche
    """
    msg.attach(MIMEText(body, 'plain'))

    part = MIMEApplication(pdf_bytes, Name=f"Demande_{request_id}.pdf")
    part['Content-Disposition'] = f'attachment; filename="Demande_{request_id}.pdf"'
    msg.attach(part)

    with smtplib.SMTP(st.secrets["EMAIL_HOST"], st.secrets["EMAIL_PORT"]) as server:
        server.starttls()
        server.login(sender, password)
        server.send_message(msg)

def send_completion_email(sample_name: str, recipient: str, request_id: str):
    sender = st.secrets["EMAIL_USER"]
    password = st.secrets["EMAIL_PASSWORD"]

    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = recipient
    msg['Subject'] = f"Analyse terminée pour l'échantillon {sample_name} (Demande {request_id})"

    body = f"""
    Bonjour,

    Nous avons le plaisir de vous informer que l'analyse de l'échantillon **{sample_name}** (demande N° {request_id}) est terminée.

    Vous pouvez venir récupérer vos résultats et votre échantillon à notre laboratoire aux heures d'ouverture.

    Cordialement,
    Badreddine Mansouri
    Unité de Service commune de Recherche
    """
    msg.attach(MIMEText(body, 'plain'))

    with smtplib.SMTP(st.secrets["EMAIL_HOST"], st.secrets["EMAIL_PORT"]) as server:
        server.starttls()
        server.login(sender, password)
        server.send_message(msg)
