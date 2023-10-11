import customtkinter as tk


def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))


def clear():
    entry.delete(0, tk.END)


def evaluate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")


# 创建主窗口
window = tk.CTk()
window.title("简单计算器")

# 创建输入框
entry = tk.CTkEntry(window, width=200)
entry.grid(row=0, column=0, columnspan=4)

# 创建按钮
buttons = [
    "7",
    "8",
    "9",
    "/",
    "4",
    "5",
    "6",
    "*",
    "1",
    "2",
    "3",
    "-",
    "0",
    "C",
    "=",
    "+",
]

row, col = 1, 0
for button_text in buttons:
    if button_text == "=":
        button = tk.CTkButton(window, text=button_text, width=20, command=evaluate)
    elif button_text == "C":
        button = tk.CTkButton(window, text=button_text, width=20, command=clear)
    else:
        button = tk.CTkButton(
            window,
            text=button_text,
            width=15,
            command=lambda text=button_text: button_click(text),
        )

    button.grid(row=row, column=col, padx=2, pady=2)
    col += 1
    if col > 3:
        col = 0
        row += 1

# 运行主循环
window.resizable(width=False, height=False)
window.mainloop()
