# test123
from PyQt5.QtWidgets import QAbstractScrollArea, QTableWidget, QTableWidgetItem, QApplication, QLabel, QLineEdit, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QMessageBox
import requests
import aiohttp
import asyncio
from PyQt5 import QtCore


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
        self.table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.table.setColumnCount(6)

        for row in range(len(self.users)):
            for col in range(6):
                if col == 0:
                    self.table.setItem(
                        row, col, QTableWidgetItem(str(self.users[row]["id"])))
                elif col == 1:
                    self.table.setItem(
                        row, col, QTableWidgetItem(self.users[row]["username"]))
                elif col == 2:
                    self.table.setItem(
                        row, col, QTableWidgetItem(self.users[row]["name"]))
                elif col == 3:
                    self.table.setItem(
                        row, col, QTableWidgetItem(self.users[row]["email"]))
                elif col == 4:
                    self.table.setItem(
                        row, col, QTableWidgetItem("{},{}".format(self.users[row]["address"]["street"], self.users[row]["address"]["city"])))
                else:
                    self.table.setItem(row, col, QTableWidgetItem(
                        self.users[row]["phone"]))

        self.table.setHorizontalHeaderLabels(
            ["id", "username", "name", "email", "adrress", "phone"])

    def setWidget(self):
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.table)
        self.layout.addWidget(self.lineEdit)
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.resultInput)

        self.widget = QWidget()
        self.widget.setLayout(self.layout)

    def showName(self):
        dataTables = self.table.findItems(
            self.lineEdit.text().title(), QtCore.Qt.MatchExactly)

        if dataTables:
            results = '\n'.join('Congratulations Data ! %s found in row %d coloumn %d' % (
                item.text(), item.row() + 1, item.column() + 1)for item in dataTables)
            # all_data = list(map(lambda x: datas in x, self.data))
            # print(all_data)
        else:
            results = 'Found Nothing'

        QMessageBox.information(self, 'Search Results', results)


if __name__ == "__main__":
    app = QApplication([])
    window = MyApp()
    window.show()
    app.exec_()
