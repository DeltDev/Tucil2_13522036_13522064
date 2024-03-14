import tkinter as tk
from threading import Thread, Event
import time
from branchWindow import spawnInfoWindow,spawnPygame
# Define a flag to control the execution of tkinter thread
tkinter_stop_flag = Event()

# Define a flag to control the execution of pygame thread
pygame_stop_flag = Event()

# Function for tkinter thread
def tkinter_thread_function(P0_X, P0_Y, P1_X, P1_Y, P2_X, P2_Y, ITERATION, root):
    spawned = False
    while not tkinter_stop_flag.is_set():
        if(not spawned):
            spawnInfoWindow(P0_X, P0_Y, P1_X, P1_Y, P2_X, P2_Y, ITERATION, root)
            spawned = True
        time.sleep(1)  # Adjust the sleep time as needed

# Function for pygame thread
def pygame_thread_function():
    spawned = False
    while not pygame_stop_flag.is_set():
        if(not spawned):
            spawnPygame()
            spawned = True
        time.sleep(1)  # Adjust the sleep time as needed

# Function to stop both threads
def stop_threads():
    tkinter_stop_flag.set()
    pygame_stop_flag.set()

# Create Tkinter window
root = tk.Tk()

# Create a button to stop the threads
stop_button = tk.Button(root, text="Stop Threads", command=stop_threads)
stop_button.pack()

# Start tkinter thread
tkinter_thread = Thread(target=tkinter_thread_function, args=("1", "2", "3", "4", "5", "6", "7", root))
tkinter_thread.start()

# Start pygame thread
pygame_thread = Thread(target=pygame_thread_function)
pygame_thread.start()

# Start the Tkinter event loop
root.mainloop()

# Wait for both threads to finish
tkinter_thread.join()
pygame_thread.join()

print("Main thread exiting.")
