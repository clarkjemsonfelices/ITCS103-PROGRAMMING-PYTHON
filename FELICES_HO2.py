import tkinter as tk

# functions for shortcuts - faster editing
color = "aqua"
tcolor = "black" # t = text
tfont = "Arial"
tsize = 12
space = 5

# window
window = tk.Tk()
window.title("Clark Jemson's Profile")
window.geometry("600x600")
window.resizable(False, True)
window.configure(bg = color)

profile = tk.Label(window, 
								text = "Student Profile",
								font = (tfont, 25, "bold"),
								bg = color)
profile.pack(pady = 20)

name = tk.Label(window,
								text = "Name: Clark Jemson I. Felices",
								font = (tfont, tsize),
								bg = color,
								fg = tcolor)
name.pack(pady = space, anchor = "w")

age = tk.Label(window,
								text = "Age: 18 years old",
								font = (tfont, tsize),
								bg = color,
								fg = tcolor)
age.pack(pady = space, anchor = "w")

course = tk.Label(window,
								text = "Course: BSIT",
								font = (tfont, tsize),
								bg = color,
								fg = tcolor)
course.pack(pady = space, anchor = "w")

birthday = tk.Label(window,
								text = "Birthday: July 26,2007",
								font = (tfont, tsize),
								bg = color,
								fg = tcolor)
birthday.pack(pady = space, anchor = "w")

motto = tk.Label(window,
								text = "Motto:",
								font = (tfont, tsize),
								bg = color,
								fg = tcolor)
motto.pack(pady = space, anchor = "w")

motto2 = tk.Label(window,
								text = "Honesty is the best policy",
								font = (tfont, tsize),
								bg = color,
								fg = tcolor)
motto2.pack(padx = 20, pady = space, anchor = "w")

window.mainloop()