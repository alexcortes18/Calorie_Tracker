import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Calorie Tracker TK")
root.geometry("1200x750")

# ================= TOP BAR =================
top_frame = tk.Frame(root)
top_frame.pack(fill="x", padx=10, pady=10)

# Date (left)
tk.Label(top_frame, text="Date:").pack(side="left", padx=5)
date_entry = tk.Entry(top_frame, width=12)
date_entry.insert(0, "YYYY-MM-DD")
date_entry.pack(side="left")

# Spacer
tk.Frame(top_frame).pack(side="left", expand=True)

# Weight (right)
tk.Label(top_frame, text="Weight (kg):").pack(side="left", padx=5)
weight_entry = tk.Entry(top_frame, width=8)
weight_entry.pack(side="left")

# ================= MAIN AREA =================
main_frame = tk.Frame(root)
main_frame.pack(fill="both", expand=True, padx=10)

# ================= FOOD LOG =================
food_frame = tk.LabelFrame(main_frame, text="Food Log")
food_frame.pack(side="left", fill="both", expand=True, padx=5)

food_columns = ("Meal", "Item", "Calories", "Protein", "Fat", "Carbs")
food_table = ttk.Treeview(food_frame, columns=food_columns, show="headings", height=12)

for col in food_columns:
    food_table.heading(col, text=col)
    food_table.column(col, width=120 if col != "Item" else 300)

food_table.pack(fill="both", expand=True, padx=5, pady=5)

food_btns = tk.Frame(food_frame)
food_btns.pack(fill="x", pady=5)

tk.Button(food_btns, text="Delete Entry").pack(side="left", padx=5)
tk.Button(food_btns, text="Add Food", bg="#6dbf73").pack(side="left")

# ================= EXERCISE LOG =================
exercise_frame = tk.LabelFrame(main_frame, text="Exercise Log")
exercise_frame.pack(side="left", fill="both", expand=True, padx=5)

exercise_columns = ("Exercise", "Duration", "Calories Burned")
exercise_table = ttk.Treeview(
    exercise_frame, columns=exercise_columns, show="headings", height=12
)

for col in exercise_columns:
    exercise_table.heading(col, text=col)
    exercise_table.column(col, width=150)

exercise_table.pack(fill="both", expand=True, padx=5, pady=5)

exercise_btns = tk.Frame(exercise_frame)
exercise_btns.pack(fill="x", pady=5)

tk.Button(exercise_btns, text="Delete Entry").pack(side="left", padx=5)
tk.Button(exercise_btns, text="Add Exercise", bg="#5b8def").pack(side="left")

# ================= DAILY SUMMARY =================
summary_frame = tk.LabelFrame(root, text="Daily Summary")
summary_frame.pack(fill="x", padx=10, pady=10)

summary_items = [
    "Calories Consumed",
    "Protein (g)",
    "Fat (g)",
    "Carbs (g)",
    "Exercise (kCal)",
    "Net Calories"
]

for item in summary_items:
    block = tk.Frame(summary_frame, padx=15)
    block.pack(side="left", expand=True)

    tk.Label(block, text=item).pack()
    tk.Label(block, text="0", font=("Arial", 11, "bold")).pack()

# ================= NOTES =================
notes_frame = tk.LabelFrame(root, text="Notes")
notes_frame.pack(fill="x", padx=10, pady=5)

notes_text = tk.Text(notes_frame, height=4)
notes_text.pack(fill="x", padx=5, pady=5)

# ================= UPDATE =================
update_frame = tk.Frame(root)
update_frame.pack(fill="x", pady=10)

tk.Button(update_frame, text="Update", width=14).pack(side="right", padx=20)

root.mainloop()
