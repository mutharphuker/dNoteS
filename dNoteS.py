from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showerror, showinfo
from PIL import Image
import keyboard
import json
import os

with open("lang.json", "r", encoding="utf-8") as file:
	lng = json.load(file)
if lng['current'] == "eng":
	lang = lng['eng']
elif lng['current'] == "rus":
	lang = lng['rus']
elif lng['current'] == "uzb":
	lang = lng['uzb']

def start():
	root = Tk()
	root.title("dNoteS")
	root.geometry("250x300")
	root.iconbitmap('icons\\icon.ico')
	root.attributes('-toolwindow', True)

	text = Text(root, width=250, height=300, bg='#FDF78E', font=("Segoe Print", 18), selectbackground='black', bd=0, wrap=WORD)
	text.pack() 

	def help():
		help = Tk()
		help.geometry("400x360")
		help.title(lang[0])
		help.resizable(False, False)
		lb = Label(help, text='dNoteS', fg='#00FF78', font=('Segoe Print', 70)).pack()
		lb1 = Label(help, font=('Arial', 10), text=lang[1]).pack()
		help.mainloop()
		
	keyboard.add_hotkey('Ctrl + N', start)
	keyboard.add_hotkey('Ctrl + Q', lambda: root.destroy())
	keyboard.add_hotkey('Ctrl + Plus', lambda: root.overrideredirect(True))
	keyboard.add_hotkey('Ctrl + -', lambda: root.overrideredirect(False))
	keyboard.add_hotkey('F1', help)

	yellow = PhotoImage(file='icons\\yellow.png')
	blue = PhotoImage(file='icons\\blue.png')
	green = PhotoImage(file='icons\\green.png')
	white = PhotoImage(file='icons\\white.png')

	var = BooleanVar()
	var2 = BooleanVar()
	def top():
		if var.get():
			root.attributes('-topmost', True)
		else:
			root.attributes('-topmost', False)
	def over():
		if var2.get():
			root.overrideredirect(True)
		else:
			root.overrideredirect(False)	

	def language(which):
		lng['current'] = which
		with open("lang.json", "w", encoding="utf-8") as file:
			json.dump(lng, file)
		showinfo(message=lang[7])

	langmenu = Menu(tearoff=0)
	langmenu.add_command(label='English', command=lambda: language("eng"))
	langmenu.add_command(label='Русский', command=lambda: language("rus"))
	langmenu.add_command(label='O`zbekcha', command=lambda: language("uzb"))

	editmenu = Menu(tearoff=0)
	editmenu.add_command(label=lang[2], accelerator='Ctrl + N', command=start)
	editmenu.add_checkbutton(label=lang[3], accelerator='Ctrl + (+)', command=over, variable=var2)
	editmenu.add_checkbutton(label=lang[4], command=top, variable=var)
	editmenu.add_cascade(label=lang[5], menu=langmenu)
	editmenu.add_command(label=lang[6], accelerator='Ctrl + Q', command=lambda: root.destroy())
	editmenu.add_separator()
	editmenu.add_command(image=yellow, command=lambda: text.config(bg='#FDF78E'))
	editmenu.add_command(image=blue, command=lambda: text.config(bg='#69afff'))
	editmenu.add_command(image=green, command=lambda: text.config(bg='#29ffa6'))
	editmenu.add_command(image=white, command=lambda: text.config(bg='white'))

	x = 0
	y = 0
	def popup(event):
	    global x, y
	    x = event.x
	    y = event.y
	    editmenu.post(event.x_root, event.y_root)
	text.bind("<Button-3>", popup)
	def hotkeys(event):
		if event.keycode==86:
			event.widget.event_generate("<<Paste>>")
		if event.keycode==67: 
			event.widget.event_generate("<<Copy>>")    
		if event.keycode==88: 
			event.widget.event_generate("<<Cut>>")
		if event.keycode==65: 
			event.widget.event_generate("<<SelectAll>>")
	text.bind("<Control-KeyPress>", hotkeys)
	root.mainloop()
start() 
