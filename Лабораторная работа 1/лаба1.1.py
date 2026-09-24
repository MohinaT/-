import tkinter as tk
from tkinter import messagebox
import math

root = tk.Tk()
root.title("Площадь треугольника")
root.geometry("450x350")
root.configure(bg="#EAF4FF")

title = tk.Label(
    root,
    text="Вычисление площади треугольника",
    font=("Arial", 16, "bold"),
    bg="#EAF4FF",
    fg="#004080"
)
title.pack(pady=15)

frame = tk.Frame(root, bg="#EAF4FF")
frame.pack()

tk.Label(frame, text="Сторона a:", bg="#EAF4FF").grid(row=0, column=0, pady=5)
tk.Label(frame, text="Сторона b:", bg="#EAF4FF").grid(row=1, column=0, pady=5)
tk.Label(frame, text="Сторона c:", bg="#EAF4FF").grid(row=2, column=0, pady=5)

entry_a = tk.Entry(frame)
entry_b = tk.Entry(frame)
entry_c = tk.Entry(frame)

entry_a.grid(row=0, column=1)
entry_b.grid(row=1, column=1)
entry_c.grid(row=2, column=1)

result_label = tk.Label(
    root,
    text="Введите стороны треугольника",
    font=("Arial", 12),
    bg="#EAF4FF",
    fg="#333333"
)
result_label.pack(pady=20)

def calculate():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())

        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError

        if a + b <= c or a + c <= b or b + c <= a:
            messagebox.showerror("Ошибка", "Такой треугольник не существует")
            return

        p = (a + b + c) / 2
        s = math.sqrt(p * (p - a) * (p - b) * (p - c))

        result_label.config(
            text=f"Площадь = {s:.2f}",
            fg="green"
        )

    except:
        messagebox.showerror("Ошибка", "Введите корректные значения")

def clear():
    entry_a.delete(0, tk.END)
    entry_b.delete(0, tk.END)
    entry_c.delete(0, tk.END)
    result_label.config(
        text="Введите стороны треугольника",
        fg="#333333"
    )

button_frame = tk.Frame(root, bg="#EAF4FF")
button_frame.pack()

tk.Button(
    button_frame,
    text="Рассчитать",
    bg="#4A90E2",
    fg="white",
    command=calculate
).grid(row=0, column=0, padx=10)

tk.Button(
    button_frame,
    text="Очистить",
    bg="#888888",
    fg="white",
    command=clear
).grid(row=0, column=1, padx=10)

root.mainloop()