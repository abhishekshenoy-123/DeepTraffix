import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton,
    QFileDialog, QVBoxLayout, QFrame
)
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import Qt


class FileUploader(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("📤 File Uploader")
        self.setGeometry(100, 100, 600, 400)
        self.init_ui()

    def init_ui(self):
        # Main window styling
        self.setStyleSheet("background-color: #f5f8fb;")

        # === Upload Card ===
        card = QFrame(self)
        card.setFrameShape(QFrame.StyledPanel)
        card.setStyleSheet("""
            QFrame {
                background-color: #ffffff;
                border: 2px dashed #a0c4ff;
                border-radius: 16px;
                padding: 30px;
                max-width: 420px;
            }
            QFrame:hover {
                border: 2px solid #4a90e2;
            }
        """)

        # Title Label
        title = QLabel("Drop your file here or click below")
        title.setFont(QFont("Segoe UI", 12, QFont.Bold))
        title.setStyleSheet("color: #333; margin-bottom: 10px;")
        title.setAlignment(Qt.AlignCenter)

        # File path label
        self.label = QLabel("No file selected")
        self.label.setFont(QFont("Segoe UI", 10))
        self.label.setStyleSheet("color: #777; padding: 10px;")
        self.label.setWordWrap(True)
        self.label.setAlignment(Qt.AlignCenter)

        # Upload button
        self.button = QPushButton("📁 Browse File")
        self.button.setCursor(Qt.PointingHandCursor)
        self.button.setStyleSheet("""
            QPushButton {
                background-color: #4a90e2;
                color: white;
                padding: 10px 20px;
                border-radius: 10px;
                font-size: 14px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #357ab8;
            }
            QPushButton:pressed {
                background-color: #2e6da4;
            }
        """)
        self.button.clicked.connect(self.browse_file)

        # Card layout
        card_layout = QVBoxLayout(card)
        card_layout.addWidget(title)
        card_layout.addWidget(self.label)
        card_layout.addWidget(self.button, alignment=Qt.AlignCenter)

        # Main layout
        main_layout = QVBoxLayout(self)
        main_layout.addStretch()
        main_layout.addWidget(card, alignment=Qt.AlignCenter)
        main_layout.addStretch()
        self.setLayout(main_layout)

    def browse_file(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Select File")
        if file_name:
            self.label.setText(f"✅ File selected:\n{file_name}")
        else:
            self.label.setText("❌ No file selected")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = FileUploader()
    window.show()
    sys.exit(app.exec_())
