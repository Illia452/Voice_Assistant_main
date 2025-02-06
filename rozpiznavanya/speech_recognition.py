from vosk import Model, KaldiRecognizer
import pyaudio
import numpy as np
import noisereduce as nr
from pydub import AudioSegment
from commands import VoiceCommands
import json
import time
from pydub.utils import db_to_float
import itertools
from find_silence import detect_silence
# from work_NLP import Work_NL







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


    def processing_list(self, list_sentenceForWork):
        len_sentence = len(list_sentenceForWork)
        main_sentence = list_sentenceForWork[0]
        for sentence in list_sentenceForWork:


    def key_word_commands(self, text):
        self.detect_time = 3
        self.i = 0
        print("МИ В ЦИКЛІ")
        
                       
        sentence = text.split()
        self.list_sentence.append(sentence)
        print(f"НАША КОМАНДА{self.list_sentence}")
            
        
        

        # for key, vallue in self.output_data.items():
        #     for values in vallue:
        #         if values in self.text:
        #             print(f"НАША КОМАНДА {values} з ключа {key}")     

    def analyze_comand(self, res_key):
        if self.detect_time == 3:
            self.list_silence.append(self.str_audio) # додавання фрагментів після підвищення гучності
            full_audio = sum(self.list_silence) # об'єднання цих фрагментів 
            self.silence = detect_silence(full_audio, min_silence_len=500, silence_thresh=-50, seek_step=100) # налаштування для функції тиші

            for silence in self.silence:
                if (silence[1] - silence[0]) >= 1800:
                    print("ЗНАЙДЕНО ТИШУ")
                    self.detect_key_world = False
                    self.detect_silence = True
                    self.detect_time = 1
                    break
        if time.time() - self.start >= 4.8 and self.detect_time == 2:
            print("ЧАС ОЧІКУВАННЯ МИНУВ")
            self.detect_key_world = False
            self.start = 0.0
            self.detect_time = 1
            self.i = 0
        if self.detect_silence == True:
            self.processing_list(self.list_sentence)
            self.detect_silence = False
            # тут буде викликатися обробка вкладених словників
        if len(self.result[res_key]) == 0:
            return
        else:
            self.text = (self.result[res_key])
            print(self.text)

            if self.detect_key_world == True:
                print("ПОЧАТОК ВХОДУ У ЦИКЛ")
                if self.detect_time == 2 and self.i < 7 and self.found == True:
                    print("RERERE")
                    for word in self.key_word:
                        if word in self.text:
                            self.i = self.i + 1
                            self.found = True
                            break
                    else:
                        self.found = False
                        self.i = 0    # __ ПЕРЕВІРИТИ ЧИ ПРАЦЮЄ ЦЯ ЧАСТИНА
                else:
                    self.key_word_commands(self.text)
                    
# ------------------------------------------------------------------------------------------------------
# 1. Перевірити чи працює код на 141
# 2. Почати писати обробку вкладених словників на 125 
# 3. Продовжити писати код за планом
# 4. Зформувати гарний чистий код по функція
# ------------------------------------------------------------------------------------------------------

            else:
                for word in self.key_word:
                    if word in self.text:
                        self.detect_key_world = True
                        print("РОЗПІЗНАНО КЛЮЧОВЕ СЛОВО")
                        self.start = time.time()
                        self.detect_time = 2
                        self.found = True
                        break


        # if self.time_make_command == 0.0 or time.time() - self.time_make_command > 3:
        #     for word in self.key_word:
        #         if word in self.text:
        #             self.work_nlp.analyze_key_word(self.text)
        #             self.time_make_command = time.time()  # оновлюємо час після виконання команди
        #             break  # зупиняємо цикл після першої виконаної команди

        # if self.detect_command == True:
        #     for key, vallue in self.output_data.items():
        #         for values in vallue:
        #             if values in self.text:
        #                 print(f"НАША КОМАНДА {values} з ключа {key}")
        #                 if key == "scrin" and (self.time_make_command_scrin == 0.0 or time.time() - self.time_make_command_scrin > 3):
        #                     self.voice_commands.TakeScreenShot()
        #                     self.time_make_command_scrin = time.time()
        #                 elif key == "open_browser" and (self.time_make_command_browze == 0.0 or time.time() - self.time_make_command_browze > 3):
        #                     self.voice_commands.OpenBrowser()
        #                     self.time_make_command_browze = time.time()
                        
                        # elif key == "select_file" and (self.time_make_command_browze == 0.0 or time.time() - self.time_make_command_browze > 2):
                        #     self.voice_commands.SelectFile()
                        #     self.time_make_command_selectfile = time.time()


                        
                            

    

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