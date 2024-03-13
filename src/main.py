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
input_frame.pack(padx=10,pady=10,fill="x",expand=True)

#komponen GUI
testLabel1 = ttk.Label(input_frame,text="Test 1:")
testLabel1.pack(padx=10,fill="x",expand=True)
TEST_ENTRY1 = tk.StringVar()
testEntry1 = ttk.Entry(input_frame,textvariable=TEST_ENTRY1)
testEntry1.pack(padx=10,fill="x",expand=True)
#perintah tombol
def buttonClick():
    print(TEST_ENTRY1.get())
testButton1 = ttk.Button(input_frame,text="tampilkan teks",command=buttonClick)
testButton1.pack(fill='x',expand=True,padx=10,pady=10)
window.mainloop()