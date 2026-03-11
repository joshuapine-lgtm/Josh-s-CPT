import tkinter as tk
import turtle as trtl

root = tk.Tk()
#Defining Main GUI Functions

def open_new_interface():
    # create a simple new window
    new_window = tk.Toplevel(root)
    new_window.geometry("450x200")
    new_window.title("New Interface")
    Back_Button = tk.Button(new_window, text="Back", command=lambda: close_new(new_window))
    Back_Button.pack(side=tk.BOTTOM)
 
def close_new(win):
    win.destroy()

def end_program():
    root.destroy()

#GUI
root.title("Main interface")
root.geometry("1200x750")
Color_label = tk.Label(root, text="Enter left team's color: ",  compound="center",
    font=("times new roman", 14), bd=0, relief=tk.FLAT,)
Color_label.pack(side=tk.LEFT)
listbox = tk.Listbox(root, height = 6, width = 50)
team_colors = ["green", "red", "blue", "purple", "yellow","white", "black"]
for colors in team_colors:
    listbox.insert(tk.END, colors)
listbox.pack(side = tk.LEFT)

# code from google
def getfromlistbox():
    sel = listbox.curselection()
    if not sel:
        return None
    return listbox.get(sel[0]).lower()

# Function to update color
def apply_color():
    color = getfromlistbox()
    if color:
        Left_team.config(bg=color)
        root.config(bg=color)

Left_team = tk.Frame(root, bg = getfromlistbox(), height = 400, width = 350)
Left_team.pack(side=tk.LEFT, padx=40) 

Apply_Button = tk.Button (Left_team, text = "Apply Color", command = apply_color)
Apply_Button.pack(side=tk.LEFT, padx=10)

Rebound_Button = tk.Button(Left_team, text = "Rebound", command = open_new_interface)
Rebound_Button.pack()

Finish_button = tk.Button(Left_team, text = "Finish", command = end_program)
Finish_button.pack()



#Actual program


root.mainloop()
