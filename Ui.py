from PyQt5 import QtCore, QtGui, QtWidgets                                     #Importing Modules
from sympy import pretty_print as pp,latex
from sympy.abc import *
import Solve
import Ui_Functions
import Keyboard
import Keyboard_input
import Graph
import numpy as np
import os


class Ui_UI_Mainwindow(object):

    Equation_input=[]

    def setupUi(self, UI_Mainwindow):                                                 #To Set the Requirements For Ui

        UI_Mainwindow.setObjectName("UI_Mainwindow")
        UI_Mainwindow.resize(1920, 1080)
        UI_Mainwindow.setFocusPolicy(QtCore.Qt.StrongFocus)                   #Focus Policy Helps to
                                                                                    #enable the windows multitasking
        UI_Mainwindow.setAutoFillBackground(True)                               #background Resizing
        UI_Mainwindow.setStyleSheet("#centralwidget{\n"                        #Set picture background
            "border-image: url(E:/Python Package/Backgrd.jpg);\n"
            " }\n" " ")
        self.centralwidget = QtWidgets.QWidget(UI_Mainwindow)                #Making QMainWindow as
                                                                                                #centralwidget

        #Specifying Size Policies
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")

        #Specifying Layouts
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)

        #Creating Title Label
        self.TitleLabel = QtWidgets.QLabel(self.centralwidget)

        #Specifying size Policies
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TitleLabel.sizePolicy().hasHeightForWidth())
        self.TitleLabel.setSizePolicy(sizePolicy)
        self.TitleLabel.setMinimumSize(QtCore.QSize(151, 71))
        self.TitleLabel.setMaximumSize(QtCore.QSize(16777215, 71))

        #Adding Styles
        self.TitleLabel.setStyleSheet("background-color: rgba(98, 98, 98, 50);\n"
                                            "font: 75 italic 24pt \"Georgia\";")
        self.TitleLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.TitleLabel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.TitleLabel.setLineWidth(5)
        self.TitleLabel.setMidLineWidth(1)

        #Setting Object Name
        self.TitleLabel.setObjectName("TitleLabel")

        #Adding to the Layout
        self.horizontalLayout_2.addWidget(self.TitleLabel)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)

        ##Adding Size policies to the layout
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        #Defining another layout for the Next label
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        #Setting Info Label
        self.Info_Label = QtWidgets.QLabel(self.centralwidget)

        #sizePolicies
        self.Info_Label.setMinimumSize(QtCore.QSize(151, 61))
        self.Info_Label.setMaximumSize(QtCore.QSize(16777215, 61))
        self.Info_Label.setFocusPolicy(QtCore.Qt.WheelFocus)

        #Styles
        self.Info_Label.setStyleSheet("background-color: rgba(212, 212, 212, 122);\n"
                                            "font: 75 italic 24pt \"Georgia\";")
        self.Info_Label.setFrameShape(QtWidgets.QFrame.Box)
        self.Info_Label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Info_Label.setLineWidth(2)
        self.Info_Label.setMidLineWidth(1)
        self.Info_Label.setObjectName("Info_Label")

        #Adding to the layout
        self.horizontalLayout.addWidget(self.Info_Label)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.Input_Vertical_Layout =QtWidgets.QVBoxLayout()
        self.Input_Vertical_Layout.setSpacing(20)
        self.Input_Vertical_Layout.setObjectName("Input_Vertical_Layout")

        #List that stores all the function values
        self.Function_Input_List=[]

        Input=Ui_Functions.Ui_Input(UI_Mainwindow)
        self.Input_Vertical_Layout.addLayout(Input.Input_Layout)
        self.Function_Input_List.append(Input)

        self.verticalLayout.addLayout(self.Input_Vertical_Layout)

        self.Button_Layout = QtWidgets.QHBoxLayout()
        self.Button_Layout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.Button_Layout.setSpacing(10)
        self.Button_Layout.setObjectName("Button_Layout")

        spacerItem3 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)

        self.Button_Layout.addItem(spacerItem3)
        self.AddFunction_Button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AddFunction_Button.sizePolicy().hasHeightForWidth())

        self.AddFunction_Button.setSizePolicy(sizePolicy)
        self.AddFunction_Button.setMinimumSize(QtCore.QSize(40, 51))
        self.AddFunction_Button.setMaximumSize(QtCore.QSize(45, 51))
        self.AddFunction_Button.setStyleSheet(" QPushButton {\n"
        "     background-color: rgba(212, 212, 212, 50);\n"
        "    font: 75 italic 30pt \"Georgia\";\n"
        "    color:rgba(255, 85, 0, 200);\  n"
        "    border-radius:10px;\n"
        " }\n"
        " QPushButton:hover {\n"
        "background-color: rgba(212, 212, 212, 252);\n"
        "color:rgba(255, 85, 0, 250);\n"
        "border-radius:10px;\n"
        "\n"
        " }")

        self.AddFunction_Button.setObjectName("AddFunction_Button")
        self.Button_Layout.addWidget(self.AddFunction_Button)

        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.Button_Layout.addItem(spacerItem4)
        self.Button_Layout.setStretch(2, 2)
        self.verticalLayout.addLayout(self.Button_Layout)

        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")

        self.Function_Label_2 = QtWidgets.QLabel(self.centralwidget)
        self.Function_Label_2.setMinimumSize(QtCore.QSize(300, 51))
        self.Function_Label_2.setMaximumSize(QtCore.QSize(300, 51))
        self.Function_Label_2.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.Function_Label_2.setStyleSheet("background-color: rgba(212, 212, 212, 122);\n"
                                                    "font: 75 italic 24pt \"Georgia\";")

        self.Function_Label_2.setFrameShape(QtWidgets.QFrame.Box)
        self.Function_Label_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Function_Label_2.setLineWidth(2)
        self.Function_Label_2.setMidLineWidth(1)
        self.Function_Label_2.setObjectName("Function_Label_2")

        self.horizontalLayout_3.addWidget(self.Function_Label_2)
        self.Harmonic_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Harmonic_lineEdit.sizePolicy().hasHeightForWidth())

        self.Harmonic_lineEdit.setSizePolicy(sizePolicy)
        self.Harmonic_lineEdit.setMinimumSize(QtCore.QSize(80, 51))
        self.Harmonic_lineEdit.setMaximumSize(QtCore.QSize(80, 51))
        self.Harmonic_lineEdit.setStyleSheet("background-color: rgba(212, 212, 212, 122);\n"
                                                        "font: 75 italic 18pt \"Georgia\";")
        self.Harmonic_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.Harmonic_lineEdit.setObjectName("Harmonic_lineEdit")

        self.horizontalLayout_3.addWidget(self.Harmonic_lineEdit)

        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(spacerItem5)

        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem6)

        self.Getgraph = QtWidgets.QPushButton(self.centralwidget)
        self.Getgraph.setMinimumSize(QtCore.QSize(200, 61))
        self.Getgraph.setMaximumSize(QtCore.QSize(200, 61))
        self.Getgraph.setStyleSheet(" QPushButton {\n"
            "     background-color: rgba(212, 212, 212, 50);\n"
            "    font: 75 italic 22pt \"Georgia\";\n"
            "    color:rgba(255, 85, 0, 200);\n"
            "    border-radius:30px;\n"
            " }\n"
            " QPushButton:hover {\n"
            "background-color: rgba(212, 212, 212, 252);\n"
            "color:rgba(255, 85, 0, 250);\n"
            "border-radius:30px;\n"
            "\n"
            " }")
        self.Getgraph.setObjectName("Getgraph")

        self.horizontalLayout_4.addWidget(self.Getgraph)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(spacerItem7)
        self.verticalLayout.addLayout(self.horizontalLayout_4)

        UI_Mainwindow.setCentralWidget(self.centralwidget)


        self.retranslateUi(UI_Mainwindow)

        self.Function_Input_List[0].Function_LineEdit.selectionChanged.connect(self.Keyboard_fun1)


        self.AddFunction_Button.clicked.connect(self.Input)
        self.text=""
        self.Getgraph.clicked.connect(self.Equation_fun)
        QtCore.QMetaObject.connectSlotsByName(UI_Mainwindow)

#Input Adding Function_input
    def Input(self):
        x=QtWidgets.QWidget(UI_Mainwindow)
        x.setMinimumHeight(70)
        x.setMaximumHeight(70)
        y=Ui_Functions.Ui_Input(x)
        self.Input_Vertical_Layout.addWidget(x)
        self.Function_Input_List.append(y)
        if len(self.Function_Input_List)==2:
            y.Function_LineEdit.selectionChanged.connect(self.Keyboard_fun2)
        if len(self.Function_Input_List)==3:
            y.Function_LineEdit.selectionChanged.connect(self.Keyboard_fun3)
        elif len(self.Function_Input_List)==4:
            y.Function_LineEdit.selectionChanged.connect(self.Keyboard_fun4)
        elif len(self.Function_Input_List)==5:
            y.Function_LineEdit.selectionChanged.connect(self.Keyboard_fun5)
        elif len(self.Function_Input_List)==6:
            y.Function_LineEdit.selectionChanged.connect(self.Keyboard_fun6)
        elif len(self.Function_Input_List)==7:
            y.Function_LineEdit.selectionChanged.connect(self.Keyboard_fun7)

#Enter slot for the keyboard superscript
    def Superscript_fun(self):
        temp=self.ui.Function_LineEdit.displayText()
        # plaintext=self.Function_Input_List[self.Current_lineEdit].Function_LineEdit.toPlainText()
        temp2=self.Function_Input_List[self.Current_lineEdit].Function_LineEdit.toHtml()

        # x=len(self.Equation_input)
        # self.Equation_input+=plaintext[x-1::]

        up="<sup>"+"("+temp+")"+"</sup> "

        doc=QtGui.QTextDocument()
        doc.setHtml(up)

        self.text=temp2[:len(temp2)-18:]+up+temp2[len(temp2)-18::]
        #print(self.text)
        self.Function_Input_List[self.Current_lineEdit].Function_LineEdit.setText(self.text)
        # self.Equation_input+="^"+temp+" "
        # self.Harmonic_lineEdit.setText(self.Equation_input)
    count=0
    a=0

#Slot for pi
    def Pi_fun(self):
        try:
            temp2=self.Function_Input_List[self.Current_lineEdit].Function_LineEdit.toHtml()

            up=" \u03C0 "

            doc=QtGui.QTextDocument()
            doc.setHtml(up)

            self.text=temp2[:len(temp2)-18:]+up+temp2[len(temp2)-18::]

            self.Function_Input_List[self.Current_lineEdit].Function_LineEdit.setText(self.text)

        except:
            self.text=" \u03C0 "
            self.Function_Input_List[self.Current_lineEdit].Function_LineEdit.insertPlainTex(self.text)

#Slot for Modulus
    def Modulus_fun(self):

        temp=self.ui.Function_LineEdit.displayText()

        temp2=self.Function_Input_List[self.Current_lineEdit].Function_LineEdit.toHtml()

        up=" abs("+ temp+")"

        doc=QtGui.QTextDocument()
        doc.setHtml(up)
        self.text=temp2[:len(temp2)-18:]+up+temp2[len(temp2)-18::]

        self.Function_Input_List[self.Current_lineEdit].Function_LineEdit.setText(self.text)

#Slot for Less
    def Lessthan_fun(self):

        try:
            # temp=self.ui.Function_LineEdit.displayText()

            temp2=self.Function_Input_List[self.Current_lineEdit].Function_LineEdit.toHtml()

            up=" ≤ "

            doc=QtGui.QTextDocument()
            doc.setHtml(up)
            self.text=temp2[:len(temp2)-18:]+up+temp2[len(temp2)-18::]
            self.Function_Input_List[self.Current_lineEdit].Function_LineEdit.setText(self.text)
        except:
            self.text=" ≤ "
            self.Function_Input_List[self.Current_lineEdit].Function_LineEdit.insertPlainText(self.text)

#Slot for Great
    def Greaterthan_fun(self):

        try:
            # temp=self.ui.Function_LineEdit.displayText()

            temp2=self.Function_Input_List[self.Current_lineEdit].Function_LineEdit.toHtml()

            up=" ≥ "

            doc=QtGui.QTextDocument()
            doc.setHtml(up)
            self.text=temp2[:len(temp2)-18:]+up+temp2[len(temp2)-18::]
            self.Function_Input_List[self.Current_lineEdit].Function_LineEdit.setText(self.text)

        except:
            self.text=" ≥ "
            self.Function_Input_List[self.Current_lineEdit].Function_LineEdit.insertPlainText(self.text)

#Slot for Sqrt
    def Sqrt_fun(self):


        temp=self.ui.Function_LineEdit.displayText()

        self.Function_Input_List[self.Current_lineEdit].Function_LineEdit.insertPlainText("("+temp+")")

        temp2=self.Function_Input_List[self.Current_lineEdit].Function_LineEdit.toHtml()

        up="<sup>"+"(1/2)"+"</sup> "

        doc=QtGui.QTextDocument()
        doc.setHtml(up)
        print(up)

        self.text=temp2[:len(temp2)-18:]+up+temp2[len(temp2)-18::]
        # print(self.text)
        self.Function_Input_List[self.Current_lineEdit].Function_LineEdit.setText(self.text)


#Slot for Exponential
    def Exponential_fun(self):

        try:
            # temp=self.ui.Function_LineEdit.displayText()

            temp2=self.Function_Input_List[self.Current_lineEdit].Function_LineEdit.toHtml()

            up=" 2.718 "

            doc=QtGui.QTextDocument()
            doc.setHtml(up)
            self.text=temp2[:len(temp2)-18:]+up+temp2[len(temp2)-18::]
            self.Function_Input_List[self.Current_lineEdit].Function_LineEdit.setText(self.text)

        except:
            self.text=" 2.718 "

            self.Function_Input_List[self.Current_lineEdit].Function_LineEdit.insertPlainText(self.text)


#Slot for Constant
    def Constant_fun(self):

        try:
            # temp=self.ui.Function_LineEdit.displayText()

            temp2=self.Function_Input_List[self.Current_lineEdit].Function_LineEdit.toHtml()

            up=" k "

            doc=QtGui.QTextDocument()
            doc.setHtml(up)
            self.text=temp2[:len(temp2)-18:]+up+temp2[len(temp2)-18::]
            self.Function_Input_List[self.Current_lineEdit].Function_LineEdit.setText(self.text)

        except:
            self.text=" k "
            self.Function_Input_List[self.Current_lineEdit].Function_LineEdit.insertPlainText(self.text)

    Current_lineEdit=0  #For specipying the keyboard index
    form_var_tem=0      #For deleteLater of widgets



### For all the Keyboard creation
    def Keyboard_fun1(self):

        if self.a ==0:
            self.a+=1
        #Keyboard
            self.Keyboard=QtWidgets.QWidget(UI_Mainwindow)
            self.Keyboard.setMinimumHeight(70)
            self.Keyboard.setMaximumHeight(70)
            Keyboard_ui=Keyboard.Ui_Keyboard(self.Keyboard)

            self.Addition_Layout=QtWidgets.QVBoxLayout(self.Keyboard)
            self.Addition_Layout.setContentsMargins(0,0,0,0)
            self.Addition_Layout.setObjectName("Addition_Layout")
            self.verticalLayout.addLayout(self.Addition_Layout)
            self.Addition_Layout.addWidget(self.Keyboard)

            Keyboard_ui.x_pow_n_button.clicked.connect(self.superscript)
            Keyboard_ui.Pi_button.clicked.connect(self.Pi_fun)
            Keyboard_ui.Modulus_button.clicked.connect(self.Modulus)
            Keyboard_ui.Lessthan_button.clicked.connect(self.Lessthan_fun)
            Keyboard_ui.Greaterthan_button.clicked.connect(self.Greaterthan_fun)
            Keyboard_ui.Sqrt_button.clicked.connect(self.Sqrt)
            Keyboard_ui.Exponential_button.clicked.connect(self.Exponential_fun)
            Keyboard_ui.Constant_button.clicked.connect(self.Constant_fun)
            self.Current_lineEdit=0
        else:
            self.Keyboard.deleteLater()
            if self.form_var_tem!=0:
                self.Form.deleteLater()
                self.form_var_tem=0
            self.count=0
            self.a-=1


    def Keyboard_fun2(self):
        if self.a ==0:
            self.a+=1
        #Keyboard
            self.Keyboard=QtWidgets.QWidget(UI_Mainwindow)
            self.Keyboard.setMinimumHeight(70)
            self.Keyboard.setMaximumHeight(70)
            Keyboard_ui=Keyboard.Ui_Keyboard(self.Keyboard)

            self.Addition_Layout=QtWidgets.QVBoxLayout(self.Keyboard)
            self.Addition_Layout.setContentsMargins(0,0,0,0)
            self.Addition_Layout.setObjectName("Addition_Layout")
            self.verticalLayout.addLayout(self.Addition_Layout)
            self.Addition_Layout.addWidget(self.Keyboard)

            Keyboard_ui.x_pow_n_button.clicked.connect(self.superscript)
            Keyboard_ui.Pi_button.clicked.connect(self.Pi_fun)
            Keyboard_ui.Modulus_button.clicked.connect(self.Modulus)
            Keyboard_ui.Lessthan_button.clicked.connect(self.Lessthan_fun)
            Keyboard_ui.Greaterthan_button.clicked.connect(self.Greaterthan_fun)
            Keyboard_ui.Sqrt_button.clicked.connect(self.Sqrt)
            Keyboard_ui.Exponential_button.clicked.connect(self.Exponential_fun)
            Keyboard_ui.Constant_button.clicked.connect(self.Constant_fun)
            self.Current_lineEdit=1
        else:
            self.Keyboard.deleteLater()
            if self.form_var_tem!=0:
                self.Form.deleteLater()
                self.form_var_tem=0
            self.count=0
            self.a-=1

    def Keyboard_fun3(self):

        if self.a ==0:
            self.a+=1
        #Keyboard
            self.Keyboard=QtWidgets.QWidget(UI_Mainwindow)
            self.Keyboard.setMinimumHeight(70)
            self.Keyboard.setMaximumHeight(70)
            Keyboard_ui=Keyboard.Ui_Keyboard(self.Keyboard)

            self.Addition_Layout=QtWidgets.QVBoxLayout(self.Keyboard)
            self.Addition_Layout.setContentsMargins(0,0,0,0)
            self.Addition_Layout.setObjectName("Addition_Layout")
            self.verticalLayout.addLayout(self.Addition_Layout)
            self.Addition_Layout.addWidget(self.Keyboard)

            Keyboard_ui.x_pow_n_button.clicked.connect(self.superscript)
            Keyboard_ui.Pi_button.clicked.connect(self.Pi_fun)
            Keyboard_ui.Modulus_button.clicked.connect(self.Modulus)
            Keyboard_ui.Lessthan_button.clicked.connect(self.Lessthan_fun)
            Keyboard_ui.Greaterthan_button.clicked.connect(self.Greaterthan_fun)
            Keyboard_ui.Sqrt_button.clicked.connect(self.Sqrt)
            Keyboard_ui.Exponential_button.clicked.connect(self.Exponential_fun)
            Keyboard_ui.Constant_button.clicked.connect(self.Constant_fun)
            self.Current_lineEdit=2
        else:
            self.Keyboard.deleteLater()
            if self.form_var_tem!=0:
                self.Form.deleteLater()
                self.form_var_tem=0
            self.count=0
            self.a-=1

    def Keyboard_fun4(self):

        if self.a ==0:
            self.a+=1
        #Keyboard
            self.Keyboard=QtWidgets.QWidget(UI_Mainwindow)
            self.Keyboard.setMinimumHeight(70)
            self.Keyboard.setMaximumHeight(70)
            Keyboard_ui=Keyboard.Ui_Keyboard(self.Keyboard)

            self.Addition_Layout=QtWidgets.QVBoxLayout(self.Keyboard)
            self.Addition_Layout.setContentsMargins(0,0,0,0)
            self.Addition_Layout.setObjectName("Addition_Layout")
            self.verticalLayout.addLayout(self.Addition_Layout)
            self.Addition_Layout.addWidget(self.Keyboard)

            Keyboard_ui.x_pow_n_button.clicked.connect(self.superscript)
            Keyboard_ui.Pi_button.clicked.connect(self.Pi_fun)
            Keyboard_ui.Modulus_button.clicked.connect(self.Modulus)
            Keyboard_ui.Lessthan_button.clicked.connect(self.Lessthan_fun)
            Keyboard_ui.Greaterthan_button.clicked.connect(self.Greaterthan_fun)
            Keyboard_ui.Sqrt_button.clicked.connect(self.Sqrt)
            Keyboard_ui.Exponential_button.clicked.connect(self.Exponential_fun)
            Keyboard_ui.Constant_button.clicked.connect(self.Constant_fun)
            self.Current_lineEdit=3
        else:
            self.Keyboard.deleteLater()
            if self.form_var_tem!=0:
                self.Form.deleteLater()
                self.form_var_tem=0
            self.count=0
            self.a-=1

    def Keyboard_fun5(self):

        if self.a ==0:
            self.a+=1
        #Keyboard
            self.Keyboard=QtWidgets.QWidget(UI_Mainwindow)
            self.Keyboard.setMinimumHeight(70)
            self.Keyboard.setMaximumHeight(70)
            Keyboard_ui=Keyboard.Ui_Keyboard(self.Keyboard)

            self.Addition_Layout=QtWidgets.QVBoxLayout(self.Keyboard)
            self.Addition_Layout.setContentsMargins(0,0,0,0)
            self.Addition_Layout.setObjectName("Addition_Layout")
            self.verticalLayout.addLayout(self.Addition_Layout)
            self.Addition_Layout.addWidget(self.Keyboard)

            Keyboard_ui.x_pow_n_button.clicked.connect(self.superscript)
            Keyboard_ui.Pi_button.clicked.connect(self.Pi_fun)
            Keyboard_ui.Modulus_button.clicked.connect(self.Modulus)
            Keyboard_ui.Lessthan_button.clicked.connect(self.Lessthan_fun)
            Keyboard_ui.Greaterthan_button.clicked.connect(self.Greaterthan_fun)
            Keyboard_ui.Sqrt_button.clicked.connect(self.Sqrt)
            Keyboard_ui.Exponential_button.clicked.connect(self.Exponential_fun)
            Keyboard_ui.Constant_button.clicked.connect(self.Constant_fun)
            self.Current_lineEdit=4
        else:
            self.Keyboard.deleteLater()
            if self.form_var_tem!=0:
                self.Form.deleteLater()
                self.form_var_tem=0
            self.count=0
            self.a-=1

    def Keyboard_fun6(self):

        if self.a ==0:
            self.a+=1
    #Keyboard
            self.Keyboard=QtWidgets.QWidget(UI_Mainwindow)
            self.Keyboard.setMinimumHeight(70)
            self.Keyboard.setMaximumHeight(70)
            Keyboard_ui=Keyboard.Ui_Keyboard(self.Keyboard)

            self.Addition_Layout=QtWidgets.QVBoxLayout(self.Keyboard)
            self.Addition_Layout.setContentsMargins(0,0,0,0)
            self.Addition_Layout.setObjectName("Addition_Layout")
            self.verticalLayout.addLayout(self.Addition_Layout)
            self.Addition_Layout.addWidget(self.Keyboard)

            Keyboard_ui.x_pow_n_button.clicked.connect(self.superscript)
            Keyboard_ui.Pi_button.clicked.connect(self.Pi_fun)
            Keyboard_ui.Modulus_button.clicked.connect(self.Modulus)
            Keyboard_ui.Lessthan_button.clicked.connect(self.Lessthan_fun)
            Keyboard_ui.Greaterthan_button.clicked.connect(self.Greaterthan_fun)
            Keyboard_ui.Sqrt_button.clicked.connect(self.Sqrt)
            Keyboard_ui.Exponential_button.clicked.connect(self.Exponential_fun)
            Keyboard_ui.Constant_button.clicked.connect(self.Constant_fun)
            self.Current_lineEdit=5
        else:
            self.Keyboard.deleteLater()
            if self.form_var_tem!=0:
                self.Form.deleteLater()
                self.form_var_tem=0
            self.count=0
            self.a-=1

    def Keyboard_fun7(self):

        if self.a ==0:
            self.a+=1
    #Keyboard
            self.Keyboard=QtWidgets.QWidget(UI_Mainwindow)
            self.Keyboard.setMinimumHeight(70)
            self.Keyboard.setMaximumHeight(70)
            Keyboard_ui=Keyboard.Ui_Keyboard(self.Keyboard)

            self.Addition_Layout=QtWidgets.QVBoxLayout(self.Keyboard)
            self.Addition_Layout.setContentsMargins(0,0,0,0)
            self.Addition_Layout.setObjectName("Addition_Layout")
            self.verticalLayout.addLayout(self.Addition_Layout)
            self.Addition_Layout.addWidget(self.Keyboard)

            Keyboard_ui.x_pow_n_button.clicked.connect(self.superscript)
            Keyboard_ui.Pi_button.clicked.connect(self.Pi_fun)
            Keyboard_ui.Modulus_button.clicked.connect(self.Modulus)
            Keyboard_ui.Lessthan_button.clicked.connect(self.Lessthan_fun)
            Keyboard_ui.Greaterthan_button.clicked.connect(self.Greaterthan_fun)
            Keyboard_ui.Sqrt_button.clicked.connect(self.Sqrt)
            Keyboard_ui.Exponential_button.clicked.connect(self.Exponential_fun)
            Keyboard_ui.Constant_button.clicked.connect(self.Constant_fun)
            self.Current_lineEdit=6
        else:
            self.Keyboard.deleteLater()
            if self.form_var_tem!=0:
                self.Form.deleteLater()
                self.form_var_tem=0
            self.count=0
            self.a-=1


#for superscript slot
    def superscript(self):
        if(self.count>=1):
            self.Form.deleteLater()
            self.Form = QtWidgets.QWidget()
            self.ui = Keyboard_input.Keyboard_LineEdit(self.Form)
            self.ui.Function_LineEdit.setPlaceholderText("Enter the Superscript text")
            self.Addition_Layout.addWidget(self.Form)
            self.Form.setMinimumHeight(70)
            self.Form.setMaximumHeight(70)

        else:
            self.Form = QtWidgets.QWidget()
            self.ui = Keyboard_input.Keyboard_LineEdit(self.Form)
            self.ui.Function_LineEdit.setPlaceholderText("Enter the Superscript text")
            self.Addition_Layout.addWidget(self.Form)
            self.Form.setMinimumHeight(70)
            self.Form.setMaximumHeight(70)

        self.Enter_Button=QtWidgets.QPushButton(self.Keyboard)
        self.Enter_Button.setMinimumSize(QtCore.QSize(120, 61))
        self.Enter_Button.setMaximumSize(QtCore.QSize(140, 61))
        self.Enter_Button.setStyleSheet("QPushButton {\n"
                            "background-color: rgba(212, 212, 212, 250);\n"
                            "font: 75 italic 22pt Georgia;\n"
                            "color:rgba(255, 85, 0, 200);\n"
                            "border-radius:30px;\n"
                            "}\n"
                            "QPushButton:hover {\n"
                            "background-color: rgba(212, 212, 212, 52);\n"
                            "color:rgba(255, 85, 0, 250);\n"
                            "border-radius:30px;\n"
                            "}")
        self.Enter_Button.setObjectName("Enter_Button")
        self.verticalLayout.addWidget(self.Keyboard)
        self.Enter_Button.setText("Enter")
        self.ui.Input_Layout.addWidget(self.Enter_Button)

        self.count+=1
        self.Enter_Button.clicked.connect(self.Superscript_fun)
        self.form_var_tem=1


#for Modulus slot
    def Modulus(self):
        if(self.count>=1):
            self.Form.deleteLater()
            self.Form = QtWidgets.QWidget()
            self.ui = Keyboard_input.Keyboard_LineEdit(self.Form)
            self.ui.Function_LineEdit.setPlaceholderText("Enter the Modulus value")
            self.Addition_Layout.addWidget(self.Form)
            self.Form.setMinimumHeight(70)
            self.Form.setMaximumHeight(70)

        else:
            self.Form = QtWidgets.QWidget()
            self.ui = Keyboard_input.Keyboard_LineEdit(self.Form)
            self.ui.Function_LineEdit.setPlaceholderText("Enter the Modulus value")
            self.Addition_Layout.addWidget(self.Form)
            self.Form.setMinimumHeight(70)
            self.Form.setMaximumHeight(70)

        self.Enter_Button=QtWidgets.QPushButton(self.Keyboard)
        self.Enter_Button.setMinimumSize(QtCore.QSize(120, 61))
        self.Enter_Button.setMaximumSize(QtCore.QSize(140, 61))
        self.Enter_Button.setStyleSheet("QPushButton {\n"
                            "background-color: rgba(212, 212, 212, 250);\n"
                            "font: 75 italic 22pt Georgia;\n"
                            "color:rgba(255, 85, 0, 200);\n"
                            "border-radius:30px;\n"
                            "}\n"
                            "QPushButton:hover {\n"
                            "background-color: rgba(212, 212, 212, 52);\n"
                            "color:rgba(255, 85, 0, 250);\n"
                            "border-radius:30px;\n"
                            "}")
        self.Enter_Button.setObjectName("Enter_Button")
        self.verticalLayout.addWidget(self.Keyboard)
        self.Enter_Button.setText("Enter")
        self.ui.Input_Layout.addWidget(self.Enter_Button)

        self.count+=1
        self.form_var_tem=1
        self.Enter_Button.clicked.connect(self.Modulus_fun)


#For Squareroot slot
    def Sqrt(self):
        if(self.count>=1):
            self.Form.deleteLater()
            self.Form = QtWidgets.QWidget()
            self.ui = Keyboard_input.Keyboard_LineEdit(self.Form)
            self.ui.Function_LineEdit.setPlaceholderText("Enter the square root value")
            self.Addition_Layout.addWidget(self.Form)
            self.Form.setMinimumHeight(70)
            self.Form.setMaximumHeight(70)

        else:
            self.Form = QtWidgets.QWidget()
            self.ui = Keyboard_input.Keyboard_LineEdit(self.Form)
            self.ui.Function_LineEdit.setPlaceholderText("Enter the square root value")
            self.Addition_Layout.addWidget(self.Form)
            self.Form.setMinimumHeight(70)
            self.Form.setMaximumHeight(70)

        self.Enter_Button=QtWidgets.QPushButton(self.Keyboard)
        self.Enter_Button.setMinimumSize(QtCore.QSize(120, 61))
        self.Enter_Button.setMaximumSize(QtCore.QSize(140, 61))
        self.Enter_Button.setStyleSheet("QPushButton {\n"
                            "background-color: rgba(212, 212, 212, 250);\n"
                            "font: 75 italic 22pt Georgia;\n"
                            "color:rgba(255, 85, 0, 200);\n"
                            "border-radius:30px;\n"
                            "}\n"
                            "QPushButton:hover {\n"
                            "background-color: rgba(212, 212, 212, 52);\n"
                            "color:rgba(255, 85, 0, 250);\n"
                            "border-radius:30px;\n"
                            "}")
        self.Enter_Button.setObjectName("Enter_Button")
        self.verticalLayout.addWidget(self.Keyboard)
        self.Enter_Button.setText("Enter")
        self.ui.Input_Layout.addWidget(self.Enter_Button)
        self.form_var_tem=1
        self.count+=1
        self.Enter_Button.clicked.connect(self.Sqrt_fun)

    Interval_input=[]
    temp3=0




    def message(self,input="Please Enter all the Inputs",head="Missing Inputs"):
        self.Equation_input=[]
        self.Interval_input=[]
        self.msg = QtWidgets.QMessageBox()
        self.msg.setIcon(QtWidgets.QMessageBox.Warning)
        self.msg.setStyleSheet("font: 75 italic 20pt \"Georgia\";")

        self.msg.setText(input)
        self.msg.setWindowTitle(head)
        self.msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        self.msg.show()
        self.msg.buttonClicked.connect(self.msg.close)


    def checkEqnfun(self):

        if len(self.Equation_input)!=len(self.Interval_input):
            self.message()

        # for x in self.Equation_input:
        #     if x=="":
        #         self.message("Enter the equation inputs Correctly")
        #
        # for y in self.Interval_input:
        #     if y=="":
        #         self.message("Enter the interval inputs correctly")

        if self.Harmonic_Num=="":
            self.message("Please Enter the Harmonic Number")

    def Equation_fun(self):
        try:
        #Functions
            if(self.temp3==1):
                self.Equation_input=[]
                self.Interval_input=[]
            self.temp3=1
            for x in self.Function_Input_List:
                temp=""
                temp=x.Function_LineEdit.toHtml()
                # print(temp)
                interval=x.Interval_LineEdit.displayText()
                interval+=" "
                for y in range(len(temp)):
                    if(temp[y:y+37:]=="<span style=\" vertical-align:super;\">"):
                        m=temp[:y:]
                        z=temp[y+37::]
                        temp=m+"**"+z
                    if(temp[y:y+7:]=="</span>"):
                        m=temp[:y:]
                        z=temp[y+7::]
                        temp=m+z
                for iter in range(len(temp)):
                    if(temp[iter]=="\u03C0"):
                        m=temp[:iter:]
                        n=temp[iter+1::]
                        temp=m+"3.14"+n

                for iter in range(len(interval)):
                    if(interval[iter]=="<"):
                        m=interval[:iter:]
                        interval=interval[iter+1::]
                        break

                for iter in range(len(interval)):
                    if(interval[iter]=="<"):

                        n=interval[iter+1::]
                        break

                self.Interval_input.append(m+","+n)
                x.Function_LineEdit.setText(temp)
                temp=x.Function_LineEdit.toPlainText()
                self.Equation_input.append(temp)
                self.Harmonic_Num=self.Harmonic_lineEdit.displayText()


            for m in range(len(self.Equation_input)):
                print(self.Equation_input[m],self.Interval_input[m])

            print(self.Harmonic_Num)

            import re

            self.Harmonic_Num=re.sub(' ','',self.Harmonic_Num)

            self.checkEqnfun()

            f = open("input.txt","w")
            f.write(str(len(self.Equation_input))+"\n")
            for pp in range(len(self.Equation_input)):
                pal=self.Equation_input[pp]
                sal=self.Interval_input[pp]+"\n"
                pal=re.sub(' ','',pal)
                sal=re.sub(' ','',sal)
                f.write(pal+" "+sal)
            f.write(self.Harmonic_Num+"\n")
            f.close()

            os.system("E:")
            os.system("cd \"Python Package\"")
            os.system("python Graph.py")

        except:
            self.message()


        #proper naming of widgets
    def retranslateUi(self, UI_Mainwindow):
        _translate = QtCore.QCoreApplication.translate
        UI_Mainwindow.setWindowTitle(_translate("UI_Mainwindow", "Harmonic Analysis"))
        self.TitleLabel.setText(_translate("UI_Mainwindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                    "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                    "p, li { white-space: pre-wrap; }\n"
                    "</style></head><body style=\" font-family:\'Georgia\'; font-size:24pt; font-weight:72; font-style:italic;\">\n"
                    "<p align=\"center\" dir=\'rtl\' style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Harmonic Analysis</p></body></html>"))
        self.Info_Label.setText(_translate("UI_Mainwindow", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:400;\">Enter the function and its interval :</span></p></body></html>"))
        self.AddFunction_Button.setText(_translate("UI_Mainwindow", "+"))
        self.Function_Label_2.setText(_translate("UI_Mainwindow", "<html><head/><body><p><span style=\" font-size:18pt;\">Harmonic Number :</span></p></body></html>"))
        self.Harmonic_lineEdit.setPlaceholderText(_translate("UI_Mainwindow", "100 "))
        self.Getgraph.setText(_translate("UI_Mainwindow", "Get Graph"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    UI_Mainwindow = QtWidgets.QMainWindow()
    ui = Ui_UI_Mainwindow()
    UI_Mainwindow.setGeometry(0,0,1920,1080)
    UI_Mainwindow.showMaximized()
    ui.setupUi(UI_Mainwindow)
    UI_Mainwindow.show()
    sys.exit(app.exec_())
