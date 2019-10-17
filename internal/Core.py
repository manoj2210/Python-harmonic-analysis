import sys
import random
import matplotlib
matplotlib.use("Qt5Agg")
from PyQt5 import QtCore, QtGui, QtWidgets
from numpy import arange, sin, pi
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

import numpy as np


class MyCanvas(FigureCanvas):
    def __init__(self, parent=None,width=300,height=300,t=[],y=[]):

        fig = Figure()
        fig.patch.set_facecolor('xkcd:black')
        self.axes = fig.add_subplot(111)
        # self.compute_initial_figure()
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)
        FigureCanvas.setGeometry(self,0,0,width,height)
        FigureCanvas.updateGeometry(self)

        self.t=t
        self.s =sin(self.t)
        self.y=y
    i=0
    t = []


    y=[]

    def compute_initial_figure(self):
        pass

class Plot_canvas(MyCanvas):

    def __init__(self, *args, **kwargs):
        MyCanvas.__init__(self, *args, **kwargs)
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.update_figure)
        # timer.start(30)

    def compute_initial_figure(self):


        self.axes.set_facecolor('xkcd:grey')
        self.axes.plot(self.t, self.s,"black")
        self.axes.spines['left'].set_position('center')
        self.axes.spines['bottom'].set_position('center')
        plt.setp(self.axes.spines.values(), color="black")
        plt.setp([self.axes.get_xticklines(), self.axes.get_yticklines()], color="black")
        self.axes.spines['right'].set_color('none')
        self.axes.spines['top'].set_color('none')
        self.axes.xaxis.set_ticks_position('bottom')
        self.axes.yaxis.set_ticks_position('left')
        # self.axes.set_ylim([-6.14,6.14])
        # self.axes.set_xticks(np.arange(-6,7,step=1))
        # self.axes.set_yticks(np.arange(-6,7,step=1))

        # self.axes.set_xlabel("x",fontsize=22)
        # self.axes.set_ylabel("f(x)",fontsize=22)


    def update_figure(self):

        if self.i==len(self.y):
            self.i=0
        # self.axes.cla()
        self.axes.plot(self.t,self.y[self.i])
        self.draw()
        self.i+=1

# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     UI_Mainwindow = QtWidgets.QWidget()
#     UI_Mainwindow.setStyleSheet("background-color: rgb(0,0,0);")
#     UI_Mainwindow.setMinimumSize(QtCore.QSize(1000,1000))
#
#     ui = Plot_canvas(UI_Mainwindow,1000,1000,arange(-6.14,6.14,0.1))
#     ui.compute_initial_figure()
#     # ui.timer.start(1000)
#
#     UI_Mainwindow.show()
#     sys.exit(app.exec_())
