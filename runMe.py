from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
import sys
from pdf2audio import p2a

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(591, 155)
        font = QtGui.QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.fileToolButton1 = QtWidgets.QToolButton(self.centralwidget)
        self.fileToolButton1.setGeometry(QtCore.QRect(530, 20, 27, 22))
        self.fileToolButton1.setObjectName("fileToolButton1")
        self.fileLabel = QtWidgets.QLabel(self.centralwidget)
        self.fileLabel.setGeometry(QtCore.QRect(10, 20, 131, 16))
        self.fileLabel.setObjectName("fileLabel")
        self.saveLabel = QtWidgets.QLabel(self.centralwidget)
        self.saveLabel.setGeometry(QtCore.QRect(10, 60, 141, 16))
        self.saveLabel.setObjectName("saveLabel")
        self.fileToolButton2 = QtWidgets.QToolButton(self.centralwidget)
        self.fileToolButton2.setGeometry(QtCore.QRect(530, 60, 27, 22))
        self.fileToolButton2.setObjectName("fileToolButton2")
        self.buttonBox = QtWidgets.QDialogButtonBox(self.centralwidget)
        self.buttonBox.setGeometry(QtCore.QRect(340, 100, 193, 28))
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.outputLine1 = QtWidgets.QLineEdit(self.centralwidget)
        self.outputLine1.setGeometry(QtCore.QRect(160, 20, 361, 22))
        self.outputLine1.setObjectName("outputLine1")
        self.outputLine2 = QtWidgets.QLineEdit(self.centralwidget)
        self.outputLine2.setGeometry(QtCore.QRect(160, 50, 361, 22))
        self.outputLine2.setObjectName("outputLine2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 591, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PDF_2_MP3"))
        self.fileToolButton1.setText(_translate("MainWindow", "..."))
        self.fileLabel.setText(_translate("MainWindow", "FILE LOCATION :"))
        self.saveLabel.setText(_translate("MainWindow", "SAVE LOCATION :"))
        self.fileToolButton2.setText(_translate("MainWindow", "..."))
        # conecting  the button to the clicked signal
        self.fileToolButton1.clicked.connect(self.fileLocation)
        self.fileToolButton2.clicked.connect(self.saveLocation)

        self.buttonBox.accepted.connect(self.call)
        self.buttonBox.rejected.connect(self.exit)


    def fileLocation(self):
        self.file = QFileDialog.getOpenFileName()[0]
        self.outputLine1.setText(self.file)

    def saveLocation(self):
        self.save = QFileDialog.getSaveFileName()[0]
        self.outputLine2.setText(self.save+".mp3")

    def call(self):
        p2a(self.file, self.save)
        sys.exit()

    def exit(self):
        sys.exit()

    def test(self):
        """
        this file is only for test pourpouses
        """
        # sys.exit()
        print("test")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
