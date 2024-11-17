import librosa
import soundfile as sf
import numpy as np
import noisereduce as nr
import pyaudio
from pydub import AudioSegment


RATE = 16000  # Частота дискретизації
BUFFER = 1024  # Розмір буфера
DURATION = 5  # Тривалість запису в секундах

# Ініціалізація PyAudio для запису аудіо
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=RATE, input=True, frames_per_buffer=BUFFER)

print("Запис почався...")

# Запис аудіо
frames = []
for _ in range(int(RATE / BUFFER * DURATION)):
    data = stream.read(BUFFER)
    frames.append(data)

print("Запис завершено.")

# Зупинка і закриття потоку
stream.stop_stream()
stream.close()
p.terminate()

# Об'єднання фреймів в один масив
audio_data = np.frombuffer(b''.join(frames), dtype=np.int16)

# Збереження оригінального запису
sf.write("original_audio.wav", audio_data, RATE)
print("Оригінальний файл збережено як 'original_audio.wav'.")

# Зменшення шуму за допомогою noisereduce
reduced_noise = nr.reduce_noise(y=audio_data, sr=RATE)
sf.write("reduced_noise_audio.wav", reduced_noise, RATE)  # Збереження після зменшення шуму
print("Файл після зменшення шуму збережено як 'reduced_noise_audio.wav'.")

a = reduced_noise.astype(np.int16).tobytes()
audio_segment = AudioSegment(
    data=a,
    sample_width=2,    # 16-бітний формат (2 байти)
    frame_rate=RATE,   # Частота дискретизації
    channels=1         # Моно
)
new_audioo = audio_segment + 10
new_audioo.export("new_audioo.wav", format="wav")
#sf.write("reduced_noise_audio.wav", new_audioo, RATE)  
print("Файл після зменшення шуму збережено як 'new_audioo'.")


#normalized_audio = librosa.util.normalize(reduced_noise, norm=1, axis=0, fill=False)
#sf.write("normalized_audio.wav", normalized_audio, RATE)  # Збереження після нормалізації
#print("Файл після нормалізації збережено як 'normalized_audio.wav'.")

#--------------------------------------------------------------------------------------------------------------
"""
RATE = 16000  # Частота дискретизації
BUFFER = 1024  # Розмір буфера
DURATION = 5  # Тривалість запису в секундах

# Ініціалізація PyAudio для запису аудіо
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=RATE, input=True, frames_per_buffer=BUFFER)

print("Запис почався...")

# Запис аудіо
frames = []
for _ in range(int(RATE / BUFFER * DURATION)):
    data = stream.read(BUFFER)
    frames.append(data)

print("Запис завершено.")

# Зупинка і закриття потоку
stream.stop_stream()
stream.close()
p.terminate()

# Об'єднання фреймів в один масив
audio_data = np.frombuffer(b''.join(frames), dtype=np.int16)

# Збереження оригінального запису
sf.write("original_audio.wav", audio_data, RATE)
print("Оригінальний файл збережено як 'original_audio.wav'.")

# Зменшення шуму за допомогою noisereduce
reduced_noise = nr.reduce_noise(y=audio_data, sr=RATE)
reduced_noise = reduced_noise.astype(np.float32)
sf.write("reduced_noise_audio.wav", reduced_noise, RATE)  # Збереження після зменшення шуму
print("Файл після зменшення шуму збережено як 'reduced_noise_audio.wav'.")

# Нормалізація
normalized_audio = librosa.util.normalize(reduced_noise, norm=1)
normalized_audio = np.clip(normalized_audio, -1.0, 1.0)
sf.write("normalized_audio.wav", normalized_audio, RATE)  # Збереження після нормалізації
print("Файл після нормалізації збережено як 'normalized_audio.wav'.")"""




"""
RATE = 16000  # Частота дискретизації
BUFFER = 1024  # Розмір буфера
DURATION = 5  # Тривалість запису в секундах

# Ініціалізація PyAudio для запису аудіо
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=RATE, input=True, frames_per_buffer=BUFFER)

print("Запис почався...")

# Запис аудіо
frames = []
for _ in range(int(RATE / BUFFER * DURATION)):
    data = stream.read(BUFFER)
    frames.append(data)

print("Запис завершено.")

# Зупинка і закриття потоку
stream.stop_stream()
stream.close()
p.terminate()

# Об'єднання фреймів в один масив
audio_data = np.frombuffer(b''.join(frames), dtype=np.int16)

# Збереження оригінального запису
sf.write("original_audio.wav", audio_data, RATE)
print("Оригінальний файл збережено як 'original_audio.wav'.")

# Зменшення шуму за допомогою noisereduce
reduced_noise = nr.reduce_noise(y=audio_data.astype(np.float64), sr=RATE)

# Перетворення назад до int16
reduced_noise = np.clip(reduced_noise, -32768, 32767).astype(np.int16)
sf.write("reduced_noise_audio.wav", reduced_noise, RATE)  # Збереження після зменшення шуму
print("Файл після зменшення шуму збережено як 'reduced_noise_audio.wav'.")

# Нормалізація для int16
max_val = np.max(np.abs(reduced_noise))
if max_val > 0:
    normalized_audio = (reduced_noise / max_val * 32767).astype(np.int16)
else:
    normalized_audio = reduced_noise

sf.write("normalized_audio.wav", normalized_audio, RATE)  # Збереження після нормалізації
print("Файл після нормалізації збережено як 'normalized_audio.wav'.")
"""