import tkinter as tk
from tkinter import messagebox

#Services offered 
services = {
    "Oil Change": 30.00,
    "Lube Job": 20.00,
    "Radiator Flush": 40.00,
    "Transmission Flush": 100.00,
    "Inspection": 35.00,
    "Muffler Replacement": 200.00,
    "Tire Rotation": 20.00
    }

#Lets calculate the charges and display them

def total_cost():
    total = 0
    for service, var in checkbuttons.items():
        if var.get():
            total += services[service]
            
    messagebox.showinfo("Total Service Cost", f"Your total comes to:${total:,.2f}")
    

#Main window
root = tk.Tk()
root.title("Joe's Automotive")


#Making a button for each service
checkbuttons = {}

for service, price in services.items():
    var = tk.BooleanVar() #stores the state of the buttons
    cb = tk.Checkbutton(root, text=f"{service} - ${price:,.2f}", variable=var)
    cb.pack(anchor='w') # aligns to the left
    checkbuttons[service] = var #stores the variable in the dictionary we got going
    
#Display charges button
total_button = tk.Button(root, text="Total Cost", command=total_cost)
total_button.pack(pady=10)

#Exit button
exit_button = tk.Button(root, text="Exit", command=root.destroy)
exit_button.pack(pady=5)

#starts the loop
root.mainloop()
            
    
