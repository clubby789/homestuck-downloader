import sys, hsdl, glob, requests
from PyQt5.QtWidgets import QMainWindow, QTextEdit, QAction, QApplication, QLabel
from PyQt5.QtCore import (Qt)
from PyQt5.QtGui import *
s = requests.Session()

def readText(page):
    fileName = "./downloaded/images/"+str(page).rjust(5,'0')+"*.gif"
    if not glob.glob(fileName):
        hsdl.dlPage(page,s)
    with open("./downloaded/text/"+str(page)+".txt", 'r') as f:
        text = f.read()
        title = text[text.find("title:")+6:text.find("TITLEEND")]
        if not text.find("body:") == -1:
            body = text[text.find("body:")+5:text.find("BODYEND")]
        else:
            body = ""
        command = text[text.find("command:")+8:text.find("COMMANDEND")]
    return [title,body,command]
            
class Page():
    text = []
    def __init__(self,page):
        self.text = readText(page)
class Example(QMainWindow):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):               
        p1 = Page(1)
        title = p1.text[0]
        body = p1.text[1]
        command = p1.text[2]
        lbl1 = QLabel(title, self)
        lbl1.move(370,50)
        lbl2 = QLabel(body, self)
        lbl2.move(100,100)
        lbl2.resize(5700,500)
        
        lbl3 = QLabel(command, self)
        lbl3.move(55, 70)   
        
        self.setGeometry(300, 300, 750, 550)
        self.setWindowTitle('Main window')    
        self.show()

        
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
