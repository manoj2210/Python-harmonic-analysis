import os
from pyqtgraph.Qt import QtCore, QtGui, QtWidgets
import pyqtgraph as pg
import pyqtgraph.opengl as gl
import numpy as np

# Create a GL View widget to display data
app = QtGui.QApplication([])

m = QtWidgets.QMainWindow()
m.setGeometry(0, 0, 1920, 1080)
m.setWindowFlag(QtCore.Qt.FramelessWindowHint)

w = gl.GLViewWidget(m)

w.setWindowTitle("Harmonic Analysis")
w.setCameraPosition(distance=50)
w.setGeometry(0, 0, 1920, 1080)
w.setWindowFlags(QtCore.Qt.FramelessWindowHint)

label = QtWidgets.QLabel(m)
label.setWindowTitle("Harmonic Analysis")
label.setText("Python Package\nBy\n   M . Manoj kumar")
label.setStyleSheet("background-color:black;\n"
                    "font: 75 italic 22pt \"Georgia\";\n"
                    "color:white;")
label.setGeometry(100, 50, 800, 120)
label.setWindowFlags(QtCore.Qt.FramelessWindowHint)

label.raise_()

Ok_button = QtWidgets.QPushButton(m)
Ok_button.setText("Next")
Ok_button.setObjectName("Ok_button")
Ok_button.setGeometry(100, 150, 120, 100)
Ok_button.setStyleSheet(" QPushButton#Ok_button {\n"
                        "     background-color:grey;\n"
                        "    font: 75 italic 22pt \"Georgia\";\n"
                        "    color: white;\n"
                        "    border-radius:30px;\n"
                        " }\n"
                        )
Ok_button.raise_()

m.show()
# Add a grid to the view
g = gl.GLGridItem()
g.scale(2, 2, 1)
g.setDepthValue(10)  # draw grid after surfaces since they may be translucent
w.addItem(g)

z = pg.gaussianFilter(np.random.normal(size=(50, 50)), (1, 1))
p1 = gl.GLSurfacePlotItem(z=z, shader='shaded', color=(0, 0.41, 0.58, 0.29))
p1.scale(16. / 49., 16. / 49., 1.0)
p1.translate(-18, 2, 0)
w.addItem(p1)

# Saddle with x and y specified
x = np.linspace(-8, 8, 50)
y = np.linspace(-8, 8, 50)
z = 0.1 * ((x.reshape(50, 1) ** 2) - (y.reshape(1, 50) ** 2))
p2 = gl.GLSurfacePlotItem(x=x, y=y, z=z, shader='normalColor')
p2.translate(-10, -10, 0)
w.addItem(p2)

# Manually specified colors
z = pg.gaussianFilter(np.random.normal(size=(50, 50)), (1, 1))
x = np.linspace(-12, 12, 50)
y = np.linspace(-12, 12, 50)
colors = np.ones((50, 50, 4), dtype=float)
colors[..., 0] = np.clip(np.cos(((x.reshape(50, 1) ** 2) + (y.reshape(1, 50) ** 2)) ** 0.5), 0, 1)
colors[..., 1] = colors[..., 0]

p3 = gl.GLSurfacePlotItem(z=z, colors=colors.reshape(50 * 50, 4), shader='shaded', smooth=False)
p3.scale(16. / 49., 16. / 49., 1.0)
p3.translate(2, -18, 0)
w.addItem(p3)

cols = 90
rows = 100
x = np.linspace(-8, 8, cols + 1).reshape(cols + 1, 1)
y = np.linspace(-8, 8, rows + 1).reshape(1, rows + 1)
d = (x ** 2 + y ** 2) * 0.1
d2 = d ** 0.5 + 0.1

phi = np.arange(0, np.pi * 2, np.pi / 20.)
z = np.sin(d[np.newaxis, ...] + phi.reshape(phi.shape[0], 1, 1)) / d2[np.newaxis, ...]

p4 = gl.GLSurfacePlotItem(x=x[:, 0], y=y[0, :], shader='heightColor', computeNormals=False, smooth=False)
p4.shader()['colorMap'] = np.array([0.2, 2, 0.5, 0.2, 1, 1, 0.2, 0, 2])
p4.translate(10, 10, 0)
w.addItem(p4)

index = 0
count = 0


def update():
    global p4, z, index, count
    index -= 1
    p4.setData(z=z[index % z.shape[0]])
    count += 1
    if count == 20:
        p1.setData(z=pg.gaussianFilter(np.random.normal(size=(50, 50)), (1.5, 2)))
        p3.setData(z=pg.gaussianFilter(np.random.normal(size=(50, 50)), (1.5, 1)))
        count = 0


if __name__ == '__main__':
    import sys

    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()
