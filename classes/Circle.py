import sys
import math
from classes.Helpers import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class Circle(QWidget):
    def __init__(self, supply, depth, velocity, diameter):
        super().__init__()
        try:
            self.supply = supply
            self.depth = depth
            self.velocity = velocity
            self.diameter = diameter

            self.setWindowTitle("Circle Results")
            self.setWindowIcon(QIcon("images/main-icon.png"))

            window_width = 300 + diameter * 200
            window_height = diameter * 200
            self.setFixedSize(window_width, window_height)
            layout = QVBoxLayout()

            self.diameter_label = QLabel("Διάμετρος διατομής:" + str(round(diameter, 3)) + " (m)")
            self.supply_label = QLabel("Παροχή:" + str(round(supply, 3)) + " (m³/s)")
            self.depth_label = QLabel("Βάθος ροής:" + str(round(depth, 3)) + " (m)")
            self.velocity_label = QLabel("Ταχύτητα ροής:" + str(round(velocity, 3)) + " (m/s)")

            self.diameter_label.setFont(Helpers.get_bold_font())
            self.supply_label.setFont(Helpers.get_bold_font())
            self.depth_label.setFont(Helpers.get_bold_font())
            self.velocity_label.setFont(Helpers.get_bold_font())

            layout.addWidget(self.diameter_label)
            layout.addWidget(self.supply_label)
            layout.addWidget(self.depth_label)
            layout.addWidget(self.velocity_label)
            self.setLayout(layout)

            global cir_window
            cir_window = self
            cir_window.show()
        except:
            e = sys.exc_info()
            print(str(e))

    def paintEvent(self, e):
        try:
            painter = QPainter(self)
            painter.setPen(QPen(Qt.black, 8))
            my_diameter = self.diameter * 100
            my_radius = my_diameter / 2
            my_depth = self.depth * 100
            starting_point_x = my_diameter + 200
            starting_point_y = my_diameter * 0.8
            painter.drawEllipse(starting_point_x, starting_point_y, my_diameter, my_diameter)
            distance_y = round(my_depth - my_radius, 0)
            distance_x = math.sqrt((my_radius ** 2 - (my_depth - my_radius) ** 2))
            painter.setPen(QPen(Qt.blue, 8))
            painter.drawLine(starting_point_x + my_radius - distance_x, starting_point_y + my_radius - distance_y, starting_point_x + my_radius + distance_x, starting_point_y + my_radius - distance_y)

        except:
            e = sys.exc_info()
            print(str(e))

