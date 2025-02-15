# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtGui import QColor, QFont
from PyQt5.QtWidgets import QGraphicsDropShadowEffect
from PyQt5.QtCore import Qt
from PyQt5.QtSvg import QSvgWidget
from PyQt5.QtGui import QPixmap

class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi()
        self.setGeometry(500,150,960,600)

    def setupUi(self):
        self.MainWindow = QtWidgets.QMainWindow()
        self.MainWindow.setObjectName("MainWindow")
        self.MainWindow.resize(960, 600)
        self.MainWindow.setStyleSheet("background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, \n"
                                      "                                stop:0 #F3E8FF, stop:1 #D8B4FE);")
        
        self.centralwidget = QtWidgets.QWidget(self.MainWindow)
        self.centralwidget.setObjectName("centralwidget")




        # кнопка запуску
        self.but_start = QtWidgets.QPushButton(self.centralwidget)
        self.but_start.setGeometry(QtCore.QRect(390, 310, 64, 64))
        self.but_start.setStyleSheet("""
			QPushButton {
				background-color: #c084fc;
				border-radius: 5px;
				border: 1px solid #e1e6ef;
			}
			QPushButton:hover {
                background-color: #a855f7;
									
			}
	    """)
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(15)  # Розмиття
        shadow.setOffset(0, 4)  # Зміщення тіні (по X та Y)
        shadow.setColor(QColor(0, 0, 0, 30))  # Колір тіні (чорний з прозорістю)
        self.but_start.setGraphicsEffect(shadow)
        
        self.but_start.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon/play_regular_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.but_start.setIcon(icon)
        self.but_start.setIconSize(QtCore.QSize(20, 20))
        self.but_start.setObjectName("but_start")
        self.but_start.clicked.connect(self.on_click_but_start)
        self.is_on_but_start = False 
        self.on_click_but_start()

    

        # кнопка мікрофону
        self.but_micro = QtWidgets.QPushButton(self.centralwidget)
        self.but_micro.setGeometry(QtCore.QRect(490, 310, 64, 64))
        self.but_micro.setStyleSheet("""
			QPushButton {
				background-color: #c084fc;
				border-radius: 5px;
				border: 1px solid #e1e6ef;
			}
			QPushButton:hover {
                background-color: #a855f7;
									
			}
        """)
        shadow2 = QGraphicsDropShadowEffect()
        shadow2.setBlurRadius(15)  # Розмиття
        shadow2.setOffset(0, 4)  # Зміщення тіні (по X та Y)
        shadow2.setColor(QColor(0, 0, 0, 30))  # Колір тіні (чорний з прозорістю)
        self.but_micro.setGraphicsEffect(shadow2)
        self.but_micro.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icon/mic_on_regular_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.but_micro.setIcon(icon1)
        self.but_micro.setIconSize(QtCore.QSize(22, 22))
        self.but_micro.setObjectName("but_micro")
        self.but_micro.clicked.connect(self.on_click_but_micro)
        self.is_on_but_micro = False 
        self.on_click_but_micro()




        # кнопка налаштування 
        self.but_setting = QtWidgets.QPushButton(self.centralwidget)
        self.but_setting.setGeometry(QtCore.QRect(20, 30, 35, 40))
        self.but_setting.setStyleSheet("""
			QPushButton {
				background-color: rgb(209, 213, 219);
				border-radius: 5px;
				border: 1px solid #d1d5db;
			}
			QPushButton:hover {
                background-color: #9ca3af;
				border: 1px solid #9ca3af;					
			}
		""")
        shadow3 = QGraphicsDropShadowEffect()
        shadow3.setBlurRadius(15)  # Розмиття
        shadow3.setOffset(0, 4)  # Зміщення тіні (по X та Y)
        shadow3.setColor(QColor(0, 0, 0, 30))  # Колір тіні (чорний з прозорістю)
        self.but_setting.setGraphicsEffect(shadow3)

        self.but_setting.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icon/settings_regular_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.but_setting.setIcon(icon2)
        self.but_setting.setIconSize(QtCore.QSize(20, 20))
        self.but_setting.setObjectName("but_setting")




        # кнопка історія
        self.but_history = QtWidgets.QPushButton(self.centralwidget)
        self.but_history.setGeometry(QtCore.QRect(905, 30, 35, 40))
        self.but_history.setStyleSheet("""
			QPushButton {
				background-color: rgb(209, 213, 219);
				border-radius: 5px;
				border: 1px solid #d1d5db;
			}
			QPushButton:hover {
                background-color: #9ca3af;
				border: 1px solid #9ca3af;					
			}
		""")
        shadow4 = QGraphicsDropShadowEffect()
        shadow4.setBlurRadius(15)  # Розмиття
        shadow4.setOffset(0, 4)  # Зміщення тіні (по X та Y)
        shadow4.setColor(QColor(0, 0, 0, 30))  # Колір тіні (чорний з прозорістю)
        self.but_history.setGraphicsEffect(shadow4)

        self.but_history.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icon/history_regular_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.but_history.setIcon(icon3)
        self.but_history.setIconSize(QtCore.QSize(20, 20))
        self.but_history.setObjectName("but_history")




        # Label
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(400, 30, 151, 41))
        self.label.setStyleSheet("font: 20pt \"Roboto\";\n"
                                 "color: rgb(88, 28, 135);\n"
                                 "background-color: transparent;")
        self.label.setObjectName("label")




        # іконка
        self.image_label = QLabel(self.centralwidget)  # Створюємо новий QLabel
        self.image_label.setGeometry(370, 80, 200, 200)  # Встановлюємо розмір та позицію
        pixmap = QPixmap('icon/zefir.png')  # Завантажуємо зображення
        self.image_label.setPixmap(pixmap)  # Встановлюємо зображення в QLabel
        self.image_label.setScaledContents(True)
        self.image_label.setStyleSheet("""
			QLabel {
				background-color: transparent;
			}
        """)


        # поле вводу
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(230, 450, 500, 48))
        self.lineEdit.setPlaceholderText("Введіть команду вручну...")
        self.lineEdit.setFocusPolicy(Qt.ClickFocus)
        self.lineEdit.setFont(QFont("Roboto", 14))  # Шрифт
        
        
        self.lineEdit.setStyleSheet("""
            QLineEdit {
                background-color: rgb(243, 244, 246);
                border-radius: 10px;
                padding: 5px 45px 5px 10px;
                font-size: 16px;
                border: 1px solid #e5e7eb;                         
            }
            QLineEdit:focus {
                border: 2px solid #a855f7;  /* Бордер з'являється при фокусі */
                background-color: #faf5ff;  /* Легка зміна кольору */
            }
        """)
        
        
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        shadow5 = QGraphicsDropShadowEffect()
        shadow5.setBlurRadius(15)  # Розмиття
        shadow5.setOffset(0, 4)  # Зміщення тіні (по X та Y)
        shadow5.setColor(QColor(0, 0, 0, 30))  # Колір тіні (чорний з прозорістю)
        self.lineEdit.setGraphicsEffect(shadow5)





        # кнопка для надсилання
        self.but_send = QtWidgets.QPushButton(self.centralwidget)
        self.but_send.setGeometry(QtCore.QRect(690, 460, 30, 30))
        self.but_send.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.but_send.setStyleSheet("""
			QPushButton {
				background-color: rgb(243, 244, 246);
                border-radius: 5px;
        	}
            QPushButton:hover {
                background-color: #c0c1c3;  
                                
            }                    
		""")
        self.but_send.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icon/send_regular_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.but_send.setIcon(icon4)
        self.but_send.setObjectName("but_send")




        # Set central widget
        self.MainWindow.setCentralWidget(self.centralwidget)

        # # Status bar
        # self.statusbar = QtWidgets.QStatusBar(self.MainWindow)
        # self.statusbar.setObjectName("statusbar")
        # self.MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self.MainWindow)







    def on_click_but_start(self):
        if self.is_on_but_start:
            self.but_start.setStyleSheet("""
			QPushButton {
				background-color: rgba(140, 210, 205, 0.65);
                border-radius: 5px;
				border: 1px solid #e1e6ef;
			}
            QPushButton:hover {
                background-color: rgba(124, 196, 192, 0.65);
			}
	    """)
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("icon/pause_regular_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.but_start.setIcon(icon)
            self.but_start.setIconSize(QtCore.QSize(20, 20))
        else:
            self.but_start.setStyleSheet("""
			QPushButton {
				background-color: #c084fc;
				border-radius: 5px;
				border: 1px solid #e1e6ef;
			}
			QPushButton:hover {
                background-color: #a855f7;
									
			}
	    """)
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("icon/play_regular_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off) 
            self.but_start.setIcon(icon)
            self.but_start.setIconSize(QtCore.QSize(20, 20))
        self.is_on_but_start = not self.is_on_but_start







    def on_click_but_micro(self):
        if self.is_on_but_micro:
            self.but_micro.setStyleSheet("""
			QPushButton {
				background-color: rgba(230, 160, 160, 0.9);
                border-radius: 5px;
				border: 1px solid #e1e6ef;
			}
            QPushButton:hover {
                background-color: rgba(223, 146, 146, 0.9);
			}
	    """)
            icon1 = QtGui.QIcon()
            icon1.addPixmap(QtGui.QPixmap("icon/mic_off_regular_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.but_micro.setIcon(icon1)
            self.but_micro.setIconSize(QtCore.QSize(22, 22))
        else:
            self.but_micro.setStyleSheet("""
			QPushButton {
				background-color: #c084fc;
				border-radius: 5px;
				border: 1px solid #e1e6ef;
			}
			QPushButton:hover {
                background-color: #a855f7;
									
			}
	    """)
            icon1 = QtGui.QIcon()
            icon1.addPixmap(QtGui.QPixmap("icon/mic_on_regular_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.but_micro.setIcon(icon1)
            self.but_micro.setIconSize(QtCore.QSize(22, 22))
        self.is_on_but_micro = not self.is_on_but_micro





    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Активний"))

if __name__ == "__main__":
    
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_MainWindow()
    ui.MainWindow.show()
    sys.exit(app.exec_())
