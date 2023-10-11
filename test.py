import tkinter as tk

window = tk.Tk()
window.title("columnspan示例")

label1 = tk.Label(window, text="跨越两列")
label1.grid(row=0, column=0, columnspan=2)

label2 = tk.Label(window, text="单独的列")
label2.grid(row=1, column=0)

window.mainloop()
