import tkinter as tk
from tkinter import ttk

def reset():
    estado_select.set(None)

window = tk.Tk()
window.geometry("200x320")
window.title('Radio Buttons')

window.columnconfigure(0, weight=3)
window.rowconfigure(0, weight=3)

label = ttk.Label(text="¿Cuál es tu estado civil?")
label.pack(fill='x', padx=5, pady=5)

estado_select = tk.StringVar()

r1 = ttk.Radiobutton(window, text="Soltero", value='Soltero', variable=estado_select)
r1.pack(fill='x', padx=5, pady=5)
r2 = ttk.Radiobutton(window, text="Casado", value='Casado', variable=estado_select)
r2.pack(fill='x', padx=5, pady=5)
r3 = ttk.Radiobutton(window, text="Separado", value='Separado', variable=estado_select)
r3.pack(fill='x', padx=5, pady=5)
r4 = ttk.Radiobutton(window, text="Viudo", value='Viudo', variable=estado_select)
r4.pack(fill='x', padx=5, pady=5)

labelselected = ttk.Label(text="Tu seleción: ")
labelselected.pack(fill='x', padx=5, pady=5)

labelselected = ttk.Label(textvariable=estado_select)
labelselected.pack(fill='x', padx=5, pady=5)

reset_button = ttk.Button(window, text="Reset", command=reset)
reset_button.pack(fill='x', padx=5, pady=5)

window.mainloop()