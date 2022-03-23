from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
import PyQt5.QtGui as qtg
import sys

"""
    This takes input regarding one of the planets from our solar system and 
    displays how far all the other plants are from it. 
"""

__program_name__ = "Planet Distance Calculator"
__author__ = "Alex Ocegueda"
__version__ = "1.0"
__github__ = "https://github.com/AlexOcegueda/Python_Assignments/planet_distance_calculator"


class MyWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 200, 200, 200)
        self.setWindowTitle("Planet Distance Calculator")
        self.setLayout(QtWidgets.QVBoxLayout())  # Vertical layout
        self.setup_window()
        self.show()

    def setup_window(self):
        """

        Displays all text on screen including the submit button which is used to
        display the results.

        """
        welcome_label = QtWidgets.QLabel("Planet Distance Calculator")
        welcome_label.setFont(qtg.QFont("Helvetica", 20))
        welcome_label.move(200, 100)
        self.layout().addWidget(welcome_label)

        entry_box = QtWidgets.QLineEdit()
        entry_box.setObjectName("Entry_Planet_Field")
        entry_box.setText("")
        self.layout().addWidget(entry_box)

        done_btn = QtWidgets.QPushButton("Submit", clicked=lambda: display_results())
        self.layout().addWidget(done_btn)

        self.show()

        def display_results():
            """

            Adds labels to screen which calculate the distance between the user's chosen
            planet and the rest of the solar system.

            """

            # storing the user's input
            chosen_planet = entry_box.text()

            planet_distance_list = [["Mercury", 46], ["Venus", 107], ["Earth", 147], ["Mars", 205],
                                    ["Jupiter", 741], ["Saturn", 1350], ["Uranus", 2750], ["Neptune", 4450]]

            # need to store distance of chosen planet for distance between
            for planet in planet_distance_list:
                if chosen_planet == planet[0]:
                    chosen_planet_distance = planet[1]
                else:
                    continue

            # unpacks planets and calculates distance between
            for planet in planet_distance_list:
                planet_name = planet[0]
                planet_distance = planet[1]

                if chosen_planet == planet_name:
                    continue
                else:
                    distance_between = abs(planet_distance - chosen_planet_distance)
                    planet_distance_label = QtWidgets.QLabel(f"{planet_name} is {distance_between} million miles"
                                                             f"away from {chosen_planet}")
                    self.layout().addWidget(planet_distance_label)


def main():
    app = QApplication(sys.argv)
    win = MyWindow()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
