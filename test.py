import main,re,data, loginPage
from tkinter import font
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
import sys

class Event():
    
    def __init__(self):
        self.number=0
        # self를 활용하는 멤버변수의 경우 생성자에서 초기화 할것
        self.ui=main.Ui()
        # 임포트 받은 ui클래스를 객체화 해준것임 
        self.db=loginPage.LoginPage()
        self.ui.MainWindow.show()
       




        
        
#id찾기 페이지에서 찾기를 누르면
    def IdcheckBtn(self):
        self.ui.findIdBtn.clicked.connect(self.Idcheck)
    def Idcheck(self):
        myName=self.ui.joinNameEnter.text()
        myBirth=self.ui.joinBirthEnter.text()

#Pw찾기 페이지에서 찾기를 누르면
    def PwcheckBtn(self):
        self.ui.findPwBtn.clicked.connect(self.Pwcheck)
    def Pwcheck(self):
        myName=self.ui.joinNameEnter.text()
        myEmail=self.ui.joinEmailEnter.text()
        myBirth=self.ui.joinBirthEnter.text()






if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    Main=Event()
    sys.exit(app.exec_())