import os
import tkinter as tk
from tkinter import ttk

def getSRCDir(): #dapatkan directory ke folder src di repository ini
    currDir = os.getcwd()
    parentDir = os.path.dirname(currDir)
    while "src" not in os.listdir(parentDir):
        parentDir = os.path.dirname(parentDir)

    return parentDir+"\src"

def createGeneralLabelPack(teks: str, frame): #membuat label baru
    newLabel =ttk.Label(frame,text=teks)
    newLabel.pack(padx=5,pady=5,fill="x",expand=True)

def createGeneralEntryPack(frame,txtVar): #membuat entry baru
    newEntry = ttk.Entry(frame,textvariable=txtVar)
    newEntry.pack(padx=5,pady=5,fill="x",expand=True)

def createControlPointInput(frame,X_VAR,Y_VAR,idx):
    Label = ttk.Label(frame,text="Titik Kontrol P"+str(idx))
    Label.pack(padx=5,pady=5,fill="x",expand=True)
    XLabel = ttk.Label(frame,text="Nilai X: ")
    XLabel.pack(padx=5,pady=5,fill="x",expand=True)
    XEntry = ttk.Entry(frame,textvariable=X_VAR)
    XEntry.pack(padx=5,pady=5,fill="x",expand=True)
    YLabel = ttk.Label(frame,text="Nilai Y: ")
    YLabel.pack(padx=5,pady=5,fill="x",expand=True)
    YEntry = ttk.Entry(frame,textvariable=Y_VAR)
    YEntry.pack(padx=5,pady=5,fill="x",expand=True)

def createControlPointOutput(frame,teks,xVal,yVal):
    P0LabelOutput = ttk.Label(frame,text = teks)
    P0LabelOutput.pack(padx=5,pady=5,fill="x",expand=True)
    P0XLabelOutput = ttk.Label(frame,text = "X: " + str(xVal))
    P0XLabelOutput.pack(padx=5,pady=5,fill="x",expand=True)
    P0YLabelOutput = ttk.Label(frame,text = "Y: " + str(yVal))
    P0YLabelOutput.pack(padx=5,pady=5,fill="x",expand=True)