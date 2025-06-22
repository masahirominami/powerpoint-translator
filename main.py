# main.py

import os
from pptx_handler import translate_text_in_place
from pptx_handler import extract_text_from_pptx
from config_loader import load_config  # Assuming you have a config_loader module

def is_valid_pptx(path):
    return os.path.isfile(path) and path.lower().endswith('.pptx')

def setup_forbidden_keywords():
    from config_loader import load_config

    # This method can be used to set up any forbidden keywords or characters
    # For now, we will just initialize an empty list
    # Load from config
    config = load_config()
    return set(word.lower() for word in config.get("forbidden_keywords", []))

def main():
    print("🎯 PowerPoint Translator")

    # Get input file
    input_path = input("Enter path to input .pptx file: ").strip()
    while not is_valid_pptx(input_path):
        input_path = input("⚠️ Invalid file. Please enter a valid .pptx path: ").strip()

    # Get output file name
    output_path = input("Enter path for translated output file: ").strip()
    if not output_path.lower().endswith('.pptx'):
        output_path += ".pptx"

    # Get language code
    target_lang = input("Enter target language code (e.g., ja, fr, es): ").strip().lower()
    if not target_lang:
        print("⚠️ No language code entered. Defaulting to 'en'.")
        target_lang = 'en'

    # Load forbidden keywords
    forbidden_keywords = setup_forbidden_keywords()

    try:
        extracted_text = extract_text_from_pptx(input_path)  # Just extract text without translation
        keywords_found = any(
            keyword.lower() in extracted_text.lower() for keyword in forbidden_keywords)
        if keywords_found:
            print("⚠️ Translation was not executed. This document contains protected keywords and cannot be translated. ")
            return

    except Exception as e:
        print(f"Failed to extract text:\n{e}")
        return

    # Run translation
    # generate_translated_pptx(input_path, output_path, target_lang)
    translate_text_in_place(input_path, output_path, target_lang,
                            forbidden_keywords)
if __name__ == "__main__":
    main()

