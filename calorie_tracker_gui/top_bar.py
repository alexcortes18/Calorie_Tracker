from PyQt6.QtWidgets import (QWidget, QHBoxLayout, QLabel, QLineEdit, QDateEdit)
from PyQt6.QtCore import QDate

class TopBar(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QHBoxLayout()

        self.date_entry = QDateEdit()
        self.date_entry.setCalendarPopup(True)
        self.date_entry.setDate(QDate.currentDate())
        layout.addWidget(QLabel("Date:"))
        layout.addWidget(self.date_entry)

        layout.addStretch()

        self.weight_entry = QLineEdit()
        layout.addWidget(QLabel("Weight (kg):"))
        layout.addWidget(self.weight_entry)

        self.setLayout(layout)

    def get_weight(self):
        return self.weight_entry.text()

    def get_date(self):
        return self.date_entry.date().toString("yyyy-MM-dd")
