# utils_i18n.py
TRANSLATIONS = {
    "fr": {
        "nav_home": "🏠 Accueil",
        "nav_analyses": "🔬 Analyses",
        "nav_request": "📝 Demande",
        "nav_resources": "📚 Ressources",
        "nav_contact": "📞 Contact",
        "nav_admin": "🔐 Admin",
        "welcome": "Bienvenue",
        "theme_light": "☀️ Clair",
        "theme_dark": "🌙 Sombre",
        "language": "Langue",
        "our_team": "Notre équipe",
        "contact_us": "Contactez-nous",
        "make_request": "Faire une demande",
        "back_to_analyses": "← Retour aux analyses",
    },
    "en": {
        "nav_home": "🏠 Home",
        "nav_analyses": "🔬 Analyses",
        "nav_request": "📝 Request",
        "nav_resources": "📚 Resources",
        "nav_contact": "📞 Contact",
        "nav_admin": "🔐 Admin",
        "welcome": "Welcome",
        "theme_light": "☀️ Light",
        "theme_dark": "🌙 Dark",
        "language": "Language",
        "our_team": "Our Team",
        "contact_us": "Contact Us",
        "make_request": "Make a request",
        "back_to_analyses": "← Back to analyses",
    }
}

def get_text(key, lang="fr"):
    return TRANSLATIONS.get(lang, TRANSLATIONS["fr"]).get(key, key)
