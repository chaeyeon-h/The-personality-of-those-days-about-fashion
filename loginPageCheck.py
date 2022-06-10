import data
import main
import joinPageCheck, FindIdCheck,FindPwCheck
from tkinter import font
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
import sys
class LoginPage:
    def __init__(self):
        self.db=data.Database()
        self.ui=main.Ui()
        self.join=joinPageCheck.JoinPage(self.ui)
        self.Id=FindIdCheck.FindId(self .ui)
        self.Pw=FindPwCheck.FindPw(self.ui)

        self.btnCheckMover()
        self.btnJoinMover()
        self.btnFindIdMover()
        self.btnFindPwMover()

#db랑 입력정보 비교하는 함수
    def memberLogin(self,idValue,pwValue):
        if len(self.db.readData("user",["email","pw"],[idValue, pwValue]))!=0:
            dialogError=QtWidgets.QDialog()
            self.ui.dialogError(dialogError,"로그인 성공")
            dialogError.show()
            dialogError.exec()
            self.ui.stackedWidget.setCurrentWidget(self.ui.findId) #창 선택페이지로 바꿔야뎀
            self.editClear()
            return True

        else:
            dialogError=QtWidgets.QDialog()
            self.ui.dialogError(dialogError,"로그인 실패")
            dialogError.show()
            dialogError.exec()
            return False
        
        

        

#확인 버튼 누르면 -> 이메일 비번 db에서 찾기
    def btnCheckMover(self):
        self.ui.loginBtn.clicked.connect(self.checkmove)
    def checkmove(self):
        myEmail=self.ui.loginIdEnter.text()
        myPw=self.ui.loginPwEnter.text()
        self.memberLogin(myEmail, myPw)

#회원가입 버튼 누르면 -> joinPage로 이동
    def btnJoinMover(self):
        self.ui.loginJoinBtn.clicked.connect(self.joinmove)
    def joinmove(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.joinPage)

#이메일 찾기 버튼 누르면 -> findIdPage로 이동
    def btnFindIdMover(self):
        self.ui.loginIdBtn.clicked.connect(self.FindIdmove)
    def FindIdmove(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.findId)

#비밀번호 찾기 버튼 누르면 -> findPwPage로 이동     
    def btnFindPwMover(self):
        self.ui.loginPwBtn.clicked.connect(self.FindPwMove)
    def FindPwMove(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.findPw)

    def editClear(self):
        self.ui.loginPwEnter.setText("")
        self.ui.loginIdEnter.setText("")


if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    lg=LoginPage()
    sys.exit(app.exec_()) 
