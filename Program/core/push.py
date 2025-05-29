from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, QTimer
import sys
from PyQt5.QtWidgets import QMainWindow, QLabel
from PyQt5 import QtCore, QtGui, QtWidgets
class PushWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setStyleSheet("background-color: #F7F0FF; border: 2px solid #D8B4FE; border-radius: 12px;")

        # Іконка зефірки
        icon = QLabel()
        icon.setPixmap(QPixmap("../image/icon/zefir.png").scaled(800, 200, Qt.KeepAspectRatio))

        # Текст
        self.label = QLabel("Слухаємо...")
        self.label.setStyleSheet("color: #3B0764; font-size: 16px;")

        # Кнопки
        btn_add = QPushButton("➕")
        btn_add.setStyleSheet("border: none; font-size: 18px;")
        btn_close = QPushButton("🔇")
        btn_close.setStyleSheet("border: none; font-size: 18px;")
        btn_close.clicked.connect(self.close)

        # Розмітка
        vbox_buttons = QVBoxLayout()
        vbox_buttons.addWidget(btn_add)
        vbox_buttons.addWidget(btn_close)

        hbox = QHBoxLayout()
        hbox.addWidget(icon)
        hbox.addWidget(self.label)
        hbox.addLayout(vbox_buttons)

        self.setLayout(hbox)



if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    ui = PushWidget()
    ui.show()
    sys.exit(app.exec_())