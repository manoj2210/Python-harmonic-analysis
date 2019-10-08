from Core import *

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    UI_Mainwindow = QtWidgets.QLabel()
    UI_Mainwindow.setStyleSheet("background-color: rgb(0,0,0);")
    UI_Mainwindow.setMinimumSize(QtCore.QSize(1000,1000))

    ui = Plot_canvas(UI_Mainwindow,1000,1000)
    ui.compute_initial_figure()

    UI_Mainwindow.show()
    sys.exit(app.exec_())
