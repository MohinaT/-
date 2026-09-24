import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Проверка года")
root.geometry("450x300")
root.configure(bg="#F0FFF0")

title = tk.Label(
    root,
    text="Определение високосного года",
    font=("Tahoma", 16, "bold"),
    bg="#F0FFF0",
    fg="#006400"
)
title.pack(pady=15)

tk.Label(
    root,
    text="Введите год:",
    bg="#F0FFF0",
    font=("Tahoma", 11)
).pack()

year_entry = tk.Entry(root, font=("Tahoma", 12))
year_entry.pack(pady=10)

result = tk.Label(
    root,
    text="",
    font=("Tahoma", 14, "bold"),
    bg="#F0FFF0"
)
result.pack(pady=20)

rule_label = tk.Label(
    root,
    text="",
    bg="#F0FFF0",
    font=("Tahoma", 10)
)
rule_label.pack()

def check_year():
    try:
        year = int(year_entry.get())

        if year % 400 == 0:
            result.config(
                text="✓ Високосный год",
                fg="green"
            )
            rule_label.config(
                text="Год делится на 400"
            )

        elif year % 100 == 0:
            result.config(
                text="✗ Не високосный год",
                fg="red"
            )
            rule_label.config(
                text="Год делится на 100, но не делится на 400"
            )

        elif year % 4 == 0:
            result.config(
                text="✓ Високосный год",
                fg="green"
            )
            rule_label.config(
                text="Год делится на 4"
            )

        else:
            result.config(
                text="✗ Не високосный год",
                fg="red"
            )
            rule_label.config(
                text="Год не делится на 4"
            )

    except:
        messagebox.showerror("Ошибка", "Введите корректный год")

tk.Button(
    root,
    text="Проверить",
    command=check_year,
    bg="#228B22",
    fg="white",
    font=("Tahoma", 10, "bold")
).pack(pady=10)

root.mainloop()