from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMessageBox
import PyQt5.QtGui as qtg
import sys


class MyWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 200, 300, 300)
        self.setWindowTitle("Planet Distance Calculator")
        self.setLayout(QtWidgets.QHBoxLayout())  # Horizontal layout
        self.setup_window()
        self.show()

    def setup_questions(self, questions):
        planet_distance_list = [["Mercury", 0], ["Venus", 1], ['Earth', 2], ["Mars", 3], ["Jupiter", 4], ]
        questions.setText('What planet do you want calculate distance?:')
        questions.setDetailedText("Enter Planet Here")

        questions.setIcon(QMessageBox.Information)
        bonus_pluto_question = ["Of course! Show it on the list!",
                                "No, its a dwarf planet!",
                                "I'm too young to remember Pluto!"]

        x = questions.exec_()

    def button_clicked(self):
        questions_box = QMessageBox()
        questions_box.setWindowTitle("Planet Distance Questions")

        self.setup_questions(questions_box)

    def setup_window(self):
        welcome_label = QtWidgets.QLabel("Welcome!")
        welcome_label.setFont(qtg.QFont("Helvetica", 18))
        self.layout().addWidget(welcome_label)

        entry_box = QtWidgets.QLineEdit()
        entry_box.setObjectName("Entry_Planet_Field")
        entry_box.setText("Enter Planet Name")
        self.layout().addWidget(entry_box)

def main():
    app = QApplication(sys.argv)
    win = MyWindow()

    sys.exit(app.exec_())


main()
