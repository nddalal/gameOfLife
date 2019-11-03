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
    app.w,app.h= 80, 80
    app.colors=4
    app.color=set(i for i in range(app.colors+1))
    app.grid=([[random.randint(0,1)for j in range(app.w//2)] + [2*random.randint(0,1)for j in range(app.w//2)] for i in range(app.h//2)]
    + [[3*random.randint(0,1)for j in range(app.w//2)] + [4*random.randint(0,1)for j in range(app.w//2)] for i in range(app.h//2)])
    app.timerDelay = 50
    app.started = False

def bruh(n):
    a=[1,1,1,0,-1,-1,-1,0]
    b=[-1,0,1,1,1,0,-1,-1]
    return (a[n],b[n])

def ruleset(cell,neigh, app):
    listAlive = [bool(i) for i in neigh]
    numAlive = sum(listAlive)
    colorCounts = [neigh.count(i+1) for i in range(app.colors)]
    if cell==0:
        if numAlive == 3:
            if colorCounts.count(1) == 3:
                return colorCounts.index(0)+1
            else: return colorCounts.index(max(colorCounts))+1
        else:return 0
    else:
        if numAlive<2 or numAlive>3:return 0
        else:return cell
        
def keyPressed(app, event):
    if event.key == 'Space':
        app.started = True

def timerFired(app):
    if app.started == True:
        newgrid=[[0]*app.w for i in range(app.h)]
        for i in range(app.h):
            for j in range(app.w):
                near=[]
                for k in range(8):
                    near.append(app.grid[(i+bruh(k)[0])%app.h][(j+bruh(k)[1])%
                                         app.w])
                newgrid[i][j]=ruleset(app.grid[i][j],near, app)
        app.grid = newgrid
                
def drawBoard(app, canvas): #loops through board and draws cells for row & col
    for row in range(len(app.grid)):
        for col in range(len(app.grid[0])):
            drawCell(app, canvas, row, col)
            


def drawCell(app, canvas, row, col):
    colorList = ['black', 'green', 'yellow', 'red', 'blue']
    cellSize = app.width/len(app.grid) 
    color = colorList[app.grid[row][col]]
    canvas.create_rectangle(col * cellSize, row * cellSize, 
                            (col+1) * cellSize, 
                            (row+1) * cellSize, 
                            fill = color, outline = color)
    
def redrawAll(app, canvas):
    if app.started == True:
        drawBoard(app, canvas)
    else:
        canvas.create_rectangle(0, 0, app.width, app.height, 
                                fill = 'black', outline = 'black')
        canvas.create_text(app.width/2, app.height/2, text = 'Welcome to Quad Life', 
                           font = 'Arial 36 bold',fill = 'white')
        canvas.create_text(app.width/2, app.height/2 + 80 , text = 'Press Space to Start', 
                           font = 'Arial 24',fill = 'white')


runApp(width = 2000, height = 2000)
    
    