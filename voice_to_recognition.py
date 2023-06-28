import numpy as np
import scipy.io.wavfile
import wav_to_string
import string_to_command
from pykakasi import kakasi # kanji to kana


# kakasi config
kakasi = kakasi()
kakasi.setMode('J', 'H') 
conv = kakasi.getConverter()

def update_command(data, command):
        filename = "hoge.wav"
        scipy.io.wavfile.write(filename, rate=44100, data=data.astype(np.int16))
        st = wav_to_string.wavToString(filename)
        st = conv.do(st)
        command = string_to_command.string_to_command(st, command)
        print(command)
        return command