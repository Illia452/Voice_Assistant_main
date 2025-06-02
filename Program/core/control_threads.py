from speech_recognition_from_Vosk.start_vosk import SpeechRecognition_forKeyWord
from speech_recognition_from_Vosk.work_with_streamText import Work_withTexts_FromVosk
from selenium_window import WindowSelenium
from getting_text_from_docs import GetTextfromGoogleDocs
import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import QThread, QObject, pyqtSignal, pyqtSlot
import time
from push import PushWindow


class Vosk_Thread(QObject):

    finished = pyqtSignal()

    def __init__(self, work_with_text):
        super().__init__()
        self.work_WithText = work_with_text

    @pyqtSlot() #показуємо Qt що функція run() буде результатом чогось
    def run(self):
        self.sr = SpeechRecognition_forKeyWord(self.work_WithText)
        self.sr.print_text()
        self.finished.emit()

    def stopping_process(self):
        if self.sr:
            self.sr.stop_Vosk()

class Selenium_Window_Thread(QObject):

    finished = pyqtSignal()

    def __init__(self):
        super().__init__()

    @pyqtSlot()
    def run(self):
        self.ws = WindowSelenium()
        self.ws.startWindow()
        self.finished.emit()

    def stopping_process(self):
        if self.ws:
            self.ws.stop_Selenium()

class GetTextFromGoogleDocs_Thread(QObject):

    finished = pyqtSignal()

    def __init__(self, work_with_text):
        super().__init__()
        self.work_WithText = work_with_text

    @pyqtSlot()
    def run(self):
        self.gtts = GetTextfromGoogleDocs(self.work_WithText)
        self.gtts.start()
        self.finished.emit()

    def stopping_process(self):
        if self.gtts:
            self.gtts.stop_GetText()
   

if __name__ == "__main__":
    from app import UI_MainWindow

    
    app = QtWidgets.QApplication(sys.argv)


    


    work_with_text = Work_withTexts_FromVosk()

    thread_for_Vosk = QThread()
    vosk_worker = Vosk_Thread(work_with_text)
    vosk_worker.moveToThread(thread_for_Vosk)
    thread_for_Vosk.started.connect(vosk_worker.run)
    vosk_worker.finished.connect(thread_for_Vosk.quit)
    vosk_worker.finished.connect(vosk_worker.deleteLater)
    thread_for_Vosk.finished.connect(thread_for_Vosk.deleteLater)
    thread_for_Vosk.start()


    thread_for_Selenium = QThread()
    selenium_worker = Selenium_Window_Thread()
    selenium_worker.moveToThread(thread_for_Selenium)
    thread_for_Selenium.started.connect(selenium_worker.run)
    selenium_worker.finished.connect(thread_for_Selenium.quit)
    selenium_worker.finished.connect(selenium_worker.deleteLater)
    thread_for_Selenium.finished.connect(thread_for_Selenium.deleteLater)
    thread_for_Selenium.start()



    
    thread_for_GetText = QThread()
    get_text_worker = GetTextFromGoogleDocs_Thread(work_with_text)
    get_text_worker.moveToThread(thread_for_GetText)
    thread_for_GetText.started.connect(get_text_worker.run)
    get_text_worker.finished.connect(thread_for_GetText.quit)
    get_text_worker.finished.connect(get_text_worker.deleteLater)
    thread_for_GetText.finished.connect(thread_for_GetText.deleteLater)
    thread_for_GetText.start()

    
    ui = UI_MainWindow(vosk_worker, selenium_worker, get_text_worker)
    ui.show()

    push_window = PushWindow(vosk_worker)
    push_window.hide()



    work_with_text.start_Push.connect(push_window.animate_show_push)
    # work_with_text.start_print_textInPush.connect(get_text_worker.active_push)
    work_with_text.google_docs_text_available.connect(push_window.print_text)
    work_with_text.close_Push.connect(push_window.animate_hide_push)



    sys.exit(app.exec_())

