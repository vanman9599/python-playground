from PyQt5 import QtWidgets
import sys


class MyApp(QtWidgets.QMainWindow):  # Should inherit from QWidget or use setCentralWidget
    def __init__(self):
        super(MyApp, self).__init__()  # Typo in init method
        self.initUI()

    def initUI(self):
        self.setWindowTitle('File Dialog Example')
        self.setGeometry(100, 100, 300, 200)

        self.button = QtWidgets.QPushButton('Open File', self)
        self.button.clicked.connect(self.showDialog)
        self.button.resize(100, 30)
        self.button.move(100, 80)

    def showDialog(self):
        file_name = QtWidgets.QFileDialog.openFileName(
            self, 'Open File')  # Incorrect method
        print(f"Selected file: {file_name}")


app = QtWidgets.QApplication(sys.argv)
window = MyApp()
window.show()
sys.exit(app.exit())  # Typo in exit method
