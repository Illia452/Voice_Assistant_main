import stanza
import json
import sqlite3
from rapidfuzz import fuzz
import time

# Завантажуємо модель при умові якщо цього не зроблено
# stanza.download('uk')
# download_method - забороняє автоматичне завантаження ресурсів під час виконання pipeline, тобто вмикається офлайн-режим
# mwt - Multi-Word Token Expansion - обробляє багатослівні токени — слова, які складаються з кількох частин
# pos - Part-of-Speech Tagging - цей процесор визначає частини мови для кожного слова

# nlp = stanza.Pipeline('uk', processors='tokenize,mwt,pos,lemma', download_method=None)

# text_command= ['зроби', 'будь', 'ласка', 'знімок', 'екрану']
# sentence = ' '.join(text_command)  


# mytable = str.maketrans(" ", " ", "./,-")
# # перше значення що саме ми хочемо замінити
# # чим саме ми хочемо замінити перше значення
# # що ми хочемо видалити

# clear_text = sentence.translate(mytable) # очищення слів від ,-/.

# doc = nlp(clear_text) 

# lemmas = [word.lemma for sentence in doc.sentences for word in sentence.words]


# output_data=[]
# with open('synonyms.json', 'r', encoding='utf-8') as f:
#     output_data = json.load(f)


#  """# for key, vallue in self.output_data.items():
#         #     for values in vallue:
#         #         if values in self.result[res_key]:
#         #             print(f"НАША КОМАНДА {values}")
#         #             self.list_command.append(values)
#         #             print(f"Наш список зафіксованих команд:{self.list_command}")
#         #               # зупиняємо цикл після знаходження першої команди"""



# found_synonyms = []
# for synonym in scrin:
#     if synonym in sentence:
#         found_synonyms.append(synonym)

# if found_synonyms:
#     print(f"Знайдено синоніми в реченні: {', '.join(found_synonyms)}")
# else:
#     print("Синонімів не знайдено в реченні.")








# ____________________________________________________________________________________________________________________________
# unique_set = {
#     "екранний зйомка", "екранний знімок", "екранний зображення", 
#     "екранний копія", "екранний світлина", "екранний скрін", 
#     "екранний скріна", "екранний фото", "екранний фотографія", 
#     "зйомка екран", "знімок", "знімок вікно", "знімок дисплей", 
#     "знімок диспло", "знімок екран", "знімок монітор", 
#     "зображення дисплей", "зображення екран", "зображення монітор", 
#     "картинка екран", "картинка монітор", "скриншот", 
#     "скрін", "скрін екран", "скріна", "скріна екран", 
#     "скріншот", "скріншот вікно", "скріншот екран", 
#     "скріншот монітор", "фото дисплей", "фото диспло", 
#     "фото екран", "фото екранний вміст", "фотографія екран"
# }


# a = "знімок екран"
# if a in unique_set:
#     print("Знайдено!")
# else:
#     print("Не знайдено!")






# scrin = [
#         "екранний зйомка", "екранний знімок", "екранний зображення", 
#         "екранний копія", "екранний світлина", "екранний скрін", 
#         "екранний скріна", "екранний фото", "екранний фотографія", 
#         "зйомка екран", "знімок", "знімок вікно", "знімок дисплей", 
#         "знімок диспло", "знімок екран", "знімок монітор", 
#         "зображення дисплей", "зображення екран", "зображення монітор", 
#         "картинка екран", "картинка монітор", "скриншот", 
#         "скрін", "скрін екран", "скріна", "скріна екран", 
#         "скріншот", "скріншот вікно", "скріншот екран", 
#         "скріншот монітор", "фото дисплей", "фото диспло", 
#         "фото екран", "фото екранний вміст", "фотографія екран"
#     ]


# print(len(scrin))

    
# text2 = []
# nlp = stanza.Pipeline('uk', processors='tokenize', download_method=None) 

# text_vosk = "кіт їсть торт і плаче"
# doc1 = nlp(text_vosk)

# tokens1 = [word.text for sentence in doc1.sentences for word in sentence.words]



# for i in range(len(tokens1)):
#     if i < len(text2):
#         similarity = (fuzz.ratio(text2[i], tokens1[i])) 
#         if similarity >= 80: # при умові якщо слова в речені з однаковими індексами мають схожість більше 80% то залишаємо все як є
#             continue   
#         elif similarity <= 79: # якщо ж слово має менше 80% cхожості то замінюємо його з потоку vosk
#             text2[i] = tokens1[i]
#     else:
#         for number, item in enumerate(tokens1): # якщо ж кількість слів між потоком vosk та нашим текстом...
#             text2.extend(tokens1[len(text2):]) # ...відрізняється то додаємо залишившусь кількість слів


# print(text2)







# # Завантажуємо модель при умові якщо цього не зроблено
# stanza.download('uk')

# nlp = stanza.Pipeline('uk', processors='tokenize,mwt,pos,lemma', download_method=None) 
# # download_method - забороняє автоматичне завантаження ресурсів під час виконання pipeline, тобто вмикається офлайн-режим
# # mwt - Multi-Word Token Expansion - обробляє багатослівні токени — слова, які складаються з кількох частин
# # pos - Part-of-Speech Tagging - цей процесор визначає частини мови для кожного слова.

# text = "скріншот, знімок екран, екранний копія, скрін, знімок, картинка екран, знімок екран, фото екран, скріншот екран, скриншот, знімок монітор, картинка екран, знімок дисплей, екранний зображення, зображення екран, зображення монітор, екранний зйомка, екранний знімок, знімок екран, знімок екран, фото дисплей, фото екран, картинка монітор, екранний фотографія, скріншот монітор, скрін екран, екранний фото, зображення екран, фото екран, знімок екран, знімок дисплей, знімок вікно, екранний світлина, скріншот вікно, картинка екран, фото екранний вміст, зйомка екран, зображення дисплей, екранний знімок, фотографія екран, скріншот екран, екранний зйомка,екранний скрін, фото екран"


# mytable = str.maketrans(" ", " ", "./,-")
# # перше значення що саме ми хочемо замінити
# # чим саме ми хочемо замінити перше значення
# # що ми хочемо видалити

# clear_text = text.translate(mytable) # очищення слів від ,-/.

# doc = nlp(clear_text) 

# lemmas = [word.lemma for sentence in doc.sentences for word in sentence.words]
# print(lemmas)



# # mytable = str.maketrans(",", "-")
# # print(txt.translate(mytable))

# from rapidfuzz import fuzz
# print(fuzz.ratio("кіт їх", "кіт їх торт"))

# кіт
# кіт їх
# кіт їх торт
# кіт їх торт і
# кіт їх торт і плаче
# кіт їх торт і плаче
# кіт їх торт і плаче
# кіт їсть торт і плач

"""    def analyze_key_word(self):
        start_time = time.time()
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
"""






    # def key_word_commands(self, res_key):
    #     print("УВІЙШЛО")
    #     self.start = time.time()
    #     self.detect_command = True
    #     self.detect_c(res_key)
    #     if time.time() - self.start >= 3.2:
    #         print(f"Команда: {self.list_command_orig}")

    #     for key, vallue in self.output_data.items():
    #         for values in vallue:
    #             if values in self.result[res_key]:
    #                 print(f"НАША КОМАНДА {values}")
    #                 self.list_command.append(values)
    #                 print(f"Наш список зафіксованих команд:{self.list_command}")
    #                   # зупиняємо цикл після знаходження першої команди
    # def detect_c(self, res_key):
    #     if self.detect_command == True:
    #         self.list_command = self.list_command + " " + self.result[res_key]
    #     if time.time() - self.start >= 3:
    #         self.detect_command = False
    #         self.list_command_orig = self.list_command
    #         self.list_command = ""
                

    # def analyze_comand(self, res_key):
    #     if len(self.result[res_key]) == 0:
    #         return
    #     # else:
    #     #     print(self.result[res_key])
        
    #     if self.time_make_command == 0.0 or time.time() - self.time_make_command > 3:
    #         for word in self.key_word:
    #             if word in self.result[res_key]:
    #                 self.key_word_commands(res_key)
    #                 self.time_make_command = time.time()  # оновлюємо час після виконання команди
    #                 break  # зупиняємо цикл після першої виконаної команди
                            

    #     if "скріншот" in self.result[res_key]:
    #         self.voice_commands.TakeScreenShot()
    #     if 'відкрити браузер' in self.result[res_key]:
    #         self.voice_commands.OpenBrowser()


#     "select_file" : [
#         "поточний", "поточити файл", "оточений файл", "поточних файл", "поточних", 
#         "поточний файл",
#         "теперішній файл",
#         "активний файл",
#         "файл, що відкритий зараз",
#         "файл, що використовується",
#         "поточний документ",
#         "чинний файл",
#         "цей файл",
#         "цей документ",
#         "вказаний файл",
#         "конкретний файл",
#         "даний файл",
#         "цей конкретний файл"
#     ]

# }
