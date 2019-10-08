from PyQt5 import QtCore, QtGui, QtWidgets
import Function

from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1135, 783)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.File_button = QtWidgets.QPushButton(self.centralwidget)
        self.File_button.setMinimumSize(QtCore.QSize(50, 50))
        self.File_button.setMaximumSize(QtCore.QSize(50, 50))
        self.File_button.setStyleSheet("border-image:url(E:/Python Package/Image/File.png);")
        self.File_button.setText("")
        self.File_button.setObjectName("File_button")
        self.horizontalLayout.addWidget(self.File_button)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.Save_button = QtWidgets.QPushButton(self.centralwidget)
        self.Save_button.setMinimumSize(QtCore.QSize(50, 50))
        self.Save_button.setStyleSheet("border-image:url(E:/Python Package/Image/save.png);")
        self.Save_button.setText("")
        self.Save_button.setObjectName("Save_button")
        self.horizontalLayout.addWidget(self.Save_button)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.Blur = QtWidgets.QPushButton(self.centralwidget)
        self.Blur.setMinimumSize(QtCore.QSize(50, 50))
        self.Blur.setMaximumSize(QtCore.QSize(50, 50))
        self.Blur.setText("Blur")
        self.Blur.setObjectName("Blur")
        self.Blur.setStyleSheet("background-color: black;color:white;")
        self.horizontalLayout.addWidget(self.Blur)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setMinimumSize(QtCore.QSize(100, 50))
        self.pushButton_4.setMaximumSize(QtCore.QSize(100, 50))
        self.pushButton_4.setText("Denoise")
        self.pushButton_4.setStyleSheet("background-color: black;color:white;")
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout.addWidget(self.pushButton_4)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setMinimumSize(QtCore.QSize(50, 50))
        self.pushButton_3.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setMinimumSize(QtCore.QSize(50, 50))
        self.pushButton_2.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMinimumSize(QtCore.QSize(500, 700))
        self.label.setStyleSheet("background-color: blue;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_2.setStretch(0, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        MainWindow.setGeometry(0,0,1920,1080)
        self.File_button.clicked.connect(self.openFileNameDialog)
        self.Save_button.clicked.connect(self.saveFileDialog)

        self.ui = Function.Plot_canvas(self.label)

        self.Blur.clicked.connect(self.blur)
        self.pushButton_4.clicked.connect(self.denoise)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(MainWindow,"Select the Image", "","Image (*.png)", options=options)
        if fileName:
            print(fileName)


    def saveFileDialog(self):

        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(MainWindow,"Save the Image","","All Files (*);;Text Files (*.txt)", options=options)
        if fileName:
            print(fileName)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Image Processing"))

    def blur(self):
        self.ui.blur()

    def denoise(self):
        self.ui.denoise()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
