import tkinter as tk

#GUI
root =tk.Tk()
root.title = ("Main interface")
frame = tk.Frame(root)
root.attributes('-fullscreen', True)
frame.pack()
def open_new_interface():
    new_window = tk.Toplevel(root)
    new_window.title ("New Interface")
    Back_Button = tk.Button(new_window, text = "Back", command = close_window)
    Back_Button.pack()
def close_window():
    root.destroy()
Rebound_Button = tk.Button(root, text = "Rebound", command = open_new_interface)
Rebound_Button.pack()

Finish_button = tk.Button(root, text = "Finish", command = close_window)
Finish_button.pack()

#Actual program


root.mainloop()
