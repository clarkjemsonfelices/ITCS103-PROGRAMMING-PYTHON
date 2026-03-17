import tkinter as tk

main_color = "light green"
male_color = "light blue"
female_color = "pink"

def popup():
    profile_id = tk.Toplevel()
    profile_id.title("Profile ID")
    profile_id.resizable(False, False)
    profile_id.config(bg = main_color)

    first = first_entry.get()
    middle = middle_entry.get()
    last = last_entry.get()

    student_id = tk.Label(profile_id,
                           text = "Student ID",
                           font = ("times new roman", 20, "bold"),
                           bg = main_color)
    student_id.grid(row = 0, column = 0)

    frame2 = tk.Frame(profile_id)
    frame2.grid(row = 1, column = 0)


def age_calculate(event):
    year = int(year_entry.get())
    result = 2026 - year
    age["text"] = f"You are {result} years old"

def male():
    profile["bg"] = male_color
    window["bg"] = male_color

def female():
    profile["bg"] = female_color
    window["bg"] = female_color

window = tk.Tk()
window.title("Profile Builder")
#window.geometry("500x400")
window.resizable(False , False)
window.configure(bg = main_color)

profile = tk.Label(window,
                   text = "Profile Builder",
                   bg = main_color,
                   font = ("times new roman", 15, "bold"))
profile.grid(row = 0, column = 0)

frame = tk.Frame(window,
                 bg = main_color,
                 bd = 10)
frame.grid(row = 1, column = 0, padx = 10, pady = 10)

# First Name
first_entry = tk.Entry(frame)
first_entry.grid(row = 0, column = 0, columnspan = 3)

first_name = tk.Label(frame,
                      text = "First Name",
                      bg = main_color)
first_name.grid(row = 1, column = 0, columnspan = 3)

# Middle Name
middle_entry = tk.Entry(frame)
middle_entry.grid(row = 0, column = 3, columnspan = 3, padx = 20)

middle_name = tk.Label(frame,
                      text = "Middle Name",
                      bg = main_color)
middle_name.grid(row = 1, column = 3, columnspan = 3)

# Last Name
last_entry = tk.Entry(frame)
last_entry.grid(row = 0, column = 6, columnspan = 3)

last_name = tk.Label(frame,
                      text = "Last Name",
                      bg = main_color)
last_name.grid(row = 1, column = 6, columnspan = 3)

# Year Born
year_entry = tk.Entry(frame)
year_entry.grid(row = 2, column = 0)

year_label = tk.Label(frame,
                      text = "Year Born",
                      bg = main_color)
year_label.grid(row = 3, column = 0, columnspan = 3)

age = tk.Label(frame,
               text = "You are 0 years old",
               font = ("times new roman", 15, "bold"),
               bg = main_color)
age.grid(row = 2, column = 4, rowspan = 2, columnspan = 6)

window.bind("<Return>", age_calculate)

# Gender
gender_val = tk.IntVar()
gender_label = tk.Label(frame,
                        text = "Gender",
                        bg = main_color)
gender_label.grid(row = 4, column = 0, columnspan = 3)

gender_male = tk.Radiobutton(frame,
                             text = "Male",
                             bg = main_color,
                             value = 1,
                             variable = gender_val,
                            command = male)
gender_male.grid(row = 4, column = 3)

gender_female = tk.Radiobutton(frame,
                             text = "Female",
                             bg = main_color,
                             value = 2,
                             variable = gender_val,
                             command = female)
gender_female.grid(row = 4, column = 4)

button = tk.Button(window,
                   text = "Submit",
                   font = ("arial", 10, "bold"),
                   bg = main_color,
                   command = popup)
button.grid(row = 2, column = 0)




window.mainloop()