import time
from rapidfuzz import fuzz
from find_silence import detect_silence
from speech_recognition import SpeechRecognition


class Work_NL():
    def __init__(self):
        pass

    def analyze_key_word(self, text):
        start_time = time.time()
        # while True:
            
            

            
            












        
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