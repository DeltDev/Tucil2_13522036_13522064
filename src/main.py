#import GUI dan visualisasi kurva bezier
import tkinter as tk
from tkinter import ttk
from point import *
import branchWindow as BW
from helper import getSRCDir,createGeneralLabelPack,createGeneralEntryPack,createControlPointInput
from tkinter import messagebox as msgbox
def SpawnMainWindow(initWindow,CTRLPOINTNUM):
    try: #handling kevalidan input jumlah control point
        ctrlPointCount = int(CTRLPOINTNUM.get())
        initWindow.destroy()
    except ValueError: #keluarkan pesan error jika input tidak valid
        msgbox.showerror("Program Error", "Input Anda tidak valid! \n Silahkan ulangi input data Anda.")
        return  
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

    #setup nilai-nilai yang ditangkap oleh gui di window utama
    X_ARR = [tk.StringVar() for i in range(ctrlPointCount)]
    Y_ARR = [tk.StringVar() for i in range(ctrlPointCount)]

    ITERATION = tk.StringVar()

    for i in range(ctrlPointCount): #buat input control point sebanyak n control point
        createControlPointInput(frame2,X_ARR[i],Y_ARR[i],i)
    #input data iterasi
    createGeneralLabelPack("Banyak Iterasi",frame2)
    createGeneralEntryPack(frame2,ITERATION)
    #input radio button mode pembentukan kurva bezier
    createGeneralLabelPack("Pilih Metode Pembentukan Kurva Bezier",frame2)
    MODES =[
        ("Brute Force","Brute Force"),
        ("Divide And Conquer","Divide And Conquer")
    ]

    BezierMethod = tk.StringVar()
    BezierMethod.set("Brute Force")
    for text, mode in MODES:
        RB = ttk.Radiobutton(frame2,text=text,variable=BezierMethod, value=mode)
        RB.pack(padx=5,pady=5,fill="x",expand=True)
    NextWindowButton = ttk.Button(frame2,text="Simulasikan Kurva Bezier",command= lambda: BW.spawnInfoWindow(X_ARR,Y_ARR,ITERATION,ctrlPointCount,root,BezierMethod)) #tombol untuk mensimulasikan Kurva Bezier
    NextWindowButton.pack(padx=5,fill="x",expand=True)
    root.mainloop() #fungsi untuk mencegah window root tertutup otomatis