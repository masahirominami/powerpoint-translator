# gui.py

import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton,
    QVBoxLayout, QFileDialog, QMessageBox
)
from PyQt5.QtCore import Qt
from pptx_handler import translate_text_in_place
from pptx_handler import extract_text_from_pptx
from preview_dialog import TextPreviewDialog  # If you save it in a separate file

class TranslatorApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PowerPoint Translator")
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()

        self.input_label = QLabel("Select a .pptx file to translate:")
        self.input_path = QLineEdit()
        browse_btn = QPushButton("Browse")
        browse_btn.clicked.connect(self.browse_file)

        self.output_label = QLabel("Save translated file as:")
        self.output_path = QLineEdit()
        output_browse_btn = QPushButton("Browse")
        output_browse_btn.clicked.connect(self.browse_output_file)

        self.preview_label = QLabel("Preview extracted text:")
        preview_btn = QPushButton("Preview")
        preview_btn.clicked.connect(self.preview_text)

        self.lang_label = QLabel("Enter target language code (e.g. ja, fr, es):")
        self.lang_input = QLineEdit()

        translate_btn = QPushButton("Translate")
        translate_btn.setObjectName("Translate")  # For easy access later
        translate_btn.clicked.connect(self.translate)

        layout.addWidget(self.input_label)
        layout.addWidget(self.input_path)
        layout.addWidget(browse_btn)

        layout.addWidget(self.output_label)
        layout.addWidget(self.output_path)
        layout.addWidget(output_browse_btn)

        layout.addWidget(self.preview_label)
        layout.addWidget(preview_btn)

        layout.addWidget(self.lang_label)
        layout.addWidget(self.lang_input)
        layout.addWidget(translate_btn)

        self.setLayout(layout)

    def browse_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select PowerPoint File", "", "PowerPoint Files (*.pptx)")
        if file_path:
            self.input_path.setText(file_path)
            self.toggle_translate_button(False)  # Need to preview text before enabling translation 

    def browse_output_file(self):
        file_path, _ = QFileDialog.getSaveFileName(self, "Save Translated File As", "", "PowerPoint Files (*.pptx)")
        if file_path:
            if not file_path.lower().endswith(".pptx"):
                file_path += ".pptx"
            self.output_path.setText(file_path)
            self.toggle_translate_button(False)  # Need to preview text before enabling translation 

    def preview_text(self):
        input_file = self.input_path.text().strip()
        if not input_file:
            QMessageBox.warning(self, "Missing File", "Please select a PowerPoint file to preview.")
            return

        try:
            extracted_text = extract_text_from_pptx(input_file)  # Just extract text without translation
            dialog = TextPreviewDialog(extracted_text, self)
            dialog.exec_()
            self.toggle_translate_button(True)  # Enable translate button after

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to extract text:\n{e}")

    def translate(self):
        input_file = self.input_path.text().strip()
        output_file = self.output_path.text().strip()
        target_lang = self.lang_input.text().strip()

        if not input_file or not output_file or not target_lang:
            QMessageBox.warning(self, "Missing Info", "Please fill in all
                                fields and preview first.")
            return

        QApplication.setOverrideCursor(Qt.WaitCursor)  # 👈 Show busy cursor
        try:
            translate_text_in_place(input_file, output_file, target_lang)
            QMessageBox.information(self, "Success", f"Translation completed!\nSaved to:\n{output_file}")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Translation failed:\n{e}")
        finally:
            QApplication.restoreOverrideCursor() # 👈 Restore cursor
            self.toggle_translate_button(False)

    def toggle_translate_button(self, enabled):
        self.findChild(QPushButton, "Translate").setEnabled(enabled)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TranslatorApp()
    window.show()
    sys.exit(app.exec_())

