import numpy
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import serial

def data_gen():
    while True:
        c = ser.readline();
        if c.find('s') != -1:
            temp = ( 5*float(ser.readline())/1024.0 -0.5)*100
            ti = float(ser.readline())/1000
            yield ti, temp
def init():
    ax.set_ylim(15, 45)
    ax.set_xlim(0, 10)
    del xdata[:]
    del ydata[:]

    line.set_data(xdata, ydata)
    return line,



def run(data):
    # update the data
    t, y = data
    xdata.append(t)
    ydata.append(y)
    xmin, xmax = ax.get_xlim()

    if t >= xmax:
        ax.set_xlim(xdata[0], t)
        xdata.pop(0)
        ydata.pop(0)
        ax.figure.canvas.draw()
    line.set_data(xdata, ydata)


    return line,


ser = serial.Serial('/dev/ttyUSB0', 9600)
fig, ax = plt.subplots()
line, = ax.plot([], [], lw=2)
ax.grid()
xdata, ydata = [], []

ani = animation.FuncAnimation(fig, run, data_gen, blit=False,
                              repeat=False, init_func=init)
plt.show()
