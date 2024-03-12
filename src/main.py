#import GUI dan visualisasi kurva bezier
import tkinter as tk
from tkinter import ttk
#Setup window GUI
window = tk.Tk()
window.configure(bg="gray")
window.geometry("540x720")
window.resizable(False,False)
window.title("Simulasi Kurva Bezier")

#frame input
input_frame = ttk.Frame(window)

window.mainloop()