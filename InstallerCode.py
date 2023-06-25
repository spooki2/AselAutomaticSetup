import os
import threading
import webbrowser
import sys
import subprocess
import time
installFinished = False
pyqtFound = False
try:
    subprocess.check_output(['pip', 'show', 'pyqt5'], universal_newlines=True)
    pyqtFound = True
except subprocess.CalledProcessError:
    pyqtFound = False

if not pyqtFound:
    os.system('pip install pyqt5')
from PyQt5 import QtCore, QtGui, QtWidgets
mods = {'opencv-python', 'numpy', 'pyaudio', 'pyqt5'}

buttonCSSinstalling = '''
QPushButton{
	background-color: rgb(149, 149, 149);
	border: 1px rgb(60,60,60);
	color: rgb(59, 59, 59);
	font-size:12;
	border-radius:10px
}
'''
buttonCSS = '''
QPushButton{
	background-color: rgb(35,35,35);
	border: 1px rgb(60,60,60);
	color: white;
	font-size:12;
	highlight: white;
	border-radius:10px
}
QPushButton:hover {
	background-color: rgb(80,80,80);
}
QPushButton:pressed {
	background-color: rgb(40,40,40);
}
'''


class installerClass(object):
    def setupUi(self, installerWindow):
        installerWindow.setObjectName("installerWindow")
        installerWindow.resize(370, 220)
        installerWindow.setStyleSheet("background-color: rgb(51,51,51);")
        self.centralwidget = QtWidgets.QWidget(installerWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 370, 220))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page2 = QtWidgets.QWidget()
        self.page2.setObjectName("page2")
        self.line2 = QtWidgets.QFrame(self.page2)
        self.line2.setGeometry(QtCore.QRect(-30, 60, 401, 20))
        self.line2.setLineWidth(3)
        self.line2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line2.setObjectName("line2")
        self.label4 = QtWidgets.QLabel(self.page2)
        self.label4.setGeometry(QtCore.QRect(10, 70, 351, 101))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label4.setFont(font)
        self.label4.setMouseTracking(True)
        self.label4.setStyleSheet("")
        self.label4.setObjectName("label4")
        self.closeButton = QtWidgets.QPushButton(self.page2)
        self.closeButton.setGeometry(QtCore.QRect(130, 170, 121, 41))
        self.closeButton.setStyleSheet(buttonCSSinstalling)
        self.closeButton.setObjectName("closeButton")
        self.label3 = QtWidgets.QLabel(self.page2)
        self.label3.setGeometry(QtCore.QRect(10, 10, 351, 51))
        self.label3.setObjectName("label3")
        self.stackedWidget.addWidget(self.page2)
        self.page1 = QtWidgets.QWidget()
        self.page1.setObjectName("page1")
        self.label = QtWidgets.QLabel(self.page1)
        self.label.setGeometry(QtCore.QRect(10, 10, 141, 51))
        self.label.setObjectName("label")
        self.line = QtWidgets.QFrame(self.page1)
        self.line.setGeometry(QtCore.QRect(-30, 60, 401, 20))
        self.line.setLineWidth(3)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label2 = QtWidgets.QLabel(self.page1)
        self.label2.setGeometry(QtCore.QRect(10, 80, 351, 101))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label2.setFont(font)
        self.label2.setMouseTracking(True)
        self.label2.setStyleSheet("")
        self.label2.setObjectName("label2")
        self.installButton = QtWidgets.QPushButton(self.page1)
        self.installButton.setGeometry(QtCore.QRect(240, 180, 121, 31))
        self.installButton.setStyleSheet(buttonCSS)
        self.installButton.setObjectName("installButton")
        self.stackedWidget.addWidget(self.page1)
        installerWindow.setCentralWidget(self.centralwidget)

        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(installerWindow)

        self.label4.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; color:#ffffff;\">Asel will now install..</span></p><p align=\"center\"><span style=\" font-size:10pt; color:#ffffff;\">you may close this window after installation.</span></p></body></html>")
        self.closeButton.setText("Installing...")
        self.label3.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600; color:#ffffff;\">Thank You For Installing!</span></p></body></html>")
        self.label.setText("<html><head/><body><p><span style=\" font-size:16pt; font-weight:600; color:#ffffff;\">Asel Installer</span></p></body></html>")
        self.label2.setText("<html><head/><body><p><span style=\" font-size:10pt; color:#ffffff;\">Asel is an app developed by Ben Eshel,</span></p><p><span style=\" font-size:10pt; color:#ffffff;\">it allows users to communicate via text or video chats.</span></p><p><span style=\" font-size:10pt; color:#ffffff;\">in order to install the software on your desktop</span></p><p><span style=\" font-size:10pt; color:#ffffff;\">press the install button.</span></p></body></html>")
        self.installButton.setText("Install")
        def quitAsel():
            if installFinished:
                quit()

        def aselPrep():
            self.stackedWidget.setCurrentIndex(0)
            threading.Thread(target=aselInstall).start()
        def aselInstall():
            for mod in mods:
                os.system(f'pip install {mod}')
            self.closeButton.setText("Close")
            self.closeButton.setStyleSheet(buttonCSS)
            global installFinished
            installFinished = True
            time.sleep(1)
            webbrowser.open('https://github.com/spooki2/Asel/archive/refs/heads/main.zip')

        self.installButton.clicked.connect(aselPrep)
        self.closeButton.clicked.connect(quitAsel)

app = QtWidgets.QApplication(sys.argv)
installerWindow = QtWidgets.QMainWindow()
ui = installerClass()
ui.setupUi(installerWindow)
installerWindow.show()
sys.exit(app.exec_())
