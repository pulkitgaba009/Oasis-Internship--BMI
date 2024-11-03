import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())

        if weight <= 0 or height <= 0:
            raise ValueError("Inputs must be positive numbers.")

        # Calculate BMI
        bmi = weight / (height ** 2)
        bmi = round(bmi, 2)

        # Determine the BMI category
        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 24.9:
            category = "Normal weight"
        elif 25 <= bmi < 29.9:
            category = "Overweight"
        else:
            category = "Obesity"

        result_label.config(text=f"BMI: {bmi}\nCategory: {category}")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers for weight and height.")

# Setting up the GUI window
root = tk.Tk()
root.title("BMI Calculator")

# Labels and entry fields for weight and height
tk.Label(root, text="Weight (kg):").grid(row=0, column=0, padx=10, pady=5)
weight_entry = tk.Entry(root)
weight_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Height (m):").grid(row=1, column=0, padx=10, pady=5)
height_entry = tk.Entry(root)
height_entry.grid(row=1, column=1, padx=10, pady=5)

# Button to calculate BMI
calculate_button = tk.Button(root, text="Calculate BMI", command=calculate_bmi)
calculate_button.grid(row=2, column=0, columnspan=2, pady=10)

# Label to display the BMI result and category
result_label = tk.Label(root, text="")
result_label.grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()
