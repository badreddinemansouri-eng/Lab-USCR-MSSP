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
import os
# Chemin absolu du dossier contenant utils.py
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# ---------- Nettoyage du texte ----------
def clean_text(text):
    if text is None:
        return ""
    replacements = {
        "\u2019": "'", "\u2018": "'", "\u201c": '"', "\u201d": '"',
        "\u2013": "-", "\u2014": "--", "\u00e9": "e", "\u00e8": "e",
        "\u00ea": "e", "\u00e2": "a", "\u00f4": "o", "\u00ee": "i",
        "\u00fb": "u", "\u00e0": "a", "\u00e7": "c",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text

def format_date(date_str):
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

# ---------- PDF Generation (version avec décalage pour directeur et labo) ----------
def generate_pdf(data: dict) -> bytes:
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=10)

    # ----- Trois logos (placeholders) -----
            
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    
    noms_fichiers = ["logo-gauche.jpg", "logo-centre.png", "logo-droit.png"]
    positions = [(10, 8, 30), (90, 8, 30), (170, 8, 30)]
    
    for i, nom in enumerate(noms_fichiers):
        chemin = os.path.join(BASE_DIR, "Logo", nom)   # attention au L majuscule
        if os.path.exists(chemin):
            pdf.image(chemin, x=positions[i][0], y=positions[i][1], w=positions[i][2])
        else:
            # Fallback rectangle gris
            pdf.set_fill_color(200, 200, 200)
            pdf.rect(positions[i][0], positions[i][1], positions[i][2], 30, 'F')
            pdf.set_xy(positions[i][0], positions[i][1] + 7)
            pdf.set_font("Arial", 'B', 8)
            pdf.cell(positions[i][2], 6, "Logo", align='C', border=0)
            pdf.set_font("Arial", size=10)
    # ----- Titre -----
    pdf.set_y(40)
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(0, 10, txt=clean_text("Demande d'une mesure de la surface specifique et de la porosite"), ln=True, align='C')
    pdf.ln(5)

    # ----- Informations chercheur (marges normales A4) -----
    pdf.set_font("Arial", size=10)
    line_height = 6
    left_margin = 10
    label_width = 55
    value_width = 135
    value_x = left_margin + label_width + 2

    def write_multiline(label, value):
        pdf.set_x(left_margin)
        pdf.set_font("Arial", 'B', 10)          # label en gras
        pdf.cell(label_width, line_height, clean_text(label + " : "), 0, 0)
        pdf.set_font("Arial", '', 10)            # valeur en normal
        pdf.set_x(value_x)
        pdf.multi_cell(value_width, line_height, clean_text(value), 0, 'L')

    # Ligne 1 : Nom + Tél
    pdf.set_x(left_margin)
    pdf.set_font("Arial", 'B', 10)
    pdf.cell(label_width, line_height, clean_text("Nom et prénom du demandeur : "), 0, 0)
    pdf.set_font("Arial", '', 10)
    pdf.set_x(value_x)
    pdf.cell(value_width - 50, line_height, clean_text(data.get('researcher_name', '__________________')), 0, 0)
    pdf.set_font("Arial", 'B', 10)
    pdf.cell(20, line_height, clean_text("Tél : "), 0, 0)
    pdf.set_font("Arial", '', 10)
    pdf.cell(30, line_height, clean_text(data.get('researcher_phone', '__________________')), 0, 1)

    # Ligne 2 : Email + Qualité
    pdf.set_x(left_margin)
    pdf.set_font("Arial", 'B', 10)
    pdf.cell(label_width, line_height, clean_text("Email : "), 0, 0)
    pdf.set_font("Arial", '', 10)
    pdf.set_x(value_x)
    pdf.cell(value_width - 50, line_height, clean_text(data.get('researcher_email', '__________________')), 0, 0)
    pdf.set_font("Arial", 'B', 10)
    pdf.cell(20, line_height, clean_text("Qualité : "), 0, 0)
    pdf.set_font("Arial", '', 10)
    pdf.cell(30, line_height, clean_text(data.get('qualification', '__________________')), 0, 1)

    # Champs longs (avec labels en gras grâce à write_multiline)
    write_multiline("Organisme", data.get('organisation', '__________________'))
    write_multiline("Diplôme en cours", data.get('diploma', '__________________'))
    write_multiline("Nom et prénom de l'encadrant", data.get('supervisor_name', '__________________'))

    # ----- Champ Directeur (décalé de +15, label en gras) -----
    pdf.set_x(left_margin)
    pdf.set_font("Arial", 'B', 10)
    pdf.cell(label_width, line_height, clean_text("Nom et prénom du Directeur de laboratoire : "), 0, 0)
    pdf.set_font("Arial", '', 10)
    pdf.set_x(value_x + 19)
    pdf.multi_cell(value_width - 19, line_height, clean_text(data.get('director_name', '__________________')), 0, 'L')

    # ----- Champ Laboratoire (décalé de +15, label en gras) -----
    pdf.set_x(left_margin)
    pdf.set_font("Arial", 'B', 10)   # gras mais police réduite pour le label long
    pdf.cell(label_width, line_height, clean_text("Laboratoire/Unité de Recherche/Service (Nom & Code) : "), 0, 0)
    pdf.set_font("Arial", '', 10)    # retour à normal pour la valeur
    pdf.set_x(value_x + 37)
    pdf.multi_cell(value_width - 37, line_height, clean_text(data.get('lab_unit', '__________________')), 0, 'L')

    pdf.ln(3)

    # ----- Tableau des échantillons centré -----
    table_width = 40 + 60 + 40  # 140 mm
    table_x = (210 - table_width) / 2  # centré sur page A4

    pdf.set_x(table_x)
    pdf.set_font("Arial", 'B', 10)
    pdf.cell(table_width, line_height, clean_text("Nombre d'échantillons (max 4)"), ln=True, align='C')
    pdf.set_font("Arial", size=10)

    # En-têtes
    pdf.set_x(table_x)
    pdf.cell(40, line_height, clean_text("Nom (max 8 car.)"), 1, 0, 'C')
    pdf.cell(60, line_height, clean_text("Nature de l'échantillon"), 1, 0, 'C')
    pdf.cell(40, line_height, clean_text("Traitement (°C)"), 1, 1, 'C')

    samples = data.get('samples', [])
    for i in range(4):
        sample = samples[i] if i < len(samples) else {}
        pdf.set_x(table_x)
        pdf.cell(40, line_height, clean_text(sample.get('name', '')[:8]), 1)
        pdf.cell(60, line_height, clean_text(sample.get('nature', '')), 1)
        pdf.cell(40, line_height, clean_text(sample.get('temp', '')), 1, 1)

    pdf.ln(5)

    # ----- Traitement de l'échantillon -----
    pdf.set_font("Arial", 'B', 10)
    pdf.cell(0, line_height, clean_text("Traitement de l'échantillon :"), ln=True)
    pdf.set_font("Arial", size=10)
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
    pdf.set_font("Arial", size=10)

    analysis_list = ["S BET", "Porosité", "t-plot", "BJH-des", "Isothermes"]
    selected = data.get('analysis_types', [])

    for analysis in analysis_list:
        checked = "[X]" if analysis in selected else "[ ]"
        pdf.cell(50, line_height, clean_text(f"{checked} {analysis}"), 0, 1)

    # Colonne droite : signature
    pdf.set_xy(120, start_y)
    pdf.set_font("Arial", 'B', 10)
    pdf.multi_cell(75, line_height, clean_text("Signature & cachet de l'Encadrant / du Directeur du Laboratoire (Obligatoire) :"))
    pdf.set_xy(120, pdf.get_y())
    pdf.cell(75, line_height, clean_text("......................................"), ln=True)

    # Ajustement vertical
    pdf.set_y(max(pdf.get_y(), start_y + len(analysis_list)*line_height + 10))

    # ----- Avis du responsable (aligné à gauche) -----
    # ----- Avis du responsable (aligné à gauche) -----
    pdf.set_x(left_margin)
    pdf.ln(5)
    pdf.set_font("Arial", size=10)
    pdf.cell(0, line_height, clean_text("Avis du responsable des équipements : L. BEN HAMMOUDA"), ln=True)
    pdf.set_x(left_margin)
    pdf.cell(0, line_height, clean_text("........................................"), ln=True)
    pdf.ln(5)
    
    # ----- Date et référence (en gras) -----
    pdf.set_font("Arial", 'B', 10)   # passage en gras
    date_str = format_date(data.get('date_demande'))
    pdf.cell(35, line_height, clean_text("Date de la demande :"), 0, 0)
    pdf.cell(50, line_height, clean_text(" " + date_str), 0, 0)
    pdf.cell(45, line_height, clean_text("Références de la Demande :"), 0, 0)
    pdf.cell(0, line_height, clean_text(" " + data.get('request_id', 'MSSP_2025')), 0, 1)
    pdf.set_font("Arial", size=10)   # retour à la police normale
    pdf.ln(3)   # espace avant les remarques
    
    # ----- Remarques en bas -----
    pdf.set_font("Arial", size=8)
    remarques = [
        "*Masse de l'échantillon entre 120 et 150 mg.",
        "*formulaire doit être dument rempli et signé.",
        "*Veuillez récupérer vos échantillons, sinon ils seront jetés après une semaine."
    ]
    for ligne in remarques:
        pdf.cell(0, line_height, clean_text(ligne), ln=True)
    pdf.ln(3)
    return pdf.output(dest='S')
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
# ---------- Gestion des actualités ----------
def get_all_news():
    supabase = init_supabase()
    response = supabase.table("news").select("*").order("created_at", desc=True).execute()
    return response.data

def add_news(title, content, image_url=""):
    supabase = init_supabase()
    data = {
        "title": title,
        "content": content,
        "image_url": image_url
    }
    response = supabase.table("news").insert(data).execute()
    return response.data

def update_news(news_id, title, content, image_url):
    supabase = init_supabase()
    data = {
        "title": title,
        "content": content,
        "image_url": image_url,
        "updated_at": datetime.now().isoformat()
    }
    response = supabase.table("news").update(data).eq("id", news_id).execute()
    return response.data

def delete_news(news_id):
    supabase = init_supabase()
    response = supabase.table("news").delete().eq("id", news_id).execute()
    return response.data        
