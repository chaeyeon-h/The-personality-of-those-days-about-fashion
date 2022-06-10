from tkinter import font
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
import sys

class Ui():
    
    def __init__(self):
        self.MainWindow=QtWidgets.QMainWindow()
        self.MainWindow.setGeometry(700,60,800,950)
        self.MainWindow.setMinimumSize(800,950)
        self.MainWindow.setMaximumSize(800,950)
        self.MainWindow.setStyleSheet("background-color : white;")

        self.centralwidget = QtWidgets.QWidget(self.MainWindow)

        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(0,0,1500,1600)

        self.stackedWidget.setObjectName("stackedWidget")

#########################################################################################
#loginPage

#사진넣기 코드
        self.loginPage=QtWidgets.QWidget()
        self.loginPage.setObjectName("LoginPage")
        loginBorder=QtWidgets.QLabel(self.loginPage)
        loginBorder.setGeometry(25,20,750,900)
        loginBorder.setStyleSheet("background-color: white ;border-style: solid;border-color: #FF843A; border-width: 10px")

 
        loginLogoPic=QtWidgets.QLabel(self.loginPage)
        loginLogoPic.setGeometry(225,60,350,260)
        loginLogoPic.setStyleSheet("background-color: white;")
        self.qPixmapVar = QPixmap()
        self.qPixmapVar.load("image/loginlogo.jpg")
        self.qPixmapVar=self.qPixmapVar.scaled(350,260)
        loginLogoPic.setPixmap(self.qPixmapVar)

        loginLogo=QtWidgets.QLabel(self.loginPage)
        loginLogo.setGeometry(190,330,500,100)
        font=QtGui.QFont()      
        font.setFamily("HY중고딕")
        font.setPointSize(37)
        loginLogo.setFont(font)
        loginLogo.setText("그 ㅅi절 ㄱH성")
        loginLogo.setStyleSheet("background-color: white; color:black;")

        
        loginLogo=QtWidgets.QLabel(self.loginPage)
        loginLogo.setGeometry(200,440,100,30)
        font=QtGui.QFont()
        font.setFamily("함초롬돋움")
        font.setPointSize(13)
        loginLogo.setFont(font)
        loginLogo.setText("이메일*")
        font.setBold(True)
        loginLogo.setStyleSheet("background-color: white;")


        self.loginIdEnter=QtWidgets.QLineEdit(self.loginPage)
        self.loginIdEnter.setGeometry(200,480,400,50)
        self.loginIdEnter.setStyleSheet("background-color: #ffffff;  border-style: solid; border-width:2px; border-color:#A6A6A6 ; border-radius:2px")
        font=QtGui.QFont()
        font.setFamily("함초롬돋움")
        self.loginIdEnter.setFont(font)
        
        
        loginLogo=QtWidgets.QLabel(self.loginPage)
        loginLogo.setGeometry(200,540,100,30)
        font=QtGui.QFont()
        font.setFamily("함초롬돋움")
        font.setPointSize(13)
        loginLogo.setFont(font)
        loginLogo.setText("비밀번호*")
        font.setBold(True)
        loginLogo.setStyleSheet("background-color: white;")

        
        self.loginPwEnter=QtWidgets.QLineEdit(self.loginPage)
        self.loginPwEnter.setGeometry(200,580,400,50)
        self.loginPwEnter.setStyleSheet("background-color: white; border-style: solid;border-width:2px; border-color:#A6A6A6; border-radius:2px")
        font=QtGui.QFont()
        font.setFamily("함초롬돋움")
        self.loginPwEnter.setFont(font)
        self.loginPwEnter.setEchoMode(QtWidgets.QLineEdit.Password)
        
        self.stackedWidget.addWidget(self.loginPage)
 

        self.loginBtn=QtWidgets.QToolButton(self.loginPage)
        self.loginBtn.setGeometry(200,660,400,50)
        font=QtGui.QFont()
        self.loginBtn.setStyleSheet("background-color: white ;border-style: solid;border-color: #FFD4B9; border-width: 2px;border-radius:5px")
        font.setFamily("함초롬돋움")
        font.setBold(True)
        font.setPointSize(10)
        self.loginBtn.setFont(font)
        self.loginBtn.setText("로그인")
        self.loginBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        

       
        
        self.loginJoinBtn=QtWidgets.QToolButton(self.loginPage)
        self.loginJoinBtn.setGeometry(200,720,400,50)
        font=QtGui.QFont()
        self.loginJoinBtn.setStyleSheet("background-color: white ;border-style: solid;border-color: #FFD4B9; border-width: 2px;border-radius:5px ")
        font.setBold(True)
        self.loginJoinBtn.setText("회원가입")
        self.loginJoinBtn.setFont(font)
        self.loginJoinBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        font.setFamily("함초롬돋움")
        

        self.loginIdBtn=QtWidgets.QToolButton(self.loginPage)
        self.loginIdBtn.setGeometry(200,780,195,50)
        font=QtGui.QFont()
        self.loginIdBtn.setStyleSheet("background-color: white ;border-style: solid;border-color: #FFD4B9; border-width: 2px;border-radius:5px")
        font.setFamily("함초롬돋움")
        font.setBold(True)
        font.setPointSize(10)
        self.loginIdBtn.setFont(font)
        self.loginIdBtn.setText("이메일 찾기")
        self.loginIdBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.loginPwBtn=QtWidgets.QToolButton(self.loginPage)
        self.loginPwBtn.setGeometry(405,780,195,50)
        font=QtGui.QFont()
        self.loginPwBtn.setStyleSheet("background-color: white ;border-style: solid;border-color: #FFD4B9; border-width: 2px;border-radius:5px")
        font.setFamily("함초롬돋움")
        font.setBold(True)
        font.setPointSize(10)
        self.loginPwBtn.setFont(font)
        self.loginPwBtn.setText("비밀번호 찾기")
        self.loginPwBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))


        self.MainWindow.setCentralWidget(self.centralwidget)

################################################################################################################################
        
#findPW page
        self.findPw=QtWidgets.QWidget()
        self.findPw.setObjectName("findPw")
        findBorder=QtWidgets.QLabel(self.findPw)
        findBorder.setGeometry(25,20,750,900)
        findBorder.setStyleSheet("background-color:white ;border-style: solid;border-color: #FF843A; border-width: 10px")

        self.findPwBacktoLogin=QtWidgets.QPushButton(self.findPw)
        self.findPwBacktoLogin.setGeometry(700,40,40,40)
        self.findPwBacktoLogin.setIcon(QtGui.QIcon("image/backbtn.png"))
        self.findPwBacktoLogin.setIconSize(QtCore.QSize(60,60))
        
        self.stackedWidget.addWidget(self.findPw)
        
        findLogo=QtWidgets.QLabel(self.findPw)
        findLogo.setGeometry(70,40,210,51)
        font=QtGui.QFont()
        font.setFamily("함초롬돋움")
        font.setPointSize(20)
        findLogo.setFont(font)
        findLogo.setText("비밀번호 찾기")
        font.setBold(True)
        findLogo.setStyleSheet("background-color: white;")

        self.loginBtn.setStyleSheet("background-color: white ;border-style: solid;border-color: #FFD4B9; border-width: 2px;border-radius:5px")
        font.setFamily("함초롬돋움")
        font.setPointSize(10)
        self.loginBtn.setFont(font)
        self.loginBtn.setText("확인")
        self.loginBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        
     
        FindPwLogoPic=QtWidgets.QLabel(self.findPw)
        FindPwLogoPic.setGeometry(320,140,180,150)
        FindPwLogoPic.setStyleSheet("background-color: white;")
        self.qPixmapVar = QPixmap()
        self.qPixmapVar.load("image/findlog.png")
        self.qPixmapVar=self.qPixmapVar.scaled(180,150)
        FindPwLogoPic.setPixmap(self.qPixmapVar)
        
#이름,이메일,생년월일 쓰는 빈칸 

        findLogo=QtWidgets.QLabel(self.findPw)
        findLogo.setGeometry(150,330,210,50)
        font=QtGui.QFont()
        font.setFamily("함초롬돋움")
        font.setPointSize(13)
        findLogo.setFont(font)
        findLogo.setText("이름*")
        font.setBold(True)
        findLogo.setStyleSheet("background-color: white;")


        self.findPwName=QtWidgets.QLineEdit(self.findPw)
        self.findPwName.setGeometry(150,390,500,50)
        self.findPwName.setStyleSheet("background-color: white ;  border-style: solid; border-color:#A6A6A6; border-width:2px; border-radius:2px")
        font=QtGui.QFont()
        font.setFamily("함초롬돋움")
        self.findPwName.setFont(font)

        findLogo=QtWidgets.QLabel(self.findPw)
        findLogo.setGeometry(150,450,200,50)
        font=QtGui.QFont()
        font.setFamily("함초롬돋움")
        font.setPointSize(13)
        findLogo.setFont(font)
        findLogo.setText("이메일*")
        font.setBold(True)
        findLogo.setStyleSheet("background-color: white;")
    
        self.findPwID=QtWidgets.QLineEdit(self.findPw)
        self.findPwID.setGeometry(150,510,500,50)
        font=QtGui.QFont()
        font.setFamily("함초롬돋움")
        self.findPwID.setFont(font)
        self.findPwID.setStyleSheet("background-color:white;  border-style: solid;border-width:2px; border-color:#A6A6A6;border-radius:2px")
        
               
        findLogo=QtWidgets.QLabel(self.findPw)
        findLogo.setGeometry(150,580,500,50)
        font=QtGui.QFont()
        font.setFamily("함초롬돋움")
        font.setPointSize(13)
        findLogo.setFont(font)
        findLogo.setText("생년월일*")
        font.setBold(True)
        findLogo.setStyleSheet("background-color: white;")
    

        self.findPwBirth=QtWidgets.QLineEdit(self.findPw)
        self.findPwBirth.setGeometry(150,640,500,50)
        self.findPwBirth.setStyleSheet("background-color: white ; border-style: solid; border-width:2px; border-color:#A6A6A6;border-radius:2px")
        font=QtGui.QFont()
        font.setFamily("함초롬돋움")
        self.findPwBirth.setFont(font)

        self.findPwBtn=QtWidgets.QToolButton(self.findPw)
        self.findPwBtn.setGeometry(200,740,400,50)
        font=QtGui.QFont()
        self.findPwBtn.setStyleSheet("background-color: white ;border-style: solid;border-color: #FFD4B9; border-width: 2px;border-radius:5px")
        font.setFamily("함초롬돋움")
        font.setBold(True)
        font.setPointSize(10)
        self.findPwBtn.setFont(font)
        self.findPwBtn.setText("확인")
        self.findPwBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        font.setPointSize(10)

################################################################################################################################################

#findId page
        self.findId=QtWidgets.QWidget()
        self.findId.setObjectName("findId")
        findBorder=QtWidgets.QLabel(self.findId)
        findBorder.setGeometry(25,20,750,900)
        findBorder.setStyleSheet("background-color:white ;border-style: solid;border-color: #FF843A; border-width: 10px")

        

        self.findIdBacktoLogin=QtWidgets.QPushButton(self.findId)
        self.findIdBacktoLogin.setGeometry(700,40,40,40)
        self.findIdBacktoLogin.setIcon(QtGui.QIcon("image/backbtn.png"))
        self.findIdBacktoLogin.setIconSize(QtCore.QSize(60,60))
        
        findLogo=QtWidgets.QLabel(self.findId)
        findLogo.setGeometry(70,40,210,51)
        font=QtGui.QFont()
        font.setFamily("함초롬돋움")
        font.setPointSize(20)
        findLogo.setFont(font)
        findLogo.setText("이메일 찾기")
        font.setBold(True)
        findLogo.setStyleSheet("background-color: white;")
        


        
         
        FindIdLogoPic=QtWidgets.QLabel(self.findId)
        FindIdLogoPic.setGeometry(320,140,180,150)
        FindIdLogoPic.setStyleSheet("background-color: white;")
        self.qPixmapVar = QPixmap()
        self.qPixmapVar.load("image/findlog.png")
        self.qPixmapVar=self.qPixmapVar.scaled(180,150)
        FindIdLogoPic.setPixmap(self.qPixmapVar)

#이름,이메일 쓰는 빈칸 

        findLogo=QtWidgets.QLabel(self.findId)
        findLogo.setGeometry(150,370,210,51)
        font=QtGui.QFont()
        font.setFamily("함초롬돋움")
        font.setPointSize(13)
        findLogo.setFont(font)
        findLogo.setText("이름*")
        font.setBold(True)
        findLogo.setStyleSheet("background-color: white;")


        self.findIdName=QtWidgets.QLineEdit(self.findId)
        self.findIdName.setGeometry(150,430,500,50)
        self.findIdName.setStyleSheet("background-color: white ;border-style: solid;border-width:2px; border-color:#A6A6A6;border-radius:2px")
        font=QtGui.QFont()
        font.setFamily("함초롬돋움")
        self.findIdName.setFont(font)
        findLogo=QtWidgets.QLabel(self.findId)
        findLogo.setGeometry(150,500,500,50)
        
        font=QtGui.QFont()
        font.setFamily("함초롬돋움")
        font.setPointSize(13)
        findLogo.setFont(font)
        findLogo.setText("생년월일*")
        font.setBold(True)
        findLogo.setStyleSheet("background-color: white;")
        
        self.findIdBirth=QtWidgets.QLineEdit(self.findId)
        self.findIdBirth.setGeometry(150,560,500,50)
        self.findIdBirth.setStyleSheet("background-color: #ffffff;border-style: solid; border-width:2px; border-color:#A6A6A6;border-radius:2px")
        font=QtGui.QFont()
        font.setFamily("함초롬돋움")
        self.findIdBirth.setFont(font)


        self.findIdBtn=QtWidgets.QToolButton(self.findId)
        self.findIdBtn.setGeometry(200,700,400,50)
        font=QtGui.QFont()
        self.findIdBtn.setStyleSheet("background-color: white ;border-style: solid;border-color: #FFD4B9; border-width: 2px;border-radius:5px")
        font.setFamily("함초롬돋움")
        font.setBold(True)
        font.setPointSize(10)
        self.findIdBtn.setFont(font)
        self.findIdBtn.setText("확인")
        self.findIdBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))



        self.stackedWidget.addWidget(self.findId)
        font.setPointSize(10)

################################################################################################################################################

#join page
        self.joinPage=QtWidgets.QWidget()
        self.joinPage.setObjectName("joinPage")
        
        joinBorder=QtWidgets.QLabel(self.joinPage)
        joinBorder.setGeometry(25,20,750,900)
        joinBorder.setStyleSheet("background-color:white ;border-style: solid;border-color: #FF843A; border-width: 10px")
        
        joinLogo=QtWidgets.QLabel(self.joinPage)
        joinLogo.setGeometry(70,40,210,51)
        font=QtGui.QFont()
        font.setFamily("함초롬돋움")
        font.setPointSize(20)
        joinLogo.setFont(font)
        joinLogo.setText("회원가입")
        joinLogo.setStyleSheet("background-color: white;")


        self.joinBacktoLogin=QtWidgets.QPushButton(self.joinPage)
        self.joinBacktoLogin.setGeometry(700,40,40,40)
        self.joinBacktoLogin.setIcon(QtGui.QIcon("image/backbtn.png"))
        self.joinBacktoLogin.setIconSize(QtCore.QSize(60,60))
                

        
        JoinLogoPic=QtWidgets.QLabel(self.joinPage)
        JoinLogoPic.setGeometry(320,140,180,150)
        JoinLogoPic.setStyleSheet("background-color: white;")
        self.qPixmapVar = QPixmap()
        self.qPixmapVar.load("image/joinlog.png")
        self.qPixmapVar=self.qPixmapVar.scaled(180,150)
        JoinLogoPic.setPixmap(self.qPixmapVar)

        addLogo=QtWidgets.QLabel(self.joinPage)
        addLogo.setGeometry(200,330,100,40)
        font=QtGui.QFont()
        font.setFamily("함초롬돋움")
        font.setPointSize(11)
        addLogo.setFont(font)
        addLogo.setText("이름*")
        font.setBold(True)
        addLogo.setStyleSheet("background-color: white;")        

        self.joinNameEnter=QtWidgets.QLineEdit(self.joinPage)
        self.joinNameEnter.setGeometry(200,370,400,50)
        self.joinNameEnter.setStyleSheet("background-color: white;border-style: solid;border-width:2px; border-color:#A6A6A6;border-radius:2px")
        font=QtGui.QFont()
        font.setFamily("함초롬돋움")
        self.joinNameEnter.setFont(font)
                
        
        addLogo=QtWidgets.QLabel(self.joinPage)
        addLogo.setGeometry(200,430,210,40)
        font=QtGui.QFont()
        font.setFamily("함초롬돋움")
        font.setPointSize(11)
        addLogo.setFont(font)
        addLogo.setText("이메일*")
        font.setBold(True)
        addLogo.setStyleSheet("background-color: white;")

        self.joinEmailEnter=QtWidgets.QLineEdit(self.joinPage)
        self.joinEmailEnter.setGeometry(200,470,400,50)
        self.joinEmailEnter.setStyleSheet("background-color: white ;border-style: solid;border-width:2px; border-color:#A6A6A6;border-radius:2px")
        font=QtGui.QFont()
        font.setFamily("함초롬돋움")
        self.joinEmailEnter.setFont(font)

        addLogo=QtWidgets.QLabel(self.joinPage)
        addLogo.setGeometry(200,530,210,40)
        font=QtGui.QFont()
        font.setFamily("함초롬돋움")
        font.setPointSize(11)
        addLogo.setFont(font)
        addLogo.setText("비밀번호*")
        font.setBold(True)
        addLogo.setStyleSheet("background-color: white;")
        
        self.joinPwEnter=QtWidgets.QLineEdit(self.joinPage)
        self.joinPwEnter.setGeometry(200,570,400,50)
        self.joinPwEnter.setStyleSheet("background-color: #ffffff; border-style: solid; border-width:2px; border-color:#A6A6A6;border-radius:2px")
        font=QtGui.QFont()
        font.setFamily("함초롬돋움")
        self.joinPwEnter.setFont(font)
        
        
        addLogo=QtWidgets.QLabel(self.joinPage)
        addLogo.setGeometry(200,630,210,40)
        font=QtGui.QFont()
        font.setFamily("함초롬돋움")
        font.setPointSize(11)
        addLogo.setFont(font)
        addLogo.setText("생년월일(8자리)*")
        font.setBold(True)
        addLogo.setStyleSheet("background-color: white;")
        
        self.joinBirthEnter=QtWidgets.QLineEdit(self.joinPage)
        self.joinBirthEnter.setGeometry(200,670,400,50)
        self.joinBirthEnter.setStyleSheet("background-color: white;border-style: solid; border-width:2px; border-color:#A6A6A6;border-radius:2px")
        font=QtGui.QFont()
        font.setFamily("함초롬돋움")
        self.joinBirthEnter.setFont(font)


        self.joinBtn=QtWidgets.QToolButton(self.joinPage)
        self.joinBtn.setGeometry(300,740,200,50)
        font=QtGui.QFont()
        self.joinBtn.setStyleSheet("background-color:#A6A6A6;color:#ffffff;border-radius:8px")
        font.setFamily("함초롬돋움")
        font.setBold(True)
        font.setPointSize(10)
        self.joinBtn.setFont(font)
        self.joinBtn.setText("가입")
        self.joinBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.stackedWidget.addWidget(self.joinPage)


################################################################################################################################################

        font.setPointSize(10)

        
        self.stackedWidget.setCurrentWidget(self.loginPage)
        
        self.MainWindow.setCentralWidget(self.centralwidget)

        self.MainWindow.show()


    def dialogError(self,Dialog,text):
        Dialog.setObjectName("Dialog")
        Dialog.resize(750,550)
        dialogBorder=QtWidgets.QLabel(Dialog)
        dialogBorder.setGeometry(20,10,700,500)
        dialogBorder.setStyleSheet("background-color: white ;border-style: solid;border-color: #FF843A ; border-width: 10px")
        Dialog.setStyleSheet("background-color : white;")


        LogoPic=QtWidgets.QLabel(Dialog)
        LogoPic.setGeometry(30,120,250,220)
        LogoPic.setStyleSheet("background-color: white;")
        self.qPixmapVar = QPixmap()
        self.qPixmapVar.load("image/joinpic.jpg")
        self.qPixmapVar=self.qPixmapVar.scaled(250,220)
        LogoPic.setPixmap(self.qPixmapVar)



        self.dialogLabel = QtWidgets.QLabel(Dialog)
        self.dialogLabel.setGeometry(280, 110, 400, 300)
        font = QtGui.QFont()
        font.setFamily("함초롬돋움")
        font.setPointSize(14)
        self.dialogLabel.setFont(font)
        self.dialogLabel.setText(text)
        self.dialogLabel.setStyleSheet("color : red;")
        self.dialogLabel.setObjectName("label")




if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    Main=Ui()
    Main.MainWindow.show()
    sys.exit(app.exec_())
    