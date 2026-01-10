from PyQt6.QtWidgets import (
    QGroupBox, QVBoxLayout, QHBoxLayout,
    QTableWidget, QPushButton, QTableWidgetItem, QMessageBox
)

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
            if header in ("Exercise", "Duration"):
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
