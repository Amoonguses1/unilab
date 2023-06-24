import sounddevice as sd
import numpy as np
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import scipy.io.wavfile
import wav_to_string
import string_to_command
from pykakasi import kakasi # kanji to kana
import socket # send to unity


# kakasi config
kakasi = kakasi()
kakasi.setMode('J', 'H') 
conv = kakasi.getConverter()
# socket config
HOST = '127.0.0.1'
PORT = 50007
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# voice get config
voice = {"threshold": 750, "skip": 35, "y_size": 1000}


def callback(indata, frames, time_name, status):
    def savefunc(data):
        global count
        global command
        filename = "hoge.wav"
        scipy.io.wavfile.write(filename, rate=44100, data=data.astype(np.int16))
        st = wav_to_string.wavToString(filename)
        st = conv.do(st)
        command = string_to_command.string_to_command(st, command)
        print(command)
        count = 0
    global plotdata
    global count
    global command
    flag = False
    data = indata[::downsample, 0]
    shift = len(data)
    if count == 0:
        for val in data:
            if(val > voice["threshold"]):
                print("utter")
                count += 1
                flag = True
                break
    plotdata = np.roll(plotdata, -shift, axis=0)
    plotdata[-shift:] = data
    if not flag:
        if count != 0:
            count += 1
        if count > voice["skip"]:
            savefunc(plotdata)
    client.sendto(command.encode('utf-8'),(HOST,PORT))


def update_plot(frame):
    """This is called by matplotlib for each plot update.
    """
    global plotdata
    line.set_ydata(plotdata)
    return line,

command = "0"
downsample = 1
length = int(1000 * 44100 / (1000 * downsample))
plotdata = np.zeros((length))
count = 0
fig, ax = plt.subplots()
line, = ax.plot(plotdata)
ax.set_ylim([-1*voice["y_size"], voice["y_size"]])
ax.set_xlim([0, length])
ax.yaxis.grid(True)
fig.tight_layout()

stream = sd.InputStream(
        channels=1,
        dtype='int16',
        callback=callback
    )
ani = FuncAnimation(fig, update_plot, interval=30, blit=True)
with stream:
    plt.show()
