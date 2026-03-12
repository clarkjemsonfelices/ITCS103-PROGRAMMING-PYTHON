import tkinter as tk

# ===================== Simple Calculator ==========================

# Operator Functions
def addition():
	num1 = first_entry.get()
	num2 = second_entry.get()
	result = int(num1) + int(num2)
	
	label["text"] = f"The sum of {num1} + {num2} is {result}"
	
def substract():
	num1 = first_entry.get()
	num2 = second_entry.get()
	result = int(num1) - int(num2)
	
	label["text"] = f"The difference of {num1} - {num2} is {result}"
	
def multiply():
	num1 = first_entry.get()
	num2 = second_entry.get()
	result = int(num1) * int(num2)
	
	label["text"] = f"The product of {num1} x {num2} is {result}"
	
def division():
	num1 = first_entry.get()
	num2 = second_entry.get()
	
	if int(num2) != 0:
		result = int(num1) / int(num2)
		label["text"] = f"The quotient of {num1} / {num2} is {result}"
	else:
		label["text"] = f"Cannot Divide by 0"

# Window
window = tk.Tk()
window.title("Simple Calculator")
window.resizable(False, False)

# Label
label = tk.Label(window,
							text = "Simple Calculator")
label.grid(row = 0, column = 0)

# Frame
frame = tk.Frame(window, 
								bg = "cyan",
								bd = 10)
frame.grid(row = 1, column = 0)

# First Number
first_label = tk.Label(frame,
							text = "Enter 1st Number:")
first_label.grid(row = 0, column = 0)

first_entry = tk.Entry(frame)
first_entry.grid(row = 0, column = 1, padx = 2)

# Second Number
second_label = tk.Label(frame,
							text = "Enter 2nd Number:")
second_label.grid(row = 1, column = 0, pady = 5, padx = 2)

second_entry = tk.Entry(frame)
second_entry.grid(row = 1, column = 1)

# Operator Buttons
add_button = tk.Button(frame,
										  text = "Add",
										  command = addition)
add_button.grid(row = 2, column = 0)

sub_button = tk.Button(frame,
										  text = "Substract",
										  command = substract)
sub_button.grid(row = 2, column = 1)

mul_button = tk.Button(frame,
										  text = "Multiply",
										  command = multiply)
mul_button.grid(row = 3, column = 0)

div_button = tk.Button(frame,
										  text = "Division",
										  command = division)
div_button.grid(row = 3, column = 1)

window.mainloop()