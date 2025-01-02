from vosk import Model, KaldiRecognizer
import pyaudio
import numpy as np
import noisereduce as nr
from pydub import AudioSegment
from commands import VoiceCommands
import json


class SpeechRecognition():
    def __init__(self):
        model = Model(r'..\models\vosk-model-uk-v3') 
        self.recognizer = KaldiRecognizer(model, 16000) # розпізнавач
        cap = pyaudio.PyAudio()

        # paInt16 - 16-бітний формат зберігання, frames_per_buffer=2048 - кількість фреймів що зчитуються за один раз        

        self.stream = cap.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=2048)
        self.stream.start_stream()
        self.result = []

        self.voice_commands = VoiceCommands()
        
        

    def delete_noise(self):

        data = self.stream.read(4096)
        
        masiv = np.frombuffer(data, dtype=np.int16) # перетворення байтів в масив

        audio_without_noise = nr.reduce_noise(y=masiv, sr=16000) # зняття шуму з аудіо

        self.bytes_audio = audio_without_noise.astype(np.int16).tobytes() # конвертація назад в байти
        
        

    def volume_up(self):
        audio_segment = AudioSegment(
        data=self.bytes_audio,
        sample_width=2,    # 16 бітний формат (= 2 байти)
        frame_rate=16000,   
        channels=1         
        )
        str_audio = audio_segment + 10 # підвищення гучності на 10 дец

        audio_np = np.array(str_audio.get_array_of_samples(), dtype=np.int16) # перетворення у numpy масив
        self.final_audio = audio_np.tobytes() # перетворення у байти

    def analyze_comand(self, res_key):
        if len(self.result[res_key]) == 0:
            return
        else:
            print(self.result[res_key])

            if("скріншот" in self.result[res_key]):
                self.voice_commands.TakeScreenShot()       

    def print_text(self):

        while True:
            
            self.delete_noise()
            self.volume_up()

            #if len(data) == 0:  # якщо не надходить звук цикл припиняється
            #    break

            if self.recognizer.AcceptWaveform(self.final_audio): 
                rec = self.recognizer.Result()
                self.result = json.loads(rec)
                self.analyze_comand("text")
                                  
            else:
                # постійне прослуховування аудіо з реальним виведенням
                rec = self.recognizer.PartialResult()
                self.result = json.loads(rec)
                self.analyze_comand("partial")
                



speech_recognition = SpeechRecognition()
speech_recognition.print_text()
