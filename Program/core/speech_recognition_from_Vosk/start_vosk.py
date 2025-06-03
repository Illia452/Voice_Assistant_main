from vosk import Model, KaldiRecognizer
import pyaudio
import numpy as np
import noisereduce as nr
from pydub import AudioSegment
import time
import json
from PyQt5.QtCore import QObject, pyqtSlot, pyqtSignal
from speech_recognition_from_Vosk.work_with_streamText import Work_withTexts_FromVosk


class SpeechRecognition_forKeyWord(QObject):
    

    def __init__(self, control_signals, work_with_text):
        model = Model(r'..\..\models\speech_to_text\vosk-model-small-en-us-0.15')
        self.recognizer = KaldiRecognizer(model, 16000) # розпізнавач
        cap = pyaudio.PyAudio()


        self.stream = cap.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=2048)
        self.stream.start_stream()
        self.detect_stop = False
        self.vosk_running = True
        self.control_signals = control_signals
        self.work_withText = work_with_text


    def delete_noise(self):
        data = self.stream.read(4096) 
        self.masiv = np.frombuffer(data, dtype=np.int16) # Перетворення байтових даних в масив
        # audio_without_noise = nr.reduce_noise(y=masiv, sr=16000) # Зняття шуму з аудіопотоку
        # self.bytes_audio = audio_without_noise.astype(np.int16).tobytes() # Конвертація масиву в байти


    def volume_up(self):
        audio_segment = AudioSegment(
        data=self.masiv,
        sample_width=2,    # 16 бітний формат (= 2 байти)
        frame_rate=16000,   
        channels=1         
        )
        self.str_audio = audio_segment + 10 # підвищення гучності на 10 дец
        audio_np = np.array(self.str_audio.get_array_of_samples(), dtype=np.int16) # перетворення у numpy масив
        self.final_audio = audio_np.tobytes() # перетворення у байти


    def analyze_comand(self, res_key):
        if len(self.result[res_key]) == 0:
            self.text = ""
            self.work_withText.check_whether_detectedKW(self.text)
            return
        else:
            self.text = (self.result[res_key])
            print(self.text)
            self.work_withText.check_whether_detectedKW(self.text)



    def speechToText_Vosk(self):
        if self.recognizer.AcceptWaveform(self.final_audio): 
            rec = self.recognizer.Result()
            self.result = json.loads(rec)
            self.analyze_comand("text")
                                
        else:
            # постійне прослуховування аудіо з реальним виведенням
            rec = self.recognizer.PartialResult()
            self.result = json.loads(rec)
            self.analyze_comand("partial")

    
    def stop_Vosk(self):
        self.vosk_running = False


    def print_text(self):
        while True:
            self.delete_noise()
            self.volume_up()
            self.speechToText_Vosk()
            time.sleep(0.05)

            if self.vosk_running == False:
                break


if __name__ == "__main__":
    speech_recognition = SpeechRecognition_forKeyWord()
    speech_recognition.print_text()