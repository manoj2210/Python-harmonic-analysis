from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Input(object):

    def __init__(self, Base):

        #Layout Definition
        self.Input_Layout = QtWidgets.QHBoxLayout(Base)
        self.Input_Layout.setSpacing(20)
        self.Input_Layout.setObjectName("Input_Layout")

        #Label Definition for functions
        self.Function_Label = QtWidgets.QLabel(Base)
        self.Function_Label.setMinimumSize(QtCore.QSize(151, 51))
        self.Function_Label.setMaximumSize(QtCore.QSize(300, 51))
        self.Function_Label.setStyleSheet("background-color: rgba(212, 212, 212, 122);\n"
                                                    "font: 75 italic 24pt \"Georgia\";")
        self.Function_Label.setFrameShape(QtWidgets.QFrame.Box)
        self.Function_Label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Function_Label.setLineWidth(2)
        self.Function_Label.setMidLineWidth(1)
        self.Function_Label.setObjectName("Function_Label")

        #Adding Label into layout
        self.Input_Layout.addWidget(self.Function_Label)

        #Adding Lineedit
        self.Function_LineEdit = QtWidgets.QTextEdit(Base)
        self.Function_LineEdit.setMinimumSize(QtCore.QSize(151, 51))
        self.Function_LineEdit.setMaximumHeight(51)
        self.Function_LineEdit.setStyleSheet("background-color: rgba(212, 212, 212, 122);\n"
                                                        "font: 75 italic 18pt \"Georgia\";")

        self.Function_LineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.Function_LineEdit.setObjectName("Function_LineEdit")

        #Adding Lineedit to layout
        self.Input_Layout.addWidget(self.Function_LineEdit)
        #Interval Label
        self.Interval_Label = QtWidgets.QLabel(Base)
        self.Interval_Label.setMinimumSize(QtCore.QSize(151, 51))
        self.Interval_Label.setMaximumSize(QtCore.QSize(16777215, 51))
        self.Interval_Label.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.Interval_Label.setStyleSheet("background-color: rgba(212, 212, 212, 122);\n"
                                                    "font: 75 italic 24pt \"Georgia\";")
        self.Interval_Label.setFrameShape(QtWidgets.QFrame.Box)
        self.Interval_Label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Interval_Label.setLineWidth(2)
        self.Interval_Label.setMidLineWidth(1)
        self.Interval_Label.setObjectName("Interval_Label")

        self.Input_Layout.addWidget(self.Interval_Label)

        self.Interval_LineEdit = QtWidgets.QLineEdit(Base)
        self.Interval_LineEdit.setMinimumSize(QtCore.QSize(200, 51))
        self.Interval_LineEdit.setMaximumSize(QtCore.QSize(300, 51))
        self.Interval_LineEdit.setStyleSheet("background-color: rgba(212, 212, 212, 122);\n"
                                                        "font: 75 italic 18pt \"Georgia\";\n""")
        self.Interval_LineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.Interval_LineEdit.setObjectName("Interval_LineEdit")

        self.Input_Layout.addWidget(self.Interval_LineEdit)

        #Setting Buddies
        self.Function_Label.setBuddy(self.Function_LineEdit)
        self.Interval_Label.setBuddy(self.Function_LineEdit)

        self.retranslateUi(Base)     #Text inside the widgets
        QtCore.QMetaObject.connectSlotsByName(Base)

    def retranslateUi(self, Base):
        _translate = QtCore.QCoreApplication.translate
        Base.setWindowTitle(_translate("Base", "Base"))
        self.Function_Label.setText(_translate("Base", "<html><head/><body><p><span style=\" font-size:18pt;\">Function :</span></p></body></html>"))
        self.Function_LineEdit.setPlaceholderText(_translate("Base", "Enter the function "))
        self.Interval_Label.setText(_translate("Base", "<html><head/><body><p><span style=\" font-size:18pt;\">Interval :</span></p></body></html>"))
        self.Interval_LineEdit.setPlaceholderText(_translate("Base", "1 < x < 2"))
