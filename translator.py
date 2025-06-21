from deep_translator import GoogleTranslator

def translate_text(text, target_lang):
    if not text.strip():
        return text
    try:
        return GoogleTranslator(source='auto', target=target_lang).translate(text)
    except Exception as e:
        print(f"[⚠️] Translation error: {e}")
        return "[translation failed]"

