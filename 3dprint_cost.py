import tkinter as tk
from tkinter import messagebox

def estimate_3dprint_cost():
    try:
        filament_weight = float(entry_filament_weight.get())
        filament_price_per_kg = float(entry_filament_price.get())
        print_time = float(entry_print_time.get())
        electricity_rate = float(entry_electricity_rate.get())

        # Constants
        machine_wear_per_hour = 1.5
        labor_per_hour = 5.0
        profit_margin = 0.25

        # Cost calculations
        filament_cost = (filament_weight / 1000) * filament_price_per_kg
        electricity_cost = print_time * electricity_rate
        machine_wear_cost = print_time * machine_wear_per_hour
        labor_cost = print_time * labor_per_hour
        base_cost = filament_cost + electricity_cost + machine_wear_cost + labor_cost
        final_price = base_cost * (1 + profit_margin)

        # Update result label
        result_text.set(f"Total Price: €{round(final_price, 2)}")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")

# GUI setup
root = tk.Tk()
root.title("3D Print Cost Estimator")

tk.Label(root, text="Filament Used (g):").grid(row=0, column=0)
entry_filament_weight = tk.Entry(root)
entry_filament_weight.grid(row=0, column=1)

tk.Label(root, text="Filament Price per kg (€):").grid(row=1, column=0)
entry_filament_price = tk.Entry(root)
entry_filament_price.grid(row=1, column=1)

tk.Label(root, text="Print Time (hours):").grid(row=2, column=0)
entry_print_time = tk.Entry(root)
entry_print_time.grid(row=2, column=1)

tk.Label(root, text="Electricity Rate per hour (€):").grid(row=3, column=0)
entry_electricity_rate = tk.Entry(root)
entry_electricity_rate.grid(row=3, column=1)

result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text, font=("Arial", 12, "bold"))
result_label.grid(row=5, columnspan=2)

tk.Button(root, text="Calculate", command=estimate_3dprint_cost).grid(row=4, columnspan=2)

root.mainloop()
