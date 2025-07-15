import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

FILE = r"images\apple.png"
img = np.asarray(Image.open(FILE).convert('RGB'))
np.asarray(img)
imgplot = plt.imshow(img)
width, height = img.shape[1], img.shape[0]
x,y = 100,200
plt.imshow(img, extent=(x,x+width/2, y+height, y))

plt.show()