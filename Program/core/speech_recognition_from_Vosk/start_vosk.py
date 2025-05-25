from vosk import Model, KaldiRecognizer
import pyaudio
import numpy as np
import noisereduce as nr
from pydub import AudioSegment
import time
import json


class SpeechRecognition():
    def __init__(self):
        model = Model(r'..\models\speech_to_text\vosk-model-uk-v3') 
        self.recognizer = KaldiRecognizer(model, 16000) # розпізнавач
        cap = pyaudio.PyAudio()
        self.stream = cap.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=2048)
        self.stream.start_stream()


    def delete_noise(self):
        data = self.stream.read(4096) 
        masiv = np.frombuffer(data, dtype=np.int16) # Перетворення байтових даних в масив
        audio_without_noise = nr.reduce_noise(y=masiv, sr=16000) # Зняття шуму з аудіопотоку
        self.bytes_audio = audio_without_noise.astype(np.int16).tobytes() # Конвертація масиву в байти


    def volume_up(self):
        audio_segment = AudioSegment(
        data=self.bytes_audio,
        sample_width=2,    # 16 бітний формат (= 2 байти)
        frame_rate=16000,   
        channels=1         
        )
        self.str_audio = audio_segment + 10 # підвищення гучності на 10 дец
        audio_np = np.array(self.str_audio.get_array_of_samples(), dtype=np.int16) # перетворення у numpy масив
        self.final_audio = audio_np.tobytes() # перетворення у байти


    def analyze_comand(self, res_key):
        if len(self.result[res_key]) == 0:
            return
        else:
            self.text = (self.result[res_key])
            print(self.text)


    def print_text(self):
        while True:
            self.delete_noise()
            self.volume_up()

            if self.recognizer.AcceptWaveform(self.final_audio): 
                rec = self.recognizer.Result()
                self.result = json.loads(rec)
                self.analyze_comand("text")
                                  
            # else:
            #     # постійне прослуховування аудіо з реальним виведенням
            #     rec = self.recognizer.PartialResult()
            #     self.result = json.loads(rec)
            #     self.analyze_comand("partial")


if __name__ == "__main__":
    speech_recognition = SpeechRecognition()
    speech_recognition.print_text()