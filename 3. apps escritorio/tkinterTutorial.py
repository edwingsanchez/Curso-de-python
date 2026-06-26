import tkinter as tk
from tkinter import ttk, messagebox

# Simple Tkinter tutorial application
# Demonstrates labels, entry, buttons, checkbuttons, radiobuttons, combobox, and listbox

def greet():
    name = name_var.get().strip()
    if name:
        messagebox.showinfo("Greeting", f"Hola, {name}!")
    else:
        messagebox.showwarning("Input required", "Por favor ingresa tu nombre.")


def update_choice():
    selected = color_var.get()
    choice_label.config(text=f"Color seleccionado: {selected}")


root = tk.Tk()
root.title("Tkinter Tutorial")
root.geometry("480x420")
root.resizable(False, False)

# Frame for user input
frame_top = ttk.LabelFrame(root, text="Información de usuario")
frame_top.pack(fill="x", padx=12, pady=12)

name_var = tk.StringVar()
color_var = tk.StringVar(value="Rojo")
subscribe_var = tk.BooleanVar(value=False)
mode_var = tk.StringVar(value="Claro")

name_label = ttk.Label(frame_top, text="Nombre:")
name_label.grid(row=0, column=0, padx=6, pady=6, sticky="w")
name_entry = ttk.Entry(frame_top, textvariable=name_var, width=30)
name_entry.grid(row=0, column=1, padx=6, pady=6)

subscribe_check = ttk.Checkbutton(
    frame_top,
    text="Suscribirse al boletín",
    variable=subscribe_var,
)
subscribe_check.grid(row=1, column=0, columnspan=2, padx=6, pady=6, sticky="w")

# Button section
button_frame = ttk.Frame(root)
button_frame.pack(fill="x", padx=12, pady=(0, 12))

greet_button = ttk.Button(button_frame, text="Saludar", command=greet)
greet_button.pack(side="left", padx=(0, 6))
reset_button = ttk.Button(
    button_frame,
    text="Limpiar",
    command=lambda: name_var.set("")
)
reset_button.pack(side="left")

# Options section
frame_options = ttk.LabelFrame(root, text="Opciones")
frame_options.pack(fill="x", padx=12, pady=0)

color_label = ttk.Label(frame_options, text="Color favorito:")
color_label.grid(row=0, column=0, padx=6, pady=6, sticky="w")
color_combo = ttk.Combobox(
    frame_options,
    textvariable=color_var,
    values=["Rojo", "Verde", "Azul", "Amarillo"],
    state="readonly",
)
color_combo.grid(row=0, column=1, padx=6, pady=6)
color_combo.bind("<<ComboboxSelected>>", lambda e: update_choice())

mode_label = ttk.Label(frame_options, text="Modo:")
mode_label.grid(row=1, column=0, padx=6, pady=6, sticky="w")

mode_radio_light = ttk.Radiobutton(
    frame_options, text="Claro", variable=mode_var, value="Claro", command=update_choice
)
mode_radio_light.grid(row=1, column=1, sticky="w", padx=6)
mode_radio_dark = ttk.Radiobutton(
    frame_options, text="Oscuro", variable=mode_var, value="Oscuro", command=update_choice
)
mode_radio_dark.grid(row=1, column=1, sticky="e", padx=6)

choice_label = ttk.Label(frame_options, text=f"Color seleccionado: {color_var.get()}")
choice_label.grid(row=2, column=0, columnspan=2, padx=6, pady=(10, 6), sticky="w")

# Listbox section
frame_list = ttk.LabelFrame(root, text="Elementos")
frame_list.pack(fill="both", expand=True, padx=12, pady=12)

items = ["Python", "Tkinter", "Widgets", "Eventos", "Layouts"]
listbox = tk.Listbox(frame_list, height=5)
for item in items:
    listbox.insert(tk.END, item)
listbox.pack(fill="both", expand=True, padx=6, pady=6)

root.mainloop()
