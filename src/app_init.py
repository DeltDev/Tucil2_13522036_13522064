import tkinter as tk
from tkinter import ttk
from point import *
import branchWindow as BW
from helper import getSRCDir
from helper import createGeneralLabelPack,createGeneralEntryPack
from main import SpawnMainWindow
#setup window tkinter 
def GoToMain(root,CTRLPOINTNUM):
    SpawnMainWindow(root,CTRLPOINTNUM)
root = tk.Tk()
root.configure(bg="gray")
root.geometry("400x510")
root.resizable(False,False)
root.title("Simulasi Kurva Bezier")

print(getSRCDir()+'\BezierCurveIcon.ico')
root.iconbitmap(getSRCDir()+'\BezierCurveIcon.ico')

frame1 = ttk.Frame(root)
frame1.pack(padx=5,pady=5,fill="x",expand=True)

#banyak control point yang diinput
CTRLPOINTNUM = tk.StringVar()
createGeneralLabelPack("Input Banyak Control Point: ",frame1)
createGeneralEntryPack(frame1,CTRLPOINTNUM)

GoToMainButton = ttk.Button(frame1,text="Submit jumlah control point",command = lambda: GoToMain(root,CTRLPOINTNUM)) #tombol untuk lanjut ke window berikutnya
GoToMainButton.pack(padx=5,fill="x",expand=True)
root.mainloop()

