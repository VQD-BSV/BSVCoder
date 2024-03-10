import sys, time
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from Sc import Ui_MainWindow

class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self.main_win)

        # them item
        self.uic.listWidget.addItem("Item_ok")
        self.uic.b_add.clicked.connect(self.addItem_list)


    def addItem_list(self):
        self.uic.listWidget.addItem(self.uic.lineEdit.text()) #self.uic.lineEdit.text() lay gia tri text

    def show(self):
        # command to run
        self.main_win.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())