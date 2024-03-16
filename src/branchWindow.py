import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msgbox
import BezierFormulas as Bezier
from point import Point
from matplotlib import pyplot as plt
from visualizer import spawnPygame
import pygame
import time
def disable_close_window(): #matikan fungsi tombol close default
    pass
def spawnInfoWindow(P0_X,P0_Y,P1_X,P1_Y,P2_X,P2_Y,ITERATION,root):
    
    try: #handling kevalidan input pada entry
        p0x = float(P0_X.get()) #jangan lupa diganti
        p0y = float(P0_Y.get())
        p1x = float(P1_X.get())
        p1y = float(P1_Y.get())
        p2x = float(P2_X.get())
        p2y = float(P2_Y.get())
        it = int(ITERATION.get())
        
    except ValueError: #keluarkan pesan error jika input tidak valid
        msgbox.showerror("Program Error", "Input Anda tidak valid! \n Silahkan ulangi input data Anda.")
        return        
    #setup window kedua
    root.withdraw()
    newWindow = tk.Toplevel(root)
    newWindow.title("Window baru")
    newWindow.config(bg = "gray")
    newWindow.protocol("WM_DELETE_WINDOW", disable_close_window)
    #setup frame output
    newWindowFrame = ttk.Frame(newWindow)
    newWindowFrame.pack(padx=5,pady=5,fill="x",expand=True)
    #label output data titik P0
    P0LabelOutput = ttk.Label(newWindowFrame,text = "Titik P0")
    P0LabelOutput.pack(padx=5,pady=5,fill="x",expand=True)
    P0XLabelOutput = ttk.Label(newWindowFrame,text = "X: " + str(p0x))
    P0XLabelOutput.pack(padx=5,pady=5,fill="x",expand=True)
    P0YLabelOutput = ttk.Label(newWindowFrame,text = "Y: " + str(p0y))
    P0YLabelOutput.pack(padx=5,pady=5,fill="x",expand=True)
    #Label output data titik P1
    P1LabelOutput = ttk.Label(newWindowFrame,text = "Titik P1")
    P1LabelOutput.pack(padx=5,pady=5,fill="x",expand=True)
    P1XLabelOutput = ttk.Label(newWindowFrame,text = "X: " + str(p1x))
    P1XLabelOutput.pack(padx=5,pady=5,fill="x",expand=True)
    P1YLabelOutput = ttk.Label(newWindowFrame,text = "Y: " + str(p1y))
    P1YLabelOutput.pack(padx=5,pady=5,fill="x",expand=True)
    #Label output data titik P2
    P2LabelOutput = ttk.Label(newWindowFrame,text = "Titik P2")
    P2LabelOutput.pack(padx=5,pady=5,fill="x",expand=True)
    P2XLabelOutput = ttk.Label(newWindowFrame,text = "X: " + str(p2x))
    P2XLabelOutput.pack(padx=5,pady=5,fill="x",expand=True)
    P2YLabelOutput = ttk.Label(newWindowFrame,text = "Y: " + str(p2y))
    P2YLabelOutput.pack(padx=5,pady=5,fill="x",expand=True)
    #Label output data banyak iterasi
    IterationLabelOutput = ttk.Label(newWindowFrame,text = "Banyak iterasi: " + str(it))
    IterationLabelOutput.pack(padx=5,pady=5,fill="x",expand=True)
    #tombol kembali ke root
    newWindowReturn = ttk.Button(newWindowFrame,text="Visualisasikan!",command=lambda: OpenVisualizer(newWindow))
    newWindowReturn.pack(padx=5,pady=5,fill="x",expand=True)

def OpenVisualizer(newWindow):
    newWindow.destroy()
    spawnPygame()

def runBranchThread(P0_X,P0_Y,P1_X,P1_Y,P2_X,P2_Y,ITERATION,root):
    spawnInfoWindow(P0_X,P0_Y,P1_X,P1_Y,P2_X,P2_Y,ITERATION,root)