import tkinter as tk
import turtle as trtl

root = tk.Tk()
#Defining Main GUI Functions

root.title("Main interface")
root.geometry("1200x750")

#code from google
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.rowconfigure(1, weight=1)

#Interface creation and deletion defined
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

# Top labels
Color_label = tk.Label(root, text="Enter each team's color:", compound="center",
    font=("times new roman", 14))
Color_label.grid(row=0, column=0, columnspan=2, pady=10)

#split screen in half
Left_team = tk.Frame(root, height=400, width=300)
Right_team = tk.Frame(root, height=400, width=300)

#code from google
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.rowconfigure(1, weight=1)

Left_team.grid(row=1, column=0, sticky="nsew")
Right_team.grid(row=1, column=1, sticky="nsew")

# Put a listbox and apply button inside the left frame
left_listbox = tk.Listbox(Left_team, height=6, width=30)
team_colors = ["green", "red", "blue", "purple", "yellow", "white", "black"]
for colors in team_colors:
    left_listbox.insert(tk.END, colors)
left_listbox.pack(side=tk.LEFT)

# code from google
def getfromleftlistbox():
    sel = left_listbox.curselection()
    if not sel:
        return None
    return left_listbox.get(sel[0]).lower()


def getfromrightlistbox():
    sel = right_listbox.curselection()
    if not sel:
        return None
    return right_listbox.get(sel[0]).lower()

def applyleftcolor():
    color = getfromleftlistbox()
    if color:
        Left_team.config(bg=color)

Apply_Button_left = tk.Button(Left_team, text="Apply Color", command=applyleftcolor)
Apply_Button_left.pack(side=tk.LEFT)

# Put a listbox and apply button inside the right frame
right_listbox = tk.Listbox(Right_team, height=6, width=30)
for colors in team_colors:
    right_listbox.insert(tk.END, colors)
right_listbox.pack(side=tk.RIGHT)

def applyrightcolor():
    color = getfromrightlistbox()
    if color:
        Right_team.config(bg=color)

Apply_Button_right = tk.Button(Right_team, text="Apply Color", command=applyrightcolor)
Apply_Button_right.pack(side=tk.RIGHT)

#Clear GUI of everything so far
def cleareverything():
    for item in firstGUI_list:
        item.destroy()


Completedcolor_button = tk.Button(root, text="Completed Selection", command=cleareverything)
Completedcolor_button.grid(row=0, column=1, columnspan=2, pady=10)

firstGUI_list = [Apply_Button_left, left_listbox, right_listbox, Apply_Button_right, Completedcolor_button, Color_label]

#Actual program


root.mainloop()
