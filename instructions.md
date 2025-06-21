# 📝 PowerPoint Translator: Project Overview

A standalone Python application to:
- Read `.pptx` files
- Translate all slide content into a user-selected language
- Generate a new `.pptx` where each translated slide follows the original

---

## 🧰 Requirements

- Python 3.9+
- `python-pptx`: Read and write PowerPoint files
- Translation API:
  - Option 1: `deep-translator` (Google Translate or LibreTranslate support)
  - Option 2: Official Microsoft Translator or Google Translate APIs
- (Optional) CLI library for input arguments, e.g. `argparse`

---

## 🗺️ Project Structure

ppt-translator/ ├── main.py # Entry point for the app ├── translator.py # Handles API interaction ├── pptx_handler.py # Reads and writes .pptx slides ├── config.py # API keys or settings └── requirements.txt # Python dependencies


---

## 🔄 Processing Flow

1. **User inputs:**
   - File path to `.pptx`
   - Target language (e.g., `ja`, `fr`, `es`)
2. **Parse `.pptx`:**
   - Loop through slides
   - Extract all text from shapes
3. **Translate text:**
   - Use selected translation method to convert content
4. **Generate output:**
   - Duplicate original slide layout
   - Insert translated text into new slide
5. **Save new file:**
   - Output file saved as `translated_{original_name}.pptx`

---

## 🚀 Next Steps

- [ ] Set up project environment
- [ ] Choose translation engine
- [ ] Write basic slide reader and duplicator
- [ ] Integrate translation
- [ ] Add CLI or UI if needed

---

✅ *Clean separation of logic will make it easy to test, maintain, and even extend later with GUI or web support.*


