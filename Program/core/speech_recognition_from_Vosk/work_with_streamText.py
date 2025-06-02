import time
from PyQt5.QtCore import pyqtSignal, QObject, pyqtSlot

class Work_withTexts_FromVosk(QObject):

    start_Push = pyqtSignal()
    close_Push = pyqtSignal()
    google_docs_text_available = pyqtSignal(str)

    def __init__(self):
        super().__init__()
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
        self.pushIS_Active = False


    def check_whether_detectedKW(self, text):
        if self.iSdetect_key_word:
            self.startPushWindow_GetText()
        else:
            self.find_keyWord(text)

    

    def find_keyWord(self, text_from_streamVosk):
        for key_word in self.en_list_key_words:
            if key_word in text_from_streamVosk:
                self.steps_after_DetectKeyWord()
                break

    def steps_after_DetectKeyWord(self):
        self.iSdetect_key_word = True
        self.time_detected_keyword = time.time()
        print("КЛЮЧОВЕ СЛОВО РОЗПІЗНАНО")


    def startPushWindow_GetText(self):
        if self.pushIS_Active == False:
            self.pushIS_Active = True
            time.sleep(1)
            self.start_Push.emit()
            self.time_open_push = time.time()
            time.sleep(0.1)

    
    def wait_signal_for_close_push(self):
        while True:
            if self.pushIS_Active == False:
                self.close_Push.emit()


    
            
            
    
    @pyqtSlot(str) # Декоратор, що вказує, що це слот, який приймає рядок
    def receive_google_docs_text(self, text_content):
        self.google_docs_text_available.emit(text_content)


    # def waitSpeechAfterDetectedKW(self, iStext):
    #     self.time_that_passed = time.time() - self.time_detected_keyword
    #     print(f"ЧАС: {self.time_that_passed} ЧИ Є ТЕКСТ: {iStext}")
    #     if 1.5 <= self.time_that_passed:
    #         if iStext:

    #             time.sleep(2)

    #             #запускаємо мікро в докс
    #         elif iStext != True and 4.8 <= self.time_that_passed:
    #             self.iSdetect_key_word = False
    #             print("ЧАС ОЧІКУВАННЯ МИНУВ")
