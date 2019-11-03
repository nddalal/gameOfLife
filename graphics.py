# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 19:47:40 2019

@author: nihar
"""

from tkinter import *
from cmu_112_graphics import *

import time,random



def appStarted(app):
    app.width, app.height = 10000, 10000
    app.w,app.h= 100, 100
    colors=3
    app.color=set(i for i in range(colors+1))
    app.grid=[[random.randint(0,colors)for j in range(app.w)]for i in range(app.h)]
    app.timerDelay = 100

def bruh(n):
    a=[1,1,1,0,-1,-1,-1,0]
    b=[-1,0,1,1,1,0,-1,-1]
    return (a[n],b[n])

def ruleset(cell,neigh):
    s=set(neigh)
    d=len(s)
    l=[bool(i) for i in neigh]
    n=len(l)
    if cell==0:
        if n>4 or d>3:return 0
        else:return app.color.difference(s).pop()
    else:
        if n>4 or d>3:return 0
        else:return cell

def timerFired(app):
    newgrid=[[0]*app.w for i in range(app.h)]
    for i in range(app.h):
        for j in range(app.w):
            near=[]
            for k in range(8):
                near.append(app.grid[(i+bruh(k)[0])%app.h][(j+bruh(k)[1])%
                                     app.w])
            newgrid[i][j]=ruleset(app.grid[i][j],near)
    app.grid = newgrid
                
def drawBoard(app, canvas): #loops through board and draws cells for row & col
    for row in range(len(app.grid)):
        for col in range(len(app.grid[0])):
            drawCell(app, canvas, row, col)
            


def drawCell(app, canvas, row, col):
    colorList = ['black', 'white', 'blue', 'red']
    cellSize = app.width/len(app.grid) 
    color = colorList [app.grid[row][col]]
    canvas.create_rectangle(col * cellSize, row * cellSize, 
                            (col+1) * cellSize, 
                            (row+1) * cellSize, 
                            fill = color, outline = 'white')
    
def redrawAll(app, canvas):
    drawBoard(app, canvas)
    

runApp(width = 1000, height = 1000)
    
    




