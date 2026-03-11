import tkinter as tk
root = tk.Tk()
#Defining Main GUI Functions

def open_new_interface():
    new_window = tk.Toplevel(root, hight = 200, width = 150)
    new_window.attributes("-zoomed", True)
    new_window.title("New Interface")
    Back_Button = tk.Button(new_window, text="Back",command=lambda: close_new(new_window))
    Back_Button.pack(side = tk.BOTTOM)
 
def close_new(win):
    win.destroy()

def end_program():
    root.destroy()

#GUI
root.title("Main interface")
root.geometry("400x300")

Team_color_list = ["blue", "green", "red", "purple", "white", "black", "yellow"]
Left_team_color = int(input("Choose a team color by inputting the corresponding # (1:blue, 2:green, 3:red, 4:purple, 5:white, 6:black, 7:yellow): "))
Left_team = tk.Frame(root, bg = Team_color_list(Left_team_color), height = 400, width = 350)


Rebound_Button = tk.Button(Left_team, text = "Rebound", command = open_new_interface)
Rebound_Button.pack()

Finish_button = tk.Button(Left_team, text = "Finish", command = end_program)
Finish_button.pack()



#Actual program


root.mainloop()
