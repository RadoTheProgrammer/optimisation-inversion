import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 500)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y)
plt.title("Zoom or Pan to trigger events")

# Callback functions
def on_xlim_change(event_ax):
    print("X-limits changed:", event_ax.get_xlim())
    

def on_ylim_change(event_ax):
    print("Y-limits changed:", event_ax.get_ylim())
    ax.set_aspect("equal")

# Connect the callbacks to the axes
ax.callbacks.connect('xlim_changed', on_xlim_change)
ax.callbacks.connect('ylim_changed', on_ylim_change)

plt.show()
