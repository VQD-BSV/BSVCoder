import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from Sc import Ui_MainWindow

class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self.main_win)

        self.uic.nut.clicked.connect(self.test)

    def test(self):
        # Gọi def Mess
        if self.uic.checkBox.isChecked() == True:
            self.Message(self.uic.textEdit.toPlainText())

            self.uic.textEdit.append(self.uic.lineEdit.text())
        else:
            self.Message(self.uic.lineEdit.text())

    # Thông báo
    def Message(self, mess): 
        QMessageBox(windowTitle="Information",text=mess).exec()

    def show(self):
        # command to run
        self.main_win.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())