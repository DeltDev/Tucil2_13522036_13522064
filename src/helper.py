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
    