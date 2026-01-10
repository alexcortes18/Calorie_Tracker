from PyQt6.QtWidgets import (QWidget, QHBoxLayout, QLabel, QLineEdit
    
)
class TopBar(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        
        top_bar = QHBoxLayout()
        top_bar.addWidget(QLabel("Date:"))
        self.date_entry = QLineEdit()
        top_bar.addWidget(self.date_entry)

        top_bar.addStretch()

        top_bar.addWidget(QLabel("Weight (kg):"))
        self.weight_entry = QLineEdit()
        top_bar.addWidget(self.weight_entry) 