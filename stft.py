import numpy as np
import matplotlib.pyplot as plt
import librosa
import librosa.display as disp
# stft
# ref: https://qiita.com/lilacs/items/a331a8933ec135f63ab1

# data load
data, sample_rate = librosa.load("meian_0000.wav")
# spectrogram
stft_data = librosa.stft(data.astype(np.float32))
Sdb = librosa.amplitude_to_db(np.abs(stft_data))

# visualization
fig, ax = plt.subplots(figsize=(8, 4))
img = librosa.display.specshow(Sdb, sr=sample_rate, x_axis='time', y_axis='log')
fig.colorbar(img, ax=ax, format="%+2.fdB")
ax.set_ylim(0,8000)
ax.set_xlabel("Time[sec]")
ax.set_ylabel("Frequency [Hz]")
fig.savefig("stft")