from PIL import Image
import numpy as np
from numba import vectorize
import time

# Load image and convert to numpy array
u,v = None,None
RADIUS = None
X_SHAPE,Y_SHAPE = None,None
FILE = 'image2.png'  # Replace with your image file path
class Stopwatch:
    def reset(self):
        self.tt = time.time()
        self.last_tt = self.tt
    def __init__(self,active=True):
        self.active=active
        self.reset()
    def lap(self,msg):
        if self.active:
            tt = time.time()
            tt_delta = tt-self.last_tt
            tt_total = tt-self.tt
            self.last_tt = tt
            print(f"[{tt_delta:06.3f} {tt_total:06.3f}] {msg}")
        #print(f"[{tt_delta:6.3f} {tt_total:6.3f}] {msg}")



def inversion(file_input,shape_output=(),center=(),radius=0,file_output=""):
    stopwatch = Stopwatch()
    image = Image.open(file_input).convert('RGB')
    stopwatch.lap("image opened")
    image_array = np.array(image)
    image_array[0,0] = (255,0,0) # default pixel


    shape_input_y,shape_input_x = image_array.shape[:2]
    if not shape_output:
        shape_output = shape_input_x,shape_input_y

    shape_output_x,shape_output_y = shape_output
    if not radius:
        radius = min(shape_output_x,shape_output_y)/4 if RADIUS is None else RADIUS
    if not center:
        center = (shape_output_x/2,shape_output_y/2)
    center_x,center_y = center
    print(shape_output_x,shape_output_y,radius,center_x,center_y)

    stopwatch.lap("l1")
    if not file_output:
        filename,_,ext = file_input.rpartition(".")
        file_output=f"{filename}-inversion.{ext}"

    indices_y1,indices_x1 = np.indices((shape_output_y, shape_output_x))
    stopwatch.lap("indices")
    distances = (indices_x1 - center_x)**2 + (indices_y1 - center_y)**2 # CP^2

    distances[distances == 0] = 1  # Avoid division by zero
    stopwatch.lap("distances")
    indices_x2 = (center_x + radius**2/distances * (indices_x1 - center_x)).astype(np.int64)
    indices_y2 = (center_y + radius**2/distances * (indices_y1 - center_y)).astype(np.int64)

    stopwatch.lap("l2")
    # avoid IndexError
    on_image = (indices_x2 >= 0) & (indices_x2 < shape_input_x) & (indices_y2 >= 0) & (indices_y2 < shape_input_y)
    indices_x2[~on_image] = 0
    indices_y2[~on_image] = 0

    #print(on_image)
    #print("Hello")

    @vectorize
    def myfunc(indice_x,indice_y,color):
        return image_array[indice_y,indice_x,color]
    stopwatch.lap("l3")
    result = [myfunc(indices_x2, indices_y2,color) for color in range(3)]
    stopwatch.lap("result")
    result=np.array(result).transpose((1,2,0))
    print(result.shape)
    stopwatch.lap("save")
    Image.fromarray(result).save(file_output)

    stopwatch.lap("end")
if __name__=="__main__":
    inversion(r"images\apple.png",(1000,500))
input()