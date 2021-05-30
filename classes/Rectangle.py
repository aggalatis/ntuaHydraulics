import sys
from classes.Helpers import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class Rectangle(QWidget):
    def __init__(self, supply, depth, velocity, width):
        super().__init__()
        self.supply = supply
        self.depth = depth
        self.velocity = velocity
        self.width = width
        self.setWindowTitle("Rectangle Results")
        self.setWindowIcon(QIcon("images/main-icon.png"))
        window_width = 300 + width * 200
        window_height = 50 + depth * 130
        self.setFixedSize(window_width, window_height)
        layout = QVBoxLayout()
        self.width_label = QLabel("Πλάτος διατομής:" + str(round(width, 3)) + " (m)")
        self.supply_label = QLabel("Παροχή:" + str(round(supply, 3)) + " (m³/s)")
        self.depth_label = QLabel("Βάθος ροής:" + str(round(depth, 3)) + " (m)")
        self.velocity_label = QLabel("Ταχύτητα ροής:" + str(round(velocity, 3)) + " (m/s)")
        self.width_label.setFont(Helpers.get_bold_font())
        self.supply_label.setFont(Helpers.get_bold_font())
        self.depth_label.setFont(Helpers.get_bold_font())
        self.velocity_label.setFont(Helpers.get_bold_font())
        layout.addWidget(self.width_label)
        layout.addWidget(self.supply_label)
        layout.addWidget(self.depth_label)
        layout.addWidget(self.velocity_label)
        self.setLayout(layout)
        global rec_window
        rec_window = self
        rec_window.show()

    def paintEvent(self, e):

        try:
            painter = QPainter(self)
            painter.setPen(QPen(Qt.black, 8))
            painter.drawRect(300, 10, self.width * 100, self.depth * 130)
            distance_from_top = round(10 + 30 * self.depth, 0)
            painter.setPen(QPen(Qt.blue, 6))
            painter.drawLine(300, distance_from_top, 300 + self.width * 100,  distance_from_top)
        except:
            e = sys.exc_info()
            print(str(e))

