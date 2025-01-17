from pydub import AudioSegment
from pydub.utils import db_to_float
import itertools

# Завантажте файл
audio = AudioSegment.from_file("volume_increased.mp3")

# Виклик функції detect_silence

def detect_silence(audio_segment, min_silence_len=500, silence_thresh=-52, seek_step=100):
    """
    Returns a list of all silent sections [start, end] in milliseconds of audio_segment.
    Inverse of detect_nonsilent()

    audio_segment - the segment to find silence in
    min_silence_len - the minimum length for any silent section
    silence_thresh - the upper bound for how quiet is silent in dFBS
    seek_step - step size for interating over the segment in ms
    """
    seg_len = len(audio_segment)

    # you can't have a silent portion of a sound that is longer than the sound
    if seg_len < min_silence_len:
        return []

    # convert silence threshold to a float value (so we can compare it to rms)
    silence_thresh = db_to_float(silence_thresh) * audio_segment.max_possible_amplitude

    # find silence and add start and end indicies to the to_cut list
    silence_starts = []

    # check successive (1 sec by default) chunk of sound for silence
    # try a chunk at every "seek step" (or every chunk for a seek step == 1)
    last_slice_start = seg_len - min_silence_len
    slice_starts = range(0, last_slice_start + 1, seek_step)

    # guarantee last_slice_start is included in the range
    # to make sure the last portion of the audio is searched
    if last_slice_start % seek_step:
        slice_starts = itertools.chain(slice_starts, [last_slice_start])

    for i in slice_starts:
        audio_slice = audio_segment[i:i + min_silence_len]
        if audio_slice.rms <= silence_thresh:
            silence_starts.append(i)

    # short circuit when there is no silence
    if not silence_starts:
        return []

    # combine the silence we detected into ranges (start ms - end ms)
    silent_ranges = []

    prev_i = silence_starts.pop(0)
    current_range_start = prev_i

    for silence_start_i in silence_starts:
        continuous = (silence_start_i == prev_i + seek_step)

        # sometimes two small blips are enough for one particular slice to be
        # non-silent, despite the silence all running together. Just combine
        # the two overlapping silent ranges.
        silence_has_gap = silence_start_i > (prev_i + min_silence_len)

        if not continuous and silence_has_gap:
            silent_ranges.append([current_range_start,
                                  prev_i + min_silence_len])
            current_range_start = silence_start_i
        prev_i = silence_start_i

    silent_ranges.append([current_range_start,
                          prev_i + min_silence_len])

    return silent_ranges


silences = detect_silence(audio, min_silence_len=1000, silence_thresh=-50, seek_step=100)

# Вивести знайдені діапазони тиші
print(f"Found silent sections: {silences}")




# from pydub import AudioSegment
# from pydub.silence import detect_silence

# # Завантаження аудіо
# audio = AudioSegment.from_file("test_audio3.wav")

# # Вивести інформацію про файл
# print(f"Довжина аудіо: {len(audio) / 1000} сек")
# print(f"Середній рівень звуку: {audio.dBFS} дБ")

# # Автоматичний поріг
# silence_thresh = audio.dBFS - 10  # Рівень тиші трохи нижче середнього рівня
# min_silence_len = 500  # Мінімальна тиша (в мс)
# seek_step = 100  # Крок пошуку (в мс)

# # Визначення тиші
# silent_sections = detect_silence(
#     audio_segment=audio,
#     min_silence_len=min_silence_len,
#     silence_thresh=silence_thresh,
#     seek_step=seek_step
# )

# # Перетворення результатів у секунди
# silent_sections_seconds = [[start / 1000, end / 1000] for start, end in silent_sections]

# # Вивід результатів
# print(f"Знайдені тихі ділянки: {silent_sections_seconds}")





























# import os
# import pyaudio
# import wave
# import numpy as np
# import noisereduce as nr
# from pydub import AudioSegment

# # Параметри для запису аудіо
# FORMAT = pyaudio.paInt16
# CHANNELS = 1
# RATE = 16000
# CHUNK = 1024
# RECORD_SECONDS = 10
# OUTPUT_FOLDER = "processed_audio"

# # Створення папки для збереження файлів, якщо вона не існує
# if not os.path.exists(OUTPUT_FOLDER):
#     os.makedirs(OUTPUT_FOLDER)

# # Запис аудіо
# def record_audio(output_path):
#     p = pyaudio.PyAudio()
    
#     print("Запис аудіо...")
#     stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)
#     frames = []

#     for _ in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
#         data = stream.read(CHUNK)
#         frames.append(data)

#     print("Запис завершено.")
    
#     stream.stop_stream()
#     stream.close()
#     p.terminate()

#     # Збереження аудіо у форматі WAV
#     wav_path = os.path.join(output_path, "raw_audio.wav")
#     wf = wave.open(wav_path, 'wb')
#     wf.setnchannels(CHANNELS)
#     wf.setsampwidth(p.get_sample_size(FORMAT))
#     wf.setframerate(RATE)
#     wf.writeframes(b''.join(frames))
#     wf.close()
    
#     return wav_path

# # Зняття шуму
# def reduce_noise(input_path, output_path):
#     print("Обробка аудіо від шуму...")
#     audio = AudioSegment.from_file(input_path, format="wav")
#     samples = np.array(audio.get_array_of_samples(), dtype=np.int16)
#     reduced_noise = nr.reduce_noise(y=samples, sr=RATE)
    
#     # Збереження обробленого файлу
#     noise_reduced_path = os.path.join(output_path, "noise_reduced.mp3")
#     reduced_audio = AudioSegment(
#         reduced_noise.tobytes(), 
#         frame_rate=RATE, 
#         sample_width=audio.sample_width, 
#         channels=audio.channels
#     )
#     reduced_audio.export(noise_reduced_path, format="mp3")
#     print("Файл без шуму збережено.")
    
#     return noise_reduced_path

# # Підвищення гучності
# def increase_volume(input_path, output_path):
#     print("Підвищення гучності...")
#     audio = AudioSegment.from_file(input_path, format="mp3")
#     louder_audio = audio + 10

#     # Збереження файлу з підвищеною гучністю
#     louder_path = os.path.join(output_path, "volume_increased.mp3")
#     louder_audio.export(louder_path, format="mp3")
#     print("Файл із підвищеною гучністю збережено.")
    
#     return louder_path

# # Основна програма
# if __name__ == "__main__":
#     raw_audio_path = record_audio(OUTPUT_FOLDER)
#     noise_reduced_path = reduce_noise(raw_audio_path, OUTPUT_FOLDER)
#     increase_volume(noise_reduced_path, OUTPUT_FOLDER)
#     print(f"Усі файли збережено в папці: {OUTPUT_FOLDER}")
