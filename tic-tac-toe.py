#!/usr/bin/python3

from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *
from random import randint
import functools

#=====================[ Variables ]=====================#
ActivePlayer = 1
p1 = [] # what player1 selected
p2 = [] # what player2 selected
win = False
draw = False
count = 0

#=====================[ Window Config ]=====================#
root = Tk()
root.title('Tic Tac Toe: Player 1')
style = Style()
style.theme_use('classic')

#=====================[ Game Boxes ]=====================#
buttons = dict()
n = 0

def BuClick(id):
	global ActivePlayer
	global p1, p2
	global win, count
	count += 1
	if ActivePlayer == 1:
		SetLayout(id, 'X')
		root.title('Tic Tac Toe: Player 2')
		p1.append(id)
		ActivePlayer = 2
		print('P1:{}'.format(p1))
		CheckWinner()
		if (not win) and (not draw):
			AutoPlay()
	elif ActivePlayer == 2:
		SetLayout(id, 'O')
		root.title('Tic Tac Toe: Player 1')
		p2.append(id)
		ActivePlayer = 1
		print('P2:{}'.format(p2))
		CheckWinner()

for i in range(9):
	x = int(i/3)
	y = i%3
	buttons[i] = Button(root, text=' ')
	buttons[i].grid(row=x, column=y, sticky='snew', ipadx=40, ipady=40)
	buttons[i].config(command=functools.partial(BuClick, i+1))

#=====================[ Print Layout ]=====================#
def SetLayout(id, text):
	id = id - 1
	if id in buttons.keys():
		b = buttons[id]
		b.config(text=text)
		b.state(['disabled'])

#=====================[ Check Winner ]=====================#
def CheckWinner():
	global p1, p2
	global count, win
	global draw
	winner = False
	if (1 in p1 and 2 in p1 and 3 in p1) or (4 in p1 and 5 in p1 and 6 in p1) or (7 in p1 and 8 in p1 and 9 in p1) or (1 in p1 and 5 in p1 and 9 in p1) or (3 in p1 and 5 in p1 and 7 in p1) or (1 in p1 and 4 in p1 and 7 in p1) or (2 in p1 and 5 in p1 and 8 in p1) or (3 in p1 and 6 in p1 and 9 in p1):
		winner = 1
	elif (1 in p2 and 2 in p2 and 3 in p2) or (4 in p2 and 5 in p2 and 6 in p2) or (7 in p2 and 8 in p2 and 9 in p2) or (1 in p2 and 5 in p2 and 9 in p2) or (3 in p2 and 5 in p2 and 7 in p2) or (1 in p2 and 4 in p2 and 7 in p2) or (2 in p2 and 5 in p2 and 8 in p2) or (3 in p2 and 6 in p2 and 9 in p2):
		winner = 2
	if winner:
		showinfo(title='Congratulations!', message=f'Player {winner} wins')
		win = True
		root.destroy()
	else:
		if not win and count == 9:
			showinfo(title='Title', message='Draw!')
			draw = True
			root.destroy()

# #=====================[ Robot ]=====================#

def AutoPlay():
	global p1, p2
	EmptyCells = []
	for cell in range(1,10):
		if (not cell in p1) and (not cell in p2):
			EmptyCells.append(cell)
	RandIndex = randint(0, len(EmptyCells)-1)
	BuClick(EmptyCells[RandIndex])

root.mainloop()