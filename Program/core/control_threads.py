from app import UI_MainWindow
from speech_recognition_from_Vosk.start_vosk import SpeechRecognition_forKeyWord
import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import QThread, QObject, pyqtSignal, pyqtSlot


class Vosk_Thread(QObject):

    finished = pyqtSignal()

    @pyqtSlot() #показуємо Qt що функція run() буде результатом чогось
    def run(self):
        sr = SpeechRecognition_forKeyWord()
        sr.print_text()
        self.finished.emit()


if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    ui = UI_MainWindow()
    ui.show()


    thread_for_Vosk = QThread()
    vosk_worker = Vosk_Thread()
    vosk_worker.moveToThread(thread_for_Vosk)
    thread_for_Vosk.started.connect(vosk_worker.run)
    vosk_worker.finished.connect(thread_for_Vosk.quit)
    vosk_worker.finished.connect(vosk_worker.deleteLater)
    thread_for_Vosk.finished.connect(thread_for_Vosk.deleteLater)
    thread_for_Vosk.start()
    

    sys.exit(app.exec_())

    print("ijcm")

    