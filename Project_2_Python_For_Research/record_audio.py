import os
import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd
import scipy.io.wavfile as wav
from scipy.fftpack import fft

DURATION = 10
SAMPLERATE = 41100

os.makedirs("audios", exist_ok=True)
os.makedirs("images", exist_ok=True)

audio_path = os.path.join("audios", "record.wav")
image_path = os.path.join("images", "frequencyRecord.png")

print("start")
audio = sd.rec(int(DURATION * SAMPLERATE), samplerate=SAMPLERATE, channels=1, dtype='int16')
sd.wait()
print("ready")

wav.write(audio_path, SAMPLERATE, audio)

samplerate, data = wav.read(audio_path)
data = data.flatten()

N = len(data)
frequencies = np.fft.fftfreq(N, 1 / samplerate)
fft_values = np.abs(fft(data))

plt.figure(figsize=(10, 5))
plt.plot(frequencies[:N // 2], fft_values[:N // 2])
plt.xlabel("Frequency(Hz)")
plt.ylabel("Amplitude")
plt.title("Voice Frequency Spectrum")
plt.savefig(image_path)

print(f"Graph saved as '{image_path}'.")
