from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Keyboard(object):
    def __init__(self, Form):
        self.Base_Layout = QtWidgets.QVBoxLayout(Form)
        self.Base_Layout.setContentsMargins(0, 0, 0, 0)
        self.Base_Layout.setObjectName("Base_Layout")


        self.buttonlayout = QtWidgets.QHBoxLayout(Form)
        self.buttonlayout.setObjectName("buttonlayout")
        self.x_pow_n_button = QtWidgets.QPushButton(Form)
        self.x_pow_n_button.setMinimumSize(QtCore.QSize(120, 61))
        self.x_pow_n_button.setMaximumSize(QtCore.QSize(140, 61))
        self.x_pow_n_button.setStyleSheet("QPushButton {\n"
                                                "background-color: rgba(212, 212, 212, 250);\n"
                                                "font: 75 italic 22pt Georgia;\n"
                                                "color:rgba(21, 21, 21, 200);\n"
                                                "border-radius:30px;\n"
                                                "}\n"
                                                "QPushButton:hover {\n"
                                                "background-color: rgba(212, 212, 212, 52);\n"
                                                "color:rgba(21, 21, 21, 50);\n"
                                                "border-radius:30px;\n"
                                                "}")
        self.x_pow_n_button.setObjectName("x_pow_n_button")

        self.Pi_button = QtWidgets.QPushButton(Form)
        self.Pi_button.setMinimumSize(QtCore.QSize(120, 61))
        self.Pi_button.setMaximumSize(QtCore.QSize(140, 61))
        self.Pi_button.setStyleSheet("QPushButton {\n"
"             background-color: rgba(212, 212, 212, 250);\n"
"                font: 75 italic 22pt Georgia;\n"
"                color:rgba(21, 21, 21, 200);\n"
"                border-radius:30px;\n"
"             }\n"
"             QPushButton:hover {\n"
"            background-color: rgba(212, 212, 212, 52);\n"
"           color:rgba(21, 21, 21, 250);\n"
"           border-radius:30px;\n"
"   }")
        self.Pi_button.setObjectName("Pi_button")

        self.Modulus_button = QtWidgets.QPushButton(Form)
        self.Modulus_button.setMinimumSize(QtCore.QSize(120, 61))
        self.Modulus_button.setMaximumSize(QtCore.QSize(140, 61))
        self.Modulus_button.setStyleSheet("QPushButton {\n"
"             background-color: rgba(212, 212, 212, 250);\n"
"                font: 75 italic 22pt Georgia;\n"
"                color:rgba(21, 21, 21, 200);\n"
"                border-radius:30px;\n"
"             }\n"
"             QPushButton:hover {\n"
"            background-color: rgba(212, 212, 212, 52);\n"
"           color:rgba(21, 21, 21, 250);\n"
"           border-radius:30px;\n"
"   }")
        self.Modulus_button.setObjectName("Modulus_button")

        self.Lessthan_button = QtWidgets.QPushButton(Form)
        self.Lessthan_button.setMinimumSize(QtCore.QSize(120, 61))
        self.Lessthan_button.setMaximumSize(QtCore.QSize(140, 61))
        self.Lessthan_button.setStyleSheet("QPushButton {\n"
"             background-color: rgba(212, 212, 212, 250);\n"
"                font: 75 italic 22pt Georgia;\n"
"                color:rgba(21, 21, 21, 200);\n"
"                border-radius:30px;\n"
"             }\n"
"             QPushButton:hover {\n"
"            background-color: rgba(212, 212, 212, 52);\n"
"           color:rgba(21, 21, 21, 250);\n"
"           border-radius:30px;\n"
"   }")
        self.Lessthan_button.setObjectName("Lessthan_button")

        self.Greaterthan_button = QtWidgets.QPushButton(Form)
        self.Greaterthan_button.setMinimumSize(QtCore.QSize(120, 61))
        self.Greaterthan_button.setMaximumSize(QtCore.QSize(140, 61))
        self.Greaterthan_button.setStyleSheet("QPushButton {\n"
"             background-color: rgba(212, 212, 212, 250);\n"
"                font: 75 italic 22pt Georgia;\n"
"                color:rgba(21, 21, 21, 200);\n"
"                border-radius:30px;\n"
"             }\n"
"             QPushButton:hover {\n"
"            background-color: rgba(212, 212, 212, 52);\n"
"           color:rgba(21, 21, 21, 250);\n"
"           border-radius:30px;\n"
"   }")
        self.Greaterthan_button.setObjectName("Greaterthan_button")


        self.Sqrt_button = QtWidgets.QPushButton(Form)
        self.Sqrt_button.setMinimumSize(QtCore.QSize(120, 61))
        self.Sqrt_button.setMaximumSize(QtCore.QSize(140, 61))
        self.Sqrt_button.setStyleSheet("QPushButton {\n"
        "             background-color: rgba(212, 212, 212, 250);\n"
        "                font: 75 italic 22pt Georgia;\n"
        "                color:rgba(21, 21, 21, 200);\n"
        "                border-radius:30px;\n"
        "             }\n"
        "             QPushButton:hover {\n"
        "            background-color: rgba(212, 212, 212, 52);\n"
        "           color:rgba(21, 21, 21, 250);\n"
        "           border-radius:30px;\n"
        "   }")
        self.Sqrt_button.setObjectName("Sqrt_button")



        self.Exponential_button = QtWidgets.QPushButton(Form)
        self.Exponential_button.setMinimumSize(QtCore.QSize(120, 61))
        self.Exponential_button.setMaximumSize(QtCore.QSize(140, 61))
        self.Exponential_button.setStyleSheet("QPushButton {\n"
        "             background-color: rgba(212, 212, 212, 250);\n"
        "                font: 75 italic 22pt Georgia;\n"
        "                color:rgba(21, 21, 21, 200);\n"
        "                border-radius:30px;\n"
        "             }\n"
        "             QPushButton:hover {\n"
        "            background-color: rgba(212, 212, 212, 52);\n"
        "           color:rgba(21, 21, 21, 250);\n"
        "           border-radius:30px;\n"
        "   }")
        self.Exponential_button.setObjectName("Exponential_button")



        self.Constant_button = QtWidgets.QPushButton(Form)
        self.Constant_button.setMinimumSize(QtCore.QSize(120, 61))
        self.Constant_button.setMaximumSize(QtCore.QSize(140, 61))
        self.Constant_button.setStyleSheet("QPushButton {\n"
        "             background-color: rgba(212, 212, 212, 250);\n"
        "                font: 75 italic 22pt Georgia;\n"
        "                color:rgba(21, 21, 21, 200);\n"
        "                border-radius:30px;\n"
        "             }\n"
        "             QPushButton:hover {\n"
        "            background-color: rgba(212, 212, 212, 52);\n"
        "           color:rgba(21, 21, 21, 250);\n"
        "           border-radius:30px;\n"
        "   }")
        self.Constant_button.setObjectName("Constant_button")



        self.buttonlayout.addWidget(self.x_pow_n_button)
        self.buttonlayout.addWidget(self.Pi_button)
        self.buttonlayout.addWidget(self.Modulus_button)
        self.buttonlayout.addWidget(self.Lessthan_button)
        self.buttonlayout.addWidget(self.Greaterthan_button)
        self.buttonlayout.addWidget(self.Sqrt_button)
        self.buttonlayout.addWidget(self.Exponential_button)
        self.buttonlayout.addWidget(self.Constant_button)

        self.Base_Layout.addLayout(self.buttonlayout)

        self.retranslateUi(Form)

        QtCore.QMetaObject.connectSlotsByName(Form)



    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.x_pow_n_button.setText(_translate("Form", "x ⁿ"))
        self.Pi_button.setText(_translate("Form", "π"))
        self.Modulus_button.setText(_translate("Form", " "))
        self.Sqrt_button.setText(_translate("Form", "√"))
        self.Lessthan_button.setText(_translate("Form", "≤"))
        self.Greaterthan_button.setText(_translate("Form", "≥"))
        self.Exponential_button.setText(_translate("Form", "℮"))
        self.Constant_button.setText(_translate("Form", " "))

# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     Form = QtWidgets.QWidget()
#     ui = Ui_Keyboard(Form)
#     Form.show()
#     sys.exit(app.exec_())
