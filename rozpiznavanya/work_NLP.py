import time
from rapidfuzz import fuzz
from find_silence import detect_silence
import stanza


# class Work_NL():
#     def __init__(self):
        
#         self.list_sentence = []
#         self.detect_key_world = False
#         self.start = 0.0
#         self.detect_time = 1
#         self.i = 0
#         self.found = False
#         self.detect_silence = False
#         self.list_silence = []




#     def delete_key_words_from_begin(self, text, key_word):  # видалення повторів ключовмх слів
#         print("ПОЧАТОК ВХОДУ У ЦИКЛ")
#         if self.detect_time == 2 and self.i < 7 and self.found == True:
#             print("RERERE")
#             for word in key_word:
#                 if word in text:
#                     self.i = self.i + 1 # кількість ключових слів, яка може бути на початку, оскільки в подальшому користувач може використовувати ключове слово
#                     self.found = True
#                     break
#             else:
#                 self.found = False # якщо уже немає ключових слів на початку речення
#                 self.i = 0    # __ ПЕРЕВІРИТИ ЧИ ПРАЦЮЄ ЦЯ ЧАСТИНА
#         else:
#             self.broadcast_recording(text)


#     def find_key_word(self, text, key_word):    # пошук ключового слова
#         for word in key_word:
#             if word in text:
#                 self.detect_key_world = True
#                 print("РОЗПІЗНАНО КЛЮЧОВЕ СЛОВО")
#                 self.start = time.time()
#                 self.detect_time = 2
#                 self.found = True
#                 break
    

#     def search_silence(self, str_audio):   # пошук тиші в аудіопотоці
#         self.list_silence.append(str_audio) # додавання фрагментів після підвищення гучності
#         full_audio = sum(self.list_silence) # об'єднання цих фрагментів 
#         self.silence = detect_silence(full_audio, min_silence_len=500, silence_thresh=-50, seek_step=100) # налаштування для функції тиші

#         for silence in self.silence:
#             if (silence[1] - silence[0]) >= 1800: # шукаємо тишу в 1800мс
#                 print("ЗНАЙДЕНО ТИШУ")
#                 self.detect_key_world = False # перестаємо записувати нашу команду
#                 self.detect_silence = True # знайдено тишу
#                 self.detect_time = 1 # 
#                 self.list_silence = []
#                 full_audio = None
#                 break


#     def wait_speech(self): # очікуємо текст після розрізнавання ключових слів
#         print("ЧАС ОЧІКУВАННЯ МИНУВ")
#         self.detect_key_world = False
#         self.start = 0.0
#         self.detect_time = 1
#         self.i = 0


#     def found_silence(self): # дії після знайдення тиші
#         self.processing_list(self.list_sentence)
#         self.detect_silence = False


#     def processing_list(self, list_sentenceForWork):    # обробка списку 
#         pass

#     def broadcast_recording(self, text):    # початок запису мовлення після ключового слова
#         self.detect_time = 3 # показуємо що триває запис команди
#         self.i = 0
#         print("МИ В ЦИКЛІ")
        
#         sentence = text.split()
#         self.list_sentence.append(sentence)
#         print(f"НАША КОМАНДА{self.list_sentence}")
            
    



# work_NLP = Work_NL()



    # def processing_list(self, list_sentenceForWork):    # обробка списку 


    #     # stanza.download('uk') # Завантажуємо модель при умові якщо цього не зроблено(перший запуск програми з інтернетом)

    #     nlp = stanza.Pipeline('uk', processors='tokenize,mwt,pos,lemma', download_method=None)
    #     # download_method - забороняє автоматичне завантаження ресурсів під час виконання pipeline, тобто вмикається офлайн-режим
    #     # mwt - Multi-Word Token Expansion - обробляє багатослівні токени — слова, які складаються з кількох частин
    #     # pos - Part-of-Speech Tagging - цей процесор визначає частини мови для кожного слова.


    #     main_list_sentence = []
    #     other_main_sentence = []
    #     main_sentence = list_sentenceForWork[0]
    #     num = -2
    #     final_MAIN_text = []
    #     possible_worlds = []

    #     for sentence_num in range(len(list_sentenceForWork)):
    #         for i in range(len(list_sentenceForWork[sentence_num])):
    #             if i < len(main_sentence):
    #                 similarity = (fuzz.ratio(main_sentence[i], list_sentenceForWork[sentence_num][i])) 
    #                 if similarity >= 80: # при умові якщо слова в речені з однаковими індексами мають схожість більше 80% то залишаємо все як є
    #                     continue   
    #                 elif 70 < similarity < 80: # якщо ж слово має менше 80% cхожості то замінюємо його з потоку vosk
    #                     main_sentence[i] = list_sentenceForWork[sentence_num][i]
    #                 elif similarity <= 70:
                        
    #                     if num == i - 1:
    #                         possible_worlds.append(list_sentenceForWork[sentence_num][i])
    #                         main_list_sentence.append(main_sentence)
    #                         main_sentence = possible_worlds.copy()
    #                         other_main_sentence = []
    #                     else:
    #                         possible_worlds.append(list_sentenceForWork[sentence_num][i])

    #                         num = i
    #             else:
    #                 for number, item in enumerate(list_sentenceForWork[sentence_num]): # якщо ж кількість слів між потоком vosk та нашим текстом...
    #                     main_sentence.extend(list_sentenceForWork[sentence_num][len(main_sentence):]) # ...відрізняється то додаємо залишившусь кількість слів
    #     main_list_sentence.append(main_sentence)      


    #     for text in main_list_sentence:
    #         main_text = ' '.join(text)
    #         doc = nlp(main_text)
    #         lemmas = [word.lemma for sentence in doc.sentences for word in sentence.words]
    #         final_MAIN_text.append(lemmas)
    #     # 1. додати перевірку other_main_sentence при умові якщо там
    #     #    щось залишається при одноразових спрацювань циклу <60%
    #     # 2. повставляти коментарі які знизу по всьому коду
    #     # 3. вирішити питання звідки хапає звук наш метод тиші


    #     print(main_list_sentence)
    #     print(final_MAIN_text)
