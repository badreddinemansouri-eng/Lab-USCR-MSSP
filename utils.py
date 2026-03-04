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

# ---------- PDF Generation (exactly like your photo) ----------
def generate_pdf(data: dict) -> bytes:
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=10)

    # ----- Three logos at the top (left, center, right) -----
    # Replace these URLs with your actual logos
    logo_left = "https://via.placeholder.com/80x80?text=Logo+Gauche"
    logo_center = "https://via.placeholder.com/80x80?text=Logo+Centre"
    logo_right = "https://via.placeholder.com/80x80?text=Logo+Droit"

    # Position logos
    pdf.image(logo_left, x=10, y=8, w=30)
    pdf.image(logo_center, x=90, y=8, w=30)  # adjust x to center
    pdf.image(logo_right, x=170, y=8, w=30)

    # ----- Title below logos -----
    pdf.set_y(30)  # move down below logos
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(0, 10, txt="Demande d’une mesure de la surface spécifique et de la porosité", ln=True, align='C')
    pdf.ln(5)

    # ----- Researcher information (two‑column layout) -----
    pdf.set_font("Arial", size=10)
    line_height = 6

    # Row1: Nom et prénom du demandeur
    pdf.cell(50, line_height, "Nom et prénom du demandeur :", 0, 0)
    pdf.cell(70, line_height, data.get('researcher_name', '__________________'), 0, 0)
    pdf.cell(30, line_height, "Tél :", 0, 0)
    pdf.cell(0, line_height, data.get('researcher_phone', '__________________'), 0, 1)

    # Row2: Email / Qualité
    pdf.cell(50, line_height, "Email :", 0, 0)
    pdf.cell(70, line_height, data.get('researcher_email', '__________________'), 0, 0)
    pdf.cell(30, line_height, "Qualité :", 0, 0)
    pdf.cell(0, line_height, data.get('qualification', '__________________'), 0, 1)

    # Row3: Organisme
    pdf.cell(50, line_height, "Organisme :", 0, 0)
    pdf.cell(0, line_height, data.get('organisation', '__________________'), 0, 1)

    # Row4: Diplôme en cours
    pdf.cell(50, line_height, "Diplôme en cours :", 0, 0)
    pdf.cell(0, line_height, data.get('diploma', '__________________'), 0, 1)

    # Row5: Nom et prénom de l’encadrant
    pdf.cell(50, line_height, "Nom et prénom de l’encadrant :", 0, 0)
    pdf.cell(0, line_height, data.get('supervisor_name', '__________________'), 0, 1)

    # Row6: Laboratoire/Unité de Recherche/Service
    pdf.cell(50, line_height, "Laboratoire/Unité de Recherche/Service (Nom & Code) :", 0, 0)
    pdf.cell(0, line_height, data.get('lab_unit', '__________________'), 0, 1)

    pdf.ln(5)

    # ----- Samples table (max 4) -----
    pdf.set_font("Arial", 'B', 10)
    pdf.cell(0, line_height, "Nombre d’échantillons (max 4)", ln=True)
    pdf.set_font("Arial", size=9)

    # Table header with temperature column
    col_widths = [40, 60, 40]  # Name, Nature, Treatment Temp
    pdf.cell(col_widths[0], line_height, "Nom (max 8 car.)", 1, 0, 'C')
    pdf.cell(col_widths[1], line_height, "Nature de l’échantillon", 1, 0, 'C')
    pdf.cell(col_widths[2], line_height, "Traitement (°C)", 1, 1, 'C')

    samples = data.get('samples', [])
    for i in range(4):  # Always show 4 rows
        sample = samples[i] if i < len(samples) else {}
        pdf.cell(col_widths[0], line_height, sample.get('name', '')[:8], 1)
        pdf.cell(col_widths[1], line_height, sample.get('nature', ''), 1)
        pdf.cell(col_widths[2], line_height, sample.get('temp', ''), 1, 1)

    pdf.ln(5)

    # ----- Treatment section -----
    pdf.set_font("Arial", 'B', 10)
    pdf.cell(0, line_height, "Traitement de l’échantillon :", ln=True)
    pdf.set_font("Arial", size=9)
    ambiance = "☒" if data.get('treatment_ambiance') else "☐"
    pdf.cell(30, line_height, f"{ambiance} Ambiance", 0, 0)
    pdf.cell(20, line_height, "Autre ☐", 0, 0)
    pdf.cell(15, line_height, "T =", 0, 0)
    pdf.cell(20, line_height, data.get('treatment_temperature', '_____ °C'), 0, 1)

    pdf.cell(0, line_height, "Votre échantillon est stable jusqu’à la température : T = __________ °C", ln=True)
    pdf.ln(5)

    # ----- Analysis types and signature (two columns) -----
    start_y = pdf.get_y()

    # Left column: analysis checkboxes
    pdf.set_font("Arial", 'B', 10)
    pdf.cell(0, line_height, "Types d’analyses demandées :", ln=True)
    pdf.set_font("Arial", size=9)

    analysis_list = ["S BET", "Porosité", "t-plot", "BJH-des", "Isothermes"]
    selected = data.get('analysis_types', [])

    for analysis in analysis_list:
        checked = "☒" if analysis in selected else "☐"
        pdf.cell(40, line_height, f"{checked} {analysis}", 0, 1)

    # Right column: signature block
    pdf.set_xy(120, start_y)  # move to right side
    pdf.set_font("Arial", 'B', 9)
    pdf.multi_cell(70, line_height, "Signature & cachet de l’Encadrant / du Directeur du Laboratoire (Obligatoire) :")
    pdf.set_xy(120, pdf.get_y())
    pdf.cell(70, line_height, "......................................", ln=True)

    # Move below both columns
    pdf.set_y(max(pdf.get_y(), start_y + len(analysis_list)*line_height + 10))

    # ----- Avis du responsable -----
    pdf.ln(5)
    pdf.set_font("Arial", size=10)
    pdf.cell(0, line_height, "Avis du responsable des équipements : L. BEN HAMMOUDA", ln=True)
    pdf.ln(5)

    # ----- Date and reference -----
    pdf.cell(30, line_height, "Date de la demande :", 0, 0)
    pdf.cell(50, line_height, data.get('date_demande', datetime.now().strftime("%d/%m/%Y")), 0, 0)
    pdf.cell(40, line_height, "Références de la Demande :", 0, 0)
    pdf.cell(0, line_height, data.get('request_id', 'MSSP_2025'), 0, 1)

    return pdf.output(dest='S').encode('latin1')

# ---------- Email Functions ----------
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
