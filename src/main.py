#import GUI dan visualisasi kurva bezier
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msgbox
import BezierFormulas as Bezier
from point import *
from matplotlib import pyplot as plt
from visualizer import spawnPygame
from threading import Thread
import branchWindow as BW
#Setup window root GUI 
root = tk.Tk()
root.configure(bg="gray")
root.geometry("540x720")
root.resizable(False,False)
root.title("Simulasi Kurva Bezier")

#setup frame input
input_frame1 = ttk.Frame(root)
input_frame1.pack(padx=5,pady=5,fill="x",expand=True)
input_frame2 = ttk.Frame(root)
input_frame2.pack(padx=5,pady=5,fill="x",expand=True)
input_frame3 = ttk.Frame(root)
input_frame3.pack(padx=5,pady=5,fill="x",expand=True)
input_frame4 = ttk.Frame(root)
input_frame4.pack(padx=5,pady=5,fill="x",expand=True)
input_frame5 = ttk.Frame(root)
input_frame5.pack(padx=5,pady=5,fill="x",expand=True)
#setup nilai-nilai yang ditangkap oleh gui
P0_X = tk.StringVar()
P0_Y = tk.StringVar()
P1_X = tk.StringVar()
P1_Y = tk.StringVar()
P2_X = tk.StringVar()
P2_Y = tk.StringVar()
ITERATION = tk.StringVar()
WindowSpawnSucceed = True
#input data titik P0
P0Label = ttk.Label(input_frame1,text="Titik Kontrol P0")
P0Label.pack(padx=5,pady=5,fill="x",expand=True)
P0XLabel = ttk.Label(input_frame1,text="Nilai X: ")
P0XLabel.pack(padx=5,pady=5,fill="x",expand=True)
P0XEntry = ttk.Entry(input_frame1,textvariable=P0_X)
P0XEntry.pack(padx=5,pady=5,fill="x",expand=True)
P0YLabel = ttk.Label(input_frame1,text="Nilai Y: ")
P0YLabel.pack(padx=5,pady=5,fill="x",expand=True)
P0YEntry = ttk.Entry(input_frame1,textvariable=P0_Y)
P0YEntry.pack(padx=5,pady=5,fill="x",expand=True)
#input data titik P1
P1Label = ttk.Label(input_frame2,text="Titik Kontrol P1")
P1Label.pack(padx=5,pady=5,fill="x",expand=True)
P1XLabel = ttk.Label(input_frame2,text="Nilai X: ")
P1XLabel.pack(padx=5,pady=5,fill="x",expand=True)
P1XEntry = ttk.Entry(input_frame2,textvariable=P1_X)
P1XEntry.pack(padx=5,pady=5,fill="x",expand=True)
P1YLabel = ttk.Label(input_frame2,text="Nilai Y: ")
P1YLabel.pack(padx=5,pady=5,fill="x",expand=True)
P1YEntry = ttk.Entry(input_frame2,textvariable=P1_Y)
P1YEntry.pack(padx=5,pady=5,fill="x",expand=True)
#input data titik P2
P2Label = ttk.Label(input_frame3,text="Titik Kontrol P2")
P2Label.pack(padx=5,pady=5,fill="x",expand=True)
P2XLabel = ttk.Label(input_frame3,text="Nilai X: ")
P2XLabel.pack(padx=5,pady=5,fill="x",expand=True)
P2XEntry = ttk.Entry(input_frame3,textvariable=P2_X)
P2XEntry.pack(padx=5,pady=5,fill="x",expand=True)
P2YLabel = ttk.Label(input_frame3,text="Nilai Y: ")
P2YLabel.pack(padx=5,pady=5,fill="x",expand=True)
P2YEntry = ttk.Entry(input_frame3,textvariable=P2_Y)
P2YEntry.pack(padx=5,pady=5,fill="x",expand=True)
#input data iterasi
IterationLabel = ttk.Label(input_frame4,text="Banyak Iterasi")
IterationLabel.pack(padx=5,pady=5,fill="x",expand=True)
IterationEntry = ttk.Entry(input_frame4,textvariable=ITERATION)
IterationEntry.pack(padx=5,pady=5,fill="x",expand=True)
NextWindowButton = ttk.Button(input_frame5,text="Simulasikan Kurva Bezier",command= lambda: BW.runBranchThread(P0_X,P0_Y,P1_X,P1_Y,P2_X,P2_Y,ITERATION,root)) #tombol untuk mensimulasikan Kurva Bezier
NextWindowButton.pack(padx=5,fill="x",expand=True)
root.mainloop() #fungsi untuk mencegah window root tertutup otomatis