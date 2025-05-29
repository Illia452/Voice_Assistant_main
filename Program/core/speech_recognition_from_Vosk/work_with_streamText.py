import time

class Work_withTexts_FromVosk():

    def __init__(self):
        self.uk_list_key_words = ["заір","зельфія","опір", "зір зефір", "зір зоря", "зегер", "дзеффіреллі",
        "зефір","захід", "з ефір", "ефір", "земфіра", "засіяти", "захир", "захір", "за часів","часів",
        "за шию", "зефірс", "захер", "захур", "заньєр", "за кар'єру", "звір", "зір", "жахів", "вже ефір",
        "жаль зір", "вважає р","зір","жаль зір","вже ефір","вже зір","жан-п'єр","ефір","взявши р",
        "режисер","уже","твір","лея","в ефірі","наші","сесій","між ефіру","сім","одесі","це гір","вечір",
        "ігор","жахів","спікер","вже фірм","р","це зір","цей твір","герой"]
        
        self.en_list_key_words = ["the fear", "this year", "is fear", "zero fear", "zephyr",
        "they feed", "the field", "the here", "is here", "effective here", "if is few", "it's a few", "see it", 
        "the ship", "last year", "there's a few", "live here", "the sheer", "they fear",
        "the therefore", "the food", "as i fea", "the share", "they feel", "the feel"]
        self.time_detected_keyword = 0
        self.iSdetect_key_word = False

    def find_keyWord(self, text_from_streamVosk):
        for key_word in self.en_list_key_words:
            if key_word in text_from_streamVosk:
                self.steps_after_DetectKeyWord()
                break

    def steps_after_DetectKeyWord(self):
        self.iSdetect_key_word = True
        self.time_detected_keyword = time.time()
        print("КЛЮЧОВЕ СЛОВО РОЗПІЗНАНО")

    def waitSpeechAfterDetectedKW(self, iStext):
        self.time_that_passed = time.time() - self.time_detected_keyword
        print(f"ЧАС: {self.time_that_passed} ЧИ Є ТЕКСТ: {iStext}")
        if 1.8 <= self.time_that_passed:
            if iStext:
                print("КОМАНДА РОЗПІЗНАНА")
                time.sleep(2)
                self.iSdetect_key_word = False
                #запускаємо мікро в докс
            elif iStext != True and 4.8 <= self.time_that_passed:
                self.iSdetect_key_word = False
                print("ЧАС ОЧІКУВАННЯ МИНУВ")

    def whether_detectedKeyWord(self, text, iStext):
        if self.iSdetect_key_word:
            self.waitSpeechAfterDetectedKW(iStext)
        else:
            self.find_keyWord(text)