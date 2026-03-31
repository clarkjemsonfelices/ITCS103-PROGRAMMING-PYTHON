import tkinter as tk

# Background Color
register_bg = "green"
login_bg = "red"

# Account
username = ""
password = ""

def register():
    def register_function():
        user = username_entry.get()
        passw = password_entry.get()

        if len(passw) < 8:
            label['text'] = "Error, Password must have minimum of 8 characters"
        else:
            label['text'] = "You have succesfully registered!"
            username = user
            password = passw

    def see():
        val = pass_val.get()

        if val == 1:
            password_entry['show'] = ""
        else:
            password_entry['show'] = "*"

    popup = tk.Toplevel(window)
    popup.title("Felices HO Exam")
    popup.resizable(False , False)
    popup.config(bg = register_bg, bd = 10)

    popup.transient(window)
    popup.grab_set()

    label = tk.Label(popup,
                     text = "Welcome!",
                     bg = register_bg,
                     fg = "white")
    label.grid(row = 0, column = 0, columnspan= 2)

    username_label = tk.Label(popup,
                              text = "Username: ",
                              bg = register_bg,
                              font = ("Arial", 10, "bold"))
    username_label.grid(row = 1, column = 0)

    username_entry = tk.Entry(popup)
    username_entry.grid(row = 1, column = 1)

    password_label = tk.Label(popup,
                              text = "Password: ",
                              bg = register_bg,
                              font = ("Arial", 10, "bold"))
    password_label.grid(row = 2, column = 0)

    password_entry = tk.Entry(popup, show = "*")
    password_entry.grid(row = 2, column = 1)

    pass_val = tk.IntVar()
    see_pass = tk.Checkbutton(popup,
                              text = "See Password",
                              offvalue = 0,
                              onvalue = 1,
                              variable = pass_val,
                              command = see)
    see_pass.grid(row = 3, column = 1)

    register = tk.Button(popup,
                         text = "Register",
                         width = 20,
                         command = register_function)
    register.grid(row = 4, column = 0, columnspan = 2)

def LogIn():
    def login_function():
        user = username_entry.get()
        passw = password_entry.get()

        if username == user and password == passw:
            label['text'] = "You have succesfully logged in!"
        else:
            label['text'] = "Your user credentials are incorrect!"

    def see():
        val = pass_val.get()

        if val == 1:
            password_entry['show'] = ""
        else:
            password_entry['show'] = "*"

    popup = tk.Toplevel(window)
    popup.title("Felices HO Exam")
    popup.resizable(False , False)
    popup.config(bg = login_bg, bd = 10)

    popup.transient(window)
    popup.grab_set()

    label = tk.Label(popup,
                     text = "Welcome!",
                     bg = login_bg,
                     fg = "white")
    label.grid(row = 0, column = 0, columnspan= 2)

    login_label = tk.Label(popup,
                           text = "Log In",
                           font = ("arial", 20, "bold"),
                           bg = login_bg)
    login_label.grid(row = 1, column = 0, columnspan= 2)

    username_label = tk.Label(popup,
                              text = "Username: ",
                              bg = login_bg,
                              font = ("Arial", 10, "bold"))
    username_label.grid(row = 2, column = 0)

    username_entry = tk.Entry(popup)
    username_entry.grid(row = 2, column = 1)

    password_label = tk.Label(popup,
                              text = "Password: ",
                              bg = login_bg,
                              font = ("Arial", 10, "bold"))
    password_label.grid(row = 3, column = 0)

    password_entry = tk.Entry(popup, show = "*")
    password_entry.grid(row = 3, column = 1)

    pass_val = tk.IntVar()
    see_pass = tk.Checkbutton(popup,
                              text = "See Password",
                              offvalue = 0,
                              onvalue = 1,
                              variable = pass_val,
                              command = see)
    see_pass.grid(row = 4, column = 1)

    login = tk.Button(popup,
                         text = "Log In",
                         bg = "green",
                         width = 20,
                         command = login_function)
    login.grid(row = 5, column = 0, columnspan = 2)


window = tk.Tk()
window.title("Felices HO Exam")
window.resizable(False , False)

greet = tk.Label(window,
                 text = "Welcome!",
                 font = ("Arial", 10, "bold"))
greet.grid(row = 0, column = 0)

register_button = tk.Button(window,
                            text = "Register",
                            bg = "blue",
                            width = 30,
                            command = register)
register_button.grid(row = 1, column = 0, pady = 5)

login_button = tk.Button(window,
                            text = "Log In",
                            bg = "green",
                            width = 30,
                            command = LogIn)
login_button.grid(row = 2, column = 0)

window.mainloop()