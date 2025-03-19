import os
import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as wav
from scipy.fftpack import fft

audio_file = input("Enter the audio file name (just work with .wav extention): ")

samplerate, data = wav.read(audio_file)

if len(data.shape) > 1:
    data = data.mean(axis=1)

data = data / np.max(np.abs(data))

N = len(data)

frequencies = np.fft.fftfreq(N, d=1.0 / samplerate)
fft_values = np.abs(fft(data))

os.makedirs("images", exist_ok=True)
output_image = os.path.join("images", "frequency.png")

plt.figure(figsize=(10, 5))
plt.plot(frequencies[:N // 2], fft_values[:N // 2])
plt.xlabel("Frequency (Hz)")
plt.ylabel("Amplitude")
plt.title(f"Frequency Spectrum of '{audio_file}'")
plt.savefig(output_image)

print(f"Graph saved as '{output_image}'.")
