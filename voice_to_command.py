import sounddevice as sd
import numpy as np
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt


import voice_to_recognition
import string_to_command
# voice get config
voice_config = {"threshold": 750, "skip": 35, "y_size": 1000}
command_config = {"step": 20}

def callback(indata, frames, time_name, status):
    global plotdata
    global count
    global command
    flag = False
    data = indata[::1, 0]
    shift = len(indata)
    if count == 0:
        for val in data:
            if(val > voice_config["threshold"]):
                print("utter")
                count += 1
                flag = True
                break
    plotdata = np.roll(plotdata, -shift, axis=0)
    plotdata[-shift:] = data
    command = string_to_command.command_admin(step, command, command_config["step"])
    if flag:
        return
    if count != 0:
        count += 1
    if count > voice_config["skip"]:
        command = voice_to_recognition.update_command(plotdata, command)
        count = 0

def update_plot(frame):
    """This is called by matplotlib for each plot update.
    """
    global plotdata
    line.set_ydata(plotdata)
    return line,

command = "0"
count = 0
step = [0,0]
length = int(1000 * 44100 / (1000))
plotdata = np.zeros((length))
fig, ax = plt.subplots()
line, = ax.plot(plotdata)
ax.set_ylim([-1*voice_config["y_size"], voice_config["y_size"]])
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
