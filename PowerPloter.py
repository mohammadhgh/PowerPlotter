import matplotlib
matplotlib.use('TkAgg')

from numpy import arange, sin, pi
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
# implement the default mpl key bindings
from matplotlib.backend_bases import key_press_handler


from matplotlib.figure import Figure

import sys
if sys.version_info[0] < 3:
    import Tkinter as Tk
else:
    import tkinter as Tk

root = Tk.Tk()
root.wm_title("Power measure")


import matplotlib.pyplot as plt
import numpy as np
import time
import serial


#f = Figure(figsize=(5, 4), dpi=100)
#a = f.add_subplot(111)
#t = arange(0.0, 3.0, 0.01)
#s = sin(2*pi*t)

#a.plot(t, s)


# a tk.DrawingArea


ser = serial.Serial(port='ttyUSB0', baudrate=9600, timeout=0.1)
#ser.open()

fig = Figure()
ax = fig.add_subplot(111)

# some X and Y data
x = np.arange(50)
y = np.linspace(0, 300, 50)

li, = ax.plot(x, y)

# draw and show it
#ax.relim() 
ax.autoscale_view(True,True,True)
#fig.canvas.draw()
#plt.show(block=False)
#plt.ylim(50,200)

canvas = FigureCanvasTkAgg(fig, master=root)
canvas.show()
canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)

toolbar = NavigationToolbar2TkAgg(canvas, root)
toolbar.update()
canvas._tkcanvas.pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)


def on_key_event(event):
    print('you pressed %s' % event.key)
    key_press_handler(event, canvas, toolbar)

canvas.mpl_connect('key_press_event', on_key_event)


#while True:
def itteration():
    try:
        #.write("salam\n")
        #time.sleep(0.1)
        received = ser.readline()
        try:
            print(received)
            rec_array = received.split(',');
            power = int(rec_array)
            print("power is: ",power)
        except:
            #continue
            power=0;
            pass
            
       
        #y[-1:] = np.random.randn(10)
        if(power1 != 0):
            y[:-1] = y[1:]
            y[-1:] = power1
        # set the new data
        li.set_ydata(y)

        fig.canvas.draw()
        plt.pause(0.001)

        time.sleep(0.001)
        root.after(100, itteration) 
    except KeyboardInterrupt:
        plt.close()
        root.quit() 
        root.destroy()
    except:
        pass


def _quit():
    root.quit()     # stops mainloop
    root.destroy()  # this is necessary on Windows to prevent
                    # Fatal Python Error: PyEval_RestoreThread: NULL tstate
                    
def on1():
    ser.write("a")
    print("ON 1")
    
def off1():
    ser.write("b")
    print("OFF 1")
    
                    
button = Tk.Button(master=root, text='Quit', command=_quit)
button.pack(side=Tk.BOTTOM)

on1 = Tk.Button(master=root, text='ON 1', command=on1)
on1.pack(side=Tk.BOTTOM)

off1 = Tk.Button(master=root, text='OFF 1', command=off1)
off1.pack(side=Tk.BOTTOM)
                    
root.after(100, itteration)                    
Tk.mainloop()

# If you put root.destroy() here, it will cause an error if
# the window is closed with the window manager.
