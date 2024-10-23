# This program aim's to help auto-format award write-ups for the Coast Guard. Ideally, I will be able to use the ground work here for the Navy.

import tkinter as tk

root = tk.Tk()


frame = tk.Frame(root)
frame.pack()

menuButton = tk.Menubutton(root, text="Menu Button")
menuButton.pack()

menu = tk.Menu(menuButton, tearoff=0)
menu.add_command(label="Option 1")
menu.add_command(label="Option 2")
menuButton.config(menu=menu)

label = tk.Label(root, text="This is my Label")
label.pack()

entry = tk.Entry(root, width=50)
entry.pack()

button = tk.Button(root, text="This is a Button")
button.pack()

check_button = tk.Checkbutton(root, text="This is a Checkbutton")
check_button.pack()

radio_button = tk.Radiobutton(root, text="This is a radio button")
radio_button.pack()

selected_option = tk.StringVar(root)
selected_option.set("Option 1")

option_menu = tk.OptionMenu(root, selected_option, "Option 1", "Option 2", "Option 3")
option_menu.pack()

frame2 = tk.Frame(root)
frame2.pack()

newButton = tk.Menubutton(root, text="Second Menu Button")
newButton.pack()

newMenu = tk.Menu(newButton, tearoff=0)
newMenu.add_command(label="Choice 1")
newMenu.add_radiobutton(label="Double Choice")
newButton.config(menu=newMenu)

list_box = tk.Listbox(frame2)

root.mainloop()
