from vosk import Model, KaldiRecognizer
import pyaudio
import numpy as np
import noisereduce as nr
from pydub import AudioSegment
from list_commands import VoiceCommands
from work_NLP import Work_NL
import json
import time
from pydub.utils import db_to_float
import itertools
from find_silence import detect_silence
from rapidfuzz import fuzz
import stanza
from designer_app import Ui_MainWindow
import threading
from PyQt5 import QtWidgets
import sys
from command_execution import MakeCommands


def GUI_Start(recognitionInstance):
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_MainWindow(recognitionInstance)
    ui.MainWindow.show()
    sys.exit(app.exec_())



class SpeechRecognition():
    def __init__(self):
        model = Model(r'..\models\speech_to_text\vosk-model-uk-v3') 
        self.recognizer = KaldiRecognizer(model, 16000) # розпізнавач
        cap = pyaudio.PyAudio()

        self.MIC_IS_OFF = False
        self.START_BUT = True
        self.close_win = False

        self.work_assis = None
        # paInt16 - 16-бітний формат зберігання, frames_per_buffer=2048 - кількість фреймів що зчитуються за один раз        
        self.stream = cap.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=2048)
        self.stream.start_stream()
        self.result = []
        self.voice_commands = VoiceCommands()
        self.work_nl = Work_NL()
        self.make_command = MakeCommands()

        self.output_data=[]
        with open('synonyms.json', 'r', encoding='utf-8') as f:
            self.output_data = json.load(f)

        self.detect_command = False

        self.key_word =["заір","зельфія","опір", "зір зефір", "зір зоря", "зегер", "дзеффіреллі", "зефір",
                         "захід", "з ефір", "ефір", "земфіра", "засіяти", "захир", "захір",
                           "за часів", "часів", "за шию", "зефірс", "захер", "захур", "заньєр", "за кар'єру", "звір"]

        self.time_make_command = 0.0
        self.list_sentence = []
        self.detect_key_world = False
        self.start = 0.0
        self.detect_time = 1
        self.i = 0
        self.found = False
        self.detect_silence = False
        self.list_silence = []


        
    def get_text(self, text):
        self.make_command.text_from_App(text)


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

 
    def delete_key_words_from_begin(self):  # видалення повторів ключовмх слів
        print("ПОЧАТОК ВХОДУ У ЦИКЛ")
        if self.detect_time == 2 and self.i < 7 and self.found == True:
            print("RERERE")
            for word in self.key_word:
                if word in self.text:
                    self.i = self.i + 1 # кількість ключових слів, яка може бути на початку, оскільки в подальшому користувач може використовувати ключове слово
                    self.found = True
                    break
            else:
                self.found = False # якщо уже немає ключових слів на початку речення
                self.i = 0    # __ ПЕРЕВІРИТИ ЧИ ПРАЦЮЄ ЦЯ ЧАСТИНА
        else:
            self.broadcast_recording(self.text)


    def find_key_word(self):    # пошук ключового слова
        for word in self.key_word:
            if word in self.text:
                self.detect_key_world = True
                print("РОЗПІЗНАНО КЛЮЧОВЕ СЛОВО")
                self.start = time.time()
                self.detect_time = 2
                self.found = True
                break
    
    
    def search_silence(self):   # пошук тиші в аудіопотоці
        self.list_silence.append(self.str_audio) # додавання фрагментів після підвищення гучності
        full_audio = sum(self.list_silence) # об'єднання цих фрагментів 
        self.silence = detect_silence(full_audio, min_silence_len=500, silence_thresh=-50, seek_step=100) # налаштування для функції тиші

        for silence in self.silence:
            if (silence[1] - silence[0]) >= 1800: # шукаємо тишу в 1800мс
                print("ЗНАЙДЕНО ТИШУ")
                self.detect_key_world = False # перестаємо записувати нашу команду
                self.detect_silence = True # знайдено тишу
                self.detect_time = 1 # 
                self.list_silence = []
                full_audio = None
                break

    def wait_speech(self): # очікуємо текст після розпізнавання ключових слів
        print("ЧАС ОЧІКУВАННЯ МИНУВ")
        self.detect_key_world = False
        self.start = 0.0
        self.detect_time = 1
        self.i = 0


    def found_silence(self): # дії після знайдення тиші
        self.work_nl.processing_list(self.list_sentence)
        self.list_sentence = []
        self.detect_silence = False


    def broadcast_recording(self, text):    # початок запису мовлення після ключового слова
        self.detect_time = 3 # показуємо що триває запис команди
        self.i = 0
        print("МИ В ЦИКЛІ")
        
        sentence = text.split()
        self.list_sentence.append(sentence)
        print(f"НАША КОМАНДА{self.list_sentence}")


    def analyze_comand(self, res_key):
        if self.detect_time == 3: # якщо триває запис команди
            self.search_silence() # пошук тиші в аудіопотоці

        if time.time() - self.start >= 4.8 and self.detect_time == 2: # якщо користувач не говорить нічого після сказаного ключового слова
            self.wait_speech() # очікуємо текст після розрізнавання ключових слів

        if self.detect_silence == True:
            self.found_silence() # дії після знайдення тиші

        if len(self.result[res_key]) == 0:
            return
        else:
            self.text = (self.result[res_key])
            print(self.text)
               
            if self.detect_key_world == True:
                self.delete_key_words_from_begin() # видалення повторів ключовмх слів
            else:
                self.find_key_word() # пошук ключового слова

        
    

    

    def print_text(self):
        while True:
            if self.close_win == True:
                print("cdcdcfvdtntybvdfcfgbgfdfghgfd")
                break
            if self.MIC_IS_OFF:
                continue
            if self.START_BUT == False:
                self.work_assis = False
                continue
            else:
                if self.work_assis == False:
                    # запуск пакетів
                    self.work_assis = True

            self.delete_noise()
            self.volume_up()



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
time.sleep(1)
gui = threading.Thread(target=GUI_Start, args=(speech_recognition,))
gui.start()
speech_recognition.print_text()