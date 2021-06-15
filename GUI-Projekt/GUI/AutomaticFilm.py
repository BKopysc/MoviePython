from GUI.FilmGenerate import Ui_Generate
from GUI.SelectList import Ui_Form
from PyQt5 import QtCore, QtGui, QtWidgets
from os.path import isfile, join
from os import listdir
from pathlib import Path

class Ui_AutomaticFilmWindow(object):
    short_files_names = []
    short_clips_names = None
    short_music_names = None
    clips_dir = ""
    music_dir = ""
    selected_clips = []
    selected_music = []
    output_path = ""
    max_time = 10
    automatic_window = None

    def setupUi(self, AutomaticFilmWindow):
        AutomaticFilmWindow.setObjectName("AutomaticFilmWindow")
        AutomaticFilmWindow.setEnabled(True)
        AutomaticFilmWindow.resize(784, 492)
        AutomaticFilmWindow.setFixedSize(784,492)
        AutomaticFilmWindow.setStyleSheet("background: rgb(0, 0, 0);")
        AutomaticFilmWindow.setDockOptions(QtWidgets.QMainWindow.AllowTabbedDocks|QtWidgets.QMainWindow.AnimatedDocks)
        self.centralwidget = QtWidgets.QWidget(AutomaticFilmWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 30, 481, 20))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setStyleSheet("color:white;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 100, 391, 20))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:white;")
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.line_clips = QtWidgets.QLineEdit(self.centralwidget)
        self.line_clips.setEnabled(True)
        self.line_clips.setGeometry(QtCore.QRect(40, 130, 361, 20))
        self.line_clips.setStyleSheet("background-color:white;")
        self.line_clips.setReadOnly(True)
        self.line_clips.setObjectName("line_clips")
        self.select_clips = QtWidgets.QToolButton(self.centralwidget)
        self.select_clips.setGeometry(QtCore.QRect(420, 130, 31, 21))
        self.select_clips.setStyleSheet("background-color:white")
        self.select_clips.setObjectName("select_clips")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 190, 391, 20))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color:white;")
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.select_music = QtWidgets.QToolButton(self.centralwidget)
        self.select_music.setGeometry(QtCore.QRect(420, 220, 31, 21))
        self.select_music.setStyleSheet("background-color:white")
        self.select_music.setObjectName("select_music")
        self.line_music = QtWidgets.QLineEdit(self.centralwidget)
        self.line_music.setEnabled(True)
        self.line_music.setGeometry(QtCore.QRect(40, 220, 361, 20))
        self.line_music.setStyleSheet("background-color:white;")
        self.line_music.setReadOnly(True)
        self.line_music.setObjectName("line_music")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(40, 280, 391, 20))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:white;")
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.line_output = QtWidgets.QLineEdit(self.centralwidget)
        self.line_output.setEnabled(True)
        self.line_output.setGeometry(QtCore.QRect(40, 310, 361, 20))
        self.line_output.setStyleSheet("background-color:white;")
        self.line_output.setReadOnly(True)
        self.line_output.setObjectName("line_output")
        self.select_output = QtWidgets.QToolButton(self.centralwidget)
        self.select_output.setGeometry(QtCore.QRect(420, 310, 31, 21))
        self.select_output.setStyleSheet("background-color:white")
        self.select_output.setObjectName("select_output")
        self.loadedArea = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.loadedArea.setEnabled(True)
        self.loadedArea.setGeometry(QtCore.QRect(480, 70, 291, 301))
        self.loadedArea.setStyleSheet("background-color:white")
        self.loadedArea.setReadOnly(True)
        self.loadedArea.setObjectName("loadedArea")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(480, 40, 291, 20))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color:white")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(40, 360, 141, 20))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color:white;")
        self.label_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox.setGeometry(QtCore.QRect(170, 360, 62, 22))
        self.doubleSpinBox.setStyleSheet("background:white")
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.doubleSpinBox.setValue(self.max_time)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 400, 781, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(100, 20, 100, 20)
        self.horizontalLayout.setSpacing(50)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.check_files_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.check_files_button.sizePolicy().hasHeightForWidth())
        self.check_files_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)
        self.check_files_button.setFont(font)
        self.check_files_button.setStyleSheet("QPushButton{\n"
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
        self.check_files_button.setObjectName("check_files_button")
        self.horizontalLayout.addWidget(self.check_files_button)
        self.make_movie_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.make_movie_button.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.make_movie_button.sizePolicy().hasHeightForWidth())
        self.make_movie_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)
        self.make_movie_button.setFont(font)
        self.make_movie_button.setStyleSheet("QPushButton{\n"
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
        self.make_movie_button.setObjectName("make_movie_button")
        self.horizontalLayout.addWidget(self.make_movie_button)
        AutomaticFilmWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(AutomaticFilmWindow)
        
#------------Actions
        self.automatic_window = AutomaticFilmWindow
        self.select_clips.clicked.connect(self.select_clips_window)
        self.select_music.clicked.connect(self.select_music_window)
        self.select_output.clicked.connect(self.select_output_window)
        self.check_files_button.clicked.connect(self.check_window)
        self.make_movie_button.clicked.connect(self.make_film_action)


        QtCore.QMetaObject.connectSlotsByName(AutomaticFilmWindow)

    def retranslateUi(self, AutomaticFilmWindow):
        _translate = QtCore.QCoreApplication.translate
        AutomaticFilmWindow.setWindowTitle(_translate("AutomaticFilmWindow", "Automatic Film"))
        self.label.setText(_translate("AutomaticFilmWindow", "Automatic Film Edit"))
        self.label_2.setText(_translate("AutomaticFilmWindow", "Choose clips path:"))
        self.line_clips.setText(_translate("AutomaticFilmWindow", "..."))
        self.select_clips.setText(_translate("AutomaticFilmWindow", "..."))
        self.label_3.setText(_translate("AutomaticFilmWindow", "Choose music path:"))
        self.select_music.setText(_translate("AutomaticFilmWindow", "..."))
        self.line_music.setText(_translate("AutomaticFilmWindow", "..."))
        self.label_4.setText(_translate("AutomaticFilmWindow", "Choose output path:"))
        self.line_output.setText(_translate("AutomaticFilmWindow", "..."))
        self.select_output.setText(_translate("AutomaticFilmWindow", "..."))
        self.loadedArea.setPlainText(_translate("AutomaticFilmWindow", "Waiting for Check"))
        self.label_5.setText(_translate("AutomaticFilmWindow", "Loaded files"))
        self.label_6.setText(_translate("AutomaticFilmWindow", "Max clip duration:"))
        self.check_files_button.setText(_translate("AutomaticFilmWindow", "Check"))
        self.make_movie_button.setText(_translate("AutomaticFilmWindow", "Make movie!"))

    def make_film_action(self):
        full_clips_path = [self.clips_dir + f for f in self.short_clips_names]
        full_music_path = [self.music_dir + f for f in self.short_music_names]
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Generate()
        self.ui.setupUi(self.window, full_clips_path, full_music_path, self.output_path, self.max_time)
        self.window.show()
        self.automatic_window.hide()




        
    def select_clips_window(self):
        folder = str(QtWidgets.QFileDialog.getExistingDirectory(None,"Select Clips Directory"))
        if folder != None:
            self.clips_dir = folder + "/"
            self.line_clips.setText(self.clips_dir)
            allowed_clip_formats = (".MP4", ".AVI", ".OBV",".MOV", ".mp4", ".avi", ".OBV", ".MOV")
            self.open_list_window(self.clips_dir, allowed_clip_formats)
        #print(folder)

    def select_music_window(self):
        folder = str(QtWidgets.QFileDialog.getExistingDirectory(None,"Select Music Directory"))
        if folder != None:
            self.music_dir = folder + "/"
            self.line_music.setText(self.music_dir)
            allowed_music_formats = (".MP3", ".WAV", ".mp3", ".wav")
            self.open_list_window(self.music_dir, allowed_music_formats)
        #print(folder)

    
    def select_output_window(self):
        file_path = ""
        file_path = QtWidgets.QFileDialog.getSaveFileName(None,'Save Output File','',"MP4 (*.mp4);;MOV (*.mov);;AVI (*.avi)")
        print(file_path[0])

        if (''.join(file_path) != ""):
            self.output_path = file_path[0]
            self.line_output.setText(self.output_path)
        else:
            self.output_path = str(Path.home())
        #print(folder)

    def check_window2(self):
        showed_text = ""
        #check clips
        allowed_clip_formats = (".MP4", ".AVI", ".OBV",".MOV", ".mp4", ".avi", ".OBV", ".MOV")
        allowed_music_formats = (".MP3", ".WAV", ".mp3", ".wav")
        clips = []
        for file in listdir(self.clips_dir):
            if file.endswith(allowed_clip_formats):
                clips.append(file)

        self.short_clips_names = clips

        music = []
        for file in listdir(self.music_dir):
            if file.endswith(allowed_music_formats):
                music.append(file)
        self.short_music_names = music

        showed_text = "I Found Clips:\n\n"

        i = 0
        for n in clips:
            text = str(i) + ": " + n + "\n"
            showed_text  = showed_text + text
            i += 1

        showed_text += "\nI Found Music:\n\n"

        i=0
        for n in music:
            text = str(i) + ": " + n + "\n"
            #text = ''.join(text)
            showed_text  = showed_text + text
            i += 1
        
        print(showed_text)

        self.loadedArea.setPlainText(showed_text)
        self.make_movie_button.setEnabled(True)

    def check_window(self):
        if self.short_clips_names == None or self.short_music_names == None:
            self.error_dialog("Check if clips or music are loaded!")
        else:
            showed_text = "Selected Clips:\n\n"

            i = 0
            for n in self.short_clips_names:
                text = str(i) + ": " + n + "\n"
                showed_text  = showed_text + text
                i += 1

            showed_text += "\nSelected Music:\n\n"

            i=0
            for n in self.short_music_names:
                text = str(i) + ": " + n + "\n"
                #text = ''.join(text)
                showed_text  = showed_text + text
                i += 1
            
            print(showed_text)

            self.max_time = round((self.doubleSpinBox.value()),2)

            self.loadedArea.setPlainText(showed_text)
            self.make_movie_button.setEnabled(True)


    def open_list_window(self, path, allowed_formats):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Form()
        self.ui.setupUi(self.window, path, allowed_formats,self)
        self.window.show()

    def get_data(self, files):
        if self.short_clips_names == None:
            self.short_clips_names = files
        else:
            self.short_music_names = files

    def error_dialog(self, message):
        
        app = QtWidgets.QApplication
        error = QtWidgets.QMessageBox()
        error.setIcon(QtWidgets.QMessageBox.Critical)
        error.setWindowTitle("Error has occured")
        error.setText(message)

        error.exec_()
    


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     AutomaticFilmWindow = QtWidgets.QMainWindow()
#     ui = Ui_AutomaticFilmWindow()
#     ui.setupUi(AutomaticFilmWindow)
#     AutomaticFilmWindow.show()
#     sys.exit(app.exec_())
