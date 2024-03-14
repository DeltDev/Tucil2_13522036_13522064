import threading
import time

# Define a flag to control the thread's execution
stop_flag = threading.Event()

# Define a function that the thread will execute
def my_thread_function():
    while not stop_flag.is_set():
        print("Thread is running...")
        time.sleep(1)
    print("Thread stopped.")

# Create and start the thread
my_thread = threading.Thread(target=my_thread_function)
my_thread.start()

# Let the thread run for some time
time.sleep(5)

# Set the stop flag to True, indicating the thread should stop
stop_flag.set()

# Wait for the thread to finish
my_thread.join()

print("Main thread exiting.")
