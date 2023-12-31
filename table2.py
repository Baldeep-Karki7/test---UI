# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem
from second_window_3 import Ui_Second_Window


class Ui_MainWindow(object):
    voter_id = "abcd"
    voters_who_have_already_voted = []
    candidate_selected_by_voter = ""
    list_of_candidates = []
    row_selected = 0
    column_selected = 0
    no_of_votes = 0

    def __init__(self):
        super().__init__()

    # sets value to the variable list_of_candidates

    def get_candidate_list(self, candidate_list):
        self.list_of_candidates = candidate_list

    # opens the second window
    def open_window(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Second_Window()
        self.ui.setupUi(self.window)

        # constructing rows for new window

        self.ui.tableWidget.setRowCount(len(candidate_list))

        # adding the candidates' names in second window
        col = 0
        for i in range(0, len(candidate_list)):
            item = QtWidgets.QTableWidgetItem(candidate_list[i])
            self.ui.tableWidget.setItem(i, col, item)

        # adding the vote to Votes in second window

        col = 1
        row = self.row_selected
        self.no_of_votes += 1
        item = QtWidgets.QTableWidgetItem(self.no_of_votes)
        self.ui.tableWidget.setItem(int(row), int(col), item)
        self.window.show()

    def setupUi(self, MainWindow, candidate_list):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(685, 534)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(100, 110, 441, 291))
        self.tableWidget.setEditTriggers(
            QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setRowCount(len(candidate_list))

        # table widget items

        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        self.tableWidget.verticalHeader().setVisible(False)

        # putting the candidates from list in table
        row = 0
        for i in range(0, len(candidate_list)):
            col = 0

            item = QtWidgets.QTableWidgetItem(candidate_list[i])
            self.tableWidget.setItem(row, col, item)
            row += 1

        # horizontal and vertical header default size
        self.tableWidget.horizontalHeader().setDefaultSectionSize(435)
        self.tableWidget.verticalHeader().setDefaultSectionSize(40)

        # finding which row is sleected
        self.tableWidget.selectionModel().selectionChanged.connect(
            self.on_selectionChanged)
        #####

        # pushbutton
        self.pushButton = QtWidgets.QPushButton(
            self.centralwidget, clicked=lambda: self.vote())

        self.pushButton.setGeometry(QtCore.QRect(250, 420, 100, 32))
        self.pushButton.setObjectName("pushButton")

        # pushbutton clicked

###
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(120, 30, 311, 23))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        # label
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.voter_id_line_edit = QtWidgets.QLineEdit(self.widget)
        self.voter_id_line_edit.setObjectName("voter_id_line_edit")
        self.horizontalLayout.addWidget(self.voter_id_line_edit)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 685, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

     # finds out which item(candidate) has been selected in qtablewidget
    def on_selectionChanged(self, selected):
        for j in selected.indexes():
            print('Selected cell location Row: {0}, Column :{1}'.format(
                j.row(), j.column()))
        self.row_selected = int(format(j.row()))
        self.column_selected = int(format(j.column()))

       # print(self.tableWidget.item(selected_row, selected_column).text())
        selected_candidate = self.tableWidget.item(
            self.row_selected, self.column_selected).text()
        print(selected_candidate)
        print(self.row_selected, self.column_selected)

        self.candidate_selected_by_voter = selected_candidate
 #####

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

        # set horizontal header to candidates
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "candidates"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)

        self.tableWidget.setSortingEnabled(__sortingEnabled)

        # set pushbutton text to vote
        self.pushButton.setText(_translate("MainWindow", "Vote"))
        self.label.setText(_translate("MainWindow", "Voter ID:"))

    def vote(self):

        if self.voter_id_line_edit.text() == "abcd" and self.voter_id not in self.voters_who_have_already_voted:
            print(self.candidate_selected_by_voter)
            # self.voters_who_have_already_voted.append(self.voter_id)
            self.open_window()
        elif self.voter_id in self.voters_who_have_already_voted:
            print("You have already voted")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    candidate_list = ["Baldeep", "Kritan",
                      "Sankalpa", "Rubin", "Prachanda"]
    ui.setupUi(MainWindow, candidate_list)
    ui.get_candidate_list(candidate_list)

    MainWindow.show()
    sys.exit(app.exec_())
