import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import numpy as np

class Plan:
    def __init__(self):
        self.fig,self.ax = plt.subplots()
        self.points_plot = {}
        self.sliders = {}
        self.data = {}
        self.figures_plot = {}
        self.figures_update = {}
        self.dragging_point = None
        plt.subplots_adjust(bottom=0.25)
        self.fig.canvas.mpl_connect('button_press_event', self.on_press)
        self.fig.canvas.mpl_connect('button_release_event', self.on_release)
        self.fig.canvas.mpl_connect('motion_notify_event', self.on_motion)

    def add_point(self,name,coords):
        self.points_plot[name], = self.ax.plot([],[],'o')
        self.new_data(name,coords)
    
    def add_slider(self,name,valinit,valmin,valmax):
        self.new_data(name,valinit)
        ax_slider = plt.axes((0.25, 0.1, 0.65, 0.03))
        slider = Slider(
        ax=ax_slider,
        label=name,
        valmin=valmin,
        valmax=valmax,
        valinit=valinit,
        valstep=0.01
        )
        slider.on_changed(lambda val:self.update_slider(name,val))
        self.sliders[name] = slider
    def update_slider(self,name,val):
        self.data[name] = val
        print(self.data)
        self.update()

    def new_data(self,name,val):
        assert name not in self.data,f"{name!r} already exist"
        self.data[name] = val

    def update(self):
        for name,plot in self.points_plot.items():
            val = self.data[name]
            plot.set_data([val[0]],[val[1]])

        for name,plot in self.figures_plot.items():
            update_func = self.figures_update[name]
            update_func(plot,self)

        self.ax.relim()
        print(self.ax.get_xlim())
        self.fig.canvas.draw_idle()
        
        #self.ax.autoscale_view()
    def show(self):
        self.update()
        self.ax.set_aspect('equal',adjustable="box")
        self.ax.set_xlabel('x')
        self.ax.set_ylabel('y')
        # self.ax.set_xlim(min(self.data[name][0] for name in self.data) - 1,
        #                  max(self.data[name][0] for name in self.data) + 1)
        # self.ax.set_ylim(min(self.data[name][1] for name in self.data) - 1,
        #                  max(self.data[name][1] for name in self.data) + 1)
        self.ax.set_aspect('equal', adjustable='box')
        #self.ax.grid(True)
        plt.show()

    def on_press(self,event):
        
        for name,plot in self.points_plot.items():
            if plot.contains(event)[0]:
                self.dragging_point = name
                print(name)
                return
            
    def on_motion(self,event):
        if self.dragging_point and event.xdata is not None and event.ydata is not None:
            self.data[self.dragging_point] = (event.xdata,event.ydata)
            self.update()

    def on_release(self,event):
        self.dragging_point = None

    def add_figure(self,name,update_func):
        """
        update_func(plot,plan)
        """
        self.figures_plot[name], = self.ax.plot([],[])
        self.figures_update[name] = update_func

class Droite:
    def __init__(self,point1_name,point2_name):
        self.p1_name = point1_name
        self.p2_name = point2_name

    def __call__(self,plot,plan:Plan):
        p1_coords = plan.data[self.p1_name]
        p2_coords = plan.data[self.p2_name]
        plan.ax.relim()
        print(plan.ax.get_xlim())

        if p1_coords[0] == p2_coords[0]:
            d_equ = {"a":1,"b":0,"c":-p1_coords[0]}
            #print(d_equ)
            x_vals = [p1_coords[0], p1_coords[0]]
            y_vals = plan.ax.get_ylim()
        else:
            print("ss")
            m = (p2_coords[1]-p1_coords[1]) / (p2_coords[0]-p1_coords[0])
            h = p1_coords[1] - m * p1_coords[0]
            d_equ = {"a":m, "b":-1, "c":h}
            x_vals = np.array(plan.ax.get_xlim())
            y_vals = m * x_vals + h
        plot.set_data(x_vals, y_vals)
if __name__=="__main__":
    plan = Plan()
    plan.add_point("point1",(0,0))
    plan.add_point("point2",(1,0))
    plan.add_figure("droite",Droite("point1","point2"))
    plan.add_slider("slider",5,0,10)
    plan.show()