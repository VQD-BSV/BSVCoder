import sys, time
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from Sc import Ui_MainWindow

class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self.main_win)

        self.uic.nut.clicked.connect(self.test)

    def test(self):
        print("Xử lí")
        for i in range(1, 101):

            time.sleep(0.2)
            self.uic.progressBar.setValue(i)

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