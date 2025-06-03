import time
from PyQt5.QtCore import pyqtSignal, QObject, pyqtSlot

class Work_withTexts_FromVosk(QObject):


    def __init__(self, control_signals):
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
        self.time_passed_after_openPush = 0
        self.iSdetect_key_word = False
        self.pushIS_Active = False
        self.isText = False
        self.control_signals = control_signals


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
            self.control_signals.open_PushWindow()
            self.time_open_push = time.time()
            time.sleep(0.1)
            self.control_signals.start_write_text_inPush()
        else:
            self.steps_if_PushWindow_active()

    def steps_if_PushWindow_active(self):
        if self.isText == False:
            self.time_passed_after_openPush = time.time() - self.time_open_push
            self.check_how_Many_time_passed_after_openPush()


    def check_how_Many_time_passed_after_openPush(self):
        if self.time_passed_after_openPush >= 4.8:
            self.control_signals.stop_write_text_inPush()
            self.control_signals.close_PushWindow()
            

    def change_status_isText_(self):
        self.isText = True


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
