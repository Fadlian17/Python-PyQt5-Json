# test123
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QApplication, QLabel, QLineEdit, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QMessageBox
import requests


class Fetch():
    def fetchUser(self):
        self.data = requests.get(
            "https://jsonplaceholder.typicode.com/users").json()
        return self.data


class MyApp(QMainWindow):
    def __init__(self):
        super(MyApp, self).__init__()
        self.users = Fetch().fetchUser()
        self.createTable()
        self.mainUI()
        self.setWidget()
        self.setCentralWidget(self.widget)
        self.setWindowTitle("Pyqt Json")

    def mainUI(self):
        # line text
        self.lineEdit = QLineEdit()
        self.lineEdit.setPlaceholderText("Type your name here ...")
        # push button
        self.button = QPushButton("enter")
        # signal slots pushButton
        self.button.clicked.connect(self.showName)
        # signal slots LineEdit
        self.lineEdit.returnPressed.connect(self.showName)
        # label result
        self.resultInput = QLabel()
        # message Box
        self.message = QMessageBox()

    # tableWidget
    def createTable(self):
        self.table = QTableWidget()
        self.table.setRowCount(len(self.users))
        self.table.setColumnCount(5)

        # self.table.setItem(0,0,QTableWidgetItem("name"))
        # self.table.setItem(0,1,QTableWidgetItem("name"))
        # self.table.setItem(1,0,QTableWidgetItem("name"))
        # self.table.setItem(1,1,QTableWidgetItem("name"))
        # self.table.setItem(2,0,QTableWidgetItem("name"))
        # self.table.setItem(2,1,QTableWidgetItem("name"))

        for row in range(len(self.users)):
            for col in range(5):
                if col == 0:
                    self.table.setItem(
                        row, col, QTableWidgetItem(self.users[row]["name"]))
                elif col == 1:
                    self.table.setItem(
                        row, col, QTableWidgetItem(self.users[row]["username"]))
                elif col == 2:
                    self.table.setItem(
                        row, col, QTableWidgetItem(self.users[row]["email"]))
                elif col == 3:
                    self.table.setItem(
                        row, col, QTableWidgetItem(self.users[row]["address"]["street"]))
                else:
                    self.table.setItem(row, col, QTableWidgetItem(
                        self.users[row]["address"]["city"]))

        self.table.setHorizontalHeaderLabels(
            ["name", "username", "email", "address", "address"])

    def setWidget(self):
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.table)
        self.layout.addWidget(self.lineEdit)
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.resultInput)

        self.widget = QWidget()
        self.widget.setLayout(self.layout)

    def showName(self):
        name = self.lineEdit.text()
        username = self.lineEdit.text()
        self.resultInput.setText(name)
        self.resultInput.setText(username)
        # self.message.accepted()
        QMessageBox.information(self, "Result", f"{name}{username} found!")
        print(name, username)


if __name__ == "__main__":
    app = QApplication([])
    window = MyApp()
    window.show()
    app.exec_()
