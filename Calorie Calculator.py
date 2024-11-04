import tkinter as tk
from tkinter import messagebox

def calculate_calories():
    gender = gender_var.get().strip()
    age = int(age_entry.get())
    height = int(height_entry.get())
    weight = int(weight_entry.get())
    if gender in ["man", "Man","MAN"]:
        result = 66.5 + (13.75 * weight) + (5 * height) - (6.77 * age)
    elif gender in ["Woman", "woman","WOMAN"]:
        result = 655.1 + (9.56 * weight) + (1.85 * height) - (4.67 * age)
    else:
        messagebox.showerror("Eror","You did not enter your gender")
        return
    
    result_label.config(text=f"You need to take {result:.2f} calories per day")
app = tk.Tk()
app.minsize()
app.config(bg="light blue")
app.title("Calorie Calculator")

tk.Label(app, text="Enter Your Gender (man/woman):").grid(row=0, column=0, padx=10, pady=10)
gender_var = tk.StringVar()
gender_entry = tk.Entry(app, textvariable=gender_var)
gender_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(app, text="Enter Your Age:").grid(row=1, column=0, padx=10, pady=10)
age_entry = tk.Entry(app)
age_entry.grid(row=1, column=1, padx=10, pady=10)

tk.Label(app, text="Enter Your Height:").grid(row=2, column=0, padx=10, pady=10)
height_entry = tk.Entry(app)
height_entry.grid(row=2, column=1, padx=10, pady=10)

tk.Label(app, text="Enter Your Weight:").grid(row=3, column=0, padx=10, pady=10)
weight_entry = tk.Entry(app)
weight_entry.grid(row=3, column=1, padx=10, pady=10)

calculate_button = tk.Button(app, text="Calculate", command=calculate_calories)
calculate_button.grid(row=4, column=0, columnspan=2, pady=10)

result_label = tk.Label(app, text="")
result_label.grid(row=5, column=0, columnspan=2, pady=10)

app.mainloop()
