from PyQt5 import QtWidgets, QtGui, QtCore

from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import QCoreApplication


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        # Create a button to open the file dialog

        self.load_button = QtWidgets.QPushButton("Load")
        self.setCentralWidget(self.load_button)
        self.load_button.clicked.connect(self.on_load_clicked)
        self.load_button.setFixedSize(100, 50)
        self.setLayout(QtWidgets.QVBoxLayout())
        self.load_button.setFont(QtGui.QFont("Times", 20))

        self.load_button.setStyleSheet(
            "background-color: #00FF00 radius: 10px")

        # Set the central widget of the window
        self.setCentralWidget(self.load_button)

    def on_load_clicked(self):
        # Open the file dialog and get the selected file path
        file_path, _ = QtWidgets.QFileDialog.getOpenFileName()

        print(file_path)

        # Do something with the file (e.g. load it into the program)
        # ...

# Create the main window and show it


if __name__ == '__main__':
    # Create a pool of workers to download videos in parallel
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
