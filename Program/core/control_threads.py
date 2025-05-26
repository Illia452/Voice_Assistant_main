import threading
from app import UI_MainWindow
from speech_recognition_from_Vosk.start_vosk import SpeechRecognition
import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import QThread, QObject, pyqtSignal, pyqtSlot


class Vosk_Thread(QObject):

    finished = pyqtSignal()

    @pyqtSlot() #показуємо Qt що функція run() буде результатом чогось
    def run(self):
        sr = SpeechRecognition()
        sr.print_text()
        self.finished.emit()

def Signall():
    print("КНООПКА")


if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    ui = UI_MainWindow()
    ui.show()

    thread = QThread()

    vosk_thread = Vosk_Thread()

    vosk_thread.moveToThread(thread)

    thread.started.connect(vosk_thread.run)
    vosk_thread.finished.connect(thread.quit)
    vosk_thread.finished.connect(vosk_thread.deleteLater)
    thread.finished.connect(thread.deleteLater)
    ui.Signal_ButtonMicrophone.connect(Signall)

    thread.start()

    sys.exit(app.exec_())

    print("ijcm")

    