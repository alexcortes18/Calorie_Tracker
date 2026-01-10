# calorie_tracker_gui/food_log.py
from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem,
    QPushButton, QHBoxLayout, QMessageBox
)
from SQL.db_connection import get_connection

class FoodLog(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        layout = QVBoxLayout()

        # Table setup
        self.table = QTableWidget(0, 6)  # start with 0 rows, 6 columns
        self.table.setMinimumHeight(300)
        self.table.setHorizontalHeaderLabels([
            "Food", "Item", "Calories", "Protein (g)", "Fat (g)", "Carbs (g)"
        ])
        self.table.setColumnWidth(1, 300)
        layout.addWidget(self.table)

        # Buttons (Delete first, then Add)
        btns = QHBoxLayout()
        delete_btn = QPushButton("Delete Entry")
        add_btn = QPushButton("Add Food")
        delete_btn.clicked.connect(self.delete_food)
        add_btn.clicked.connect(self.add_food)
        btns.addWidget(delete_btn)
        btns.addWidget(add_btn)

        layout.addLayout(btns)
        self.setLayout(layout)

    def add_food(self):
        row = self.table.rowCount()
        self.table.insertRow(row)
        for col in range(self.table.columnCount()):
            header = self.table.horizontalHeaderItem(col).text()
            if header in ("Food", "Item"):
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

    def load_from_db(self):
        selected_date = None
        if self.parent() and hasattr(self.parent(), "top_bar"):
            selected_date = self.parent().top_bar.get_date()

        conn = None
        cursor = None
        try:
            conn = get_connection()
            cursor = conn.cursor()

            if selected_date:
                cursor.execute(
                    "SELECT meal_type, food_item, calories, protein, fat, carbs "
                    "FROM food_log WHERE date = %s",
                    (selected_date,)
                )
            else:
                cursor.execute(
                    "SELECT meal_type, food_item, calories, protein, fat, carbs FROM food_log"
                )

            rows = cursor.fetchall()
            self.table.setRowCount(0)

            for row_data in rows:
                row = self.table.rowCount()
                self.table.insertRow(row)
                for col, value in enumerate(row_data):
                    self.table.setItem(row, col, QTableWidgetItem(str(value)))

        except Exception as e:
            QMessageBox.critical(self, "Database Error", str(e))
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()
