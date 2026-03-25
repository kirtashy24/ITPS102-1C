import tkinter as tk

window = tk.Tk()
window.title("LOG IN WINDOW")
window.config(bg="white")

wc_text = tk.Label(window, text="Welcome!", font = ("Arial", 15, "bold"), anchor = "center")
wc_text.grid(row = 0, column = 5)

def register_window():
    register_window = tk.Toplevel()

    register = tk.Label(register_window, text="Register", font = ("Arial", 15, "bold"), anchor = "center" )
    register.grid(row = 0, column = 0, columnspan = 3)


    user = tk.Label(register_window, text="Username", font = ("Arial", 10))
    user.grid(row = 1, column = 0)

    pw = tk.Label(register_window, text="Password", font = ("Arial", 10))
    pw.grid(row = 2, column = 0)

b_button = tk.Button(window, text = "Register", font = ("Arial", 15, "bold"), bg = "Blue", width = 40, command = register_window)
b_button.grid(row = 1, column = 5, pady = 5)

def login_window():
    register_window = tk.Toplevel()

    register = tk.Label(register_window, text="Log In", font = ("Arial", 15, "bold"), anchor = "center" )
    register.grid(row = 0, column = 0, columnspan = 3)

g_button = tk.Button(window, text = "Log In", font = ("Arial", 15, "bold"), bg = "Green", width = 40, command = login_window)
g_button.grid(row = 2, column = 5, pady = 5)

window.mainloop()