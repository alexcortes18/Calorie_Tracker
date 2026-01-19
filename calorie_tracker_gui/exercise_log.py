from PyQt6.QtWidgets import (
    QGroupBox, QVBoxLayout, QHBoxLayout,
    QTableWidget, QPushButton, QTableWidgetItem, QMessageBox
)
from SQL.db_connection import get_connection
from SQL.db_operations import get_exercises_entries

class ExerciseLog(QGroupBox):
    def __init__(self, parent=None):
        super().__init__("Exercise Log", parent)

        self.setMinimumHeight(200)
        layout = QVBoxLayout()

        # table
        self.table = QTableWidget(0, 3)
        self.table.setHorizontalHeaderLabels(
            ["Exercise", "Duration", "Calories Burned"]
        )
        layout.addWidget(self.table)

        # buttons
        btns = QHBoxLayout()
        delete_btn = QPushButton("Delete Entry")
        add_btn = QPushButton("Add Exercise")
        delete_btn.clicked.connect(self.delete_exercise)
        add_btn.clicked.connect(self.add_exercise)
        btns.addWidget(delete_btn)
        btns.addWidget(add_btn)

        layout.addLayout(btns)
        self.setLayout(layout)

    def add_exercise(self):
        row = self.table.rowCount()
        self.table.insertRow(row)
        for col in range(self.table.columnCount()):
            header = self.table.horizontalHeaderItem(col).text()
            if header in ("Exercise"):
                self.table.setItem(row, col, QTableWidgetItem("-"))
            else:
                self.table.setItem(row, col, QTableWidgetItem("0"))

    def delete_exercise(self):
        row = self.table.currentRow()
        if row >= 0:
            self.table.removeRow(row)
        else:
            msg = QMessageBox()
            msg.setWindowTitle("No Selection")
            msg.setText("Please select a row to delete.")
            msg.setIcon(QMessageBox.Icon.Warning)
            msg.exec()
            
    def load_exercises_from_db(self, selected_date):
        rows = get_exercises_entries(selected_date)
        self.table.setRowCount(0)

        for row_data in rows:
            row = self.table.rowCount()
            self.table.insertRow(row)
            for col, value in enumerate(row_data):
                self.table.setItem(row, col, QTableWidgetItem(str(value)))

