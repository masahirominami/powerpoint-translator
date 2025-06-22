from deep_translator import GoogleTranslator
from scan_forbidden_chars import scan_forbidden_chars

def translate_text(text, target_lang, forbidden_keywords):

    # After extracting preview text:
    if scan_forbidden_chars(forbidden_keywords, text):
        print(f"Translation was not executed. This document contains protected keywords and cannot be translated. [{text}]")
        return text

    if not text.strip():
        return text
    try:
        return GoogleTranslator(source='auto', target=target_lang).translate(text)
    except Exception as e:
        print(f"[⚠️] Translation error: {e}")
        return "[translation failed]"

