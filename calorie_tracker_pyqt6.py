import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit,
    QTableWidget, QTableWidgetItem, QPushButton, QTextEdit, QGroupBox
)

class CalorieTracker(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calorie Tracker PyQT6")
        self.resize(1200, 750)

        main_layout = QVBoxLayout(self)

        # ===== Top Bar =====
        top_bar = QHBoxLayout()
        top_bar.addWidget(QLabel("Date:"))
        self.date_entry = QLineEdit("2026-01-09")
        top_bar.addWidget(self.date_entry)

        top_bar.addStretch()

        top_bar.addWidget(QLabel("Weight (kg):"))
        self.weight_entry = QLineEdit("73.6")
        top_bar.addWidget(self.weight_entry)
        main_layout.addLayout(top_bar)

        # ===== Food Log =====
        food_group = QGroupBox("Food Log")
        food_layout = QVBoxLayout()
        self.food_table = QTableWidget(2, 6)
        self.food_table.setHorizontalHeaderLabels(
            ["Meal", "Item", "Calories", "Protein", "Fat", "Carbs"]
        )
        self.food_table.setItem(0, 0, QTableWidgetItem("Breakfast"))
        self.food_table.setItem(0, 1, QTableWidgetItem("French toast + honey (90g)"))
        self.food_table.setItem(0, 2, QTableWidgetItem("238"))
        self.food_table.setItem(0, 3, QTableWidgetItem("9"))
        self.food_table.setItem(0, 4, QTableWidgetItem("8"))
        self.food_table.setItem(0, 5, QTableWidgetItem("34"))

        self.food_table.setItem(1, 0, QTableWidgetItem("Lunch"))
        self.food_table.setItem(1, 1, QTableWidgetItem("Beans, beef, plantain, salad, cuajada, juice"))
        self.food_table.setItem(1, 2, QTableWidgetItem("1093"))
        self.food_table.setItem(1, 3, QTableWidgetItem("56"))
        self.food_table.setItem(1, 4, QTableWidgetItem("46"))
        self.food_table.setItem(1, 5, QTableWidgetItem("111"))

        food_layout.addWidget(self.food_table)

        food_buttons = QHBoxLayout()
        food_buttons.addWidget(QPushButton("Delete Entry"))
        food_buttons.addWidget(QPushButton("Add Food"))
        food_layout.addLayout(food_buttons)

        food_group.setLayout(food_layout)
        main_layout.addWidget(food_group)

        # ===== Exercise Log =====
        exercise_group = QGroupBox("Exercise Log")
        exercise_layout = QVBoxLayout()
        self.exercise_table = QTableWidget(1, 3)
        self.exercise_table.setHorizontalHeaderLabels(
            ["Exercise", "Duration", "Calories Burned"]
        )
        self.exercise_table.setItem(0, 0, QTableWidgetItem("Running"))
        self.exercise_table.setItem(0, 1, QTableWidgetItem("30 min"))
        self.exercise_table.setItem(0, 2, QTableWidgetItem("300"))

        exercise_layout.addWidget(self.exercise_table)

        exercise_buttons = QHBoxLayout()
        exercise_buttons.addWidget(QPushButton("Delete Entry"))
        exercise_buttons.addWidget(QPushButton("Add Exercise"))
        exercise_layout.addLayout(exercise_buttons)

        exercise_group.setLayout(exercise_layout)
        main_layout.addWidget(exercise_group)

        # ===== Daily Summary =====
        summary_group = QGroupBox("Daily Summary")
        summary_layout = QHBoxLayout()
        summary_items = [
            ("Calories Consumed", "1331"),
            ("Protein (g)", "65"),
            ("Fat (g)", "54"),
            ("Carbs (g)", "145"),
            ("Exercise (kCal)", "300"),
            ("Net Calories", str(1331 - 300)),
        ]
        for label, value in summary_items:
            block = QVBoxLayout()
            block.addWidget(QLabel(label))
            block.addWidget(QLabel(value))
            summary_layout.addLayout(block)
        summary_group.setLayout(summary_layout)
        main_layout.addWidget(summary_group)

        # ===== Notes =====
        notes_group = QGroupBox("Notes")
        notes_layout = QVBoxLayout()
        self.notes_text = QTextEdit("Feeling good today. Logged meals and exercise.")
        notes_layout.addWidget(self.notes_text)
        notes_group.setLayout(notes_layout)
        main_layout.addWidget(notes_group)

        # ===== Update Button =====
        update_button = QPushButton("Update")
        main_layout.addWidget(update_button)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CalorieTracker()
    window.show()
    sys.exit(app.exec())
