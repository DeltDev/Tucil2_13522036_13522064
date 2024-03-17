#import GUI dan visualisasi kurva bezier
import tkinter as tk
from tkinter import ttk
from point import *
import branchWindow as BW
from helper import getSRCDir

#Setup window root GUI 
root = tk.Tk()
root.configure(bg="gray")
root.geometry("400x510")
root.resizable(False,False)
root.title("Simulasi Kurva Bezier")

print(getSRCDir()+'\BezierCurveIcon.ico')
root.iconbitmap(getSRCDir()+'\BezierCurveIcon.ico')
# setup scroll bar
mainFrame = ttk.Frame(root)
mainFrame.pack(fill="both", expand=1)

#setup canvas
mainCanvas = tk.Canvas(mainFrame)
mainCanvas.pack(side="left", fill="both", expand=1)

#setup scrollbar
mainScrollbar = ttk.Scrollbar(mainFrame,orient="vertical",command=mainCanvas.yview)
mainScrollbar.pack(side="right",fill="y")

#config canvas
mainCanvas.configure(yscrollcommand=mainScrollbar.set)
mainCanvas.bind('<Configure>',lambda e: mainCanvas.configure(scrollregion= mainCanvas.bbox("all")))

#frame kedua
frame2 = ttk.Frame(mainCanvas)

#buka di window
mainCanvas.create_window((0,0), window=frame2, anchor="n")

#setup nilai-nilai yang ditangkap oleh gui
P0_X = tk.StringVar()
P0_Y = tk.StringVar()
P1_X = tk.StringVar()
P1_Y = tk.StringVar()
P2_X = tk.StringVar()
P2_Y = tk.StringVar()
ITERATION = tk.StringVar()

#input data titik P0
P0Label = ttk.Label(frame2,text="Titik Kontrol P0")
P0Label.pack(padx=5,pady=5,fill="x",expand=True)
P0XLabel = ttk.Label(frame2,text="Nilai X: ")
P0XLabel.pack(padx=5,pady=5,fill="x",expand=True)
P0XEntry = ttk.Entry(frame2,textvariable=P0_X)
P0XEntry.pack(padx=5,pady=5,fill="x",expand=True)
P0YLabel = ttk.Label(frame2,text="Nilai Y: ")
P0YLabel.pack(padx=5,pady=5,fill="x",expand=True)
P0YEntry = ttk.Entry(frame2,textvariable=P0_Y)
P0YEntry.pack(padx=5,pady=5,fill="x",expand=True)
#input data titik P1
P1Label = ttk.Label(frame2,text="Titik Kontrol P1")
P1Label.pack(padx=5,pady=5,fill="x",expand=True)
P1XLabel = ttk.Label(frame2,text="Nilai X: ")
P1XLabel.pack(padx=5,pady=5,fill="x",expand=True)
P1XEntry = ttk.Entry(frame2,textvariable=P1_X)
P1XEntry.pack(padx=5,pady=5,fill="x",expand=True)
P1YLabel = ttk.Label(frame2,text="Nilai Y: ")
P1YLabel.pack(padx=5,pady=5,fill="x",expand=True)
P1YEntry = ttk.Entry(frame2,textvariable=P1_Y)
P1YEntry.pack(padx=5,pady=5,fill="x",expand=True)
#input data titik P2
P2Label = ttk.Label(frame2,text="Titik Kontrol P2")
P2Label.pack(padx=5,pady=5,fill="x",expand=True)
P2XLabel = ttk.Label(frame2,text="Nilai X: ")
P2XLabel.pack(padx=5,pady=5,fill="x",expand=True)
P2XEntry = ttk.Entry(frame2,textvariable=P2_X)
P2XEntry.pack(padx=5,pady=5,fill="x",expand=True)
P2YLabel = ttk.Label(frame2,text="Nilai Y: ")
P2YLabel.pack(padx=5,pady=5,fill="x",expand=True)
P2YEntry = ttk.Entry(frame2,textvariable=P2_Y)
P2YEntry.pack(padx=5,pady=5,fill="x",expand=True)
#input data iterasi
IterationLabel = ttk.Label(frame2,text="Banyak Iterasi")
IterationLabel.pack(padx=5,pady=5,fill="x",expand=True)
IterationEntry = ttk.Entry(frame2,textvariable=ITERATION)
IterationEntry.pack(padx=5,pady=5,fill="x",expand=True)
#input radio button mode pembentukan kurva bezier
RadioButtonLabel =ttk.Label(frame2,text="Pilih Metode Pembentukan Kurva Bezier")
RadioButtonLabel.pack(padx=5,pady=5,fill="x",expand=True)
MODES =[
    ("Brute Force","Brute Force"),
    ("Divide And Conquer","Divide And Conquer")
]

BezierMethod = tk.StringVar()
BezierMethod.set("Brute Force")
for text, mode in MODES:
    RB = ttk.Radiobutton(frame2,text=text,variable=BezierMethod, value=mode)
    RB.pack(padx=5,pady=5,fill="x",expand=True)
NextWindowButton = ttk.Button(frame2,text="Simulasikan Kurva Bezier",command= lambda: BW.runBranchThread(P0_X,P0_Y,P1_X,P1_Y,P2_X,P2_Y,ITERATION,root,BezierMethod)) #tombol untuk mensimulasikan Kurva Bezier
NextWindowButton.pack(padx=5,fill="x",expand=True)
root.mainloop() #fungsi untuk mencegah window root tertutup otomatis