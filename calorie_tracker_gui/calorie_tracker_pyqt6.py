import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit,
    QTableWidget, QPushButton, QTextEdit, QGroupBox, QTableWidgetItem, QMessageBox
)
from calorie_tracker_gui.food_log import FoodLog
from calorie_tracker_gui.top_bar import TopBar
from calorie_tracker_gui.exercise_log import ExerciseLog
from SQL.db_operations import save_food_entries, save_exercise_entries, save_daily_summary

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
        
        # Change the values for exercise data when you click on a different date
        self.top_bar.date_entry.dateChanged.connect(self.exercise_log.load_exercises_from_db)

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
        food_entries = []
        for row in range(self.food_log.table.rowCount()):
            meal_type = self.food_log.table.item(row, 0).text()
            food_item = self.food_log.table.item(row, 1).text()
            cal = float(self.food_log.table.item(row, 2).text())
            prot = float(self.food_log.table.item(row, 3).text())
            f = float(self.food_log.table.item(row, 4).text())
            c = float(self.food_log.table.item(row, 5).text())
            food_entries.append([meal_type, food_item, cal, prot, f, c])
            calories += cal
            protein  += prot
            fat      += f
            carbs    += c

        # --- Exercise totals ---
        exercise = 0
        exercise_entries = []
        for row in range(self.exercise_log.table.rowCount()):
            exercise_name = self.exercise_log.table.item(row, 0).text()
            duration = float(self.exercise_log.table.item(row, 1).text())
            burned = float(self.exercise_log.table.item(row, 2).text())
            exercise_entries.append([exercise_name, duration, burned])
            exercise += burned

        # --- Net calories ---
        net = calories - exercise

        # --- Update labels ---
        self.summary_labels["Calories Consumed"].setText(str(calories)) 
        self.summary_labels["Protein (g)"].setText(str(protein))
        self.summary_labels["Fat (g)"].setText(str(fat))
        self.summary_labels["Carbs (g)"].setText(str(carbs))
        self.summary_labels["Exercise (kCal)"].setText(str(exercise))
        self.summary_labels["Net Calories"].setText(str(net))

        # --- Save to DB ---
        selected_date = self.top_bar.get_date()
        weight = float(self.top_bar.get_weight() or 0)
        notes = self.notes_text.toPlainText()

        save_food_entries(food_entries, selected_date)
        save_exercise_entries(exercise_entries, selected_date)
        save_daily_summary(selected_date, weight, calories, notes)



            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CalorieTracker()
    window.show()
    sys.exit(app.exec())

