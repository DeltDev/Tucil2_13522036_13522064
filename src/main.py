#import GUI dan visualisasi kurva bezier
import tkinter as tk
from tkinter import ttk
#Setup window root GUI 
root = tk.Tk()
root.configure(bg="gray")
root.geometry("540x720")
root.resizable(False,False)
root.title("Simulasi Kurva Bezier")

input_frame = ttk.Frame(root)
input_frame.pack(padx=10,pady=10,fill="x",expand=True)

def ReopenRootWindow(newWindow):
    newWindow.destroy()
    root.deiconify()
def OpenNextWindow():
    newWindow = tk.Toplevel(root)

    newWindow.title("Window baru")

    newWindow.geometry("200x200")
    newWindowFrame = ttk.Frame(newWindow)
    newWindowFrame.pack(padx=10,pady=10,fill="x",expand=True)
    newWindowLabel = ttk.Label(newWindow,text = "Ini window baru")
    newWindowLabel.pack(padx=10,pady=10,fill="x",expand=True)
    newWindowReturn = ttk.Button(newWindow,text="Kembali ke root",command=lambda: ReopenRootWindow(newWindow))
    newWindowReturn.pack(padx=10,pady=10,fill="x",expand=True)
    root.withdraw()
    
NextWindowButton = ttk.Button(input_frame,text="Ke Window Berikutnya",command=OpenNextWindow)
NextWindowButton.pack(padx=10,pady=10,fill="x",expand=True)


root.mainloop()