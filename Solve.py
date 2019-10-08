import sympy as sy
import numpy as np
from sympy import *
x,n =sy.symbols("x n")


class Solving:

    def __init__(self,Equation=[],Interval=[],Harmonic_Num=0):

        self.Equation_list=Equation
        self.Interval_list=Interval
        self.Harmonic_Num=int(Harmonic_Num)

        for y in range(len(self.Interval_list)):
            a,b=self.Interval_list[y].split(",")
            a=float(a)
            b=float(b)
            self.a.append(float(a))
            self.b.append(float(b))

        self.l=(max(self.b)-min(self.a))/2

        for x in range(len(self.Equation_list)):
            self.Solve()

        self.Final_series()

        # print(self.an)

    fourier_series=0
    count=0
    a=[]
    b=[]
    a0=0
    an=0
    bn=0
    series=0
    cosine=[]
    sine=[]
    series_list=[]

    def Solve(self):

        a,b=self.Interval_list[self.count].split(",")
        a=float(a)
        b=float(b)
        f=(self.Equation_list[self.count])

        self.count+=1
        self.a.append(float(a))
        self.b.append(float(b))
        self.Fourier_Series(float(a),float(b),f)


    def Fourier_Series(self,a,b,f):

        a0=sy.integrate(f,(x,a,b))
        an=sy.integrate(f*sy.cos((n*sy.pi*x)/self.l),(x,a,b),conds="none")
        bn=sy.integrate(f*sy.sin((n*sy.pi*x)/self.l),(x,a,b),conds="none")

        self.a0+=(a0).evalf()
        self.an+=(an).evalf()
        self.bn+=(bn).evalf()

    def Final_series(self):

        self.a0*=1/self.l
        self.an*=1/self.l
        self.bn*=1/self.l

        for i in range(1,self.Harmonic_Num):
            try:
                value=(self.an*sy.cos((n*sy.pi*x)/self.l)).subs(n,i)
                self.cosine.append(value)

            except ZeroDivisionError:
                temp=integrate(self.f*sy.cos((i*sy.pi*x)/self.l),(x,a,b),conds="none")
                temp=temp*(sy.cos(n*x*sy.pi/self.l)).subs(n,i)
                self.cosine.append(temp)
                pass
            try:
                self.sine.append((self.bn*sy.sin((n*sy.pi*x)/self.l)).subs(n,i))
            except ZeroDivisionError:
                temp=integrate(self.f*sy.sin((i*self.pi*x)/self.l),(x,a,b),conds="none")
                temp=temp*(sy.sin(n*x*sy.pi/l)).subs(n,i)
                self.sine.append(temp)
                pass
        self.series=self.a0/2
        for i in range(1,self.Harmonic_Num):
            self.series+=self.cosine[i-1]+self.sine[i-1]
            self.series=(self.series).evalf()

        # self.series=self.series.truncate()
        print(self.series.subs(x,1).evalf())
        print(self.series)

        for p in np.arange(-6.14,6.14,0.1):
            hh=self.series.subs(x,p)
            self.series_list.append(hh)


# import matplotlib.pyplot as plt



# m=np.arange(-3.14,3.14,0.01)
# MainWindow = QtWidgets.QMainWindow()
# ui = Graph.Ui_MainWindow(m,p.series_list)
# ui.setupUi(MainWindow)
# MainWindow.show()
