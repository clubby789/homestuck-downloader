# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hsdl.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 884)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.labelTitle = QtWidgets.QLabel(self.centralwidget)
        self.labelTitle.setGeometry(QtCore.QRect(0, 20, 791, 41))
        self.labelTitle.setTextFormat(QtCore.Qt.RichText)
        self.labelTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.labelTitle.setObjectName("labelTitle")
        self.labelBody = QtWidgets.QLabel(self.centralwidget)
        self.labelBody.setGeometry(QtCore.QRect(60, 430, 651, 231))
        self.labelBody.setTextFormat(QtCore.Qt.RichText)
        self.labelBody.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.labelBody.setObjectName("labelBody")
        self.buttonNext = QtWidgets.QPushButton(self.centralwidget)
        self.buttonNext.setGeometry(QtCore.QRect(150, 720, 461, 91))
        self.buttonNext.setObjectName("buttonNext")
        self.viewImage = QtWidgets.QGraphicsView(self.centralwidget)
        self.viewImage.setGeometry(QtCore.QRect(140, 80, 501, 331))
        self.viewImage.setObjectName("viewImage")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Homestuck Downloader"))
        self.labelTitle.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:28pt; font-weight:600;\">Title Text</span></p></body></html>"))
        self.labelBody.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt;\">A young man stands in his bedroom</span></p><p><br/></p></body></html>"))
        self.buttonNext.setText(_translate("MainWindow", "Enter Name"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

