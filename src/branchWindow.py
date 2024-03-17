import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msgbox
import BezierFormulas as Bezier
from point import Point
from visualizer import spawnPygame
import time
import os
from helper import getSRCDir
def disable_close_window(): #matikan fungsi tombol close default
    pass
def spawnInfoWindow(P0_X,P0_Y,P1_X,P1_Y,P2_X,P2_Y,ITERATION,root,BezierMethod):
    
    try: #handling kevalidan input pada entry
        p0x = float(P0_X.get()) #jangan lupa diganti
        p0y = float(P0_Y.get())
        p1x = float(P1_X.get())
        p1y = float(P1_Y.get())
        p2x = float(P2_X.get())
        p2y = float(P2_Y.get())
        it = int(ITERATION.get())
        method = BezierMethod.get()
    except ValueError: #keluarkan pesan error jika input tidak valid
        msgbox.showerror("Program Error", "Input Anda tidak valid! \n Silahkan ulangi input data Anda.")
        return        
    ControlPointList =[Point(p0x,p0y,"P0"),Point(p1x,p1y,"P1"),Point(p2x,p2y,"P2")]

    BezierPointList = []
    MidpointList = []
    deltaTime = 0.0
    if(method == "Brute Force"): #metode yang dipilih adalah brute force
        start = time.perf_counter()
        BezierPointList = Bezier.BruteForceBezier(ControlPointList[0],ControlPointList[1],ControlPointList[2],2**it) #samakan jumlah titik dengan jumlah titik yang didapatkan dengan cara divide and conquer
        end = time.perf_counter()

        deltaTime = (end-start) *1000
        MidpointList = []
    elif(method == "Divide And Conquer"): #metode yang dipilih adalah divide and conquer
        start = time.perf_counter()
        Bezier.DivideAndConquerBezier(ControlPointList[0],ControlPointList[1],ControlPointList[2],it,MidpointList)
        end = time.perf_counter()
        deltaTime = (end-start) *1000
        BezierPointList.append(ControlPointList[0]) #P0 adalah titik awal kurva bezier
        for i in MidpointList:
            if(i.pointName == "TENGAH"): #append semua titik yang diberi nama "TENGAH" setelah proses DnC ke daftar titik ti kurva bezier 
                BezierPointList.append(i)
        BezierPointList.append(ControlPointList[2]) #P2 adalah titik akhir kurva bezier
        

    #setup window kedua
    root.withdraw()
    newWindow = tk.Toplevel(root)
    newWindow.title("Hasil Simulasi Kurva Bezier")
    newWindow.config(bg = "gray")
    newWindow.protocol("WM_DELETE_WINDOW", disable_close_window)
    newWindow.geometry("400x300")
    newWindow.iconbitmap(getSRCDir()+'\BezierCurveIcon.ico')
    # setup scroll bar
    mainFrame = ttk.Frame(newWindow)
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
    newWindowFrame = ttk.Frame(mainCanvas)

    #buka di window
    mainCanvas.create_window((0,0), window=newWindowFrame, anchor="n")

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
    #Label metode yang dipilih
    MethodLabel = ttk.Label(newWindowFrame,text = "Metode: " + method)
    MethodLabel.pack(padx=5,pady=5,fill="x",expand=True)
    #Waktu eksekusi
    MethodLabel = ttk.Label(newWindowFrame,text = "Waktu Eksekusi: " + str(deltaTime) + " ms")
    MethodLabel.pack(padx=5,pady=5,fill="x",expand=True)
    #tombol kembali ke root
    newWindowReturn = ttk.Button(newWindowFrame,text="Visualisasikan!",command=lambda: OpenVisualizer(newWindow,ControlPointList,BezierPointList,MidpointList,method))
    newWindowReturn.pack(padx=5,pady=5,fill="x",expand=True)

def OpenVisualizer(newWindow,ControlPointList,BezierPointList,MidpointList,BezierMethod):
    newWindow.destroy()
    spawnPygame(ControlPointList,BezierPointList,MidpointList,BezierMethod)

def runBranchThread(P0_X,P0_Y,P1_X,P1_Y,P2_X,P2_Y,ITERATION,root,BezierMethod):
    spawnInfoWindow(P0_X,P0_Y,P1_X,P1_Y,P2_X,P2_Y,ITERATION,root,BezierMethod)