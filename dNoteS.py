from tkinter import *
from tkinter import ttk
from PIL import Image
import keyboard
import os

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
		help.title("dNoteS - О программе")
		help.resizable(False, False)
		lb = Label(help, text='dNoteS', fg='#00FF78', font=('Segoe Print', 70)).pack()
		lb1 = Label(help, font=('Arial', 10), text='dNoteS - программма для заметок на рабочем столе\nВерсия 1.0 (02.2021)\n\nPowered by Python 3.8 (tkinter)\n\nОбратная связь:\nGmail - ddxoffi@gmail.com\nTelegram - t.me/ddx_offi/\n\nddx Inc. 2021').pack()
		help.mainloop()

	def hotbabyes():
		hot = Tk()
		hot.resizable(False, False)
		hot.title("Быстрые клавиши")
		lb = Label(hot, font=('Arial', 15), text='Ctrl + (+) - закрепить заметку\nCtrl + (-) - открепить заметку\nAlt + 7 - •\nAlt + 1 - ☺').pack()
		hot.mainloop()
		
	keyboard.add_hotkey('Ctrl + N', start)
	keyboard.add_hotkey('Ctrl + Q', lambda: root.destroy())
	keyboard.add_hotkey('Ctrl + Plus', lambda: root.overrideredirect(True))
	keyboard.add_hotkey('Ctrl + -', lambda: root.overrideredirect(False))
	keyboard.add_hotkey('F1', help)
	keyboard.add_hotkey('F2', hotbabyes)

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

	editmenu = Menu(tearoff=0)
	editmenu.add_command(label='Новая', command=start)
	editmenu.add_checkbutton(label='Закрепить', command=over, variable=var2)
	editmenu.add_checkbutton(label='Всегда впереди', command=top, variable=var)
	editmenu.add_command(label='Заркыть', command=lambda: root.destroy())
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
	root.mainloop()
start() 
