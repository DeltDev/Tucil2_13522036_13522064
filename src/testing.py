import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Create some data
x_data = np.linspace(0, 10, 100)
y_data = np.sin(x_data)

# Create a figure and axis
fig, ax = plt.subplots()
line, = ax.plot([], [], lw=2)

# Initialization function: plot the background of each frame
def init():
    line.set_data([], [])
    return line,

# Animation function: this is called sequentially
def animate(i):
    x = x_data[:i]
    y = y_data[:i]
    line.set_data(x, y)
    return line,

# Create the animation
ani = FuncAnimation(fig, animate, init_func=init, frames=len(x_data), interval=50, blit=True)

# Show the animation
plt.show()
