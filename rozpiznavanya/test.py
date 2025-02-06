from rapidfuzz import fuzz
import stanza
import time

stanza.download('uk')

nlp = stanza.Pipeline('uk', processors='tokenize,mwt,pos,lemma', download_method=None)

start = time.time()

list_sentenceForWork = [['один'], ['один', 'два'], ['один', 'два', 'три'], ['один', 'два', 'три', 'чотири'], ['один', 'два', 'три', 'амачмамама'],['один', 'два', 'три', 'амачмамама', 'вьлдмвотм']]

main_list_sentence = []
other_main_sentence = []
main_sentence = list_sentenceForWork[0]
num = -2
final_MAIN_text = []
possible_worlds = []

for sentence_num in range(len(list_sentenceForWork)):
    for i in range(len(list_sentenceForWork[sentence_num])):
        if i < len(main_sentence):
            similarity = (fuzz.ratio(main_sentence[i], list_sentenceForWork[sentence_num][i])) 
            if similarity >= 80: # при умові якщо слова в речені з однаковими індексами мають схожість більше 80% то залишаємо все як є
                continue   
            elif 70 < similarity < 80: # якщо ж слово має менше 80% cхожості то замінюємо його з потоку vosk
                main_sentence[i] = list_sentenceForWork[sentence_num][i]
            elif similarity <= 70:
                
                if num == i - 1:
                    possible_worlds.append(list_sentenceForWork[sentence_num][i])
                    main_list_sentence.append(main_sentence)
                    main_sentence = possible_worlds.copy()
                    other_main_sentence = []
                else:
                    possible_worlds.append(list_sentenceForWork[sentence_num][i])

                    num = i
        else:
            for number, item in enumerate(list_sentenceForWork[sentence_num]): # якщо ж кількість слів між потоком vosk та нашим текстом...
                main_sentence.extend(list_sentenceForWork[sentence_num][len(main_sentence):]) # ...відрізняється то додаємо залишившусь кількість слів
main_list_sentence.append(main_sentence)      


for text in main_list_sentence:
    main_text = ' '.join(text)
    doc = nlp(main_text)
    lemmas = [word.lemma for sentence in doc.sentences for word in sentence.words]
    final_MAIN_text.append(lemmas)
# 1. додати перевірку other_main_sentence при умові якщо там
#    щось залишається при одноразових спрацювань циклу <60%
# 2. повставляти коментарі які знизу по всьому коду
# 3. вирішити питання звідки хапає звук наш метод тиші


print(main_list_sentence)
print(final_MAIN_text)

print(f"НАш час: {time.time()-start}")

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