from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np
import Core
import Solve
from sympy import *
from sympy.abc import x as w



class Ui_MainWindow(object):
    def __init__(self,x=[],y=[],animateX=[],animateY=[]):

        f = open("input.txt","r")
        self.expr=[]
        r=[]
        ip=int(f.readline())
        for i in range(0,ip):
            temp=f.readline().split()
            self.expr.append(sympify(temp[0]))
            r.append(temp[1])
        h=int(f.readline())
        p=Solve.Solving(self.expr,r,h)

        f.close()

        self.Eq="||"
        for htp in range(len(self.expr)):
            self.Eq+=str(self.expr[htp])+" => "+str(r[htp])+"||"
        self.x=np.arange(-6.14,6.14,0.1)
        self.y=p.series_list

        self.m=[]
        self.original=[]
        y=[]
        for i in range(len(r)):
            a,b=list(map(float,r[i].split(',')))
            for j in np.arange(a,b,0.1):
                y.append((self.expr[i]).subs(w,j))
            self.original.append(np.arange(a,b,0.1))
            self.m.append(y)
            y=[]

        self.l=len(self.expr)

    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.showMaximized()
        MainWindow.resize(1920, 1080)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Head_label = QtWidgets.QLabel(self.centralwidget)
        self.Head_label.setMaximumSize(QtCore.QSize(16777215, 100))
        self.Head_label.setStyleSheet("font: 32pt \"Segoe Print\";")
        self.Head_label.setObjectName("Head_label")
        self.horizontalLayout.addWidget(self.Head_label)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.Equation_label = QtWidgets.QLabel(self.centralwidget)
        self.Equation_label.setMaximumSize(QtCore.QSize(16777215, 100))
        self.Equation_label.setStyleSheet("font: 22pt \"Segoe Print\";\n"
"color: rgb(255, 255, 255);background-color:darkgrey;")
        self.Equation_label.setObjectName("Equation_label")
        self.Equation_label.setText(self.Eq)
        self.verticalLayout.addWidget(self.Equation_label)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.Head_label1 = QtWidgets.QLabel(self.centralwidget)
        self.Head_label1.setMinimumSize(QtCore.QSize(0, 75))
        self.Head_label1.setMaximumSize(QtCore.QSize(16777215, 75))
        self.Head_label1.setStyleSheet("font: 22pt \"Segoe Print\";\n"
"color: rgb(255, 255, 255);")
        self.Head_label1.setObjectName("Head_label1")
        self.horizontalLayout_2.addWidget(self.Head_label1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Head_label2 = QtWidgets.QLabel(self.centralwidget)
        self.Head_label2.setMinimumSize(QtCore.QSize(0, 50))
        self.Head_label2.setMaximumSize(QtCore.QSize(16777215, 100))
        self.Head_label2.setStyleSheet("font: 16pt \"Segoe Print\";\n"
"color: rgb(255, 255, 255);background-color:darkgrey;")
        self.Head_label2.setObjectName("Head_label2")
        self.verticalLayout_2.addWidget(self.Head_label2)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setMinimumSize(QtCore.QSize(0, 700))
        self.widget.setMaximumSize(QtCore.QSize(16777215, 700))
        self.widget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.widget.setObjectName("widget")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.Harmonic_graph_label = QtWidgets.QLabel(self.widget)
        self.Harmonic_graph_label.setMinimumSize(QtCore.QSize(700, 700))
        self.Harmonic_graph_label.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.Harmonic_graph_label.setText("")
        self.Harmonic_graph_label.setObjectName("Harmonic_graph_label")
        self.horizontalLayout_6.addWidget(self.Harmonic_graph_label)
        self.verticalLayout_2.addWidget(self.widget)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.Draw_graph_button = QtWidgets.QPushButton(self.centralwidget)
        self.Draw_graph_button.setMinimumSize(QtCore.QSize(0, 50))
        self.Draw_graph_button.setMaximumSize(QtCore.QSize(700, 16777215))
        self.Draw_graph_button.setStyleSheet("\n"
"QPushButton {\n"
"    background-color: rgb(0, 0, 0);\n"
"font: 16pt \"Segoe Print\";\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"\n"
" QPushButton:hover {\n"
"        background-color: rgba(212, 212, 212, 252);\n"
"        color:rgba(255, 85, 0, 250);\n"
"        border-radius:10px;\n"
"\n"
" }")
        self.Draw_graph_button.setObjectName("Draw_graph_button")
        self.horizontalLayout_3.addWidget(self.Draw_graph_button)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_5.addLayout(self.verticalLayout_2)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.Head_label3 = QtWidgets.QLabel(self.centralwidget)
        self.Head_label3.setMinimumSize(QtCore.QSize(0, 50))
        self.Head_label3.setMaximumSize(QtCore.QSize(16777215, 100))
        self.Head_label3.setStyleSheet("font: 16pt \"Segoe Print\";\n"
"color: rgb(255, 255, 255);background-color:darkgrey;")
        self.Head_label3.setObjectName("Head_label3")
        self.verticalLayout_4.addWidget(self.Head_label3)
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setMinimumSize(QtCore.QSize(0, 700))
        self.widget_2.setMaximumSize(QtCore.QSize(16777215, 700))
        self.widget_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.Animation_label = QtWidgets.QLabel(self.widget_2)
        self.Animation_label.setMinimumSize(QtCore.QSize(700, 700))
        self.Animation_label.setMaximumSize(QtCore.QSize(1889, 700))
        self.Animation_label.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.Animation_label.setText("")
        self.Animation_label.setObjectName("Animation_label")
        self.horizontalLayout_7.addWidget(self.Animation_label)
        self.verticalLayout_4.addWidget(self.widget_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem5)
        self.Animate_button = QtWidgets.QPushButton(self.centralwidget)
        self.Animate_button.setMaximumSize(QtCore.QSize(700, 16777215))
        self.Animate_button.setStyleSheet("\n"
"QPushButton {\n"
"    background-color: rgb(0, 0, 0);\n"
"font: 16pt \"Segoe Print\";\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"\n"
" QPushButton:hover {\n"
"        background-color: rgba(212, 212, 212, 252);\n"
"        color:rgba(255, 85, 0, 250);\n"
"        border-radius:10px;\n"
"\n"
" }")
        self.Animate_button.setObjectName("Animate_button")
        self.horizontalLayout_4.addWidget(self.Animate_button)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem6)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5.addLayout(self.verticalLayout_4)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        MainWindow.setCentralWidget(self.centralwidget)

        self.Animate_button.clicked.connect(self.Animate)
        self.Draw_graph_button.clicked.connect(self.Get_Graph)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def Get_Graph(self):

        self.Graph_ui = Core.Plot_canvas(self.Harmonic_graph_label,943,700)
        self.Graph_ui.t=self.x
        self.Graph_ui.s=self.y
        self.Graph_ui.compute_initial_figure()
        self.Graph_ui.show()

    def Animate(self):
        self.Animate_ui= Core.Plot_canvas(self.Animation_label,943,700,self.x,self.y)
        for i in range(len(self.expr)):
            print(self.original[i],self.m[i])
            self.Animate_ui.t=self.original[i].copy()
            self.Animate_ui.s=self.m[i].copy()

            self.Animate_ui.compute_initial_figure()
            self.Animate_ui.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Graph_Window"))
        self.Head_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:28pt; color:#ffffff;\">Fourier Series Equation</span></p></body></html>"))
        self.Equation_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">"+self.Eq+"</p></body></html>"))
        self.Head_label1.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:22pt;\">Graph</span></p></body></html>"))
        self.Head_label2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Fourier Series for Given Harmonic</p></body></html>"))
        self.Draw_graph_button.setText(_translate("MainWindow", "Draw Graph"))
        self.Head_label3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Visualisation of Harmonic Analysis</p></body></html>"))
        self.Animate_button.setText(_translate("MainWindow", "Original Graph"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
