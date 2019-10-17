from PyQt5 import QtCore, QtGui, QtWidgets

class Keyboard_LineEdit(object):
    def __init__(self, Base):

        #Layout Definition
        self.Input_Layout = QtWidgets.QHBoxLayout(Base)
        self.Input_Layout.setSpacing(20)
        self.Input_Layout.setObjectName("Input_Layout")

        #Adding Lineedit
        self.Function_LineEdit = QtWidgets.QLineEdit(Base)
        self.Function_LineEdit.setMinimumSize(QtCore.QSize(200, 51))
        self.Function_LineEdit.setStyleSheet("background-color: rgba(212, 212, 212, 122);\n"
                                                        "font: 75 italic 18pt \"Georgia\";")

        self.Function_LineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.Function_LineEdit.setObjectName("Function_LineEdit")

        #Adding Lineedit to layout
        self.Input_Layout.addWidget(self.Function_LineEdit)



        self.retranslateUi(Base)     #Text inside the widgets
        QtCore.QMetaObject.connectSlotsByName(Base)


    def retranslateUi(self, Base):
        _translate = QtCore.QCoreApplication.translate
        Base.setWindowTitle(_translate("Base", "Base"))
        #self.Function_Label.setText(_translate("Base", "<html><head/><body><p><span style=\" font-size:18pt;\">"+ self.temp+"</span></p></body></html>"))
        self.Function_LineEdit.setPlaceholderText(_translate("Base", "Enter the function "))

# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     Form = QtWidgets.QWidget()
#     ui = Keyboard_LineEdit(Form)
#     # ui.setupUi(Form)
#     Form.show()
#     sys.exit(app.exec_())
