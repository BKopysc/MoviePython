from GUI.AutomaticFilmGen import AutomaticFilmGen
#from AutomaticFilm import AutomaticFilmWindow
import os
from PyQt5 import QtCore, QtGui, QtWidgets
import subprocess
import threading

#Tylko z Windowsem !!!
FILEBROWSER_PATH = os.path.join(os.getenv('WINDIR'), 'explorer.exe')

class Ui_Generate(object):
    multi_clips = []
    multi_music = []
    output_path = ""
    max_time = 10.0
    def setupUi(self, Form, multi_clips, multi_music, output_path, max_time):
        self.multi_clips = multi_clips
        self.multi_music = multi_music
        self.output_path = output_path
        self.max_time = max_time
        Form.setObjectName("Form")
        Form.resize(806, 489)
        Form.setFixedSize(806,489)
        Form.setStyleSheet("background:black")
        self.console_text = QtWidgets.QPlainTextEdit(Form)
        self.console_text.setEnabled(False)
        self.console_text.setGeometry(QtCore.QRect(20, 20, 761, 391))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(9)
        self.console_text.setFont(font)
        self.console_text.setStyleSheet("color:white")
        self.console_text.setPlainText("")
        self.console_text.setObjectName("console_text")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 420, 781, 61))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(300, 0, 300, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.watch_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.hide_button = QtWidgets.QPushButton()

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.watch_button.sizePolicy().hasHeightForWidth())
        self.watch_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(19)
        self.watch_button.setFont(font)
        self.watch_button.setStyleSheet("QPushButton{\n"
"background-color: rgb(0, 0, 0);\n"
"border-style:outset;\n"
"border-color: rgb(255, 255, 255);\n"
"border-radius: 8px;\n"
"border-width: 1px;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton::hover{\n"
"background-color:white;\n"
"color: black;\n"
"}\n"
"QPushButton::pressed{\n"
"border-color: black;\n"
"border-width: 3px;\n"
"}")
        self.watch_button.setObjectName("watch_button")
        self.horizontalLayout.addWidget(self.watch_button)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

#---------- Actions
        self.watch_button.clicked.connect(self.start_action)
        #self.hide_button.clicked.connect(self.start_action)
        #self.hide_button.click()
        
    def start_action(self):
        self.start_generating()

    def watch_action(self):
        print("watch")

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Generate Film"))
        self.watch_button.setText(_translate("Form", "Start film!"))

    def print_console(self, line):
        current_text = self.console_text.toPlainText()
        current_text = current_text + line
        self.console_text.setPlainText(current_text)
    

    def gen_func(self,multi_clips, multi_music, output_path, max_time):
        generator = AutomaticFilmGen()
        generator.make_film(multi_clips, multi_music, output_path, max_time)

    def start_generating(self):

        self.console_text.setPlainText("Started process... Please wait...\n")
        thread = threading.Thread(target = self.gen_func, args = (self.multi_clips, self.multi_music, self.output_path, self.max_time,), daemon=True)
        thread.start()
        #generator = AutomaticFilmGen()
        #generator.make_film(self.multi_clips, self.multi_music, self.output_path, self.max_time)
        thread.join()
        text = self.console_text.toPlainText()
        text = text + f"Check your output file!\n{self.output_path} \n"
        #read_str = 'explorer /select, ' + self.output_pat
        subprocess.run([FILEBROWSER_PATH, '/select,', os.path.normpath(self.output_path)])
        self.console_text.setPlainText(text)




# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     Form = QtWidgets.QWidget()
#     ui = Ui_Form()
#     ui.setupUi(Form)
#     Form.show()
#     sys.exit(app.exec_())
