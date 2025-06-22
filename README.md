# 🧭 PowerPoint Translator App

This cross-platform desktop application allows users to **translate the text inside PowerPoint `.pptx` files** into any target language — without altering slide layouts, images, or formatting. It uses a simple **PyQt5 GUI** to streamline the process and supports in-place translation to preserve visual fidelity.

**Most of this program was done by Microsoft Copilot.**

---

## ⚙️ Technical Requirements

- Python **3.7+**
- [python-pptx](https://python-pptx.readthedocs.io/)
- [deep-translator](https://github.com/nidhaloff/deep-translator)
- PyQt5

Install dependencies:

```bash
pip install -r requirements.txt
```

Or individually:

```bash
pip install python-pptx deep-translator PyQt5
```

## 📁 Project Structure

| File / Folder            | Description                                           |
|--------------------------|-------------------------------------------------------|
| config_loader.py         | Loads forbidden keywords from the config file         |
| config.yaml.sample       | Sample config                                         |
| gui.py                   | PyQt-based GUI logic, entry point for GUI             |
| instructions.md          | Copilot output for creating this project              |
| main.py                  | Entry point for CLI-based translation execution       |
| pptx_handler.py          | Handles PowerPoint generation and layout logic        |
| preview_dialog.py        | Displays extracted text for preview/edit              |
| scan_forbidden_chars.py  | Scans for forbidden terms before translation          |
| translator.py            | Wraps the translation logic using deep-translator     |
| requirements.txt         | Lists required Python packages with pinned versions   |
| .gitignore               | Excludes virtual envs, caches, and OS-generated files |
| README.md                | This file: overview, usage instructions               |


## 🚀 Usage`

### Prerequisites:
Prepare config.yaml of your project, where you define forbidden keywords and translation settings.

### Option 1: Using the GUI (recommended)

1. Run the application:
   ```bash
   python gui.py
   ```
2. Select the PowerPoint file you want to translate.
3. Choose the target language from the dropdown menu.
4. Click the "Translate" button.

### Option 2: Using the CLI

1. Run the application:
```bash
python main.py
```

2. You'll be prompted to enter:

   The input file path
   The output file path
   A target language code

3. The application will process the file and save the translated version.


