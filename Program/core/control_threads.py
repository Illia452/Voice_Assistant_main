from speech_recognition_from_Vosk.start_vosk import SpeechRecognition_forKeyWord
from selenium_window import WindowSelenium
import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import QThread, QObject, pyqtSignal, pyqtSlot
import time


class Vosk_Thread(QObject):

    finished = pyqtSignal()

    def __init__(self):
        super().__init__()

    @pyqtSlot() #показуємо Qt що функція run() буде результатом чогось
    def run(self):
        self.sr = SpeechRecognition_forKeyWord()
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
   

if __name__ == "__main__":
    from app import UI_MainWindow

    app = QtWidgets.QApplication(sys.argv)


    thread_for_Vosk = QThread()
    vosk_worker = Vosk_Thread()
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
    
    ui = UI_MainWindow(vosk_worker, selenium_worker)
    ui.show()


    sys.exit(app.exec_())

    print("ijcm")

    