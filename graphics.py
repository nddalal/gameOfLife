# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 19:47:40 2019

@author: nihar
"""

from tkinter import *


gameOfLifeTest = [['black']*50 for i in range(50)]

def drawBoard(canvas, width, height, gameOfLife): #loops through board and draws cells for row & col
    for row in range(len(gameOfLife)):
        for col in range(len(gameOfLife[0])):
            drawCell(canvas, width, height, gameOfLife, row, col)

def drawCell(canvas, width, height, gameOfLife, row, col):
    cellSize = width/len(gameOfLife) 
    color = gameOfLife[row][col],
    canvas.create_rectangle(col * cellSize, row * cellSize, 
                            (col+1) * cellSize, 
                            (row+1) * cellSize, 
                            fill = color, outline = 'white')


width = 1000
height = 1000    
root = Tk()
root.resizable(width=False, height=False) # non-resizable
canvas = Canvas(root, width=width, height=height)
canvas.configure(bd=0, highlightthickness=0)
canvas.pack()
drawBoard(canvas, width, height, gameOfLifeTest)
root.mainloop()
