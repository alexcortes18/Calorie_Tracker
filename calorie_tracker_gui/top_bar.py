from PyQt6.QtWidgets import (QWidget, QHBoxLayout, QLabel, QLineEdit, QDateEdit, 
                             QTableWidgetItem, QMessageBox)
from PyQt6.QtCore import QDate

from SQL.db_connection import get_connection
from SQL.db_operations import get_weight_entry

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
    
    def load_weights_from_db (self, selected_date):
        row = get_weight_entry(selected_date)
        if row:
            print(selected_date)
            print(str(row[0]))
            self.weight_entry.setText(str(row[0])) # information comes as a tuple, hence (,)
        else:
            self.weight_entry.clear()