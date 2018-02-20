import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QInputDialog, QTextBrowser,QLineEdit)

class GUI(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.list_1=[]
        self.list_2=[]
        self.calculate()

    def initUI(self):
        self.setGeometry(500,500,1000,500)
        self.setWindowTitle('真实GPA计算器')

        self.lable_1=QLabel("科目：",self)
        self.lable_2=QLabel("学分:",self)
        self.lable_3=QLabel("成绩:",self)
        self.label_4=QLabel("科目:",self)
        self.label_5=QLabel("GPA:",self)
        self.label_6=QLabel("加权GPA:",self)

        self.lable_1.move(20,40)
        self.lable_2.move(20,120)
        self.lable_3.move(20,200)
        self.label_4.move(450,20)
        self.label_5.move(700,20)
        self.label_6.move(450,400)

        self.textbox_1=QLineEdit(self)
        self.textbox_1.move(100,20)
        self.textbox_1.resize(300,50)

        self.textbox_2=QLineEdit(self)
        self.textbox_2.move(100,100)
        self.textbox_2.resize(300,50)


        self.textbox_3=QLineEdit(self)
        self.textbox_3.move(100,180)
        self.textbox_3.resize(300,50)

        self.textbox_4=QTextBrowser(self)
        self.textbox_4.move(450,70)
        self.textbox_4.resize(200,300)

        self.textbox_5=QTextBrowser(self)
        self.textbox_5.move(700,70)
        self.textbox_5.resize(200,300)

        #self.textbox_6=QTextBrowser(self)
        #self.textbox_6.move(450,420)
        #self.textbox_6.resize(120,30)

        self.textbox_7 = QTextBrowser(self)
        self.textbox_7.move(450, 420)
        self.textbox_7.resize(130, 50)

        self.button_1=QPushButton("submit",self)
        self.button_1.move(20,450)
        self.button_1.clicked.connect(self.show_text)


    def show_text(self):

        text_1=self.textbox_1.text()
        text_2=self.textbox_2.text()
        text_3=self.textbox_3.text()


        self.textbox_3.setText(' ')
        self.textbox_2.setText(' ')
        self.textbox_1.setText(' ')

        gpa=self.search(int(text_3))
        credit=int(text_2)

        self.textbox_4.append(text_1)
        self.textbox_5.append(str(gpa))

        self.list_1.append(gpa)
        self.list_2.append(credit)

        print(self.list_1)
        print(self.list_2)
        self.calculate()

    def search(self,score):
        if score>=95:
            return 4.3
        elif score>=90:
            return 4.0
        elif score>=85:
            return 3.7
        elif score>=83:
            return 3.3
        elif score>=78:
            return 3.0
        elif score>=75:
            return 2.7
        elif score>=72:
            return 2.3
        elif score>=68:
            return 2
        elif score>=65:
            return 1.7
        elif score>=64:
            return 1.5
        elif score>=61:
            return 1.3
        elif score==60:
            return 1
        else:
            return 0

    def calculate(self):
        sum=0
        credit_sum=0

        for i in range(len(self.list_1)):
            sum+=self.list_1[i] * self.list_2[i]

        for i in self.list_2:
            credit_sum+=i
        if len(self.list_1)==0:
            return 0
        else:
            print(float('%.5f'%(sum/credit_sum)))
            self.textbox_7.setText(('%.5f'%(sum/credit_sum)))

if __name__ == '__main__':
    app=QApplication(sys.argv)
    gui=GUI()
    gui.show()
    sys.exit(app.exec_())