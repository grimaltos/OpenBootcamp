import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.geometry("200x320")
window.title('Lista Elementos')

window.columnconfigure(0, weight=3)
window.rowconfigure(0, weight=3)

vehiculos = ('Coche', 'Moto', 'Bici', 'Patinete')
vehiculos_var = tk.StringVar(value=vehiculos)

label = ttk.Label(text="¿Cuál es tu vehiculo favorito?")
label.pack(fill='x', padx=5, pady=5)

s1 = tk.Listbox(window, height=6, listvariable=vehiculos_var)
s1.pack(fill='x', padx=5, pady=5)


window.mainloop()