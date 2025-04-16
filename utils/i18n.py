# i18n.py
from locales import pt, en, es

languages = {
    "pt": pt.texts,
    "en": en.texts,
    "es": es.texts
}

def get_texts(locale_code):
    lang_code = locale_code.split("-")[0]  # pega só "pt" de "pt-BR"
    return languages.get(lang_code, en.texts)  # fallback: inglês