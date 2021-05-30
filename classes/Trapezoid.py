import sys
import math
from classes.Helpers import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class Trapezoid(QWidget):
    def __init__(self, supply, depth, velocity, left_angle, right_angle, width):
        super().__init__()
        self.supply = supply
        self.depth = depth
        self.velocity = velocity
        self.width = width
        self.left_angle = left_angle
        self.right_angle = right_angle
        self.setWindowTitle("Trapezoid Results")
        self.setWindowIcon(QIcon("images/main-icon.png"))
        window_width = 300 + width * 200
        window_height = 500 + self.depth * 300
        self.setFixedSize(window_width, window_height)
        layout = QVBoxLayout()
        self.width_label = QLabel("Πλάτος διατομής:" + str(round(width, 3)) + " (m)")
        self.left_angle_label = QLabel("Αριστερή γωνία:" + str(left_angle) + " (°)")
        self.right_angle_label = QLabel("Δεξιά γωνία διατομής:" + str(right_angle) + " (°)")
        self.supply_label = QLabel("Παροχή:" + str(round(supply, 3)) + " (m³/s)")
        self.depth_label = QLabel("Βάθος ροής:" + str(round(depth, 3)) + " (m)")
        self.velocity_label = QLabel("Ταχύτητα ροής:" + str(round(velocity, 3)) + " (m/s)")
        self.width_label.setFont(Helpers.get_bold_font())
        self.left_angle_label.setFont(Helpers.get_bold_font())
        self.right_angle_label.setFont(Helpers.get_bold_font())
        self.supply_label.setFont(Helpers.get_bold_font())
        self.depth_label.setFont(Helpers.get_bold_font())
        self.velocity_label.setFont(Helpers.get_bold_font())
        layout.addWidget(self.width_label)
        layout.addWidget(self.left_angle_label)
        layout.addWidget(self.right_angle_label)
        layout.addWidget(self.supply_label)
        layout.addWidget(self.depth_label)
        layout.addWidget(self.velocity_label)
        self.setLayout(layout)
        global trap_window
        trap_window = self
        trap_window.show()

    def paintEvent(self, e):
        try:
            painter = QPainter(self)
            painter.setPen(QPen(Qt.black, 8))
            starting_point_x = 300
            starting_point_y = 200 + round(self.depth * 100, 0)
            painter.drawLine(starting_point_x, starting_point_y, starting_point_x + self.width * 100, starting_point_y)
            base_distance = self.depth * 130
            rad_l = math.radians(self.left_angle)
            rad_r = math.radians(self.right_angle)
            left_point_x = starting_point_x - base_distance / math.tan(rad_l)
            right_point_x = starting_point_x + self.width * 100 + base_distance / math.tan(rad_r)
            painter.drawLine(300, starting_point_y, left_point_x,
                             starting_point_y - base_distance)
            painter.drawLine(starting_point_x + self.width * 100, starting_point_y, right_point_x, starting_point_y - base_distance)

            water_distance = self.depth * 100
            ending_point_y = starting_point_y - water_distance
            left_point_x = starting_point_x - water_distance / math.tan(rad_l)
            right_point_x = starting_point_x + self.width * 100 + water_distance / math.tan(rad_r)
            painter.setPen(QPen(Qt.blue, 8))
            painter.drawLine(left_point_x, ending_point_y, right_point_x,
                             ending_point_y)

        except:
            e = sys.exc_info()
            print(str(e))

