import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit,
    QTableWidget, QPushButton, QTextEdit, QGroupBox, QTableWidgetItem, QMessageBox
)
from calorie_tracker_gui.food_log import FoodLog
from calorie_tracker_gui.top_bar import TopBar
from calorie_tracker_gui.exercise_log import ExerciseLog

class CalorieTracker(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calorie Tracker PyQT6")
        self.resize(900, 750)
        self.setStyleSheet("background-color: lightgray;") # lightblue, beige

        main_layout = QVBoxLayout(self)

        # ========================= Top Bar =========================
        self.top_bar = TopBar()
        main_layout.addWidget(self.top_bar)

        # ========================= Food Log =========================
        self.food_log = FoodLog() 
        main_layout.addWidget(self.food_log, stretch= 10)
        
        # Change the values from calories when you click on a different date
        self.top_bar.date_entry.dateChanged.connect(self.food_log.load_foods_from_db)

        # ========================= Exercise Log =========================

        self.exercise_log = ExerciseLog()
        main_layout.addWidget(self.exercise_log)

        # ========================= Daily Summary =========================
        summary_group = QGroupBox("Daily Summary")
        summary_layout = QHBoxLayout()
        self.summary_labels = {}
        
        summary_items = [
            "Calories Consumed",
            "Protein (g)",
            "Fat (g)",
            "Carbs (g)",
            "Exercise (kCal)",
            "Net Calories",
        ]
        for label in summary_items:
            block = QVBoxLayout()
            block.addWidget(QLabel(label))  # Label
            value_label = QLabel("0")       
            block.addWidget(value_label)    # Initial value 0
            summary_layout.addLayout(block)
            self.summary_labels[label] = value_label
        summary_group.setLayout(summary_layout)
        main_layout.addWidget(summary_group)

        # ========================= Notes =========================
        notes_group = QGroupBox("Notes")
        notes_layout = QVBoxLayout()
        self.notes_text = QTextEdit()
        notes_layout.addWidget(self.notes_text)
        notes_group.setLayout(notes_layout)
        main_layout.addWidget(notes_group)

        # ========================= Update Button =========================
        update_button = QPushButton("Update")
        update_button.clicked.connect(self.update_summary)
        main_layout.addWidget(update_button)

    def update_summary(self):
        # --- Food totals ---
        calories = protein = fat = carbs = 0
        for row in range(self.food_log.table.rowCount()):
            calories += float(self.food_log.table.item(row, 2).text())
            protein  += float(self.food_log.table.item(row, 3).text())
            fat      += float(self.food_log.table.item(row, 4).text())
            carbs    += float(self.food_log.table.item(row, 5).text())

        # --- Exercise totals ---
        exercise = 0
        for row in range(self.exercise_log.table.rowCount()):
            exercise += float(self.exercise_log.table.item(row, 2).text())

        # --- Net calories ---
        net = calories - exercise

        # --- Update labels ---
        # In here we lookup the dictionary entries and apply (setText) a different value onto each "value_label"
        self.summary_labels["Calories Consumed"].setText(str(calories)) 
        self.summary_labels["Protein (g)"].setText(str(protein))
        self.summary_labels["Fat (g)"].setText(str(fat))
        self.summary_labels["Carbs (g)"].setText(str(carbs))
        self.summary_labels["Exercise (kCal)"].setText(str(exercise))
        self.summary_labels["Net Calories"].setText(str(net))

            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CalorieTracker()
    window.show()
    sys.exit(app.exec())

