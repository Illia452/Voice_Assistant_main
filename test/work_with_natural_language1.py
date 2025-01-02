# # class TransformationLanguage():
# #     pass

# import stanza
# stanza.download('uk')
# nlp = stanza.Pipeline()

# text = 'Коти гуляють по дахах будинків.'
# doc = nlp(text)
# print(doc)

# --------------------------------------------------------------------------------------------------------------------------------
# import re
# nlpp = ("Привіт!!! включи-музику, а також ще щось &2,?")
# nlpp = re.split(r"\W+", nlpp)
# token_text = []
# for i in nlpp:
#     if i.split():
#         token_text.append(i)
# print(token_text)

# -------------------------------------------------------------------------------------------------------------------------------

# import stanza
# nlp = stanza.Pipeline('uk', processors='tokenize,mwt,pos,lemma', download_method=None)
# # mwt - Multi-Word Token Expansion - обробляє багатослівні токени — слова, які складаються з кількох частин
# # pos - Part-of-Speech Tagging - цей процесор визначає частини мови для кожного слова.

# text = "Коти гуляють- по дахах будинків."
# text2 = "Коти гуляють по дахах будинків."
# text3 = "Коти гуляють по дахах будинків."

# # Аналіз тексту
# doc = nlp(text)
# doc2 = nlp(text2)
# doc3 = nlp(text3)

# # Отримуємо леми
# lemmas1 = [word.lemma for sentence in doc.sentences for word in sentence.words]

# print(" ".join(lemmas1))
# lemmas2 = [word.lemma for sentence in doc2.sentences for word in sentence.words]
# print(" ".join(lemmas2))
# lemmas3 = [word.lemma for sentence in doc3.sentences for word in sentence.words]
# print(" ".join(lemmas3))

# # -------------------------------------------------------------------------------------------------------------------------------

# from sparknlp.annotator.lemmatizer  import LemmatizerModel
# from sparknlp.base import Pipeline, LightPipeline
# from sparknlp.base import document_assembler
# # import sparknlp as spark
# from sparknlp.annotator.token import tokenizer
# import pyspark as spark


# lemmatizer = LemmatizerModel.pretrained('lemma_antbnc', 'uk') \
# .setInputCols(["token"]) \
# .setOutputCol("lemma")
# nlp_pipeline = Pipeline(stages=[document_assembler, tokenizer, lemmatizer])
# light_pipeline = LightPipeline(nlp_pipeline.fit(spark.createDataFrame([['']]).toDF("text")))
# results = light_pipeline.fullAnnotate("За винятком того, що є королем півночі, Джон Сноу є англійським лікарем та лідером у розвитку анестезії та медичної гігієни.")

# -------------------------------------------------------------------------------------------------------------------------------

# import pymorphy2
# morph = pymorphy2.MorphAnalyzer(lang='uk')

# # print(morph.parse('коти'))
# print(morph.normal_forms('музики'))

# -------------------------------------------------------------------------------------------------------------------------------

# # import sparknlp
# # from sparknlp.base import *
# # from sparknlp.annotator import *
# from pyspark.sql import SparkSession
# from sparknlp.annotator.lemmatizer  import LemmatizerModel
# from sparknlp.base import Pipeline, LightPipeline
# from sparknlp.base import document_assembler
# # import sparknlp as spark
# from sparknlp.annotator.token import tokenizer
# import pyspark as spark

# # Ініціалізація SparkSession
# spark = SparkSession.builder \
#     .appName("Ukrainian Lemmatizer") \
#     .config("spark.driver.memory", "4G") \
#     .getOrCreate()

# # Тепер можна завантажувати моделі і запускати пайплайн
# lemmatizer = LemmatizerModel.pretrained('lemma_antbnc', 'uk') \
#     .setInputCols(["token"]) \
#     .setOutputCol("lemma")

# nlp_pipeline = Pipeline(stages=[document_assembler, tokenizer, lemmatizer])
# light_pipeline = LightPipeline(nlp_pipeline.fit(spark.createDataFrame([['']]).toDF("text")))
# results = light_pipeline.fullAnnotate("За винятком того, що є королем півночі, Джон Сноу є англійським лікарем та лідером у розвитку анестезії та медичної гігієни.")
# print(results)


import time
import stanza

# Завантажуємо модель для української мови (якщо це ще не зроблено)
# stanza.download('uk')

# Ініціалізація Stanza Pipeline для лемматизації
nlp = stanza.Pipeline('uk', processors='tokenize,mwt,pos,lemma', download_method=None)

# Список тестових текстів
texts = [
    "Ці прекрасні пташки літають високо.",
    "Час від часу я люблю читати книги.",
    "У цей день було дуже спекотно.",
    "Ми вирушаємо в подорож по світу.",
    "Вона працює на важливому проекті.",
    "Морозне повітря п’янить на зиму.",
    "Котик спостерігає за птахами у вікні.",
    "Вони запланували зустріч на завтра.",
    "Вітер приніс запах морської води.",
    "Сонце заходить за гори, і стає темно.",
    "Школярі підготувалися до контрольної роботи.",
    "Цей новий фільм став дуже популярним.",
    "Ми купили квитки на концерт.",
    "Всі готові до важливого змагання.",
    "Насолоджуйтеся відпочинком, поки є час.",
    "Він часто мандрує по різних країнах.",
    "Ми зібралися на пікнік у парку.",
    "У бібліотеці багато цікавих книг.",
    "Кінотеатр наповнений людьми, що чекають на початок сеансу.",
    "Небо покрите хмарами, і ось-ось почнеться дощ."
]

# Змінні для вимірювання часу
total_time = 0
times = []

# Обробляємо кожен текст і вимірюємо час
for i, text in enumerate(texts, 1):
    start_time = time.time()
    
    # Обробляємо текст
    doc = nlp(text)
    
    # Леми для кожного слова в реченні
    lemmas = [word.lemma for sentence in doc.sentences for word in sentence.words]
    
    # Обчислюємо час лемматизації для поточного тексту
    end_time = time.time()
    time_taken = end_time - start_time
    
    # Виводимо результат для кожного тексту
    print(f"Text {i}:")
    print(f"Lemmas: {lemmas}")
    print(f"Time taken: {time_taken:.4f} seconds\n")
    
    # Додаємо час до загальної суми
    total_time += time_taken
    times.append(time_taken)

# Обчислюємо середній час
average_time = total_time / len(texts)

# Виводимо середній час
print(f"Average time for lemmatization: {average_time:.4f} seconds")
