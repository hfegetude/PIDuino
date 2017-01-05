import numpy as np
import matplotlib.pyplot as plt
import serial


def fifo_move(queue, data):
    queue.pop(0)
    queue.append(data)


number_of_elements_per_frame = 20
list_of_times = number_of_elements_per_frame * [0]
list_of_temps = number_of_elements_per_frame * [0]
list_of_power = number_of_elements_per_frame * [0]
list_of_aims = number_of_elements_per_frame * [0]
number_of_data = 0;


while True:
    ser = serial.Serial('/dev/ttyUSB0', 9600)

    fifo_move(list_of_temps ,float(ser.readline()))
    fifo_move(list_of_power, float(ser.readline())/255)
    fifo_move(list_of_aims, float(ser.readline()))
    fifo_move(list_of_times,float(ser.readline()))
    number_of_data = number_of_data +1;
    if number_of_data > 0:
        plt.clear()
        plt.axis([min(list_of_times), max(list_of_times), 15, 50])
        plt.plot(list_of_times, list_of_temps , 'r', list_of_times, list_of_power , 'g', list_of_times, list_of_power , 'b',)
        plt.show();
