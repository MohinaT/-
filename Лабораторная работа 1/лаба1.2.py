import tkinter as tk
from tkinter import ttk, messagebox

UNITS = {
    "Километры": 1000,
    "Метры": 1,
    "Сантиметры": 0.01,
    "Миллиметры": 0.001,
    "Мили": 1609.344,
    "Ярды": 0.9144
}

root = tk.Tk()
root.title("Конвертер расстояний")
root.geometry("500x350")
root.configure(bg="#2B2B2B")

title = tk.Label(
    root,
    text="Конвертер единиц расстояния",
    font=("Verdana", 16, "bold"),
    bg="#2B2B2B",
    fg="#FFA500"
)
title.pack(pady=15)

tk.Label(
    root,
    text="Введите значение:",
    bg="#2B2B2B",
    fg="white"
).pack()

value_entry = tk.Entry(root, width=25)
value_entry.pack(pady=5)

tk.Label(
    root,
    text="Из:",
    bg="#2B2B2B",
    fg="white"
).pack()

from_box = ttk.Combobox(root, values=list(UNITS.keys()), state="readonly")
from_box.pack()
from_box.current(0)

tk.Label(
    root,
    text="В:",
    bg="#2B2B2B",
    fg="white"
).pack()

to_box = ttk.Combobox(root, values=list(UNITS.keys()), state="readonly")
to_box.pack()
to_box.current(1)

result = tk.Label(
    root,
    text="",
    font=("Verdana", 12, "bold"),
    bg="#2B2B2B",
    fg="#00FF99"
)
result.pack(pady=25)

def convert():
    try:
        value = float(value_entry.get())

        meters = value * UNITS[from_box.get()]
        answer = meters / UNITS[to_box.get()]

        result.config(
            text=f"{value:g} {from_box.get()} = {answer:.6g} {to_box.get()}"
        )

    except:
        messagebox.showerror("Ошибка", "Введите число")

tk.Button(
    root,
    text="Конвертировать",
    command=convert,
    bg="#FFA500",
    fg="black",
    font=("Verdana", 10, "bold")
).pack(pady=10)

root.mainloop()