from PyQt6.QtWidgets import (
    QGroupBox, QVBoxLayout, QHBoxLayout,
    QTableWidget, QPushButton, QTableWidgetItem, QMessageBox
)

class FoodLog(QGroupBox):
    def __init__(self, parent=None):
        super().__init__("Food Log", parent)
        
        self.setMinimumHeight(300)
        food_layout = QVBoxLayout()

        # table
        self.table = QTableWidget(0, 6)
        self.table.setHorizontalHeaderLabels(
            ["Meal", "Item(s)", "Calories", "Protein", "Fat", "Carbs"]
        )
        food_layout.addWidget(self.table)

        # buttons
        btns = QHBoxLayout()
        delete_btn = QPushButton("Delete Entry")
        add_btn = QPushButton("Add Food")
        delete_btn.clicked.connect(self.delete_food)
        add_btn.clicked.connect(self.add_food)
        btns.addWidget(delete_btn)
        btns.addWidget(add_btn)

        food_layout.addLayout(btns)
        self.setLayout(food_layout)

    def add_food(self):
        row = self.table.rowCount()
        self.table.insertRow(row)
        for col in range(self.table.columnCount()):
            header = self.table.horizontalHeaderItem(col).text()
            if header in ("Meal", "Item(s)"):
                self.table.setItem(row, col, QTableWidgetItem("-"))
            else:
                self.table.setItem(row, col, QTableWidgetItem("0"))

    def delete_food(self):
        row = self.table.currentRow()
        if row >= 0:
            self.table.removeRow(row)
        else:
            msg = QMessageBox()
            msg.setWindowTitle("No Selection")
            msg.setText("Please select a row to delete.")
            msg.setIcon(QMessageBox.Icon.Warning)
            msg.exec()
