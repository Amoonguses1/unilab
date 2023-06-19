import sounddevice as sd
import numpy as np
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import scipy.io.wavfile
import wav_to_string

def callback(indata, frames, time_name, status):
    def savefunc(data):
        global count
        global name_count
        filename = "hoge.wav"
        scipy.io.wavfile.write(filename, rate=44100, data=data.astype(np.int16))
        print(wav_to_string.wavToString(filename))
        name_count += 1
        count = 0
    # indata.shape=(n_samples, n_channels)
    global plotdata
    global count
    flag = False
    data = indata[::downsample, 0]
    shift = len(data)
    if count == 0:
        for val in data:
            if(val > 500):
                print("utter")
                count += 1
                flag = True
                break
    plotdata = np.roll(plotdata, -shift, axis=0)
    plotdata[-shift:] = data
    if not flag:
        if count != 0:
            count += 1
        if count > 35:
            savefunc(plotdata)


def update_plot(frame):
    """This is called by matplotlib for each plot update.
    """
    global plotdata
    line.set_ydata(plotdata)
    return line,

downsample = 1
length = int(1000 * 44100 / (1000 * downsample))
plotdata = np.zeros((length))
count = 0
name_count = 0
fig, ax = plt.subplots()
line, = ax.plot(plotdata)
ax.set_ylim([-1000, 1000])
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
