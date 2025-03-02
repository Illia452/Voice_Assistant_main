import time
from rapidfuzz import fuzz
from find_silence import detect_silence
import stanza
from command_execution import MakeCommands


class Work_NL():
    def __init__(self):
        # Завантажуємо модель при умові якщо цього не зроблено(перший запуск програми з інтернетом)
        # stanza.download('uk') 
        # self.nlp = stanza.Pipeline('uk', processors='tokenize,mwt,pos,lemma')


        self.nlp = stanza.Pipeline('uk', processors='tokenize,mwt,pos,lemma', download_method=None)

        
        # download_method - забороняє автоматичне завантаження ресурсів під час виконання pipeline, тобто вмикається офлайн-режим
        # mwt - Multi-Word Token Expansion - обробляє багатослівні токени — слова, які складаються з кількох частин
        # pos - Part-of-Speech Tagging - цей процесор визначає частини мови для кожного слова.

        self.main_list_sentence = []
        self.other_main_sentence = []
        
        self.num = -2
        self.final_MAIN_text = []
        self.possible_worlds = []
        self.make_command = MakeCommands()

    def processing_list(self, list_sentenceForWork):    # обробка списку 

        self.main_sentence = list_sentenceForWork[0]
        

        for sentence_num in range(len(list_sentenceForWork)):
            for i in range(len(list_sentenceForWork[sentence_num])):
                if i < len(self.main_sentence):
                    similarity = (fuzz.ratio(self.main_sentence[i], list_sentenceForWork[sentence_num][i])) 
                    if similarity >= 80: # при умові якщо слова в речені з однаковими індексами мають схожість більше 80% то залишаємо все як є
                        continue   
                    elif 70 < similarity < 80: # якщо ж слово має менше 80% cхожості то замінюємо його з потоку vosk
                        self.main_sentence[i] = list_sentenceForWork[sentence_num][i]
                    elif similarity <= 70:
                        self.possible_worlds.append(list_sentenceForWork[sentence_num][i]) # при умові якщо схожість менше 70% то зберігіємо наше основне речення в основний список речень...
                        self.main_list_sentence.append(self.main_sentence)                 # ...обнуляємо змінну з основним реченням та починаємо з 0 основне речення оскільки є шанс...
                        self.main_sentence = self.possible_worlds                          # ...що це як нове речення або ж команда з нового рядка
                        self.other_main_sentence = []
                        self.possible_worlds = []
                    
                else:
                    for number, item in enumerate(list_sentenceForWork[sentence_num]): # якщо ж кількість слів між потоком vosk та нашим текстом...
                        self.main_sentence.extend(list_sentenceForWork[sentence_num][len(self.main_sentence):]) # ...відрізняється то додаємо залишившусь кількість слів
        self.main_list_sentence.append(self.main_sentence)      


        for text in self.main_list_sentence:
            main_text = ' '.join(text)                          # процес трансформації основних речень в self.main_list_sentence(основному списку) з списку в ""
            doc = self.nlp(main_text)                           # далі лематизація та токенізація
            lemmas = [word.lemma for sentence in doc.sentences for word in sentence.words]   
            self.final_MAIN_text.append(lemmas)

        print("______________________________________________")
        print(self.main_list_sentence)
        print("----------------------------------------------")
        print(self.final_MAIN_text)
        print("______________________________________________")

        self.make_command.analyze_command(self.final_MAIN_text)     # передаємо наш фінальний список основних речень у наступний метод для аналізу 
        self.final_MAIN_text = []
        self.main_list_sentence = []

        


work_NLP = Work_NL()