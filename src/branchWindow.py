import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msgbox
import BezierFormulas as Bezier
from point import Point
from visualizer import spawnPygame
import time
from helper import getSRCDir,createGeneralLabelPack,createControlPointOutput
def checkArrayValidity(Values,ARR,n): #cek kevalidan array
    for i in range(n):
        Values[i] = float(ARR[i].get())

def spawnInfoWindow(X_ARR,Y_ARR,ITERATION,ctrlPointCount,root,BezierMethod):
    
    try: #handling kevalidan input pada entry
        xValues = [0.0 for i in range(ctrlPointCount)]
        yValues = [0.0 for i in range(ctrlPointCount)]
        checkArrayValidity(xValues,X_ARR,ctrlPointCount)
        checkArrayValidity(yValues,Y_ARR,ctrlPointCount)
        it = int(ITERATION.get())
        method = BezierMethod.get()
    except ValueError: #keluarkan pesan error jika input tidak valid
        msgbox.showerror("Program Error", "Input Anda tidak valid! \n Silahkan ulangi input data Anda.")
        return   
         
    ControlPointList =[]
    BezierPointList = []
    MidpointList = []
    deltaTime = 0.0

    for i in range(ctrlPointCount): #masukkan semua control point yang didapat dari input GUI
        ControlPointList.append(Point(xValues[i],yValues[i],"P"+str(i)))

    if(method == "Brute Force"): #metode yang dipilih adalah brute force
        start = time.perf_counter() 
        BezierPointList = Bezier.GeneralBruteForceBezier(ControlPointList,2**it) #samakan jumlah titik dengan jumlah titik yang didapatkan dengan cara divide and conquer
        end = time.perf_counter()
        deltaTime = (end-start) *1000 #hitung waktu eksekusi
    elif(method == "Divide And Conquer"): #metode yang dipilih adalah divide and conquer
        start = time.perf_counter()
        Bezier.GeneralDivideAndConquerBezier(ControlPointList,it,MidpointList) #lakukan divide and conquer
        end = time.perf_counter()
        deltaTime = (end-start) *1000 #hitung waktu eksekusi
        BezierPointList.append(ControlPointList[0]) #P0 adalah titik awal kurva bezier
        for i in MidpointList:
            if(i.pointName == "NEW"): #append semua titik yang diberi nama "NEW" setelah proses DnC ke daftar titik di kurva bezier 
                BezierPointList.append(i)
        BezierPointList.append(ControlPointList[ctrlPointCount-1]) #P(n-1) adalah titik akhir dari kurva bezier

    #setup window kedua
    root.withdraw()
    newWindow = tk.Toplevel(root)
    newWindow.title("Hasil Simulasi Kurva Bezier")
    newWindow.config(bg = "gray")
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

    #output semua data control point
    for i in range(ctrlPointCount):
        createControlPointOutput(newWindowFrame,"Control Point P"+str(i),xValues[i],yValues[i])
    #buat label output data banyak iterasi
    createGeneralLabelPack("Banyak iterasi: "+str(it),newWindowFrame)
    #buat label metode yang dipilih
    createGeneralLabelPack("Metode: " + method,newWindowFrame)
    #Waktu eksekusi
    createGeneralLabelPack("Waktu Eksekusi: " + str(deltaTime) + " ms",newWindowFrame)
    #tombol ke visualisasi kurva bezier
    VisualizeButton = ttk.Button(newWindowFrame,text="Visualisasikan!",command=lambda: OpenVisualizer(newWindow,ControlPointList,BezierPointList,MidpointList,method))
    VisualizeButton.pack(padx=5,pady=5,fill="x",expand=True)

def OpenVisualizer(newWindow,ControlPointList,BezierPointList,MidpointList,BezierMethod): #buka visualizer
    newWindow.destroy()
    spawnPygame(ControlPointList,BezierPointList,MidpointList,BezierMethod)