import numpy
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.widgets import Slider
from matplotlib.patches import Rectangle
import serial

def data_gen():
    currentMean = 0
    while True:
        c = ser.readline();
        if c.find('s') != -1:
            temp = ( 5*float(ser.readline())/1024.0 -0.5)*100
            power =float(ser.readline())/255*10
            aim = (5*float(ser.readline())/1024.0 - 0.5)*100
            ti = float(ser.readline())/1000
            currentMean = (temp + currentMean)/2
            
            yield [temp, power, aim,  ti, currentMean]
def init():
    ax.set_ylim(0, 50)
    ax.set_xlim(0, 10)
    del xdata[:]
    del ydata[:]
    del pdata[:]
    del adata[:]
    line.set_data(xdata, ydata)
    line2.set_data(xdata, pdata)
    line3.set_data(xdata, adata)
    return [line, line2, line3]



def run(data):
    # update the data
    xdata.append(data[3])
    adata.append(data[2])
    pdata.append(data[1])
    ydata.append(data[0])
    TextBox.set_text( '{0:.3f}'.format( data[4] ) )
    xmin, xmax = ax.get_xlim()
    if data[3] >= xmax:
        ax.set_xlim(xdata[0], data[3])
        xdata.pop(0)
        ydata.pop(0)
        pdata.pop(0)
        adata.pop(0)
        ax.figure.canvas.draw()
    line.set_data(xdata, ydata)
    line2.set_data(xdata, pdata)
    line3.set_data(xdata, adata)

    return [line, line2, line3]


ser = serial.Serial('/dev/ttyUSB0', 9600)

fig, ax = plt.subplots()
TextBox = ax.text(0.5, 1.0, str(0), transform=ax.transAxes, ha="right", va="bottom", color="black", family="sans-serif", fontweight="light", fontsize=16)

axamp = plt.axes([0.12, 0.02, 0.8, 0.03], axisbg='b')
stemp = Slider(axamp, 'Temp', 20, 50, valinit=5)


def send_temp(val):
    ser.write( '{0:.0f}'.format(stemp.val*100) )
stemp.on_changed(send_temp)
line, = ax.plot([], [], lw=2)
line2, = ax.plot([], [], lw=2 )
line3, = ax.plot([], [], lw=2 )
ax.grid()
xdata, ydata = [], []
pdata, adata = [], []
ani = animation.FuncAnimation(fig, run, data_gen, blit=False,
                              repeat=False, init_func=init)

plt.show()
