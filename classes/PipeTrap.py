import sys
import math
from classes.Helpers import *
from PyQt5.QtWidgets import *


class PipeTrap:
    def __init__(self, pipe_calculation_type, pipe_width, pipe_supply, pipe_depth, pipe_manning, pipe_slope, pipe_angle_left, pipe_angle_right):
        self.pipe_calculation_type = pipe_calculation_type
        self.pipe_width = pipe_width
        self.pipe_depth = pipe_depth
        self.pipe_supply = pipe_supply
        self.pipe_manning = pipe_manning
        self.pipe_slope = pipe_slope
        self.pipe_angle_left = pipe_angle_left
        self.pipe_angle_right = pipe_angle_right
        self.pipe_velocity = None

    def save_to_file(self):
        file_name = QFileDialog.getSaveFileName(None, "Επιλογή σημείου αποθήκευσης", "", "Hyd Files (*.hyd)")
        try:
            file_str = "pipe_calculation_type: " + self.pipe_calculation_type + "\n"
            file_str += "pipe_type: " + "Τραπεζοειδής" + "\n"
            file_str += "pipe_width: " + str(self.pipe_width) + "\n"
            file_str += "pipe_depth: " + str(self.pipe_depth) + "\n"
            file_str += "pipe_supply: " + str(self.pipe_supply) + "\n"
            file_str += "pipe_manning: " + str(self.pipe_manning) + "\n"
            file_str += "pipe_slope: " + str(self.pipe_slope) + "\n"
            file_str += "pipe_angle_left: " + str(self.pipe_angle_left) + "\n"
            file_str += "pipe_angle_right: " + str(self.pipe_angle_right)
            f = open(str(file_name[0]), "w+")
            f.write(file_str)
            f.close()
            Helpers.success_message("Επιτυχής αποθήκευση αρχείου.")
        except:
            e = sys.exc_info()
            print(str(e))

    def calc_supply(self):
        rad_a = math.radians(self.pipe_angle_left)
        rad_b = math.radians(self.pipe_angle_right)
        big_base = self.pipe_width + self.pipe_depth * (math.tan(rad_a) + math.tan(rad_b))
        area = (self.pipe_width + big_base) * self.pipe_depth / 2
        perimeter = self.pipe_width + self.pipe_depth * (1 / math.cos(rad_a) + 1 / math.cos(rad_b))
        rh = area / perimeter
        velocity = (1 / self.pipe_manning) * rh ** (2 / 3) * math.sqrt(self.pipe_slope)
        supply = area * velocity
        self.pipe_supply = supply
        self.pipe_velocity = velocity
        Helpers.result_message(self.pipe_supply, self.pipe_depth, self.pipe_velocity)

    def calc_depth(self):
        st_param = (self.pipe_supply * self.pipe_manning / math.sqrt(self.pipe_slope)) ** 3
        rad_a = math.radians(self.pipe_angle_left)
        rad_b = math.radians(self.pipe_angle_right)
        my_result = 0
        pipe_height = 0.00
        while round(my_result, 3) != round(st_param, 3):
            pipe_height += 0.000001
            big_base = self.pipe_width + pipe_height * (math.tan(rad_a) + math.tan(rad_b))
            numerator = ((self.pipe_width + big_base) * pipe_height / 2) ** 5
            denominator = (self.pipe_width + pipe_height * (1 / math.cos(rad_a) + 1 / math.cos(rad_b))) ** 2
            my_result = numerator / denominator
        self.pipe_depth = pipe_height
        area = (self.pipe_width + big_base) * self.pipe_depth / 2
        self.pipe_velocity = self.pipe_supply / area
        Helpers.result_message(self.pipe_supply, self.pipe_depth, self.pipe_velocity)
