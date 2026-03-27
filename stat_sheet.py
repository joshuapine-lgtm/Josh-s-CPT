import tkinter as tk

#Create player numbers
Left_team_player_list=[]
Count = 0
Player = input("Enter a player's number from the first team ")
while Count != 5:
    Left_team_player_list.append(Player)
    Count = Count + 1
    if Count != 5:
     Player = input("Enter a different player's number from the first team ")

Right_team_player_list=[]
count = 0
Player = input("Enter a player's number from the second team ")
while count != 5:
    Right_team_player_list.append(Player)
    count = count + 1
    if count != 5:
     Player = input("Enter a different player's number from the second team ")
     
root = tk.Tk()
root.geometry("1200x750")
#Defining Main GUI Functions

start_frame = tk.Frame(root)
main_frame = tk.Frame(root)

start_frame.grid(row=0, column=0, sticky="nsew")
main_frame.grid(row=0, column=0, sticky="nsew")
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
    return new_window
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

#Set everyone's stats to zero and use dictionary to store: 
Left_team_stats = {}

for player in Left_team_player_list:
    Left_team_stats[player] = {"pts": 0,"reb": 0, "assists":0}

def Chose_player(win, player_ind, stat):
    #Uses player's index to find their actual jersey number
    player_num = Left_team_player_list[player_ind]
    t = True
    if stat != "pts":
        Left_team_stats[player_num][stat] += 1
    else:
        while t == True:
        #Accounting for freethrows, midrange, 3-pt shots
            shot = input("1, 2, or 3 pointer? ")
            if shot == "1" or shot == "2" or shot == "3":
                Left_team_stats[player_num][stat] += int(shot)
                t = False
            else: 
                print("Enter either 1, 2, or 3")
    print("Player" + " " + str(player_num) + " " + stat + ": " + str(Left_team_stats[player_num][stat]))
    close_new(win)
    
    
    
#Creates player buttons
def create_player_buttons(new_window,stat):
    Player1_button = tk.Button(new_window, text = Left_team_player_list[0], command=lambda: Chose_player(new_window,0,stat))
    Player2_button = tk.Button(new_window, text = Left_team_player_list[1], command=lambda: Chose_player(new_window,1,stat))
    Player3_button = tk.Button(new_window, text = Left_team_player_list[2], command=lambda: Chose_player(new_window,2,stat))
    Player4_button = tk.Button(new_window, text = Left_team_player_list[3], command=lambda: Chose_player(new_window,3,stat))
    Player5_button = tk.Button(new_window, text = Left_team_player_list[4], command=lambda: Chose_player(new_window,4,stat))
    Player1_button.pack()
    Player2_button.pack()
    Player3_button.pack()
    Player4_button.pack()
    Player5_button.pack()
#Opens interface with player numbers
def open_number_interface(stat):
    new_window = open_new_interface()
    create_player_buttons(new_window,stat)
    
#Create buttons for next interface, but keep hidden
Rebound_button = tk.Button(Left_team, text = "Rebound", command=lambda: open_number_interface("reb"))
Assist_button = tk.Button(Left_team, text = "Assist", command=lambda: open_number_interface("assists"))
Point_button = tk.Button(Left_team, text = "Point", command=lambda: open_number_interface("pts"))
Finish_button = tk.Button(Left_team, text = "Finish", command=lambda: end_program())

#Points have their own listbox
leftpt_listbox = tk.Listbox(Left_team, height=6, width=30)
pt_options = ["1","2","3"]
for options in pt_options:
    leftpt_listbox.insert(tk.END, options)
    
def get_from_leftpt_listbox():
    sel = left_listbox.curselection()
    if not sel:
        return None
    return leftpt_listbox.get(sel[0]).lower()


def applyptselection():
    color = getfromrightlistbox()
    if color:
        Right_team.config(bg=color)

Apply_Button_pt = tk.Button(Left_team, text="Done selecting", command=applyptselection)

#Clear GUI of everything so far (Procedure)

def cleareverything(list):
    for item in list:
        item.destroy()
    if list == firstGUI_list:
        Completed_color_button.destroy()
        
        #Show buttons after click of completed color button
        Rebound_button.pack(side=tk.LEFT)
        Finish_button.pack(side=tk.BOTTOM)
        leftpt_listbox.pack(side=tk.TOP)
        Apply_Button_pt.pack(side=tk.TOP)
    else: 
        something()

firstGUI_list = [Apply_Button_left, left_listbox, right_listbox, Apply_Button_right, Color_label]

Completed_color_button = tk.Button(root, text="Completed Selection", command=lambda:cleareverything(firstGUI_list))
Completed_color_button.grid(row=0, column=1, columnspan=2, pady=10)

root.mainloop()
