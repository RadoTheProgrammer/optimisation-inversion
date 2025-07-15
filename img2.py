import matplotlib.pyplot as plt
import numpy as np

plt.ion()

# Example image data
img = np.random.rand(10, 10)
# Desired position
x, y = -2,-2  # bottom-left corner of image
width, height = img.shape[1], img.shape[0]
print(img)
# Display image
#plt.imshow(img)
#plt.imshow(img, extent=(0,width,height,0))
plt.imshow(img, extent=(x, x + width, y, y+height))
ax = plt.gca()
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_aspect('equal', adjustable='box')
plt.axhline(0, color='black', linewidth=1)  # x-axis
plt.axvline(0, color='black', linewidth=1)  # y-axis
plt.colorbar()
plt.grid(True)
plt.show()
