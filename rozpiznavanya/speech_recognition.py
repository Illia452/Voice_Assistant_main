from vosk import Model, KaldiRecognizer
import pyaudio
import numpy as np
import noisereduce as nr
from pydub import AudioSegment
from commands import * 

model = Model(r'C:\vosk_models_uk\vosk-model-uk-v3') 
recognizer = KaldiRecognizer(model, 16000) # розпізнавач

# paInt16 - 16-бітний формат зберігання, frames_per_buffer=2048 - кількість фреймів що зчитуються за один раз

cap = pyaudio.PyAudio()
stream = cap.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=2048)
stream.start_stream()



while True:
    data = stream.read(4096)

    masiv = np.frombuffer(data, dtype=np.int16) # перетворення байтів в масив

    audio_without_noise = nr.reduce_noise(y=masiv, sr=16000) # зняття шуму з аудіо

    bytes_audio = audio_without_noise.astype(np.int16).tobytes() # конвертація назад в байти

    audio_segment = AudioSegment(
    data=bytes_audio,
    sample_width=2,    # 16 бітний формат (= 2 байти)
    frame_rate=16000,   
    channels=1         
    )
    str_audio = audio_segment + 10 # підвищення гучності на 10 дец

    
    audio_np = np.array(str_audio.get_array_of_samples(), dtype=np.int16) # перетворення numpy масив
    final_audio = audio_np.tobytes() # перетворення у байти


    #if len(data) == 0:  # якщо не надходить звук цикл припиняється
    #    break

    if recognizer.AcceptWaveform(final_audio): 
        rec = recognizer.Result()
        print(recognizer.Result())
        if("скріншот" in rec):
            TakeScreenShot()                        
    else:
        rec = recognizer.PartialResult()
        print(recognizer.PartialResult()) # постійне прослуховування аудіо з реальним виведенням
        if("скріншот" in rec):
            TakeScreenShot()
        

        
        