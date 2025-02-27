import tkinter as tk
import math

def evaluate_expression():
    expression = output_box.get("1.0", 'end-1c')
    expression = expression.replace('^2', '**2').replace('sqrt', 'math.sqrt').replace('1/x', '(1/float')
    expression = expression.replace('^', '**').replace('sin', 'math.sin(math.radians').replace('cos', 'math.cos(math.radians')
    expression = expression.replace('tan', 'math.tan(math.radians').replace('log', 'math.log10').replace('x!', 'math.factorial')
    expression = expression.replace('ln', 'math.log').replace('√', 'math.sqrt')
    try:
        result = eval(expression + ')'*expression.count('('))
        output_box.config(state=tk.NORMAL)
        output_box.delete("1.0", tk.END)
        output_box.insert(tk.END, str(result))
        output_box.config(state=tk.DISABLED)
    except Exception as e:
        print(f"Error evaluating expression: {e}")

def create_output_box(width, height):
    box = tk.Text(root, height=height, bg='white', fg='black', font=('Arial', 14), state=tk.DISABLED, width=width)
    box.pack(fill=tk.BOTH, padx=10, pady=5)
    box.pack_configure(anchor=tk.CENTER)
    return box

def insert_number(number):
    output_box.config(state=tk.NORMAL)
    output_box.insert('end', str(number))
    output_box.config(state=tk.DISABLED)

def clear_output_box():
    output_box.config(state=tk.NORMAL)
    output_box.delete('1.0', 'end')
    output_box.config(state=tk.DISABLED)

def calculate(func):
    current_text = output_box.get("1.0", 'end-1c')
    if not current_text:
        return
    current_number = float(current_text)
    result = func(current_number)
    output_box.config(state=tk.NORMAL)
    output_box.delete("1.0", tk.END)
    output_box.insert(tk.END, str(result))
    output_box.config(state=tk.DISABLED)

def exit_app():
    root.destroy()

root = tk.Tk()
root.title("Vazgen's Absolutluy Great And Amazing Calculator")
root.configure(bg="gray")
root.attributes('-fullscreen', True)

output_box = create_output_box(10, 3)

button_frame = tk.Frame(root)
button_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

buttons = [
    ('1', 0, 0), ('2', 0, 1), ('3', 0, 2), ('+', 0, 3), ('^2', 0, 4),
    ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('-', 1, 3), ('√', 1, 4),
    ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('*', 2, 3), ('log', 2, 4),
    ('0', 3, 1), ('Clear', 3, 2), ('Enter', 3, 0), ('/', 3, 3), ('.', 3, 4),
    ('sin', 0, 5), ('cos', 1, 5), ('tan', 2, 5), ('x!', 3, 5),
    ('ln', 2, 6), (',', 3, 6), ('(', 0, 6), (')', 1, 6), ('Exit', 3, 7)
]

for (text, row, col) in buttons:
    if text in '1234567890+-*/.':
        cmd = lambda t=text: insert_number(t)
    elif text == 'Clear':
        cmd = clear_output_box
    elif text == 'Enter':
        cmd = evaluate_expression
    elif text == '^2':
        cmd = lambda: calculate(lambda x: x**2)
    elif text == '√':
        cmd = lambda: calculate(math.sqrt)
    elif text == 'log':
        cmd = lambda: calculate(lambda x: math.log(x, 10))
    elif text == 'sin':
        cmd = lambda: calculate(lambda x: math.sin(math.radians(x)))
    elif text == 'cos':
        cmd = lambda: calculate(lambda x: math.cos(math.radians(x)))
    elif text == 'tan':
        cmd = lambda: calculate(lambda x: math.tan(math.radians(x)))
    elif text == 'x!':
        cmd = lambda: calculate(math.factorial)
    elif text == 'ln':
        cmd = lambda: calculate(math.log)
    elif text == ',': 
        cmd = lambda: insert_number(',')
    elif text == '(':
        cmd = lambda: insert_number('(')
    elif text == ')':
        cmd = lambda: insert_number(')')
    elif text == 'Exit':
        cmd = exit_app
    button = tk.Button(button_frame, text=text, command=cmd, width=13, height=6, font=('Arial', 16, 'bold'))
    button.grid(row=row, column=col, padx=0, pady=0, sticky=tk.NSEW)

root.mainloop()
