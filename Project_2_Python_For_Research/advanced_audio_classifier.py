import os
import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as wav
from scipy.fftpack import fft

AUDIO_FOLDER = "audios"

RANGE_SOUNDS = {
    "Niño/Niña": (250, 400),
    "Mujer": (165, 255),
    "Hombre": (85, 180),
    "Silbido": (1000, 4000),
    "Vidrio Quebrado": (3000, 12000),
    "Campana": (500, 2500),
    "Explosión": (20, 2000),
    "Motor": (50, 500),
    "Ladrido de Perro": (400, 6000),
    "Rayo/Trueno": (20, 200)
}

def classify_sound(f0):
    categories = [category for category, (low, high) in RANGE_SOUNDS.items() if low <= f0 <= high]
    return categories if categories else ["Desconocido"]

audio_name = input("Enter the audio file name (just work with .wav extention): ")

audio_path = os.path.join(AUDIO_FOLDER, audio_name)

try:
    samplerate, data = wav.read(audio_path)

    if len(data.shape) > 1:
        data = data.mean(axis=1)

    data = data / np.max(np.abs(data))

    N = len(data)
    frequencies = np.fft.fftfreq(N, d=1.0 / samplerate)
    fft_values = np.abs(fft(data))

    idx_max = np.argmax(fft_values[:N // 2])
    fundamental_freq = abs(frequencies[idx_max])

    sound_categories = classify_sound(fundamental_freq)

    categories_str = ", ".join(sound_categories)

    plt.figure(figsize=(10, 5))
    plt.plot(frequencies[:N // 2], fft_values[:N // 2])
    plt.xlabel("Frecuencia (Hz)")
    plt.ylabel("Amplitud")
    plt.title(f"Espectro de Frecuencia de '{audio_name}'\nClasificación: {categories_str} (F0 ≈ {fundamental_freq:.2f} Hz)")

    output_image = "frecuencia.png"
    plt.savefig(output_image)
    print(f"Gráfica guardada como '{output_image}'.")
    print(f"Clasificación del audio: {categories_str} (F0 ≈ {fundamental_freq:.2f} Hz)")

except FileNotFoundError:
    print(f"Error: El archivo '{audio_name}' no fue encontrado en la carpeta '{AUDIO_FOLDER}'.")
except Exception as e:
    print(f"Ocurrió un error: {e}")
