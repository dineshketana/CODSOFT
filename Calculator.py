import tkinter as tk

def button_click(symbol):
    current = entry_display.get()
    entry_display.delete(0, tk.END)
    entry_display.insert(tk.END, current + symbol)

def clear_display():
    entry_display.delete(0, tk.END)

def calculate():
    try:
        expression = entry_display.get()
        result = eval(expression)
        entry_display.delete(0, tk.END)
        entry_display.insert(tk.END, str(result))
    except Exception as e:
        entry_display.delete(0, tk.END)
        entry_display.insert(tk.END, "Error")

root = tk.Tk()
root.title("Digital Calculator")

entry_display = tk.Entry(root, width=40, borderwidth=5)
entry_display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

button_list = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

for button in button_list:
    symbol, row, col = button
    if symbol == '=':
        btn = tk.Button(root, text=symbol, padx=30, pady=20, command=calculate)
    elif symbol == 'C':
        btn = tk.Button(root, text=symbol, padx=30, pady=20, command=clear_display)
    else:
        btn = tk.Button(root, text=symbol, padx=30, pady=20, command=lambda sym=symbol: button_click(sym))
    btn.grid(row=row, column=col)

root.mainloop()