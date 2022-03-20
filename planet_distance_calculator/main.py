from PyQt5 import QtCore, QtGui, QtWidgets
import sys


class UIMainWindow(QtWidgets.QWidget):
    """
        Displays and takes in all input from user.
    """

    def setup_UI(self, MainWindow):
        MainWindow.resize(422, 255)
        self.centralwidget = QtWidgets.QWidget(MainWindow)

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(160, 130, 93, 28))

        # For displaying confirmation message along with user's info.
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(170, 40, 201, 111))

        # Keeping the text of label empty initially.
        self.label.setText("")

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Proceed"))
        self.pushButton.clicked.connect(self.takeinputs)

    def takeinputs(self):
        planet_distance_list = [["Mercury", 0], ["Venus", 1], ['Earth', 2], ["Mars", 3], ["Jupiter", 4], ]

        name, chosen_planet = QtWidgets.QInputDialog.getText(self, 'Input Dialog', 'Enter a Planet:')

        bonus_pluto_question = ["Of course! Show it on the list!",
                                "No, its a dwarf planet!",
                                "I'm too young to remember Pluto!"]

        belief_in_pluto, done4 = QtWidgets.QInputDialog.getItem(
            self, 'Input Dialog', 'Do you secretly still consider Pluto a planet?:', bonus_pluto_question)

        if chosen_planet:
            # Showing confirmation message along
            # with information provided by user.
            self.label.setText('Information stored Successfully\nName: '
                               + str(name) + '(' + ')' + '\n' +
                               '\nSelected Language: ' + str(belief_in_pluto))

            # Hide the pushbutton after inputs provided by the use.
            self.pushButton.hide()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()

    UI = UIMainWindow()  # User Interface
    UI.setup_UI(main_window)
    main_window.show()

    sys.exit(app.exec_())
