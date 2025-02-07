import time
from rapidfuzz import fuzz
from find_silence import detect_silence
from speech_recognition import SpeechRecognition
import stanza


class Work_NL():
    def __init__(self):

        self.list_sentence = []
        self.detect_key_world = False
        self.start = 0.0
        self.detect_time = 1
        self.i = 0
        self.found = False
        self.detect_silence = False
        self.list_silence = []




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
                break


    def wait_speech(self): # очікуємо текст після розрізнавання ключових слів
        print("ЧАС ОЧІКУВАННЯ МИНУВ")
        self.detect_key_world = False
        self.start = 0.0
        self.detect_time = 1
        self.i = 0


    def found_silence(self): # дії після знайдення тиші
        self.processing_list(self.list_sentence)
        self.detect_silence = False


    def processing_list(self, list_sentenceForWork):    # обробка списку 
        numberOFsentence = len(list_sentenceForWork) # кількість речень
        main_sentence = list_sentenceForWork[0] 

        for sentence in list_sentenceForWork:
            for word, main_word in sentence, main_sentence:
                similarity = (fuzz.ratio())


    def broadcast_recording(self, text):    # початок запису мовлення після ключового слова
        self.detect_time = 3 # показуємо що триває запис команди
        self.i = 0
        print("МИ В ЦИКЛІ")
        
        sentence = text.split()
        self.list_sentence.append(sentence)
        print(f"НАША КОМАНДА{self.list_sentence}")
            
    
    def processing_list(self, list_sentenceForWork):    # обробка списку 
        numberOFsentence = len(list_sentenceForWork) # кількість речень
        main_sentence = list_sentenceForWork[0] 

        for sentence in list_sentenceForWork:
            for word, main_word in sentence, main_sentence:
                similarity = (fuzz.ratio())





        
        # while True:
        #     if len(self.text_command) != 0:
        #         break
        #     elif time.time() >= start_time + 4.8:
        #         return
        #     else:
        #         continue

        while True:
            text = self.result.get("text", "")
            partial = self.result.get("partial", "")

            if not text and not partial:
                continue
            if "зефір" in text or "зефір" in partial:
                continue
            
            self.text_vosk_text = text
            self.text_vosk_partial = partial 
            print("Вхід в цикл")

            if len(self.text_vosk_partial) != 0:
                self.text_vosk = self.text_vosk_partial
                
            else:
                self.text_vosk = self.text_vosk_text

            doc1 = self.nlp(self.text_vosk)
            self.text_vosk = []
            self.text_vosk_partial = []
            self.text_vosk_text = []

            tokens1 = [word.text for sentence in doc1.sentences for word in sentence.words]

            for i in range(len(tokens1)):
                if i < len(self.text_command):
                    similarity = (fuzz.ratio(self.text_command[i], tokens1[i])) 
                    if similarity >= 80: # при умові якщо слова в речені з однаковими індексами мають схожість більше 80% то залишаємо все як є
                        continue   
                    elif similarity <= 79: # якщо ж слово має менше 80% cхожості то замінюємо його з потоку vosk
                        self.text_command[i] = tokens1[i]
                    elif similarity <=60:
                        self.text_command.insert(i+1, tokens1[i]) # якщо ж слово має схожість менше 60%, додаємо це слово поряд
                else:                                               # є шанс що це нова команда
                    for number, item in enumerate(tokens1): # якщо ж кількість слів між потоком vosk та нашим текстом відрізняється...
                        self.text_command.extend(tokens1[len(self.text_command):]) # ...то додаємо кількість слів яка залишилась
            if self.detect == True:
                return
            print(f"Кількість слів: {self.text_command}")
            if len(self.text_command) != 0:
                print(f"Result: {self.text_command}")
                while True:

                    self.list_silence.append(self.str_audio) # додавання фрагментів після підвищення гучності
                    full_audio = sum(self.list_silence) # об'єднання цих фрагментів 
                    self.silence = detect_silence(full_audio, min_silence_len=500, silence_thresh=-50, seek_step=100) # налаштування для функції тиші

                    for silence in self.silence:
                        if (silence[1] - silence[0]) >= 1800:
                            print(f"НАША КОМАНДА: {self.text_command}")
                            self.detect = True
                            break
                            
                    print(f"НАША КОМАНДА: {self.text_command}")
                    return  