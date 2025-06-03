from speech_recognition_from_Vosk.start_vosk import SpeechRecognition_forKeyWord
from speech_recognition_from_Vosk.work_with_streamText import Work_withTexts_FromVosk
from selenium_window import WindowSelenium
from getting_text_from_docs import GetTextfromGoogleDocs
import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import QThread, QObject, pyqtSignal, pyqtSlot
import time
from push import PushWindow
from control_signals_app import ControlSignals



class Vosk_Thread(QObject):
    finished = pyqtSignal()
    def __init__(self, control_signals, work_with_text):
        super().__init__()
        self.control_signals = control_signals
        self.sr = SpeechRecognition_forKeyWord(self.control_signals, work_with_text)

    @pyqtSlot() #показуємо Qt що функція run() буде результатом чогось
    def run(self):

        self.sr.print_text()
        self.finished.emit()
    def stopping_process(self):
        if self.sr:
            self.sr.stop_Vosk()




class Selenium_Window_Thread(QObject):
    finished = pyqtSignal()
    def __init__(self, control_signals):
        super().__init__()
        self.control_signals = control_signals

    @pyqtSlot()
    def run(self):
        self.ws = WindowSelenium(self.control_signals)
        self.ws.startWindow()
        self.finished.emit()
    def stopping_process(self):
        if self.ws:
            self.ws.stop_Selenium()




class GetTextFromGoogleDocs_Thread(QObject):
    finished = pyqtSignal()
    def __init__(self, control_signals):
        super().__init__()
        self.control_signals = control_signals

    @pyqtSlot()
    def run(self):
        self.gtts = GetTextfromGoogleDocs(self.control_signals)
        self.gtts.start()
        self.finished.emit()
    def stopping_process(self):
        if self.gtts:
            self.gtts.stop_GetText()
   



if __name__ == "__main__":
    from app import UI_MainWindow

    
    app = QtWidgets.QApplication(sys.argv)


    control_signals = ControlSignals()
    work_with_text = Work_withTexts_FromVosk(control_signals)




    thread_for_Vosk = QThread()
    vosk_worker = Vosk_Thread(control_signals, work_with_text)
    vosk_worker.moveToThread(thread_for_Vosk)
    thread_for_Vosk.started.connect(vosk_worker.run)
    vosk_worker.finished.connect(thread_for_Vosk.quit)
    vosk_worker.finished.connect(vosk_worker.deleteLater)
    thread_for_Vosk.finished.connect(thread_for_Vosk.deleteLater)
    thread_for_Vosk.start()


    thread_for_Selenium = QThread()
    selenium_worker = Selenium_Window_Thread(control_signals)
    selenium_worker.moveToThread(thread_for_Selenium)
    thread_for_Selenium.started.connect(selenium_worker.run)
    selenium_worker.finished.connect(thread_for_Selenium.quit)
    selenium_worker.finished.connect(selenium_worker.deleteLater)
    thread_for_Selenium.finished.connect(thread_for_Selenium.deleteLater)
    thread_for_Selenium.start()



    
    thread_for_GetText = QThread()
    get_text_worker = GetTextFromGoogleDocs_Thread(control_signals)
    get_text_worker.moveToThread(thread_for_GetText)
    thread_for_GetText.started.connect(get_text_worker.run)
    get_text_worker.finished.connect(thread_for_GetText.quit)
    get_text_worker.finished.connect(get_text_worker.deleteLater)
    thread_for_GetText.finished.connect(thread_for_GetText.deleteLater)
    thread_for_GetText.start()

    
    ui = UI_MainWindow(vosk_worker, selenium_worker, get_text_worker)
    ui.show()

    push_window = PushWindow()
    push_window.hide()


    control_signals.open_Push.connect(push_window.animate_show_push)
    control_signals.close_Push.connect(push_window.animate_hide_push)
    control_signals.transfer_text.connect(push_window.print_text)




    sys.exit(app.exec_())

