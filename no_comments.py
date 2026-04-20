import tkinter as tk

for _ in range (20):
    print (" ")

Left_team_player_list=[]
Count = 0
Player = input("Enter a player's number from the first team ")
while Count < 5:
    Left_team_player_list.append(Player)
    Count = Count + 1
    if Count != 5:
        Player = input("Enter a different player's number from the first team ")

Right_team_player_list=[]
count = 0
Player = input("Enter a player's number from the second team ")
while count < 5:
    Right_team_player_list.append(Player)
    count = count + 1
    if count != 5:
        Player = input("Enter a different player's number from the second team ")

root = tk.Tk()
root.geometry("1200x750")

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.rowconfigure(1, weight=1)

def open_new_interface():
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

Color_label = tk.Label(root, text="Enter each team's color:", compound="center",
font=("times new roman", 14))
Color_label.grid(row=0, column=0, columnspan=2, pady=10)

Left_team = tk.Frame(root, height=400, width=300)
Right_team = tk.Frame(root, height=400, width=300)
Left_team.grid(row=1, column=0, sticky="nsew")
Right_team.grid(row=1, column=1, sticky="nsew")

left_listbox = tk.Listbox(Left_team, height=6, width=30)
team_colors = ["green", "red", "blue", "purple", "yellow", "white", "black"]
for colors in team_colors:
    left_listbox.insert(tk.END, colors)
left_listbox.pack(side=tk.LEFT)

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

Left_team_stats = {}

for player in Left_team_player_list:
    Left_team_stats[player] = {"pts": 0,"reb": 0, "assists":0}

Right_team_stats = {}

for player in Right_team_player_list:
    Right_team_stats[player] = {"pts": 0, "reb": 0, "assists": 0}

def Choose_player(win, team, player_ind, stat, points):
    if team == "left":
        player_num = Left_team_player_list[player_ind]
        stats_dict = Left_team_stats
    else:
        player_num = Right_team_player_list[player_ind]
        stats_dict = Right_team_stats

    if stat != "pts":
        stats_dict[player_num][stat] += 1
    elif points is not None:
        stats_dict[player_num][stat] += int(points)

    print("Player", player_num, stat + ":", stats_dict[player_num][stat])
    close_new(win)

def create_player_buttons(new_window, team, stat, points):
    num_of_players = 5

    if team == "left":
        player_list = Left_team_player_list
    else:
        player_list = Right_team_player_list

    for i in range(num_of_players):
        btn = tk.Button(new_window, text=player_list[i],
                        command=lambda i=i: Choose_player(new_window, team, i, stat, points))
        btn.pack()

def open_number_interface(team,stats,points):
    new_window = open_new_interface()
    create_player_buttons(new_window,team,stats,points)

Rebound_button = tk.Button(Left_team, text = "Rebound", command=lambda: open_number_interface("left", "reb", 0))
Assist_button = tk.Button(Left_team, text = "Assist", command=lambda: open_number_interface("left", "assists", 0))
Finish_button = tk.Button(Left_team, text = "Finish", command=lambda: end_program())

Rebound_button_R = tk.Button(Right_team, text="Rebound",command=lambda: open_number_interface("right", "reb", 0))
Assist_button_R = tk.Button(Right_team, text="Assist",command=lambda: open_number_interface("right", "assists", 0))

leftpt_listbox = tk.Listbox(Left_team, height=3, width=30)
pt_options = ["1","2","3"]
for options in pt_options:
    leftpt_listbox.insert(tk.END, options)

def get_from_leftpt_listbox():
    sel = leftpt_listbox.curselection()
    if not sel:
        return None
    return leftpt_listbox.get(sel[0]).lower()

def applyptselection():
    points = get_from_leftpt_listbox()
    open_number_interface("left","pts", points)

rightpt_listbox = tk.Listbox(Right_team, height=3, width=30)
for options in pt_options:
    rightpt_listbox.insert(tk.END, options)

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

def cleareverything(list):
    for item in list:
        item.destroy()
    if list == firstGUI_list:
        Completed_color_button.destroy()

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
        Stat_sheet_btn.destroy()
        show_stat_sheet()

firstGUI_list = [Apply_Button_left, left_listbox, right_listbox, Apply_Button_right, Color_label]
secondGUI_list = [Rebound_button, Assist_button, Finish_button, leftpt_listbox,
Apply_Button_pt, Rebound_button_R, Assist_button_R, rightpt_listbox, Apply_Button_pt_R]

Completed_color_button = tk.Button(root, text="Completed Selection",
command=lambda:cleareverything(firstGUI_list))
Completed_color_button.grid(row=0, column=1, columnspan=2, pady=10)

Stat_sheet_btn = tk.Button(Left_team, text = "Show Final Stats (not reversible)",
command=lambda:cleareverything(secondGUI_list))

def show_stat_sheet():
    stat_window = tk.Toplevel(root)
    stat_window.geometry("1000x300")

    canvas = tk.Canvas(stat_window, width=1000, height=300)
    canvas.pack(fill="both", expand=True)

    bg_image = None
    try:
        bg_image = tk.PhotoImage(file="Stat_sheet_paper.png")
        stat_window.bg_image = bg_image
        canvas.create_image(0, 0, image=bg_image, anchor="nw")
        canvas.create_image(500, 0, image=bg_image, anchor="nw")
    except:
        pass

    start_y = 77
    row_spacing = 36

    for i, player in enumerate(Left_team_player_list):
        y = start_y + i * row_spacing
        stats = Left_team_stats[player]

        canvas.create_text(20, y, text=player, font=("Arial", 12, "bold"))
        canvas.create_text(120, y, text=stats["pts"], font=("Arial", 12))
        canvas.create_text(260, y, text=stats["reb"], font=("Arial", 12))
        canvas.create_text(380, y, text=stats["assists"], font=("Arial", 12))

    for i, player in enumerate(Right_team_player_list):
        y = start_y + i * row_spacing
        stats = Right_team_stats[player]

        canvas.create_text(520, y, text=player, font=("Arial", 12, "bold"))
        canvas.create_text(620, y, text=stats["pts"], font=("Arial", 12))
        canvas.create_text(760, y, text=stats["reb"], font=("Arial", 12))
        canvas.create_text(880, y, text=stats["assists"], font=("Arial", 12))

root.mainloop()