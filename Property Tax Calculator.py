import tkinter as tk
from tkinter import messagebox

def tax_calculation():
    try:
        actual_value = float(property_value_entry.get())
        
        assessed_value = actual_value * .06
        
        property_tax = (assessed_value / 100) * 0.75
        
        messagebox.showinfo("Property Tax Assessment",
                            f"Assessed Value: ${assessed_value:,.2f}\n"
                            f"Property Tax: ${property_tax:,.2f}")
        
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a proper number for the property value.")
            
#Main window
            
root = tk.Tk()
root.title("Property Tax Assessment")

tk.Label(root, text="Enter the value of your property:").pack(pady=10)

property_value_entry = tk.Entry(root)
property_value_entry.pack(pady=10)

calculate_button = tk.Button(root, text="Calculate Tax", command=tax_calculation)
calculate_button.pack(pady=10)

exit_button = tk.Button(root, text="Exit", command=root.destroy)
exit_button.pack(pady=10)

#starting the loop

root.mainloop()