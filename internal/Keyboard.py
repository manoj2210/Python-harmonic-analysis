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

        self.Base_Layout.addLayout(self.buttonlayout)

        self.retranslateUi(Form)

        QtCore.QMetaObject.connectSlotsByName(Form)



    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.x_pow_n_button.setText(_translate("Form", "x ⁿ"))
        self.Pi_button.setText(_translate("Form", "π"))

# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     Form = QtWidgets.QWidget()
#     ui = Ui_Keyboard(Form)
#     Form.show()
#     sys.exit(app.exec_())
