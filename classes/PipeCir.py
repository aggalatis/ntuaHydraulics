import sys
import math
from classes.Helpers import *
from PyQt5.QtWidgets import *


class PipeCir:
    def __init__(self, pipe_calculation_type, pipe_diameter, pipe_supply, pipe_depth, pipe_manning, pipe_slope):
        self.pipe_calculation_type = pipe_calculation_type
        self.pipe_diameter = pipe_diameter
        self.pipe_radius = pipe_diameter / 2
        self.pipe_depth = pipe_depth
        self.pipe_supply = pipe_supply
        self.pipe_manning = pipe_manning
        self.pipe_slope = pipe_slope
        self.pipe_velocity = 0

    def save_to_file(self):
        file_name = QFileDialog.getSaveFileName(None, "Επιλογή σημείου αποθήκευσης", "", "Hyd Files (*.hyd)")
        try:
            file_str = "pipe_calculation_type: " + self.pipe_calculation_type + "\n"
            file_str += "pipe_type: " + "Κυκλική" + "\n"
            file_str += "pipe_diameter: " + str(self.pipe_diameter) + "\n"
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
        if self.pipe_depth > self.pipe_diameter:
            Helpers.validation_error("Η τιμή του βάθους ροής δεν γίνεται να υπερβαίνει τη διάμετρο του αγωγού.")
            return
        small_radius = self.pipe_radius - self.pipe_depth
        cos_a = small_radius / self.pipe_radius
        my_angle = math.acos(cos_a) * 2
        wet_perimeter = self.pipe_radius * my_angle
        disc_area = self.pipe_radius ** 2 * my_angle / 2
        triangle_base = math.sqrt(self.pipe_radius ** 2 - (self.pipe_radius - self.pipe_depth) ** 2)
        wet_area = disc_area - triangle_base * (self.pipe_radius - self.pipe_depth)
        rh = wet_area / wet_perimeter
        pipe_velocity = (1 / self.pipe_manning) * rh ** (2 / 3) * math.sqrt(self.pipe_slope)
        pipe_supply = pipe_velocity * wet_area
        self.pipe_supply = pipe_supply
        self.pipe_velocity = pipe_velocity
        Helpers.result_message(self.pipe_supply, self.pipe_depth, self.pipe_velocity)

    def calc_depth(self):
        st_param = (self.pipe_supply * self.pipe_manning / math.sqrt(self.pipe_slope)) ** 3 * self.pipe_radius ** 2 / (self.pipe_diameter ** 2 / 8) ** 5
        my_result = 0
        my_angle = 0
        while round(my_result, 3) != round(st_param, 3):
            my_angle += 0.00001
            if round(my_angle) > math.pi * 2:
                Helpers.validation_error("Αδυναμία επίλυσης, το βάθος ροής υπερβαίνει την διάμετρο του αγωγού.")
                return
            my_result = (my_angle - math.sin(my_angle)) ** 5 / my_angle ** 2
        wet_area = self.pipe_diameter ** 2 * (my_angle - math.sin(my_angle)) / 8
        pipe_velocity = self.pipe_supply / wet_area
        pipe_depth = self.pipe_radius * (1 - math.cos(my_angle / 2))

        self.pipe_depth = pipe_depth
        self.pipe_velocity = pipe_velocity
        Helpers.result_message(self.pipe_supply, self.pipe_depth, self.pipe_velocity)


