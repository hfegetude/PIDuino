import numpy
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import serial

def data_gen():
    while True:
        c = ser.readline();
        if c.find('s') != -1:
            temp = ( 5*float(ser.readline())/1024.0 -0.5)*100
            power =float(ser.readline())/255*10
            aim = float(ser.readline())
            ti = float(ser.readline())/1000
            yield [temp, power, aim,  ti]
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

line, = ax.plot([], [], lw=2)
line2, = ax.plot([], [], lw=2 )
line3, = ax.plot([], [], lw=2 )
ax.grid()
xdata, ydata = [], []
pdata, adata = [], []
ani = animation.FuncAnimation(fig, run, data_gen, blit=False,
                              repeat=False, init_func=init)
plt.show()
