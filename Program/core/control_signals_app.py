from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot



class ControlSignals(QObject):
    open_Push = pyqtSignal()
    close_Push = pyqtSignal()
    start_writeText = pyqtSignal()
    stop_writeText = pyqtSignal()
    transfer_text = pyqtSignal(str)

    def __init__(self):
        super().__init__()

    
    def open_PushWindow(self):
        self.open_Push.emit()

    
    def close_PushWindow(self):
        self.close_Push.emit()


    def start_write_text_inPush(self):
        self.start_writeText.emit()


    def stop_write_text_inPush(self):
        self.stop_writeText.emit()


    def transfer_text_toPush(self, text):
        self.transfer_text.emit(text)