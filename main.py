import tkinter as tk

def button_click(symbol):
    if symbol == "=":
        try:
            result = eval(display.get())
            display.delete(0, tk.END)
            display.insert(tk.END, str(result))
        except Exception as e:
            display.delete(0, tk.END)
            display.insert(tk.END, "Error")
    elif symbol == "C":
        display.delete(0, tk.END)
    else:
        display.insert(tk.END, symbol)

def key_press(event):
    key = event.char
    if key.isdigit() or key in "+-*/.=":
        button_click(key)
    elif event.keysym == "Return":
        button_click("=")
    elif event.keysym == "BackSpace":
        display.delete(len(display.get()) - 1, tk.END)

root = tk.Tk()
root.title("Colorful Calculator")
root.geometry("300x400")
root.config(bg="#f0f0f0")

display = tk.Entry(root, width=30, borderwidth=5, font=("Arial", 14), bg="#ffffff")
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ('C', 5, 0)
]

for (text, row, col) in buttons:
    button = tk.Button(root, text=text, padx=20, pady=10, font=("Arial", 12), bg="#a5d8ff", activebackground="#77aaff",
                       command=lambda symbol=text: button_click(symbol))
    button.grid(row=row, column=col, padx=5, pady=5)
    root.bind('<KeyPress-{}>'.format(text), key_press)

root.bind('<KeyPress-Return>', key_press)
root.bind('<KeyPress-BackSpace>', key_press)

root.mainloop()
