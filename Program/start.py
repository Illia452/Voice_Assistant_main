import threading
from core.app import UI_MainWindow
from core.speech_recognition_from_Vosk.start_vosk import SpeechRecognition
import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import QThread, QObject


class Vosk_Thread(QObject):
    sr = SpeechRecognition()

    def run(self):
        self.sr.print_text()


if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    ui = UI_MainWindow()
    ui.show()
    vosk_thread = Vosk_Thread()
    vosk_thread.start()
    sys.exit(app.exec_())

    print("ijcm")

    