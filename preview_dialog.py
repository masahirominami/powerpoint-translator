from PyQt5.QtWidgets import QDialog, QVBoxLayout, QTextEdit, QPushButton
from PyQt5.QtCore import Qt

class TextPreviewDialog(QDialog):
    def __init__(self, extracted_text, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Preview Extracted Text")
        self.setMinimumSize(600, 400)

        layout = QVBoxLayout()

        self.text_edit = QTextEdit()
        self.text_edit.setPlainText(extracted_text)
        layout.addWidget(self.text_edit)

        self.btn_ok = QPushButton("Ok")
        self.btn_ok.clicked.connect(self.accept)
        layout.addWidget(self.btn_ok)

        self.setLayout(layout)

    def get_modified_text(self):
        return self.text_edit.toPlainText()

