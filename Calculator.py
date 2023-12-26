import tkinter
from PIL import Image, ImageTk
import urllib.request
import io
import math


def evaluate_expression():
    # Get the expression from the output box
    expression = output_box.get("1.0", 'end-1c')

    # Check for advanced operators and replace them with their Python equivalents
    expression = expression.replace('^2', '**2')
    expression = expression.replace('sqrt', 'math.sqrt(')
    expression = expression.replace('1/x', '(1/float(')
    expression = expression.replace('^', '**')
    expression = expression.replace('sin', 'math.sin(')
    expression = expression.replace('cos', 'math.cos(')
    expression = expression.replace('tan', 'math.tan(')
    expression = expression.replace('log', 'math.log(')
    expression = expression.replace('x!', 'math.factorial(')
    expression = expression.replace('ln', 'math.ln(')

    # Add closing parentheses
    expression = expression.replace('(', '()', 1)

    try:
        # Evaluate the expression
        result = eval(expression)

        # Temporarily enable the output_box
        output_box.config(state=tkinter.NORMAL)

        # Clear the output_box and insert the result
        output_box.delete("1.0", tkinter.END)
        output_box.insert(tkinter.END, str(result))

        # Disable the output_box again
        output_box.config(state=tkinter.DISABLED)
    except Exception as e:
        print(f"Error evaluating expression: {e}")


# Main Window
root = tkinter.Tk()
root.title("Vazgen's Absolutluy Great And Amazing Calculator")
root.configure(bg="gray")
root.attributes('-fullscreen', True)  # Make the window fullscreen

# Output box
def create_output_box(width, height):
    output_box = tkinter.Text(root, height=height, bg='white', fg='black', font=('Arial', 14), state=tkinter.DISABLED, width=width)
    output_box.pack(fill=tkinter.BOTH, padx=10, pady=5)
    output_box.pack_configure(anchor=tkinter.CENTER)
    return output_box

output_box = create_output_box(10, 3)

# Function to insert number into output box
def insert_number(number):
    output_box.config(state=tkinter.NORMAL)  # Enable the Text widget
    output_box.insert('end', str(number))
    output_box.config(state=tkinter.DISABLED)  # Disable the Text widget

# Function to evaluate the expression
def evaluate_expression():
    output_box.config(state=tkinter.NORMAL)  # Enable the Text widget
    expression = output_box.get('1.0', 'end').strip()
    try:
        result = eval(expression)
        output_box.delete('1.0', 'end')
        output_box.insert('end', str(result))
    except Exception as e:
        output_box.delete('1.0', 'end')
        output_box.insert('end', str(e))
    output_box.config(state=tkinter.DISABLED)  # Disable the Text widget

def square_2():
    # Get the current text in the output_box
    current_text = output_box.get("1.0", 'end-1c')

    # Check if the text field is empty
    if not current_text:
        return

    # Convert the text to a float and calculate the square
    current_number = float(current_text)
    result = current_number ** 2

    # Temporarily enable the output_box
    output_box.config(state=tkinter.NORMAL)

    # Clear the output_box and insert the result
    output_box.delete("1.0", tkinter.END)
    output_box.insert(tkinter.END, str(result))

def square_root():
    # Get the current text in the output_box
    current_text = output_box.get("1.0", 'end-1c')

    # Check if the text field is empty
    if not current_text:
        return

    # Convert the text to a float and calculate the square
    current_number = float(current_text)
    result = math.sqrt(current_number)

    # Temporarily enable the output_box
    output_box.config(state=tkinter.NORMAL)

    # Clear the output_box and insert the result
    output_box.delete("1.0", tkinter.END)
    output_box.insert(tkinter.END, str(result))


def log():
    # Get the current text in the output_box
    current_text = output_box.get("1.0", 'end-1c')

    # Check if the text field is empty
    if not current_text:
        return

    # Convert the text to a float and calculate the logarithm base 10
    current_number = float(current_text)
    result = math.log(current_number, 10)

    # Temporarily enable the output_box
    output_box.config(state=tkinter.NORMAL)

    # Clear the output_box and insert the result
    output_box.delete("1.0", tkinter.END)
    output_box.insert(tkinter.END, str(result))

    # Disable the output_box again
    output_box.config(state=tkinter.DISABLED)

def ln():
    # Get the current text in the output_box
    current_text = output_box.get("1.0", 'end-1c')

    # Check if the text field is empty
    if not current_text:
        return

    # Convert the text to a float and calculate the natural logarithm
    current_number = float(current_text)
    result = math.log(current_number)

    # Temporarily enable the output_box
    output_box.config(state=tkinter.NORMAL)

    # Clear the output_box and insert the result
    output_box.delete("1.0", tkinter.END)
    output_box.insert(tkinter.END, str(result))

    # Disable the output_box again
    output_box.config(state=tkinter.DISABLED)


def sin():
    # Get the current text in the output_box
    current_text = output_box.get("1.0", 'end-1c')

    # Check if the text field is empty
    if not current_text:
        return

    # Convert the text to a float, convert degrees to radians, and calculate the sin of the number
    current_number = math.radians(float(current_text))
    result = math.sin(current_number)

    # Temporarily enable the output_box
    output_box.config(state=tkinter.NORMAL)

    # Clear the output_box and insert the result
    output_box.delete("1.0", tkinter.END)
    output_box.insert(tkinter.END, str(result))

    # Disable the output_box again
    output_box.config(state=tkinter.DISABLED)

def cos():
    # Get the current text in the output_box
    current_text = output_box.get("1.0", 'end-1c')

    # Check if the text field is empty
    if not current_text:
        return

    # Convert the text to a float, convert degrees to radians, and calculate the sin of the number
    current_number = math.radians(float(current_text))
    result = math.cos(current_number)

    # Temporarily enable the output_box
    output_box.config(state=tkinter.NORMAL)

    # Clear the output_box and insert the result
    output_box.delete("1.0", tkinter.END)
    output_box.insert(tkinter.END, str(result))

    # Disable the output_box again
    output_box.config(state=tkinter.DISABLED)

def tan():
    # Get the current text in the output_box
    current_text = output_box.get("1.0", 'end-1c')

    # Check if the text field is empty
    if not current_text:
        return

    # Convert the text to a float, convert degrees to radians, and calculate the sin of the number
    current_number = math.radians(float(current_text))
    result = math.tan(current_number)

    # Temporarily enable the output_box
    output_box.config(state=tkinter.NORMAL)

    # Clear the output_box and insert the result
    output_box.delete("1.0", tkinter.END)
    output_box.insert(tkinter.END, str(result))

    # Disable the output_box again
    output_box.config(state=tkinter.DISABLED)

def dot():
    # Get the current text in the output_box
    current_text = output_box.get("1.0", 'end-1c')

    # Check if the text field is empty
    if not current_text:
        return
    
    # Temporarily enable the output_box
    output_box.config(state=tkinter.NORMAL)

    # Clear the output_box and insert the result
    output_box.insert(tkinter.END, '.')

    # Disable the output_box again
    output_box.config(state=tkinter.DISABLED)

def x_Factorial():
    # Get the current text in the output_box
    current_text = output_box.get("1.0", 'end-1c')

    # Check if the text field is empty
    if not current_text:
        return

    # Convert the text to an integer and calculate the factorial
    current_number = int(current_text)
    result = math.factorial(current_number)

    # Temporarily enable the output_box
    output_box.config(state=tkinter.NORMAL)

    # Clear the output_box and insert the result
    output_box.delete("1.0", tkinter.END)
    output_box.insert(tkinter.END, str(result))

    # Disable the output_box again
    output_box.config(state=tkinter.DISABLED)

def comma():
    # Get the current text in the output_box
    current_text = output_box.get("1.0", 'end-1c')

    # Check if the text field is empty
    if not current_text:
        return
    
    # Temporarily enable the output_box
    output_box.config(state=tkinter.NORMAL)

    # Clear the output_box and insert the result
    output_box.insert(tkinter.END, ',')

    # Disable the output_box again
    output_box.config(state=tkinter.DISABLED)

def left_curl():
    # Get the current text in the output_box
    current_text = output_box.get("1.0", 'end-1c')

    # Check if the text field is empty
    if not current_text:
        return
    
    # Temporarily enable the output_box
    output_box.config(state=tkinter.NORMAL)

    # Clear the output_box and insert the result
    output_box.insert(tkinter.END, '(')

    # Disable the output_box again
    output_box.config(state=tkinter.DISABLED)

def right_curl():
    # Get the current text in the output_box
    current_text = output_box.get("1.0", 'end-1c')

    # Check if the text field is empty
    if not current_text:
        return
    
    # Temporarily enable the output_box
    output_box.config(state=tkinter.NORMAL)

    # Clear the output_box and insert the result
    output_box.insert(tkinter.END, ')')

    # Disable the output_box again
    output_box.config(state=tkinter.DISABLED)

# Function to clear output box
def clear_output_box():
    output_box.config(state=tkinter.NORMAL)  
    output_box.delete('1.0', 'end')
    output_box.config(state=tkinter.DISABLED) 

# Create a frame to hold the buttons
button_frame = tkinter.Frame(root)
button_frame.pack(side=tkinter.BOTTOM, fill=tkinter.BOTH, expand=True)


# Buttons for numbers 1-9
for i in range(1, 10):
    button = tkinter.Button(button_frame, text=str(i), command=lambda i=i: insert_number(i), width=13, height=6, font=('Arial', 16, 'bold'))
    button.grid(row=(i-1)//3, column=(i-1)%3, padx=0, pady=0, sticky=tkinter.NSEW)

# Button for number 0
button = tkinter.Button(button_frame, text='0', command=lambda: insert_number(0), width=13, height=6, font=('Arial', 16, 'bold'))
button.grid(row=3, column=1, padx=0, pady=0, sticky=tkinter.NSEW)

# Buttons for basic operators
for i, op in enumerate(['+', '-', '*', '/']):
    button = tkinter.Button(button_frame, text=op, command=lambda op=op: insert_number(op), width=13, height=6, font=('Arial', 16, 'bold'))
    button.grid(row=i, column=3, padx=0, pady=0, sticky=tkinter.NSEW)

# Clear button
button_clear = tkinter.Button(button_frame, text='Clear', command=clear_output_box, width=13, height=6, font=('Arial', 16, 'bold'))
button_clear.grid(row=3, column=2, padx=0, pady=0)

# Enter button
button_enter = tkinter.Button(button_frame, text='Enter', command=evaluate_expression, width=13, height=6, font=('Arial', 16, 'bold'))
button_enter.grid(row=3, column=0, padx=0, pady=0)

# Button for ^2
button = tkinter.Button(button_frame, text='^2', command=square_2, width=13, height=6, font=('Arial', 16, 'bold'))
button.grid(row=0, column=4, padx=0, pady=0, sticky=tkinter.NSEW)

# Button for sqrt root
button = tkinter.Button(button_frame, text='√', command=square_root, width=13, height=6, font=('Arial', 16, 'bold'))
button.grid(row=1, column=4, padx=0, pady=0, sticky=tkinter.NSEW)

# Button for log
button = tkinter.Button(button_frame, text='log', command=log, width=13, height=6, font=('Arial', 16, 'bold'))
button.grid(row=2, column=4, padx=0, pady=0, sticky=tkinter.NSEW)

# Button for sin
button = tkinter.Button(button_frame, text='sin', command=sin, width=13, height=6, font=('Arial', 16, 'bold'))
button.grid(row=0, column=7, padx=0, pady=0, sticky=tkinter.NSEW)

# Button for cos
button = tkinter.Button(button_frame, text='cos', command=cos, width=13, height=6, font=('Arial', 16, 'bold'))
button.grid(row=1, column=7, padx=0, pady=0, sticky=tkinter.NSEW)

# Button for tan
button = tkinter.Button(button_frame, text='tan', command=tan, width=13, height=6, font=('Arial', 16, 'bold'))
button.grid(row=2, column=7, padx=0, pady=0, sticky=tkinter.NSEW)

# Button for dot
button = tkinter.Button(button_frame, text='.', command=lambda: dot(), width=13, height=6, font=('Arial', 16, 'bold'))
button.grid(row=3, column=4, padx=0, pady=0, sticky=tkinter.NSEW)

# Button for x!
button = tkinter.Button(button_frame, text='x!', command= x_Factorial, width=13, height=6, font=('Arial', 16, 'bold'))
button.grid(row=3, column=7, padx=0, pady=0, sticky=tkinter.NSEW)

# Button for ln
ln_button = tkinter.Button(button_frame, text="ln", command=ln, width=13, height=6, font=('Arial', 16, 'bold'))
ln_button.grid(row=2, column=6, padx=0, pady=0, sticky=tkinter.NSEW)

# Button for comma
button = tkinter.Button(button_frame, text=',', command=lambda: comma(), width=13, height=6, font=('Arial', 16, 'bold'))
button.grid(row=3, column=6, padx=0, pady=0, sticky=tkinter.NSEW)

# Button for (
button = tkinter.Button(button_frame, text='(', command=lambda: left_curl(), width=13, height=6, font=('Arial', 16, 'bold'))
button.grid(row=0, column=6, padx=0, pady=0, sticky=tkinter.NSEW)

# Button for )
button = tkinter.Button(button_frame, text=')', command=lambda: right_curl(), width=13, height=6, font=('Arial', 16, 'bold'))
button.grid(row=1, column=6, padx=0, pady=0, sticky=tkinter.NSEW)

# Start the Tkinter event loop
root.mainloop()
