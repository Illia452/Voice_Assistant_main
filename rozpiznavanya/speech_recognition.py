from vosk import Model, KaldiRecognizer
import pyaudio
import numpy as np
import noisereduce as nr
from pydub import AudioSegment
from commands import VoiceCommands
from work_NLP import Work_NL
import json
import time
from pydub.utils import db_to_float
import itertools
from find_silence import detect_silence
# from work_NLP import Work_NL
from rapidfuzz import fuzz







class SpeechRecognition():
    def __init__(self):
        model = Model(r'..\models\speech_to_text\vosk-model-uk-v3') 
        self.recognizer = KaldiRecognizer(model, 16000) # розпізнавач
        cap = pyaudio.PyAudio()

        # paInt16 - 16-бітний формат зберігання, frames_per_buffer=2048 - кількість фреймів що зчитуються за один раз        

        self.stream = cap.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=2048)
        self.stream.start_stream()
        self.result = []
        self.voice_commands = VoiceCommands()
        self.work_nl = Work_NL()
        # self.work_nlp = Work_NL()

        self.output_data=[]
        with open('synonyms.json', 'r', encoding='utf-8') as f:
            self.output_data = json.load(f)

        self.detect_command = False

        self.key_word =["дзеффіреллі", "зефір", "захід", "з ефір", "ефір", "земфіра", "засіяти", "захир", "захір", "за часів", "часів", "за шию", "зефірс", "захер"]

        self.time_make_command = 0.0
        self.list_sentence = []
        self.detect_key_world = False
        self.start = 0.0
        self.detect_time = 1
        self.i = 0
        self.found = False
        self.detect_silence = False
        self.list_silence = []

        self.time_make_command_scrin = 0.0
        self.time_make_command_browze = 0.0
        self.time_make_command_selectfile = 0.0


        
        
        

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
        if self.detect_time == 3: # якщо триває запис команди
            self.work_nl.search_silence() # пошук тиші в аудіопотоці

        if time.time() - self.start >= 4.8 and self.detect_time == 2: # якщо користувач не говорить нічого після сказаного ключового слова
            self.work_nl.wait_speech() # очікуємо текст після розрізнавання ключових слів

        if self.detect_silence == True:
            self.work_nl.found_silence() # дії після знайдення тиші

        if len(self.result[res_key]) == 0:
            return
        else:
            self.text = (self.result[res_key])
            print(self.text)
               
            if self.detect_key_world == True:
                self.work_nl.delete_key_words_from_begin(self.text, self.key_word) # видалення повторів ключовмх слів
            else:
                self.work_nl.find_key_word(self.text, self.key_word) # пошук ключового слова
    

    

    def print_text(self):

        while True:
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
speech_recognition.print_text()