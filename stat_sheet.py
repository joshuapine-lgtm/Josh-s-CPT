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

#Create main window

#Create main window
root = tk.Tk()
root.geometry("1200x750")


#Defining Main GUI Functions
start_frame = tk.Frame(root)
main_frame = tk.Frame(root)

#Code from chatGPT to configure grid and frames
#Code from chatGPT to configure grid and frames
start_frame.grid(row=0, column=0, sticky="nsew")
main_frame.grid(row=0, column=0, sticky="nsew")
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.rowconfigure(1, weight=1)
#Chatgpt code end
#Chatgpt code end

#Interface creation and deletion defined
def open_new_interface():
    new_window = tk.Toplevel(root)
    new_window.geometry("450x200")
    new_window.title("New Interface")
    Back_Button = tk.Button(new_window, text="Back", command=lambda: close_new(new_window))
    Back_Button.pack(side=tk.BOTTOM)
    return new_window

#Close wanted window

#Close wanted window
def close_new(win):
    win.destroy()
     
#End program
     
#End program
def end_program():
    root.destroy()

# Top labels
Color_label = tk.Label(root, text="Enter each team's color:", compound="center",
    font=("times new roman", 14))
Color_label.grid(row=0, column=0, columnspan=2, pady=10)

#split screen in half
Left_team = tk.Frame(root, height=400, width=300)
Right_team = tk.Frame(root, height=400, width=300)

#Code from chatGPT to configure grid and frames
#Code from chatGPT to configure grid and frames
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.rowconfigure(1, weight=1)
Left_team.grid(row=1, column=0, sticky="nsew")
Right_team.grid(row=1, column=1, sticky="nsew")
#Chatgpt code end
#Chatgpt code end

# Put a listbox and apply button inside the left frame
left_listbox = tk.Listbox(Left_team, height=6, width=30)
team_colors = ["green", "red", "blue", "purple", "yellow", "white", "black"]
for colors in team_colors:
    left_listbox.insert(tk.END, colors)
left_listbox.pack(side=tk.LEFT)

#GUI project code
#GUI project code
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
#GUI project code end
#GUI project code end

#Apply color selected in left listbox
#Apply color selected in left listbox
def applyleftcolor():
    color = getfromleftlistbox()
    if color:
        Left_team.config(bg=color)

Apply_Button_left = tk.Button(Left_team, text="Apply Color", command=applyleftcolor)
Apply_Button_left.pack(side=tk.LEFT)

#Put a listbox and apply button inside the right frame
#Put a listbox and apply button inside the right frame
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

#Chat gpt code to create dictionaries to store stats
#Chat gpt code to create dictionaries to store stats
Left_team_stats = {}

for player in Left_team_player_list:
    Left_team_stats[player] = {"pts": 0,"reb": 0, "assists":0}

Right_team_stats = {}

for player in Right_team_player_list:
    Right_team_stats[player] = {"pts": 0, "reb": 0, "assists": 0}
#Chat gpt code end

#Function to update stats when player is chosen on chosen stat (Procedure)
def Chose_player(win, team, player_ind, stat, points):
    if team == "left":
        #Uses player index to get actual player number and determines team dictionary to update
        player_num = Left_team_player_list[player_ind]
        stats_dict = Left_team_stats
    else:
        player_num = Right_team_player_list[player_ind]
        stats_dict = Right_team_stats

Right_team_stats = {}

for player in Right_team_player_list:
    Right_team_stats[player] = {"pts": 0, "reb": 0, "assists": 0}
#Chat gpt code end

#Function to update stats when player is chosen on chosen stat (Procedure)
def Chose_player(win, team, player_ind, stat, points):
    if team == "left":
        #Uses player index to get actual player number and determines team dictionary to update
        player_num = Left_team_player_list[player_ind]
        stats_dict = Left_team_stats
    else:
        player_num = Right_team_player_list[player_ind]
        stats_dict = Right_team_stats

    if stat != "pts":
        stats_dict[player_num][stat] += 1
        stats_dict[player_num][stat] += 1
    else:
        stats_dict[player_num][stat] += int(points)
    #Prints out updated stats so user can always have a backup of the stats
    print("Player", player_num, stat + ":", stats_dict[player_num][stat])
        stats_dict[player_num][stat] += int(points)
    #Prints out updated stats so user can always have a backup of the stats
    print("Player", player_num, stat + ":", stats_dict[player_num][stat])
    close_new(win)

#Creates player buttons (Procedure)
def create_player_buttons(new_window, team, stat, points):
    num_of_players = 5
    #Determines team amd creates buttons that co
    if team == "left":
        player_list = Left_team_player_list
    else:
        player_list = Right_team_player_list
    #Creates 5 buttons for each player and uses 5 as per the number of player in the game on a basketball team
    for i in range(num_of_players):
        #i=i makes it so each lambda function has its own copy of i, so the buttons won't each be the last player in the list (as it finishes iterating through the loop before being pressed)
        btn = tk.Button(new_window,text=player_list[i],command=lambda i=i: Chose_player(new_window, team, i, stat, points))
        btn.pack()
#Creates player buttons (Procedure)
def create_player_buttons(new_window, team, stat, points):
    num_of_players = 5
    #Determines team amd creates buttons that co
    if team == "left":
        player_list = Left_team_player_list
    else:
        player_list = Right_team_player_list
    #Creates 5 buttons for each player and uses 5 as per the number of player in the game on a basketball team
    for i in range(num_of_players):
        #i=i makes it so each lambda function has its own copy of i, so the buttons won't each be the last player in the list (as it finishes iterating through the loop before being pressed)
        btn = tk.Button(new_window,text=player_list[i],command=lambda i=i: Chose_player(new_window, team, i, stat, points))
        btn.pack()
#Opens interface with player numbers
def open_number_interface(team,stats,points):
    new_window = open_new_interface() 
    create_player_buttons(new_window,team,stats,points)
def open_number_interface(team,stats,points):
    new_window = open_new_interface() 
    create_player_buttons(new_window,team,stats,points)
    
#Left team stat buttons defined but not packed so they are hidden until color selection is done
Rebound_button = tk.Button(Left_team, text = "Rebound", command=lambda: open_number_interface("left", "reb", 0))
Assist_button = tk.Button(Left_team, text = "Assist", command=lambda: open_number_interface("left", "assists", 0))
#Left team stat buttons defined but not packed so they are hidden until color selection is done
Rebound_button = tk.Button(Left_team, text = "Rebound", command=lambda: open_number_interface("left", "reb", 0))
Assist_button = tk.Button(Left_team, text = "Assist", command=lambda: open_number_interface("left", "assists", 0))
Finish_button = tk.Button(Left_team, text = "Finish", command=lambda: end_program())

#Right team stat buttons defined but not packed so they are hidden until color selection is done
Rebound_button_R = tk.Button(Right_team, text="Rebound",command=lambda: open_number_interface("right", "reb", 0))
Assist_button_R = tk.Button(Right_team, text="Assist",command=lambda: open_number_interface("right", "assists", 0))

#Points have their own listbox to account for freethrows, middys, and threes
#Right team stat buttons defined but not packed so they are hidden until color selection is done
Rebound_button_R = tk.Button(Right_team, text="Rebound",command=lambda: open_number_interface("right", "reb", 0))
Assist_button_R = tk.Button(Right_team, text="Assist",command=lambda: open_number_interface("right", "assists", 0))

#Points have their own listbox to account for freethrows, middys, and threes
leftpt_listbox = tk.Listbox(Left_team, height=3, width=30)
pt_options = ["1","2","3"]
for options in pt_options:
    leftpt_listbox.insert(tk.END, options)

#Code from GUI project to get points from listbox and apply to player stats

#Code from GUI project to get points from listbox and apply to player stats
def get_from_leftpt_listbox():
    sel = leftpt_listbox.curselection()
    if not sel:
        return None
    return leftpt_listbox.get(sel[0]).lower()

def applyptselection():
    points = get_from_leftpt_listbox()
    open_number_interface("left","pts", points)
    open_number_interface("left","pts", points)

#Points have their own listbox to account for freethrows, middys, and threes
rightpt_listbox = tk.Listbox(Right_team, height=3, width=30)
for options in pt_options:
    rightpt_listbox.insert(tk.END, options)

#Code from GUI project to get points from listbox and apply to player stats
def get_from_rightpt_listbox():
    sel = rightpt_listbox.curselection()
    if not sel:
        return None
    return rightpt_listbox.get(sel[0]).lower()

def applyptselection_right():
    points = get_from_rightpt_listbox()
    open_number_interface("right", "pts", points)

Apply_Button_pt_R = tk.Button(Right_team, text="Done selecting points", command=applyptselection_right)
#Points have their own listbox to account for freethrows, middys, and threes
rightpt_listbox = tk.Listbox(Right_team, height=3, width=30)
for options in pt_options:
    rightpt_listbox.insert(tk.END, options)

#Code from GUI project to get points from listbox and apply to player stats
def get_from_rightpt_listbox():
    sel = rightpt_listbox.curselection()
    if not sel:
        return None
    return rightpt_listbox.get(sel[0]).lower()

def applyptselection_right():
    points = get_from_rightpt_listbox()
    open_number_interface("right", "pts", points)

Apply_Button_pt_R = tk.Button(Right_team, text="Done selecting points", command=applyptselection_right)
Apply_Button_pt = tk.Button(Left_team, text="Done selecting points", command=applyptselection)

#Clear GUI of everything so far
#Clear GUI of everything so far
def cleareverything(list):
    for item in list:
        item.destroy()
    if list == firstGUI_list:
        Completed_color_button.destroy()
        
        #Show buttons after click of completed color button
        leftpt_listbox.pack(side=tk.TOP)
        Apply_Button_pt.pack(side=tk.TOP)
        Assist_button.pack(side=tk.TOP)
        Rebound_button.pack(side=tk.TOP)
        Stat_sheet_btn.pack(side=tk.BOTTOM)
        Finish_button.pack(side=tk.BOTTOM)
        rightpt_listbox.pack(side=tk.TOP)
        Apply_Button_pt_R.pack(side=tk.TOP)
        Assist_button_R.pack(side=tk.TOP)
        Rebound_button_R.pack(side=tk.TOP)
    else:
        #Show final stat sheet and destroy button
        Stat_sheet_btn.destroy()
        show_stat_sheet()
        Stat_sheet_btn.pack(side=tk.BOTTOM)
        Finish_button.pack(side=tk.BOTTOM)
        rightpt_listbox.pack(side=tk.TOP)
        Apply_Button_pt_R.pack(side=tk.TOP)
        Assist_button_R.pack(side=tk.TOP)
        Rebound_button_R.pack(side=tk.TOP)
    else:
        #Show final stat sheet and destroy button
        Stat_sheet_btn.destroy()
        show_stat_sheet()

#Lists to determine which buttons to clear when either completed color selection or show stat sheet button is pressed
#Lists to determine which buttons to clear when either completed color selection or show stat sheet button is pressed
firstGUI_list = [Apply_Button_left, left_listbox, right_listbox, Apply_Button_right, Color_label]
secondGUI_list = [Rebound_button, Assist_button, Finish_button, leftpt_listbox, Apply_Button_pt]
    
secondGUI_list = [Rebound_button, Assist_button, Finish_button, leftpt_listbox, Apply_Button_pt]
    
Completed_color_button = tk.Button(root, text="Completed Selection", command=lambda:cleareverything(firstGUI_list))
Completed_color_button.grid(row=0, column=1, columnspan=2, pady=10)

#Final Stats
Stat_sheet_btn = tk.Button(Left_team, text = "Show Final Stats (not reversible)", command=lambda:cleareverything(secondGUI_list))

def show_stat_sheet():
    stat_window = tk.Toplevel(root)
    stat_window.geometry("1000x300")

    #Chat GPT code to add background image and also create canvas to put stats on top of background image
    bg_image = tk.PhotoImage(file="Stat_sheet_paper.png") 
    stat_window.bg_image = bg_image  # keep reference

    canvas = tk.Canvas(stat_window, width=1000, height=300)
    canvas.pack(fill="both", expand=True)

    canvas.create_image(0, 0, image=bg_image, anchor="nw")
    canvas.create_image(500, 0, image=bg_image, anchor="nw")  
    #Chat GPT code end
    
    #Start y position for first player to be in stat sheet image box
    start_y = 77
    #Spacing between each player row so they are evenly spaced in the stat sheet image box
    row_spacing = 36   

    #Chat GPT code to loop through player lists and create text on canvas for each player's stats in the correct position on the stat sheet image
    for i, player in enumerate(Left_team_player_list):
        y = start_y + i * row_spacing

        stats = Left_team_stats[player]

        # Player number
        canvas.create_text(20, y, text=player, font=("Arial", 12, "bold"))

        # Points
        canvas.create_text(120, y, text=stats["pts"], font=("Arial", 12))

        # Rebounds
        canvas.create_text(260, y, text=stats["reb"], font=("Arial", 12))

        # Assists
        canvas.create_text(380, y, text=stats["assists"], font=("Arial", 12))

    for i, player in enumerate(Right_team_player_list):
        y = start_y + i * row_spacing

        stats = Right_team_stats[player]

        # Player number
        canvas.create_text(520, y, text=player, font=("Arial", 12, "bold"))

        # Points
        canvas.create_text(620, y, text=stats["pts"], font=("Arial", 12))

        # Rebounds
        canvas.create_text(760, y, text=stats["reb"], font=("Arial", 12))

        # Assists
        canvas.create_text(880, y, text=stats["assists"], font=("Arial", 12))
#Chat GPT code end

root.mainloop()
