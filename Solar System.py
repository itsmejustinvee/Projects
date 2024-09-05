import tkinter as tk

#storing planet values

PLANET_VALUES = {
    "Sun": {"radius": 30, "color": "yellow", "distance": 10},
    "Mercury": {"radius": 5, "color": "gray", "distance": 20},
    "Venus": {"radius": 8, "color": "orange", "distance": 40},
    "Earth": {"radius": 8, "color": "blue", "distance": 50},
    "Mars": {"radius": 6, "color": "red", "distance": 60},
    "Jupiter": {"radius": 18, "color": "brown", "distance": 70},
    "Saturn": {"radius": 16, "color": "gold", "distance": 80},
    "Uranus": {"radius": 14, "color": "light blue", "distance": 90},
    "Neptune": {"radius": 14, "color": "blue", "distance": 100},
    "Pluto": {"radius": 4, "color": "light gray", "distance": 110},
    }

#main window
root = tk.Tk()
root.title("Solar System")

#canvas
canvas = tk.Canvas(root, width=800, height=200, bg='black')
canvas.pack()

current_x = PLANET_VALUES["Sun"]["distance"] # gives the starting planet which will  be the sun

#Drawing the planets with a looperino
for planet, value in PLANET_VALUES.items():
    x = current_x + value["radius"]
    y = 80
    canvas.create_oval(x - value["radius"], y - value["radius"], #Draws the oval for the planet
                       x + value["radius"], y + value["radius"], fill=value["color"]) 
    canvas.create_text(x, y + value["radius"] + 10, text=planet, fill='white') #Slaps a label under the planet
    
    current_x += value["distance"] + value["radius"] * 2 #updates the current x position so planets dont overlap
    
#running the main loop
root.mainloop()