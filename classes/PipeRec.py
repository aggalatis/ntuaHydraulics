import sys
import math
from classes.Helpers import *
from classes.Rectangle import *
from PyQt5.QtWidgets import *


class PipeRec:
    def __init__(self, pipe_calculation_type, pipe_width, pipe_supply, pipe_depth, pipe_manning, pipe_slope):
        self.pipe_width = pipe_width
        self.pipe_depth = pipe_depth
        self.pipe_supply = pipe_supply
        self.pipe_manning = pipe_manning
        self.pipe_slope = pipe_slope
        self.pipe_calculation_type = pipe_calculation_type
        self.pipe_velocity = 0
        self.rec_window = None

    def save_to_file(self):
        file_name = QFileDialog.getSaveFileName(None, "Επιλογή σημείου αποθήκευσης", "", "Hyd Files (*.hyd)")
        try:
            file_str = "pipe_calculation_type: " + self.pipe_calculation_type + "\n"
            file_str += "pipe_type: " + "Ορθογωνική" + "\n"
            file_str += "pipe_width: " + str(self.pipe_width) + "\n"
            file_str += "pipe_depth: " + str(self.pipe_depth) + "\n"
            file_str += "pipe_supply: " + str(self.pipe_supply) + "\n"
            file_str += "pipe_manning: " + str(self.pipe_manning) + "\n"
            file_str += "pipe_slope: " + str(self.pipe_slope)
            f = open(str(file_name[0]), "w+")
            f.write(file_str)
            f.close()
            Helpers.success_message("Επιτυχής αποθήκευση αρχείου.")
        except:
            e = sys.exc_info()
            print(str(e))

    def calc_supply(self):
        area = self.pipe_depth * self.pipe_width
        perimeter = 2 * self.pipe_depth + self.pipe_width
        rh = area / perimeter
        speed = (1 / self.pipe_manning) * rh ** (2/3) * math.sqrt(self.pipe_slope)
        supply = speed * area
        self.pipe_supply = supply
        self.pipe_velocity = speed
        Rectangle(self.pipe_supply, self.pipe_depth, self.pipe_velocity, self.pipe_width)

    def calc_depth(self):
        my_result = 0
        pipe_height = 0.00
        while round(my_result, 2) != round(self.pipe_supply, 2):
            pipe_height += 0.000001
            area = pipe_height * self.pipe_width
            perimeter = 2 * pipe_height + self.pipe_width
            rh = area / perimeter
            manning_division = 1 / self.pipe_manning
            my_result = manning_division * rh ** (2/3) * math.sqrt(self.pipe_slope) * area
        self.pipe_depth = pipe_height
        self.pipe_velocity = (1 / self.pipe_manning) * rh ** (2/3) * math.sqrt(self.pipe_slope)
        Rectangle(self.pipe_supply, self.pipe_depth, self.pipe_velocity, self.pipe_width)

    def create_drawing(self):
        print(self.pipe_width)
