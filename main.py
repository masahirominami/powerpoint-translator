# main.py

import os
from pptx_handler import translate_text_in_place

def is_valid_pptx(path):
    return os.path.isfile(path) and path.lower().endswith('.pptx')

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

    # Run translation
    # generate_translated_pptx(input_path, output_path, target_lang)
    translate_text_in_place(input_path, output_path, target_lang)
if __name__ == "__main__":
    main()

