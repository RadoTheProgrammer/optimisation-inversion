import matplotlib.pyplot as plt
import numpy as np

# Turn on interactive mode
#plt.ion()

# Create some data
x = np.linspace(-10, 10, 500)
y = np.sin(x)

# Plot the data
fig, ax = plt.subplots()
ax.plot(x, y)

# Show the plot window with zoom and pan tools enabled
plt.title("Use mouse wheel to zoom, click-drag to pan")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)

# Keep the plot window open
plt.show(block=True)
