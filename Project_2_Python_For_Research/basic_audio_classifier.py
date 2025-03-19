import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as wav
from scipy.fftpack import fft

RANGE_VOICES = {
    "Niño": (250, 400),
    "Niña": (250, 400),
    "Mujer": (165, 255),
    "Hombre": (85, 180)
}

def classify_voice(f0):
    for category, (low, high) in RANGE_VOICES.items():
        if low <= f0 <= high:
            return category
    return "Desconocido"

audio_file = input("Enter the audio file name (just work with .wav extention: ")

try:
    samplerate, data = wav.read(audio_file)

    if len(data.shape) > 1:
        data = data.mean(axis=1)

    data = data / np.max(np.abs(data))

    N = len(data)
    frequencies = np.fft.fftfreq(N, d=1.0 / samplerate)
    fft_values = np.abs(fft(data))

    idx_max = np.argmax(fft_values[:N // 2])
    fundamental_freq = abs(frequencies[idx_max])

    voice_type = classify_voice(fundamental_freq)

    plt.figure(figsize=(10, 5))
    plt.plot(frequencies[:N // 2], fft_values[:N // 2])
    plt.xlabel("Frecuencia (Hz)")
    plt.ylabel("Amplitud")
    plt.title(f"Espectro de Frecuencia de '{audio_file}'\nClasificación: {voice_type} (F0 ≈ {fundamental_freq:.2f} Hz)")

    output_image = "frecuencia.png"
    plt.savefig(output_image)
    print(f"Gráfica guardada como '{output_image}'.")
    print(f"Clasificación del audio: {voice_type} (F0 ≈ {fundamental_freq:.2f} Hz)")

except FileNotFoundError:
    print("Error: El archivo no fue encontrado. Verifique el nombre y la ubicación.")
except Exception as e:
    print(f"Ocurrió un error: {e}")
