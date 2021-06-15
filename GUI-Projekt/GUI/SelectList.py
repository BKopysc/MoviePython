from PyQt5 import QtCore, QtGui, QtWidgets
from os import listdir


class Ui_Form(object):
    dir_path = ""
    allowed_formats = ()
    files = []
    set_form = None
    set_prev_window = None

    def setupUi(self, Form, path, allowed_formats, Prev_Window):
        self.set_prev_window = Prev_Window
        Form.setObjectName("Select Files")
        Form.resize(790, 462)
        Form.setFixedSize(790,462)
        self.set_form = Form
        self.choice_list = QtWidgets.QListWidget(Form)
        self.choice_list.setGeometry(QtCore.QRect(40, 50, 311, 351))
        self.choice_list.setObjectName("choice_list")
        self.choice_list.setDragDropMode(QtWidgets.QAbstractItemView.DragDrop)
        #self.choice_list.setDefaultDropAction(QtCore.Qt.Move
        self.choice_list.setDefaultDropAction(QtCore.Qt.MoveAction)

        self.selected_list = QtWidgets.QListWidget(Form)
        self.selected_list.setGeometry(QtCore.QRect(440, 50, 311, 351))
        self.selected_list.setObjectName("selected_list")
        self.selected_list.setDragDropMode(QtWidgets.QAbstractItemView.DragDrop)
        self.selected_list.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.selected_list.setAcceptDrops(True)

        self.select_all_button = QtWidgets.QPushButton(Form)
        self.select_all_button.setGeometry(QtCore.QRect(360, 200, 71, 21))
        self.select_all_button.setObjectName("select_all_button")
        self.unselect_all_button = QtWidgets.QPushButton(Form)
        self.unselect_all_button.setGeometry(QtCore.QRect(360, 240, 71, 23))
        self.unselect_all_button.setObjectName("unselect_all_button")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 10, 791, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.ok_button = QtWidgets.QPushButton(Form)
        self.ok_button.setGeometry(QtCore.QRect(300, 420, 75, 23))
        self.ok_button.setObjectName("ok_button")
        self.cancel_button = QtWidgets.QPushButton(Form)
        self.cancel_button.setGeometry(QtCore.QRect(420, 420, 75, 23))
        self.cancel_button.setObjectName("cancel_button")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        #Actions
        self.dir_path = path
        self.allowed_formats = allowed_formats
        self.choice_list.addItems(self.get_files())
        self.select_all_button.clicked.connect(self.select_all_button_event)
        self.unselect_all_button.clicked.connect(self.unselect_all_button_event)
        self.cancel_button.clicked.connect(self.cancel_action)
        self.ok_button.clicked.connect(self.ok_action)

        print(self.dir_path)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Select files"))
        self.select_all_button.setText(_translate("Form", ">>"))
        self.unselect_all_button.setText(_translate("Form", "<<"))
        self.label.setText(_translate("Form", "Drag and drop items"))
        self.ok_button.setText(_translate("Form", "Ok"))
        self.cancel_button.setText(_translate("Form", "Cancel"))

    def select_all_button_event(self):
        count = self.choice_list.count()
        for i in range(0,count):
            item = self.choice_list.takeItem(0)
            self.selected_list.addItem(item)
            print(item)
    def unselect_all_button_event(self):
        count = self.selected_list.count()
        for i in range(0,count):
            item = self.selected_list.takeItem(0)
            self.choice_list.addItem(item)
            print(item)

    def get_files(self):
        files = []
        for file in listdir(self.dir_path):
            if file.endswith(self.allowed_formats):
                files.append(file)
        return files

    def cancel_action(self):
        self.set_form.hide()

    def ok_action(self):
        count = self.selected_list.count()
        selected_items = []
        for i in range(0,count):
            item = self.selected_list.takeItem(0).text()
            selected_items.append(item)

        self.set_prev_window.get_data(selected_items)
        self.set_form.hide()
        
        

# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     Form = QtWidgets.QWidget()
#     ui = Ui_Form()
#     ui.setupUi(Form)
#     Form.show()
#     sys.exit(app.exec_())
