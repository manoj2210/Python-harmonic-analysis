import sys
import random
import matplotlib
matplotlib.use("Qt5Agg")
from PyQt5 import QtCore, QtGui, QtWidgets
from numpy import arange, sin, pi
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np
from scipy import fftpack
import matplotlib.pyplot as plt
import cv2
from matplotlib.colors import LogNorm


class MyCanvas(FigureCanvas):
    def __init__(self, parent=None):

        fig = Figure()
        self.img = plt.imread("C:\\Users\\Manoj kumar\\Pictures\\mmk.png")
        fig.patch.set_facecolor('xkcd:black')
        self.axes = fig.add_subplot(111)
        self.compute_initial_figure()
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)
        FigureCanvas.setGeometry(self,350,100,1200,800)
        FigureCanvas.updateGeometry(parent)
        self.axes.imshow(self.img)

    def compute_initial_figure(self):
        pass

class Plot_canvas(MyCanvas):
    def compute_initial_figure(self):
        self.axes.set_facecolor('xkcd:black')
        #self.axes.set_facecolor((1.0, 0.47, 0.42))
        # self.axes.plot(self.t, self.s,"w")
    def blur(self):
        self.axes.cla()
        t = np.linspace(-10, 10, 30)
        bump = np.exp(-0.1*t**2)
        bump /= np.trapz(bump) # normalize the integral to 1

        # make a 2-D kernel out of it
        kernel = bump[:, np.newaxis] * bump[np.newaxis, :]
        # Padded fourier transform, with the same shape as the image
        # We use :func:`scipy.signal.fftpack.fft2` to have a 2D FFT
        kernel_ft = fftpack.fft2(kernel, shape=self.img.shape[:2], axes=(0, 1))

        # convolve
        img_ft = fftpack.fft2(self.img, axes=(0, 1))
        # the 'newaxis' is to match to color direction
        img2_ft = kernel_ft[:, :, np.newaxis] * img_ft
        img2 = fftpack.ifft2(img2_ft, axes=(0, 1)).real

        # clip values to range
        img2 = np.clip(img2, 0, 1)

        # plot output
        #plt.figure()
        #plt.imshow(img2)

        from scipy import signal
        # mode='same' is there to enforce the same output shape as input arrays
        # (ie avoid border effects)
        img3 = signal.fftconvolve(self.img, kernel[:, :, np.newaxis], mode='same')
        self.axes.imshow(img3)

    def denoise(self):
        self.axes.cla()
        im = cv2.imread("E:\\Python Package\\Image\\File.png")
        im =cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
        # self.axes.imshow(im, plt.cm.gray)

        ############################################################
        # Compute the 2d FFT of the input image
        ############################################################

        from scipy import fftpack
        im_fft = fftpack.fft2(im)

        # Show the results

        def plot_spectrum(im_fft):


        # A logarithmic colormap
            self.axes.imshow(np.abs(im_fft), norm=LogNorm(vmin=5))
            self.axes.colorbar()


        ############################################################
        # Filter in FFT
        ############################################################

        # In the lines following, we'll make a copy of the original spectrum and
        # truncate coefficients.

        # Define the fraction of coefficients (in each direction) we keep
        keep_fraction = 0.1

        # Call ff a copy of the original transform. Numpy arrays have a copy
        # method for this purpose.
        im_fft2 = im_fft.copy()

        # Set r and c to be the number of rows and columns of the array.
        r, c = im_fft2.shape[:2]

        # Set to zero all rows with indices between r*keep_fraction and
        # r*(1-keep_fraction):
        im_fft2[int(r*keep_fraction):int(r*(1-keep_fraction))] = 0

        # Similarly with the columns:
        im_fft2[:, int(c*keep_fraction):int(c*(1-keep_fraction))] = 0



        ############################################################
        # Reconstruct the final image
        ############################################################

        # Reconstruct the denoised image from the filtered spectrum, keep only the
        # real part for display.
        im_new = fftpack.ifft2(im_fft2).real

        self.axes.imshow(im_new,plt.cm.gray)
